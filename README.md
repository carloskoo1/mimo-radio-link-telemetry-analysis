# Pipeline V3 — Tesis Jhon Torres

Pipeline científico por etapas para analizar ΔRSSI, SNR, códigos MCS propietarios Cambium y tasa de transmisión.

## Diseño

El flujo se divide en cinco etapas independientes:

1. Importación.
2. Preprocesamiento y selección canónica AP/SM.
3. Estadística descriptiva e inferencial.
4. Figuras.
5. Excel y Word.

Cada etapa genera sus propios productos y puede ejecutarse por separado.

## Instalación

```powershell
python -m venv .\.venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
& .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r .\requirements.txt
```

## Ejecución completa

```powershell
python .\run_pipeline.py
```

## Ejecución por etapa

```powershell
python .\scripts\01_importar.py
python .\scripts\02_preprocesar.py
python .\scripts\03_estadistica.py
python .\scripts\04_figuras.py
python .\scripts\05_reportes.py
```

## Criterios

- Se prioriza el rol AP por timestamp.
- Si falta AP, se utiliza SM como respaldo.
- ΔRSSI se calcula como `abs(rssi_c0p - rssi_c1p)`.
- Los MCS se conservan como códigos propietarios del equipo.
- Se calculan Pearson, Spearman y Kendall.
- Se analizan registros canónicos y medianas horarias.
- Las asociaciones no se interpretan como causalidad.
