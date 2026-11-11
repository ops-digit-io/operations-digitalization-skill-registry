---
type: Skill Reference
title: Outputs
description: The outputs od-cybersec-gate must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-cybersec-gate` delivers the request package for the Cyber Security / OT sign-off, the routed decision request and the dated record of the answer. It drafts and recommends only; the sign-off itself is human-only. The skill is not done because the work was built.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Sign-off package | `assets/cybersec-signoff-package.md`, filled | IIAE or Plant IT, who submit it to Cyber Security | Case classified (machine connection or app deployment); contents follow `references/package-contents.md` and come from existing outputs; credentials, addresses, certificates and tokens are listed as existing, never pasted |
| Routed decision request | A request on the row "Equipment integration go-ahead", using the decision request template of `od-decision-routing` | `od-decision-routing` | Opened; the sign-off is recorded as a dependency on the use case or machine record |
| Wait-state record | Section of the package | OD lead (escalation) | Submission date, follow-up owner and next check recorded; no go-live date promised |
| Recorded answer | Section of the package | `od-acceptance-test` (evidence), `od-equipment-integration`, `deploy-appstore` | Names who answered, date, scope, conditions and validity; outcome is granted, granted with conditions (conditions become open items) or refused (barrier routed); or the case is held with an owner and an escalation date |

## Handoff

- **Also receives from:** `od-migration-cutover`: Staged migration plan; Back-out plan.
- **Also receives from:** `od-first-aid-kit`: Route with reason.
- **Also receives from:** `catalog-guardrails`: Routing of failed guardrails.
- **Receives from:** `od-equipment-integration` (data path and integration concept), `deploy-appstore` (app package), `od-acceptance-test` (acceptance protocol).
- **Next in the flow:** `od-decision-routing`, then `od-acceptance-test` and go-live once the sign-off is recorded. Proposed on steps 1b3, 3a5 and 3b5 of `docs/new-state/process.yaml`; it runs in parallel with planning and build and blocks only go-live.
- **Stops here when:** no named answer is on record. A missing sign-off holds the case: no expedited path, no machine connected, no app deployed live on an unanswered request, and "implied", "verbal" or "covered" is not a sign-off.
