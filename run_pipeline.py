from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

STAGES = [
    ("01 Importación", ROOT / "scripts" / "01_importar.py"),
    ("02 Preprocesamiento", ROOT / "scripts" / "02_preprocesar.py"),
    ("03 Estadística", ROOT / "scripts" / "03_estadistica.py"),
    ("04 Figuras", ROOT / "scripts" / "04_figuras.py"),
    ("05 Reportes", ROOT / "scripts" / "05_reportes.py"),
]

def main() -> int:
    for name, script in STAGES:
        print("\n" + "=" * 70)
        print(name)
        print("=" * 70)
        result = subprocess.run([sys.executable, str(script)], cwd=ROOT)
        if result.returncode != 0:
            print(f"\nERROR EN ETAPA: {name}")
            return result.returncode
        print(f"\nOK: {name}")
    print("\nPIPELINE V3 COMPLETADO.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
