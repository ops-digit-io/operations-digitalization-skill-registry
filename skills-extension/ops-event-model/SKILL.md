---
name: ops-event-model
description: >-
  Reduce a plant request that looks unique to the objects, events and time axis it is really about, decide which
  signals are events and which are only sensor values, check that the time-series can be related to a product or
  order, and map the use case to an archetype (cross-process, per-process, unique), its methods and its ETL jobs,
  ending in a data-requirements statement for the data platform. A sensor value is not an event. Use when a request
  asks "which carrier is in the oven", "which serials with quality status", "which order and how many defects",
  when a traceability demand has no stated technical requirement, when the object relation is the suspected
  blocker, or before a use case is handed to requirements, build or standardization.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: ops-event-model
  aliases: [od-event-object-modelling]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Intake (i1), Lane 2 (21, 22)"
  new_state_step: "Classify the demand into exactly one lane; Capture the idea, process diagnostics; Requirements, features and data check"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  requires: [dept-context]
  composes: [dept-intake, funnel-use-case, funnel-requirements, mi-signals, mi-data-availability, ops-analytics-asset, catalog-standardization, catalog-compatibility]
  okf:
    type: Agent Skill
    title: Object and event modelling
    tags: [all, practice, new-state, draft]
---

# Object and event modelling

Read `dept-context` first.

## Purpose and definition of done

