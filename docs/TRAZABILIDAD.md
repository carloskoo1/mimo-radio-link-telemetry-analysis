# Trazabilidad de observación y resultados — tesis Jhon Torres

| Origen y etapa | Campo o evidencia | Operación/validez | Objetivo y producto |
| --- | --- | --- | --- |
| AP, `show rssi` | `rssi_c0p`, `rssi_c1p`, `ts` | Primary Chain 0/1; dBm; mismo ciclo; ausentes no se imputan | OE2, RSSI temporal por cadena |
| Captura canónica | `rssi_c0p`, `rssi_c1p` | `ΔRSSI=abs(rssi_c0p-rssi_c1p)`; dB solo con dos primarios válidos | OE3, distribución y comportamiento de ΔRSSI |
| AP, `show sta` | `dl_rate`, `snr_dl`, `snr_ul`, `mcs_dl`, `mcs_ul` | Identificar estación y ciclo; MCS es código fabricante; `dl_rate` es tasa reportada, no goodput | OE4, relaciones observadas; SNR/MCS complementarios |
| Script Bash/SSH, CSV | 24 columnas y archivos diarios | Cotejo CLI–CSV de 16/05/2026 y controles estructurales, sin generalizar a toda la campaña | OE1, implementación y verificación delimitada |
| Pipeline Python | CSV originales → capturas canónicas → medianas horarias | Consolidar filas AP/SM replicadas; sensibilidad temporal y dependencia | OE4, coeficientes/descripción; OE5, límites de interpretación |

Para un ejemplo ya documentado en la tesis, identificadores, unidades y criterios de validez, véase [Ficha de observación digital estructurada](tesis/FICHA_OBSERVACION_DIGITAL.md). Para la respuesta documental al jurado, véase [Subsanación M5](tesis/SUBSANACION_M5_FICHA_OBSERVACION_20261110.md).

**Advertencias:** no existe un conjunto de mediciones independientes AP + SM por la etiqueta `role`; el RSSI primario `show rssi` no se debe identificar automáticamente con polarizaciones H/V; el coeficiente de asociación no prueba causalidad. La base cruda está restringida y no puede reproducirse numéricamente solo desde este repositorio.
