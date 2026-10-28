#!/usr/bin/env python3
"""V19 post hoc segment sensitivity of archival hourly ΔRSSI telemetry.

Usage: python article_segment_sensitivity_v19.py --input path/to/03_dataset_horario.parquet
Only aggregate statistics are emitted. No telemetry is uploaded or modified.
Does not identify a causal effect, capacity, goodput, or prospective predictor.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import pandas as pd
from scipy.stats import pearsonr, spearmanr

SHA256 = "977d95ec7328edc5bc881c0ebd944ced044d2724a5ede8c5f8be7e43a65a981b"
COMPLETE = ("delta_rssi_primary","snr_dl","snr_ul","mcs_dl","mcs_ul","dl_rate_mbps")
REQUIRED = ("ts","rssi_c0p","rssi_c1p",*COMPLETE)

def rho(df, x, y):
    return float(spearmanr(df[x],df[y]).statistic)

def analyze(path, allow_other_hash=False):
    path = Path(path)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != SHA256 and not allow_other_hash:
        raise ValueError("Unexpected input SHA-256: "+digest+"; expected "+SHA256)
    data = pd.read_parquet(path)
    if any(key not in data.columns for key in REQUIRED):
        raise ValueError("Missing field(s): "+repr([k for k in REQUIRED if k not in data]))
    z = data.dropna(subset=COMPLETE).sort_values("ts").copy()
    z["ts"] = pd.to_datetime(z["ts"])
    z["date"] = z.ts.dt.date
    dates = sorted(z["date"].unique().tolist())
    runs, previous = [], None
    for day in dates:
        if previous is None or (day-previous).days>1: runs.append([])
        runs[-1].append(day)
        previous = day
    segments = []
    for index, days in enumerate(runs, 1):
        frame = z[z.date.isin(days)]
        other = z[~z.date.isin(days)]
        segments.append({
            "segment":index,"start":str(days[0]),"end":str(days[-1]),
            "dates":len(days),"hours":len(frame),
            "spearman_delta_DL":rho(frame,"delta_rssi_primary","dl_rate_mbps"),
            "pearson_delta_DL":float(pearsonr(frame.delta_rssi_primary,frame.dl_rate_mbps).statistic),
            "spearman_delta_SNR_DL":rho(frame,"delta_rssi_primary","snr_dl"),
            "spearman_delta_SNR_UL":rho(frame,"delta_rssi_primary","snr_ul"),
            "spearman_chain0_DL":rho(frame,"rssi_c0p","dl_rate_mbps"),
            "spearman_chain1_DL":rho(frame,"rssi_c1p","dl_rate_mbps"),
            "median_delta_dB":float(frame.delta_rssi_primary.median()),
            "median_reported_DL_Mbps":float(frame.dl_rate_mbps.median()),
            "leave_one_segment_out_hours":len(other),
            "leave_one_segment_out_spearman":rho(other,"delta_rssi_primary","dl_rate_mbps")
        })
    result = {
        "data_file":path.name,"sha256":digest,"frozen_source_match":digest==SHA256,
        "source_hours":len(data),"complete_hours":len(z),"complete_dates":len(dates),
        "global_spearman_delta_DL":rho(z,"delta_rssi_primary","dl_rate_mbps"),
        "global_spearman_chain0_DL":rho(z,"rssi_c0p","dl_rate_mbps"),
        "global_spearman_chain1_DL":rho(z,"rssi_c1p","dl_rate_mbps"),
        "unique_reported_DL_rates":int(z.dl_rate_mbps.nunique()),
        "hours_reported_DL_137":int((z.dl_rate_mbps==137).sum()),
        "segments":segments,
        "inference":"Descriptive retrospective diagnostics; not causal or confirmatory."
    }
    if digest==SHA256:
        assert (len(data),len(z),len(dates),len(segments))==(2023,1989,89,4)
        assert abs(result["global_spearman_delta_DL"]-0.492585)<1e-5
    return result

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input",required=True,type=Path)
    parser.add_argument("--allow-other-hash",action="store_true")
    parser.add_argument("--output-json",type=Path)
    args=parser.parse_args()
    result=analyze(args.input,args.allow_other_hash)
    encoded=json.dumps(result,ensure_ascii=False,indent=2)
    print(encoded)
    if args.output_json:
        args.output_json.write_text(encoded+"\n",encoding="utf-8")
