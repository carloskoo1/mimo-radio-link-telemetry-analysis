# Archivo Zenodo y procedencia documental

**Estado verificado: 3 de noviembre de 2026.** Se corrigieron y publicaron los metadatos de la tesis en Zenodo (revisión 8): tipo **Publication / Thesis** y título oficial literal. El DOI, los archivos y la pertenencia del registro a la familia histórica permanecen intactos. La separación de la familia de versiones del software sigue pendiente de Zenodo.

## Fuente única de código y referencia científica

- **Repositorio principal de código:** https://github.com/carloskoo1/mimo-radio-link-telemetry-analysis
- **DOI de la versión del software v2.0.1 (citación reproducible):** https://doi.org/10.5281/zenodo.21844766
- **DOI conceptual de todas las versiones de software:** https://doi.org/10.5281/zenodo.21844660
- **DOI histórico de software v1.0.2:** https://doi.org/10.5281/zenodo.21844661

El DOI conceptual y el DOI específico de v2.0.1 no son repositorios independientes. Zenodo crea un DOI para cada versión y uno para su familia. Para citar una ejecución de análisis se prefiere el DOI específico de la versión verificada.

## Inventario verificado de la familia Zenodo (5 registros)

| Registro DOI | Contenido archivado | Uso correcto |
|---|---|---|
| [21844661](https://doi.org/10.5281/zenodo.21844661) | ZIP de software v1.0.2 | Versión histórica |
| [21844740](https://doi.org/10.5281/zenodo.21844740) | ZIP de software v2.0.0 | Versión histórica |
| [21844766](https://doi.org/10.5281/zenodo.21844766) | ZIP de software v2.0.1 | **Cita del software descrito en la tesis** |
| [21845197](https://doi.org/10.5281/zenodo.21845197) | ZIP de software v2.0.2 | Versión archivada posterior; el ref GitHub `v2.0.2` no respondió en la comprobación del 3-nov-2026 |
| [23551370](https://doi.org/10.5281/zenodo.23551370) | PDF y DOCX de una tesis (22-oct-2026) | Clasificado correctamente como **Publication / Thesis**, pero aún agrupado como quinta versión del software |

**Precisión:** el registro de tesis 23551370 está hoy agrupado bajo el DOI conceptual 21844660. El DOI conceptual actualmente puede mostrar el último depósito, que es una tesis y no código. Para reproducciones de esta tesis es preferible el DOI **específico** de software v2.0.1, 21844766, hasta que Zenodo resuelva la catalogación. No borrar DOI históricos ni crear versiones artificiales para ocultar registros.

## Inconsistencia documental que exige gestión del titular en Zenodo

El registro https://doi.org/10.5281/zenodo.23551370, publicado el **22 de octubre de 2026**, contiene los archivos `Tesis_Jhon_Torres_Formato_UNC_Final.pdf` y `Tesis_Jhon_Torres_Formato_UNC_Final.docx`, y ya está correctamente clasificado como `Publication / Thesis` con el título completo aprobado. **Sigue dentro de la misma familia conceptual que las versiones del código**. No es una versión de código, por lo que no debe presentarse como continuación técnica de v2.0.1.

Este registro corresponde a una edición documental de tesis anterior a las correcciones metodológicas posteriores, no a la versión final auditada del manuscrito. No debe representarse como la tesis corregida actual.

**Estado de corrección (3-nov-2026, verificado por API de Zenodo):**

1. **Resuelto:** recurso `Publication / Thesis`; título oficial: **IMPLEMENTACIÓN DE UN SISTEMA AUTOMATIZADO DE ADQUISICIÓN DE MÉTRICAS Y ANÁLISIS DEL DESBALANCE DE SEÑAL (ΔRSSI) EN UN RADIOENLACE MIMO DE 5,8 GHz EN UN ENTORNO ANDINO**.
2. **Resuelto:** se mantiene el DOI `10.5281/zenodo.23551370`, la fecha histórica de publicación y los archivos PDF/DOCX del 22-oct-2026. **Esos archivos no contienen las correcciones documentales posteriores**.
3. **Pendiente:** Zenodo todavía relaciona el registro de tesis como quinta versión del concepto de software `10.5281/zenodo.21844660`. Cambiar la clasificación y el título no modifica esa relación.
4. **Gestión necesaria:** solicitar al soporte de Zenodo una desvinculación no destructiva del registro de tesis, manteniendo su DOI. Si no es técnicamente posible, solicitar un procedimiento para documentar la anomalía sin crear ni eliminar registros.
5. Hasta que esa gestión se resuelva, citar el software v2.0.1 por su DOI **específico** `10.5281/zenodo.21844766`; citar la copia histórica de tesis por `10.5281/zenodo.23551370`, sin afirmar que sea la versión corregida del manuscrito.

**Verificación técnica:** https://zenodo.org/api/records/23551370 (revisión 8, título exacto, tipo `publication/dissertation`, DOI y archivos preservados).

## Validaciones individuales de especialistas

El Anexo 4 de la tesis preserva tres evaluaciones atribuidas a Edgar Laurente Gómez (radiofrecuencia), Erick Brian Koo Labrín (software) y Araceli Poémape Grados (metodología). Las tablas de puntuaciones y justificaciones coinciden literalmente; los documentos incorporados, por sí mismos, no demuestran una emisión independiente. No se deben recrear respuestas, firmas, fechados históricos ni elevar esas fichas a calibración metrológica.

Para cerrar la trazabilidad documental es necesario obtener los **originales individuales** (archivos firmados, correo de devolución con adjunto o confirmación actual inequívoca de cada evaluador), conservar su procedencia y señalar en el expediente qué evidencias fueron obtenidas posteriormente. Una ratificación actual, si se solicita, debe usar su fecha real, no la fecha histórica del instrumento.

## Fuentes verificables

- Metadatos de Zenodo: https://zenodo.org/api/records/21844766 ; https://zenodo.org/api/records/21844661 ; https://zenodo.org/api/records/23551370
- Zenodo — edición de metadatos publicados: https://help.zenodo.org/docs/deposit/manage-records/
- Zenodo — versionado y DOI conceptual: https://help.zenodo.org/docs/deposit/manage-versions/


## Conciliación con el PDF de cierre — 11 de noviembre de 2026

Se comprobó el PDF de 123 páginas físicas `TESIS_JHON_TORRES_101126.pdf` (SHA-256 `219a4c023bc2fbbc039b06e320c264f051c39d4a23ac0eac9dfef47970caabdf`). En la edición cotejada, la ficha de observación digital figura en el Anexo 2, página impresa 79. Este PDF **no es idéntico por presunción** al DOCX/PDF depositado el 22/10/2026 en el registro de tesis 23551370.

La verificación sobre la catalogación y parentesco de registros Zenodo que antecede a esta nota data del **03/11/2026**; el **11/11/2026 no fue posible completar una nueva lectura directa de la API de Zenodo**. No se afirma, por tanto, haber comprobado una rectificación posterior ni depositado el PDF de cierre. Se recomienda mantener separados:
- Software científico v2.0.1: DOI específico `10.5281/zenodo.21844766`.
- Copia histórica de tesis (22/10/2026): `10.5281/zenodo.23551370`.
- PDF corregido de tesis (10/11/2026): edición local identificada por nombre, fecha y SHA-256; **depósito de esa edición no acreditado**.

La etiqueta GitHub `v2.0.1` del 07/08/2026 preserva un `CITATION.cff` con DOI `21844661`, correspondiente a la versión histórica v1.0.2 según el inventario del 03/11. La rama `main` ya muestra `21844766` para el software v2.0.1. **No reescribir la etiqueta histórica**: describir la corrección de metadatos y usar el DOI específico verificado de la rama principal, dejando la discrepancia trazable.

El PDF de cierre conserva en el capítulo III (§3.3, p. 27), el Anexo 1 (p. 74) y en [23] una afirmación que puede interpretarse como que el depósito 23551370 contiene la versión final corregida. Debe sustituirse por una referencia explícita a **edición histórica** en el archivo editable de la tesis antes de nueva remisión. No alterar referencias numéricas ni páginas por edición manual del PDF sin cotejo del Word.

Sobre los tres especialistas: las fichas del Anexo 4 son evidencia **documental incorporada**, pero la corroboración de sus originales individuales (documento devuelto, correo con adjunto, o ratificación inequívoca fechada realmente) permanece **pendiente**. No publicar firmas ni fichas originales en este repositorio sin consentimiento.

Véase [acta de conciliación documental](tesis/CONCILIACION_GITHUB_ZENODO_20261111.md).
