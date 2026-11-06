---
name: od-governance-cadence
description: >-
  Run the governance routines around the process chain - the CoP and any round the department holds
  (role, preparation, follow-up), the forums as sources of information (ODEC as a historical forum), the
  "call for action" and traffic-light status pattern, the regional and plant roadmap fields, demand and change routing (small change versus project versus governance board), the
  use-case sprint runbook, toolbox training-programme management and the community cadence between
  rounds. Use when a round or status report has to be prepared or followed up, a past decision or deck has to be found, a call for action has to be written, a
  roadmap is drafted, a request must be sorted into ticket or project, a sprint is planned or reviewed,
  or a training offer is to be run. Holds method only, no dates, counts or plant statuses.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-governance-cadence
  tier: practice
  lane: all
  new_state_lane: Spine (all lanes)
  new_state_step: "Governance rhythm: rounds, roadmap, demand routing, sprints, training"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  origin: plan-draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-decision-routing, od-scorecard-reporting, od-retro, od-risk-watch, od-use-case-definition, od-rollout-training, od-plant-onboarding, it-demand-package, od-use-case-prioritization]
  derived_from:
    - Operations Digitalization slide decks (community and strategy rounds, roadmap templates, demand management, use-case sprint reviews, training programme), abstracted into process guidance; no figures.
  okf:
    type: Agent Skill
    title: Governance cadence
    tags: [all, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Governance cadence

Read `od-context` first.

The chain (intake, lanes 1 to 3, spine) decides *what* happens to a demand. This skill holds the *routines*
that keep it moving: which forums exist or existed, what each asks, what it needs on the table and what it must leave
behind. ODEC met monthly only until 2025-12 and no longer does; there is no fixed replacement forum, so a recurring
governance meeting is never assumed. Past ODEC decks and facts remain a source of information. It does not repeat the metrics and thresholds (`od-scorecard-reporting`), the decision rights and
escalation (`od-decision-routing`), the one-change retro (`od-retro`), the risk readings (`od-risk-watch`) or
the lane flow of a use case (`od-use-case-definition`). It names them at the handoff.

## Where it sits in the chain

| Part | Process steps (`docs/new-state/process.yaml`) | Neighbour |
|---|---|---|
| Forums as sources, rounds on request, call for action, status, roadmap | spine; feeds 1b3, 3b5, 3a5 (waves, Cyber Security waits) | `od-scorecard-reporting`, `od-risk-watch`, `od-retro` |
| Demand and change routing | i1, 32, 3a4 | `od-decision-routing`, `it-demand-package` |
| Use-case sprint runbook | 23, 1a2, 1a3 | `od-use-case-definition`, `od-analytics-asset-build` |
| Training programme | 1a3, 3a6, 26 | `od-rollout-training` |
| Community routine | spine, after 26 (library, best practice) | `od-use-case-promotion` |

## References and assets

| File | Use it for |
|---|---|
| [`references/forums-and-roadmap.md`](references/forums-and-roadmap.md) | CoP and ODEC (historical): question, input, output; ODEC as a source of information; preparation and follow-up steps; the call-for-action and status pattern; regional and plant roadmap fields; community routine |
| [`references/demand-and-change-routing.md`](references/demand-and-change-routing.md) | Small change versus project versus governance board; the demand-management question list; first mover versus fast follower (wave allocation) |
| [`references/sprint-runbook.md`](references/sprint-runbook.md) | Use-case sprint: preconditions, rhythm, standard deliverables, review, additional-phase rule, pitfalls |
| [`references/training-programme.md`](references/training-programme.md) | Toolbox training offer: request, register, invitation cycle, feedback, needs list |
| [`references/rituals-and-consumption.md`](references/rituals-and-consumption.md) | The plant rituals the output is consumed in (daily Gemba, shift checks, escalation, portfolio review, waves), how to find the ritual behind a use case, the ladder from shift to round |
| [`assets/call-for-action-and-status.md`](assets/call-for-action-and-status.md) | Round pack: agenda, plant status table, numbered call for action |
| [`assets/sprint-plan-and-review.md`](assets/sprint-plan-and-review.md) | Sprint plan, weekly log, sprint-end review |

## Procedure: prepare and follow up a round

1. **Name the round and read its contract**: question, input, output (`forums-and-roadmap`). A round is held
   on request or on the department's own schedule; ODEC is historical and not a current forum, so look up any
   schedule instead of assuming one.
2. **Collect inputs against the input column**, each with source and read date: integration and rollout
   status, Cyber Security status, use-case forecast, training schedule, open feedback from the last call.
   Numbers come live from `od-scorecard-reporting`; risk readings from `od-risk-watch`.
3. **Draft the pack** from [`assets/call-for-action-and-status.md`](assets/call-for-action-and-status.md):
   agenda, status table with one traffic light (red / yellow / green) per round, one worked best-practice
   example, numbered call for action.
4. **Human gate**: the OD lead approves the pack and owns any escalation wording and deadline.
5. **Run the round; capture** questions, decisions and homework against the output column.
6. **Follow up**: classify incoming Q&A into the question pack and route each to its owning service line;
   chase open homework; carry unresolved items into the next round with the label "carried" (one round
   escalation window, `od-scorecard-reporting`). Hand the inputs to `od-retro` (CoP feedback).

## Decision rules

- A request is a **demand** first: sort it with `od-use-case-intake-triage`, then route change versus
  project with [`demand-and-change-routing`](references/demand-and-change-routing.md).
- Use cases exist only for **connected machines**; a not-connected machine goes into a wave first.
- A requirement beyond the sprint timeframe becomes an **additional use-case phase**, not scope creep.
- Savings count only against a **registered plant savings project with a baseline and an owner**.
- Rollout continues only where an **operations concept** (owner, SLA, support level) exists.

## AI agent operating notes

- **May do**: draft the round pack, the status table and the call-for-action text from the portfolio and
  integration lists; classify Q&A into the question pack; keep the sprint board and the training needs list;
  chase open homework; check a project-order request for empty owner, budget and out-of-scope.
- **Required inputs**: the lists above with read date; the previous round's open items; the schedule in force, if any.
- **Evidence to cite**: source list and read date per status cell; the earlier round or sprint a statement reuses.
- **Human gate**: the OD lead approves escalation wording, deadlines and roadmap approval; the sponsor and
  governance board decide yes or no on a project; the local key user confirms plant status and the standard
  procedure of a use case. Agents never decide a route, a budget or a priority.
- **Handoff**: pack to the OD lead; routed requests to the owner named in `od-decision-routing`; round
  feedback to `od-retro`; indicator gaps (no registered project, stale tag list, old tickets) to `od-risk-watch`.

## Still open

- `<Current standard dashboard tool>` for the sprint deliverables: check `od-context`.
- `<Ticket tool, backlog owner, governance board membership>` for demand routing.

## Do not

- Do not write dates, counts, savings or plant statuses into the skill or its templates; read them live.
- Do not name persons; use roles.
- Do not present ODEC as a current forum or a place a decision must go; there is no fixed replacement forum.
- Do not escalate by agent. The agent drafts the line; the OD lead sends it.
- Do not start a sprint without an expert for the process, a defined baseline and agreed architecture and access.
- Do not treat recorded demand as proven saving.
