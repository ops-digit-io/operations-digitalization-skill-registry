---
type: Skill Reference
title: Process chain practice
description: How the use case support lane is run end to end in the AI-driven chain - the flow blocks with preconditions, the use-case sprint, the standard deliverable set, utilization and savings tracking, handoffs between blocks and agent operating notes.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, lane, process-chain]
derived_from:
  - Operations Digitalization slide decks (support-service flow, sprint reviews, community calls, priorities and strategy decks), abstracted into process guidance; no figures.
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - support service lane

Adds to the seven-step happy path in `SKILL.md`. `PROPOSAL` marks synthesis that no deck states.

## Where it sits

Lane 2 (steps 21 to 26) and the use-case half of Lane 1. This file explains how the lane's blocks hang together
and what each block must have before the next starts. Each step has its own skill; this lane routes to them.

## 1 · Method in practice

**Flow blocks, each with a trigger and an in/out.** The updated flow stresses preconditions, data-model
integration and knowledge sharing. Map to the chain:

| Flow block | Chain step | Skill |
|---|---|---|
| Preconditions for process start | i1 | `od-use-case-intake-triage` |
| Use case workshop | 21 | `od-workshop-facilitation`, `od-use-case-definition` |
| Benefits analysis | 24 | `od-benefit-calculation` |
| Preconditions for development start | 22 | `od-requirements-breakdown`, `od-data-availability-check` |
| Data collection and exploration; data-model integration | 22 / 3b4 | `od-data-availability-check`, `od-signal-standardization` |
| Use case development | 23 | `od-prototype-poc`, `od-analytics-asset-build` |
| Preconditions for deployment; deployment | 26 | `od-acceptance-test`, `od-handover-and-adoption` |
| Documentation, knowledge sharing, lessons learned | 26 | `od-use-case-standardization`, `od-use-case-promotion` |
| Benefits and savings tracking against the plant savings project | spine | `od-portfolio-and-savings-analysis`, `od-scorecard-reporting` |

`<to confirm>`: the deck pages for this flow carry block titles only (the pictures were not extracted); the
mapping above is this registry's reading. Content must come from the skills, not from the slide titles.

**Each block ends in a precondition for the next.** Write the precondition as "what must exist before the next
block starts". `PROPOSAL`: the agent drafts a definition of done per block from the precondition pages.

**Workshop series as a fast lane.** For a family of ideas (for example predictive maintenance): a workshop series
with the central engineering interface and selected local heads collects ideas; each idea is described on a
canvas; a go / no-go rating follows; a potential analysis is produced and captures tool demand. Process-focused
analyses add scope per process, scaling factors, actual KPI deviations and rollout locations.

**Focus order for definition work:** unassessed plants first, unassessed savings first. The KPI of the definition
step is "identified use-case potential", not implemented savings.

**Use-case sprint (execution).**
- Length: a time-boxed sprint of a few weeks after the workshop; later practice re-plans per longer period as a
  continuous activity with the plant key user in the team. `<to confirm>`: decks show a shorter and a longer
  standard; take the current one from the OD lead.
- Rhythm: one weekly review, one or two technical meetings a week, a mid-sprint status, a sprint-end review with a
  Q&A / feedback link. Inputs: targets, savings baseline, plan, data access, input and transformation steps.
- Standard deliverable set: generic process-value dashboard for all machines; Andon board (status plus history);
  operations dashboard (output, cycle time, alerts per time group or shift); machine availability by mode; alert
  dashboard; one process-specific dashboard as blueprint; SPC for inline measurement; the transformation flows
  with documentation. Order the views "overview to in-depth": Andon for stakeholders, operations dashboard for
  technicians, process-value dashboard for process engineers.
- Review against: what was carried over from another plant, what is blocked, what is a rollout option.
- Sprint definition of done: dashboards live, flows and dashboards documented, scalability statement, open
  topics list, impact of IT issues stated.

**Utilization loop taught to plants:** connect high runners and trouble-makers first, run use cases, select
parameters, analyse (parts, utilization, downtime), find root cause with a known method, create and calculate a
cost-saving project, eliminate deviations. Adoption means the use case is **integrated into a standard
operating procedure with dashboards and escalation flows**, not "dashboard live".

