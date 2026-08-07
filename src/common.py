from __future__ import annotations

import csv
import hashlib
import json
import logging
import re
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

EXPECTED_COLUMNS = [
    "ts", "role", "ip", "f4", "f5", "f6", "f7",
    "mcs_dl", "mcs_ul", "snr_dl", "snr_ul",
    "rssi_c0p", "rssi_c0e", "rssi_c1p", "rssi_c1e",
    "dl_rate", "ul_rate", "sta_dl_rssi", "sta_ul_rssi",
    "res20", "res21", "res22", "res23", "res24"
]

ALIASES = {
    "timestamp": "ts",
    "time": "ts",
    "datetime": "ts",
    "date_time": "ts",
    "dl_mcs": "mcs_dl",
    "ul_mcs": "mcs_ul",
    "dl_snr": "snr_dl",
    "ul_snr": "snr_ul",
    "downlink_rate": "dl_rate",
    "uplink_rate": "ul_rate",
}

def load_config() -> dict:
    with (PROJECT_ROOT / "config" / "config.json").open("r", encoding="utf-8") as f:
        return json.load(f)

def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()

def detect_sep(path: Path, encoding: str) -> str | None:
    with path.open("r", encoding=encoding, errors="replace") as f:
        sample = f.read(8192)
    try:
        return csv.Sniffer().sniff(sample, delimiters=",;\t|").delimiter
    except csv.Error:
        return None

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    cols = [str(c).strip().lower().replace(" ", "_") for c in df.columns]
    df.columns = [ALIASES.get(c, c) for c in cols]
    return df.loc[:, ~df.columns.duplicated()].copy()

def read_csv_robust(path: Path) -> pd.DataFrame:
    errors = []
    for enc in ("utf-8-sig", "utf-8", "latin-1"):
        sep = detect_sep(path, enc)
        kwargs = {"filepath_or_buffer": path, "encoding": enc, "engine": "python", "sep": sep}
        try:
            df = normalize_columns(pd.read_csv(**kwargs))
            if "ts" in df.columns:
                return df
        except Exception as exc:
            errors.append(f"{enc}/header: {exc}")
        try:
            df = pd.read_csv(**kwargs, header=None)
            cols = EXPECTED_COLUMNS[:df.shape[1]]
            if df.shape[1] > len(EXPECTED_COLUMNS):
                cols += [f"extra_{i}" for i in range(df.shape[1] - len(EXPECTED_COLUMNS))]
            df.columns = cols
            return normalize_columns(df)
        except Exception as exc:
            errors.append(f"{enc}/no-header: {exc}")
    raise RuntimeError(" | ".join(errors[-6:]))

def parse_rate_mbps(value):
    if pd.isna(value):
        return np.nan
    if isinstance(value, (int, float, np.number)):
        return float(value)
    s = str(value).strip().lower().replace(",", ".")
    m = re.search(r"(-?\d+(?:\.\d+)?)\s*([kmg]?)", s)
    if not m:
        return np.nan
    num = float(m.group(1))
    unit = m.group(2)
    if unit == "g":
        return num * 1000.0
    if unit == "k":
        return num / 1000.0
    return num

def setup_logging(name: str) -> Path:
    path = PROJECT_ROOT / "logs" / f"{name}.log"
    path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[logging.FileHandler(path, encoding="utf-8"), logging.StreamHandler()],
        force=True,
    )
    return path
