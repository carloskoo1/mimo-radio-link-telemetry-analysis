# Trazabilidad del Pipeline V3

- Los CSV originales no se modifican.
- Cada archivo se registra con hash SHA-256.
- El resultado de cada etapa queda almacenado.
- Los MCS se tratan como códigos propietarios Cambium.
- La tasa de transmisión se convierte a Mbps antes de cualquier coerción destructiva.
- La selección canónica prioriza AP y utiliza SM únicamente como respaldo.
- Las correlaciones se calculan en datos por timestamp y medianas horarias.
