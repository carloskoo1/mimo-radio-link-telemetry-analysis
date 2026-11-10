# Metodología de adquisición y análisis de telemetría — Jhon Torres

## Diseño y unidades

Tesis cuantitativa aplicada, observacional y longitudinal, con implementación/verificación de un producto tecnológico y análisis descriptivo-correlacional de un único radioenlace MIMO de 5,8 GHz. La unidad de observación en resolución original es una **captura canónica por marca temporal**; al agregar, cada hora válida se representa con su mediana. Las observaciones consecutivas no son enlaces independientes y presentan dependencia temporal. No se infiere causalidad.

## Técnica, fuente, instrumento y registro

- **Técnica de adquisición:** observación sistemática no participante automatizada.
- **Fuente física y digital:** radio Cambium ePMP 400C; consultas `show rssi` y `show sta` ejecutadas **desde el AP**.
- **Instrumento de registro:** esquema estructurado CSV generado por scripts Linux/Bash/SSH, con marcas temporales y campos predefinidos. No es un sensor ni una ficha manual.
- **Registro:** filas de CSV y respuestas CLI conservadas; la etiqueta AP/SM no demuestra dos interrogaciones independientes.
- **Técnica para tratamiento:** análisis documental de archivos, inspección de integridad, depuración, consolidación, cálculos estadísticos y sensibilidad temporal con Python.

La especificación explícita y el ejemplo histórico de la ficha figuran en [Ficha de observación digital](tesis/FICHA_OBSERVACION_DIGITAL.md).

## Cadena de proceso

1. Adquirir: ejecutar consultas SSH al AP y conservar respuestas y CSV diarios (recolector público disponible en `acquisition/poll_epmp_public.sh`).
2. Importar: `scripts/01_importar.py`.
3. Validar/consolidar observaciones AP/SM: `scripts/02_preprocesar.py`, una captura por marca temporal.
4. Calcular ΔRSSI: `|rssi_c0p − rssi_c1p|` sobre ambos valores numéricos primarios de la misma captura.
5. Analizar: `scripts/03_estadistica.py`; la hipótesis de asociación usa ΔRSSI frente a tasa DL reportada en capturas y medianas horarias.
6. Comunicar: `scripts/04_figuras.py`, `scripts/05_reportes.py`.

## Alcance de verificación y limitaciones

De acuerdo con la tesis: 90 CSV, 347 036 filas originales, 173 513 capturas canónicas; 21 438 campos CLI–CSV concordantes el 16/05/2026, incluidos vacíos. Dicho cotejo **no valida toda la campaña**. De 12 controles del extractor histórico, 2 fueron no conformes (mezcla potencial de estación). Esta documentación no certifica exactitud metrológica, continuidad del firmware/configuración, polarización física de las cadenas ni goodput.

La telemetría original no se publica aquí: la reproducción numérica requiere autorización sobre los datos fuente. Código, documentación y herramientas pueden auditarse públicamente. Para el software reproducible archivado se conserva el **DOI de versión v2.0.1: https://doi.org/10.5281/zenodo.21844766**; esta mejora documental en `main` no cambia ese artefacto.
