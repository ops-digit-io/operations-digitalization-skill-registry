---
type: Skill Reference
title: Forums and roadmap
description: CoP, ODIC and ODEC - question, cadence, input, output; preparation and follow-up; the call-for-action and traffic-light status pattern; regional and plant roadmap fields; community cadence between rounds.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Forums and roadmap

Method only. Cadence and agenda come from the decks and are `<to confirm>` against `od-scorecard-reporting`.

## The three formats

| Format | Question it answers | Cadence (per decks) | Input | Output |
|---|---|---|---|---|
| **CoP** (community of practice call) | How are we doing Operations Digitalization? Technical, plant-facing | monthly, about one hour, one common call | Plant issues and feedback, data-model needs, flow and dashboard questions, connector needs, training needs | Guidance on issues, a call for action, triggers for next steps |
| **ODIC** (information call) | Why do we prioritise it? | quarterly `<to confirm>`, may be split by time zone | Strategy, priorities and deadlines, finished sprints with high effect, scaling potential, Cyber Security strategic view | Priorities and deadlines that feed the next CoP |
| **ODEC** | Strategy, roadmap, reporting round | `<to confirm>` | Roadmaps, rollout and Cyber Security status, KPI reading | Strategy updates, priorities, deadlines, security announcements |

Every format lists input, content and a **trigger for action**. A round without a trigger is a briefing.

## Standard CoP agenda

Roadmap and rollout status, then Cyber Security call for action, then use-case forecast with one worked
best-practice example, then trainings, then feedback on the open process question of the last call. A fixed
question pack drives it: technical issues, data-model updates, rule-engine flows, dashboards, training
schedule, new connectors, ideas for new use cases. Between calls a Q&A link serves any service line.

An opening survey (first call of a community, or yearly) asks in priority order: do the tools work, which
features are missing; which use cases were done, planned, should become standard; what process understanding
was gained and which standards should change. Add demand per system (information, implementation, training),
deep-dive topics, and a vote on which core process deserves a standard data model.

## Preparation and follow-up

| Step | Do | Evidence |
|---|---|---|
| 1 Inputs | Pull status lists live (integration, rollout, portfolio, Cyber Security) | source and read date per cell |
| 2 Gaps | List plants without a registered savings project, stale tag lists, missing use-case lists | the list used |
| 3 Draft | Agenda, status table, best-practice example, call for action | previous round's open items |
| 4 Gate | OD lead approves wording and deadline | approval line |
| 5 Run | Capture decisions, homework, questions | notes |
| 6 Follow up | Route Q&A to the owning service line; chase homework; carry open items; feed `od-retro` and `od-risk-watch` | item ids |

What a plant brings: its latest PLC programs and tag lists in the central list, its use-case list, and whether
a savings project is registered for it.

## Call for action and status pattern

- **Call for action**: numbered steps, each with a calendar week and an owner role; a named link set (project
  overview, status report, regional contacts); and, where operations management has set a deadline, an
  escalation line with the closure date. Cyber Security shape: check the project overview and process flow,
  check own status and missing factors in the shared dashboard, contact OD for the remaining steps, finish
  before the deadline. Recurring blocker: firewall rules and VLAN configuration.
- **Status per plant** (one row each): system status, machines done of planned, traffic light, call-for-action
  cell. Traffic light: red = phase delayed, yellow = close-loop update required, green = on track. An earlier
  taxonomy used input collected / delayed / at risk before the equipment request is uploaded. Use one taxonomy
  per round and say which `<to confirm>`.
- **Plant readiness table**: sprint timing, savings project registered, workshop planned, projects, link to the
  use-case list; legend not planned / urgent / planned.
- **Wave micro-process** (weekly, shifted per plant): call with the local OT expert, prepare the capital request
  with the local expert, upload with the local team, close-loop communication until approval.

## Regional and plant roadmap fields

Drafted centrally per region, approved in the plant engineering roadmap workshop; plants raise requests
proactively. Fields (not content):

- Frame conditions with owner area and end-of-quarter dates: equipment integration, use-case deployment,
  system deployment, data ecosystem and lifecycle, Cyber Security (screening, program collection), admin and
  energy use cases, standard data models (with other regions), know-how management (trainings), analytics and AI.
- Two targets (use-case effect, integration progress), chances, workload (one responsible person per location),
  responsibility (rollout timeline, cost-saving calculation and reporting, compliance of new requests).
- A brainstorm page per plant: machines, systems, open questions, `?` where unknown.
- A short, mid and long-term page across regions.
- Plant planning on one slide per plant and year: header (cluster, plant, year, status date); action items split
  Plant / OD / Shared; comments with workshop timing, sprint timing, expected effect. First plant action: evaluate
  the remaining use cases on the list that relate to the machines being integrated.
- Engineering roadmap inputs: carry-over, new plant requests with standardisation value, central initiatives,
  system and use-case rollouts.

PROPOSAL: a roadmap is `ready` only when every frame-condition row has an owner and a quarter or `<unknown>`.

## Community cadence between rounds

Pre-recorded video plus live Q&A is the delivery pattern. Keep a transformation-flow library (documented
standard flows, plant-specific flows, shared proactively), a use-case library organised from overview to
in-depth (andon board for stakeholders, operations dashboard for technicians, process-value dashboard for
process engineers), and a best-practice example per call. Presented use cases, in the exchange with the lean
organisation, get homework: is a standard working procedure defined, is an impact estimated, if not what holds
it back; the next call presents the impact.

## Pitfalls

- Reporting dropped in a turbulent period, so impact could not be shown. Keep a minimum round pack alive.
- Use cases without a registered project are invisible to the savings ledger.
- KPI basis shifts when the architecture changes: record the basis and date next to every figure.
- Calls under-used: low participation means feedback does not reach the chain. Ask for the open question in advance.
