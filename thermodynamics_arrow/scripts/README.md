# Reproducer scripts — Thermodynamics and arrow of time

Small dependency-light checks for the thermodynamics Tier-1 note.

## Contents

| File | Reproduces | Notes |
| --- | --- | --- |
| `thermo_ladder_and_c3_heat.py` | §3 ladder \(T(m)=1/(m+1)\), §4 \(C_3\) dissipation sign and Euler step | Standard library; matches Lean sign theorems in spirit |

## How to run

```bash
python3 thermo_ladder_and_c3_heat.py
python3 thermo_ladder_and_c3_heat.py --json
```

## Regenerating scripts.zip

From `papers/thermodynamics_arrow/`:

```bash
zip -r scripts.zip scripts/ -x "*.pyc" "__pycache__/*"
```

## Citation

Steven Ettinger Jr., *Thermodynamics and the Arrow of Time from the HQIV Temperature Ladder: Finite Blackbody Entropy, Causal Monogamy, and Machine-Checked Dissipation Signs* (2026). Zenodo [`10.5281/zenodo.20478826`](https://doi.org/10.5281/zenodo.20478826); `scripts.zip` shares the record.
