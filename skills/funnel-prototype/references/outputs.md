---
type: Skill Reference
title: Outputs
description: The outputs funnel-prototype must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`funnel-prototype` delivers a validation record that feeds the business case. It records a result, never a claim of proven value.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Prototype validation record | `assets/prototype-validation-record.md`, filled | `bc-build`, `bc-capital-request`; plant representative | Holds the question, the type, the criterion written before the build, the validator (a role), the result (passed, failed or inconclusive), the status label (mock-up, PoC or pilot) and the open items; nothing in it says "proven" |
| Click-dummy brief | `assets/click-dummy-brief.md`, written before the build | Plant representative (validator) | Filled before anyone builds; needed for a click-dummy only |
| Click-dummy and handover note | The mock-up and its handover note | Plant representative | Mock-up carries invented example values marked as such; handover document written |
| Plant confirmation of value | Written statement in the record | `bc-build` | The plant representative has confirmed or declined the value in writing |

## Handoff

- **Also receives from:** `funnel-features`: Epic with background; At least two user stories; Handoff file.
- **Receives from:** `funnel-use-case` (defined use case), `funnel-requirements` (requirements with acceptance
  criteria), `mi-data-availability` (a data verdict that is not "dies at step N").
- **Next in the flow:** passed: `bc-build` (step 24) as evidence for the rows, and `bc-capital-request` if
  money is needed. Failed: back to `funnel-use-case`, or close the use case. Acceptance of a later build stays with
  `deploy-acceptance`.
- **Stops here when:** the data verdict says the data is not there, a proven library solution answers the need
  (`catalog-standardization`), no pass criterion or named plant validator exists, or the open question is a value
  question. A prototype answers usability and data questions only.
