# Reproducer scripts — TUFT + SM Lagrangian synthesis paper

This directory contains the Python evaluation scripts that reproduce every
quantitative comparison table and epoch plot cited in

> **Topological Necessity of the Fermion Mass Spectrum and the Standard Model
> Lagrangian from the HQIV Discrete Action: TUFT Hopf Topology and Dynamic
> Casimir Bridge on the Octonion Carrier**

The bundle is self-contained (local import closure only) so it can ship as
`scripts.zip` on the Zenodo record alongside the paper PDF and share the
same DOI.

## Entry scripts (paper-cited)

| File | Reproduces | Notes |
| --- | --- | --- |
| `hqiv_tuft_mass_spectrum_pdg_eval.py` | PDG comparison tables at ξ_ref = 5 (lock-in deviation chart, baryon global readout) | Primary mass-spectrum readout: leptons, electroweak bosons, proton ground, global hadron layer. No fitted masses. |
| `hqiv_tuft_electroweak_boson_readout.py` | $W$/$Z$/$H$ sector table and geometric $\sin^2\theta_W$ | Mirrors `TuftElectroweakBosonReadout.lean`. |
| `hqiv_tuft_global_hadron_readout.py` | Global hadron excitation readout | Mirrors `TuftGlobalHadronReadout.lean`. |
| `hqiv_scale_witness.py` | Proton-lock-in propagation chain (§scale witness) | Cosmological scale ladder from the reference proton anchor. |
| `hqiv_lean_physics_primitives.py` | $C_2(\xi)$ epoch table and Figure~2 ($C_2$ vs $\xi$) | Lapse running on the temperature ladder. |
| `hqiv_dynamic_bulk_bbn.py` | Dynamic BBN lapse clock (§C₂–Rindler) | Opportunity-weighted shell reaction clock at BBN temperatures. |

Additional modules in this folder are **dependency modules** imported by the
entry scripts above (continuous shell mass, excited states, coupling linear
system, nuclear binding helpers, etc.).

## Requirements

* Python 3.10 or newer.
* Standard library only — no third-party packages.

## How to run

From this directory (`papers/tuft_sm_lagrangian/scripts`):

```bash
# Full PDG comparison table (primary)
python3 hqiv_tuft_mass_spectrum_pdg_eval.py
python3 hqiv_tuft_mass_spectrum_pdg_eval.py --json

# Electroweak boson readout
python3 hqiv_tuft_electroweak_boson_readout.py

# Global hadron excitation layer
python3 hqiv_tuft_global_hadron_readout.py

# Proton-lock-in scale propagation
python3 hqiv_scale_witness.py

# C₂(ξ) epoch table (Figure 2 data)
python3 hqiv_lean_physics_primitives.py

# Dynamic BBN lapse clock
python3 hqiv_dynamic_bulk_bbn.py
```

All scripts are deterministic and run in well under a minute on a modern laptop.

## Regenerating scripts.zip

From the paper directory (`papers/tuft_sm_lagrangian`):

```bash
cd /home/jr/Repos/HQIV_LEAN/papers/tuft_sm_lagrangian
zip -r scripts.zip scripts/ -x "*.pyc" "__pycache__/*"
```

To refresh the bundle from the repository root scripts after code changes:

```bash
cd /home/jr/Repos/HQIV_LEAN
python3 - <<'PY'
import ast, os, shutil
from collections import deque
ROOT, DEST = 'scripts', 'papers/tuft_sm_lagrangian/scripts'
ENTRY = [
    'hqiv_tuft_mass_spectrum_pdg_eval.py', 'hqiv_tuft_electroweak_boson_readout.py',
    'hqiv_tuft_global_hadron_readout.py', 'hqiv_scale_witness.py',
    'hqiv_dynamic_bulk_bbn.py', 'hqiv_lean_physics_primitives.py',
]
def module_to_file(name):
    return os.path.join(ROOT, name + '.py') if name.startswith(('hqiv_', 'cubic_')) else None
def imports_in(path):
    tree = ast.parse(open(path, encoding='utf-8').read(), filename=path)
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            out += [a.name.split('.')[0] for a in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module:
            out.append(node.module.split('.')[0])
    return out
seen, q = set(), deque(ENTRY)
while q:
    rel = q.popleft()
    if rel in seen: continue
    path = os.path.join(ROOT, rel)
    if not os.path.isfile(path): continue
    seen.add(rel)
    for imp in imports_in(path):
        dep = module_to_file(imp)
        if dep: q.append(os.path.basename(dep))
os.makedirs(DEST, exist_ok=True)
for rel in sorted(seen):
    shutil.copy2(os.path.join(ROOT, rel), os.path.join(DEST, rel))
print('copied', len(seen), 'files')
PY
zip -r scripts.zip scripts/ -x "*.pyc" "__pycache__/*"
```

## Provenance and versioning

* Constants ($\alpha = 3/5$, referenceM $= 4$, proton anchor 938.272 MeV,
  $\xi_{\mathrm{ref}} = 5$, lattice rationals) come from the paper and the
  Lean modules cited in Appendix~\ref{app:lean-catalog}. PDG values are
  comparison targets only — they are never fitted into the HQIV readouts.
* Machine-checked proofs build under the `paper_tuft_sm_lagrangian` Lake
  target in [HQIV/hqiv-lean](https://github.com/HQIV/hqiv-lean) (PR #12).

## Patch-ontology disclaimer

Numerical outputs are calculation-approximation translations of patch
quantities (integer cycle indices, shell ladders, normalised readouts) into
MeV, kelvins, and SI units. They are **not** a continuum-limit refinement of
the patch theory. The discrete patch layer is the ontology; these scripts are
interoperability tools for cross-citation and Zenodo reproducibility only.

## Citation

When citing the scripts bundle, cite the paper Zenodo record
[`10.5281/zenodo.20517172`](https://doi.org/10.5281/zenodo.20517172) and this
supplementary `scripts.zip` file on the same record.
