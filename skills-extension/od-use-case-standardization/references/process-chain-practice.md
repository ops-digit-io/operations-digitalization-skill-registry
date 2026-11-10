---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for standardization, abstracted from the Operations Digitalization slide decks - archetypes, category to method to data-job mapping, graduation from validated prototype to configurable container app, the library tree, and why a scaled use case needs utilization rather than a rollout count. Guidance only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [practice, use-case-support-service]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - standardizing and scaling

Deck-derived practice for step 26 (implement and graduate) and the archetype logic used at intake and definition. `PROPOSAL` = the registry's synthesis.

## 1. Method in practice

**From library to archetype to executable standard** (the journey the decks describe):

1. **Collect** - the use-case library and the plants' lists, workshop captures and canvases are the raw material. Look for the *missing pattern*: what recurs but has no standard.
2. **Categorize** - assign each use case to one archetype class (below), then to a category (for example statistical process control, machine availability, downtime).
3. **Method** - each category has a dedicated set of methods (for statistical process control: descriptive statistics, outlier detection, trend detection; for machine availability: cycle times, setup, errors).
4. **Data job** - each method translates into a data-transformation or analytics job, packaged as a container. Several use cases then share the same methods.
5. **Standard application** - the validated prototype becomes a container app with flexible algorithms and configurable rule sets, deployed through the app store; it becomes the standard other plants take.
6. **Adapt per plant** - the plant records deltas only (`SKILL.md`, procedure step 4).

A use case is **ready to use** when its methods have run and their outputs exist. A need alone (a sentence in the backlog) is not a specification: it has no technical requirements until a category is assigned.

**Archetype classes** (fixed vocabulary, same as `catalog-usecase`): standard cross-process, standard per-process, non-standard unique. The classes are about **reuse potential**, and each has a default action: cross-process - start with priority; per-process - start; unique - do not start, run an impact analysis first.

**Library tree** (for navigation): standard group (savings tracked per fixed number of machines) -> plant standard group -> single element; and core-process group -> plant core-process group -> single element.

**Process-specific data models** are the enabler of per-process standards: survey public companion specifications; extend with in-house types in a modelling editor; combine with the public standard and build an example instance for one machine; review and iterate with process engineering until release; instantiate per machine. Goal: the same views for all machines of one core process. Which process gets a model next can be decided by a vote among plants. Detail belongs to `od-signal-standardization`.

## 2. Decision rules

- **Priority order.** Savings first (value, ROI); generalization potential and effort are secondary criteria; dependency order (foundations before what depends on them) is the tie-breaker. State the order you used on every ranking.
- **Custom use cases** only if the expected value is very high; prototype first; they count as mature only after integration into the standard systems.
- **Low saving, cheap to scale.** A low-saving entry is cleaned from the list, but may stay as a scaling-effect item if a container already exists. `PROPOSAL`.
- **Manual-entry use cases** (lab data, quality data, downtime reasons) need data model, storage, input screen and analytics in one standard, otherwise each plant builds its own variant.
- **Machine-learning standards** need requirements, multi-plant data, a validated model, a defined model interface, a retraining process and a visualization concept validated with the plant.
- **Scaling is a promise to measure, not a result.** For every top use case keep three lists: where it saved, where it was deployed without saving, where it still has potential. Deployed without saving means "to be evaluated", not "no potential".
  Such an entry stays "to be evaluated" until investigated; only a human (the OD lead with the plant owner) may decide "no potential" or retirement. An agent never writes it.
- **Adoption means integration into a standard operating routine** with a defined screen, escalation flow and owner, not "dashboard live".
- **Local solutions that already fit the method** are input to standardization, not new demand.

## 3. Handoff contract

| Receives | From |
|---|---|
| use-case class, archetype guess, object / event decomposition | `od-use-case-intake-triage`, `od-first-aid-kit` |
| validated prototype, flows documentation, deltas | `od-analytics-asset-build`, `funnel-prototype` |
| standard signal set verified for a second plant | `od-signal-standardization`, `od-cross-plant-compatibility` |
| savings rows with source and basis label | `bc-build` |

| Hands on | To |
|---|---|
| review record: template, library check, cluster baseline and delta, CSP-readiness verdict, graduation checklist with missing items | `od-decision-routing` (CSP gate), `catalog-usecase` |
| list of plants where it saved / deployed without saving / has potential | `od-portfolio-and-savings-analysis`, `od-scorecard-reporting` |
| utilization moment per plant | `od-handover-and-adoption` |

## 4. Pitfalls and lessons

- **Rollout count is not value.** Many of the most widely scaled use cases reported no saving at the target plants; savings concentrated in a few that attacked a real cost driver. Reuse is cheap; monetary impact must be derived per plant.
  Report utilization next to the count of deployments.
- **Equal integration effort, unequal savings points to people and method, not technology.** The good-practice signature: production drives ideas, the engineer asks for blueprints from other plants, requirements are formalized with OD, savings are calculated with controlling.
  The bad-practice signature: a single engineer "only responsible for the technical part", standards ignored, no one knows how to calculate savings.
- **Unreported is not unused.** Deployers often do not report; distinguish unreported saving from unused potential before concluding.
- **Dashboards per plant, not harmonized** repeats as a standardization debt.
- **Standardization debt through new trackers.** New systems, slides and trackers are added instead of cleaning up. Prefer retiring the old one.
- **KPI basis moves.** A use-case count against a threshold assumes the system landscape of its year; platform centralization changes the count. Record the KPI basis with its date.
- **The generalization boundary is unstated** between a generic influencer-detection use case and process-specific analytics; do not claim a generic solution without naming the boundary.
- **The base data model fits greenfield, discrete, time-series-centric machines**; brownfield with many controller types and continuous processes needed other models. Check before calling a use case cross-process (`od-cross-plant-compatibility`).

## 5. Questions to ask and definition of done

Which archetype and why? Which category and methods? Is there a validated prototype, and is it packaged? Which plants have it, which use it, how often, with what action, and where is the saving (or the reason none is reported)?
Does the use case need production metadata (order, part, batch, recipe) beyond signals? Is the signal set consumable at a second plant?

**Done:** review record complete; archetype, category and method named; graduation checklist shows which conditions hold and which are missing; scaling lists written; utilization recorded where the entry is live.

## 6. AI agent operating notes

- **Can do:** classify use cases into archetype and category from list text; propose the method and data-job mapping; list graduation conditions met or missing; compute the three scaling lists from the use-case list and savings ledger and flag blank reliability.
- **Needs:** use-case list, library with CSP field, savings ledger, utilization records, read dates.
- **Human gate:** the CSP decision (owner outside OD); the call "retire" or "no potential"; adding a library entry. The agent must label tracked versus proven and must not conclude "no potential".
- **Must cite:** list rows, library ids, ledger rows, read dates.
- **Hands over:** the review record and the gap list to `od-decision-routing`.
