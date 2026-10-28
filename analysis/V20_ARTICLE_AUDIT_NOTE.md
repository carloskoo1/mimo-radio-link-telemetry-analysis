# V20 manuscript audit note — October 27, 2026

## Scientific scope
The submitted article draft describes one rural 5.8 GHz MIMO fixed-link observational archive. It does not claim a physical causal mechanism, independently measured throughput, a calibrated receiver imbalance threshold, or external predictive validation.

## Replication evidence
The archival source contains 347,036 AP/SM-labeled records consolidated into 173,513 canonical timestamps and 164,740 valid numerical ΔRSSI values. The archived 03_dataset_horario.parquet file (SHA-256 `977d95ec7328edc5bc881c0ebd944ced044d2724a5ede8c5f8be7e43a65a981b`) provides 2,023 hourly rows, 1,989 complete analytical rows and four contiguous calendar-date segments. The reanalysis script and verified results are in `analysis/article_segment_sensitivity_v19.py` and `analysis/V19_SEGMENT_AUDIT.md`.

Figure 5 in the revised draft is an empirical histogram over 164,740 valid imbalance measurements. Figure 6 is a **frequency-weighted plot of 161,340 complete original-resolution ΔRSSI / vendor-reported DL PHY-rate pairs**, not a simulated scatter sample.

## Data availability
The public GitHub repository contains processing methods and reproducibility documentation but does **not** contain the original telemetry files or the hourly panel. Re-execution of numerical results requires permitted access to the original source or processed panel. Do not state that the data are open when they are not.

## RF semantics
`rssi_c0p` and `rssi_c1p` originate from `show rssi` on the AP, whereas `dl_rate_mbps` is based on `connectedSTADLRateMbps` from `show sta` on the AP. Historical firmware-specific equivalence of directionality has not been independently verified.

## Article authors
The research team has approved this order: Carlos Jesús Koo Labrín (principal investigator, first and corresponding author), Víctor Sánchez Cáceres, José Camilo Micha Ortiz, Enzo Aldo Bravo Burgos, Oscar Gilberto Zocón Alva, Jhon Cristhian Torres Hoyos (final author). The other five are co-investigators. Enzo teaches Quantitative Methods at Universidad Nacional de Cajamarca, is a licensed Statistician and Economist trained at Universidad Nacional de Trujillo, and collaborates on statistical evidence assessment.

## Limits before journal submission
Confirm official template compliance, correct historical firmware semantics if source proof can be obtained, permissions for source telemetry access, thesis archival identifiers, submission declarations and journal-portal ORCID status. Do not invent evidence or grant data-access rights implicitly.

**No original source data or password files are hosted here.**
