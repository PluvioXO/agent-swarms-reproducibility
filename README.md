# Agent Swarms: Peer-Review Materials

Key reproducibility details for **Evaluating Agent Swarms: Token Budgets, Active Workers, and Baseline Choice**, by Maximilian Nicholson and Ayda Yazdani.

The `reproducibility-v1.3` snapshot covers **eleven complementary studies: 26,648 retained trials** (6,272 calibration and 20,376 evaluation), with 316 configuration cells. A separate controlled-study note records the supplied protocol and headline results now included in the paper. The **8,400 controlled-study trial records, complete methods, and full results are not included in this snapshot** and are outside the verifier's scope.

## Contents

| File | Purpose |
| --- | --- |
| [paper/main.pdf](paper/main.pdf) | Current extended abstract: two main pages plus references, with key findings and caveats. |
| [paper/main.tex](paper/main.tex), [paper/appendix.tex](paper/appendix.tex) | Current extended-abstract source and retained supplementary source; the appendix is not included in the current PDF. |
| [paper/agentevalsci2026-source.zip](paper/agentevalsci2026-source.zip) | Complete editable LaTeX package, including figures, template, fonts, licenses, and offline evidence check. |
| [docs/METHODS.md](docs/METHODS.md) | Grids, models, task sources, grading, and statistical methods. |
| [docs/DATA.md](docs/DATA.md) | Study counts, CSV fields, accounting, and exclusions. |
| [docs/EVALUATION-CELLS.md](docs/EVALUATION-CELLS.md) | Complete readable table of all 176 evaluation cells, moved from the PDF appendix. |
| [docs/CONTROLLED-STUDY.md](docs/CONTROLLED-STUDY.md) | Supplied controlled-study facts and explicit gaps; no inferred methods or new results. |
| [evidence/trials.csv](evidence/trials.csv) | All 26,648 normalized retained trials. |
| [evidence/cell-summary.json](evidence/cell-summary.json) | Cell aggregates, effect estimates, and saved interval metadata. |
| [evidence/provenance.json](evidence/provenance.json) | Original source-file hashes and snapshot scope. |
| [evidence/graph-details.json](evidence/graph-details.json) | The 100 shared graphs, witnesses, original hashes, attempt accounting, and seven operational-failure trial keys. |
| [evidence/study-configs.json](evidence/study-configs.json) | Seven recorded configuration objects; the four absent programming configurations are identified. |
| [verify_results.py](verify_results.py) | Offline aggregate and point-estimate checks. |

## Verify

Use Python 3.9 or later; no third-party packages, model access, credentials, or generated-code execution are required:

```sh
python3 verify_results.py
shasum -a 256 -c SHA256SUMS
```

Run Python without `-O`, because the verifier uses assertions. It checks trial keys, all 316 cell aggregates, 148 wider-cell comparisons, eleven paired point estimates, worker activation, and PlanBench truncation counts.

This concise package supports review of saved outcomes. It does not recompute confidence intervals, validate original graders, or provide complete inference replay or attempted-call accounting. Full experimental archives, provider payloads, and historical reports are not included. The current PDF includes the supplied controlled-study protocol and result summary; complete controlled-study methods, configuration results, and supporting records are not included in this snapshot. The tagged snapshot records what is available at this version; its coverage note identifies missing controlled-study records.

When citing these materials, give the paper title, authors, repository URL, and `reproducibility-v1.3` tag or exact commit. The evidence snapshot remains fixed; paper files on `main` contain the current extended abstract. The earlier full manuscript is retained in the repository history.

To rebuild the paper, download and unpack the complete source ZIP, then run `make` inside its extracted folder with XeLaTeX and BibTeX installed. The standalone `.tex` files above are provided for inspection; the ZIP contains their required assets. Upload `main.pdf` to OpenReview after the remaining controlled-study information and author fields are completed.
