---
type: Skill Reference
title: Process chain practice
description: How requirements are broken down in steps 22 and 31 of the AI-driven chain - category to method to data job, object and event checks, signal list handoff, AI-assisted signal selection, refinement rules, legacy-application and OT application assessment, key-user collaboration and agent operating notes.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [requirements, practice, process-chain]
derived_from:
  - Operations Digitalization slide decks (analytics, event-data, legacy-assessment, workshop and AI-assistant decks), abstracted into process guidance; no figures.
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - requirements breakdown

Adds to the procedure in `SKILL.md`, `elicitation.md` and `legacy-system-assessment.md`; it does not repeat
the template or the epic rules. `PROPOSAL` marks synthesis that no deck states.

## Where it sits

Lane 2 step **22** (features and data check) and Lane 3 front-end step **31** (requirements). Receives the
defined use case from `od-use-case-definition` (the demand row) or, in Lane 3, the shaped request from
`od-use-case-intake-triage`; hands a requirement with its lane variant to the integration lane, to
`od-system-fit-check` (step 32) or into the backlog as an epic.

## 1 · Method in practice

1. **Category, then method, then data job.** A collected use case states a need, not technical requirements.
   Assign a category (examples: statistical process control, machine availability, downtime); each category has a
   dedicated set of methods; each method translates to a data-transformation job. Only then does the use case
   enter requirements, development and deployment as a subset of the standard process.
2. **Check the data shape first.** Can the use case be served by machine time-series plus the standard base data
   model alone, or does it need production metadata (order, part, batch, recipe, serial)? Time-series data always
   relates to production metadata; where no standardised ERP or MES exists, the missing relation is the blocker.
   Check first what object data the PLC signals already carry (order, part number, tool, recipe, batch, serial,
   raw-material batch) and what the signal metadata (asset structure) gives, before waiting for a foreign system.
   Route a missing relation as a **data gap**; do not approximate it.
3. **A sensor value is not an event.** Analogue and discrete values become events through boolean or discrete tags
   (error, tolerance deviation) or deliberate event processing. Derive events with a named method before
   promising an analysis. Where error signals are booleans, require an error-number to message mapping table in a
   PLC-independent transformation.
4. **Signals are standardised before the use case.** If the machine gives a pulse heartbeat and the endpoint
   wants a continuous availability state, specify the soft logic (heartbeat to continuous state tied to automatic
   mode; a virtual batch opens when automatic mode starts and closes when it stops). Generalises to a
   state-machine transformation from raw signals to the KPI contract.
5. **Cycle time from transactional data is under-reported** when part of the cycle is invisible. Specify
   start / stop override in the rule engine, or inference from time-stamped boolean signals. Alternative to
   selecting PLC variables upfront: acquire all variables, let analytics infer cycles, return a candidate list for
   mapping to the base model.
6. **Match data resolution to the question.** Ask whether sampling resolution and product characteristics are fine
   enough; ask where production is planned (per machine or per cell). A machine-centred app does not fit a
   cell-planned process; the model must then carry cell, part number, shift, piece count.
7. **Hybrid capture.** Specify what is read automatically and a standardised manual input (reason list, rule set
   owned by an admin) for events the PLC cannot see.
8. **Put each logic in its place.** Keep in the PLC what controls the process or depends on equipment safety or
   condition; put in the rule engine what needs context across machines or systems, single-source naming, or logic
   likely to be iterated. Tool boundaries ("is / is not") are recorded in `od-system-fit-check`; reference them,
   do not respecify.
9. **Plan the ETL effort explicitly.** Data transformation is a large share of every use case; without a general
   ETL concept a notable part of use cases cannot be executed.
10. **Signal selection, AI-assisted.** Without help: a manual scan of the tag list, an interview at the HMI,
    several correction sessions, discovery during test that points are not collecting. With help: input is the
    datapoint export (id and label only), the requirements text, an optional HMI screenshot and equipment
    reference; the proposal matches by label suffix scoped to the device, drops archived points and groups matches
    into query patterns. The expert reviews the proposal on a running dashboard, not a spreadsheet. Anything needed
    but not collecting is reported up front as `signal id | label | why needed`.
11. **Refine, then freeze.** Collect once globally (method description, plant requirements, survey of roles, pain
    points and must-haves, shop-floor reality of levels, shifts, areas, machines, site and language scope); then
    strip solution bias, make each requirement atomic and testable (epic and stories), resolve plant conflicts,
    use one vocabulary, and park assumptions as listed open issues rather than silently filling them.
12. **Pilot at the plant that first raised the need,** gather requirements from the followers, publish the
    requirement document link.

**Legacy and OT application assessment (step 31, non-standard case).**
- Component workshop output: use cases of the application (what must be preserved), component inventory with
  focus on interfaces, risk table per component (risk, trigger, likelihood), impact per component (production
  stop, traceability loss, data loss with workaround, convenience loss, with minimum recovery lead time), as-is
  to to-be component mapping, key roles and activities. Rate **per component, not per application**.
- Recurring risk classes: client software failure, OS and application updates and their interaction, complex
  interface management, loss of interface-development knowledge, missing documentation, limited PLC-vendor
  knowledge, missing cyber-security approval, licence management.
- Include a **"continue as-is" scenario** with its consequences as the baseline of the decision package
  (`PROPOSAL`: make it mandatory).
