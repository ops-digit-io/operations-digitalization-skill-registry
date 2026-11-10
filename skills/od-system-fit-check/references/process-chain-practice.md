---
type: Skill Reference
title: Process chain practice
description: How the fit check is run as a step in the AI-driven process chain (i1 classify the demand, 32 tool decision) - tool boundaries and "recommended if" triggers as classifiers, demand shapes, the operations-concept check, handoffs and agent notes.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [practice, system-fit, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - the fit check as an intake classifier

Derived from the Operations Digitalization slide decks (tool and architecture decks, strategy decks, workshop decks), abstracted
into process guidance. No figures. `PROPOSAL` marks synthesis that no deck states; `<to confirm>` marks a reading the decks
leave open. The boundary sentences themselves stay in [`tool-boundaries.md`](tool-boundaries.md); this file is how to *use* them
as a classifier and how the step hands on.

## Where it sits in the chain

- **i1 Classify the demand**: called by `od-use-case-intake-triage` right after the need is stated.
- **32 Tool decision and IT gate**: called again when the requirement is broken down; the verdict routes to 3a or 3b.
- Same check both times; it must never run after a use case is scoped around a heavier system.

## 1 Method in practice

1. **Reduce the plant's sentence to objects, events and time.** Requests in plant words ("which carrier is in the oven",
   "serials produced today with quality status") look unique and mostly collapse into a few shapes: the object (part, order,
   tool, recipe, batch, carrier), the events that happen to it (error, change, stop, NOK part) and the time axis. Ask for the
   object and the event before judging uniqueness or system need. A request keyed on an identifier that lives in no signal and
   no system is a data gap, not an app.
2. **Map the asked functions onto the shop-floor function list** (data acquisition, scheduling, equipment, materials,
   information, performance analysis, energy) before naming any system. Order or recipe execution, labels, batch genealogy
   and material validation are MES territory even when the requester says "dashboard".
3. **Test the boundary sentence, then the trigger.** Every tool card has an "is / is not" line (the fit test) and an
   "integration recommended if" line (the intake trigger). Use both: the first says what the tool refuses, the second says
   when it earns a rollout. Record the tool's **cost class** (free, per-camera or per-system connector, per-plant development
   and deployment), never a number; a "recommended if" tool without a cost line invites scope creep.
4. **Check this plant**, dated (see [`deployment-reality.md`](deployment-reality.md)). A tool recommendation must name the
   defined use case behind it; a recommendation without a use case is not made.
5. **Sort the demand into its shape** before the lane is chosen:
   - use case on an already connected machine: sprint or workshop path (lane 2);
   - machine not yet connected: an equipment-integration wave first, use cases afterwards (use cases exist only for connected
     machines);
   - tool or system not in the toolbox: requirements, tool decision, IT and Cyber Security gate (lane 3);
   - quality or lab dashboard that does not depend on machine connectivity: its own path, owned by the local quality team, not
     in the machine-integration sequence.
6. **Say what is not ours.** Triage needs an explicit "not ours" list (the strategy excluded smart-automation and
   smart-equipment measures); a request on it is declined with the reason, not scoped.

## 2 Decision rules and triage

Boundary lines usable as classifiers (restated in the decks; full cards in `tool-boundaries.md`):

| Tool | Is | Is not | Recommended if |
|---|---|---|---|
| Quality feedback app | Collects part, box or batch quality feedback | A KPI calculator; a master-data store beyond quality specs | Digitalization journey started, some machines connected, parts carry a machine-readable serial |
| Rule engine | Transforms and standardizes streams; central soft logic across machines | A substitute for the service bus, for dashboards or for application connectivity | Machines are integrated but deliver no standardized format to other systems |
| Image library | Stores and serves images and inspection results | For process parameters or 2D measurement values; does not run model training | A customer asks to store pictures, or a new process includes vision |
| Edge platform | Edge acquisition, connectors, offload | A substitute for process-data acquisition or MES | See the edge rule below |
| Service bus | Default hub for transactional and streaming data | Calculates or interprets signals | `<not stated in the decks>` |

- **Edge device or plain OPC-UA client/server?** Edge is needed for a vision system or robot, when the customer expects full
  traceability (data loss means rejecting parts), for high-resolution time series from process-critical sensors, for inline
  measurement sensors, or when advanced analytics (anomaly detection, predictive quality or maintenance) is planned. Not
  needed if the machine has no high-frequency signals and OPC-UA can carry the series.
- **PLC or rule engine?** A value that controls the process or depends on equipment condition or safety (process values, set
  values, machine mode, safety doors) stays in the PLC. A value that needs context from several machines or systems, a
  single-source-of-truth concept (work-centre or location naming), or logic likely to be iterated (SPC rule alerts,
  statistics) goes to the rule engine.
- **Cheapest-test rule.** Plot the candidate on value against barrier or risk: build low-risk high-value; run a proof of
  concept where value and risk are both high; do not test or build low value. Dashboards from existing data sit in the
  low-risk corner; new-system pilots need prototypes.
