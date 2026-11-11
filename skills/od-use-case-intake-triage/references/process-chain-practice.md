---
type: Skill Reference
title: Process chain practice
description: How the intake step (i1) is run in the AI-driven chain - the SMART test and object/event reduction of a request, standard versus special, the three-way triage (just do, go forward, lead change), lane by demand shape, handoff record, pitfalls and agent operating notes.
resource: ../SKILL.md
status: draft
tags: [use-case-support-service, practice, process-chain]
---
# Process-chain practice - intake (step i1)

Adds to `SKILL.md`; it does not replace the channels, the owner table or the refusal list. `PROPOSAL` marks
synthesis that no deck states. Unknowns stay `<...>`.

## Where it sits

Step **i1 Classify the demand**. It receives a request from one of the four channels and hands a
classified, shaped request to Lane 1 (known use case), Lane 2 (`od-use-case-definition`, step 21) or
Lane 3 (`od-system-fit-check`, then step 31).

## 1 · Method in practice

Run the checks in this order; each one can end the triage.

1. **Is it OD's at all?** Owner table and refusal list in `SKILL.md`.
2. **Shape the statement (SMART test).** Admit a problem statement only if it has: a specific purpose, a clear
   objective, a real problem behind it, a timeframe, and a named stakeholder who needs it. A target with a date
   and a number but **no baseline** still fails: the target is invented. "Comfortable and easy, OD will do it"
   is not an admission; a request without purpose, objective and timeframe is a request for alignment first.
3. **Reduce to object, event, time.** Plant sentences look unique because they use plant words. Rewrite each as:
   the **object** it is about (part, order, tool, machine, recipe, batch, carrier), the **event** that happens
   to it (NOK part, error, setup, stop, tool break), and the **time** axis (live view, report on a cadence,
   record to be entered). Many "unique" requests collapse into a few shapes. Ask for the object and the event
   before judging uniqueness. Also ask where the object's identifier lives today (PLC signal, MES or ERP,
   manual entry); a missing identifier source is a finding, not a detail.
4. **Standard or special** (three classes), then act on the class:

   | Class | Meaning | Action |
   |---|---|---|
   | Standard, cross-process | Independent of the core process; has constraints (for example not for continuous processes); needs integration work because data models differ | Start with priority: high value, scalable |
   | Standard, per-process | Depends on the process values of one core process; fewest constraints; scales fastest | Start |
   | Non-standard, unique | Depends on factory conditions, a legacy system or a one-off problem; does not scale beyond the site | Do not start; run an impact analysis first. A custom case is allowed only if the expected value is very high; it may be prototyped, and counts as mature only after it is folded into the standard systems |

5. **Three-way triage by what to do** (not by size). Applies to the use-case list as well as to a single request.
   - **Just do**: generic dashboard, notification, reaction-time and energy-saving cases on equipment that is
     already integrated and has data. Copy from the use-case library; do not make it complicated.
   - **Go forward**: continue or integrate an earlier proof of concept; each depends on a shared enabler
     (for example quality-data aggregation or an event-driven data store). Name the enabler.
   - **Lead change**: exploratory (simulation first, digital shadow, generative or agentic approaches) with an
     infrastructure and process focus. Assigning this bucket is a human call.
   The bucket is **orthogonal** to the lane. Typical pairing: just do and go forward usually run in Lane 1 or
   Lane 2; lead change usually opens Lane 2 or an AI pilot. `PROPOSAL` for that pairing.
6. **Pick the lane by demand shape.** (a) A new use case on a machine that is already connected: Lane 2
   (workshop or sprint path). (b) A machine that is not connected: an equipment-integration wave first; use
   cases only afterwards, because use cases exist only for connected machines. (c) A tool or system that does
   not exist in the toolbox: requirements, then tool decision, then the IT and Cyber Security gate (Lane 3).
   (d) A catalogued use case on a connected machine: Lane 1.
7. **Test the tool boundary** whenever the ask sounds like a dashboard (below, section 2) and hand to
   `od-system-fit-check`.
8. **Record** the one-line triage output of `SKILL.md` plus the fields in section 3.

## 2 · Decision rules

- **Service gap is not a use case.** A tool that has no operations concept, owner or support role goes to the
  system and operations-concept discussion first; it is marked blocked, not triaged as a use case.
- **Local solution that already fits.** A plant often runs a local solution that satisfies the need but is not
  standard. Treat it as input to standardisation (`od-use-case-standardization`), not as a new demand.
- **Capacity tier, not eligibility.** First-mover versus fast-follower plant decides how much central support
  is available, never whether a request is legitimate. First mover: high estimated value-add, regions,
  segments and technologies covered, capacity and knowledge in the plant, integration synergies, and a
  dedicated staffed key user. Fast follower: central support only when capacity allows, locally driven, limited
  funding. Eligibility follows request order; central capacity goes first to first-mover plants that are
  staffed. Write the plant tier next to the queue position.
- **Ideas-driven is a warning.** A request driven by an idea rather than an expected effect or saving, or a
  change request launched without pre-alignment with OD, is the named cause of friction and one-offs. Ask for
  the effect.
