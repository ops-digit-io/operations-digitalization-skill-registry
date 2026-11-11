---
type: Skill Reference
title: Outputs
description: The outputs deploy-appstore must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`deploy-appstore` delivers the deployment package and release gate for putting an app on the platform. It does not
deploy: a human with deploy rights does that.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Deployment package | `assets/deployment-package.md`, filled | Human with deploy rights on the platform | App, owner, plant sponsor, target, sourcing route, data read and written, dependencies, rollback owner and acceptance protocol are all stated |
| Release gate table | Gate table in the deployment package | Cyber Security (sign-off), `dept-decision-rights` (approval route) | Protocol drafted; Cyber Security sign-off shown as requested or granted, by whom and when; approval route named |
| Acceptance protocol | Drafted with `deploy-acceptance`, referenced from the package | `deploy-acceptance` | Protocol exists before release and is named in the package |
| Open questions with owners | List in the deployment package | OD lead | Each gap (for example lead time, deploy rights, Cyber Security requirements) has a named owner |
| Hand-over to rollout | The package with the gate result | `deploy-handover` | A human has deployed and the hand-over is made |

## Handoff

- **Also receives from:** `deploy-migration`: Staged migration plan; Back-out plan.
- **Receives from:** `funnel-requirements` (accepted requirement), `invest-screen` and `dept-decision-rights` (tool decision), `bc-build` (business case), `bc-capital-request` (capital approved where needed), and `deploy-it-demand` first on routes 3a.3 and 3a.4 once the external build is delivered.
- **Next in the flow:** `deploy-handover` (step 3a6, rollout and adoption).
- **Stops here when:** a package field is missing or the Cyber Security sign-off is not granted. Then the package is invalid for release: list the gap with its owner and stop. No deployment to a shared platform without the named human approval.
