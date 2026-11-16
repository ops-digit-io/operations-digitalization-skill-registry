---
name: ops-event-model
description: >-
  Turn a plant request that looks unique (which carrier is in the oven, which serials with quality status, which order and how many defects) into what the data platform must provide: the objects, events and time axis, which signals are real events and which are only sensor values, whether the time-series can be tied to a product or order, the use-case archetype (cross-process, per-process, unique) with its methods and ETL jobs, ending in a data-requirements statement. Use when a traceability demand has no technical requirement, the object relation is the suspected blocker, or before a use case goes to requirements, build or standardization. Not for naming signals (mi-signals) or checking collection (mi-data-availability).
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

- Read `dept-context` first.
- Terms: **object** = what the answer is keyed on (part, serial, order, carrier); **event** = something that happens to an object; **signal** = a tag or data point; **sensor value** = a continuous reading that is not yet an event.

## Purpose

- Plant requests arrive in plant words ("which carrier is in the oven now", "all serials produced today with quality status", "which order ran yesterday and how many defects", "machine errors by station with reason code").
- This skill reduces such a request to objects, events and a time axis, so the data question is clear before data check, requirements or build.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

- **In:** the plant's original sentence, the tag list or data-point export, PLC metadata or asset structure, whether an MES or ERP exists at the plant, planning level (machine or cell).
- **Out:** the filled [event definition canvas](assets/event-definition-canvas.md) and the [data requirements statement](assets/data-requirements-statement.md), with open questions for the plant.

## Where it sits in the chain

| Step id | Role of this skill |
|---|---|
| `i1` Classify the demand | Optional first cut: object/event/time pre-classification of intake text, archetype guess (`dept-intake` owns the lane routing) |
| `21` Define and diagnose | Reduce the statement; fill the canvas fields for data (`funnel-use-case`) |
| `22` Features and data check | Main home: runs between `funnel-requirements` and `mi-data-availability`; names the missing relation before the data check walks the path |
| `26` Standardize | Category, method, ETL job layer that makes an archetype executable (`catalog-standardization`) |
| `3b4` Connector and pipeline | Data-class hub choice and identifier signals when a new machine is connected (`mi-signals`, `catalog-compatibility`) |

## Procedure

1. **Take the request as the plant said it.** Keep the plant's sentence; do not rewrite it yet.
   - If purpose, objective, timeframe or a named stakeholder is missing, send it back for alignment (`dept-intake`, `funnel-first-aid`) before modelling, because a vague question has no testable event.
2. **Reduce to object, event, time.** Fill sections 1-3 of the canvas: objects, events, time axis (live view, report on a cadence, a record to be entered).
   - Open `references/object-event-reduction.md` for the method and questions to ask.
3. **Classify each signal.** For every data point the answer needs: sensor value, source event, derived event, or object identifier ("objects often hide as strings inside the series").
   - Name the method of a derived event *before* the analysis is promised, because an unnamed method is an unestimated effort.
4. **Check the object relation first.** Time-series always relates to product or production metadata.
   - Ask whether machine time-series plus the standard base data model is enough, or whether serial, part, order, batch or recipe is required.
   - Look at what the PLC already carries before waiting for a foreign system.
   - No identifier source means a data gap: route it through `mi-data-availability`, do not approximate.
5. **Check sharpness.** Are sampling resolution and product characteristics fine enough for the question? Does the plant plan per machine or per cell, and does the model carry that level?
6. **Set the archetype class** (cross-process, per-process or unique) and take the action that follows; open `references/archetype-method-etl.md`. Unique: do not start; impact analysis first.
7. **Map category to method to ETL job.** Name the category, its methods and the transformation jobs each method becomes; say which ETL work is new. ETL is the hidden cost: plan it explicitly.
8. **Pick data class and hub** per signal group (transactional, time-series, master data) and the route to the platform (`references/archetype-method-etl.md`); hand signal questions to `mi-signals`.
9. **Check before handover** with the checklist below, then write the data requirements statement and hand over.

## Example

- A fully filled reduction (fictional tags and names; more in `references/worked-examples.md`):

