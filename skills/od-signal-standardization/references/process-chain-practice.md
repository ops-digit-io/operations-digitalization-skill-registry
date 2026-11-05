---
type: Skill Reference
title: Process chain practice
description: How signal standardization is run inside the new process chain - data classes and routes, the data-model creation steps, AI-assisted signal selection with a missing-signal table, decision rules, handoff contract, pitfalls, and AI agent operating notes. Process guidance only; no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [signals, process-chain, ai-agent]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice

Derived from the Operations Digitalization slide decks, abstracted into process guidance. Examples are illustrative and use
`<placeholders>`. Own synthesis is marked `PROPOSAL`; unknowns are `<...>`.

## Where it sits

Step **3b4** (connector and pipeline to the data platform), after the machine list, machine CV and integration plan and before
the flow is built. It also serves **22** (signal selection for a use case) and **1a2** (a template only works on standardized
signals). The same skill covers the signals of a machine that is already connected but not comparable.

## Handoff contract

| Receives | From | Must be there |
|---|---|---|
| Verdict "dies at step 4, not standardized" and the missing-signal table | `od-data-availability-check` | Signals named, why needed, which use case is waiting |
| Machine list entry, machine CV (PLC program, version history, vendor), integration plan | `od-equipment-integration` | Program version confirmed or marked Medium confidence |
| Tags of interest and requirement stories | `od-requirements-breakdown` | One vocabulary |

| Hands on | To | What it carries |
|---|---|---|
| Signal analysis report, filled binding sheet | `od-node-red-flow-builder` (flow config contract) | Canonical names, units, collection method, derived outputs to register |
| Same report | `od-acceptance-test`, `od-cross-plant-compatibility` | A second plant can consume it without asking |
| Machine-specific barrier | `od-barrier-triage` | Class, owner |
| Proposed standard change | IIAE decision (consultation) | An agent proposes; it does not enact |

## Method in practice

1. **Decide the data class first; it decides the route.** Transactional data (events, cycle time, counters, set values,
   limits, alarms) is hard to propagate when it changes; default hub is the service bus with OPC-UA. Time-series (curves,
   process values) is easy to propagate; default hub is the MQTT stream. Master data has one leading system (ERP);
   non-leading systems receive it via API, and per-system master data such as recipes or meter structures must be reconciled.
   The route then follows: native OPC-UA machine, aggregation server, or edge device.
2. **Per machine, decide the tag list by purpose:** transactional signals, streaming signals, what connected systems need,
   and what is wanted for analytics or data-quality loops. A machine integration is planned in this order: machine list,
   machine CV, integration guide per core process, integration plan, tag list, hardware, software, flow design to the
   standard base model.
3. **One interface for consumers.** Layers: PLC and connectivity, then data preparation (semantic mapping and
   contextualisation), then storage and applications. Third-party models are mapped into the standardized model; applications
   are not tailored to device interfaces.
4. **Standard information model.** Same structure on all comparable machines, predictable node identifiers where only
   equipment number and workplace change, a mapping layer that normalizes vendor naming. Layering: public companion
   specifications (types), then company extensions for generalized use cases, then the plant instance model. Rule:
   instances are created only from pre-defined types. The base model holds no process values.
5. **Process-specific data model, five steps:** investigate the public companion specifications for the process; prepare an
   extension of the in-house types model with a modelling editor; combine with the public standard and build an example
   instance for one machine; review and iterate with process engineering until release; instantiate per machine and roll out.
   Goal: the same views for all machines of one core process, so one dashboard works everywhere. Start by process priority.
6. **Machine-state standardization** pairs an agreed state machine with template flows and an integration guide. A raw
   signal is turned into the KPI contract by soft logic: a pulse heartbeat becomes a continuous availability state tied to
   automatic mode; a virtual batch opens when automatic mode starts and closes when it stops, with good and bad counters per
   batch. The pattern generalizes: state-machine transformation from raw machine signals to the KPI contract.
7. **Route manual data points** that no machine signal gives (for example an hourly target) through a soft HMI into the
   service bus; this is an accepted integration route.

## AI-assisted signal selection (and the missing-signal table)

Without AI the work is a manual scan of the tag list, an interview of the domain expert at the HMI screen, several rounds of
proposal and correction, hand-mapped identifiers, and a discovery during test that datapoints are not collecting.
With AI the inputs are fixed:

