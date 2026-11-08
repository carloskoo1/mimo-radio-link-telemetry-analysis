# Contrastación de la hipótesis y cumplimiento del objetivo general

Documento complementario de la tesis de Jhon Cristhian Torres Hoyos. La versión científica computacional utilizada para los resultados es v2.0.1 (DOI: https://doi.org/10.5281/zenodo.21844766). Este texto explica la lectura metodológica del conjunto conservado; no altera el código ni la serie de datos.

## Objetivo general y evidencia

**Objetivo:** implementar un sistema automatizado de adquisición de métricas y analizar el desbalance de señal (ΔRSSI) de un radioenlace MIMO de 5,8 GHz en un entorno andino.

| Componente | Procedimiento y dato | Resultado que demuestra su cumplimiento |
| --- | --- | --- |
| Implementación | Consultas automatizadas Bash/SSH al AP mediante `show rssi` y `show sta`; CSV fechados; consolidación de una captura por instante. | 90 CSV con 347 036 filas originales y 173 513 capturas canónicas. En el cotejo directo del 16 de mayo de 2026, 21 438 campos CLI–CSV concordaron en ciclos asignables. El cotejo de un día no certifica todos los días. |
| Análisis de ΔRSSI | RSSI válido de ambas cadenas en un mismo instante; ΔRSSI = abs(RSSI Chain 0 − RSSI Chain 1). | 164 740 diferencias calculables; mediana de 11 dB. Las medianas de Chain 0 y Chain 1 fueron −82 y −93 dBm. |
| Asociación observada | Emparejamiento de ΔRSSI con la tasa descendente reportada en la captura; comparación con medianas horarias y sensibilidad por bloques. | 161 340 pares completos y 1 989 horas completas. Spearman ρ = 0,224 en capturas y ρ = 0,493 en horas; la dirección positiva persistió con bloques de 1, 3 y 7 días. |

## Hipótesis de trabajo y decisión

**Hipótesis:** en los tramos registrados, ΔRSSI y la tasa descendente reportada presentan asociación positiva en las capturas válidas y en sus medianas horarias.

La contrastación descriptiva usa solo ese par de magnitudes para la decisión: exige signo positivo de Spearman en las dos escalas y conservación del signo en sensibilidades temporales de 1, 3 y 7 días. Los resultados cumplen esos criterios en el conjunto disponible. La división cronológica enero–abril/mayo muestra consistencia interna de la dirección. Como la regla se precisó durante el análisis de esta serie, la decisión se limita a los tramos observados y no constituye una prueba independiente de repetición. SNR y los códigos MCS son asociaciones complementarias y no deciden esta hipótesis.

Las capturas próximas son dependientes en el tiempo; los valores p nominales no sustituyen un análisis de esa dependencia. La tasa descendente es el valor reportado por el equipo, no una medición de caudal útil. La correlación no demuestra que modificar ΔRSSI cause un cambio de tasa.

## Correspondencia de objetivos específicos

| Objetivo | Resultado en la tesis | Conclusión |
| --- | --- | --- |
| OE1. Implementar y verificar la adquisición | §§4.1–4.2: archivos, consolidación y cotejo | Conclusión específica 1 |
| OE2. Describir RSSI por cadena | §4.3: niveles y evolución temporal | Conclusión específica 2 |
| OE3. Caracterizar ΔRSSI | §4.3: distribución y serie temporal | Conclusión específica 3 |
| OE4. Examinar asociaciones | §§4.4–4.7: coeficientes, sensibilidad y decisión | Conclusión específica 4 |
| OE5. Interpretar los hallazgos | §4.8 y capítulo V: significado y límites | Conclusión específica 5 |

Los CSV originales no se distribuyen en este repositorio. El código y la documentación son públicos; la consulta de la telemetría requiere autorización separada. Los registros adicionales `raw_show_sta` identifican al SM SanJose y su firmware en fechas disponibles, pero no prueban el firmware histórico del AP ni añaden capturas independientes a la hipótesis.
