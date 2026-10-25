# Trial Data and Analysis Scope

The normalized CSV contains completed retained scientific trials from eleven studies. It excludes pilots, smoke checks, imported full-benchmark baselines, incomplete studies, and one superseded MBPP+ Muse evaluation row. The broader source exports are outside this concise package.

## Study inventory

| Study identifier | Calibration trials | Evaluation trials |
| --- | ---: | ---: |
| `bigcodebench_luna_scaling` | 1,792 | 1,728 |
| `bigcodebench_muse_scaling` | 1,792 | 1,728 |
| `mbpp_luna_scaling` | 448 | 432 |
| `mbpp_muse_scaling` | 448 | 432 |
| `zebralogic_luna_scaling` | 1,792 | 3,456 |
| `zebralogic_luna_confirmation` | 0 | 6,600 |
| `graphcolor_luna` | 0 | 1,200 |
| `graphcolor_muse` | 0 | 1,200 |
| `countdown_luna` | 0 | 1,200 |
| `bbeh_luna` | 0 | 1,200 |
| `planbench_luna` | 0 | 1,200 |
| Total | 6,272 | 20,376 |

## CSV fields

| Field | Meaning |
| --- | --- |
| `study` | Study identifier above; model versions and task sources are study-specific. |
| `split` | `calibration` or `evaluation`. |
| `task_id` | Original task identifier within a study. |
| `repetition` | Recorded repetition index; it is not a model RNG seed. |
| `budget` | Nominal study-specific charged-token ceiling or retained-debit ceiling. |
| `width` | Requested worker count. |
| `condition` | `independent` or `communicating`; communicating denotes the tested ring revision. |
| `passed` | Binary retained final outcome. It follows the original study's grader and operational conventions. |
| `recorded_tokens` | Retained charged tokens/debit, including conservative charges where applicable. |
| `active_workers` | Recorded active count in the four programming studies; blank elsewhere. |
| `retained_stage_calls` | Retained phase-call count where available; blank in the four programming studies. |
| `length_finishes` | Retained stage calls ending at the length limit, where available. |

The unique scientific key is `(study, split, task_id, repetition, budget, width, condition)`. Every non-MBPP+ configuration has two repetitions per task; MBPP+ has one. Blank fields denote unavailable measurements, not zero.

## Accounting and inference

Recorded tokens are copied from the saved charged-token/debit ledgers. They are not exact physical compute, not a uniformly completion-only allowance, and not a complete account of retries or lost-call expenditure. Twelve retained Muse BigCodeBench calibration trials exceed their nominal ceilings; no retained evaluation ledger does. That comparison concerns recorded totals only.

Each wider evaluation cell is compared with its study's shared single-worker control at the same ceiling. `delta_pp` is the accuracy difference in percentage points. `compute_ratio`, retained as a historical field name in the summary JSON, is the ratio of mean recorded tokens; it is not a physical-compute ratio.

The 176 evaluation cells comprise 28 single-worker controls and 148 wider cells. All wider cells use more recorded tokens: 75 have lower accuracy, 24 tie, and 49 improve. These are descriptive configuration counts from unequal grids sharing tasks and controls.

The paper appendix defines the paired task-bootstrap estimands. Repetitions, budgets, and configurations remain within sampled task clusters. Some studies use strata. Saved confidence intervals are present in the JSON metadata; the offline verifier checks point estimates, not those intervals. The original ZebraLogic policy contrast uses a calibration-selected fixed-width comparator, while confirmation uses communicating fixed four at the two higher ceilings. PlanBench's degenerate stratified interval has a separate unstratified sensitivity interval.

The separate 8,400-trial controlled study has no rows in this snapshot. It must not be added to these totals or described as verified by this script.

## Graph-colouring operational accounting

| Model | Attempts | Known reported tokens | Unknown-usage calls | Known cost (USD) |
| --- | ---: | ---: | ---: | ---: |
| Luna | 7,260 | 3,588,914 | 32 | 0.6709 |
| Muse Spark | 7,568 | 5,752,449 | 327 | 1.0115 |

Actual total tokens remain unknown for both models; Muse also has missing responses and unknown total cost. The attempt ledger is separate from mean retained trial debit. Seven Muse evaluation trials at the 8,192 ceiling are budget-violation failures under a post-start continuation amendment. Their `passed=0` values are operational zeros rather than direct evidence of reasoning errors. The retained-ledger ceiling check above does not override those labels or guarantee that each provider call stayed within its allocation. [graph-details.json](../evidence/graph-details.json) preserves the original accounting summaries, amendment, and seven failure keys with reported call allocations and token use. Graph-size accuracy counts can be recovered by joining its task IDs to the trial CSV.
