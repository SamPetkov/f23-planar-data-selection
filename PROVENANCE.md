# Provenance

## Submitted package

- Archive: `Samuil_Petkov_F23_Proof_Package (1).zip`
- Received: July 18, 2026
- SHA-256:
  `0CEDD5DE2B753DA619F8269DE8B6889655A2BE3F210C441B80C2D052544BE3B5`
- Baseline commit:
  `10ef0a8705b520f2c1ab89b9355d223681ec7a16`
- Baseline tag: `submitted-package-2026-07-18`

The baseline commit preserves the supplied file contents before mathematical
or editorial revision; files were only organized into `paper/` and
`verification/`, and the original text README was renamed
`ORIGINAL_README.txt`.

## Original archive member hashes

| File | SHA-256 |
|---|---|
| `Samuil_Petkov_F23_Detailed_Proof.tex` | `D426C68467BC43C0DA7C428710E2DF27144E54BA2A1AC5C7B134024031BE1C8B` |
| `Samuil_Petkov_F23_Detailed_Proof.pdf` | `9268966F1CDA271951585639E59BFDD951D59C3BBA89B178523DF8C3B05722D4` |
| `verify_samuil_petkov_f23.py` | `7EB8FC4B001EBCBF174242B3EC8AA27EB6816F7FA38A0563D3732E2B9667C168` |
| `verify_samuil_petkov_f23_output.txt` | `F0E9E9F184D991566FBA909728FCE288C34784B1428853B3A0C0F85D2A3D216D` |
| `Samuil_Petkov_F23_README.txt` | `325108A942849EA83C1E35200CF4A12E412755754E15A624BD3BE5C9B458077D` |

## Review changes

The `agent/review-f23-proof` branch contains:

- mathematical clarification of continuity, closure, SDP compression,
  fixed-weight optimality, and scope;
- terminology corrections that do not alter the core certificate or theorem;
- an expanded, optimization-safe exact verifier;
- a rebuilt and visually inspected PDF;
- reproducibility, CI, citation, licensing, and review documentation.

See the branch diff and `REVIEW.md` for the detailed rationale.

## Assistance disclosure

The original proof and verifier were supplied by Samuil Petkov. OpenAI Codex
assisted with proof auditing, independent computational checks, editing,
rendering, and repository preparation. Mathematical authorship and
responsibility remain with Samuil Petkov.
