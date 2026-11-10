---
type: Skill Reference
title: Procedure
description: Formerly the skill od-machine-integration-plan, absorbed into od-equipment-integration on 2026-11-10 to remove duplication against the department context. Plan a machine-integration wave from the machine list to flow design - scale known machine types with at most one unknown type per deployment, sequence the wave with the weekly capital-request micro-process, prepare the integration workshop, pick the connector and route per machine type, test readiness, and keep a barrier log that states the cost of not deciding. Drafts the plan and checklists; plant, OD lead and forums decide. Use when a plant or region starts or re-plans a wave, when a machine list must become an integration plan and a capital request, when an integration workshop is being p
resource: ../../SKILL.md
status: draft
owner: human:jakob.gabriel
tags:
- information-integration-service
- practice
- wave-planning
- draft
- absorbed
derived_from:
- Operations Digitalization slide decks (machine-integration waves, integration workshops, community-of-practice calls, connector and architecture decks), abstracted into process guidance; no figures.
generated:
  by: claude-code/1
  at: 2026-11-05 00:00:00+00:00
---
# Machine integration plan

> **Absorbed.** This was the skill `od-machine-integration-plan`. It now runs as a mode of [`od-equipment-integration`](../../SKILL.md) (merged 2026-11-10, see `log.md`). Its authority stays as it was: draft.

Read `od-context` first. This skill turns a **machine list** into an **integration wave plan** that can
be sized, funded, run and handed over. It plans; it does not assess a single machine
(`od-equipment-integration`), classify a stuck machine (`od-equipment-integration`), build the flow
(`od-node-red-flow-builder`) or write the request (`od-capital-request`). It decides what goes into the
wave, in which order, with which route, and what must be true before the plant kicks off.

## Where it sits in the chain

| Step id | Role of this skill |
|---|---|
| 3b4 Connector and pipeline | Main home: machine list, machine CV, integration plan, tag list, flow design handoff |
| 1b3 Order and connect (standardized system) | Wave slot, readiness test before ordering |
| 22 Features and data check (machine demand) | Which machines the use case needs; wave candidates |
| 25 / 33 Capital request | Supplies the machine list, route and cost per machine; the request is milestone 1 of the wave |
| 3b5 / 3b6 | Readiness and barrier log carry on to procurement and acceptance |

Upstream: `od-use-case-intake-triage` (lane), `od-data-availability-check` (which machines lack data),
`od-workshop-facilitation` (the workshop where the list is finalised). Downstream:
`od-capital-request`, `od-equipment-integration` Route B per machine, `od-signal-standardization`,
`od-node-red-flow-builder`, `od-acceptance-test`, `od-cybersec-gate`.

## Purpose and definition of done

Done when: the machine list is complete enough to plan (see readiness); every machine has a type, a
route and a rough cost line; the wave obeys the **scale-known-types rule**; the plant has a named
kick-off date, a staffed team and a place in the weekly micro-process; the integration workshop is
prepared (checklist green or gaps owned); and every barrier is in the log with an owner and, where a
decision is missing, its cost of non-decision.

## References and assets

| File | Use it for |
|---|---|
| [`references/wave-planning-and-readiness.md`](references/wave-planning-and-readiness.md) | The scale rule, wave allocation, the weekly micro-process, status taxonomy, phase sequence, readiness criteria |
| [`references/route-choice-per-machine-type.md`](references/route-choice-per-machine-type.md) | Connector and route per machine type: data classes, edge or not, low-cost pattern, legacy and camera cases |
| [`references/barrier-log-and-cost-of-non-decision.md`](references/barrier-log-and-cost-of-non-decision.md) | Barrier log fields, relation to triage, the cost-of-non-decision line, the rapid decision board |
| [`assets/wave-plan-template.md`](assets/wave-plan-template.md) | Wave plan: machine list and CV fields, route and cost per machine, plant status row, readiness, barrier log |
| [`assets/workshop-prep-checklist.md`](assets/workshop-prep-checklist.md) | Preparation checklist for the equipment-integration workshop |

