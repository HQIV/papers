# S³ / SO(4) ζ(s) projection closed form — Lean formal note

**Source:** `hqiv_s3_zeta_so4_projection_closed_form.tex`

**Role:** Synthesis of the machine-checked S³ story spine: harmonic--Δ--SO(4) closure,
45° quaternion projections, regional closed forms for `ζ(s)`, polar decoupling and
log edge, j/k rotation cancellation on even π-slots, associator / S⁷ torsion channels,
the RH discharge chain (proved packaging + conditional capstone), and the shared **½**
half-slope bridge packaging **RH ∧ Goldbach parity** (`S3ExplicitFormulaDualitySlot`).

**Messaging:** includes `papers/include/readout_dictionary_messaging.tex` only—not the
full HQIV patch QFT contract (`patch_theory_messaging.tex`). §`sec:hep-zeta-bridge`
explains why “zeta” recurs in sector-zeta (TUFT), classical projection (this note),
and HEP multichannel readouts.

**Build:**
```bash
cd papers/s3_zeta_so4_projection
latexmk -pdf hqiv_s3_zeta_so4_projection_closed_form.tex
```

**Lean mirror:** `lake build HQIVStory` in [hqiv-lean](https://github.com/HQIV/hqiv-lean).

**Bib key:** `hqiv-s3-zeta-so4-paper`

**Status:** Unpublished draft (Lean formal proof note tier).

**Agent ontology:** see `AGENTS/PATCH_ONTOLOGY.md` (projection geometry / classical ζ
dictionary) and `AGENTS/OCTONION_TABLE_AUDIT_TODO.md` (frozen O-table audit).

**Key sections (2026-06):**
- §Analytic strip lift / critical-line carrier — `S3CriticalLineCarrierBundle.lean`, `S3AnalyticStripLift.lean`, `S3AnalyticStripClassification.lean`
- §Harmonic-shell arc sweep — `S3HarmonicShellZeroCounting.lean` (countable $(n,k)$ slots at $2\pi k/n$, not heights $t$)
- §$j$–$k$ unit-circle zero readout — `S3HopfJKUnitCircleZeroReadout.lean` ($e^{\pi i j k}$ phase on Hopf fiber; $\zeta$-zero $\Leftrightarrow$ amplitude balance)
- §Euler prime circle counting — `S3HopfJKEulerPrimeCircleCounting.lean` (prime phases at shell arcs; two primes pin the circle; not a $t$-height scan)
- §σ-readout scope — `S3SigmaReadoutScope.lean`
- §Orbit vs pointwise + quadruplet — `S3OrbitVsPointwiseGap.lean`, `S3ZeroQuadrupletOrbit.lean`
- §RH and Goldbach — `S3ExplicitFormulaDualitySlot.lean`, `GoldbachG2Parity.lean`
- §Log edge — `S3LogPhaseEdge.lean`
- §HEP zeta bridge — narrative link to `hep_decay_readout/`

**Related external work:** [Lee–Takahashi–Tsai (arXiv:2603.12320)](https://arxiv.org/abs/2603.12320) — PTE degree \(k=3\) anomaly cancellation; linked in §PTE degree 3.
