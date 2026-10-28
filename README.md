# Agent Swarms: Peer-Review Materials

Key reproducibility details for **Evaluating Agent Swarms: Token Budgets, Active Workers, and Baseline Choice**, by Maximilian Nicholson and Ayda Yazdani.

The current extended abstract analyses **eleven studies: 26,648 retained trials** (6,272 calibration and 20,376 evaluation), with 316 configuration cells across seven task families. The scientific trials and saved estimates are unchanged from the `reproducibility-v1.3` evidence snapshot. Current manuscript files are on `main`; earlier versions remain in repository history. The paper contributes an empirical audit of execution feasibility, realized worker participation and baseline choice in agent-scaling comparisons.

## Contents

| File | Purpose |
| --- | --- |
| [paper/main.pdf](paper/main.pdf) | Self-contained extended abstract: two main pages plus references; quotations and architecture Figure 1 on page 1, compact three-panel results Figure 2 in the body; no appendix. |
| [paper/main.tex](paper/main.tex) | Current extended-abstract source. |
| [paper/agentevalsci2026-source.zip](paper/agentevalsci2026-source.zip) | Complete editable LaTeX package, including the vector architecture and results sources, template, fonts, licenses and offline evidence check. |
| [docs/METHODS.md](docs/METHODS.md) | Grids, models, task sources, output selection and statistical methods. |
| [docs/DATA.md](docs/DATA.md) | Study counts, CSV fields, accounting and exclusions. |
| [docs/EVALUATION-CELLS.md](docs/EVALUATION-CELLS.md) | Complete readable table of all 176 evaluation cells. |
| [evidence/trials.csv](evidence/trials.csv) | All 26,648 normalized retained trials. |
| [evidence/cell-summary.json](evidence/cell-summary.json) | Cell aggregates, effect estimates and saved interval metadata. |
| [evidence/provenance.json](evidence/provenance.json) | Original source-file hashes and publication scope. |
| [evidence/graph-details.json](evidence/graph-details.json) | The 100 shared graphs, witnesses, original hashes, attempt accounting and seven operational-failure trial keys. |
| [evidence/study-configs.json](evidence/study-configs.json) | Seven recorded configuration objects; the four absent programming configurations are identified. |
| [verify_results.py](verify_results.py) | Offline aggregate and point-estimate checks. |

## Verify

Use Python 3.9 or later; no third-party packages, model access, credentials or generated-code execution are required:

```sh
python3 verify_results.py
shasum -a 256 -c SHA256SUMS
```

Run Python without `-O`, because the verifier uses assertions. It checks trial keys, all 316 cell aggregates, 148 wider-cell comparisons, eleven paired point estimates, worker activation and PlanBench truncation counts.

This concise package supports review of saved outcomes. It does not recompute confidence intervals, validate original graders, or provide complete inference replay or attempted-call accounting. Full experimental archives, provider payloads and historical reports are outside this package. Methods and data notes identify unavailable measurements and configurations without inferring them.

Cite the paper title, authors, repository URL and the exact commit used. The `reproducibility-v1.3` tag preserves the earlier evidence snapshot; manuscript files on `main` contain the current version.

To rebuild the paper, unpack the complete source ZIP, then run `make` with XeLaTeX, BibTeX and latexmk installed. The ZIP contains the figure, font and template inputs required by the standalone TeX source. OpenReview takes `main.pdf`; submission metadata and author fields are supplied separately in the ZIP. Nothing has been submitted by this workflow.
