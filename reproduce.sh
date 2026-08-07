#!/usr/bin/env bash

set -e

echo "==============================================="
echo "MIMO RADIO LINK - REPRODUCIBLE PIPELINE"
echo "==============================================="

if [[ ! -d ".venv" ]]; then
    python3 -m venv .venv
fi

source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python run_pipeline.py

echo
echo "Pipeline completed."
