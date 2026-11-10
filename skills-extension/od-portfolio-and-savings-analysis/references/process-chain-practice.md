---
type: Skill Reference
title: Process chain practice
description: How ranking and portfolio reading (steps 24 and the spine) is run in the AI-driven chain - ranking criteria and their order, numbered planning states, the where-saved matrix, dependency versus return ordering, hygiene and kill rules, and what an agent may draft. Pattern only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, analytical-support-service, practice, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice

Distilled from the Operations Digitalization slide decks, abstracted into process guidance. No company figures. `PROPOSAL`
marks a synthesis; `<...>` is unknown. It adds to [`prioritization.md`](prioritization.md) and
[`rollup-method.md`](rollup-method.md).

## 1. Method in practice

1. **Cluster first.** Group use cases by process or capability (cross-process versus per process), record demand as
   "recorded use cases in recorded plants", and assign a first-mover plant per candidate. Bundle by shared platform.
2. **Number the planning states.** Each ranking iteration is a numbered *planning state* with its trigger: state one from
   analysis of the list, then after technical input, then after the latest workshops, then after plant priority input. Keep
   each state's baseline file named. The state number and trigger belong on the record.
3. **Read scale as three lists per top use case:** where it saved, where it was deployed without savings, where it still has
   potential. A visual of "where first, where saved, where it went, where deployable, where not" helps.
4. **Split the estate by the variable that drives the economics before averaging** (`od-benefit-calculation`); compare
   regions and segments, never blend them.
5. **State the staffing assumption** next to every projection. The same portfolio projects differently under central-only
   staffing and central-plus-dedicated plant key users; most of the difference is scaling through machine connectivity.
6. **Capacity indicator for the department itself:** integration speed, use-case identification speed, development and
   deployment speed, each divided by the manpower in that activity. Use it to sanity-check the ranking against what can be
   delivered.
7. **Record the KPI basis with its date.** Counting use cases against a threshold assumes the system landscape of the past;
   centralising a platform can break reporting consistency.

## 2. Decision rules / triage

- **Order of criteria, stated explicitly:** 1) savings (value, ROI, with its basis label), then as secondary criteria
  2) generalisation potential (expected scaling effect, number of recorded demands across plants, existence of a validated
  prototype) and 3) effort. Write which order you used.
- **Dependency as tie-breaker.** Where criteria tie, order by dependency: foundation first (platform, standards, asset and
  lifecycle visibility), enablers next (training), risk and compliance, analytics last because it only proves benefit once the
  others exist. Add a dependency column to the ranking record. `PROPOSAL` (the deck shows the two orders side by side).
- **Three buckets by action, not size:** *just do* (generic dashboards, notifications, energy-saving cases that need no new
  development), *go forward* (continue or integrate an earlier proof of concept; each depends on a shared enabler),
  *lead change* (exploratory). Assigning *lead change* is a human call.
- **Maturity sanity check for AI cases:** do not rank an AI use case above basic data-model and reporting work in a plant
  that has not reached reporting.
- **Use cases with a missing baseline** go to the unscored bucket (already in the method), never to the bottom.
- **Low-saving entries:** clean up the list, but an entry that is cheap to scale (a container exists) may stay as a scaling
  item. `PROPOSAL`
- **Zero-saving scaled-out use case:** a use case that is scaled but reports no saving is "to be evaluated until
  investigated". Only a human (the OD lead with the plant owner) may decide "no potential"; an agent never writes it.
- **Kill or hold explicitly** with a recorded reason (no data foundation, insufficient savings, another party already
  collects the data), so cancelled ideas are not re-raised.
- **Plants with equal integration and unequal savings** point to people and method, not technology: look at who drives ideas,
  whether savings are calculated with controlling, and community-call participation (a leading indicator).

## 3. Handoff contract

| Receives (from) | Hands on (to) |
|---|---|
| Tagged benefit rows (`od-benefit-calculation`) | Ranked list with criteria order, planning-state number, unscored bucket, dependency column -> `od-capital-request`, plant roadmap |
| Use-case list and savings ledger, read with date (`od-sharepoint-list-export`) | Portfolio review protocol -> `od-scorecard-reporting` round prep |
| Utilisation evidence (`od-handover-and-adoption`) | Where-saved matrix and kill/hold register -> `od-retro`, `od-risk-watch` |

## 4. Pitfalls and lessons

- "Recorded" demand per cluster used as an impact proxy: tracked demand is not proven saving.
- Reporting not prioritised in a turbulent period, so impact could not be shown; the cure was an impact analysis, a barrier
  overview and automatic reporting.
- Use cases with no registered plant savings project are invisible to the ledger, so the plant looks idle.
- Estimated value per use case decays as the best ones are done first; do not project the early average forward.
- Savings reported incompletely make the target look missed while the delivery count is on target: separate *unreported*
  from *unused potential*.
- Rollout count as value: reusability is cheap; monetary impact is derived per site.

## 5. Questions to ask / definition of done

- Which planning state is this, and what triggered it? What is the denominator? Which cases are unscored, and why?
- What does each top case depend on, and is the dependency itself in the ranking?
- Done when: criteria order written, state numbered, unscored and kill/hold buckets visible, staffing assumption and read
  date stated, regions not blended.

## 6. AI agent operating notes

- **Can do:** produce the ranking table with a cited evidence cell per criterion; compute the where-saved / deployed-without-
  savings / potential matrix from the list and ledger; flag blank reliability and missing registered projects; draft the
  community-call "no registered project" list. It labels tracked versus proven and **never decides "no potential"**.
- **Required inputs:** list and ledger exports with read dates, plant priority input, prototype status.
- **Human gate:** ranking sign-off and the order of criteria; *lead change* assignment; kill or hold.
- **Evidence to cite:** list row id, ledger row id, read date, planning-state baseline file.
- **Hands over:** the review protocol to `od-scorecard-reporting`; the ranked list to `od-capital-request`.
