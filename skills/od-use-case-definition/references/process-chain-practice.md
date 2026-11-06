---
type: Skill Reference
title: Process chain practice
description: How step 21 (define and diagnose) is run in the AI-driven chain - canvas questions, data-source split, diagnosis patterns, utilization moment, can/cannot statement, definition of done, handoff record and agent operating notes.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, technical, process-chain]
derived_from:
  - Operations Digitalization slide decks (definition workshops, canvases, sprint and initiative decks), abstracted into process guidance; no figures.
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - definition (step 21)

Adds to the four phases in `SKILL.md`; it does not repeat the questionnaire or the protocol. `PROPOSAL` marks
synthesis that no deck states.

## Where it sits

Lane 2, step **21 Define and diagnose** (with `od-use-case-support-service`, `od-workshop-facilitation`,
`od-first-aid-kit`). It receives the intake record from `od-use-case-intake-triage` and hands a defined use case
to step 22 (`od-requirements-breakdown`, `od-data-availability-check`, `od-use-case-solution-evaluation`).

## 1 · Method in practice

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

## 2 · Decision rules

- **Priority of a collected list:** savings first (value, ROI); generalization potential and effort are secondary criteria; dependency order is the tie-breaker. Savings stay an
  **open task** until a pre-evaluation with a named owner is done; never quote a sum without its shown basis,
  and label it "estimated" until confirmed; "calculated" only with a documented basis. Label every figure
  input / assumption / market / unknown; finance-proven values stay separate.
- **Tool recommendations need a use case.** Recommend a tool for a plant only against a named defined use case
  ("based on defined quality use case"); no named use case, no recommendation. Use one status vocabulary
  (done / ongoing / not available) crossed with one recommendation vocabulary; `<to confirm>` the controlled
  list, because plant summaries and the strategy table use different words for the same tool.
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

## 3 · Handoff contract

**Receives** (from `od-use-case-intake-triage`): shaped statement, object / event / time, class, lane, tool
boundary result, plant tier. From `od-workshop-facilitation`: the capture sheet row.

**Hands on** (to step 22) one demand row with: plant; process group; capability; moment of use; owner role;
savings-basis label; tool dependency; machine dependency; data points by source (machine / manual / system);
success criterion with the data-quality KPI; out-of-scope list; open questions as `<...>`. Step 22 must not
re-ask these. Tag-level requirements are **not** in the definition; they are step 22's work.

## 4 · Pitfalls and lessons

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

## 5 · Questions to ask / definition of done

Ask in addition to the questionnaire: which strategic goal does it support; does an external customer require
it; where else is the same process applied and what could impede scaling; does it involve personal data,
measure worker performance or involve external partners; will analytics models be audited externally; is the
service bus available at the plant and does network capacity suffice; what is the initial state without digital
support; what would make people use it.

Done (adds to `SKILL.md`): canvas at "current state + objective + success criterion"; category; priority basis
(generalization, then saving); tool-availability check; named owner for the savings pre-evaluation; data
points split by source; can / cannot statement; utilization moment named; out-of-scope listed.

## 6 · AI agent operating notes

- **Can do:** pre-fill the canvas from the plant request, the use-case list and the machine list; flag empty
  boxes (data, dependencies, success criteria) and turn them into the question list; propose the library match;
  list the remaining use cases on the use-case list that relate to the machines in scope; draft the data-source
  split; draft the one-pager and the can / cannot statement; check that a utilization moment is named.
- **Required inputs:** intake record, plant file, tool-availability table with read date, library.
- **Human gates:** the key user confirms current state and stakeholders; the Plant ME confirms priority; the
  owner of the savings pre-evaluation accepts basis and baseline.
- **Evidence to cite:** use-case-list row, library entry, tool-status source and date.
- **Hand over:** the demand row in section 3 to `od-requirements-breakdown`; unanswered fields travel as `<...>`.
