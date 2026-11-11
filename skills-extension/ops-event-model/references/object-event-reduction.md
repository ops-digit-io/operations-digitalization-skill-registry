---
type: Skill Reference
title: Object event reduction
description: How to reduce a plant sentence to objects, events and time, why a sensor value is not an event, the event-log vocabulary, the object-relation check and the questions to ask.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---
# Object and event reduction

Source basis: Operations Digitalization decks on object-driven event mining and on transaction versus
time-series use cases, abstracted. Statements that go beyond them are marked `PROPOSAL`.

## The three questions

| Question | Typical answers | Where the answer lives |
|---|---|---|
| Which **object** is the answer keyed on? | part, serial, order, tool, machine, recipe, batch, carrier | PLC signal, MES or ERP, manual entry |
| Which **event** happens to it? | NOK part, machine error, setup, tool break, stop, tolerance deviation | boolean or discrete tag, system record, or derived from a raw series |
| Which **time** axis? | live view, report on a cadence, a record to be entered | the consumer's ritual (`ops-analytics-asset`) |

After this, many "unique" requests collapse to a small number of shapes. Ask for the object and the event
*before* judging uniqueness.

## A sensor value is not an event

- Time-series tags are mostly analogue or discrete values. They describe a state over time.
- An event is something that happens to an object at a point in time. It comes from boolean or discrete tags
  (machine error, tolerance deviation) or is **derived** from a raw series by event processing (threshold crossing,
  start/stop detection, an overridden cycle start).
- Objects often hide as strings inside the series (order number, part number, recipe name).
- Rule: derive events deliberately, with a mapped method, before promising an analysis.
- Hybrid capture: record automatically what the PLC can give; add a standardized manual input (admin-owned reason
  list and rule set) for events the PLC cannot see (waiting for material, low speed).
- Where error signals are booleans, an error-number-to-message mapping table belongs to the handoff.

## Signal classification (use in the canvas)

| Class | Test | Next step |
|---|---|---|
| Sensor value | Describes a state, no object attached | Keep as time-series; needs an event definition to answer "when" questions |
| Source event | Boolean or discrete tag, or a system record, already marks the occurrence | Name object link and timestamp source |
| Derived event | Occurrence must be computed from a raw series | Name the rule, the owner of the rule, and the ETL job |
| Object identifier | Serial, order, part, batch, recipe, tool, carrier | Name where it is carried, and whether it is stable per cycle |
| Master data | Single source of truth elsewhere (leading system) | Name the leading system and how the platform receives it |

## The object relation

Time-series data always relates to product or production metadata. Check first:

1. Can the use case be served by machine time-series plus the standard base data model alone?
2. If it needs order, part, batch or recipe, where is the identifier today? Check what the PLC signals and the
   signal metadata (asset structure) already carry before waiting for a foreign system.
3. Where no standardized MES or ERP exists, the relation to production metadata is the blocker. Name the missing
   relation and route it as a data gap; do not approximate.
4. A request for order or recipe execution, labels, batch genealogy or material validation is MES territory, not
   a dashboard (see `invest-screen`).
5. A transactional record shows only the visible part of a cycle, so cycle time looks too short and the cause is
   hidden. A time-series view with an overridden start/stop (an edge flow) gives the realistic cycle.

## Production structure and sharpness

- Where planning works per **cell** (for example a lean U-cell) and not per machine, a machine-centred model does
  not fit: carry cell, part number, shift and piece count.
- Sampling resolution and product characteristics must be fine enough for the question.
- Several machines per operator or tablet change how a downtime event is closed. Ask.

## Event-log vocabulary

Event, case, transition, variant, object. Variants versus standardization is a trade-off: many variants mean
low standardization. Process-mining progression in the decks: start with event data and process discovery (low
complexity, high impact); continue with object-centric event data (high complexity).

## Questions to ask

- Which object does the answer need to be keyed on, and where does that identifier live today?
- Which event ends or starts the thing the plant counts? Is it a tag, a system record or a manual entry?
- Live view, report on a cadence, or a record to be entered?
- What decision follows from the number, and who is the named plant owner?
- Is production planned per machine or per cell? Is there an MES or ERP at the plant?
- Is the sampling fine enough? Is the identifier stable for the whole cycle?
- Is this an idea or an expected effect? Ideas-driven requests are a named source of friction and one-offs.
