---
type: Skill Reference
title: Outputs
description: The outputs od-prototype-poc must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-prototype-poc` delivers a validation record that feeds the business case. It records a result, never a claim of proven value.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Prototype validation record | `assets/prototype-validation-record.md`, filled | `od-benefit-calculation`, `od-capital-request`; plant representative | Holds the question, the type, the criterion written before the build, the validator (a role), the result (passed, failed or inconclusive), the status label (mock-up, PoC or pilot) and the open items; nothing in it says "proven" |
| Click-dummy brief | `assets/click-dummy-brief.md`, written before the build | Plant representative (validator) | Filled before anyone builds; needed for a click-dummy only |
| Click-dummy and handover note | The mock-up and its handover note | Plant representative | Mock-up carries invented example values marked as such; handover document written |
| Plant confirmation of value | Written statement in the record | `od-benefit-calculation` | The plant representative has confirmed or declined the value in writing |

## Handoff

- **Also receives from:** `funnel-features`: Epic with background; At least two user stories; Handoff file.
- **Receives from:** `od-use-case-definition` (defined use case), `od-requirements-breakdown` (requirements with acceptance
  criteria), `od-data-availability-check` (a data verdict that is not "dies at step N").
- **Next in the flow:** passed: `od-benefit-calculation` (step 24) as evidence for the rows, and `od-capital-request` if
  money is needed. Failed: back to `od-use-case-definition`, or close the use case. Acceptance of a later build stays with
  `od-acceptance-test`.
- **Stops here when:** the data verdict says the data is not there, a proven library solution answers the need
  (`od-use-case-standardization`), no pass criterion or named plant validator exists, or the open question is a value
  question. A prototype answers usability and data questions only.
