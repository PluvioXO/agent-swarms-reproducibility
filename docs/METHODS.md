# Methods for the Eleven Complementary Studies

These notes summarize the current paper's appendices. They describe the retained experiments, not the separate 8,400-trial controlled study.

## Design and models

BigCodeBench, MBPP+, and the original ZebraLogic study use calibration ceilings of 8,192/16,384/32,768/65,536 tokens at widths 1/2/4/8. Evaluation uses 32,768/65,536/131,072 at widths 1/2/4/8/16. Independent and ring conditions share the single-worker control: seven calibration and nine evaluation cells per ceiling. Draft, revision, and model integration receive nominal shares of 50%/25%/25%; worker shares divide across the requested width. Prompt costs and minimum output reserves can prevent calls from launching.

Graph colouring uses ceilings 4,096/8,192; Countdown, BBEH, and PlanBench use 8,192/16,384. Each compares independent width one, independent width four, and ring width four. Draft/revision split the allowance 50%/50%, without model integration. Ring revision receives the predecessor's draft; independent revision receives its own. BBEH and PlanBench predecessor excerpts are capped at 512 estimated tokens.

BigCodeBench Luna records `gpt-5.6-luna`; later Luna studies request `openai/gpt-6-luna` through OpenRouter, generally with low reasoning and requested Flex service. Muse records `meta/muse-spark-1.3-contributor`. Sampling and routing vary by study; the graph-colouring Muse runner uses default reasoning and no requested service tier. These are not one experiment with uniform model/provider settings. Activation is recorded only for the four programming studies.

Calibration and evaluation tasks are distinct within the original studies. BigCodeBench uses 32 tasks per split, MBPP+ 16 per split, and original ZebraLogic 32 calibration/64 evaluation. Every non-MBPP+ cell has two repetitions per task; MBPP+ has one. The graph studies reuse tasks across models.

## Tasks and final scoring

| Family | Task source and final criterion |
| --- | --- |
| BigCodeBench | Model-integrated final code; saved sandbox test result, without hidden-test feedback to workers. |
| MBPP+ | Model-integrated final code; base and EvalPlus tests. |
| ZebraLogic | Model-integrated answer; normalized whole-grid exact correctness. Malformed or empty grids fail. |
| Graph colouring | 100 local greedy-solvable three-colour graphs; vertex counts 10/12/14/16/18, edge probability 0.2, generator seed 20260928. First valid revision in worker order, otherwise first nonempty revision; no draft rescue. This is a local adaptation inspired by Reasoning Gym. |
| Countdown | 100 custom puzzles with four to eight supplied numbers; verifier-assisted selection checks arithmetic constraints and target match. |
| BBEH | 25 tasks each from disambiguation QA, multistep arithmetic, spatial reasoning, and time arithmetic. Gold-blind normalized-answer plurality with worker-order ties, followed by local exact/fuzzy grading. |
| PlanBench | 100 Blocksworld Hard instances; first valid revision in worker order under a local STRIPS interpreter. Optimality is not required. |

Pinned task sources: [ZebraLogic grid_mode](https://huggingface.co/datasets/WildEval/ZebraLogic/tree/0a473f5a0054835754ed156d5a79c6ce27178bb1), revision `0a473f5a0054835754ed156d5a79c6ce27178bb1`; [BBEH](https://github.com/google-deepmind/bbeh/tree/80d12ca916b7158f22293fcf3144f4d3d854d4be), revision `80d12ca916b7158f22293fcf3144f4d3d854d4be`; [PlanBench](https://github.com/harshakokel/PlanBench/tree/1f4d600f4806bedbefebbbe44b168372aaf5060d), revision `1f4d600f4806bedbefebbbe44b168372aaf5060d`.

The original ZebraLogic selected-width policies are independent 2/2/2 and ring 4/8/16 across evaluation ceilings, compared with calibration-selected fixed width one. Confirmation transfers ring 4/8/16 without refitting to 300 unused puzzles (12 per size stratum), yielding eleven deduplicated cells and 6,600 trials. Its primary contrast averages ring eight minus ring four at 65,536 and ring sixteen minus ring four at 131,072; it uses a different comparator from the original study.

## Statistics and limits

Accuracy differences and token ratios use the same study and ceiling's shared single-worker control. Communication contrasts average evaluated multi-worker widths, ceilings, and repetitions; ZebraLogic instead uses the policy contrasts above. Repeated trials and shared controls are not independent task samples.

Bootstrap sampling retains each task's configurations and repetitions together. Programming communication intervals use 20,000 paired task draws, seed 20260921; original ZebraLogic uses 4,000, seed 20260926 in manifest task order; confirmation uses 10,000 size-stratified draws, seed 20260927. The smaller diagnostic studies use 10,000 paired draws stratified by graph size, Countdown size, BBEH category, or PlanBench object count. Per-budget BBEH/PlanBench width contrasts use 20,000 paired within-stratum draws.

PlanBench's singleton seven-object stratum yields a degenerate [0.25, 0.25] percentage-point communication interval. The post-hoc unstratified sensitivity uses 50,000 paired draws, seed 20260929, giving [0.00, 0.75]. Intervals are study-specific; there is no pooled meta-analysis or cross-study multiplicity correction. Saved intervals are metadata, not recomputed by the verifier.

Tokens are recorded charges/debits, including estimates or conservative unknown-usage charges where applicable. They do not measure exact compute or all attempted calls. Original ZebraLogic had protocol/retry amendments and seven abandoned whole-trial attempts; confirmation added an upstream-503 retry amendment after 1,496 trials. The studies are not uniformly preregistered. Pilots, smoke checks, imported baselines, incomplete studies, and one superseded MBPP+ Muse row are excluded; see [DATA.md](DATA.md) and the paper for scope and accounting.
