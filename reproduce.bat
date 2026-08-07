@echo off

echo ===============================================
echo MIMO RADIO LINK - REPRODUCIBLE PIPELINE
echo ===============================================

if not exist .venv (
    python -m venv .venv
)

call .venv\Scripts\activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

python run_pipeline.py

echo.
echo Pipeline completed.
pause
