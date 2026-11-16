---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## The references are the substance

**The function proposes; other people decide.** Most portfolio gates sit
outside OD. The work that reliably moves is the work where the gate was identified at
intake and the owner was named. **The work that stalls is almost never stuck on
engineering.**

## Example

Fictional example (all values invented for illustration):

If it fails: when no row or gate fits, or the rights look out of date, validate with the OD lead role and write "decision rights pending re-verification"; do not act on the row.

## Outputs and hand-off: the text before outputs.yaml

`dept-decision-rights` delivers a decision request for each decision: which row or gate applies, who decides, and how it was routed. It routes decisions and never takes them.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Decision request | `assets/decision-request.md`, filled | The deciding role named in the table (for example DBVE, IIAE, OD lead, plant budget owner, plant owner, Cyber Security) | Names the row or gate, the deciding role, the mode, the authority level and the outcome |
| Gate recorded as a dependency | Dependency on the use case or saving row | Owner of the use case or saving row; `bc-build` and `bc-capital-request` for saving rows | The gate (for example ECR creation) is recorded with a named owner, and the decision is written as decision, proposal, risk of not doing |
| Escalation | Message to the named role or forum | OD lead, or COP for technical matters | Sent when a trigger from the risk list was met, inside the agreed window |

## Handoff

- **Also receives from:** `catalog-standardization`: Standardization review; Capability and process-group placement; CSP-readiness verdict.
- **Also receives from:** `funnel-evaluation`: Evaluation protocol; Verdict and total score.
- **Also receives from:** `dept-risk`: Triggers hit and routing.
- **Also receives from:** `dept-retro`: Escalations.
- **Also receives from:** `bc-portfolio`: Prioritization record.
- **Also receives from:** `dept-plant-diagnosis`: Decision and escalation items.
- **Also receives from:** `deploy-migration`: Migration assessment; Open-items list per location.
- **Also receives from:** `dept-governance`: Follow-up log; Routed demand.
- **Also receives from:** `catalog-compatibility`: Verdict per plant; Recommendation.
- **Also receives from:** `deploy-appstore`: Release gate table.
- **Receives from:** the calling skill with the decision in question, for example `dept-intake` (expected gate), `catalog-systems` (cost-template inputs), `invest-screen` (exception to escalate), `bc-build` (open dependencies).
- **Next in the flow:** step 1b2 to `mi-equipment` (1b3) once the cost template is approved; step 25 to `bc-capital-request`; step 32 (tool-decision gate) to the route chosen by the OD lead.
- **Stops here when:** no row or gate fits, or the decision rights look out of date. Write "decision rights pending re-verification" and validate with the OD lead; every row is used at most at `recommend`. Do not act on a row above that, and do not treat urgency as a substitute for the deciding role.