## Procedure

1. **Frame the wave.** One plant or area, one budget class, one kick-off. Prefer whole processes or
   areas over scattered machines, and reuse existing infrastructure (`wave-planning-and-readiness`, section 5).
2. **Take the machine list as the backbone.** Add the machines, optionally state the method, and fill
   the machine CV (PLC program, version history, vendor). Gaps stay `<unknown>` and become questions.
   `od-data-availability-check` tells you which machines the waiting use cases really need.
3. **Group by machine type and apply the scale rule.** Known types (a controller family with a proven,
   documented process) form the bulk of the wave. Allow **at most one unknown type per deployment**. Do
   not front-load the difficult machines and leave plants the easy ones: that pattern failed.
4. **Check layout stability and preconditions.** Machines being moved, a pending controller patch, a
   missing network drop or an IT platform that cannot carry more machines go into the barrier log now,
   not at the second wave.
5. **Choose the route per machine type** with `route-choice-per-machine-type`: native OPC-UA, aggregation
   server, edge device, low-cost address translation, or a custom connector. Run Route A/B of
   `od-equipment-integration` for the detail of each machine.
6. **Prepare the integration workshop** with `assets/workshop-prep-checklist.md`; IT and OT are assessed
   in separate meetings.
7. **Estimate time and cost per machine** (hardware, software, IT/OT work, plant capacity per phase) and
   hand the lines to `od-capital-request` (through `od-investment-input` where it is used). Run the
   compatibility check before the cost line, not after.
8. **Enter the weekly micro-process** for the wave and set the status colour per plant.
9. **Keep the barrier log** and state the cost of non-decision for every barrier that waits on a decision.
   Classify stuck machines with `od-equipment-integration`; escalate decisions with `od-decision-routing`.
10. **Hand over** per machine to `od-equipment-integration` Route B, then tag list,
    `od-signal-standardization` and flow design; at the end of the wave recommend the next wave and the
    training for self-service.

## Handoff contract

Receives: use-case demand and machine need (`od-use-case-intake-triage`, `od-data-availability-check`),
machine list and CVs from the plant, the lane decision. Hands on: machine list with type, route, cost
and status; the plan and workshop output to `od-capital-request`; the barrier log to `od-equipment-integration`
and `od-risk-watch`; per-machine guidance work to `od-equipment-integration`. Nobody should re-ask for
the machine list, the route or the kick-off date.

## AI agent operating notes

- **Can do:** draft the wave plan from the machine list and PLC exports; group machines by type and mark
  the unknown type(s); propose a route per type with the cited rule; pre-fill the CV and the tag-list
  proposal; check workshop preparation items; produce the status table; compute the cost-of-non-decision
  line from the portfolio and cite the read date.
- **Must cite:** the machine-list record, the rule used (scale rule, route rule) and the source of each
  cost line. Own synthesis is marked `PROPOSAL`, unknowns `<...>`.
- **Human gates:** wave scope and allocation (OD lead with the plant), route where it changes cost,
  Cyber Security approval (`od-cybersec-gate`), the capital request, barrier decisions.
- **Never:** connect, patch, write to a PLC, open firewall rules, or print numbers it did not read live.
- **Hands over:** the plan file, the open-questions list and the barrier log, each with owner and date.

## Still open

- `<Budget classes>`: class names follow the systems needed; their limits are `<look up in the current approval policy>`.
- `<Capacity per phase>`: meetings per phase are known only qualitatively.
- `<Barrier log location and form>`; `<who convenes the rapid decision board>`.
- Back-out plan content per platform component: the sources hold diagrams only, `<...>`.

## Do not

- Do not front-load the hardest machines, or mix several unknown machine types into one deployment.
- Do not connect, patch or approve an external connection; do not start a wave without a staffed team and a started Cyber Security path (it runs in parallel and blocks only go-live).
- Do not leave a machine out of the wave without a logged barrier and an owner.
- Do not quote counts, plant statuses or budgets from this skill: read them live from the machine list and the status report.
- Do not call a plan final while the machine list is unreviewed.
