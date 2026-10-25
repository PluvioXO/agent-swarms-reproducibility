# Agent Swarms: Peer-Review Materials

Key reproducibility details for **Evaluating Agent Swarms: Token Budgets, Active Workers, and Baseline Choice**, by Maximilian Nicholson and Ayda Yazdani.

The `reproducibility-v1.1` snapshot covers **eleven complementary studies: 26,648 retained trials** (6,272 calibration and 20,376 evaluation), with 316 configuration cells. The separate **8,400-trial controlled study is not included**; its methods, results, and trial records remain pending.

## Contents

| File | Purpose |
| --- | --- |
| [paper/main.pdf](paper/main.pdf) | Current manuscript; detailed protocols and all evaluation cells are in the appendices. |
| [docs/METHODS.md](docs/METHODS.md) | Grids, models, task sources, grading, and statistical methods. |
| [docs/DATA.md](docs/DATA.md) | Study counts, CSV fields, accounting, and exclusions. |
| [evidence/trials.csv](evidence/trials.csv) | All 26,648 normalized retained trials. |
| [evidence/cell-summary.json](evidence/cell-summary.json) | Cell aggregates, effect estimates, and saved interval metadata. |
| [evidence/provenance.json](evidence/provenance.json) | Original source-file hashes and snapshot scope. |
| [verify_results.py](verify_results.py) | Offline aggregate and point-estimate checks. |

## Verify

Use Python 3.9 or later; no third-party packages, model access, credentials, or generated-code execution are required:

```sh
python3 verify_results.py
shasum -a 256 -c SHA256SUMS
```

Run Python without `-O`, because the verifier uses assertions. It checks trial keys, all 316 cell aggregates, 148 wider-cell comparisons, eleven paired point estimates, worker activation, and PlanBench truncation counts.

This concise package supports review of saved outcomes. It does not recompute confidence intervals, validate original graders, or provide complete inference replay or attempted-call accounting. Full archives, provider payloads, and historical reports are not included. The current PDF remains a working draft pending the controlled-study methods and results.

When citing these materials, give the paper title, authors, repository URL, and `reproducibility-v1.1` tag or exact commit.
