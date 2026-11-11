---
type: Skill Reference
title: Process chain practice
description: How step 21 (define and diagnose) and the use case support service lane around it are run end to end in the AI-driven chain - Part A the definition (canvas, data-source split, diagnosis, utilization moment, handoff to step 22), Part B the lane (flow blocks, use-case sprint, registration gate for savings, handoffs between blocks), with agent operating notes for each.
resource: ../SKILL.md
status: draft
tags: [use-case-support-service, technical, lane, process-chain]
---
# Process chain practice

`PROPOSAL` marks synthesis that no deck states. Part A adds to the four phases in `SKILL.md`; Part B adds to the lane flow.

## Part A · Definition (step 21)

Adds to the four phases in `SKILL.md` (§ Step 21); it does not repeat the questionnaire or the protocol. `PROPOSAL` marks
synthesis that no deck states.

### Where it sits

Lane 2, step **21 Define and diagnose** (with the lane flow in `SKILL.md`, `od-workshop-facilitation`,
`od-first-aid-kit`). It receives the intake record from `od-use-case-intake-triage` and hands a defined use case
to step 22 (`od-requirements-breakdown`, `od-data-availability-check`, `od-use-case-solution-evaluation`).

### 1 · Method in practice

- **Start from the shaped statement.** Do not open the canvas on a raw plant sentence. Use the intake record:
  SMART verdict, object / event / time, class. If it is missing, run the SMART test and object / event reduction
  first (`od-use-case-intake-triage`, `references/process-chain-practice.md`).
- **Collect on the shop floor where possible.** A walk with Production, Engineering and OPEX produces a better
  collection than a room session; dashboard structure often falls out of the walk (overview over all lines,
  shift-leader view per line, process-value history per line). Collect requirements **per organisational
  level** (head of production, shift leader, technician, plus ME, maintenance, OPEX); typical contacts know
  only the top-priority issues, the technical depth sits with setters, process engineers and specialists.
- **Canvas to "current state + objective + success criterion" at minimum.** Boxes worth keeping in spirit:
  challenge (task, steps, objective, strategic goal, customer requirement?); current state (who does what,
  where else the same process exists); solution idea; stakeholders; scalability; dependencies in both
  directions; success criteria (manufacturing KPI **and** data-quality KPI, how failure is measured);
  obstacles and risks; requirements and gaps split into data and infrastructure; change (who benefits, who is
  negatively affected, training); urgency and importance; cost and benefit including "incremental value:
  tangible benefit even if not all objectives are reached".
- **Per process step, split the data by source.** For each step list the data points needed and mark each
  "from machine", "from checklist / manual" or "from system". Also ask where the order or recipe identity
  enters the process, whether the value can be read from the machine, and whether first- and last-piece
  inspection is manual. This split is the input to `od-data-availability-check`.
- **Diagnose before you define.** Split organisational from technical causes first: a top-N error log often
  shows that a simple organisational fix (refill, operator training) beats a technical change. Reconcile with
  the paper process before accepting a dashboard idea: production records against dashboard downtime, explain
  differences (breaks, shift changes, tolerances not yet applied). Human-dependent automation caps what any
  dashboard can show; check for organisational loss before proposing technology.
- **Hybrid capture.** Record automatically what the PLC can give; add a standardised manual input (reason list,
  admin-owned rule set) for events it cannot see (waiting for material, low speed).
- **Pair with a method the plant already runs** (changeover method, waste types, digital Gemba, switch-off
  campaigns): one standard method + one digital standard use case + one standard process. The dashboard gives
  transparency, the method gives the follow-up action.
- **Write the can / cannot statement** for the plant. Example shape (illustrative): *can* explain equipment
  issues, help derive actions, notify immediately; *cannot* recommend solutions or fix them (that would be a
  separate AI use case).
- **Name the utilization moment in the definition** (who opens it, in which meeting, which action follows).
  "Deployed" is not "used"; a definition without this moment is not accepted.
- **One-pager for the library:** problem, situation, digital support, identified in (plants), machine
  integration used, development approach, link to the full entry, and "can it substitute an existing manual
  practice (for example a board)".

