from __future__ import annotations

from pathlib import Path
import pandas as pd

from src.common import PROJECT_ROOT, load_config, read_csv_robust, sha256_file, setup_logging

def main() -> None:
    setup_logging("01_importar")
    cfg = load_config()
    input_dir = Path(cfg["input_dir"])
    files = sorted(input_dir.rglob(cfg["file_pattern"]))

    print(f"Archivos descubiertos: {len(files)}")

    frames = []
    manifest = []

    for i, path in enumerate(files, start=1):
        try:
            df = read_csv_robust(path)
            df["source_file"] = path.name
            df["source_sha256"] = sha256_file(path)
            frames.append(df)
            manifest.append({
                "file_name": path.name,
                "rows": len(df),
                "size_bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "status": "OK",
            })
            print(f"[{i}/{len(files)}] OK {path.name}: {len(df)} filas")
        except Exception as exc:
            manifest.append({
                "file_name": path.name,
                "rows": None,
                "size_bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                "status": "ERROR",
                "error": str(exc),
            })
            print(f"[{i}/{len(files)}] ERROR {path.name}: {exc}")

    if not frames:
        raise RuntimeError("No se pudo importar ningún CSV.")

    raw = pd.concat(frames, ignore_index=True, sort=False)
    out = PROJECT_ROOT / "data" / "processed"
    out.mkdir(parents=True, exist_ok=True)

    raw.to_parquet(out / "01_raw_importado.parquet", index=False)
    pd.DataFrame(manifest).to_csv(out / "01_manifest.csv", index=False, encoding="utf-8-sig")

    print(f"Importación terminada: {len(raw)} filas crudas.")

if __name__ == "__main__":
    main()
