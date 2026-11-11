---
type: Skill Reference
title: Process chain practice
description: How the data check is run inside the new process chain - objects, events and time first, the missing-signal table up front, decision rules, the handoff contract to and from neighbouring skills, pitfalls, and what an AI agent may do at this step. Process guidance only; no figures.
resource: ../SKILL.md
status: draft
tags: [data-availability, process-chain, ai-agent]
---
# Process-chain practice

Derived from the Operations Digitalization slide decks, abstracted into process guidance. Examples are illustrative and use
`<placeholders>`. Where this file adds a rule of its own it is marked `PROPOSAL`; unknowns are `<...>`.

## Where it sits

Step **22** (features and data check) of the use-case funnel, in front of `od-prototype-poc` (step 23). Two other places use it:
**i1** (a quick "can this start on existing data?" before the lane is chosen) and **31** (requirements for a new connector).
It is the second half of the creation chain a plant is taught: machine integration, **data availability**, data
standardization, data integration, dashboard creation, use-case utilization.

## Handoff contract

| Receives | From | Must be there |
|---|---|---|
| Defined use case with canvas | `od-use-case-definition` | Data and Dependencies boxes filled (an empty box means the case is not ready for this check), the moment of use, a named plant owner |
| Tags of interest, requirements as stories with acceptance criteria | `od-requirements-breakdown` | One vocabulary, atomic testable requirements, assumptions parked as listed open issues |
| Machine list entry, PLC program status | `od-equipment-integration` | Machine, controller, connection status (a blank is "not recorded") |
| Hands on | To | What it carries |
|---|---|---|
| Verdict (which step the request dies at) plus the **missing-signal table** | `od-prototype-poc`, `od-analytics-asset-build` | Nothing is built on a step that failed |
| Named data gap | Information Integration lane (`od-equipment-integration`, `od-equipment-integration`) | Machines, signals, plant, the use case waiting; recorded as a dependency on the use case |
| Standardization request | `od-signal-standardization` | Signals present but not comparable |
| Barrier | `od-equipment-integration` | A machine that will not connect |
| "Not a machine request" | The owner of the other source (quality, laboratory, legacy application) | See `non-machine-data-sources.md` |

Nobody downstream should have to re-ask "is the machine connected", "which signal", "which object is it keyed on".

## Method in practice

1. **Translate the plant's sentence before checking anything.** Requests arrive as plain sentences ("which carrier is in the
   oven now", "a table of all serials produced today with quality status"). Reduce each to three things: the **objects** it
   is about (part, order, tool, machine, recipe, carrier), the **events** that happen to them (NOK part, error, setup, tool
   break) and the **time** axis. Many "unique" requests collapse into a few shapes once this is done.
2. **A sensor value is not an event.** Time-series tags are mostly analogue or discrete values. Events come from
   boolean or discrete tags (machine error, tolerance deviation) or are derived from raw series by event processing; objects
   often hide as strings inside the series. Derive events deliberately, with a named method, before promising an analysis.
3. **Check the object relation first.** Time-series data relates to product and production metadata (serial, part number,
   order). If the use case needs that relation, machine time-series plus the standard base data model alone cannot serve
   it, and the relation is unclear where no standardized ERP or MES exists. Route a missing relation as a data gap; do not
   approximate it.
4. **Shortcut before waiting for a foreign system:** look at what object data the PLC already carries (order, part number,
   tool, recipe, batch, serial, raw-material batch) and what the signal metadata (asset structure) says.
5. **Match the sharpness to the question.** Ask whether sampling resolution and product characteristics are fine enough for
   what is asked. A transactional cycle record shows only the visible part of a cycle, so the cycle looks too short and the
   cause stays hidden; a time-series view with an overridden start and stop gives the realistic cycle.
6. **Split each process step into machine / checklist / system.** For every needed data point say whether it comes from the
   machine, from a manual checklist, or from a system. Where the PLC cannot see an event (waiting for material, low speed),
   plan **hybrid capture**: automatic where the PLC gives it, a standardized manual input (reason list, admin-owned rule set)
   where it cannot.
7. **Check the production structure.** If planning runs per cell rather than per machine, a machine-centred model does not fit;
   the data model has to carry cell, part number, shift and piece count. One terminal for several machines changes how an
   event is closed.
