---
type: Skill Reference
title: Outputs
description: The outputs deploy-acceptance must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`deploy-acceptance` delivers the filled acceptance protocol for one artefact: what "passed" means, every result, and a human
sign-off. An agent may prepare the protocol but never passes or signs it.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Acceptance test protocol | `assets/acceptance-test-protocol.md`, one per artefact, items from `assets/prefilled-test-items.md` | Plant witness, receiving owner | Drafted before the build is tested: signals or functions in scope, expected value with tolerance, the full data path to the asset the plant opens, named witness, rework loop on failure |
| Recorded results | Sections 3 and 4 of the protocol | Receiving owner | Every item's result recorded, passes included; each failure has a finding and a named rework loop |
| Sign-off | Section 5 of the protocol | `deploy-handover` | Signed by a named human on the receiving side, not the builder alone and never an agent |
| Handover readiness | Section 6 of the protocol | `deploy-handover` | Output asset, business process, utilization expectation, data path and named plant owner can be read straight off it; the old process has a named switch-off owner |
| Readiness evidence | Machine List and readiness dimension update | `mi-equipment`, IIAE | On the integration side, the readiness dimension moved with evidence; `INTEGRATED` set only after the pass |

## Handoff

- **Also receives from:** `deploy-migration`: Per-location cutover checklist.
- **Receives from:** `funnel-requirements` (requirement breakdown), `mi-signals` (signal standard), and the artefact to test from `mi-equipment` or `mi-flow` (step 3b6), or from `ops-analytics-asset`, with the plant witness.
- **Next in the flow:** `deploy-handover` (steps 3a6 and 26) on a pass. On a failure, the rework loop in the skill: equipment returns for rework, the solution goes back to step 3, or the use case returns to the integration hand-off. For `deploy-appstore`, the protocol is part of the release gate.
- **Stops here when:** any item fails, the data stops short of the asset the plant opens, no human has signed, or a dashboard disagrees with the paper record the plant trusts. Record the finding and follow the rework loop; do not retry quietly or mark a machine `INTEGRATED`.
