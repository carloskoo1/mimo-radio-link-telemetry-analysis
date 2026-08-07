from __future__ import annotations

import numpy as np
import pandas as pd

from src.common import PROJECT_ROOT, load_config, parse_rate_mbps, setup_logging

NUMERIC = [
    "mcs_dl", "mcs_ul", "snr_dl", "snr_ul",
    "rssi_c0p", "rssi_c0e", "rssi_c1p", "rssi_c1e",
    "sta_dl_rssi", "sta_ul_rssi"
]

def main() -> None:
    setup_logging("02_preprocesar")
    cfg = load_config()

    raw = pd.read_parquet(PROJECT_ROOT / "data" / "processed" / "01_raw_importado.parquet")

    raw["ts"] = pd.to_datetime(raw["ts"], errors="coerce")
    raw["role"] = raw["role"].astype("string").str.upper().str.strip()

    for col in NUMERIC:
        if col in raw.columns:
            raw[col] = pd.to_numeric(raw[col], errors="coerce")

    if "dl_rate" in raw.columns:
        raw["dl_rate_mbps"] = raw["dl_rate"].map(parse_rate_mbps)

    if "ul_rate" in raw.columns:
        raw["ul_rate_mbps"] = raw["ul_rate"].map(parse_rate_mbps)

    rssi_min, rssi_max = cfg["rssi_valid_range_dbm"]
    for col in ["rssi_c0p", "rssi_c0e", "rssi_c1p", "rssi_c1e", "sta_dl_rssi", "sta_ul_rssi"]:
        if col in raw.columns:
            raw.loc[~raw[col].between(rssi_min, rssi_max), col] = np.nan

    snr_min, snr_max = cfg["snr_valid_range_db"]
    for col in ["snr_dl", "snr_ul"]:
        if col in raw.columns:
            raw.loc[~raw[col].between(snr_min, snr_max), col] = np.nan

    raw = raw.dropna(subset=["ts"]).sort_values(["ts", "role"]).reset_index(drop=True)

    canonical_role = cfg["canonical_role"]
    fallback_role = cfg["fallback_role"]

    ap = raw[raw["role"] == canonical_role].drop_duplicates("ts", keep="last")
    sm = raw[raw["role"] == fallback_role].drop_duplicates("ts", keep="last")

    all_ts = pd.DataFrame({"ts": pd.Index(raw["ts"].unique()).sort_values()})
    canonical = all_ts.merge(ap, on="ts", how="left", suffixes=("", "_ap"))

    fallback = sm.set_index("ts")
    for col in raw.columns:
        if col == "ts":
            continue
        if col not in canonical.columns:
            canonical[col] = np.nan
        if col in fallback.columns:
            canonical[col] = canonical[col].combine_first(canonical["ts"].map(fallback[col]))

    canonical["selected_role"] = np.where(canonical["role"].notna(), canonical["role"], fallback_role)
    canonical["has_ap"] = canonical["ts"].isin(set(ap["ts"]))
    canonical["has_sm"] = canonical["ts"].isin(set(sm["ts"]))

    if {"rssi_c0p", "rssi_c1p"}.issubset(canonical.columns):
        canonical["delta_rssi_primary_signed"] = canonical["rssi_c0p"] - canonical["rssi_c1p"]
        canonical["delta_rssi_primary"] = canonical["delta_rssi_primary_signed"].abs()

    if {"rssi_c0e", "rssi_c1e"}.issubset(canonical.columns):
        canonical["delta_rssi_extension_signed"] = canonical["rssi_c0e"] - canonical["rssi_c1e"]
        canonical["delta_rssi_extension"] = canonical["delta_rssi_extension_signed"].abs()

    canonical["date"] = canonical["ts"].dt.date
    canonical["hour"] = canonical["ts"].dt.hour
    canonical["weekday"] = canonical["ts"].dt.dayofweek

    out = PROJECT_ROOT / "data" / "processed"
    canonical.to_parquet(out / "02_dataset_canonico.parquet", index=False)
    canonical.to_csv(out / "02_dataset_canonico.csv", index=False, encoding="utf-8-sig")

    quality = pd.DataFrame([
        {"indicator": "raw_rows", "value": len(raw)},
        {"indicator": "canonical_rows", "value": len(canonical)},
        {"indicator": "ap_rows", "value": len(ap)},
        {"indicator": "sm_rows", "value": len(sm)},
        {"indicator": "timestamps_with_ap", "value": int(canonical["has_ap"].sum())},
        {"indicator": "timestamps_with_sm", "value": int(canonical["has_sm"].sum())},
        {"indicator": "valid_dl_rate", "value": int(canonical["dl_rate_mbps"].notna().sum()) if "dl_rate_mbps" in canonical else 0},
        {"indicator": "valid_ul_rate", "value": int(canonical["ul_rate_mbps"].notna().sum()) if "ul_rate_mbps" in canonical else 0},
    ])
    quality.to_csv(PROJECT_ROOT / "outputs" / "tables" / "tabla_calidad_dataset.csv", index=False, encoding="utf-8-sig")

    print(quality.to_string(index=False))
    print("Preprocesamiento terminado.")

if __name__ == "__main__":
    main()
