---
type: Skill Reference
title: Regional handling
description: Why the three regions are never blended into one conversion figure, and what to report instead. Method only - read the regional figures live.
resource: ../SKILL.md
status: stable
tags: [practice, use-case-support-service, analytical-support-service]
---
# Regional handling

PMI's portfolio-balancing step exists because a portfolio is not one thing to optimize
uniformly — it is organized into categories that each carry their own goal and are
measured on their own basis, then balanced against each other. Region is this estate's
clearest case of that: the three regions (Europe, Americas, Asia) are not scaled copies of
one portfolio, they are three different situations.

## How to obtain the regional table

No regional figure is stored in this skill. Build the table live from the use case list
(`know-sharepoint-export`), with the capture date:

| Region | Use cases (all) | Productive | Conversion (productive / all) |
|---|--:|--:|---|
| Europe | ⟨n⟩ | ⟨n⟩ | ⟨%⟩ |
| Americas | ⟨n⟩ | ⟨n⟩ | ⟨%⟩ |
| Asia | ⟨n⟩ | ⟨n⟩ | ⟨%⟩ |

Name the denominator on every rate. Exclude or report separately any use case without a
region, and say how many.

## The rule

**Never produce one blended conversion rate across regions.** A single global percentage
(simple average or weighted) hides that one region's situation is not "a bit behind"
another's — it can be a different problem with a different cause, and a plan written
against the blended number will under-invest in fixing it. Simple and weighted averages also
differ; if you must quote one, say which.

If a single portfolio-health number is demanded for a deck or a board paper, report it
**alongside**, never instead of, the regional table, with one sentence naming which region
is driving it up or down. The form that survives a follow-up question is: "Overall
conversion <x>, driven down by <region> at <y> against <region> at <z>."

## What is worth asking, per region

- **The lowest-converting region:** the gap is not "needs more time" by default — treat it
  as its own investigation (local IT capability, plant engagement, whether the standard
  templates actually fit the region's machine estate) rather than assuming the same fix
  that works elsewhere applies.
- **The highest-converting region:** that rate is itself a finding — what is different there
  (process, staffing, plant engagement) is worth naming explicitly rather than treated as
  unremarkable, because it is the nearest thing this portfolio has to a proven playbook for
  the other regions.
- **The region with the largest base:** the volume that moves the global number most, and
  the region where a small percentage-point gain has the largest absolute effect.

## Applying this in a rollup

Any table in `assets/portfolio-review-protocol.md` that cuts by region keeps the three
rows separate through every later aggregation step; a plant- or capability-level view
still carries its region as a column, not as a filter applied once and then dropped.