### 2 · Decision rules

- **Priority of a collected list:** savings first (value, ROI); generalization potential and effort are secondary criteria; dependency order is the tie-breaker. Savings stay an
  **open task** until a pre-evaluation with a named owner is done; never quote a sum without its shown basis,
  and label it "estimated" until confirmed; "calculated" only with a documented basis. Label every figure
  input / assumption / market / unknown; finance-proven values stay separate.
- **Tool recommendations need a use case.** Recommend a tool for a plant only against a named defined use case
  ("based on defined quality use case"); no named use case, no recommendation. Use one status vocabulary
  (done / ongoing / not available) crossed with one recommendation scale: recommended / recommended if ⟨condition⟩ /
  not recommended / not available. Plant summaries and the strategy table use different words for the same tool;
  translate them to this scale, and keep date and source with each status.
- **Machine not connected:** the use case is recorded as demand with an integration dependency; it is not
  defined down to dashboards. Use cases are available only for connected machines; a requirement beyond a
  sprint's frame becomes an additional phase, not scope creep.
- **Dashboards that do not depend on machine connectivity** (lab tests, manual quality data) run on a different
  path, owned by the local quality team; do not put them into the machine-integration sequence.
- **Out of scope is written down** ("avoid grey zones"): for example one data source driving several machines in
  parallel, or edge cases such as pauses, ramp-up and tool changes.
- **Stale entries:** a canvas with empty Data and Dependencies boxes, or "TBD" in description or scaling, is not
  ready for the data check. Re-evaluate low-saving entries; one that is cheap to scale (a container exists) may
  stay as a scaling item `PROPOSAL`.

### 3 · Handoff contract

**Receives** (from `od-use-case-intake-triage`): shaped statement, object / event / time, class, lane, tool
boundary result, plant tier. From `od-workshop-facilitation`: the capture sheet row.

**Hands on** (to step 22) one demand row with: plant; process group; capability; moment of use; owner role;
savings-basis label; tool dependency; machine dependency; data points by source (machine / manual / system);
success criterion with the data-quality KPI; out-of-scope list; open questions as `<...>`. Step 22 must not
re-ask these. Tag-level requirements are **not** in the definition; they are step 22's work.

### 4 · Pitfalls and lessons

- A collected use case is a need, not a specification; the weak point named in the decks is "no technical
  requirements", so a category must be set before development.
- Requirements "change weekly" and dashboards are not right at first delivery: schedule an explicit
  requirements-iteration loop after the first delivery instead of treating change as failure.
- Plants do not evaluate their own use cases (low confidence, "social proof" avoidance). A calculator provided
  proactively, with OD owning the first pass and iterating on pushback, works better than asking the plant to
  start; putting savings calculation into the workshop agenda stalls the meeting.
- A high delivered count hides unused potential. Do not close a definition without the utilization moment.
- Missing basic process understanding, or only one machine connected, blocks a process-specific dashboard; get a
  process expert in from the start.
- Scepticism at shop-floor level is a starting condition, not an objection to answer in the room; acceptance
  grows by visible small results and connecting more machines.

### 5 · Questions to ask / definition of done

Ask in addition to the questionnaire: which strategic goal does it support; does an external customer require
it; where else is the same process applied and what could impede scaling; does it involve personal data,
measure worker performance or involve external partners; will analytics models be audited externally; is the
service bus available at the plant and does network capacity suffice; what is the initial state without digital
support; what would make people use it.

Done (adds to `SKILL.md`): canvas at "current state + objective + success criterion"; category; priority basis
(generalization, then saving); tool-availability check; named owner for the savings pre-evaluation; data
points split by source; can / cannot statement; utilization moment named; out-of-scope listed.

### 6 · AI agent operating notes

- **Can do:** pre-fill the canvas from the plant request, the use-case list and the machine list; flag empty
  boxes (data, dependencies, success criteria) and turn them into the question list; propose the library match;
  list the remaining use cases on the use-case list that relate to the machines in scope; draft the data-source
  split; draft the one-pager and the can / cannot statement; check that a utilization moment is named.
