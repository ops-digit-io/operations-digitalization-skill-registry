---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for the first-aid step, abstracted from the Operations Digitalization slide decks - the SMART test with a good and a bad pair, object and event reduction, organizational versus technical split, diagnosis templates (loss tree, error top list, control loop), preconditions for an explainable-model claim. Guidance only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice, first-aid, ad-hoc]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - first aid and diagnosis

Deck-derived practice for intake (i1) and step 21. `PROPOSAL` = registry synthesis. Prices stay `<range from owner>`; the two data scenarios stay in `first-aid-offering.md`.

## 1. Method in practice

1. **Admit the request only if it passes the SMART test.** Specific purpose; clear objective; addresses a real problem; has a timeframe; names a stakeholder who needs it.
   - Passes (illustrative): "At `<station>` the `<daily meeting>` needs to see `<symptom>` for `<process>` by `<date>`, owner `<role>`."
   - Fails: "we want a dashboard for our `<new cell>`" (no problem, no objective, no owner).
   - Still fails: a precise date and a quantified target with **no baseline**; the target is invented. Capture the baseline first.
2. **Reduce the plant sentence to objects and events.** Plant words (which mandrel is in the oven, a serial list per day, trays traced through a cell, errors per station) look unique but reduce to a few objects (part, order, tool, recipe, batch) and events (error, change, stop) on a time axis. Ask for object and event before judging uniqueness.
3. **Ask the requester to bring a photo or the symptom in a sentence**; the assistant asks back for missing detail rather than guessing. First output is clustered into action categories (process or machine level, tool design, part design) as soft guidance without hard parameter values.
4. **Split organizational from technical at diagnosis.** A top-N error log per machine often shows that simple organizational fixes (refill the feeder, operator training) beat technical change. Check for organizational loss before proposing technology.
5. **Check data** (`od-data-availability-check`), scenario A or B (`first-aid-offering.md`), then route (`SKILL.md` table).

**Diagnosis patterns the decks use:**

- *Loss tree* for an equipment review: setup and changeover, technical, process, organizational (start-up and run-out), break. Failure frequency and repair time with targets, trend against previous periods, one measure per loss (structured problem solving, quick changeover, merging orders). An unclean KPI is flagged, not reported. Heavy daily manual data correction is itself the first use case (automatic detection of breaks, cleaning, shift ends, missing cycle times).
- *Machine error list:* boolean error signals need a mapping table from error number to message, built PLC-independent.
- *Problem classes at the first overview:* process, quality, production (waiting, unbalanced manual work), maintenance (downtime, wear), each with its KPI and available data sources.
- *Cycle time:* from transactional records it is under-reported because part of the cycle is invisible. Override start and stop in the rule engine, or infer the cycle from time-stamped boolean signals; alternatively acquire all variables, let analytics infer cycles and map a candidate list to the base model.
- *Typical output of an ad-hoc analysis:* cycle-time histogram per station; floating-bottleneck finding; cycles with and without station errors. Filters: drop cycles above a long-loss threshold (organizational loss), remove outliers with an interquartile-range rule, state the analysis window and the median with and without alerts; note when collective-fault tags cannot be mapped to a station.
- *Control-loop problem* (an unstable product dimension): transparency dashboard of controller inputs and outputs; list open questions on how control is implemented; write down the current understanding; list other influencers and signals needed; obtain the current program; plan tests at the next ramp-up; long term define closed-loop use cases.
- *Disappearing objects* (labels): track issued versus consumed versus scrapped by hour; the delta shows peak-loss hours. Training alone did not fix a systemic issue.
- *Ad-hoc sequence:* descriptive analytics per process step first; if no lever, train a predictive model and use explainability to find the few critical parameters; check model quality before trusting explanations; return the explanations to process engineering as candidate settings.

## 2. Decision rules