8. **Plan the transformation effort.** Data transformation (ETL) is a large share of every use case; without a general
   concept a notable part of use cases cannot be executed. Name the effort here, not after the promise.

## The missing-signal table, up front

Report anything needed but not yet collecting **before** any build starts, as one table:

| signal id | label | why needed | `PROPOSAL` class | owner role | next step |
|---|---|---|---|---|---|
| `<uuid>` | `<label>` | `<requirement / panel>` | PLC does not expose it / exposed but not configured / configured but not collecting | `<role>` | `<route>` |

The failure pattern this prevents: a signal is found not to be collecting only during the test, and the work goes back to
the start. The table goes with the verdict; it hands over to the Information Integration lane as the named request
(`assets/data-gap-request.md`) and is not approximated with a proxy.

## Decision rules

- **Equipment connected? yes / no** is the decision point in front of the use-case workshop. Connected: the case can start
  on existing data. Not connected: a different path, integration first (`od-equipment-integration`); use cases are only
  available for connected machines. A requirement beyond the time frame of a sprint becomes an additional phase, not scope creep.
- **Which source answers it.** Machine time-series plus base model alone, or production metadata needed. Many "unique"
  cases only need the first.
- **A base data model is not universal.** It applies to discrete manufacturing (greenfield, time-series-centric machines);
  brownfield with many controllers and continuous processes may need another model. Check the fit before giving a
  standard-model answer for a continuous process.
- **Quality data from laboratory tests** runs on a different path (driven by quality, owned by the local quality team). Do not
  put it into the machine-integration sequence.
- **Licence and hardware constraints** of laboratory devices (software bound to one test system by a dongle) are checked
  here, not at build time.
- **Layout stability.** Check whether the area is still being re-arranged before committing an integration wave to it.

## Pitfalls and lessons

- Cryptic labels, mixed languages, scaling and units held as tribal knowledge, no plausibility checks: "garbage in, garbage out".
- Planning-time files missing: machine list with location and layout, PLC programs, controller update status. The speed of any
  response is bounded by machine-list completeness (see `machine-list-completeness.md`).
- Blockers seen in real cases: product traceability behind a black-box serial-number process; test results not exposed;
  interlocking missing; entry-level controllers with no interface; the smallest high-end controller at its capacity limit,
  so tag export is slow and connectivity limited; new machines still shipped without an integration standard.
- IT architecture changes during a sprint (firewall separation, unclear access for local users) cost weeks. Agree
  architecture and user access before the check is called done.
- Low trust in existing integrations makes new use cases on them expensive; stabilize first.
- More integrated machines do not create savings on their own; ask who in production will pull the data.

## Questions to ask

- Which object (serial, order, carrier, tool) does the answer need to be keyed on, and where does that identifier live today
  (PLC signal, MES/ERP, manual entry)?
- Is the requester asking for a live view, a report on a cadence, or a record to be entered?
- What decision follows from the number, and who is the named plant owner?
- Is the machine connected, are the needed signals selected and **collecting**, and is the process understood well enough?
- Is a similar past dashboard or reference solution available (step 6 of the skill)?
- How is the production planned here: per machine, per cell, per order?

## Definition of done

The verdict names the step the request dies at; the object relation is stated (present, derivable, or a gap); events are
classed as read, derivable or not available; the missing-signal table is attached or stated empty; the data gap is routed
with an owner role; the requester has been told what can be answered with what exists, labelled as partial.

## AI agent operating notes

- **Can do:** classify intake text into object / event / time; read a tag list and PLC metadata; propose which object
  identifiers exist, which events can be derived from boolean or discrete tags and which cannot; draft the verdict and the
  missing-signal table; run `scripts/check_availability.py`; flag an empty Data or Dependencies box on the canvas.
- **Required inputs:** the canvas, the tag list (id and label), the machine-list entry, requirements as stories.
- **Evidence it must cite:** the machine-list row and read date, the label and path matched, the connector row, the rule used
  to call a tag an event. Step 5 is always "unproven" from the bundle; it never reports it as fit.
- **Human gate:** the plant key user confirms the identifier source and the production structure; the integration lead
  confirms the gap before it is routed. The agent does not decide a request is "unique" or "not worth an impact analysis".
- **Hands over:** verdict and missing-signal table to `od-prototype-poc` / `od-analytics-asset-build`; the named gap to the
  Information Integration lane. It never builds on a failed step and never substitutes a proxy without saying so.
