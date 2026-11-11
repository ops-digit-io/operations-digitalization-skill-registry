---
type: Skill Reference
title: Outputs
description: The outputs od-acceptance-test must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-acceptance-test` delivers the filled acceptance protocol for one artefact: what "passed" means, every result, and a human
sign-off. An agent may prepare the protocol but never passes or signs it.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Acceptance test protocol | `assets/acceptance-test-protocol.md`, one per artefact, items from `assets/prefilled-test-items.md` | Plant witness, receiving owner | Drafted before the build is tested: signals or functions in scope, expected value with tolerance, the full data path to the asset the plant opens, named witness, rework loop on failure |
| Recorded results | Sections 3 and 4 of the protocol | Receiving owner | Every item's result recorded, passes included; each failure has a finding and a named rework loop |
| Sign-off | Section 5 of the protocol | `od-handover-and-adoption` | Signed by a named human on the receiving side, not the builder alone and never an agent |
| Handover readiness | Section 6 of the protocol | `od-handover-and-adoption` | Output asset, business process, utilization expectation, data path and named plant owner can be read straight off it; the old process has a named switch-off owner |
| Readiness evidence | Machine List and readiness dimension update | `od-equipment-integration`, IIAE | On the integration side, the readiness dimension moved with evidence; `INTEGRATED` set only after the pass |

## Handoff

- **Also receives from:** `od-migration-cutover`: Per-location cutover checklist.
- **Receives from:** `od-requirements-breakdown` (requirement breakdown), `od-signal-standardization` (signal standard), and the artefact to test from `od-equipment-integration` or `od-node-red-flow-builder` (step 3b6), or from `od-analytics-asset-build`, with the plant witness.
- **Next in the flow:** `od-handover-and-adoption` (steps 3a6 and 26) on a pass. On a failure, the rework loop in the skill: equipment returns for rework, the solution goes back to step 3, or the use case returns to the integration hand-off. For `deploy-appstore`, the protocol is part of the release gate.
- **Stops here when:** any item fails, the data stops short of the asset the plant opens, no human has signed, or a dashboard disagrees with the paper record the plant trusts. Record the finding and follow the rework loop; do not retry quietly or mark a machine `INTEGRATED`.
