# Conciliación GitHub – Zenodo – tesis de Jhon Torres

**Cotejo realizado:** 11 de noviembre de 2026  
**Alcance:** integridad documental y procedencia de versiones; no se realizó una nueva campaña ni se repitió el análisis numérico sobre telemetría restringida.

## Identificación de la edición revisada

- **Edición cotejada:** `TESIS_JHON_TORRES_101126.pdf`
- **Páginas físicas:** 123; numeración preliminar romana y cuerpo arábigo.
- **SHA-256 del PDF cotejado:** `219a4c023bc2fbbc039b06e320c264f051c39d4a23ac0eac9dfef47970caabdf`
- **Ficha digital:** Anexo 2, p. impresa 79; dos registros históricos del 16/05/2026; verificada su presencia.
- **Secciones relevantes:** §3.3 (pp. 23–24), §3.3.2 (p. 29), Tabla I (p. 34), Tabla II (pp. 35–36), §4.7 (pp. 55–56), Anexos 2, 4 y 7.
- **Nota:** el archivo Word editable equivalente a este PDF no se pudo comprobar byte a byte en el cotejo del 11/11/2026. No se atribuye a archivos previos una edición posterior.

## Identificadores y límites de archivo

| Función | DOI o elemento | Estado |
| --- | --- | --- |
| Software científico v2.0.1 para el análisis | `10.5281/zenodo.21844766` | Documentado en `CITATION.cff` actual y expediente del 03/11/2026 |
| Concept DOI de la familia de versiones del software | `10.5281/zenodo.21844660` | Documentado; el 03/11 persistía la anomalía de agrupación con una tesis |
| Tesis histórica depositada el 22/10/2026 | `10.5281/zenodo.23551370` | Documentado como edición previa; **no equivale** a la tesis corregida del 10/11/2026 |
| Tesis corregida 10/11/2026 | SHA-256 local indicado arriba | Existencia en expediente; nuevo depósito Zenodo **no acreditado** |

La evaluación API de Zenodo de 03/11/2026 informó que el registro de tesis había sido clasificado como **Publication / Thesis**, pero seguía ligado a la misma familia conceptual que las versiones del software. No se completó una consulta API nueva el 11/11, por lo que se conserva expresamente la fecha de última comprobación.

## Diferencia histórica de CITATION.cff

- En GitHub, `v2.0.1` apunta al commit `e91214bb9931131ef971c930a76c46419076525a` del 07/08/2026.
- El `CITATION.cff` conservado en ese tag contiene `10.5281/zenodo.21844661`.
- El `CITATION.cff` actual en `main` identifica la versión v2.0.1 como `10.5281/zenodo.21844766`, que corresponde al inventario de Zenodo documentado el 03/11/2026.
- **Corrección adecuada:** no reescribir el tag histórico; mantener el registro de discrepancia y citar la versión de software mediante `21844766` en publicaciones y documentos actuales.

La mención de «master's thesis» que persiste en el README del tag de agosto también es metadato histórico; el README actualizado de `main` describe correctamente una tesis de pregrado de Ingeniería de Sistemas.

## Corrección editorial necesaria dentro del manuscrito

La tesis del 10/11 presenta el DOI `23551370` como si el depósito de Zenodo contuviera su **versión final**, en §3.3, p. 27, y Anexo 1, p. 74. Esa frase debe limitarse a la **edición histórica del 22/10/2026**.

Propuesta breve para §3.3, p. 27:
> Una edición anterior de esta tesis se depositó en Zenodo con el DOI [23]; dicho registro no corresponde a la presente edición corregida.

Propuesta para Anexo 1, p. 74:
> Una edición anterior de la tesis se depositó en Zenodo [23] con DOI 10.5281/zenodo.23551370. El registro citado contiene los archivos históricos y no debe confundirse con la edición corregida presentada al jurado.

Se recomienda verificar paginación y coincidencia Word–PDF después de insertar el texto, antes de cualquier depósito nuevo.

## Revisión especializada y datos

- **Verificado documentalmente:** existen fichas de tres especialistas en el Anexo 4 de la tesis.
- **Pendiente de procedencia:** cotejar los documentos individuales originales, correos de devolución o ratificaciones actuales reales; las firmas integradas al PDF no bastan por sí solas para demostrar emisión independiente.
- **Acceso restringido:** telemetría original, manifiestos e insumos para reproducción numérica autónoma; la verificación de integridad descrita en la tesis no sustituye una nueva ejecución por un tercero.
- **Sin conformidad formal:** ninguna actualización documental equivale a un dictamen favorable de los jurados.

## Próximos actos sin alteración retrospectiva

1. Conservar versiones históricas y SHA-256.
2. Actualizar el manuscrito editable y verificar su PDF para que [23] cite solo la edición histórica.
3. Solicitar a Zenodo, mediante el titular del registro, **desvinculación no destructiva** de la tesis respecto de la familia de versiones del software, si la anomalía continúa; no borrar DOI ni registros.
4. Documentar la procedencia de fichas de especialistas en expediente académico de acceso controlado.
5. Mantener separados los estados **verificado**, **parcial**, **pendiente** y **acceso restringido**.

**No se afirma que Zenodo haya recibido la edición corregida.**

## Copia PDF revisada creada el 11/11/2026

Se generó una **copia corregida local**, llamada `TESIS_JHON_TORRES_111126_REFERENCIAS_CONCILIADAS.pdf`, a partir del PDF cotejado. Se modificaron exclusivamente tres páginas físicas (39, 84 y 86), correspondientes a las páginas impresas 27, 72 y 74:

- §3.3 (p. 27): identifica expresamente como **edición previa** el depósito de la tesis en Zenodo.
- Referencia [23] (p. 72): consigna el título oficial completo de la tesis, en lugar del título abreviado del software.
- Anexo 1 (p. 74): identifica `23551370` como **registro histórico**, sin atribuirle la edición corregida.

**SHA-256 de la copia corregida:** `df9f252beb7db3063a8b296635406192bdf3214e0c6d646e5b2cf3775192b68a`. Conserva **123 páginas físicas**. Una comparación del texto extraído detectó cambios solo en las páginas físicas 39, 84 y 86. Se inspeccionó visualmente la maquetación de estas tres páginas. El PDF corregido se entrega al responsable en el expediente de revisión; **no se ha subido a Zenodo ni sustituido la copia histórica de GitHub**.

La edición del DOCX original correspondiente y la eventual sincronización archivística quedan pendientes de acceso/autorización a ese documento editable y de la decisión del titular en Zenodo. Las fichas de especialistas aún requieren verificación de procedencia individual.
