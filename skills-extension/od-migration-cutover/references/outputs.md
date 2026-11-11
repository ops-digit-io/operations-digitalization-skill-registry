---
type: Skill Reference
title: Outputs
description: The outputs od-migration-cutover must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-migration-cutover` delivers the assessment, the staged migration plan, the per-location cutover checklist and the back-out plan for one migration, and the record that the old system was retired. The cutover, the back-out decision and the decommissioning are human.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Migration assessment | `assets/migration-assessment.md`, filled | `od-decision-routing`, OD lead and plant | Every component and interface inventoried; each use case marked "must be preserved", "can be dropped" or "replace later"; a risk row and recovery-impact class per component; ratings confirmed by the local owner; "continue as-is" written as baseline scenario |
| Staged migration plan | Staged plan in the migration assessment | `deploy-appstore`, `od-cybersec-gate` | Lowest-risk stage first; each stage has resources, cost, risk and an exit criterion; preconditions listed |
| Per-location cutover checklist | `assets/cutover-checklist-and-backout.md`, checklist with RAG | `od-acceptance-test`, plant key user | Time plan communicated, outage window set, RAG status per item, key-user verification meeting held and recorded |
| Back-out plan | Back-out plan section of the same asset | `deploy-appstore`, `od-cybersec-gate` | One per stage; trigger and decision owner agreed before the outage window opens; read by the people who would execute it |
| Decommissioning record | Decommissioning record in the same asset | `od-handover-and-adoption` | Old system switched off by a named person, server released, application list updated; no parallel paper or shadow system remains |
| Open-items list per location | List with the filled assets | `od-risk-watch`, `od-decision-routing` | Open risks and blocked locations listed per location |

## Handoff

- **Receives from:** `od-system-fit-check` (replace, integrate or keep decision, target architecture), `od-requirements-breakdown` (use-case list of the old system), `od-cybersec-gate` (security status), plant ME and the local owner (application and interface lists).
- **Next in the flow:** `deploy-appstore` and `od-cybersec-gate` (step 3a5, deployment package and back-out plan), `od-acceptance-test` (verification list and test evidence), `od-handover-and-adoption` and `od-rollout-training` (step 3a6, service concept and retire-the-old-process owner), `od-risk-watch` for open risks. The tool-decision gate is step 32.
- **Stops here when:** preconditions or the back-out plan are missing, the outage window is not announced, the key user is not available, a customer audit or fixed external date is near, or an owner has not confirmed a rating. No stage starts and nothing is decommissioned before key-user verification and the agreed observation period.
