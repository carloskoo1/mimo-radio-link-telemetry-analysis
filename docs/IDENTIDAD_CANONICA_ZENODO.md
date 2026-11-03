# Identidad canónica del proyecto y archivo Zenodo

Fecha de verificación: 2026-11-03.

Este proyecto emplea **un solo repositorio GitHub** y **una sola familia conceptual de Zenodo**. Los DOI de versiones no son depósitos independientes: Zenodo los asigna para preservar archivos históricos inmutables.

| Función | Referencia oficial |
|---|---|
| Repositorio de código | https://github.com/carloskoo1/mimo-radio-link-telemetry-analysis |
| Familia conceptual Zenodo (todas las versiones) | https://doi.org/10.5281/zenodo.21844660 |
| Versión de software archivada y citada en la tesis (v2.0.1) | https://doi.org/10.5281/zenodo.21844766 |
| Código etiquetado v2.0.1 | https://github.com/carloskoo1/mimo-radio-link-telemetry-analysis/tree/v2.0.1 |

## Alcance de los DOI

- DOI 10.5281/zenodo.21844661: software histórico **v1.0.2** (no es la versión 2.0.1).
- DOI 10.5281/zenodo.21844766: archivo **v2.0.1**, con un ZIP del código y metadatos de sus autores.
- DOI 10.5281/zenodo.23551370: registro publicado el **22/10/2026** con un PDF y un DOCX de una versión anterior de la tesis. Este registro fue incluido en la misma familia conceptual que el software y aparece catalogado como «Software» aunque **sus archivos son documentos**. Es un asunto de catalogación y agrupación de versiones que requiere gestión con los responsables de Zenodo. **No corresponde citarlo como versión ejecutable del código ni como la tesis V4.**

La etiqueta GitHub `v2.0.1` y sus notas históricas conservan una referencia antigua al DOI 21844661, correspondiente en realidad a `v1.0.2`. Para citas de software `v2.0.1` debe prevalecer el registro Zenodo verificado (21844766), conforme a la rama principal actual. No se modifican retrospectivamente los archivos ZIP depositados ni se reasignan DOI históricos.

## Trazabilidad y límites

Los archivos originales de telemetría **no forman parte del repositorio GitHub público**. Reproducir numéricamente todos los resultados exige obtener las fuentes CSV y verificar los SHA-256 contra los manifiestos originales. La existencia del código publicado no acredita que cada versión archivada haya sido la utilizada para recolectar la campaña histórica.

Las fichas de especialistas y sus firmas **no deben agregarse como archivos públicos adicionales** sin autorización de cada persona. Las copias de consulta se administran con el expediente académico de la tesis. La concordancia literal entre tres fichas no demuestra su elaboración independiente.

## Política editorial

1. Mantener un solo GitHub principal, sin clones de publicación.
2. Citar un DOI de software **de versión** para reproducibilidad; usar el DOI **conceptual** como puerta de entrada al conjunto de versiones.
3. No crear nuevas entradas de Zenodo por correcciones solo de metadatos.
4. Solicitar la corrección editorial del registro documental 23551370 y su relación con la familia de versiones, sin borrar archivos ni alterar la trazabilidad de sus identificadores.
5. Mantener la tesis aprobada y las versiones de software diferenciadas hasta que Zenodo confirme la corrección.
