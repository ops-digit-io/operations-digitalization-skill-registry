---
type: Skill Reference
title: Process chain practice
description: How the fit check of an envisioned solution is run in step 22 of the AI-driven chain - fit tests the decks use besides the capability model (tool boundary, edge versus plain connection, PLC versus rule engine, cloud versus edge, make or buy), the operations-concept gate, handoff and agent operating notes.
resource: ../SKILL.md
status: draft
tags: [use-case-support-service, practice, process-chain]
---
# Process-chain practice - solution evaluation

Adds practical fit tests that the decks use next to the 27-driver and 16-area method in `SKILL.md`; it does not
change that method. `PROPOSAL` marks synthesis that no deck states.

## Where it sits

Lane 2 step **22** (features and data check), after `od-use-case-definition` and before the business case
(`od-benefit-calculation`, step 24). In Lane 3 the same tests feed `od-system-fit-check` at step 32. Receives the
defined use case and the demand row; hands the verdict and score to prioritization and the business case.

## 1 · Method in practice

Run the case-ranking pre-check and the four steps of `SKILL.md`, and add these quick tests at the point where
the solution is first named. Each one can turn "ready to build" into "needs a named capability raised first".

- **Tool boundary ("is / is not").** Every shop-floor tool has a boundary sentence. A quality-feedback app collects
  quality feedback and is not a KPI calculator or master-data store. The rule engine transforms and standardises
  streams and is not a substitute for the service bus or for dashboarding. The image library stores and serves
  images and inspection results and is not for process parameters or model training. A service bus does not
  calculate or interpret signals. An edge platform is not a substitute for machine or process data acquisition or
  an MES. Each tool also has an "integration recommended if" trigger and a cost class (free, per-connector,
  per-plant development); record the class, not a number.
- **MES territory.** Order or recipe execution, labels, batch genealogy and material validation are not dashboard
  work. Map the asked functions to the shop-floor business functions before choosing a system.
- **Edge device versus plain OPC-UA client / server.** An edge device is warranted for a vision system or robot,
  full traceability where data loss means rejecting parts, high-resolution time-series from process-critical
  sensors, inline measurement sensors, or planned advanced analytics (anomaly detection, predictive quality or
  maintenance). It is not needed where the machine has no high-frequency signals and OPC-UA can carry the time
  series.
- **PLC versus rule engine.** Control and safety-dependent logic stays in the PLC; cross-machine context,
  single-source naming and logic likely to be iterated goes to the rule engine.
- **Cloud data lake versus edge platform** for an analytics application: cloud when there is no real-time need,
  many sources, high compute or long storage; edge when real-time, few shop-floor sources and modest compute.
- **Stream versus batch transformation:** micro-batching for fresh data and roll-ups; scheduled batch for
  synchronising mapping files or building roll-ups. Choose by freshness need and external-system sync.
- **Design for scale from the start.** A validated prototype first, then a container- or template-based
  application. If only a prototype exists, the verdict names the development of the scalable application as the gap.
- **Make or buy rule chain.** Use cases create demand for tools; use cases determine functions; several functions
  form a module; functions determine interfaces; modules determine make or buy. Iterate requirements by iterating
  the use cases. For a bought application, ask for source ownership in the supplier contract; otherwise accept
  the highest-effort onboarding scenario (image plus deployment files only) and its cost.
- **Replacement scope for legacy functions:** aim at parallel functionality, not one-to-one replacement; keep a
  proof-of-concept scope (write access on one pilot machine); state the "continue as-is" consequences.
- **Good-fit test for an assistant or agent use case:** repetitive task, public or general skill set, good
  internal documentation available; advice only versus parameter change decides the human gate.

## 2 · Decision rules

- **Operations-concept gate.** A tool without a named operations owner, service level and support level is not
  rolled out; the verdict is "escalate" (strategy / tool rollout decision), not "ready to build". A tool rollout on request needs
  an operations concept and a named run owner; stop until both exist. `<to confirm>` current status per tool before recommending it (some strategy slides pause
  rollouts that plant summaries still recommend).
- **Precondition fields.** Separation or migration plan of a central data source available; cyber-security and
  purchasing lead times known; approval documents prepared upfront (hardened image, requirements) so approval is a
  request, not research.
- **Energy and metering cases:** data separation and migration of the metering system comes before data
  integration, dashboards and notifications.
- **Maturity sanity check for AI:** AI starts only where the plant has reached reporting and a data model.
- **Targets from need, never from the top of the scale** (already a guardrail) applies to tool choices too: a
  heavier tool needs a named driver.

## 3 · Handoff contract

**Receives:** demand row from `od-use-case-definition`, objects / events and data shape from
`od-requirements-breakdown`, tool-availability table, plant capability levels with evidence.
**Hands on:** the pasted script output and total score; verdict (ready / capability first / over-engineered /
platform investment); for each gap an owner and sequence position; tool boundary sentences relied on; cost class;
operations-concept status. To `od-benefit-calculation` (scope and cost of gaps), `od-portfolio-and-savings-analysis`
(dependency column), `od-system-fit-check` and `od-decision-routing` (escalations).

## 4 · Pitfalls and lessons

- A "recommended if" tool with no cost line invites scope creep.
- A tool rolled out without operations concept or support role was the most repeated barrier in tool landscape
  reviews.
- Rule-engine flows: wrong data types, padded identifier fields, unit conversions and mapping-file sync are
  routine standardisation tasks; budget them.
- Redeploying or upgrading a flow runtime lost production flow configuration: keep flows in version control.
- A close match in the case library is not evidence that these drivers justify this target.

## 5 · Questions to ask / definition of done

Which tool is named and what is its boundary sentence; is it available at this plant; what is its cost class; who
runs it after go-live; is an edge device warranted; where does each logic live; is the scalable state built.
Done (adds to `SKILL.md`): tool boundary and operations-concept status written next to the verdict.

## 6 · AI agent operating notes

- **Can do:** match the stated need to the boundary table and the "recommended if" triggers and return fit /
  redesign / escalate with the boundary sentence cited; run `evaluate_fit.py` on the filled JSON and paste the
  output; draft a tool-fit entry (what it is, what it is not, integration recommended if, effort, cost class,
  example); propose driver ratings for the requester and the DBVE to reconcile.
- **Required inputs:** use-case definition, tool-availability table with read date, plant levels with evidence,
  library.
- **Human gates:** target levels (stay human); the verdict; any escalation as a platform investment; operations
  concept confirmed by the owning role.
- **Evidence to cite:** boundary sentence and its source, capability-level evidence, case-library match, script output.
- **Hand over:** per section 3.
