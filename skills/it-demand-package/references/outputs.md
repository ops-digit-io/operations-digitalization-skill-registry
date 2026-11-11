---
type: Skill Reference
title: Outputs
description: The outputs it-demand-package must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`it-demand-package` delivers a cleared Lane 3 demand as an OpenSpec change package plus the OD handover annex. The skill is
not done until the package passes its check, a human has sent it and the demand record shows who received it.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| OpenSpec change package | `openspec/changes/<change-id>/` with `.openspec.yaml`, `proposal.md`, `specs/<capability>/spec.md`, `design.md`, `tasks.md` (templates in `assets/openspec/`) | IT or the external developer | One delta spec per capability, each requirement with a scenario; design states the route, platform, interfaces, Cyber Security constraints and non-goals (the growth boundaries); tasks include the acceptance test and the Cyber Security sign-off |
| OD handover annex | `handover.md` in the change folder (`assets/openspec/change/handover.md.tmpl`) | IT or the external developer | Every input IT asked for, the business case summary, the approval status and the ownership terms are filled; unknown items stay marked with who supplies them; the route, approval status and Cyber Security inputs are stated |
| Check output | Output of `scripts/check_handover.py`, attached to the package | IT or the external developer | The check reports READY with no errors and no open blocking field |
| Project context | `openspec/config.yaml` (`assets/openspec/config.yaml.tmpl`), only where the receiving repository has none | IT | Stack, deployment, interfaces, guardrails and language rules are filled |
| Demand record entry | Entry in the demand record | OD lead | Shows "handed over, awaiting acceptance" with the receiving team named; not "accepted" |

## Handoff

- **Also receives from:** `od-governance-cadence`: Routed demand.
- **Receives from:** `od-requirements-breakdown` (requirement with growth boundaries), `od-system-fit-check` (gate verdict Go or PoC-first, and route), `od-benefit-calculation` and `od-investment-input` (business case and investment estimate), `od-capital-request` and `od-decision-routing` (approval route).
- **Next in the flow:** IT or the external developer builds from the package (steps 3a.3 and 3a.4 in `process.yaml`); `deploy-appstore` (steps 3a.1, 3a.2, 3a5) takes the built app to the platform; `od-handover-and-adoption` (step 3a6) moves ownership only on formal acceptance.
- **Stops here when:** any front-end part is missing (name it and stop), the demand has no written growth boundaries, or the check does not report READY. A human sends the package; the agent never sends it and never marks an acceptance as given.
