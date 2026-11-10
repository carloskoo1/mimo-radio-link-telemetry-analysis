# Ficha de observación digital estructurada — tesis Jhon Torres

**Documento de trazabilidad metodológica (10-11-2026).** Complemento descriptivo de la tesis «Implementación de un sistema automatizado de adquisición de métricas y análisis del desbalance de señal (ΔRSSI) en un radioenlace MIMO de 5,8 GHz en un entorno andino». No representa recolección nueva, prueba experimental, calibración de radio ni una ficha manual aplicada en campo. No sustituye los originales.

## Identidad de la técnica y del instrumento

- **Técnica:** observación sistemática no participante, realizada mediante consultas automatizadas de telemetría; posteriormente, análisis documental de los CSV preservados.
- **Fuente de los valores:** equipo Cambium ePMP consultado desde el punto de acceso (AP), mediante las respuestas CLI `show rssi` y `show sta`.
- **Instrumento de registro:** esquema digital estructurado con marca temporal y columnas definidas en el CSV; el programa de adquisición implementa el llenado automático. Los archivos CSV son los registros de observación.
- **Unidad de observación:** una captura canónica por marca temporal. Las filas etiquetadas AP/SM repiten campos compartidos y **no** constituyen mediciones independientes.
- **Cadencia observada:** variable; en la tesis de cierre se informa mediana de 49 s y percentil 95 de 60 s. La cadencia del archivo no garantiza continuidad.
- **Procesamiento posterior:** Python consolida, controla validez y calcula métricas derivadas. No mide directamente las magnitudes físicas.

## Campos principales de la ficha

| Campo | Fuente digital | Unidad y regla |
| --- | --- | --- |
| `ts` | Captura del recolector | ISO 8601 con zona horaria; identificador temporal |
| `role`, `ip` | Metadatos del recolector | Identificación de fila; no acreditan dos consultas independientes |
| `rssi_c0p`, `rssi_c1p` | `show rssi`, cadena 0/1, primary | dBm; conservar valor fuente, vacío si falta |
| `rssi_c0e`, `rssi_c1e` | `show rssi`, extension | Campo auxiliar; su interpretación histórica es limitada y no entra en ΔRSSI |
| `mcs_dl`, `mcs_ul` | `show sta`, códigos reportados por el fabricante | Códigos; no tratar como escala MCS física uniforme |
| `snr_dl`, `snr_ul` | `show sta` | dB; verificar estacion objetivo |
| `dl_rate` | `show sta`, `connectedSTADLRateMbps` | Tasa DL reportada; la interpretación numérica en Mbit/s no equivale a goodput |
| `sta_dl_rssi`, `sta_ul_rssi` | `show sta` | dBm; no confundir con RSSI primario de cada cadena |
| `delta_rssi_primary` | Derivado de `rssi_c0p` y `rssi_c1p` | dB; valor absoluto de la diferencia de los dos primarios válidos de una misma captura |

El recolector público incluye 24 columnas: `ts,role,ip,f4,f5,f6,f7,mcs_dl,mcs_ul,snr_dl,snr_ul,rssi_c0p,rssi_c0e,rssi_c1p,rssi_c1e,dl_rate,ul_rate,sta_dl_rssi,sta_ul_rssi,res20,res21,res22,res23,res24`. Los campos `f4`–`f7`, `ul_rate` y `res20`–`res24` no deben presentarse como indicadores físicos adicionales sin definición y validación documental. Véanse el [recolector público](../../acquisition/poll_epmp_public.sh) y el [diccionario de variables](../DICCIONARIO_VARIABLES.md).

## Ejemplo cumplimentado, transcrito de la tesis de cierre

**Origen declarado:** tesis `Tesis_Jhon_Torres_UNC_Cierre_Defensa_Final.docx`, Anexo 2, apartado «Casos de cotejo e integridad de archivos», ciclo del **16/05/2026 a las 00:06:01 UTC−05:00**. Esta transcripción no afirma un nuevo cotejo de los archivos originales durante la presente actualización.

| Atributo | Valor informado en la tesis |
| --- | --- |
| Marca temporal del ciclo CSV | 2026-05-16T00:06:01-05:00 |
| Marca temporal de `show rssi` | 2026-05-16T00:06:02-05:00 |
| Marca temporal de `show sta` | 2026-05-16T00:06:03-05:00 |
| RSSI Chain 0 primary | −80 dBm |
| RSSI Chain 1 primary | −95 dBm |
| ΔRSSI derivado | 15 dB |
| SNR DL / UL | 20 / 19 dB |
| MCS DL / UL | 104 / 103 (códigos) |
| Tasa DL reportada | 216M (interpretación numérica 216 Mbit/s) |
| RSSI agregado DL / UL | −76 / −79 dBm |
| Fuente documental del ejemplo | Anexo 2, «Casos de cotejo e integridad de archivos» |
| Estado de la fuente original | Acceso restringido; contraste directo no rehecho con motivo de esta ficha |

**Cadena de procedencia:** consulta CLI → registro diario CSV → consolidación por marca temporal → control de integridad/correspondencia → estadística y resultados por objetivo. El ejemplo se debe vincular, al disponer de los originales autorizados, a las filas y hashes del 16/05/2026, manteniendo el resultado previo de la tesis y sus exclusiones.

## Verificación y alcance

En la tesis se documentan 90 CSV, 347 036 filas crudas y 173 513 capturas canónicas. El cotejo CLI–CSV del 16/05/2026 informa **21 438 campos concordantes** en ciclos temporalmente asignables, *incluidos vacíos*. No se debe describir este total como 21 438 mediciones físicas válidas, ni extender el resultado del día a toda la campaña. Se reportan **10/12 controles conformes** del extractor histórico; los casos C08 y C09 son no conformes y se mantienen como limitaciones. La identidad exacta del extractor desplegado en cada tramo histórico, la dirección física de cada RSSI y la calibración del receptor no quedan acreditadas por esta ficha.

## Correspondencia metodológica

- **OE1 (implementación/verificación):** consultas, CSV, integridad, ejemplos y cotejo CLI–CSV.
- **OE2 (RSSI por cadena):** `rssi_c0p`, `rssi_c1p`.
- **OE3 (ΔRSSI):** `delta_rssi_primary` calculado en una captura válida.
- **OE4 (asociaciones):** emparejamiento de ΔRSSI y tasa DL reportada, con sensibilidad temporal y límites inferenciales.
- **OE5 (interpretación):** contextualización técnica, trazabilidad y limitaciones; sin atribución causal.

**Control editorial:** su incorporación al DOCX definitivo requiere incluir título y referencia cruzada desde §3.3 y el Anexo 2, más recálculo de índices y paginación. No reescribir el depositado v2.0.1 ni afirmar que los especialistas evaluaron esta ficha nueva.
