---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## The references are the substance

Each template, asset and other resource of this skill is listed here.

A use case's value is recorded as **individual saving rows**, not as one number on the
use case. Count the rows and sum the amounts live on the savings ledger (look up: the OD
savings list, owned by the DBVE) - never quote a total from memory or from this skill.

## Example

Fictional example (invented numbers, not a company figure):

If it fails: a `CALCULATION` row with no methodology fails the check and is relabelled `ESTIMATION`; an invalid or `[unknown]` factor gets no number.

## Outputs and hand-off: the text before outputs.yaml

`bc-build` delivers the value side of a business case and the saving rows behind it. Cost stays out of
it. The skill is not done until every output below exists in the stated form and its recipient can use it without asking.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Value backbone | `assets/business-case-backbone.md`, filled | `bc-assess`, then `bc-capital-request` | Expected / min / potential headline; bankable and assumption-dependent value apart; investment envelope; minimum viable rollout and maximum scale-out; every figure tagged |
| Saving rows, one per mechanism | Rows in the backbone | DBVE (owns the savings ledger) | Amount, year, category, business rationale, reliability label; a `CALCULATION` row also carries its methodology |
| Open questions and dependencies | List in the backbone | `dept-decision-rights`, named owner per dependency | Every gate (for example ECR creation) recorded as a dependency with an owner |
| Assessment verdict | Verdict line in the backbone | `bc-assess` | Written by a person other than the case builder |

## Handoff

- **Also receives from:** `catalog-standardization`: Standardization review; Cluster tag, baseline and plant deltas.
- **Also receives from:** `funnel-evaluation`: Evaluation protocol; Verdict and total score.
- **Also receives from:** `funnel-features`: Epic with background; Handoff file.
- **Also receives from:** `process-derivation` (step 23a): the change effort and the redesign effects, as evidence for the rows and never as a result.
- **Receives from:** `funnel-use-case` (the scoped use case), `bc-cost` (the cost side, kept apart from the value).
- **Next in the flow:** `bc-assess` (step 24), then `bc-capital-request` (step 25). The capital request takes the value
  rows with their firmness from here; it never recomputes them.
- **Stops here when:** the case has no sourced driver for any lever. Return the open questions to the requester; do not
  hand over a number that rests on an `[unknown]`.
