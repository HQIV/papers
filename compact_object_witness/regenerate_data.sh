#!/usr/bin/env bash
# Regenerate all compact-object / pulsar witness JSON for the MHD equivalence paper.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../" && pwd)"
cd "$ROOT"

echo "==> compact_object_witnesses.json"
python3 scripts/hqiv_compact_object_mass.py --json

echo "==> pulsar_witness_comparison.json"
python3 scripts/hqiv_pulsar_witness_benchmark.py --json

echo "==> lagrangian_faithfulness_audit.json"
python3 scripts/hqiv_lagrangian_faithfulness_audit.py --json

echo "Done. Paper TeX: papers/compact_object_witness/hqiv_compact_object_crust_mhd_equivalence.tex"