- **Cosmetic requests** (fonts, colours, headlines of dashboards) burn capacity for little value: route by cost-saving
  impact and time-box them inside a use-case sprint.
- **Tool boundary ("is / is not").** Each shop-floor tool has a boundary sentence; use it as the fit test. A
  request for order or recipe execution, labels, batch genealogy or material validation is MES territory, not a
  dashboard; map the asked functions onto the shop-floor business functions (data acquisition, scheduling,
  equipment, materials, information, performance analysis, energy) before choosing a system. Record the tool's
  **cost class** (free, per-connector, per-plant development), not a number.
- **Cheapest-test rule.** Plot value against barrier or risk: build low-risk high-value; run a proof of
  concept where value and risk are both high; do not test or build low-value high-risk.
- **Kill is an outcome.** Intake may end in "cancelled" with a recorded reason (no data foundation,
  insufficient savings, another party already collects the data). Keep the reason; the demand owner gets it.
- **AI ideas.** Collection runs: requester enters the idea in a shared list, OD holds a short call with the
  standard questions, the idea is recorded and prioritised later into initiatives, and the expectation is set
  that not every idea is ready to be executed. Sanity check: do not rank an AI idea above basic data-model and
  reporting work in a plant that has not reached reporting. Quick grid: low barrier and high potential, mid
  barrier and high potential, high barrier and mid potential. An AI knowledge or troubleshooting assistant
  is decided case by case at intake: ask for a measurable before and after. With one, it takes the use-case route (savings
  only with a documented basis). Without one, it is tracked as an initiative with an owner and a usage measure, not as a
  counted saving.
- **Customer-mandated programmes** (a customer requires a digital process-control framework with staged
  compliance targets) have a different driver than savings. Do not force them through the savings test: they have their own intake
  branch with their own KPI (deadline and compliance driven). Required fields: customer requirement, deadline, scope, owner.

## 3 · Handoff contract

**Receives** from the channel: the requester's text, plant, requester role. Nothing else is required to start.

**Hands on** (to the lane's first skill) one record with: SMART verdict and the rewritten statement; object /
event / time; identifier source; class (cross-process, per-process, unique); bucket (just do, go forward, lead
change, or `<not set>`); lane and demand shape; machine connected yes/no/`<unknown>`; tool dependency with
boundary sentence and cost class; plant tier; local solution already running yes/no; gate expected (per
`od-decision-routing`); blocking facts. Downstream skills must not re-ask what is in this record.

- Lane 2 → `od-use-case-definition` (and `od-workshop-facilitation` when a workshop is the vehicle).
- Not connected → `od-equipment-integration` via the Information Integration lane.
- New tool → `od-system-fit-check`.
- Ad-hoc process issue → `od-first-aid-kit`.

## 4 · Pitfalls and lessons

- "Every request is unique": see object / event reduction; judge uniqueness after it, not before.
- Early belief that digitalization is an IT matter: the requirement must come from the plant. If the requester
  expects OD to know the shop-floor requirement, the first deliverable is the requester's own statement.
- A rewritten statement that the requester does not recognise is not accepted; the requester confirms it.
- Spotting early: a statement with a solution noun in it ("a dashboard for ..."), a target with no baseline,
  no named stakeholder, a request that names a technology instead of an effect.
- Agreement on a funding deadline (grant window) can drive a calendar; list it as a constraint, not as value.

## 5 · Questions to ask / definition of done

Questions: what is the manufacturing task and which goal does it serve; how is it done today and by whom;
where else does the same process exist; which object is the answer keyed on and where does its identifier live;
live view, cadence report or record to be entered; what decision follows from the number and who owns it; is the
machine connected and are the standard signals delivered; is the plant staffed with a key user; does a local
solution already exist; is a validated prototype available elsewhere; does it involve personal data or measure
worker performance.

Done when: the statement passes the SMART test or is returned with the failing test named; object / event /
time written; class and bucket set or explicitly `<not set>`; lane chosen with the demand shape stated; tool
boundary tested where relevant; cost class noted; the record above is complete.

## 6 · AI agent operating notes

- **Can do:** score a pasted request against the five SMART tests and quote the failing one; rewrite it in
  "challenge / current state / objective / measure / timeframe" form; propose object / event / time and flag a
  missing identifier source; propose class, bucket and lane and **state which fact it used** (connected? prototype
  elsewhere? library entry? boundary sentence?); match the ask to the tool-boundary table and return fit /
  redesign / escalate with the boundary sentence cited; draft the canvas from free text, leaving unknown boxes
  as `<...>` that become the question list.
- **Required inputs:** the request text, the plant's use-case list and machine list with read date, the
  tool-availability table, the library.
- **Human gates:** the requester accepts the rewritten statement; the OD lead assigns "lead change", accepts
  a non-standard unique case, and decides a refusal; priority is never inferred.
- **Evidence to cite:** use-case-list row, library entry, tool boundary sentence, machine-list row and date.
- **Hand over:** the record in section 3 to the lane's first skill; a refusal goes back to the demand owner with
  reason and route.
