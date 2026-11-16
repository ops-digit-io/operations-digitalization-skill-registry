---
name: dept-governance
description: >-
  Prepares and follows up the department's governance routines: a COP or other round (agenda, plant status with one traffic light, numbered call for action, follow-up), finds past decisions and decks (ODEC is historical), drafts regional and plant roadmap rows, sorts a request into small change, project or governance board, plans and reviews a use-case sprint, and runs a toolbox training offer. Use when a round or status report is due, a call for action must be written, a roadmap is drafted or refreshed, a request must go to a ticket or a project, a sprint is planned or reviewed, or a training offer needs a needs list. Method only: no dates, counts or plant statuses; the OD lead approves and sends. Not for the monthly retro (dept-retro), risk readings (dept-risk) or who decides (dept-decision-rights).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: dept-governance
  aliases: [od-governance-cadence]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Lane 2 (23), Spine"
  new_state_step: "Prototype / click-dummy, validated with the recipient; Supporting spine"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  origin: plan-draft
  requires: [dept-context]
  composes: [dept-decision-rights, metrics-scorecard, dept-retro, dept-risk, funnel-use-case, know-training, dept-plant-onboarding, bc-portfolio]
  okf:
    type: Agent Skill
    title: Governance cadence
    tags: [all, practice, new-state, draft]
---

# Governance cadence

## Purpose

- Read `dept-context` first.

- The chain (intake, lanes 1 to 3, spine) decides *what* happens to a demand.
- This skill holds the *routines* that keep it moving: which forums exist or existed, what each asks, what it needs on the table and what it must leave behind.
- ODEC no longer meets and there is no fixed replacement forum, so a recurring governance meeting is never assumed (dates: `references/background.md`).
- Past ODEC decks and facts remain a source of information.
- It does not repeat the metrics and thresholds (`metrics-scorecard`), the decision rights and escalation (`dept-decision-rights`), the one-change retro (`dept-retro`), the risk readings (`dept-risk`) or the lane flow of a use case (`funnel-use-case`).
- It names them at the handoff.

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

- Inputs: the lists and reports with read date (integration and rollout status, Cyber Security status, use-case forecast, training schedule), the previous round's open items, the schedule in force, if any.
- Output: a round pack, a follow-up log, a sprint plan and review, or a routed demand (see `outputs.yaml`).

## Where it sits in the chain

| Part | Process steps (`docs/new-state/process.yaml`) | Neighbour |
|---|---|---|
| Forums as sources, rounds on request, call for action, status, roadmap | spine; feeds 1b3, 3b5, 3a5 (waves, Cyber Security waits) | `metrics-scorecard`, `dept-risk`, `dept-retro` |
| Demand and change routing | i1, 32, 3a4 | `dept-decision-rights`, OpenSpec IT demand (external) |
| Use-case sprint runbook | 23, 1a2, 1a3 | `funnel-use-case`, `ops-analytics-asset` |
| Training programme | 1a3, 3a6, 26 | `know-training` |
| Community routine | spine, after 26 (library, best practice) | `catalog-standardization` |

## Definition of done

- Round pack: every status cell cites source and read date, one traffic light per round, the OD lead approved the escalation wording and deadline.
- Follow-up log: Q&A routed to an owning role, homework chased, open items labelled "carried".
- Sprint: process expert, baseline, architecture and access recorded before start; later requirements logged as additional phase.
- Demand: sorted with `dept-intake` first, owner named.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## Procedure: prepare and follow up a round

1. **Name the round and read its contract**: question, input, output (`forums-and-roadmap`). A round is held
   on request or on the department's own schedule; ODEC is historical and not a current forum, so look up any
   schedule instead of assuming one.
2. **Collect inputs against the input column**, each with source and read date: integration and rollout
   status, Cyber Security status, use-case forecast, training schedule, open feedback from the last call.
   Numbers come live from `metrics-scorecard`; risk readings from `dept-risk`.
3. **Draft the pack** from [`assets/call-for-action-and-status.md`](assets/call-for-action-and-status.md):
   agenda, status table with one traffic light (red / yellow / green) per round, one worked best-practice
   example, numbered call for action (fill the template; see the example below).
4. **Human gate**: the OD lead approves the pack and owns any escalation wording and deadline.
5. **Run the round; capture** questions, decisions and homework against the output column.
6. **Follow up**: classify incoming Q&A into the question pack and route each to its owning role; chase open homework; carry unresolved items into the next round with the label "carried" (one round escalation window, `metrics-scorecard`).
   - Hand the inputs to `dept-retro` (COP feedback).

## Procedure: sort a demand (small change, project or board)

1. Sort the request with `dept-intake` first; it decides OD or not OD and the lane.
2. Apply the small-change test (`references/demand-and-change-routing.md`): effort, budget, interface. All three small: ticket route; otherwise project route.
3. Check entry: owner role, sponsor and document location exist; demand is effect-driven; machine connected and signals selected; key user staffed. Otherwise it does not enter routing.
4. Answer the IT demand question list; mark unanswered ones `<...>`; the product owner decides.
5. Route a project to the governance board with the product owner and to `deploy-project-order`; record the owner.

## Procedure: plan and review a use-case sprint

