---
type: Skill Reference
title: Outputs
description: The outputs od-benefit-calculation must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-benefit-calculation` delivers the value side of a business case and the saving rows behind it. Cost stays out of
it. The skill is not done until every output below exists in the stated form and its recipient can use it without asking.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Value backbone | `assets/business-case-backbone.md`, filled | `bc-assessment`, then `od-capital-request` | Expected / min / potential headline; bankable and assumption-dependent value apart; investment envelope; minimum viable rollout and maximum scale-out; every figure tagged |
| Saving rows, one per mechanism | Rows in the backbone | DBVE (owns the savings ledger) | Amount, year, category, business rationale, reliability label; a `CALCULATION` row also carries its methodology |
| Open questions and dependencies | List in the backbone | `od-decision-routing`, named owner per dependency | Every gate (for example ECR creation) recorded as a dependency with an owner |
| Assessment verdict | Verdict line in the backbone | `bc-assessment` | Written by a person other than the case builder |

## Handoff

- **Also receives from:** `od-use-case-standardization`: Standardization review; Cluster tag, baseline and plant deltas.
- **Also receives from:** `od-use-case-solution-evaluation`: Evaluation protocol; Verdict and total score.
- **Also receives from:** `funnel-features`: Epic with background; Handoff file.
- **Receives from:** `od-use-case-definition` (the scoped use case), `od-investment-input` (the cost side, kept apart from the value).
- **Next in the flow:** `bc-assessment` (step 24), then `od-capital-request` (step 25). The capital request takes the value
  rows with their firmness from here; it never recomputes them.
- **Stops here when:** the case has no sourced driver for any lever. Return the open questions to the requester; do not
  hand over a number that rests on an `[unknown]`.
