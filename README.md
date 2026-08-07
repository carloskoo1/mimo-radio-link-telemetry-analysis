# Temporal Analysis of Signal Imbalance in a 5.8 GHz MIMO Radio Link

[![Scientific Pipeline Validation](https://github.com/carloskoo1/mimo-radio-link-telemetry-analysis/actions/workflows/validate.yml/badge.svg)](https://github.com/carloskoo1/mimo-radio-link-telemetry-analysis/actions/workflows/validate.yml)
[![GitHub release](https://img.shields.io/github/v/release/carloskoo1/mimo-radio-link-telemetry-analysis)](https://github.com/carloskoo1/mimo-radio-link-telemetry-analysis/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
## Overview

This repository contains the complete reproducible pipeline developed for the statistical analysis of telemetry collected from a Cambium ePMP 400C point-to-point MIMO radio link operating in the 5.8 GHz band.

The repository accompanies the master's thesis and provides a reproducible workflow for importing, preprocessing, analyzing and visualizing telemetry collected under real operating conditions.

## Dataset

- 90 CSV files
- 347,036 raw records
- 173,513 canonical observations
- 161,340 valid observations
- 1,989 hourly medians

## Pipeline

01_importar.py

?

02_preprocesar.py

?

03_estadistica.py

?

04_figuras.py

?

05_reportes.py

## Execute

python run_pipeline.py

## Author

Carlos Jesús Koo Labrín

National University of Cajamarca

## Reproducing the analysis

### Windows

    reproduce.bat

### Linux

    chmod +x reproduce.sh
    ./reproduce.sh

### Conda

    conda env create -f environment.yml
    conda activate mimo-radio-link-analysis
    python run_pipeline.py

## Continuous Integration

Every push and pull request is automatically validated using GitHub Actions.

The workflow checks:

- Python syntax.
- Dependency installation.
- Repository structure.
- Scientific reproducibility files.

## Software versioning

Stable research releases follow semantic versioning.

Current scientific baseline:

    v1.0.0

See `CHANGELOG.md` for release history.

