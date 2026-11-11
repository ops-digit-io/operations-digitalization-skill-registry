---
type: Skill Reference
title: Outputs
description: The outputs od-use-case-standardization must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-use-case-standardization` delivers one standardization review per use case: where it sits on the cross-plant templates, what the reference library already holds, its cluster baseline with the plant's deltas, and a CSP-readiness verdict. It recommends; the CSP decision sits outside OD.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Standardization review | `assets/standardization-review.md`, filled as the work happens, one per use case | `od-decision-routing`, `od-benefit-calculation` | Template placement, library check, cluster baseline and delta, and the CSP-readiness verdict are all filled, so neither receiver has to re-ask |
| Capability and process-group placement | Section 1 of the review | `od-decision-routing` | The use case hangs off an existing capability and process group; none was created for one plant |
| Cluster tag, baseline and plant deltas | Section 3 of the review | `od-benefit-calculation`; plant team | One classifier-assigned tag (C01-C12, never hand-edited); standard definition, KPI set and checklist pulled as baseline; only the plant's own deltas recorded |
| CSP-readiness verdict | Section 4 of the review, only for a rollout candidate | `od-decision-routing` ("standard enough to roll out" gate); CSP decision outside OD | Methods and actions are written down with evidence it works at its first plant; a blank or `No` is stated as readiness, not as rejection of the use case |

## Handoff

- **Also receives from:** `od-workshop-facilitation`: Follow-up list and summary.
- **Also receives from:** `od-event-object-modelling`: Archetype class, category, method, ETL list.
- **Receives from:** `od-portfolio-and-savings-analysis` (live use case list, adoption and conversion by region), `od-benefit-calculation` (value of the use case); the scoped use case.
- **Next in the flow:** Lane 2 step 26 (implement and graduate, with `od-handover-and-adoption` and `catalog-usecase`). The review goes to `od-decision-routing` for the rollout gate and into the business case of `od-benefit-calculation`.
- **Stops here when:** the library already holds a proven entry for the same capability (take it instead of specifying), or the only evidence of standardization is that templates exist. Count adoption and utilization, with the read date, not templates; do not treat a `No` as a rejection.
