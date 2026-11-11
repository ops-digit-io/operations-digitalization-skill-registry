---
type: Skill Reference
title: Outputs
description: The outputs od-system-fit-check must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-system-fit-check` delivers a fit verdict on whether a request quietly needs a system outside the lean footprint. In Lane 3 it also delivers the route and verdict of the tool-decision gate. It recommends; it never approves an exception.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| System fit check | `assets/system-fit-check.md`, filled | The calling skill (`od-use-case-intake-triage`, `od-requirements-breakdown`) | The need is restated independent of the request's wording; each tool boundary is checked with a stated reason; this plant's availability is checked and dated; one verdict (fits, redesign, escalate) and a named next step |
| Existing-system worksheet (when a legacy application or tool may cover the need) | `assets/existing-system-worksheet.md`, filled | OD lead, with the check | Filled whenever the plant may already run a covering application or tool |
| Exception escalation (verdict "escalate") | Decision request via the "Tool/system rollout" row | `od-decision-routing`; the OD lead decides together with the IT-responsible role of the business side | The boundary line crossed and the dated plant availability are cited |
| Lane 3 gate result (step 32) | Verdict and route in the system fit check | `od-decision-routing`, then the route's skill: `deploy-appstore` (3a.1, 3a.2), `it-demand-package` (3a.3, 3a.4), `od-equipment-integration` (3b) | Footprint gate has no open point (or the verdict is Blocked); one route (3a.1 to 3a.4 or 3b) with its next skill; six criteria scored with the verdict in the department's words and one decisive reason |

## Handoff

- **Receives from:** `od-use-case-intake-triage` (step i1), `od-requirements-breakdown` (step 31), `catalog-systems` (when no standard system exists), `catalog-guardrails` (guardrail G3); the request, the plant, and in Lane 3 the tool or purchase in question.
- **Next in the flow:** "fits" goes back to the calling skill; "redesign" re-scopes the request before it is defined further; "escalate" goes to `od-decision-routing` (step 32); the Lane 3 route goes on to `it-demand-package`, `deploy-appstore` or `od-equipment-integration`, and the business case follows with `od-benefit-calculation` (step 33).
- **Stops here when:** no boundary line can be named, the sources disagree, or the plant status is unknown. The check is then not finished. It also stops on a tool nobody runs (a service gap, not a fit). It never approves a rollout exception itself.