- **Required inputs:** intake record, plant file, tool-availability table with read date, library.
- **Human gates:** the key user confirms current state and stakeholders; the Plant ME confirms priority; the
  owner of the savings pre-evaluation accepts basis and baseline.
- **Evidence to cite:** use-case-list row, library entry, tool-status source and date.
- **Hand over:** the demand row in section 3 to `od-requirements-breakdown`; unanswered fields travel as `<...>`.

## Part B · Support service lane

Adds to the seven-step lane flow in `SKILL.md` (§ Lane flow). `PROPOSAL` marks synthesis that no deck states.

### Where it sits

Lane 2 (steps 21 to 26) and the use-case half of Lane 1. This file explains how the lane's blocks hang together
and what each block must have before the next starts. Each step has its own skill; this lane routes to them (step 21 itself is Part A).

### 1 · Method in practice

**Flow blocks, each with a trigger and an in/out.** The updated flow stresses preconditions, data-model
integration and knowledge sharing. Map to the chain:

| Flow block | Chain step | Skill |
|---|---|---|
| Preconditions for process start | i1 | `od-use-case-intake-triage` |
| Use case workshop | 21 | `od-workshop-facilitation`, `od-use-case-definition` |
| Benefits analysis | 24 | `od-benefit-calculation` |
| Preconditions for development start | 22 | `od-requirements-breakdown`, `od-data-availability-check` |
| Data collection and exploration; data-model integration | 22 / 3b4 | `od-data-availability-check`, `od-signal-standardization` |
| Use case development | 23 | `od-prototype-poc`, `od-analytics-asset-build` |
| Preconditions for deployment; deployment | 26 | `od-acceptance-test`, `od-handover-and-adoption` |
| Documentation, knowledge sharing, lessons learned | 26 | `od-use-case-standardization`, `od-use-case-standardization` |
| Benefits and savings tracking against the plant savings project | spine | `od-portfolio-and-savings-analysis`, `od-scorecard-reporting` |

`<to confirm>`: the deck pages for this flow carry block titles only (the pictures were not extracted); the
mapping above is this registry's reading. Content must come from the skills, not from the slide titles.

**Each block ends in a precondition for the next.** Write the precondition as "what must exist before the next
block starts". `PROPOSAL`: the agent drafts a definition of done per block from the precondition pages.

**Workshop series as a fast lane.** For a family of ideas (for example predictive maintenance): a workshop series
with the central engineering interface and selected local heads collects ideas; each idea is described on a
canvas; a go / no-go rating follows; a potential analysis is produced and captures tool demand. Process-focused
analyses add scope per process, scaling factors, actual KPI deviations and rollout locations.

**Focus order for definition work:** unassessed plants first, unassessed savings first. The KPI of the definition
step is "identified use-case potential", not implemented savings.

**Use-case sprint (execution).**
- Length: a time-boxed sprint of a few weeks after the workshop; later practice re-plans per longer period as a
  continuous activity with the plant key user in the team. `<to confirm>`: decks show a shorter and a longer
  standard; take the current one from the OD lead.
- Rhythm: one weekly review, one or two technical meetings a week, a mid-sprint status, a sprint-end review with a
  Q&A / feedback link. Inputs: targets, savings baseline, plan, data access, input and transformation steps.
- Standard deliverable set: generic process-value dashboard for all machines; Andon board (status plus history);
  operations dashboard (output, cycle time, alerts per time group or shift); machine availability by mode; alert
  dashboard; one process-specific dashboard as blueprint; SPC for inline measurement; the transformation flows
  with documentation. Order the views "overview to in-depth": Andon for stakeholders, operations dashboard for
  technicians, process-value dashboard for process engineers.
- Review against: what was carried over from another plant, what is blocked, what is a rollout option.
- Sprint definition of done: dashboards live, flows and dashboards documented, scalability statement, open
  topics list, impact of IT issues stated.

**Utilization loop taught to plants:** connect high runners and trouble-makers first, run use cases, select
parameters, analyse (parts, utilization, downtime), find root cause with a known method, create and calculate a
cost-saving project, eliminate deviations. Adoption means the use case is **integrated into a standard
operating procedure with dashboards and escalation flows**, not "dashboard live".

