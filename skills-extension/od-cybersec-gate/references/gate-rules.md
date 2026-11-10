---
type: Skill Reference
title: Gate rules
description: Every rule that governs the Cyber Security sign-off gate, one line each with its source, plus what the sources do not give - open this to answer "is this allowed and who decides".
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Gate rules

All rows are read from the department documents on 2026-11-05. Nothing here is added by this skill.

## The rules

| # | Rule | Source |
|---|---|---|
| 1 | The assistant of the Information Integration lane **may not** connect machines or write to production systems, and **may not** approve external connections | `20-lanes/information-integration-service/agent-brief.md` ("May not") |
| 2 | Guardrail: never connect externally without Cyber Security / OT sign-off | same file ("Guardrails"); repeated in `mi-connector` |
| 3 | Physical integration and external connection are human-only, `execute-with-approval` | same file ("authority_level") |
| 4 | The Project Support lane must "respect Cyber Security sign-off"; acceptance and deployment are human-only | `20-lanes/project-support-consultancy/agent-brief.md` |
| 5 | Decision right: equipment integration go-ahead - IIAE together with Plant ME / Plant IT, Tandem, approval yes, reversible partially, threshold "per investment plan; Cyber Security sign-off for external connection", `execute-with-approval` | `00-core/08-decision-rights.md` |
| 6 | Error path: sign-off missing for an external connection - hold at the wait state | `20-lanes/information-integration-service/playbook.md` |
| 7 | Wait state: "Awaiting Cyber Security / OT sign-off" (both lanes list it) | playbook.md of the Information Integration and the Project Support lanes |
| 8 | Risk row "Cyber Security / OT exposure on machine connection". Early indicator: non-compliant connection detected. Owner: OD lead + Cyber Security. Countermeasure: bundle Cyber Security with the MSB rollout; sign-off gate. Escalation trigger: security gap on connected asset | `00-core/09-risks.md` |
| 9 | There is no expedited path and no authority level that shortens the wait | `mi-connector` SKILL.md and `references/fallbacks.md` section 4 |
| 10 | Approval is needed **before scheduling**, not after | `mi-connector` `references/fallbacks.md` section 4 and `assets/assessment-protocol.md` section 4 |
| 11 | Endpoints are connected per the OT cyber-security rules in the Connext Wiki | `mi-connector` `references/iiot-edge-platform.md` (bridge task 7), `references/decision-paths.md` |
| 12 | Strategy bet: bundle the sign-off with the wave rather than per machine | `mi-connector` `references/fallbacks.md` section 4 |
| 13 | A new system at Lane 3a goes to the platform "with Cyber Security sign-off"; the sign-off is human-only; the step is marked "weeks" | `deploy-appstore`; registry `docs/new-state-flow.md` |
| 14 | Lane 1b "Order and connect" and Lane 3b "Acceptance + CS to live" carry a Cyber Security sign-off as the external wait | `docs/new-state/OD_NewState_VSM_SkillMap.html` |
| 15 | The "Cyber Security / OT interface" is listed with access `consult` for the lane, not write | `20-lanes/information-integration-service/skills.md` |

## Where the gate sits in the lanes

| Lane step | Skill that serves it | What the gate adds |
|---|---|---|
| 1b order and connect | `mi-connector` | Sign-off before the connection is scheduled |
| 3a deploy to platform | `deploy-appstore` | Release gate includes the sign-off (step 4 there) |
| 3b acceptance and live | `od-acceptance-test` | Sign-off recorded as evidence before the machine is declared live |

## What the sources do not give

| Missing | Who could supply | Evidence of the gap |
|---|---|---|
| The sign-off standard document | OD lead with Cyber Security | `15-resources.md`: "standard doc - to collect (with Cyber Security)", version "to confirm" |
| Definition of "external connection" | OD lead with Cyber Security | the term is used in rules 1, 2, 5 and 10 and never defined |
| Lead time of a sign-off | Cyber Security | the flow shows "weeks"; no number anywhere |
| Validity or expiry of a sign-off | Cyber Security | not recorded |
| Submission channel and contact role | OD lead | not recorded |
| Contents of the Connext Wiki rules | Cyber Security / IT | cited by name only |
| Machine-level cyber status | IIAE | `cyber_security_status` is a registry `open_gaps` item; check on the live Machine List whether it is filled before relying on it |
