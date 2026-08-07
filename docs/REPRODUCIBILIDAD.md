# Reproducibility

The complete analysis is divided into five processing stages.

## Pipeline

1. `scripts/01_importar.py`
2. `scripts/02_preprocesar.py`
3. `scripts/03_estadistica.py`
4. `scripts/04_figuras.py`
5. `scripts/05_reportes.py`

The complete workflow can be executed with:

    python run_pipeline.py

## Expected dataset scale

| Element | Value |
|---|---:|
| Original CSV files | 90 |
| Raw records | 347,036 |
| Canonical observations | 173,513 |
| Instantaneous correlation observations | 161,340 |
| Hourly medians | 1,989 |

These values provide a reference for verifying the reproduction of the
experimental processing workflow.

## Archived release

Version:

    v2.0.1

Version-specific DOI:

    10.5281/zenodo.21844766

Concept DOI:

    10.5281/zenodo.21844660
