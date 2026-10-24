---
type: Skill Reference
title: Regional handling
description: Why the three regions are never blended into one conversion figure, and what to report instead.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [practice, use-case-support-service, analytical-support-service]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Regional handling

PMI's portfolio-balancing step exists because a portfolio is not one thing to optimize
uniformly — it is organized into categories that each carry their own goal and are
measured on their own basis, then balanced against each other. Region is this estate's
clearest case of that: the three regions are not scaled copies of one portfolio, they are
three different situations.

## The numbers, stated once and never recomputed

| Region | Use cases | Productive | Conversion |
|---|--:|--:|---|
| Europe | 312 | 81 | 26 % |
| Americas | 168 | 70 | **42 % — best in the estate** |
| Asia | 138 | 16 | 12 % |

(Same figures as `SKILL.md` and `od-use-case-standardization` — this file explains how to
use them, not a second computation of them.)

## The rule

**Never produce one blended conversion rate across regions.** A single global percentage
(simple average 26.7 %, or weighted 29.3 % across 618 use cases) hides that Asia's
situation (12 %) is not "a bit behind" Europe's (26 %) — it is a different problem with a
different cause, and a plan written against the blended number will under-invest in
fixing it.

If a single portfolio-health number is demanded for a deck or a board paper, report it
**alongside**, never instead of, the regional table, with one sentence naming which region
is driving it up or down. "Overall conversion 27 %, driven down by Asia at 12 % against
Europe's 26 % and the Americas' 42 %" is the form that survives a follow-up question.

## What is worth asking, per region

- **Asia (12 %):** the gap is not "needs more time" by default — treat it as its own
  investigation (local IT capability, plant engagement, whether the standard templates
  actually fit the region's machine estate) rather than assuming the same fix that works
  in Europe applies.
- **Americas (42 %):** the best conversion rate in the estate is itself a finding — what is
  different there (process, staffing, plant engagement) is worth naming explicitly rather
  than treated as unremarkable, because it is the nearest thing this portfolio has to a
  proven playbook for the other two regions.
- **Europe (26 %):** the largest base (312 use cases) at a middling rate — the volume that
  moves the global number most, and the region where a small percentage-point gain has the
  largest absolute effect.

## Applying this in a rollup

Any table in `assets/portfolio-review-protocol.md` that cuts by region keeps the three
rows separate through every later aggregation step; a plant- or capability-level view
still carries its region as a column, not as a filter applied once and then dropped.
