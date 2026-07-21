# The exact planar finite-dataset constant `F(2,3)`

This repository contains a proof package for one specific mean-estimation case
of Question 1 in Hanneke, Moran, Shlimovich, and Yehudayoff's COLT 2025
[open-problem note](https://proceedings.mlr.press/v291/hanneke25e.html).

**Review status:** a line-by-line mathematical and computational audit on
July 18, 2026 found no gap in the main theorem. The review strengthened several
definitions and ancillary SDP arguments, hardened the verifier, and rebuilt the
manuscript. This is still a research manuscript, not peer-reviewed validation
or a claim of bibliographic priority.

## Precise claim

For a nonempty finite multiset `D` in `R^2`, define

```math
L_D(h)=\frac1{|D|}\sum_{z\in D}\|h-z\|_2^2,
\qquad
L_D^*=\min_h L_D(h),
```

and

```math
L_D^*(3)=
\min_{(x_1,x_2,x_3)\in\operatorname{supp}(D)^3}
L_D\!\left(\frac{x_1+x_2+x_3}{3}\right).
```

The three selected points form a sequence: repetition is allowed, even beyond
a location's multiplicity in `D`. This matches the source problem's intended
semantics; see Appendix A.2 of the authors'
[companion COLT paper](https://proceedings.mlr.press/v291/hanneke25a.html).

The manuscript proves

```math
F(2,3):=\sup_D\frac{L_D^*(3)}{L_D^*}=\frac65,
```

with the stated convention for zero variance. The upper bound holds for every
finite planar multiset, and five copies of `(0,0)` together with one copy of
`(1,0)` attain equality. This fills the previously unknown `(d,n)=(2,3)` cell
in Question 1 of the COLT note, subject to external mathematical scrutiny.

## Scope: relation to SolveAll

The current
[SolveAll page](https://solveall.org/problem/colt-2025-data-selection-for-regression-tasks)
displays a materially different stochastic pool-selection problem. It uses an
IID pool `S ~ P^N`, selects `n` distinct sample indices, and measures expected
population excess risk as a function of `n` and `N`.

This repository does **not** determine that stochastic minimax quantity. Its
theorem concerns deterministic empirical mean estimation with repeatable
selections. It also does not resolve the COLT note's general `F(d,n)`, linear
regression, vector-valued regression, or weighted-selection questions.

## Other SolveAll-related projects

- [Right outliers with exact zero weights](https://github.com/SamPetkov/zero-atom-right-outliers) — the nonnegative zero-gap special case of the ReLU/zero-diagonal outlier problem.
- [One-factor FDR–FNR frontier](https://github.com/SamPetkov/one-factor-fdr-fnr) — a special-case result for one homogeneous rank-one Gaussian family related to the broad dependent-model FDR–FNR problem.

## Proof outline

1. Variance decomposition reduces the loss ratio to `q(D) <= V(D)/5`.
2. A self-contained support reduction preserves the mean, uses original
   support points, decreases variance, and leaves at most three support points.
3. An exact two-chamber certificate randomizes over the ten denominator-three
   frequency vectors and has second moment `C_p/5` about the population weights.
4. One deterministic triple has error no larger than that finite average.
5. An explicit six-point multiset attains the matching ratio `6/5`.

The semidefinite section reformulates the same certificate through dual
feasibility; it is explanatory and is not needed for the direct proof.

## Repository contents

- [`paper/`](paper/): reviewed TeX source and rebuilt PDF.
- [`verification/`](verification/): exact SymPy/Fraction audit and expected
  output.
- [`REVIEW.md`](REVIEW.md): proof-review findings, corrections, and limits.
- [`PROVENANCE.md`](PROVENANCE.md): archive hashes and change provenance.
- [`ORIGINAL_README.txt`](ORIGINAL_README.txt): README from the submitted ZIP.
- Tag `submitted-package-2026-07-18`: untouched-content baseline before review
  edits.

## Reproduce the exact audit

With [uv](https://docs.astral.sh/uv/):

```powershell
uv run --with-requirements requirements.txt python verification/verify_samuil_petkov_f23.py
uv run --with-requirements requirements.txt python -O verification/verify_samuil_petkov_f23.py
```

Both commands must match
[`verification/verify_samuil_petkov_f23_output.txt`](verification/verify_samuil_petkov_f23_output.txt).
The `-O` run is intentional: the audit uses explicit checks that cannot be
removed by Python optimization.

The script verifies the two matrix identities exactly, checks certificate
coefficient/boundary structure, exhausts the stated equality examples, and runs
deterministic exact-rational stress tests. It does not mechanically prove the
support-reduction, continuity, or expectation-to-deterministic arguments; those
remain mathematical proof obligations audited in `REVIEW.md`.

## Build the manuscript

A TeX installation with `latexmk`, `amsmath`, `mathtools`, `booktabs`,
`microtype`, `hyperref`, `fancyhdr`, and Latin Modern fonts is sufficient:

```powershell
New-Item -ItemType Directory -Force build | Out-Null
latexmk -pdf -halt-on-error -file-line-error -interaction=nonstopmode `
  -outdir=build paper/Samuil_Petkov_F23_Detailed_Proof.tex
```

GitHub Actions runs the exact verifier and a clean LaTeX build on every push and
pull request.

## Attribution and license

Copyright (c) 2026 Samuil Petkov. Except where noted, this repository is
licensed under [CC BY 4.0](LICENSE.md). Please cite the manuscript using
[`CITATION.cff`](CITATION.cff) and indicate if you modify it.
