---
type: Skill Reference
title: Validation patterns
description: How the AI business cases in the department knowledge base define a validation plan and a pass criterion, grouped into wording patterns a key user can copy when writing the criterion for a prototype or PoC - patterns only, with placeholder thresholds.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Validation patterns

Source: the "Validation Plan" and "MVP scope" fields of the notes in the department knowledge base, `Graph/Business Cases` (SharePoint list
"BusinessCasesAIatOperations"). Almost every case carries a validation plan and most state a "pass criterion". These are
**proposed** plans in a portfolio of AI ideas, not results. None records an outcome. Use them as wording patterns, not as
evidence that a method works. Re-read the list for the current wording; this file carries no case counts and only
placeholder thresholds: every `<threshold>` is agreed with the validator for the case at hand.

## Anatomy of a validation plan in these cases

Every plan names, in one to three bullets: **where** (one plant, one line, one machine family, one product family),
**how long** (a time box), **what is built or run**, and **what passes**. Copy that shape.

## Patterns

| Pattern | Wording shape | Typical use |
|---|---|---|
| Detection quality against labels | At least `<recall>` on labeled failure events, at least `<lead time>` warning, false-positive rate at most `<rate>` per asset per period | Predictive maintenance |
| Expert recognition | At least `<share>` of inferred states recognized as real operational states by maintenance leads | State-machine mining from PLC code |
| Correctness checked by the plant | At least `<share>` label correctness validated by maintenance leads at the pilot sites | State labeling |
| Better than the current method | New model catches at least `<delta>` more defects than the classical method, false-reject rate equal or lower | Vision quality control |
| Correlation with downstream outcome | Anomaly flags correlate with downstream NOK reports at `<precision>`, better than the current SPC rule | Predictive quality |
| Early catch over a period | AI-SPC catches at least `<n>` drift events ahead of the classical rule over a stated period at an acceptable false-positive rate | SPC / Cpk |
| Measured at the meter | At least `<reduction>` reduction on the instrumented loop, verified by the plant meter | Energy optimization |
| Usable without rework | At least `<share>` of generated requirements usable without manual rewrite | Requirements engineering pipeline |
| Adoption by users | At least `<share>` of in-scope users use it weekly after `<period>` | Admin and engineering tools |
| Load and latency | Latency under `<limit>` at the 95th percentile at simulated full event rate | Process mining at scale |
| Parallel run | Run the AI in parallel with the classical team; accepted by the plant team, at least `<uplift>` throughput uplift | Generative shopfloor design |
| Data feasibility first | At least `<share>` of historical data parseable into structured features | Risk scoring |
| Count before you build | Pull the actual number of the thing (cells, machines); if under `<n>`, defer or bundle | Any case whose value depends on volume |
| Business validator | The business team validates the ranking as actionable for next-cycle decisions | Insight and ranking products |

## What to take from them

1. **A validator who is not the builder.** Maintenance leads, the plant team, the procurement team, the energy meter.
   The prototype's author never judges it.
2. **A baseline to beat.** Classical vision, the current SPC rule, the classical layout team, the previous project.
   Without a baseline, "better" has no meaning.
3. **A false-positive or rework limit next to the hit rate.** A detector that fires too often is ignored (a recurring
   key risk named in predictive-maintenance cases: alerts ignored within weeks, adoption collapses).
4. **Adoption is a pass criterion in its own right** for tools people must open (weekly use after a stated period).
5. **Some plans test feasibility, not value:** count the machines, parse the data, check the labels. That is a
   legitimate prototype step and cheaper than building.

## Pitfalls the cases themselves record

- A threshold with no source: the cases are proposals; the number is a starting point to agree with the validator,
  not a finding.
- Dependencies between cases: several name another case as a prerequisite in their prerequisites field (for example a
  state-labeling layer before predictive maintenance). A prototype that needs a missing prerequisite should wait, or
  the prerequisite's own prototype comes first. Count the dependencies live on the list before planning a sequence.
- A passed pilot is not a rollout: expect an adoption haircut in year 1 and extra work if the pilot fails its
  false-positive gate; read the case's own assumptions.

## Writing the criterion for a Lane 2 prototype

Fill four lines before any build and copy them into the validation record
(`../assets/prototype-validation-record.md`):

1. Scope: ⟨one plant, one line or machine family⟩ and a time box.
2. Measure and threshold, with a baseline to compare against.
3. Validator: a role in the plant, not the builder.
4. Decision rule: what happens on pass, on fail and on inconclusive.

For a usability click-dummy, a measure can be: the validator completes a stated task unaided (for example logging a
downtime event) in a stated number of attempts, and says in their own words what the screen is for. The cases
hold no example of this; the wording is a proposal. ⟨Agreed usability threshold⟩: OD lead with the plant.
