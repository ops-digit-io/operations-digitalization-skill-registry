---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Where it sits

Lane 2 runs definition, features and data check, **prototype / validate**, business case, capital request,
implement and graduate (`docs/new-state-flow.md`). This step comes after `funnel-use-case`,
`funnel-requirements` and `mi-data-availability`, and before `bc-build`. The flow
marks it as touched by both human and agent: an agent can draft the mock-up and the record, the plant says
whether it shows what they need.

## Outputs and hand-off: the text before outputs.yaml

`funnel-prototype` delivers a validation record that feeds the business case. It records a result, never a claim of proven value.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Prototype validation record | `assets/prototype-validation-record.md`, filled | `process-derivation`, `bc-build`, `bc-capital-request`; plant representative | Holds the question, the type, the criterion written before the build, the validator (a role), the result (passed, failed or inconclusive), the status label (mock-up, PoC or pilot) and the open items; nothing in it says "proven" |
| Click-dummy brief | `assets/click-dummy-brief.md`, written before the build | Plant representative (validator) | Filled before anyone builds; needed for a click-dummy only |
| Click-dummy and handover note | The mock-up and its handover note | Plant representative | Mock-up carries invented example values marked as such; handover document written |
| Plant confirmation of value | Written statement in the record | `bc-build` | The plant representative has confirmed or declined the value in writing |

## Handoff

- **Also receives from:** `funnel-features`: Epic with background; At least two user stories; Handoff file.
- **Receives from:** `funnel-use-case` (defined use case), `funnel-requirements` (requirements with acceptance
  criteria), `mi-data-availability` (a data verdict that is not "dies at step N").
- **Next in the flow:** passed: `process-derivation` (step 23a) derives the process, then `bc-build` (step 24) takes the evidence for the rows, and `bc-capital-request` if
  money is needed. Failed: back to `funnel-use-case`, or close the use case. Acceptance of a later build stays with
  `deploy-acceptance`.
- **Stops here when:** the data verdict says the data is not there, a proven library solution answers the need
  (`catalog-standardization`), no pass criterion or named plant validator exists, or the open question is a value
  question. A prototype answers usability and data questions only.

## Status and provenance (moved from SKILL.md)

The new-state flow lists "Prototype / validate" (Lane 2, step 3) as a thin spot. It credits `ops-analytics-asset` with "click-dummy only", but that skill has no prototype, click-dummy or proof-of-concept content (`docs/new-state-conformance.md`). This skill rests on what the knowledge base holds: one AI pilot (the Gemba App), PoC labels in two AI decks, business cases that each carry a validation plan, and the dashboard specs. It is not a validated OD method.

## Which steps rest on what

| Steps | Basis as stated in the skill and its references |
|---|---|
| 6 (click-dummy build) | The department package click-dummy master (`references/click-dummy.md`); the Gemba App pilot for the AI-generated mock-up from a brief |
| 5 (pass criterion) | Validation plans in the AI business cases (`references/validation-patterns.md`) |
| 1-4, 7-9 | Registry synthesis (marked PROPOSAL in `references/process-chain-practice.md`); not tested on a real run |

## Open questions

- No validated run of this procedure on a real use case yet; one run would allow lifting the "not validated" disclaimer.
- Which steps beyond the Gemba pilot the plant would accept as standard is not confirmed.