- Application inventory fields (local owner fills): name and used functions, location, responsible, interfaces
  (protocol, encoding), interfaced equipment, status, software supplier and supplier status, version, security
  and network status, production criticality, customer impact, support concept, licence, number of deployments.
  OD fills: application category, functional mapping to a standard application, scaling potential.
- Production-criticality rubric: **critical** (core production, immediate stop, safety or legal, no workaround,
  around the clock), **moderate** (efficiency or maintenance, workaround exists, regular use), **minimal**
  (convenience or reporting, occasional, easily replaced). Guiding questions: does it control or stop machines,
  could failure cause injury, environmental or legal issue, is it needed around the clock, would failure stop
  production, is it used for troubleshooting, is it involved in quality control, does it only report. The
  customer-impact rubric is analogous (order processing, labelling, delivery, traceability for audits and
  recalls, data shared with customers or regulators, contract effect). The rating is a human call.
- Migration order shown in decks: lowest-risk machine first to an industry-standard interface, then the edge
  platform reads PLC data, existing reporting replicated as the requirement baseline, MES prepared, remaining
  interfaces last. Also ask: any additional interface (for example laboratory), who actually uses the recorded
  data, does the current reporting need heavy manual correction (that correction effort is itself the first
  requirement). Capture requirement statements verbatim from the plant.

**Key-user collaboration.** The local key user is the entry point; weekly exchange with maintenance, production,
ESH and engineering. Stakeholders bring ideas, not tasks; iterate dashboards step by step with whiteboard
sketches. Operating model: local key user plus an integration engineer (cyber, infrastructure, governance) plus
IT product and service owners in an agile cadence (planning, requirements, issue management).

## 2 · Decision rules

- Category assigned and library checked before any requirement is written; an adoption is not a build.
- A use case that needs production metadata the plant cannot supply is a data gap (route to
  `od-data-availability-check`, then the information-integration lane), not a reduced scope.
- Plan the process-specific data model before analytics use cases for a process family; the base model holds
  no process values. Five steps: survey public companion standards, extend in a modelling editor, combine with the
  public standard and make one example instance, review with process engineering until release, instantiate per
  machine. Goal: the same views for all machines of one core process.
- Dashboard / data-product requirement sets are cheaper kept as a **one-time list plus a continuous requirements
  funnel** (collect always, evaluate and improve periodically; each entry has functional description, value add,
  success criteria for review).
- Operator-entry apps: before specifying, ask how one tablet maps to several machines, how an event closes with
  several operators, what happens when a machine is idle for a whole shift, which KPIs break if the planning
  module is not used.
- Fail it here when it cannot be tested or when no named plant role will use it in a real shift.

## 3 · Handoff contract

**Receives:** demand row (plant, process group, capability, moment of use, owner role, savings-basis label, tool
and machine dependency, data points by source, out-of-scope list).

**Hands on:** the requirement with its lane variant; tag list (labels) with a signal list carrying source
(machine / checklist / system) and an existence verdict; the missing-signal table (`signal id | label | why
needed`) to the information-integration lane; error-number mapping table; start / stop signals for cycle time;
requirements markdown; reference dashboard if any; equipment reference; open-issue list. Legacy case: component
tables, risk and impact tables, as-is to to-be mapping, "continue as-is" scenario, key roles.

## 4 · Pitfalls and lessons

- No naming convention across plants, cryptic labels, language, units and scaling as tribal knowledge, no
  plausibility check ("garbage in, garbage out").
- Prerequisites found late: product traceability blocked by a black-box serial-number process, test results not
  exposed, interlocking missing, machine list, layout, PLC programs and cyber-security update status missing at
  planning time.
- Individual rule sets per machine and no "why": any analyser must address manual signal exploration, per-machine
  rules, no plausibility check, no explanation.
- Entry-level controllers with no interface, and the smallest high-end controller at its capacity limit, slow tag
  export and limit connectivity; new machines may still ship without an integration standard.
- Hardware or licence dependencies for lab devices (for example dongle-bound software on one test system) belong
  in the data-availability step.

## 5 · Questions to ask / definition of done

Which object identifies the answer and where does it live; which events, and are they derivable; is the
production-metadata relation available; which signals, with source and existence verdict; where in the PLC and
where in the rule engine; planned per machine or per cell; who confirms the identifier source.
Done (adds to `SKILL.md`): category and method named; data shape stated (time-series only, or with metadata and
the source of the relation); missing signals listed as a table, not approximated; ETL effort named.

## 6 · AI agent operating notes

- **Can do:** match signals to requirements with a cited rule (label, path, rule used); list identifiers the tag
  list carries and events derivable from boolean or discrete tags, and those that are not; write the verdict with
  the missing relation named; turn workshop output into stories and acceptance criteria; list missing signals;
  inventory components from architecture exports; generate risk tables from the recurring risk classes; draft the
  as-is to to-be mapping; pre-fill application description, category and functional mapping from supplier pages.
- **Required inputs:** tag list or datapoint export, PLC metadata, requirements text, equipment reference,
  architecture export, interface documentation; with read dates.
- **Human gates:** the domain expert validates signals on a running dashboard; the key user confirms the
  identifier source; the local owner confirms criticality and customer-impact ratings; target architecture,
  scenario choice and budget stay human.
- **Evidence to cite:** label, signal path, rule used, component list source, interface documentation, support
  status.
- **Hand over:** per section 3, with unanswered fields as `<...>`; the missing-signal table goes to the
  information-integration lane.
