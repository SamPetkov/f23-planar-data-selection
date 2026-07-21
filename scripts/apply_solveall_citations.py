#!/usr/bin/env python3
from pathlib import Path


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise SystemExit(f"expected marker not found in {path}")
    if text.count(old) != 1:
        raise SystemExit(f"expected one marker in {path}, found {text.count(old)}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


tex = Path("paper/Samuil_Petkov_F23_Detailed_Proof.tex")
old_scope = (
    "The remainder of the manuscript proves this theorem.  The problem originates "
    "in the data-selection framework described in \\cite{HMSYopen,HMSYerm}.  In "
    "the source problem, a legal selection is a sequence $z_1,z_2,z_3\\in D$;"
)
new_scope = (
    "The remainder of the manuscript proves this theorem.  The finite-dataset "
    "problem originates in the data-selection framework described in "
    "\\cite{HMSYopen,HMSYerm}.  A current SolveAll listing under the same topic "
    "uses a materially different stochastic pool-selection formulation "
    "\\cite{SolveAllDataSelection}; the theorem here is not claimed as a solution "
    "of that formulation.  In the source finite-dataset problem, a legal selection "
    "is a sequence $z_1,z_2,z_3\\in D$;"
)
replace_once(tex, old_scope, new_scope)

old_bib_end = r'''\bibitem{HMSYerm}
S. Hanneke, S. Moran, A. Shlimovich, and A. Yehudayoff,
\emph{Data Selection for ERMs},
Proceedings of the 38th Conference on Learning Theory (COLT),
Proceedings of Machine Learning Research, vol. 291, pp. 2634--2665, 2025.
\url{https://proceedings.mlr.press/v291/hanneke25a.html}.

\end{thebibliography}'''
new_bib_end = r'''\bibitem{HMSYerm}
S. Hanneke, S. Moran, A. Shlimovich, and A. Yehudayoff,
\emph{Data Selection for ERMs},
Proceedings of the 38th Conference on Learning Theory (COLT),
Proceedings of Machine Learning Research, vol. 291, pp. 2634--2665, 2025.
\url{https://proceedings.mlr.press/v291/hanneke25a.html}.

\bibitem{SolveAllDataSelection}
SolveAll,
\emph{Data Selection for Regression Tasks},
open-problem listing, accessed 21 July 2026.
\url{https://www.solveall.org/problem/colt-2025-data-selection-for-regression-tasks}.

\end{thebibliography}'''
replace_once(tex, old_bib_end, new_bib_end)

readme = Path("README.md")
readme_text = readme.read_text(encoding="utf-8")
marker = "## Proof outline\n"
section = r'''## Other SolveAll-related projects

- [Right outliers with exact zero weights](https://github.com/SamPetkov/zero-atom-right-outliers) — the nonnegative zero-gap special case of the ReLU/zero-diagonal outlier problem.
- [One-factor FDR–FNR frontier](https://github.com/SamPetkov/one-factor-fdr-fnr) — a special-case result for one homogeneous rank-one Gaussian family related to the broad dependent-model FDR–FNR problem.

'''
if "## Other SolveAll-related projects" not in readme_text:
    if marker not in readme_text:
        raise SystemExit("README insertion marker not found")
    readme.write_text(readme_text.replace(marker, section + marker, 1), encoding="utf-8")

print("SolveAll citation and scope links applied.")
