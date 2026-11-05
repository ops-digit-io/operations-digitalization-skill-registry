---
type: Skill Reference
title: Process chain practice
description: How the Information Integration lane runs its rhythm in the AI-driven chain - wave cadence and status, the community call pack, plant tiering, integration workshop, hand-over to use-case support, recurring blockers, handoffs and agent notes.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, lane, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - the lane's operating rhythm

Derived from the Operations Digitalization slide decks (community-call, strategy, roadmap, integration-workshop and rollout decks),
abstracted into process guidance. No figures, no plant statuses. `PROPOSAL` = synthesis not stated in a deck; `<...>` = unknown or
to confirm. Per-machine routing and the wave micro-process are in `od-equipment-integration`
(`references/process-chain-practice.md`); this file is the lane view around them.

## Where it sits in the chain

The lane is "unplaced" in the flow but serves steps 1b3, 3b4 to 3b6 and feeds lane 2 (use cases exist only on connected machines).
It is also the source of the status that the spine reports.

## 1 Method in practice

### The four service lines on one chain

Equipment integration support, use-case support, human information integration and analytical support run on the same chain. The
lane's output (connected, standardized data) is the input of the next two. Integration planning passes through phases: initiation
(machine list, integration method, machine CV, plan, cost per machine including IT and OT, start of the capital request), planning
(tag list from the PLC programs), execution (hardware, PLC software integration, data-model integration and tag selection,
rule-engine configuration), knowledge sharing and hand-over (use-case results, recommendation on the next wave, project hand-over to
the plant, training for self-service).

### Wave cadence and status

- Waves are planned by quarter per plant; the capital request is milestone one; the weekly micro-process (OT expert call, prepare
  the request, upload, close-loop until approval) shifts one calendar week per plant.
- Plant status table: plant, system status, machines done of planned, traffic light (red = phase delayed, yellow = close-loop update
  required, green = on track), call-for-action cell. Plant use-case readiness table: sprint timing, savings project registered,
  workshop planned, projects, link to the use-case list; legend with three symbols (not planned, urgent, planned).
- A plant brings to the call: latest PLC programs and tag lists in the central list, its use-case list, whether a savings project
  is registered. Use cases without a registered project are invisible to the savings ledger (`od-scorecard-reporting`).
- Cyber Security is a precondition of the wave (see `od-cybersec-gate`); the plant status shows the sign-off scope.

### The community call as the lane's rhythm

Two formats with different jobs. The **technical call** (monthly in the decks) asks how the work is going: roadmap and rollout
status, Cyber Security call for action, use-case forecast with one worked example, trainings, feedback on the last call's open
process question; a fixed question pack drives it (technical issues, data-model updates, rule-engine flows, dashboards, training
schedule, new connectors, ideas for new use cases). The **strategic round** asks why: strategy, roadmap, reporting, security
announcements. Each lists input, content and trigger for action, for plant and central side. Each call ends with a call for action in
numbered steps with calendar weeks, a link set and an escalation line where management set a deadline. A Q and A form runs between
calls. Check the current cadence before copying an agenda (an early deck defines cadence, a later one shows the reduced real agenda).

### Plant tiering (capacity, not eligibility)

First mover = high estimated value, coverage of regions, segments and technologies, capacity and knowledge in the plant, integration
synergies, and a dedicated staffed key user. Fast follower = central support only when capacity allows, locally driven, limited
funding. Which rule wins when a late request meets a first-mover priority is `<to confirm>` (decks: first come first served against
a small set of first movers; the department definition is authoritative, the sector-level list is background).

### Integration workshop

Order the workshop by trigger: machine-integration workshop first when connectivity is missing, use-case workshop first when
machines are connected; a plant-dependent decision, not a habit. Skeleton: status of priority equipment and IT infrastructure,
project plan and budget, use-case requirements with production, engineering and continuous improvement (showing the same process
at other plants), plant tour, side topics, wrap-up. Preconditions on the IT side are in the equipment-integration practice file.
Hand-over: after the workshop a short block "prepare the hand-over to use-case support"; output is the machine list and baseline,
use cases per area, IT preconditions, next steps toward the capital request.

