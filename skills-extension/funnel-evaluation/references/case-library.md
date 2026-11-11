---
type: Skill Reference
title: Case library
description: The pre-evaluation step — rank a use case against a library of known configurations before running the full four-step method, and how to grow the library with real cases.
resource: ../SKILL.md
status: stable
tags: [use-case-evaluation, maturity-model]
---
# Case library and ranking — the pre-evaluation step

Before spending time on the full four-step method, rank the use case's rough configuration
against a library of known ones. A close match means the shape is already understood — low
risk, probably standard. No close match at all is itself the finding: this is a genuinely
new configuration, and the full method (and probably `dept-decision-rights`) is worth the
time.

**This is a triage step, not a verdict.** A high case-fit score raises confidence; it never
substitutes for setting the target from the driver profile (step 1-3) or for sequencing a
real gap (step 4). Treat it the way a differential diagnosis treats "this looks like a case
we've seen" — a reason to move faster, not a reason to skip the exam.

## What is in `assets/case-library.csv`

70 rows, one per literature case from the source papers' **cold-start case base**: a
case number, its source citation, and its F1-F16 configuration (the levels that
configuration actually reached). This is **literature, not an industrial population** —
research and pilot cases published 2006-2017. Treat a close match as "a documented
configuration looks like this one," never as "many plants look like this."

**No driver ratings are recorded per case** — only the resulting configuration. The source
material preserved the solution side (what the 16 areas looked like) but not a per-case
problem profile, so ranking here compares configurations (as-is or target levels), not
driver profiles. That is also the practical case: by the time you have a configuration to
rank, you already have more to go on than a driver profile alone gives you.

## The ranking itself

`scripts/evaluate_fit.py`'s `rank_cases()`: similarity = 1 minus the mean absolute level
difference (divided by 3, the largest level span any area has), computed only over the
focus areas both the use case and the case specify. A case sharing no area with the input is
dropped from ranking entirely — it is not comparable, which is a different thing from being
dissimilar, and conflating the two would quietly make partial input look more confident than
it is.

The source papers tested eight similarity measures for this kind of ordinal-level profile
and found Goodall's measure performed best by expert judgement. This skill uses the simpler
mean-absolute-difference measure instead, for one script and no extra dependency; it will
rank the same obvious cases first and is less precise in the middle of the ranking. Prefer a
proper ordinal similarity measure if this ever needs to discriminate finely between many
close cases.

## Growing the library with real cases

The literature base is a cold start, exactly in the sense the source papers use the term:
useful before any internal case exists, and meant to be overtaken by real ones. Every time
`funnel-evaluation` runs to completion on a real use case, add its final
configuration (as-is or target, whichever is more complete) as a new row in
`assets/case-library.csv`, with its own case number continuing from 70 and its source
written as the use case's name or reference (never a person's name — role and use case
only, per this registry's own citation convention). Real rows outrank literature rows for
every purpose this step exists for; nothing in the script needs to change to prefer them —
a closer real case will simply out-rank a looser literature one on similarity alone.