- **Just do / go forward / lead change** (portfolio bucket, not size): *just do* = generic dashboard, notification or energy-saving
  case on integrated equipment with no new development; *go forward* = continue or integrate an earlier proof of concept that
  depends on a shared enabler; *lead change* = exploratory (simulation, digital shadow, generative or agentic) with an
  infrastructure and process focus. Assigning *lead change* is a human call.
- **Standard or special.** Standard when a validated prototype exists and only a configurable container or app is missing.
  Special when the data source is proprietary or external, or the process method is still undefined. Local solutions that
  already satisfy the need are input to standardisation, not new demand.
- **AI-above-reporting sanity check.** In a plant that has not reached reporting on a data-model basis, do not rank an AI use
  case above basic data-model and reporting work (data-value maturity ladder).
- **Kill with a reason.** Intake may end in "cancelled" with a recorded reason (no data foundation, insufficient savings,
  another party already collects the data) so it is not re-raised.

### The recurring blocker: a tool without an operations concept

A demand that is really a **service gap** (a tool exists or is requested, nobody runs it) must not be triaged as a use case.
Before a verdict of "fits", the tool needs:

- a business owner and an IT owner (roles),
- a service concept and support level (who answers an incident, out-of-hours or not),
- roles and responsibilities, a change-management process, and a risk process.

No rollout without a named operations owner (run owner) and support level. A tool rollout on request does not start without an
operations concept and a named run owner; stop until both exist. In this skill that is a precondition of the "fits" verdict, and a missing concept
turns the verdict into "escalate" via `od-decision-routing`'s tool or system rollout row.

## 3 Handoff contract

| Receive | From | Must contain |
|---|---|---|
| Stated need, canvas draft | `od-use-case-intake-triage` / `od-requirements-breakdown` | Need in plain terms; object, event, time; is the machine connected; is the service bus present; personal data or worker-performance measurement yes or no |
| Hand on: verdict | `od-use-case-intake-triage` (lane), `od-decision-routing` (exception), `od-system-fit-check` (design) | Verdict; the boundary sentence crossed (quoted); the tool and the plant checked with date; cost class; operations-concept status; the use case behind any tool recommendation |

If the verdict is *redesign onto a lighter tool*, the redesigned need goes back to requirements breakdown, not forward.

## 4 Pitfalls and lessons

- Requesters bring fonts, colours and headlines of dashboards; route by cost-saving impact and time-box, do not run them as
  fit questions.
- An idea-driven (not effect-driven) request, or a change request launched without pre-alignment with OD, is the usual root of
  one-off, non-scalable builds. Spot it early: no named effect, no named plant owner.
- Plants keep local digital solutions that fit the method but are not standard. Do not treat them as new demand.
- A tool recommended widely but with no operations concept is the most repeated barrier in the tool landscape reviews.
- Tool status is time-stamped; strategy decks have prioritised one platform, then stopped it, then migrated others. Look the
  status up live and date it.

## 5 Questions to ask and definition of done

- What is the manufacturing task and which strategic goal does it serve? Which object and event? What decision follows from the
  number, and who is the named plant owner?
- Is the machine connected and delivering the standard signals? Is the plant staffed with a key user?
- Does it involve personal data or measure worker performance? Is the service bus present? Is network capacity enough?
- Does the plant already run a local solution that fits the method?

Done = tool boundary tested with the sentence quoted, plant availability checked and dated, operations concept status stated,
lane chosen, cost class noted, verdict named with the next step.

## 6 Contradictions left open

- Performance analysis (OEE) is assigned both to the edge or analytics side and to the MES side ("may overlap with MES
  functionalities"). Choose the lighter solution and name the overlap explicitly; do not build in parallel what the execution
  system (MES) already does.
- Energy monitoring: cloud tool with data logger against edge platform plus service bus; no deck says which is preferred for a
  new plant. `<to confirm>` with the OD lead.
- Recommendation wording differs for the same tool in the sources ("not necessary", "not recommended as of now", stop or
  continue). State the tool recommendation on one scale: recommended / recommended if <condition> / not recommended / not
  available. Each status carries its date and source; quote the source wording next to it.

## 7 AI agent operating notes

- **Can do**: restate the need, extract object, event and time from free text, match against the boundary and trigger lines,
  pre-fill the canvas and list empty boxes as questions, look up plant availability, draft the verdict record.
- **Inputs required**: the request text, the plant, the tool overview and boundary cards, the operations-concept status of the
  tool.
- **Evidence to cite**: the boundary sentence crossed, the tool-status source and its read date, the use-case list row.
- **Human gate**: the verdict stays with the DBVE or IIAE; an exception goes through `od-decision-routing`. Whether a unique
  case earns an impact analysis, and any *lead change* label, is a human call.
- **Handover**: verdict record to the calling skill; open questions as a list with owner roles.
