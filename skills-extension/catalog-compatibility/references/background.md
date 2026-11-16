---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Outputs and hand-off: the text before outputs.yaml

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

## Plan item and decision-rights context

- Plan item P-08 of the department's skill map.
- The decision-rights table gives the rule in one line: data-model and signal standardization (IIAE, consultation, no approval, reversible) carries the threshold "must stay consumable by every plant's instance of the capability", authority level `recommend`. This skill is how that threshold is tested instead of assumed.
- It composes, it does not repeat: `mi-signals` defines the standard signal set for one machine; `catalog-standardization` places a use case on a capability template and runs the CSP gate. This skill asks the question neither asks: does the thing still work at the plants that are not the first plant?

## Why a check is needed

- A capability is not a one-off. Each cross-plant capability template has an instance at (nearly) every plant (read the Capability Epics notes). The standard has to serve all of them.
- The plants are not uniform underneath. The grid in `plant-differences.md` shows that most plants have Siemens controllers but several also run Rockwell, Mitsubishi, Beckhoff and others, and that there are three different integration paths to the platform (IIoT Edge, central OPC UA aggregation server, "evaluation ongoing"). A name or mapping that holds for the first plant's path may not hold for another.
- The foundation data model does not fit every machine: it was found suitable for greenfield, discrete, time-series-centric machines, while brownfield and continuous processes need other models (`process-chain-practice.md`). A standard for continuous processes must be checked for fit first.
- Naming already drifts without a check: many distinct signal names for a much smaller set of concepts, several names for machine state alone (`mi-signals`). Plant languages are a further source of variance.

## Open questions

- How the "eleven cross-plant capability templates" relate to the cluster classification C01-C12 of `catalog-standardization` is not reconciled in the sources read; SKILL.md therefore says "capability" without a number.
- The skill has not yet been run against one real signal standard; the consumer inventory per capability and the COP lead time are still to collect.
