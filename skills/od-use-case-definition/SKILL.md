---
name: od-use-case-definition
description: >-
  Define a plant use case so it can be built, standardized, handed over and measured —
  scope it against the plant's process, break down the requirement, assess the (legacy)
  MF IT systems it touches, place it on its capability template and process group, and
  record the fields that make it findable and evaluable later. Also covers preparing and
  running Use Case Definition and Use Case Integration workshops. Use when a plant demand
  has been accepted and needs turning into a defined use case, when an existing use-case
  record is too thin to act on, or when a definition or integration workshop is being
  prepared.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-use-case-definition
  tier: practice
  lane: use-case-support-service
  owner_role: Digital-Business-Value-Engineer (DBVE)
  authority_level: draft
  status: stable
  sources_read: 2026-08-10
  requires: [od-context]
  composes: [od-use-case-standardization, od-benefit-calculation, od-data-availability-check]
  derived_from:
    - ops-knowledge-graph/.../20-lanes/use-case-support-service/{playbook,tasks}.md
    - ops-knowledge-graph/_knowledge/10-Department/Use case lifecycle.md
    - ops-knowledge-graph/_knowledge/10-Department/Use case standardization.md
  okf:
    type: Agent Skill
    title: Use-case definition
    tags: [practice, use-case-support-service]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Use-case definition

Read `od-context` first. Every use case is **one plant's instance of one need** — never a
programme, never a plant-wide ambition.

## The coordinate every use case carries

1. **Plant** — one of 33 (20 Europe, 9 Americas, 4 Asia).
2. **Material family / process group** — Rubber, Plastic, Metal or Assembly, and one of
   29 process groups inside them.
3. **Capability** — one of eleven cross-plant templates: Andon Board, OEE Calculation,
   Downtime Reporting, Process Quality Data, Machine Alerts, Cycle Time, Recipe Values,
   Process Values, Manual Quality Data, Analytics, Other Use Cases.

Without all three, the use case is not findable from another plant, which is the whole
reason the taxonomy exists. Every capability is already instantiated at 32 or 33 of the
33 plants — the template is never the thing that is missing.

## The states it will be tracked in

Set expectations at definition time, because these fail separately:

- **Delivery status** — `IDEA` → `PLANNED` → `IMPLEMENTED` → `PRODUCTIVE` (or `STOPPED`).
- **Three workflow states, tracked independently** — development, implementation,
  handover. Handover consistently trails the other two by about thirty use cases across
  the portfolio; that is the normal shape, not an anomaly to explain away.
- **Rollout phase** — `PHASE 1`…`PHASE 5`, named rollout batches usually tied to a plant
  project, not sequential queues.
- **Category** — standard cross-process · standard per-process · non-standard unique to
  one plant · AI use case. **This declaration is the hinge the whole function turns on**:
  declaring "standard" commits the use case to `od-use-case-standardization`.

## Procedure

1. **Confirm the need is one need.** If it decomposes into two decisions taken by two
   people at two moments, it is two use cases.
2. **Name the moment in the day it belongs to** — the Gemba walk, a shift check, an
   escalation. A use case that is not consumed inside a ritual is a use case nobody will
   open; see the daily-Gemba pattern (125 of the 202 use cases recording a utilization
   rate are used **daily**).
3. **Run process diagnostics** to get from the stated problem to the actual one, and
   record the analytical insight that justifies the scope.
4. **Break down the customer / process requirement**, and **assess the (legacy) MF IT
   systems** it touches. 268 legacy applications are tracked as being replaced or
   retired — check whether the need is already served by one being retired.
5. **Check the data exists** → `od-data-availability-check`. A use case whose data is not
   readable is an integration request first; record that dependency now.
6. **Check the library before specifying** → `od-use-case-standardization`. Take a proven
   entry rather than starting from a blank page.
7. **Record the fields that make it evaluable**: output asset (Dashboard / Analytics /
   Report / App / Agent), business process, utilization expectation, plant owner by name,
   and every known dependency. A title alone is not a definition.
8. **Prioritize** with the business case → `od-benefit-calculation`.

## Workshops

| Workshop | When | Template |
|---|---|---|
| Use Case Definition Workshop | Plant onboarding or a new demand wave | Standard Agenda — Use Case Workshop (SharePoint) |
| Use Case Integration Workshop | Use case ready for integration | Use Case Integration Workshop agenda |

Locations on record for past workshops: Northeim, Dolne Vestenice, Carei, Timisoara,
Andrezieux, Subotica, Karben. ⟨A dedicated OD use-case one-pager / business-case template
is not confirmed to exist — to confirm or create.⟩

## Definition of done

The use case is scoped with a clear objective, its requirement is broken down, its system
assessment is complete, and it carries plant, capability, process group, category, output
asset, utilization expectation, a named plant owner and its dependencies.

## Do not

- Do not record `UNKNOWN` priority or potential as though it were low. 362 use cases
  carry `UNKNOWN` priority and 405 `UNKNOWN` potential; absence is not an answer.
- Do not declare a use case `standard` to make it look scalable. The CSP gate will not
  agree, and the declaration is what the rollout economics rest on.
- Do not write a definition that only its author can read. The handover test applies from
  the first draft: what is this, where does its data come from, who owns it.
