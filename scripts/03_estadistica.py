from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from src.common import PROJECT_ROOT, load_config, setup_logging

VARS = [
    "rssi_c0p", "rssi_c1p", "delta_rssi_primary",
    "snr_dl", "snr_ul", "mcs_dl", "mcs_ul",
    "dl_rate_mbps", "ul_rate_mbps"
]

PAIRS = [
    ("delta_rssi_primary", "snr_dl"),
    ("delta_rssi_primary", "snr_ul"),
    ("delta_rssi_primary", "mcs_dl"),
    ("delta_rssi_primary", "mcs_ul"),
    ("delta_rssi_primary", "dl_rate_mbps"),
    ("delta_rssi_primary", "ul_rate_mbps"),
]

def effect_label(r: float) -> str:
    a = abs(r)
    if a < 0.10:
        return "prácticamente nula"
    if a < 0.30:
        return "débil"
    if a < 0.50:
        return "moderada"
    if a < 0.70:
        return "fuerte"
    return "muy fuerte"

def correlation_rows(df: pd.DataFrame, level: str) -> list[dict]:
    rows = []
    for x, y in PAIRS:
        if x not in df.columns or y not in df.columns:
            continue
        pair = df[[x, y]].dropna()
        if len(pair) < 30:
            continue
        pr = stats.pearsonr(pair[x], pair[y])
        sr = stats.spearmanr(pair[x], pair[y])
        kt = stats.kendalltau(pair[x], pair[y])
        r = float(pr.statistic)
        n = len(pair)
        if n > 3 and abs(r) < 1:
            z = np.arctanh(r)
            se = 1 / np.sqrt(n - 3)
            ci_low, ci_high = np.tanh([z - 1.96 * se, z + 1.96 * se])
        else:
            ci_low = ci_high = np.nan

        rows.append({
            "level": level,
            "x": x,
            "y": y,
            "n": n,
            "pearson_r": r,
            "pearson_p": float(pr.pvalue),
            "pearson_ci95_low": ci_low,
            "pearson_ci95_high": ci_high,
            "r_squared": r * r,
            "spearman_rho": float(sr.statistic),
            "spearman_p": float(sr.pvalue),
            "kendall_tau": float(kt.statistic),
            "kendall_p": float(kt.pvalue),
            "effect_magnitude": effect_label(r),
        })
    return rows

def main() -> None:
    setup_logging("03_estadistica")
    cfg = load_config()

    df = pd.read_parquet(PROJECT_ROOT / "data" / "processed" / "02_dataset_canonico.parquet")

    desc = []
    for col in [c for c in VARS if c in df.columns]:
        s = pd.to_numeric(df[col], errors="coerce").dropna()
        desc.append({
            "variable": col,
            "n": len(s),
            "mean": s.mean(),
            "median": s.median(),
            "std": s.std(ddof=1),
            "min": s.min(),
            "p25": s.quantile(0.25),
            "p75": s.quantile(0.75),
            "p95": s.quantile(0.95),
            "max": s.max(),
            "missing": int(df[col].isna().sum()),
            "missing_pct": float(df[col].isna().mean() * 100),
        })

    desc_df = pd.DataFrame(desc)

    hourly_cols = [c for c in VARS if c in df.columns]
    hourly = (
        df.set_index("ts")[hourly_cols]
        .resample(cfg["hourly_frequency"])
        .median()
        .dropna(how="all")
        .reset_index()
    )

    corr_df = pd.DataFrame(
        correlation_rows(df, "timestamp")
        + correlation_rows(hourly, "hourly_median")
    )

    mcs_rows = []
    for col in ["mcs_dl", "mcs_ul"]:
        if col in df.columns:
            vc = df[col].value_counts(dropna=False).sort_index()
            for code, count in vc.items():
                mcs_rows.append({
                    "direction": col,
                    "manufacturer_mcs_code": code,
                    "count": int(count),
                    "pct": float(count / len(df) * 100),
                })
    mcs_df = pd.DataFrame(mcs_rows)

    out = PROJECT_ROOT / "outputs" / "tables"
    out.mkdir(parents=True, exist_ok=True)
    desc_df.to_csv(out / "tabla_descriptivos.csv", index=False, encoding="utf-8-sig")
    corr_df.to_csv(out / "tabla_correlaciones.csv", index=False, encoding="utf-8-sig")
    mcs_df.to_csv(out / "tabla_frecuencia_mcs.csv", index=False, encoding="utf-8-sig")
    hourly.to_parquet(PROJECT_ROOT / "data" / "processed" / "03_dataset_horario.parquet", index=False)

    print("Estadística terminada.")
    print(corr_df[["level", "x", "y", "n", "pearson_r", "spearman_rho", "effect_magnitude"]].to_string(index=False))

if __name__ == "__main__":
    main()
