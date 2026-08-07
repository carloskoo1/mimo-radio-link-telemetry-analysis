from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from src.common import PROJECT_ROOT, load_config, setup_logging

def main() -> None:
    setup_logging("04_figuras")
    cfg = load_config()

    df = pd.read_parquet(PROJECT_ROOT / "data" / "processed" / "02_dataset_canonico.parquet")
    out = PROJECT_ROOT / "outputs" / "figures"
    out.mkdir(parents=True, exist_ok=True)

    if {"ts", "rssi_c0p", "rssi_c1p"}.issubset(df.columns):
        h = df.set_index("ts")[["rssi_c0p", "rssi_c1p"]].resample("1h").median()
        fig, ax = plt.subplots(figsize=(10, 4.8))
        h.plot(ax=ax)
        ax.set_title("RSSI por cadena de recepción")
        ax.set_xlabel("Fecha")
        ax.set_ylabel("RSSI (dBm)")
        ax.grid(alpha=0.25)
        fig.tight_layout()
        fig.savefig(out / "fig_4_1_rssi_cadenas.png", dpi=300, bbox_inches="tight")
        plt.close(fig)

    if {"ts", "delta_rssi_primary"}.issubset(df.columns):
        h = df.set_index("ts")["delta_rssi_primary"].resample("1h").median()
        fig, ax = plt.subplots(figsize=(10, 4.8))
        h.plot(ax=ax)
        ax.set_title("Desbalance de señal ΔRSSI")
        ax.set_xlabel("Fecha")
        ax.set_ylabel("ΔRSSI (dB)")
        ax.grid(alpha=0.25)
        fig.tight_layout()
        fig.savefig(out / "fig_4_2_delta_rssi_serie.png", dpi=300, bbox_inches="tight")
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(7.2, 4.8))
        df["delta_rssi_primary"].dropna().hist(bins=40, ax=ax)
        ax.set_title("Distribución del ΔRSSI")
        ax.set_xlabel("ΔRSSI (dB)")
        ax.set_ylabel("Frecuencia")
        fig.tight_layout()
        fig.savefig(out / "fig_4_3_delta_rssi_histograma.png", dpi=300, bbox_inches="tight")
        plt.close(fig)

    targets = [
        ("snr_dl", "fig_4_4_delta_vs_snr_dl.png", "SNR DL (dB)"),
        ("mcs_dl", "fig_4_5_delta_vs_mcs_dl.png", "Código MCS DL"),
        ("dl_rate_mbps", "fig_4_6_delta_vs_tasa_dl.png", "Tasa DL (Mbps)"),
    ]

    for y, filename, ylabel in targets:
        if {"delta_rssi_primary", y}.issubset(df.columns):
            pair = df[["delta_rssi_primary", y]].dropna()
            if pair.empty:
                continue
            sample = pair.sample(
                min(cfg["plot_sample_max"], len(pair)),
                random_state=cfg["random_seed"],
            )
            fig, ax = plt.subplots(figsize=(7.2, 5.2))
            ax.scatter(sample["delta_rssi_primary"], sample[y], s=7, alpha=0.22)
            if pair["delta_rssi_primary"].nunique() > 1:
                coef = np.polyfit(pair["delta_rssi_primary"], pair[y], 1)
                xx = np.linspace(pair["delta_rssi_primary"].min(), pair["delta_rssi_primary"].max(), 100)
                ax.plot(xx, coef[0] * xx + coef[1], linewidth=2)
            ax.set_title(f"Relación entre ΔRSSI y {ylabel}")
            ax.set_xlabel("ΔRSSI (dB)")
            ax.set_ylabel(ylabel)
            ax.grid(alpha=0.2)
            fig.tight_layout()
            fig.savefig(out / filename, dpi=300, bbox_inches="tight")
            plt.close(fig)

    print("Figuras terminadas.")

if __name__ == "__main__":
    main()
