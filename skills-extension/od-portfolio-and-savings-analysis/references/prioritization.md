---
type: Skill Reference
title: Prioritization
description: A weighted-scoring method for ranking use cases in a portfolio review, and the honest bucket for the ones that cannot be scored at all.
resource: ../SKILL.md
status: stable
tags: [practice, use-case-support-service, analytical-support-service]
---
# Prioritization

A weighted scoring model is the right tool here for the same reason it is the standard
choice for any capped-budget, governance-reviewed ranking: it forces the weighting
argument to happen once, explicitly, instead of being re-litigated use case by use case. A
value-vs-effort matrix (the two-axis simplification of the same idea) is the quick view for
a round; the weighted score is what the ranking actually rests on.

## The two axes

**Value** — from fields this estate already records, never invented for the exercise:

- Tracked savings amount (`od-benefit-calculation`), weighted down if `ESTIMATION` or
  unrecorded rather than `CALCULATION` — an unreliable number should rank below a smaller
  reliable one, not above it on face value alone.
- Strategic-plant alignment and roadmap link (`od-use-case-intake-triage`'s own admission
  criteria — a use case already has to clear this bar to exist in the portfolio at all).
- Standardization leverage: a use case against a capability with an existing proven library
  entry (`od-use-case-standardization`) scores higher than a bespoke build, because the
  second plant's cost of adoption is close to zero once one plant has it working.

**Effort** — from fields this estate already records:

- Named dependencies and their owner (`od-benefit-calculation`'s dependency field — `ECR
  APPROVAL`, `MACHINE INTEGRATION` and the rest are effort, stated plainly).
- Known blockers logged against the use case or its machine.
- Category: `non-standard, unique to one plant` carries more effort by definition than a
  `standard, cross process` instance of an existing capability.

## The bucket a score must not hide: unscoreable

Many use cases carry `UNKNOWN` priority or `UNKNOWN` potential (count them live and quote the date). **A use
case with no value field populated is not a zero-value use case — it is unscored**, and
belongs in a separate bucket reported alongside the ranked list, not blended into it at the
bottom. Forcing a score onto it (defaulting blanks to zero, or to the scale's midpoint)
manufactures a ranking the input data does not support, and `od-use-case-standardization`'s
own point about C12 "Other" applies here too: a rising unscoreable bucket is a data-quality
signal, not a finding about those use cases' worth.

## Worked example (illustrative) — one quadrant read correctly

A `standard, cross process` OEE-capability use case with a `CALCULATION` tracked saving of
<amount>/year, roadmap-linked at a strategic plant, one dependency (`ECR APPROVAL`, owner
named): **high value, low-to-medium effort** — a quick win, prioritized ahead of a
`non-standard` use case with a larger but `ESTIMATION`-only saving and three unresolved
blockers, which is **high value on paper, high effort in practice** — paced, not dropped,
and flagged for whoever owns its blockers.

## How this feeds a review round

Rank only within a category (standard vs. non-standard, region) before comparing across
them — the same rule `rollup-method.md` states for euros applies to rank. A single
portfolio-wide ranked list that puts the use cases of a low-conversion region beside those of a
high-conversion region on one axis manufactures a comparison the regional-handling reference forbids.
