# Reproducer scripts — accelerations / galaxy-evolution paper

Canonical LaTeX: `hqiv_accelerations_galaxy_evolution.tex`  
Legacy alias: `hqiv_orbital_flyby_anomaly.tex` (inputs the canonical file).

## SPARC catalog summary (WHIM + filaments on by default)

From the HQIV_Orbital repository root (requires `scripts/data/sparc/`):

```bash
export PYTHONPATH="${PWD}/HQIV_LEAN/scripts:${PWD}"
python3 HQIV_LEAN/papers/orbital_flyby/scripts/generate_sparc_map.py
```

Outputs:

- `papers/orbital_flyby/artifacts/sparc_hqiv_catalog.json` — full 175-galaxy summary
- Full per-galaxy payload: `HQIV_Orbital/artifacts/sparc_hqiv_whim_filament_v2.json`

Filament spine setup:

```bash
bash scripts/download_filament_environment.sh
```

## Flyby table

```bash
python3 scripts/hqiv_orbital_flyby_omaxwell.py --paper-table \
  > papers/orbital_flyby/flyby_paper_table.tex
```

## Extended catalog + mm/s noise budget

```bash
python3 scripts/hqiv_flyby_extended_catalog.py \
  --json scripts/artifacts/flyby_extended_catalog.json
```

Includes MESSENGER, Rosetta II/III, Juno, and Rosetta-I space-weather context (quiet Dst week, not May 2005 superstorm).