Plant requests arrive in plant words ("which carrier is in the oven now", "all serials produced today with
quality status", "which order ran yesterday and how many defects", "machine errors by station with reason code").
Each sounds unique. Most reduce to a few **objects** (part, serial, order, tool, recipe, batch, carrier), the
**events** that happen to them (NOK part, error, setup, tool break, stop) and a **time** axis. This skill does
that reduction on purpose, so the use case gets a category, a method and a data requirement instead of staying a
"need without a specification".

Done when:
- the request is restated as object(s), event(s) and time axis, in the
  [event definition canvas](assets/event-definition-canvas.md);
- every event is marked **source event** (boolean/discrete tag or system record) or **derived event** (needs event
  processing on a raw series, with the method named), never a bare sensor value;
- the **object relation** (serial, order, part, batch, recipe to the time-series) has a named identifier source
  or is routed as a data gap;
- the use case has an **archetype class** (cross-process, per-process, unique) and the category to method to ETL
  mapping is drafted;
- the [data requirements for the data platform](assets/data-requirements-statement.md) are written and handed on.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Where it sits in the chain

| Step id | Role of this skill |
|---|---|
| `i1` Classify the demand | Optional first cut: object/event/time pre-classification of intake text, archetype guess (`dept-intake` owns the lane routing) |
| `21` Define and diagnose | Reduce the statement; fill the canvas fields for data (`funnel-use-case`) |
| `22` Features and data check | Main home: runs between `funnel-requirements` and `mi-data-availability`; names the missing relation before the data check walks the path |
| `26` Standardize | Category, method, ETL job layer that makes an archetype executable (`catalog-standardization`) |
| `3b4` Connector and pipeline | Data-class hub choice and identifier signals when a new machine is connected (`mi-signals`, `catalog-compatibility`) |

Not a step of its own in `process.yaml`: it is a method used inside these steps. `PROPOSAL`: place it as a
named skill at step `22`.

## References and assets

| File | Use it for |
|---|---|
| [`references/object-event-reduction.md`](references/object-event-reduction.md) | The reduction method, the "sensor value is not an event" rule, event-log vocabulary, the object-relation check, questions to ask |
| [`references/archetype-method-etl.md`](references/archetype-method-etl.md) | Cross-process / per-process / unique, category to method to ETL, data classes and hubs, data-model choice, platform requirements |
| [`references/worked-examples.md`](references/worked-examples.md) | Illustrative reductions and a cycle-time case |
| [`assets/event-definition-canvas.md`](assets/event-definition-canvas.md) | The canvas, one per use case |
| [`assets/data-requirements-statement.md`](assets/data-requirements-statement.md) | What the data platform and the integration lane must provide |

## Procedure

1. **Take the request as the plant said it.** Keep the plant's sentence; do not rewrite it yet. If purpose,
   objective, timeframe or a named stakeholder is missing, send it back for alignment (`dept-intake`,
   `funnel-first-aid`) before modelling.
2. **Reduce to object, event, time.** Fill sections 1-3 of the canvas: which objects the answer is keyed on, which
   events happen to them, and which time axis (live view, report on a cadence, a record to be entered).
3. **Classify each signal.** For every data point the answer needs: sensor value, source event, derived event,
   or object identifier ("objects often hide as strings inside the series"). Derived events get a named method
   *before* the analysis is promised.
4. **Check the object relation first.** Time-series always relates to product or production metadata. Ask whether
   machine time-series plus the standard base data model is enough, or whether serial, part, order, batch or recipe
   is required. Look at what the PLC already carries before waiting for a foreign system. No identifier source
   means a data gap: route it through `mi-data-availability`, do not approximate.
5. **Check sharpness.** Are sampling resolution and product characteristics fine enough for the question? Does
   the plant plan per machine or per cell, and does the model carry that level?
6. **Set the archetype class.** Cross-process, per-process or unique (see the reference) and the action that
   follows. Unique: do not start; impact analysis first.
7. **Map category to method to ETL job.** Name the category, its methods, and the transformation jobs each method
   becomes. Say which ETL work is new. ETL is the hidden cost: plan it explicitly.
8. **Pick data class and hub** per signal group (transactional, time-series, master data) and the route to the
   platform; hand signal questions to `mi-signals`.
9. **Write the data requirements statement** and hand over (below).

## Handoff contract

| Receives | From |
|---|---|
| Accepted demand in the plant's words, owner role, the decision that follows from the number | `dept-intake` / `funnel-use-case` |
| Tag list, PLC metadata, machine connected or not | `mi-data-availability`, `mi-equipment` |

| Hands on | To |
|---|---|
| Canvas plus archetype class and category | `funnel-use-case` (canvas data box), `catalog-standardization` |
| Event, identifier and relation requirements per signal | `funnel-requirements` (requirement and acceptance criteria), `mi-signals` |
| Missing relation or identifier named as a data gap | `mi-data-availability`, then the Information Integration lane |
| Method and ETL list, asset type hint | `ops-analytics-asset`, `mi-flow` |

## AI agent operating notes

- **Can do:** classify intake text into object / event / time; list candidate identifiers and events from a pasted
  tag list and PLC metadata; mark which events are source vs derived; draft the canvas, archetype guess and
  data requirements statement; flag "missing identifier source" and empty canvas boxes as `<...>`.
- **Inputs needed:** the plant's original sentence, tag list or datapoint export, PLC metadata or asset structure,
  whether an MES or ERP exists at the plant, planning level (machine or cell).
- **Human gate:** the key user confirms the identifier source and the event definition; the OD lead or DBVE
  decides whether a unique case gets an impact analysis. The agent never promises an analysis on a derived event
  whose method is unnamed.
- **Evidence to cite:** the tag or signal name, the canvas box, the source statement in the request. Unverified
  items stay `<to confirm>`.
- **Hands over:** the filled canvas and requirements statement, with open questions listed for the plant.

## Still open

- `<Whether this becomes its own step id or stays a method inside 22>`: owner of `process.yaml`.
- `<Who owns the method catalogue per category>` once archetypes exist: OD lead.
- The decks assess an object-centric event log as an affordable option; no deck states a platform decision for
  it. `<to confirm>` with the data-platform owner before recommending it as a standard.
- Whether the share of use cases that need production metadata is still small: `<to confirm>`, re-count from the
  use-case list; do not quote an old share.

## Do not

- Do not treat a sensor value as an event, or promise a trace or a per-order analysis without the object relation.
- Do not approximate a missing order or serial relation from timestamps and call it traced.
- Do not start a unique case without the impact analysis; do not rebuild a cross-process case per plant.
- Do not choose a data model before the object and event questions are answered.
- Do not hide ETL effort; do not model every signal, only those the question needs.
- Do not change a signal standard to fit one machine (`mi-signals` decides).
