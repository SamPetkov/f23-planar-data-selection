# Mathematical review report

Review date: **July 18, 2026**

## Verdict

**Correct with clarifying revisions under the manuscript's stated
selection-with-repetition model.** No counterexample, missing case, circular
dependency, or reversed inequality was found in the proof of
`F(2,3)=6/5`.

This verdict is an adversarial technical review, not peer review. Mathematical
responsibility remains with the author.

## Exact theorem reviewed

The reviewed theorem is the finite-dataset planar mean-estimation case from
Question 1 of the COLT open-problem note. The selector chooses a sequence of
three points from `supp(D)` and may repeat a point. The result does not cover
the distinct-index, IID-pool, population-risk minimax problem displayed by the
current SolveAll page.

## Review methods

- Line-by-line dependency audit of all definitions, lemmas, theorem proofs,
  equality examples, and ancillary SDP claims.
- Independent recomputation of both chamber certificates and all nine entries
  of each matrix identity using exact rational polynomial algebra.
- Adversarial checks of coefficient signs, chamber coverage, label
  permutations, interfaces, edges, vertices, zero variance, coincident points,
  collinear support, and rank-two support.
- Independent exact tests of the support-reduction construction on thousands
  of rational multi-support laws.
- Exact and numerical searches over rational/random laws with more than three
  support points and extreme weights.
- Clean LaTeX compilation and visual inspection of representative pages.
- Code review of every verifier check, including behavior under `python -O`.

## Core proof findings

### 1. Loss reduction: pass

The identity

```math
L_D(h)=V(D)+\|h-\mu_D\|^2
```

is used correctly. Positive and zero variance are separated before division,
and the target is exactly `q(D) <= V(D)/5`.

### 2. Weighted-law closure: pass after wording repair

Rational weights correspond exactly to finite multisets under repeatable
selection. The original text called a fixed-support stratum a "simplex face";
this was tightened to the relative interior of a coordinate face because `q`
need not be continuous when a support atom disappears. The proof only needs
fixed-support continuity, and the rational-density argument is valid there.

The weighted ratio `R(P)` and both directions in the equality of real- and
rational-weight suprema are now explicit.

### 3. Support reduction: pass

The compact feasible weight polytope preserves total mass and both mean
coordinates. Minimizing the second moment and selecting a sparsest minimizer
gives at most three positive coordinates. The two-sided nullspace perturbation,
boundary push, variance comparison, and crucial direction

```math
q(P)\le q(P')\le \frac15V(P')\le\frac15V(P)
```

are all correct. No use of the target inequality is hidden in this reduction.

### 4. Exact certificate: pass

Cases `p_2 >= 1/6` and `p_2 < 1/6` are disjoint and exhaustive after sorting.
Every listed coefficient is nonnegative in its chamber and sums to one. Both
first/second-moment computations and all matrix entries are exact. The
zero-coordinate clause covers all edges and vertices after undoing the label
permutation.

The revised text now emphasizes that the left side is a second moment about
`p`, not generally `Cov(S)`; no false assumption `E[S]=p` is made.

### 5. Deterministic extraction and upper bound: pass

Contracting the certificate with the support Gram matrix gives expected error
`V/5`. Since this is a finite probability-weighted average of legal triple
errors, one deterministic triple has error at most `V/5`. The support-reduction
chain then proves the universal upper bound.

### 6. Lower bound and equality examples: pass

The six-point construction has mean `(1/6,0)`, variance `5/36`, selected-mean
error `1/36`, and ratio `6/5`. The two-point equality classification and both
noncollinear/rank-two examples recompute exactly. The section title now makes
clear that higher-support extremizers are exhibited rather than classified.

### 7. SDP material: correct after clarification

The primal, dual, Slater argument, and planar realization are valid. The
certificate is an exact **dual-feasible** point with `r=1/5`, not necessarily a
dual optimum for every fixed `p`; for example, `p=(1/3,1/3,1/3)` has value
zero. The revised manuscript defines compression to the tangent space,
expands the global identity, handles boundary support in the dual, and supplies
the averaging step in the rank-two argument.

## Verifier changes

The supplied script's formulas were correct, but every check originally used a
Python `assert`; `python -O` could therefore print an all-passed transcript
without performing the checks. The reviewed verifier now:

- uses explicit `require(...)` failures that remain active under `python -O`;
- pins SymPy and mpmath versions in `requirements.txt`;
- checks grid-permutation structure, coefficient decompositions, the chamber
  interface, zero labels, and a zero-variance case;
- checks the rank-two equality example exactly; and
- adds 500 exact rational tests with two through six represented labels, in
  addition to the original 500 centered three-point tests.

Both normal and optimized runs match the committed expected output.

## Remaining limitations

- A finite or randomized computation is evidence, not proof of a universal
  inequality. The manuscript's analytical reductions remain essential.
- The review does not establish novelty or priority and is not an endorsement
  by the COLT authors, PMLR, or SolveAll.
- The result does not answer the broader stochastic formulation on SolveAll or
  the other regression questions in the COLT note.
- Publication should still invite independent expert review, especially of the
  support-reduction and exact-certificate sections.

## Final assessment

The revised package is internally consistent and provides a complete proof of
the stated finite-dataset theorem. No unresolved mathematical blocker remains
from this review.
