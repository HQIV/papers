# HQIV proof spine synthesis (programme overview)

**Title:** The HQIV Proof Spine: Machine-Checked Synthesis of Flavor, Electroweak, Strong-Sector, and Cosmological Readouts from the Discrete Octonion Carrier

**Purpose:** Big-picture document citing `proofSpineInventory_holds` as the verified backbone and mapping Tier papers to spine phases.

**Lean capstone:** `lake build paper_flavor_mixing`

**Export witness + TeX tables:**

```bash
python3 scripts/hqiv_proof_spine_synthesis_export.py
```

**Build PDF:**

```bash
cd papers/proof_spine_synthesis
latexmk -pdf hqiv_proof_spine_synthesis.tex
```

**Related:** `docs/PROOF_SPINE_MAP.md`, `papers/flavor_mixing_readout/`
