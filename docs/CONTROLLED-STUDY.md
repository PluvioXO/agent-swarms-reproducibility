# Controlled Study: Supplied Summary and Coverage

This note collects the controlled-study information supplied in the manuscript abstract and schedule figure and now summarized in the paper's main text. Its reported results are accepted as supplied by the author. The separate 8,400-trial dataset, complete methods, configuration results, and interval calculations are not included in this snapshot and are not checked by `verify_results.py`. The eleven complementary studies have their own data and methods.

## Recorded design

- The abstract reports 8,400 trials on fresh arithmetic and graph-colouring tasks. The author describes graph-colouring and Countdown datasets as algorithmically generated and deterministically checkable. The exact task sets, generators, splits, and relationship to the controlled arithmetic task family remain unspecified for this experiment.
- Figure 1 tests parallel widths `N = 1, 2, 4`, with per-worker completion allowance `d` and total completion ceiling `B = N*d`.
- The diagram schedules `2*N` calls, each allowed `d/2` completion tokens, and states that all scheduled calls execute. Fixed-per-worker comparisons hold `d` constant; fixed-total comparisons hold `B` constant.
- The diagram depicts independent draft/revision, directed-ring predecessor information, and a sequential worker receiving the previous candidate and verifier feedback. It depicts verification of every candidate and retention of the first valid candidate. Precise prompts, candidate ordering, and implementation records remain unavailable.

## Results reported in the abstract

| Comparison or audit | Reported finding |
| --- | --- |
| Independent width one versus four at 4,096 completion tokens per worker | Accuracy increases by 16.0 percentage points in both task families while the total ceiling quadruples. |
| Width one versus four under a fixed 4,096-token total completion ceiling | Graph accuracy changes from 56.0% to 18.5%; the arithmetic change is inconclusive. |
| Primary comparisons against the matched sequential control | No established accuracy advantage at matched scheduled calls and nominal ceiling. |
| Ring communication | No consistent gain. |
| Candidate recovery | Finding a valid answer after an initial failure depends on the token allowance. |
| Request accounting | 97 attempts have unknown usage; the total-attempt denominator and affected-trial count have not been supplied. |

These statements do not provide configuration-level pass counts or uncertainty intervals. The earlier 2,400-trial graph-colouring study and 1,200-trial Countdown study do not supply the missing controlled-study results.

## Information still needed

Still missing are the trial inventory summing to 8,400; exact model and settings; remaining schedule, grading, and budget definitions; primary cell counts, contrasts, and interval method; recovery numerator/denominator; and the attempt denominator and treatment of unknown usage. The paper contains a concise account of the supplied protocol and headline results. Add the missing supporting details here and update the paper's summaries where necessary; missing numbers or model settings must not be inferred from the earlier studies.
