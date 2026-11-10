# Diccionario operativo de los campos de observación — radioenlace MIMO 5,8 GHz

**Fuente:** extractor público `acquisition/poll_epmp_public.sh`. Esta tabla documenta su salida; no presupone identidad byte a byte entre el archivo público y el extractor desplegado en cada fecha histórica.

| Nombre CSV | Papel / procedencia | Unidad e interpretación |
| --- | --- | --- |
| `ts` | Marca temporal generada por el recolector | ISO 8601 con zona horaria |
| `role` | Etiqueta de la fila AP/SM | Identificador; no supone observación autónoma |
| `ip` | Dirección referida a la etiqueta | Identificador, no métrica RF |
| `f4`, `f5`, `f6`, `f7` | Campos auxiliares del formato legado | No se atribuyen magnitudes RF sin documentación |
| `mcs_dl`, `mcs_ul` | `show sta` | Códigos MCS propietarios reportados, **no** índices IEEE homogéneos |
| `snr_dl`, `snr_ul` | `show sta` | dB |
| `rssi_c0p`, `rssi_c1p` | `show rssi`, primary, Chain 0/1 | dBm; base de ΔRSSI |
| `rssi_c0e`, `rssi_c1e` | `show rssi`, extension | Auxiliar, sujeto a limitaciones del extractor histórico; fuera del cálculo principal |
| `dl_rate` | `show sta`, `connectedSTADLRateMbps` | Tasa descendente reportada, en el análisis Mbit/s; no goodput |
| `ul_rate` | Campo reservado en extractor público | No completado por el código público |
| `sta_dl_rssi`, `sta_ul_rssi` | `show sta` | dBm, **no** los RSSI primarios por cadena |
| `res20`–`res24` | Reservados | Sin indicador asignado |
 
**Variable calculada, no presente como columna fuente en los 24 campos originales:** `delta_rssi_primary = abs(rssi_c0p - rssi_c1p)`, en dB, cuando los dos primarios de un mismo ciclo son numéricos válidos.

**Precauciones de interpretación:** el firmware Cambium puede codificar el MCS como 104, 105, 205, etc.; no debe equipararse sin comprobación a un índice estándar. La dirección física exacta de las indicaciones RSSI y su equivalencia en el firmware histórico no se certifican aquí. Los valores reportados por el equipo no constituyen una calibración.

Véanse la [ficha estructurada](tesis/FICHA_OBSERVACION_DIGITAL.md), la [metodología](METODOLOGIA.md) y el [recolector](../acquisition/poll_epmp_public.sh).
