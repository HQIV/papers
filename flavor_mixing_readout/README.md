# Flavor mixing readout (CKM + PMNS holonomy)

**Title:** Flavor Mixing, Rare Decays, and SMEFT Coefficients from the HQIV Discrete Octonion Carrier: A Machine-Checked Proof Ladder

**Lean build:** `lake build paper_flavor_mixing`

**Witness export + TeX tables + scripts bundle:**

```bash
python3 scripts/hqiv_flavor_mixing_export.py
```

**Upstream:** TUFT+SM, HEP decay readout (CKM slot discipline), `HopfShellBeltramiMassBridge` (T10 PMNS), Sievers glueball preprint (strong-sector bridge).

**Lean spine:** `Hqiv/Physics/ProofSpineInventory.lean` — seven-phase certificate bundle + Sievers bridge.

**Proof map:** `docs/PROOF_SPINE_MAP.md`

**Attachments:** `scripts.zip`, `data/flavor_mixing_witness.json`, `generated/*.tex`

## Build paper

```bash
cd papers/flavor_mixing_readout
latexmk -pdf hqiv_flavor_mixing_readout.tex
```
