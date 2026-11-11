---
type: Skill Reference
title: Outputs
description: The outputs deploy-handover must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`deploy-handover` delivers the handover of a use case to the plant and the evidence of whether it is really in use.
Built is not handed over, and handed over is not in use.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Handover protocol | `assets/handover-protocol.md`, filled once per use case | Plant owner; `metrics-scorecard` reads it back on every cadence | Three-question test answered by the receiving side without asking the builder; ADKAR barrier point and evidence-of-adoption tier recorded; acceptance result pulled from `deploy-acceptance`, not re-asked |
| Definition-of-done fields on the record | Use case record | Plant owner | Output asset, business process and utilization expectation present; data path written to the machine; plant owner named and has used it in a real shift; affected people told before go-live (by whom, when); open items recorded as dependencies |
| Adoption tier | Entry in the protocol | Plant owner; DBVE | Tier no stronger than the evidence available (system usage log, named owner's dated statement, or third-party observation); never "handover marked DONE" |
| Low-utilization action | Entry in the protocol | Plant owner; OD lead | For low or `NEVER` utilization: ADKAR diagnostic run and an action recorded (review with requester, fix at the barrier point, or retire) |

## Handoff

- **Also receives from:** `deploy-project-order`: Handover check.
- **Also receives from:** `deploy-migration`: Decommissioning record.
- **Also receives from:** `deploy-appstore`: Hand-over to rollout.
- **Also receives from:** `catalog-guardrails`: Utilization expectation; Routing of failed guardrails.
- **Also receives from:** `ops-dashboard-engine`: Dashboard JSON; Handover facts.
- **Receives from:** `deploy-acceptance` (acceptance protocol); `bc-capital-request` and `funnel-use-case` (the approved
  use case and its record); the named plant owner.
- **Next in the flow:** `metrics-scorecard` (reads the protocol on every cadence); a proven, repeatable result goes to
  `catalog-standardization` and `catalog-usecase`. This is step 26 in Lane 2 and 3a6 in Lane 3; it also closes
  1a3 and 1b4 in Lane 1.
- **Stops here when:** a test question cannot be answered or the plant owner is unnamed. The handover is invalid and stays
  `ONGOING`; never mark it `DONE` because delivery happened. The plant, not OD, decides `PRODUCTIVE`.
