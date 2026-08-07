# Auditoría científica del repositorio

**Repositorio:** carloskoo1/mimo-radio-link-telemetry-analysis  
**Versión auditada:** v2.0.0  
**DOI:** 10.5281/zenodo.21844661  
**Fecha de auditoría:** 2026-08-07 18:26:42

## Resumen

- PASS: 37
- WARN: 
- FAIL: 0
- Puntuación técnica: **10 / 10**

## Resultados

| Área | Verificación | Estado | Detalle |
|---|---|---|---|
| Estructura | README | PASS | README.md |
| Estructura | Licencia | PASS | LICENSE |
| Estructura | CITATION.cff | PASS | CITATION.cff |
| Estructura | CHANGELOG | PASS | CHANGELOG.md |
| Estructura | requirements.txt | PASS | requirements.txt |
| Estructura | environment.yml | PASS | environment.yml |
| Estructura | Pipeline principal | PASS | run_pipeline.py |
| Estructura | Script reproducible Windows | PASS | reproduce.bat |
| Estructura | Script reproducible Linux | PASS | reproduce.sh |
| Estructura | GitHub Actions | PASS | .github\workflows\validate.yml |
| Estructura | scripts\01_importar.py | PASS | scripts\01_importar.py |
| Estructura | scripts\02_preprocesar.py | PASS | scripts\02_preprocesar.py |
| Estructura | scripts\03_estadistica.py | PASS | scripts\03_estadistica.py |
| Estructura | scripts\04_figuras.py | PASS | scripts\04_figuras.py |
| Estructura | scripts\05_reportes.py | PASS | scripts\05_reportes.py |
| Estructura | src\common.py | PASS | src\common.py |
| Estructura | docs\TRAZABILIDAD.md | PASS | docs\TRAZABILIDAD.md |
| Estructura | docs\METODOLOGIA.md | PASS | docs\METODOLOGIA.md |
| Estructura | docs\DICCIONARIO_VARIABLES.md | PASS | docs\DICCIONARIO_VARIABLES.md |
| Estructura | docs\REPRODUCIBILIDAD.md | PASS | docs\REPRODUCIBILIDAD.md |
| Estructura | manifests\release_v1_metadata.json | PASS | manifests\release_v1_metadata.json |
| Estructura | manifests\release_v1_sha256.csv | PASS | manifests\release_v1_sha256.csv |
| Estructura | acquisition\poll_epmp_public.sh | PASS | acquisition\poll_epmp_public.sh |
| Git | Repositorio inicializado | PASS | .git presente |
| Git | Rama principal | PASS | main |
| Git | Working tree limpio | PASS | Sin cambios pendientes |
| Git | Remote origin | PASS | https://github.com/carloskoo1/mimo-radio-link-telemetry-analysis.git |
| Git | Release científica v2.0.0 | PASS | Tag v2.0.0 encontrado |
| Python | Sintaxis del pipeline | PASS | py_compile sin errores |
| Python | Versión local | INFO |  |
| Citación | ORCID Jhon Torres | PASS | 0009-0005-1167-9930 |
| Citación | ORCID Carlos Koo | PASS | 0000-0002-0323-2961 |
| Citación | DOI Zenodo | PASS | 10.5281/zenodo.21844661 |
| Citación | Versión CFF | PASS | 2.0.0 |
| Reproducibilidad | Documento de reproducibilidad | PASS | Presente |
| Reproducibilidad | Windows reproduce | PASS | Presente |
| Reproducibilidad | Linux reproduce | PASS | Presente |
| Seguridad | Secretos evidentes | PASS | No detectados |
| Integridad | Manifiesto SHA-256 de auditoría | PASS | audit\AUDIT_SHA256.csv |
## Criterio de interpretación

- **PASS:** requisito satisfecho.
- **WARN:** no invalida el repositorio, pero conviene mejorar.
- **FAIL:** debe corregirse antes de considerar el repositorio completamente auditado.

## Alcance de reproducibilidad

El repositorio permite reproducir el flujo de procesamiento y análisis mediante los scripts y entornos proporcionados. La reproducción numérica integral de todos los resultados requiere disponer del conjunto original de telemetría utilizado en la investigación.

## DOI

https://doi.org/10.5281/zenodo.21844661

## Autores

- Jhon Cristhian Torres Hoyos — ORCID 0009-0005-1167-9930
- Carlos Jesús Koo Labrín — ORCID 0000-0002-0323-2961

