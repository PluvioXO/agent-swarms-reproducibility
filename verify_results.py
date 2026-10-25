#!/usr/bin/env python3
"""Check the eleven complementary studies against their saved trial outcomes."""

import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
cells = defaultdict(list)
seen = set()
with (ROOT / "evidence/trials.csv").open(newline="") as source:
    for row in csv.DictReader(source):
        for key in ("repetition", "budget", "width", "passed", "recorded_tokens"):
            row[key] = int(row[key])
        for key in ("active_workers", "retained_stage_calls", "length_finishes"):
            row[key] = int(row[key]) if row[key] else None
        key = tuple(row[k] for k in
                    ("study", "split", "task_id", "repetition", "budget", "width", "condition"))
        assert key not in seen, ("duplicate trial", key)
        seen.add(key)
        assert row["passed"] in (0, 1) and row["recorded_tokens"] >= 0, key
        if row["active_workers"] is not None:
            assert 0 <= row["active_workers"] <= row["width"], key
        cells[(row["study"], row["split"], row["budget"], row["width"], row["condition"])].append(row)

saved = json.loads((ROOT / "evidence/cell-summary.json").read_text())
assert len(seen) == saved["included_trials"] == 26648
assert len(cells) == len(saved["cells"]) == 316
for cell in saved["cells"]:
    key = tuple(cell[k] for k in ("study", "split", "budget", "width", "condition"))
    rows = cells[key]
    assert len(rows) == cell["trials"], key
    assert sum(r["passed"] for r in rows) == cell["passed"], key
    tokens = sum(r["recorded_tokens"] for r in rows) / len(rows)
    assert math.isclose(tokens, cell["mean_tokens"], abs_tol=1e-7), key
    if cell["mean_active"] is not None:
        assert math.isclose(sum(r["active_workers"] for r in rows) / len(rows),
                            cell["mean_active"], abs_tol=1e-7), key

evaluation = [c for c in saved["cells"] if c["split"] == "evaluation"]
wider = [c for c in evaluation if c["width"] > 1]
assert len(evaluation) == saved["evaluation_cells"] == 176
assert sum(c["trials"] for c in evaluation) == 20376
assert len(wider) == 148 and len(evaluation) - len(wider) == 28
counts = Counter()
for cell in wider:
    baseline = next(c for c in evaluation if c["study"] == cell["study"]
                    and c["budget"] == cell["budget"] and c["width"] == 1)
    delta = 100 * (cell["passed"] / cell["trials"] - baseline["passed"] / baseline["trials"])
    ratio = cell["mean_tokens"] / baseline["mean_tokens"]
    assert math.isclose(delta, cell["delta_pp"], abs_tol=1e-7)
    assert math.isclose(ratio, cell["compute_ratio"], abs_tol=1e-7)
    counts["equal_accuracy" if abs(delta) < 1e-8 else
           "higher_accuracy" if delta > 0 else "lower_accuracy"] += 1
    counts["higher_recorded_token_use"] += int(ratio > 1)
assert dict(counts) == saved["descriptive_evaluation_counts"]
assert counts["lower_accuracy"] + counts["equal_accuracy"] == 99
programming = [c for c in wider if c["study"].startswith(("bigcodebench", "mbpp"))]
assert len(programming) == 96 and sum(c["delta_pp"] <= 1e-8 for c in programming) == 81

for budget, expected_passes, expected_lengths in ((8192, 0, 1599), (16384, 200, 3)):
    rows = cells[("planbench_luna", "evaluation", budget, 4, "independent")]
    assert sum(r["passed"] for r in rows) == expected_passes
    assert sum(r["retained_stage_calls"] for r in rows) == 1600
    assert sum(r["length_finishes"] for r in rows) == expected_lengths
for budget, expected_rate in ((32768, 7.3), (65536, 45.3), (131072, 93.5)):
    rows = [r for key, group in cells.items() for r in group if
            key[0] == "bigcodebench_muse_scaling" and key[1] == "evaluation"
            and key[2] == budget and key[3] == 16]
    assert round(100 * sum(r["active_workers"] for r in rows) / (16 * len(rows)), 1) == expected_rate

for contrast in saved["paired_contrasts"]:
    study = contrast["study"]
    if contrast["contrast"] == "ring minus independent":
        differences = []
        for cell in evaluation:
            if cell["study"] != study or cell["condition"] != "communicating":
                continue
            control = next(c for c in evaluation if c["study"] == study
                           and c["budget"] == cell["budget"] and c["width"] == cell["width"]
                           and c["condition"] == "independent")
            differences.append(100 * (cell["accuracy"] - control["accuracy"]))
    else:
        policies = (("independent", (2, 2, 2)), ("communicating", (4, 8, 16)))
        differences = []
        for condition, widths in policies:
            for budget, width in zip((32768, 65536, 131072), widths):
                if study.endswith("confirmation") and (condition != "communicating" or budget == 32768):
                    continue
                baseline_width = 4 if study.endswith("confirmation") else 1
                def accuracy(n):
                    rows = cells[(study, "evaluation", budget, n,
                                  "independent" if n == 1 else condition)]
                    return sum(r["passed"] for r in rows) / len(rows)
                differences.append(100 * (accuracy(width) - accuracy(baseline_width)))
    assert math.isclose(sum(differences) / len(differences), contrast["mean_pp"], abs_tol=1e-7), study

overruns = Counter(r["split"] for rows in cells.values() for r in rows
                   if r["recorded_tokens"] > r["budget"])
assert overruns == {"calibration": 12}

print("Verified 26,648 unique retained trials, 316 cells, 176 evaluation cells,")
print("all 148 wider comparisons, 11 paired estimates, activation and truncation counts.")
print("Saved confidence intervals are documented metadata, not recomputed here.")