### 2 · Decision rules

- **Standard versus special:** see `od-use-case-intake-triage` (`references/process-chain-practice.md`).
- **Three-way bucket per use case:** just do / go forward / lead change; just-do items are copied from the
  library and need no new development.
- **Registration gate:** savings count only against a registered plant savings project with a baseline and an
  owner. A use case without a registered project is invisible to the savings ledger. Register a project for
  what is already implemented rather than waiting.
- **Savings are not rollout count.** Rollout count and savings are separate metrics; the widest-scaled cases
  often show no tracked saving, and savings concentrate in cases that attack a real cost driver. A scaled
  use case with deployments but no savings is "to be evaluated" until investigated, not "no potential"; only a human (the OD lead
  with the plant owner) may decide "no potential"; an agent never writes it.
- **Staffing assumption** is written next to every savings projection (central staffing only versus central plus
  dedicated plant key users).
- **Scope growth:** a requirement beyond the sprint frame becomes an additional use-case phase.
- **Quality dashboards independent of machine connectivity** follow the quality path, not the integration path.
- **Service gap:** a tool with no operations concept (owner, SLA, support level) is not rolled out; mark the use
  case blocked and route it to strategy (already in the error paths).

### 3 · Handoff contract

| From | To | Must travel |
|---|---|---|
| Intake | Definition | Shaped statement, class, lane, plant tier |
| Definition | Requirements | Demand row (plant, process group, capability, moment of use, owner, savings-basis label, tool and machine dependency, data by source) |
| Requirements | Integration lane | Requirement with lane variant (see `od-requirements-breakdown`) and business case |
| Integration | Sprint / build | Machine connected, signals selected, architecture and user access agreed |
| Sprint | Handover | Deliverables, flow documentation, open topics, impact of IT issues, scalability statement |
| Handover | Utilization review | Utilization table row per use case (name, who uses it, related process, method, rate, impact, plant-management relevant) |

Agree architecture and user access **before** the sprint starts: firewall changes and unclear access cost weeks.
Notification channels and data historization are IT changes; request them early. Keep flows in version control and
check the redeployment impact before upgrading the flow runtime.

### 4 · Pitfalls and lessons

- Deployed is not used; many scaled cases ran with no reported saving. Add a utilization check to every handover.
- Sprint reviews that start without a savings baseline never report a saving.
- A rollout of a dashboard to another process is gated by machine integration and tag selection, not by the dashboard.
- Single-file flow structures are brittle and do not modularise; enforce documented, reusable flows.
- IT architecture changing mid-sprint and an expert missing for the process are the two recurring delays.
- Savings reported incompletely make a target look missed while delivery count is on target; separate unreported
  savings from non-utilized potential.
- Plants that realise savings show production proactively driving ideas, the ME asking for blueprints, formal
  requirements with OD, savings calculated with controlling. Plants that do not: "only responsible for the
  technical part", standards ignored. Use as a readiness check.

### 5 · Questions to ask / definition of done

Per block: which precondition is met, by whom, with which evidence. Done for the lane: as in `SKILL.md` (Lane flow), plus a
utilization table row per live use case and a registered savings project (or an explicit "none, because ...").

### 6 · AI agent operating notes

- **Can do:** keep a sprint board from the deliverable list (available / ongoing / blocked / rollout option);
  draft the sprint-end summary and propose which blueprint to carry over; list use cases without a registered
  savings project; maintain the utilization table fields from call notes and chase open homework; draft the
  per-block definition of done.
- **Required inputs:** use-case list, machine list, savings ledger, flow documentation and dashboard links, with
  read dates.
- **Human gates:** DBVE and Plant ME agree the business case and priority; the OD lead sets wave and sprint
  length; the plant key user confirms the standard procedure that uses the use case.
- **Evidence to cite:** list row, ledger row, flow documentation, dashboard link, read date.
- **Hand over:** per the table in section 3; state which skill is next and what is still `<...>`.