- **Standard, special, unique** (restated): cross-process, per-process, unique. A request that is unique ends in first aid or an impact analysis, not in the use-case funnel.
- **A statement of what it can and cannot do** goes in the request: can explain equipment issues, derive actions and notify immediately; cannot recommend solutions or solve them (candidate for an AI use case).
- **Advice versus parameter change.** An agent or assistant may give advice; a parameter change is a human and process-engineering decision.
- **Kill with a reason.** A request can end cancelled (no data foundation, insufficient benefit, someone else already collects the data); record why.
- **Comfortable-and-easy anti-pattern.** "OD will do it" for a request without purpose, objective and timeframe is a request for alignment first, not for delivery. The requirement must come from the plant.
- **Hybrid capture.** Record automatically what the controller gives, add a standardized manual input (reason list, administrator-owned rule set) for events the controller cannot see (waiting for material, low speed).
- **Infrastructure for an analysis app:** a cloud data lake when no real time is needed, many sources and long storage; the edge platform when real time, few shop-floor sources and modest compute are enough.
- **Quick-charter set** (for a data-science-type request): business problem; investment capacity; business benefit; deadline and why; requesting organisation and proposed sponsor; risk if not solved; obstacles; business functions needed; existing solution to modify versus new.

## 3. Handoff contract

| Receives | From |
|---|---|
| plant sentence, requester role, plant owner | intake (`od-use-case-intake-triage`) |
| machine and process, what is measured | plant ME |

| Hands on | To |
|---|---|
| the filled request form (SMART statement, object / event, data verdict, scenario, route with reason, requester told) | `od-first-aid-kit` (one-off), `od-use-case-intake-triage` / `od-use-case-definition` (recurring), Information Integration (data gap) |
| organizational-versus-technical finding | the plant owner |
| missing-signal table (`signal id | label | why needed`) | `od-requirements-breakdown`, Information Integration |

## 4. Pitfalls and lessons

- **Signal selection is hours of manual exploration per machine**, with individual rule sets, no plausibility check and no "why". Any proposal must address those four.
- **A sensor value is not an event.** Derive events deliberately; objects often hide as strings inside series.
- **Time series relates to production metadata** (serial, part, order). Use cases needing that relation cannot be served by signals alone; where no standard execution system exists the relation is the blocker. Check what object data is already carried in the controller (order, part, tool, recipe, batch, serial) before waiting for another system. Route a missing relation as a data gap; do not approximate.
- **Reconcile with the paper process** (breaks, shift changes, tolerance not yet applied) before trusting a dashboard.
- **Before any explainable-model claim:** state the data period, sample size per class, OK / NOK ratio, and which parameters were removed and why. Most effort is data preparation and plausibility checks; sparse recipe data may have to be removed; too few samples limit validity; analyses are retrospective when the process is continuously optimized.
- **Plants raise requests about fonts and colours;** route by cost-saving impact and time-box.
- **Idea-driven, not effect-driven** requests, and change requests launched without pre-alignment with OD, produce friction and one-offs.

## 5. Questions to ask and definition of done

What happened, where, since when? Which object and event? What is already measured, at what resolution? What was tried? What decision will the answer inform and who owns it at the plant? What is the baseline? What is the timeframe?

**Done (adds to `SKILL.md`):** statement passes the SMART test or the missing item is named; object / event written; organizational versus technical split noted; baseline present or marked `<to collect>`; route reason recorded.

## 6. AI agent operating notes

- **Can do:** score a pasted request against the SMART test; rewrite it as *challenge / current state / objective / measure / timeframe*; propose the object and event decomposition; classify intake text (photo plus sentence, ticket); run plausibility checks first (missing or sparse features, class balance, period) and report whether model quality is enough for explainability; draft the analysis plan; cite the failure catalogue for each suggested measure.
- **Needs:** the request text, tag list or signal export, machine and process, read dates.
- **Human gate:** the requester accepts the rewritten statement; the plant owner confirms facts; "needs expert review" is a mandatory human step before a conclusion leaves the lane; anything that commits cost or a connection.
- **Must cite:** signal ids, list rows, the catalogue or method used, the date range of data.
- **Hands over:** the form with every unknown as `<...>`; a missing-signal table up front.
