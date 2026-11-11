---
type: Skill Reference
title: Outputs
description: The outputs ops-event-model must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`ops-event-model` delivers the reduction of a plant request to objects, events and a time axis, with an archetype class and a data requirements statement for the data platform. The skill is not done until a sensor value is no longer passed off as an event.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Event definition canvas | `assets/event-definition-canvas.md`, one per use case | `funnel-use-case`, `funnel-requirements` | Request restated as object(s), event(s) and time axis; every event marked source event or derived event with the method named; every signal classified as sensor value, event or object identifier |
| Object relation | Section of the canvas | `mi-data-availability` (if a gap) | Identifier source for serial, order, part, batch or recipe is named, or the relation is routed as a data gap, never approximated from timestamps |
| Archetype class, category, method, ETL list | Section of the canvas | `catalog-standardization`, `ops-analytics-asset`, `mi-flow` | Class is cross-process, per-process or unique; category to method to ETL mapping drafted; new ETL work stated |
| Data requirements statement | `assets/data-requirements-statement.md`, filled | Data platform and information-integration lane, `mi-signals` | Written and handed on; open questions for the plant listed |

## Handoff

- **Receives from:** `dept-intake` and `funnel-use-case` (the accepted demand in the plant's words, owner role, the decision that follows), `mi-data-availability` and `mi-equipment` (tag list, PLC metadata, machine connected or not).
- **Next in the flow:** `funnel-use-case`, `funnel-requirements` and `mi-signals`; `mi-data-availability` for a missing relation; `catalog-standardization` and `ops-analytics-asset` for archetype and method. Proposed on steps i1, 21 and 22 of `docs/new-state/process.yaml`.
- **Stops here when:** purpose, objective, timeframe or a named stakeholder is missing (back to `dept-intake`), the case is unique (impact analysis first, the OD lead or DBVE decides), or a derived event has no named method. Do not promise a trace or per-order analysis without the object relation.
