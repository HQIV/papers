#!/usr/bin/env python3
"""Regenerate SPARC figure + JSON for the orbital flyby paper."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / "scripts" / "hqiv_sparc_rotation.py"
OUT_JSON = Path(__file__).resolve().parents[1] / "artifacts" / "sparc_hqiv_catalog.json"
OUT_FIG = Path(__file__).resolve().parents[1] / "figures" / "sparc_hqiv_map.pdf"


def main() -> int:
    cmd = [
        sys.executable,
        str(SCRIPT),
        "--run-all",
        "--quality-cut",
        "2",
        "--min-inclination",
        "30",
        "--summary-only",
        "--write",
        str(OUT_JSON),
        "--plot-figure",
        str(OUT_FIG),
    ]
    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True, cwd=ROOT)
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_FIG}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
