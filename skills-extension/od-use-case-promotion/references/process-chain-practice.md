---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for promotion, abstracted from the Operations Digitalization slide decks - graduation conditions, the use-case exchange with the operational-excellence function, the promotion template fields, recurrence evidence, and retire versus re-evaluate. Guidance only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice, new-state, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - promoting an asset

Deck-derived practice for step 26 (graduate) and the analytical lane's step 6. `PROPOSAL` = registry synthesis; `<to confirm>` = decks disagree.

## 1. Method in practice

1. **Gather recurrence evidence from demands, not from deliveries.** Recorded demand across plants ("n use cases in m plants") is a scaling estimate, not proven saving. Pair it with the object / event reduction: if several differently worded requests reduce to the same object and event, that is recurrence.
2. **Check the graduation conditions** the decks list (a promotion package must state each as met, missing or not applicable):
   - the prototype is **validated** with its plant owner;
   - it is **packaged** as a configurable container app (flexible algorithm, configurable rule set) rather than a one-plant flow;
   - its **interface** is defined;
   - for learned models: a retraining and monitoring process and data from several plants;
   - it has a **library entry** (problem, situation, digital support, identified in, machine integration used, development, link, can it replace a manual practice);
   - the signals are standard and consumable at a second plant.
3. **Run the exchange with the operational-excellence function** (OPEX) before promoting. Format: a standing call with OPEX, engineering, OD and the plant; two use cases per call, a short slot each, showing scope and potential.
   Homework per item for OPEX and the plant: *what is the defined working procedure with this artefact? is there an estimated impact? if not, what holds you back?* Next call: the impact is presented.
   Capture in the library: presented? potential defined? standard procedure defined? estimated impact? action for impact measurement? improvement project initiated (with link)? Hand over to OPEX per item: awareness, evaluation and feedback, improvement.
4. **Complete the promotion template** (fields the decks use for marketing a use case): method name and link; the standard method; the digital standard use case; the standard process; WHAT the standard process achieves; HOW method and use case combine; WHY; an example everybody understands; interfacing processes, responsibilities and channels.
   Pair *standard method + digital standard use case + standard process* (for example changeover method, value-stream mapping for lead times, switch-off campaigns and peak detection for energy).
5. Continue with `SKILL.md` steps 5 to 9 (placement, handover check, catalog conditions, decision, handover).

## 2. Decision rules

- **Promote / keep as ad-hoc / retire** remains the result set. Refusing to promote is valid.
- **Promote only with an action behind it.** An asset whose users do not act on it, and where no standard working procedure exists, is a keep or a retire, however many plants asked for it.
- **Zero-saving scaled assets.** A scaled-out asset with deployments but no saving is "to be evaluated" until investigated; do not write "probably no potential" (one deck revision did, unproven). Only a human (the OD lead with the plant owner) may decide "no potential" or retirement; an agent never writes it.
- **Unique stays unique.** A site-specific asset (factory condition, legacy system, one-off) is not promoted; run an impact analysis only if the value is very high.
- **Go forward / lead change.** A candidate that depends on a shared enabler that does not exist yet waits for it and is recorded as such; an exploratory candidate is a human call.
- **Value ordering.** Rank competing promotion candidates by savings first (value, ROI); generalization potential and effort are secondary criteria; dependency order is the tie-breaker (`od-use-case-prioritization`).
- **Kill with a reason.** Record why a candidate was stopped (no data foundation, insufficient saving, another party collects the data) so it is not raised again.
- **A knowledge or troubleshooting assistant** does not fit the before / after and savings definition of a use case; it is decided case by case at intake (`od-use-case-intake-triage`): with a measurable before and after it follows the use-case route, without one it is tracked as an initiative with an owner and a usage measure. Do not force it through promotion as a counted saving.

## 3. Handoff contract

| Receives | From |
|---|---|
| insight delivered and used, request history, utilization records | `od-analytical-support-service`, `od-first-aid-kit` |
| validated asset, flow documentation, signal list | `od-analytics-asset-build`, `od-signal-standardization` |
| handover record with plant owner | `od-handover-and-adoption` |
| savings rows with basis | `od-benefit-calculation` |

| Hands on | To |
|---|---|
| promotion package with decision, evidence, graduation conditions met and missing, named responsible human | `od-use-case-definition` (collect phase), `od-use-case-prioritization` |
| CSP preparation input | `od-use-case-standardization` |
| outcome record for the promotion rate | `od-scorecard-reporting` |

## 4. Pitfalls and lessons

- **A prototype that works at one plant is not a standard.** Scaling it needs a containerized, more flexible algorithm; iterations also add scope (operator times, loading times) after the first rule set.
- **Utilization not measured, savings not registered.** Use cases without a registered savings project are invisible to the ledger; a sprint review without a savings baseline never reports the saving.
- **Library with savings: nobody looks.** Offering it is not adoption. A proactive calculator and an owner at OD worked better than asking plants to evaluate their own use cases.
- **Scaling count mistaken for value.** Many widely scaled assets carried no saving. Promotion by popularity alone repeats that.
- **A dashboard without an action owner** is a build smell and a weak promotion candidate.
- **Reuse question:** ask "what needs to happen to be able to reuse this?" (concept and quality) before promoting.

## 5. Questions to ask and definition of done

How many distinct requesters, plants and periods? What changed between requests? Who uses the asset, in which routine, with which action? Is there an estimated impact and who owns the measurement? Which graduation conditions are missing?

**Done:** decision stated; evidence cited; graduation conditions listed as met / missing; responsible human named; next step named.

## 6. AI agent operating notes

- **Can do:** collect recurrence evidence from request logs and the use-case list; reduce requests to object / event; check the graduation conditions; draft the promotion template and the library capture fields; keep OPEX homework items up to date from call notes and chase the open ones; compute where-saved / deployed-without-saving / potential.
- **Needs:** request history, utilization records, list and library rows, savings ledger, read dates.
- **Human gate:** commitment to industrialization (named responsible human); CSP; the call "retire" or "no potential"; the local key user confirms the standard procedure.
- **Must cite:** request ids, utilization records, ledger rows, library ids, read dates.
- **Hands over:** the package, with unknowns as `<...>`, and an outcome record for the promotion rate.
