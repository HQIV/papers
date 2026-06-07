#!/usr/bin/env python3
"""Regenerate SPARC JSON summary for the accelerations / galaxy-evolution paper."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ORB_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "hqiv_sparc_rotation.py"
OUT_JSON = ORB_ROOT / "artifacts" / "sparc_hqiv_catalog.json"
OUT_FIG = ORB_ROOT / "figures" / "sparc_hqiv_map.pdf"


def main() -> int:
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{ROOT / 'scripts'}:{ROOT}:{env.get('PYTHONPATH', '')}"
    cmd = [
        sys.executable,
        str(SCRIPT),
        "--run-all",
        "--quality-cut",
        "2",
        "--min-inclination",
        "30",
        "--write",
        str(OUT_JSON),
    ]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True, cwd=ROOT, env=env)
    print(f"Wrote {OUT_JSON}")
    if OUT_FIG.parent.exists():
        print(
            "Note: figure PDF is optional; add --plot-figure to hqiv_sparc_rotation.py "
            "or copy from HQIV_Orbital artifacts/sparc_hqiv_whim_filament_v2.json."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