```text
Plant sentence : "Which carrier is in the oven now?"            (fictional)
Objects        : carrier (id), part serial
Events         : carrier enters oven (source event: boolean tag OVEN_ENTRY), carrier leaves oven (source event: OVEN_EXIT)
Time axis      : live view
Signals        : CARRIER_ID (object identifier, string in the series), OVEN_ENTRY, OVEN_EXIT (source events),
                 OVEN_TEMP (sensor value: not an event)
Relation       : carrier to part serial: recorded only by manual entry -> data gap, routed to mi-data-availability
Archetype      : per-process (the oven type recurs); category: traceability; method: join entry and exit per carrier
ETL            : new job "carrier dwell per oven" (stated as new work)
Open           : who confirms that CARRIER_ID is unique per shift (key user, to confirm)
```

## Check before handover

- [ ] The request is restated as object(s), event(s) and time axis in the canvas
- [ ] Every signal is classified (sensor value, source event, derived event, object identifier)
- [ ] Every derived event has a named method; every source event names its tag or system record
- [ ] The object relation has a named identifier source or is routed as a data gap
- [ ] Archetype class set; category to method to ETL mapped; new ETL work stated
- [ ] Data class and hub chosen per signal group
- [ ] Open items marked `<to confirm>` with the role that answers them
- If an item fails, fix the canvas, re-run the list, and only then hand over.

## Definition of done

- The checklist above is fully ticked or its open items are named, the data requirements statement is written and handed on, and no analysis is promised on a derived event whose method is unnamed.

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

## Human gate and AI-agent notes

- **Can do:** classify intake text into object / event / time; list candidate identifiers and events from a pasted tag list and PLC metadata; mark source against derived events; draft the canvas, archetype guess and data requirements statement.
- Flag "missing identifier source" and empty canvas boxes as `<...>`.
- **Human gate:** the key user confirms the identifier source and the event definition; the OD lead or DBVE decides whether a unique case gets an impact analysis.
- The agent never promises an analysis on a derived event whose method is unnamed.
- **Evidence to cite:** the tag or signal name, the canvas box, the source statement in the request. Unverified items stay `<to confirm>`.
- **Hands over:** the filled canvas and requirements statement, with open questions listed for the plant.

## Still open

- `<Whether this becomes its own step id or stays a method inside 22>`: owner of `process.yaml`.
- `<Who owns the method catalogue per category>` once archetypes exist: OD lead.
- The decks assess an object-centric event log as an affordable option; no deck states a platform decision for it. `<to confirm>` with the data-platform owner before recommending it as a standard.
- Whether the share of use cases that need production metadata is still small: `<to confirm>`, re-count from the use-case list; do not quote an old share.

## Do not

- Do not treat a sensor value as an event, because a continuous reading has no "happened" moment to count or join.
- Do not promise a trace or a per-order analysis without the object relation, because nothing ties the series to the product.
- Do not approximate a missing order or serial relation from timestamps and call it traced: overlaps and rework make it wrong.
- Do not start a unique case without the impact analysis; do not rebuild a cross-process case per plant.
- Do not choose a data model before the object and event questions are answered.
- Do not hide ETL effort; do not model every signal, only those the question needs.
- Do not change a signal standard to fit one machine (`mi-signals` decides).

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/object-event-reduction.md`](references/object-event-reduction.md) | Procedure steps 2 and 3: the reduction method, "a sensor value is not an event", event-log vocabulary, the object-relation check, questions to ask |
| [`references/archetype-method-etl.md`](references/archetype-method-etl.md) | Steps 6 to 8: cross-process / per-process / unique, category to method to ETL, data classes and hubs, data-model choice, platform requirements |
| [`references/worked-examples.md`](references/worked-examples.md) | You want more illustrative reductions (serials, errors by station, cycle time, downtime) to imitate |
| [`assets/event-definition-canvas.md`](assets/event-definition-canvas.md) | Filling the canvas, one per use case |
| [`assets/data-requirements-statement.md`](assets/data-requirements-statement.md) | Step 9: what the data platform and the integration lane must provide |
| [`references/background.md`](references/background.md) | You need context, rationale and sources; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
