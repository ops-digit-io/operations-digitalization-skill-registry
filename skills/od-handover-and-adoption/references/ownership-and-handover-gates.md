---
type: Skill Reference
title: Ownership and handover gates
description: "The OD x IT rules for who runs an application and when ownership moves (2026-09-11): build-and-run, formal acceptance, the handover checklist, shared responsibility, criticality gates, and the recurring self-assessment."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [handover, ownership, it-alignment, lane-3]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/Transcripts/2026-09-11_OD-IT-alignment_meeting-notes.txt (themes 3 and 5, action items 5 and 7), read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Ownership and handover gates

Agreed direction from the OD x IT alignment of 2026-09-11. The formal gates are an open IT action item
(IT and the OD lead: "ownership and handover gates based on locality, operational criticality,
technology alignment, observability, backlog status, maintenance readiness and shared-responsibility
boundaries"). Use these rules now and mark the gate definition ⟨to confirm⟩ until it is published.

## Build and run

The team that builds a solution runs it. A model where one group builds and another operates without the
knowledge is rejected. A business team may run a **simple local** application itself when the platform
gives security, connectivity, logging and the other controls out of the box.

## Ownership moves only on formal acceptance

Until the receiving team formally accepts the application, the current owner stays responsible for
support and operation. The receiving team needs time to understand the implementation, review the backlog
and confirm the operational controls. The current owner closes missing mechanisms (for example logging)
**before** the receiving team takes over.

## Handover checklist

| Item | The receiving team checks |
|---|---|
| Legacy status | Is it, or does it replace, a legacy application; is it on the legacy inventory |
| Backlog | Open items, who owns them, what is promised |
| Version currency | Runtime, libraries and platform versions current |
| Architecture | Components, hosting, interfaces, data flows |
| Business logic | What it does and why, written down (the requirement) |
| Logging | Present and usable |
| Observability | Health, alerts, dashboards for operations |

## Shared responsibility

For complex applications, involve IT from the start instead of relying on a late handover.
Responsibility can be split: the business investigates business-data issues; IT handles platform
failures and full outages.

## Criticality gates

Locality alone does not decide. A locally built application still needs IT involvement when it is
operationally important or could cause significant financial impact. Technology alignment and whether
engineers who know the stack are available also decide whether ownership can move.

## Recurring self-assessment

Production owners run a lightweight self-assessment every six or twelve months: architectural alignment,
maintainability, backlog and upgrade status, observability, current IT practices, and whether the
application should stay in production. The format is an open action item (IT and the OD lead).

## No delivery dates without commitment

IT gives no delivery date unless a team has formally committed the work in sprint, PI or comparable
planning. OD does not pass on informal forecasts to the plant (the Gemba app lesson).