## 2 Decision rules

| Situation | Rule |
|---|---|
| Use case wanted on a machine that is not connected | Integration wave first; use cases only afterwards |
| Quality or lab dashboard, no machine connection | Separate path, owned by local quality; not in the integration sequence |
| Wave allocation conflict | State the rule used (request order or first-mover priority) on the plan, `<to confirm>` |
| Plant without staffed key user | Fast-follower support only; check the resource rating before committing the wave |
| Centralising data into a new environment | Warn that every workflow and connection at every location changes; use a per-location checklist |

## 3 Handoff contract

| Direction | Skill | Content |
|---|---|---|
| Receive | `od-requirements-breakdown` | Requirement, use-case demand per machine |
| Receive | `od-capital-request` / `od-investment-input` | Approved wave scope |
| Hand on | `od-use-case-support-service` | Connected machine list, remaining machines with blocker, hand-over note |
| Hand on | `od-analytical-support-service` | Standardized data, data period and quality notes |
| Hand on | `od-scorecard-reporting` | Plant status table, traffic light, call-for-action |
| Hand on | `od-barrier-triage` | Machines with no route, class and dependent use cases |

## 4 Pitfalls and lessons (lane level)

- **Tool without an operations concept.** The most repeated barrier in tool reviews. A machine can be connected and still have no
  system to send data to; escalate as a tool rollout decision and do not roll out on demand until the concept exists.
- **Cyber patches on controllers** blocked the second wave and the savings behind it: precondition, not a late gate.
- **Machine lists not updated** at most plants bound the response to a vulnerability notice and the wave plan.
- **Mixed ambitions.** Hard machines first burned reputation; scale known machine types.
- **Connecting more machines needs capable IT infrastructure first.** Do not size a wave beyond what the infrastructure carries.
- **More connected machines do not mean savings.** Equal integration effort with zero savings points to people and method.
  Good-practice signature: production proactively drives ideas, the ME asks for blueprints, requirements are formalised with OD,
  savings are calculated with controlling. Bad-practice signature: one engineer only responsible for the technical part,
  standards ignored, "we do not know how to calculate savings".
- **Missing ownership shows as silence:** no reply to follow-ups for weeks, unclear owner of an artifact registry. Treat a silent
  thread as an ownership gap and ask who is responsible for the connection, what other sites do, and what the alternative is.
- **Preconditions of a platform or server migration** (artifact registry, source-code host, firewall changes, cloud approval) must
  exist before it starts; a customer audit is a hard external deadline that outranks the internal plan.
- **Participation in the community call is a leading indicator:** low participation went with low understanding and low savings.

## 5 Questions to ask and definition of done

Questions: Which machines does an accepted use case need? Is the plant staffed with a key user? Is the infrastructure capable? Is the
controller patched and the sign-off scope known? Who runs the target system?

Done = the lane's existing definition of done, plus: plant status table current and dated, the savings project registered or its
absence flagged, remaining machines listed with blocker, hand-over note sent to use-case support.

## 6 AI agent operating notes

- **Can do** (`PROPOSAL`): draft the call pack from the portfolio and integration status lists (traffic light, call-for-action
  text, plants without registered savings project, stale tag lists); classify incoming feedback into the question-pack categories and
  route to the owning service line; build a blocker one-pager (technical, commercial, customer; options with separate decision,
  infrastructure and customer deadlines) from tickets and mail and highlight silent threads.
- **Inputs required**: Machine List export (dated), plant status lists, tool overview, savings-project register.
- **Evidence to cite**: list name and read date for every row.
- **Human gates**: the OD lead decides escalation wording and wave allocation; the plant confirms its status; nothing connects without
  sign-off.
- **Handover**: status table plus open items with owner roles.