## 2 · Decision rules

- **Standard versus special:** see `od-use-case-intake-triage` (`references/process-chain-practice.md`).
- **Three-way bucket per use case:** just do / go forward / lead change; just-do items are copied from the
  library and need no new development.
- **Registration gate:** savings count only against a registered plant savings project with a baseline and an
  owner. A use case without a registered project is invisible to the savings ledger. Register a project for
  what is already implemented rather than waiting.
- **Savings are not rollout count.** Rollout count and savings are separate metrics; the widest-scaled cases
  often show no tracked saving, and savings concentrate in cases that attack a real cost driver. A scaled
  use case with deployments but no savings is "to be evaluated" until investigated, not "no potential"; only a human (the OD lead
  with the plant owner) may decide "no potential"; an agent never writes it.
- **Staffing assumption** is written next to every savings projection (central staffing only versus central plus
  dedicated plant key users).
- **Scope growth:** a requirement beyond the sprint frame becomes an additional use-case phase.
- **Quality dashboards independent of machine connectivity** follow the quality path, not the integration path.
- **Service gap:** a tool with no operations concept (owner, SLA, support level) is not rolled out; mark the use
  case blocked and route it to strategy (already in the error paths).

## 3 · Handoff contract

| From | To | Must travel |
|---|---|---|
| Intake | Definition | Shaped statement, class, lane, plant tier |
| Definition | Requirements | Demand row (plant, process group, capability, moment of use, owner, savings-basis label, tool and machine dependency, data by source) |
| Requirements | Integration lane | Requirement with lane variant (see `od-requirements-breakdown`) and business case |
| Integration | Sprint / build | Machine connected, signals selected, architecture and user access agreed |
| Sprint | Handover | Deliverables, flow documentation, open topics, impact of IT issues, scalability statement |
| Handover | Utilization review | Utilization table row per use case (name, who uses it, related process, method, rate, impact, plant-management relevant) |

Agree architecture and user access **before** the sprint starts: firewall changes and unclear access cost weeks.
Notification channels and data historization are IT changes; request them early. Keep flows in version control and
check the redeployment impact before upgrading the flow runtime.

## 4 · Pitfalls and lessons

- Deployed is not used; many scaled cases ran with no reported saving. Add a utilization check to every handover.
- Sprint reviews that start without a savings baseline never report a saving.
- A rollout of a dashboard to another process is gated by machine integration and tag selection, not by the dashboard.
- Single-file flow structures are brittle and do not modularise; enforce documented, reusable flows.
- IT architecture changing mid-sprint and an expert missing for the process are the two recurring delays.
- Savings reported incompletely make a target look missed while delivery count is on target; separate unreported
  savings from non-utilized potential.
- Plants that realise savings show production proactively driving ideas, the ME asking for blueprints, formal
  requirements with OD, savings calculated with controlling. Plants that do not: "only responsible for the
  technical part", standards ignored. Use as a readiness check.

## 5 · Questions to ask / definition of done

Per block: which precondition is met, by whom, with which evidence. Done for the lane: as in `SKILL.md`, plus a
utilization table row per live use case and a registered savings project (or an explicit "none, because ...").

## 6 · AI agent operating notes

- **Can do:** keep a sprint board from the deliverable list (available / ongoing / blocked / rollout option);
  draft the sprint-end summary and propose which blueprint to carry over; list use cases without a registered
  savings project; maintain the utilization table fields from call notes and chase open homework; draft the
  per-block definition of done.
- **Required inputs:** use-case list, machine list, savings ledger, flow documentation and dashboard links, with
  read dates.
- **Human gates:** DBVE and Plant ME agree the business case and priority; the OD lead sets wave and sprint
  length; the plant key user confirms the standard procedure that uses the use case.
- **Evidence to cite:** list row, ledger row, flow documentation, dashboard link, read date.
- **Hand over:** per the table in section 3; state which skill is next and what is still `<...>`.
