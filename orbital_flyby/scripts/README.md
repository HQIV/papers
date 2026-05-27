# Reproducer scripts — orbital flyby paper

## SPARC rotation-curve map

From the repository root (requires `scripts/data/sparc/` from `scripts/download_sparc_data.sh`):

```bash
python3 papers/orbital_flyby/scripts/generate_sparc_map.py
```

Outputs:

- `papers/orbital_flyby/artifacts/sparc_hqiv_catalog.json` — catalog summary + $R^2$ block
- `papers/orbital_flyby/figures/sparc_hqiv_map.pdf` — $v_{\rm obs}$ vs $v_{\rm HQIV}$ scatter

Uses the same single-exponent lapse $\varphi(R)=\varphi_{\rm hom}/(1+R/R_d)$ and gas+disk+bulge SPARC components as `scripts/hqiv_sparc_rotation.py` (no halo fit).

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
