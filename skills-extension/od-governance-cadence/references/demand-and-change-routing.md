---
type: Skill Reference
title: Demand and change routing
description: Sorting a request into small change, project or governance board; the demand-management question list; wave allocation and first-mover rule; funding of an unfamiliar field.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Demand and change routing

Decision rights and forums stay in `od-decision-routing`. This file sorts the request first.

## Small change versus project

| Test | Small change | Project |
|---|---|---|
| Effort | a few days at most `<to confirm threshold>` | larger |
| Budget | already available | needs central budget |
| Interface | standard | non-standard |
| Route | local key user requests it in the ticket tool; approved in the change process | governance board with the product owner; project order; `bc-capital-request` where money is needed |

Flow of a ticketed demand: request (key user), backlog (product owner), evaluation, work order, development
system, test system, user acceptance, transport to production, post-implementation review with the requester,
change coordination (tasks, approvals, risks, affected configuration items).

## Question list (it-demand-package checklist)

Who can raise requests; who manages the backlog; who evaluates; who decides yes or no; who estimates effort;
who decides to start development; who develops; who does the final test; who triggers implementation; which
configuration items are affected; who is responsible for implementation; per step, which tool documents it.
Mark unanswered ones `<...>`; the product owner decides.

## Entry checks before routing

- Initiative has an owner role, a sponsor and a document location, else it does not enter routing.
- Demand is effect-driven, not idea-driven; changes launched without pre-alignment with OD cause friction and one-offs.
- Is the machine connected and are the signals selected; is a key user staffed; does a local solution already fit
  the method (treat it as input to standardisation, not as new demand).
- A service gap (tool without operations concept or support role) goes to the operations-concept discussion, not to use-case triage.
- Keep an explicit "not ours" list.
- Notification channels and data historization are IT changes: raise the change request early.

## Waves and plants

- Wave allocation: **eligibility follows request order; central capacity goes first to first-mover plants that
  are staffed** (within a quarter and budget class, by systems needed).
- First mover: high estimated value, regions, segments and technologies covered, capacity and knowledge in the
  plant, integration synergy, a dedicated staffed key user. Fast follower: support when capacity allows, locally driven.
- Wave decision includes a staffing check (plant resource and skill), not only the budget.
- Connect whole processes or areas at once; reuse existing infrastructure.

## Funding an unfamiliar field

Fund only the first step (the governing tool or platform), time-boxed, assess benefit, then decide the
continuation at minimum cost. Write decisions as numbered options with the "risk of not doing". Budget is never
left empty: give an educated guess; minimum timing is start, end, first version, first three milestones.

## Pitfalls

Capital requests not supported by plants; incomplete requests; deviation from templates and frame contracts
(use the cost calculator per connectivity scenario first).
