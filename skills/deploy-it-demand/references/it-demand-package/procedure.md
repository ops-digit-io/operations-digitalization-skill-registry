---
type: Skill Reference
title: Procedure
description: Formerly the skill deploy-it-demand, absorbed into deploy-it-demand on 2026-11-10 to remove duplication against the department context. Package a demand for IT demand management and its evaluation board, or for an external developer (new-state Lane 3a, routes 3a.3 external development and 3a.4 foreign-app integration) - one hand-off that carries the requirement, the fit-check verdict, the business case, the approval route, the plant sponsor and the open Cyber Security points. Drafts the package; submitting it and the board's decision stay human. Use when a demand touches a platform OD does not own, when a foreign app must be integrated, when an app is to be built externally, or when someone asks what IT needs from OD. Draft sc
resource: ../../SKILL.md
status: draft
tags:
- all
- practice
- new-state
- draft
- absorbed
---
# IT demand package

> **Absorbed.** This was the skill `deploy-it-demand`. It now runs as a mode of [`deploy-it-demand`](../../SKILL.md) (merged 2026-11-10, see `log.md`). Its authority stays as it was: draft the package; submission and the evaluation board's decision are human.

Read `dept-context` first.

**Status: draft scaffold.** The registry already **routes** an IT demand (`dept-decision-rights`: IT demand goes through
demand management). The new-state flow lists the **packaging** of that demand as a net-new build. The sources read hold
OD's side of the package and none of IT's own requirements. This skill assembles OD's side and marks IT's as open.

## The rule it serves

Knowledge bundle, `Decision rights`: requests that need something from IT go through **IT demand management**, with a
demand evaluation board. This is the route for anything touching a platform the function does not own.

## Where the flow puts it

Lane 3, branch 3a, "Package / build app", for the two routes that leave OD's hands:

- **3a.3 External development** - the specification is written in-house, the build is done externally.
- **3a.4 Integrate a foreign app** - a third-party app is integrated through IT and Cyber Security.

The shared front-end before it (requirements, tool-decision gate, business case) must be done. The flow marks the wait
that follows as weeks (IT commitment and approval).

## The references

| File | Use it for |
|---|---|
| [`references/it-touchpoints.md`](references/it-touchpoints.md) | Which demands belong here, the kinds of ask OD puts to IT (licences and budget, platform integration, capacity), the IT roles of the platform operations concept, how to find the initiatives that lean on IT, where demands typically wait |
| [`references/external-build-and-foreign-app-inputs.md`](references/external-build-and-foreign-app-inputs.md) | The foreign-app description in the legacy list's own columns, the four assessment questions, what an external developer can be handed from OD's side, typical foreign-app patterns and how to count them on the live legacy list |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | The package at chain step 3a4: demand-management question list, request flow, small change versus project, supplier-built app practice, commercial consistency check, decision pairs, agent notes |
| [`assets/it-demand-package.md`](assets/it-demand-package.md) | The package to fill: parts 0 to 12, with the pre-wired skills and the checks before hand-over |

What stays open after mining the knowledge base: IT's own demand form, the board's criteria and rhythm, the contact and the lead time are in none of the sources read.

## What OD can put into the package

| Part | Where it comes from |
|---|---|
| The requirement, and the epic with its stories | `funnel-requirements` |
| The fit-check verdict | `invest-screen` |
| The business case, with sources and capture dates, no invented figures | `bc-build` |
| The approval route and the owner of each decision | `dept-decision-rights` |
| The plant sponsor and the plant owner | the demand itself |
| The acceptance criteria the delivery will be tested against | `deploy-acceptance`, drafted |
| Open Cyber Security points | `dept-decision-rights`; the sign-off is human-only |
| For 3a.4: what the foreign app reads and writes, and where it runs | the requester - mark every field not given as ⟨missing⟩ |

## Procedure

1. **Check the front-end** is complete: requirement, tool decision, business case. If a part is missing, name it and stop.
   A small change (a few days, budget available, standard interface) is a ticket by the local key user, not a package.
2. **Pick the route**: 3a.3 or 3a.4. The routes 3a.1 and 3a.2 do not need this package.
3. **Assemble the package** from the table. Every gap stays visible as ⟨missing⟩ with the person who can close it.
4. **Add IT's own required fields** once they are known: ⟨IT demand form fields - to be supplied⟩.
   Before calling it ready check that offer, capital request and contract are the same version (offer first, then the capital request; before ordering all three must agree) and that a named role drives purchasing.
5. **Hand over for submission.** A human submits to IT demand management. The evaluation board decides. This skill neither
   submits nor decides.
6. **After the decision**, continue with `deploy-appstore` (deployment gate) and `deploy-handover` (rollout).

## Output - the IT demand package

One document: the demand in one paragraph; the route (3a.3 / 3a.4); the parts above in that order; a list of open items
with owners; a line "Submitted by a human on ⟨date⟩ - not yet".

## Open - what only the OD lead can supply

- ⟨IT's demand form⟩ and ⟨the evaluation board's criteria and rhythm⟩ - searched in the bundle, the knowledge base's AI decks and the initiatives on 2026-11-05; the sources carry the route and OD's asks, not the form.
- ⟨Who the contact in IT demand management is⟩ and ⟨the usual lead time⟩ beyond the flow's "weeks".
- ⟨What an external developer must receive⟩ (spec format, environment access, security terms).

## Do not

- Submit the package, or state the board's decision in advance.
- Put an unsourced figure in the business-case part.
- Fill an IT field from a guess. Mark it ⟨missing⟩.
- Use this package for a demand that stays inside platforms OD owns.
