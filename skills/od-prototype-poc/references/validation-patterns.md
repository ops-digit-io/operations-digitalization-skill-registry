---
type: Skill Reference
title: Validation patterns
description: How the 29 AI business cases in the work vault define a validation plan and a pass criterion, grouped into patterns a key user can copy when writing the criterion for a prototype or PoC.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Validation patterns

Source: the "Validation Plan" and "MVP scope" fields of the 29 notes in the work vault, `Graph/Business Cases`
(SharePoint list "BusinessCasesAIatOperations", items created 2026-05-13, read 2026-11-05). All 29 carry a
validation plan; 26 state a "pass criterion" or "pass criteria"; 12 mention a pilot or prototype in it. These are
**proposed** plans in a portfolio of AI ideas, not results. None records an outcome. Use them as wording
patterns, not as evidence that a method works. The thresholds below are the cases' own proposals, not OD standards.

## Anatomy of a validation plan in these cases

Every plan names, in one to three bullets: **where** (one plant, one line, one machine family, one product family),
**how long** (6 to 8 weeks, 60 days, 90 days, 6 months), **what is built or run**, and **what passes**. Copy that shape.

## Patterns, with the case that shows each

| Pattern | Wording in the case (shortened) | Case |
|---|---|---|
| Detection quality against labels | At least 50 % recall on labeled failure events, at least 48 h lead time, false-positive rate at most 1 per asset per month | Predictive Maintenance (6-8 week pilot, 10 critical assets) |
| Expert recognition | At least 80 % of inferred states recognized as real operational states by maintenance leads | Reverse-Engineering PLC, State-Machine Mining (60-day pilot, one machine family, 3 plants) |
| Correctness checked by the plant | At least 80 % state-label correctness validated by maintenance leads at all 3 sites | State-Labeling Layer |
| Better than the current method | Deep-learning model catches at least 10 % more defects than classical vision, false-reject rate equal or lower | Vision QC (6-week pilot, one inspection station) |
| Correlation with downstream outcome | Anomaly flags correlate with downstream NOK reports at least 40 % precision, better than current SPC | Predictive Quality (8-week pilot, one line) |
| Early catch over a month | AI-SPC catches at least 3 drift events ahead of the Shewhart rule over one month at acceptable false-positive rate | SPC - Cpk AI |
| Measured at the meter | At least 10 % energy-spend reduction on the instrumented loop, verified by the plant energy meter | Energy Optimization (8-week pilot, one plant) |
| Usable without rework | At least 70 % of requirements usable without manual rewrite | AI Requirements Engineering Pipeline (one onboarding flow) |
| Adoption by users | At least 25 % of in-scope admins use it weekly after 90 days; at least 30 % of 5 engineers use it weekly | Agentic Admin Workflows; Generative PLC Engineering |
| Load and latency | Latency under 5 s at the 95th percentile at simulated full event rate | Cycle Time Optimization - Process Mining |
| Parallel run | Run the AI in parallel with the classical team; accepted by the plant team, at least 10 % throughput uplift | Generative Shopfloor Design |
| Data feasibility first | At least 60 % of historical FMEA / eCR data parseable into structured features | Production Risk Scoring |
| Count before you build | Pull the actual number of robotic cells; if under 30, defer or bundle | Generative Robot Programs |
| Business validator | Procurement team validates the ranking as actionable for next-cycle decisions | Procurement Insights from Manufacturing Data |

## What to take from them

1. **A validator who is not the builder.** Maintenance leads, the plant team, the procurement team, the energy meter.
   The prototype's author never judges it.
2. **A baseline to beat.** Classical vision, the current SPC rule, the classical layout team, the previous project.
   Without a baseline, "better" has no meaning.
3. **A false-positive or rework limit next to the hit rate.** A detector that fires too often is ignored (the
   Predictive Maintenance case names this as its key risk: alerts ignored within weeks, adoption collapses).
4. **Adoption is a pass criterion in its own right** for tools people must open (weekly use after 90 days).
5. **Some plans test feasibility, not value:** count the machines, parse the data, check the labels. That is a
   legitimate prototype step and cheaper than building.

## Pitfalls the cases themselves record

- A threshold with no source: the cases are proposals; the number is a starting point to agree with the validator,
  not a finding.
- Dependencies between cases: 14 of the 29 name another case as a prerequisite in their prerequisites field
  (for example the State-Labeling Layer before Predictive Maintenance). A prototype that needs a missing
  prerequisite should wait, or the prerequisite's own prototype comes first.
- A passed pilot is not a rollout: the Predictive Maintenance case itself plans a 30 to 50 % adoption haircut in
  year 1 and 6 to 12 months of extra work if the pilot fails its false-positive gate.

## Writing the criterion for a Lane 2 prototype

Fill four lines before any build and copy them into the validation record
([`../assets/prototype-validation-record.md`](../assets/prototype-validation-record.md)):

1. Scope: ⟨one plant, one line or machine family⟩ and a time box.
2. Measure and threshold, with a baseline to compare against.
3. Validator: a role in the plant, not the builder.
4. Decision rule: what happens on pass, on fail and on inconclusive.

For a usability click-dummy, a measure can be: the validator completes a stated task unaided (for example logging a
downtime event) in a stated number of attempts, and says in their own words what the screen is for. The cases
hold no example of this; the wording is a proposal. ⟨Agreed usability threshold⟩: OD lead with the plant.