1. Check all preconditions before day one (`references/sprint-runbook.md`): connected machines, named process expert, baseline and owner, architecture and access, out-of-scope written. Any missing: do not start.
2. Plan the time-box and rhythm in `assets/sprint-plan-and-review.md`; keep the IT-issue log from day one.
3. Deliver the standard set; log any requirement beyond the time-box as an additional phase.
4. Hold the sprint-end review with the review questions; done means integrated into a standard operating procedure with a utilisation review.

## Procedure: write or refresh a roadmap row

1. Open the roadmap fields in `references/forums-and-roadmap.md`; one row per plant, regional rows roll up from plant rows.
2. Fill system status and machines done of planned from the lists, each with source and read date; unknowns stay `<...>`.
3. Set one traffic light and one call-for-action cell per row; the local key user confirms the plant status.

## Procedure: run a training offer

1. Keep the needs list (training, description, requester, status) and review registrations monthly (`references/training-programme.md`).
2. Invite, collect feedback, and report offer, attendance and feedback to the next round and to `dept-retro`.
3. The plant training package and competence checklist stay with `know-training`.

## Decision rules

- A request is a **demand** first: sort it with `dept-intake`, then route change versus project (`references/demand-and-change-routing.md`), because routing a project as a ticket skips the budget gate.
- Use cases exist only for **connected machines**; a not-connected machine goes into a wave first, because without signals the use case has nothing to read.
- A requirement beyond the sprint timeframe becomes an **additional use-case phase**, not scope creep, because the time-box is what keeps the sprint finishable.
- Savings count only against a **registered plant savings project with a baseline and an owner**, because without a baseline the saving cannot be shown.
- Rollout continues only where an **operations concept** (owner, SLA, support level) exists, because a rollout without support turns into an unowned system.

## Example: status row and call for action (fictional)

```text
Status row : Plant A (fictional) | system status: connected, rollout under way |
             machines done of planned: 3 of 8 | light: yellow (close-loop update required) |
             call-for-action cell: step 2 | source: Machine List, read 2026-03-02 (fictional)
Call for action
  1. Check the project overview and process flow (week 12, plant key user)
  2. Check own status and missing factors in the shared dashboard (week 13, plant key user)
  3. Contact OD for the remaining steps (week 14, OD contact)
  Escalation line (OD lead sends): finish before <deadline set by operations management>
```

## Human gate and AI-agent notes

- **May do**: draft the round pack, the status table and the call-for-action text from the portfolio and integration lists; classify Q&A into the question pack; keep the sprint board and the training needs list; chase open homework;
   - check a project-order request for empty owner, budget and out-of-scope.
- **Required inputs**: the lists above with read date; the previous round's open items; the schedule in force, if any.
- **Evidence to cite**: source list and read date per status cell; the earlier round or sprint a statement reuses.
- **Human gate**: the OD lead approves escalation wording, deadlines and roadmap approval; the sponsor and governance board decide yes or no on a project; the local key user confirms plant status and the standard procedure of a use case.
   - Agents never decide a route, a budget or a priority.
- **Handoff**: pack to the OD lead; routed requests to the owner named in `dept-decision-rights`; round
  feedback to `dept-retro`; indicator gaps (no registered project, stale tag list, old tickets) to `dept-risk`.

## Still open

- `<Current standard dashboard tool>` for the sprint deliverables: check `dept-context`.
- `<Ticket tool, backlog owner, governance board membership>` for demand routing.

## Pitfalls

- Several traffic-light scales in one round: use one scale; put "delayed" or "at risk" in the comment text only.
- A status cell without source and read date: the OD lead cannot tell a live figure from a copied one.
- Treating recorded demand as proven saving: they sit on different gates.
- Starting a sprint before the baseline exists: savings are then never reported.
- Dashboards deployed without a defined action: visibility, no saving.
- Assuming a fixed forum schedule: look it up, ODEC is historical.

## Do not

- Do not write dates, counts, savings or plant statuses into the skill or its templates; read them live.
- Do not name persons; use roles.
- Do not present ODEC as a current forum or a place a decision must go; there is no fixed replacement forum.
- Do not escalate by agent, because escalation wording and deadline are the OD lead's. The agent drafts the line; the OD lead sends it.
- Do not start a sprint without an expert for the process, a defined baseline and agreed architecture and access.
- Do not treat recorded demand as proven saving.

## References and assets

| File | Open when |
|---|---|
| [`references/forums-and-roadmap.md`](references/forums-and-roadmap.md) | You prepare a COP or other round, write a call for action or status row, draft roadmap fields, or must find a past decision (ODEC) |
| [`references/demand-and-change-routing.md`](references/demand-and-change-routing.md) | A request must be sorted into small change, project or board, or a wave must be allocated |
| [`references/sprint-runbook.md`](references/sprint-runbook.md) | A use-case sprint is planned, started or reviewed |
| [`references/training-programme.md`](references/training-programme.md) | A training offer is run or a needs list is kept |
| [`references/rituals-and-consumption.md`](references/rituals-and-consumption.md) | You must find the plant ritual a use case's output is consumed in |
| [`assets/call-for-action-and-status.md`](assets/call-for-action-and-status.md) | You draft a round pack |
| [`assets/sprint-plan-and-review.md`](assets/sprint-plan-and-review.md) | You plan a sprint or write the sprint-end review |
| [`references/background.md`](references/background.md) | You want the context, dates or rationale; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