- datapoint export (id and label only), requirements text, optionally an HMI screenshot and an equipment reference;
- the equipment context carried in the skill or a reference (known signal paths, scaling conventions, thresholds).

The agent matches by label suffix scoped to the device, drops archived points, and groups matches into query patterns
(trend, latest, event-anchored, scaled). The expert reviews the proposal **on a running dashboard, not a spreadsheet**, in one
focused session. Anything needed but not collecting is reported up front as `signal id | label | why needed`
(`od-data-availability-check` owns the table; this skill resolves it). Units and scaling are written into the panel
description. Time-series data is not needed to generate a proposal, but is needed to accept one.

## Decision rules

- **Public model first** (step 3 of the skill). Require a companion specification in the purchase requirement where possible.
- **PLC or rule engine?** Keep in the PLC what controls the process or depends on equipment condition or safety (process
  values, set values, machine mode, safety doors). Put in the rule engine what needs context from several machines or systems,
  is a single-source-of-truth concept (work-centre or location naming), or is complex logic likely to be iterated (SPC rule
  alerts, statistical functions).
- **Standard or special.** Cross-process standard (independent of the core process but with constraints and integration work
  because data models differ), per-process standard (depends on process values of one core process, fewest constraints, scales
  fastest), or non-standard unique (factory conditions, legacy system, not scalable beyond the site).
- **Fit of the base model.** Greenfield, discrete, time-series-centric machines fit; brownfield with many controllers and
  continuous processes need other models. Say which applies `<to confirm: roadmap material calls the base model standard for all connected machines>`.
- **Scale known machine types.** At most one unknown machine type per new deployment; document the process per controller type and
  write an integration standard `<to confirm: other material says connect the difficult machines first; the decks report the
  difficult-first approach burned reputation, so the scale-known reading is used>`.
- **Never bury a per-plant fix-up** in a function or a query (see Do not in the skill); a mapping layer is the place for it.
- **Master-data leader.** One architecture names the ERP as leading system, another shows recipe and meter-structure master
  data in local specialist systems; the rule "single source of truth, others receive via API" is stated, the reconciliation
  of existing local masters is not `<to confirm>`.

## Pitfalls and lessons

- No naming convention across plants, cryptic labels, mixed languages, scaling and units as tribal knowledge, no plausibility
  checks.
- Typical standardization tasks that go wrong in flows: values stored as the wrong type, padded identifier fields, unit
  conversions, synchronization of mapping files.
- Standards scale only with a gate: a mandatory object structure, a naming convention for measure points and series, a white
  list of tested devices, and a shared knowledge site (energy metering is the worked example). The argument that carried it:
  easier purchasing, maintenance, support and transparency.
- Measure-point naming has to be thought through up front; master-data entry is laborious.
- Vendor software versions are inconsistent (an API exists in one version only); record the version with the signal.
- Missing planning-time information (program, version, update status of the controller) blocks later waves; collect it at
  the integration plan, not at the tag list.

## Questions to ask

- Which data class is this (transactional, time-series, master) and which hub carries it?
- Which public model or companion specification covers the process; is the machine already delivered with it?
- Where does the cycle start on this machine; which signals form the state machine; what makes a part good?
- Which signals does the use case need, which exist, which are collecting (the missing-signal table)?
- Is the program version in hand the deployed one?

## Definition of done

As in the skill, plus: data class and route stated for each signal group; the information-model instance created from a
pre-defined type; every derived output registered before the flow; the missing-signal table closed or handed on with an owner;
the report states the context situation (full context, tag export only, and so on).

## AI agent operating notes

- **Can do:** run `scripts/analyze_signals.py`; match tag labels to the vocabulary and to requirements by label suffix scoped to
  the device; classify signals (canonical, variant, local language, machine-specific, raw tag, derived); group matches
  into query patterns; draft the signal analysis report and the binding sheet; propose a standard change.
- **Required inputs:** datapoint export, requirements text, the machine context sources, program version.
- **Evidence it must cite:** the label and uuid matched, the vocabulary row or public-model clause used, the context source
  and its confidence per signal.
- **Human gate:** the domain expert validates the proposal on a running dashboard; the IIAE decides any standard or data-model
  change; a native speaker confirms translated tag names. The agent never translates a signal name and uses it directly.
- **Hands over:** the report and binding sheet to `od-node-red-flow-builder`; open gaps back to `od-data-availability-check`
  or `od-barrier-triage`.
