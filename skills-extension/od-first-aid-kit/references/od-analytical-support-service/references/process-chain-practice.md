---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for the analytical lane, abstracted from the Operations Digitalization slide decks - ad-hoc, standard and custom analytics, plausibility before explainability, local-versus-global comparison, the idea-collection and potential-analysis routes, the statements an analysis must carry. Guidance only, no figures.
resource: ../procedure.md
status: draft
tags: [analytical-support-service, practice, new-state, draft]
---
# Process-chain practice - ad-hoc and analytical work

Deck-derived practice for the lane's steps 1 to 6, which sit beside the new-state chain (the first-aid kit feeds it; promotion leaves it). `PROPOSAL` = registry synthesis; `<to confirm>` = decks disagree.

## 1. Method in practice

1. **Scope** with `od-first-aid-kit` (SMART statement, object and event, baseline). Then `od-data-availability-check`.
2. **Descriptive first.** Descriptive analytics per process step before anything predictive. If no lever shows, train a predictive model and use explainability to find the few critical parameters; check model quality with an agreement metric before trusting explanations; return explanations to process engineering as candidate settings, not as findings.
3. **Plausibility before models.** Missing or sparse features, class balance, period, units. Report "model quality enough for explainability: yes / no" before drawing any plot. Most of the effort is data preparation.
4. **Statistical comparison of a small local dataset with a large global reference:** descriptive statistics; distribution fit on the worst-case histogram; discrete-class distribution; compare local to global per class; report classes missing locally. Pitfalls: uneven bin widths distort fits at small and large sizes; reject fits that violate a plausibly decreasing curve; read the axis scale before comparing.
5. **Control-loop problems:** build a transparency dashboard of controller inputs and outputs; list open questions on how control is implemented (built-in or custom block, parameters, dead band, interval); write down current understanding; list other influencers and signals needed; obtain the current program; plan tests at the next ramp-up; long term define closed-loop use cases.
6. **Deliver and explain** (step 5), then track utilization (step 6) and hand a recurring one to promotion.

**Two further routes into the lane:**

- *AI idea collection* (four steps): requester enters the idea in a shared list; OD is notified and holds a short call asking the standard questions; the idea is recorded and later prioritized into initiatives; expectation set: not every idea is ready to be executed.
- *Potential analysis for an idea family* (for example predictive maintenance or a process-focused analysis): workshop series with the central interface and selected local heads to collect ideas; each idea on a canvas; go / no-go rating; potential analysis with scaling factors, actual KPIs (especially deviations), technical requirements, risks and obstacles; demand for tools captured. The result is a 360-degree view, not an implementation.
- *Pilot approach for an AI idea:* listen to process specialists; get clear targets and measurables; check what data is acquired and how reliable and complete it is; decide in a workshop; run the pilot, with an external expert if needed; train the team on tools first; start with labelled data, first insights, then a first predictive model.

## 2. Decision rules

- **Ad-hoc, standard, custom.** Ad-hoc answers a question. Standard is maintained centrally and rolled out. Custom only if the value is very high, prototyped first, and integrated into standard systems before it counts as mature.
- **Value-risk screening.** Build what is high value and low risk. For high risk, design the cheapest possible test that teaches the most important thing. Do not test or build low-value ideas. A triage grid for AI topics: low barrier / high potential, mid barrier / high potential, high barrier / mid potential.
- **Maturity sanity check.** AI starts at the third level of the data-value ladder; do not rank AI work above basic data-model and reporting work where the plant has not reached reporting.
- **Hybrid capture** for events the controller cannot see.
- **Infrastructure:** cloud data lake when no real time, many sources, long storage; edge platform when real time, few sources, modest compute.
- **Human-supervised analysers:** the tool proposes (signal candidates, start and stop conditions, plausible cycle times and downtimes), a person confirms, abnormal values go to notification, outputs include an influencer ranking; user interaction at tuning and deployment is mandatory.
- **Promote only on recurrence** (`od-use-case-standardization`). A one-off analysis closes as ad-hoc.
- **A knowledge or troubleshooting assistant** is decided case by case at intake: ask for a measurable before/after. With one it goes the use-case route (savings only with documented basis); without one it is tracked as an initiative with an owner and a usage measure, not a counted saving.

## 3. Statements every analysis must carry

Data period; sample size per class; OK / NOK ratio; which parameters were removed and why; filters applied (long-loss threshold, outlier rule); analysis window; median with and without alerts; model-quality verdict; what the result cannot show. Basis label for any saving mentioned: calculated / estimated / none.

## 4. Handoff contract

| Receives | From |
|---|---|
| the filled first-aid form with SMART statement and object / event | `od-first-aid-kit` |
| data verdict | `od-data-availability-check` |

| Hands on | To |
|---|---|
| insight, asset, caveats list and the statements above | the requester (plant, operational-excellence function) |
| recurrence and utilization evidence | `od-use-case-standardization` |
| data gap with missing-signal table | Information Integration lane |
| analysis outcome that needs expert interpretation | the process expert, marked "needs expert review" |

## 5. Pitfalls and lessons

- **Retrospective only:** the process is continuously optimized, the data are snapshots.
- **Sparse recipe data** had to be removed; too few samples for aggregated product models limit validity.
- **Factors identified, impact unproven:** the process impact needs interactive analysis with process experts; a model revision followed.
- **No standard process for ad-hoc analyses,** unclear responsibilities, capacity limits for analytics and for pre-processing, data quality: all named organizational lessons.
- **Iterations add scope** (operator times, loading times) after the first rule set; agree the definition of done first.
- **Keep the requirement from the plant.** An analysis without a plant owner for the decision it informs does not get used.

## 6. Questions to ask and definition of done

Which question, which decision, whose? Which period and sample? Which baseline? Is the result retrospective? Who validates with process engineering?

**Done (adds to `SKILL.md`):** statements in section 3 are in the output; the "needs expert review" step has a named reviewer; recurrence evidence recorded for promotion.

## 7. AI agent operating notes

- **Can do:** run descriptive statistics and the plausibility checks; compare local with global distributions; draft the analysis plan and the caveats list; build the statement block of section 3; label the work ad-hoc; collect recurrence evidence; capture AI ideas in the four-step list and draft the standard questions.
- **Needs:** data extract with period, the first-aid form, read dates.
- **Human gate:** "needs expert review" before any conclusion about a process; the requester accepts the result; commitment to industrialization is the responsible human's.
- **Must cite:** data source and period, filters, model-quality check.
- **Hands over:** the insight with its caveats, never an unvalidated insight presented as fact.
