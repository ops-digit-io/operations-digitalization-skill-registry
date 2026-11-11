---
type: Skill Reference
title: Outputs
description: The outputs catalog-compatibility must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`catalog-compatibility` delivers a verdict per plant on whether a signal standard, data model or capability solution stays consumable by every plant's instance of the capability, with a recommendation. The skill is not done until each plant in scope has one of the four verdicts.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Plant grid | In `assets/compatibility-check.md`: controller vendor, field network, ingress variant, tool versions, tag language and instance state per plant | IIAE | Every plant in scope is listed; figures relied on were refreshed from the live lists |
| Verdict per plant | In the same file | `dept-decision-rights`, IIAE | Each plant is consumable, consumable with mapping, not consumable or unknown; unknown is never rounded to consumable; each mapping is written down and owned |
| Recommendation | In the same file | `dept-decision-rights` (IIAE by consultation; COP for a data-model or connector change) | Follows the decision table; a not-consumable plant leads to a changed standard, a mapping rule or a narrowed scope, never a plant-specific branch |
| Verdict grid for the catalog | The grid, handed over when the standard feeds the catalog | `catalog-usecase` | The entry shows which plants it was checked at and which not |

## Handoff

- **Receives from:** `mi-signals` (the signal standard report) or `catalog-standardization` (the review), `mi-data-availability` (what the platform really receives per plant instance), `mi-equipment`.
- **Next in the flow:** `dept-decision-rights`, then `catalog-usecase` when the standard feeds the catalog. The skill is proposed on step 3b4 of `docs/new-state/process.yaml`.
- **Stops here when:** only the first plant's evidence exists (a proposal, not a standard), any plant is not consumable (do not recommend as "standard for all plants"), or more than a few plants are unknown (recommend only for the checked plants). The skill recommends; it does not decide the data-model change.
