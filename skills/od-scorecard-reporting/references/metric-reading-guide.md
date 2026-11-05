---
type: Skill Reference
title: Metric reading guide
description: How to read each kind of department and lane metric (the rule behind an intervene-from column, the label for a missing target), definitions of the lane-level metrics including those not yet captured with a proposed start and stop event, and companion pairs that stop a single number from misleading.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, scorecard, metrics]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Metric reading guide

Derived from the lane `metrics.md` notes and the department metrics note. **Definitions and ways of reading only: no targets, no
actuals, no read dates.** Targets and actuals are looked up on the Scorecard and the two reports, with their read date, before any
figure is quoted. Own synthesis is marked `PROPOSAL`; unknowns are `<...>`.

## 1. The shape of a lane metric row

Every lane metric note carries the same five columns. Read them in this order.

| Column | What to read | Typical trap |
|---|---|---|
| Metric (this lane only) | The question it answers for this lane, not the department average | Quoting the department roll-up as if it were the lane's |
| Formula | The event counted and the period | Counting a different event (created versus integrated versus live) |
| Source | The report, view or tracker that is authoritative | Using a second source with a different filter (see "Sources, and which one wins" in `SKILL.md`) |
| Target | Look-up value, or a label (section 3) | Inventing a target, or carrying one from another year |
| Intervene from | The condition that triggers a conversation | Reading it as "failed"; it is the threshold for asking why |

The metrics notes also carry a review cadence in their header (weekly for lane metrics, longer for context notes). Match the
cadence of the question to the cadence of the metric: a weekly look at a monthly bar tells you nothing new.

## 2. The rule types behind "intervene from"

| Rule type | Wording seen | Reads as | First question when it fires |
|---|---|---|---|
| Actual versus target-to-date | "actual below target-to-date" | Cumulative position against the pro-rata of the year target | Is the gap a late start, a stalled pipeline or a demand shortage? |
| Month versus run-rate | "month below the monthly target (red bar)" | One month under the run-rate implied by the annual target | One-off (holiday, freeze) or a trend? Look at the previous months |
| Readiness colour | "not available (red) at a strategic plant" | A cell on the readiness matrix is red where the strategy says it must be available | Which acceptance evidence is missing (`readiness-evidence.md`)? |
| Share rising | "low-utilization share rising" | A trend in a distribution, not a level | Which use cases moved into the low band, and do they share a ritual gap? |
| Turnaround rising | "turnaround rising" | Time between two events grows | Which stage grew: waiting, data, analysis or delivery? |
| Behind plan | "behind plan" | Progress report below the plan for the same period | Is the plan or the progress stale? |
| Descriptive / value indicator | "portfolio indicator", "value indicator" | No intervention; read for context | Does the mix still fit the strategy? |
| Nothing to measure yet | "-" with a label | The metric has no source | Who collects it, and from which event? (section 4) |

A metric with a **descriptive** rule must not be put in a red-amber-green status. A metric with **no source** must not be shown
with a number.

## 3. Labels for a missing target

Use one of these words in every table instead of a blank or an invented number.

| Label | Meaning |
|---|---|
| look up (owner) | A target exists; it lives in the named report or with the named owner |
| trend only | By decision there is no fixed target; watch direction |
| descriptive | An indicator of portfolio shape, not performance |
| not captured | No system records the event today; nothing to measure against |
| `<to confirm>` | A target is expected but unconfirmed |
| `<to collect>` | A source is expected but not built |

## 4. Lane metric definitions

### Use Case Support Service

| Metric | Definition | Reading note |
|---|---|---|
| Integrated use cases (year, per month) | Use cases whose integration reached the counted status in the period | A delivery figure, not a value figure. Show utilization next to it |
| Use-case utilization rate | Distribution of integrated use cases by recorded utilization rate | Trend only. A falling share of high-frequency use is the signal; ask for the ritual (`od-governance-cadence/references/rituals-and-consumption.md`) |
| Asset mix | Share of delivered assets by type (dashboard, analytics, report, app, agent) | Descriptive. A mix drifting to one type is a question for `od-analytics-asset-build`, not a target miss |
| Value delivery cycle | Time from demand to live use case | Not captured. `PROPOSAL`: define start as the demand registered at intake (`i1`), stop as the use case recorded live; whether both timestamps exist on the lists and can be joined is `<to confirm>` |

### Analytical Support Service

| Metric | Definition | Reading note |
|---|---|---|
| Use-case utilization rate | As above | Same reading |
| Analytics asset output | Count of dashboards, reports and analytics delivered in the period | Output, not use. Pair with utilization |
| Ad-hoc turnaround | Time from request to insight delivered | Not captured. `PROPOSAL`: start at the request timestamp in the request channel, stop at the answer sent; classify requests so that waiting for data is separated from analysis time |
| Promotion rate | Share of ad-hoc analytics promoted to a standard use case | Value indicator, no intervention. A rate near zero can mean either no recurring value or a missing promotion step |

### Project Support and Application Consultancy

| Metric | Definition | Reading note |
|---|---|---|
| Integration projects to acceptance | Projects that passed acceptance, against the active ones | Not captured in a tracker. The acceptance evidence is the protocol (`od-acceptance-test`), so the count can be built from protocols `<to confirm>` |
| Equipment integration progress | Reported progress against plan in the ODEC report | Compare with the equipment report of the integration lane; the two should agree |
| Applications progress | Reported progress against plan | Same |
| Use-case impact | Realised impact of delivered use cases in the ODEC report | Impact is only as good as the saving basis behind it (`od-benefit-calculation`) |
| On-time delivery | Projects delivered on schedule | Not captured. Define "schedule" as the milestone agreed at kick-off, not the last re-plan |

### Information Integration Service

| Metric | Definition | Reading note |
|---|---|---|
| Integrated equipment (year, per month) | Machines integrated in the period | Capacity indicator, the earliest leading signal |
| System / capability readiness | Colour per dimension and location on the readiness matrix | Move to green only with an acceptance pass |
| Integration acceptance and rework rate | Acceptances passed against reworked | Not captured. `PROPOSAL`: derive from acceptance protocols, counting a re-test after a failed item as rework |

## 5. Companion pairs

Never show one half alone.

| Pair | Why |
|---|---|
| Integrated use cases and utilization | Delivery without adoption is cost |
| Integrated equipment and readiness | Machines connected are not capabilities available |
| Analytics asset output and promotion rate | Output without a path to standard produces one-offs |
| Project progress (ODEC) and acceptance passed | Reported progress is a claim; acceptance is evidence |
| Utilization and tracked savings | Use without a saving basis cannot be claimed as value |

## 6. Reading a number against a manual baseline

When a metric compares a digital measurement with an earlier manual one, state how each was captured. Manually recorded performance
figures tend to read more favourably than automatic ones, so a first automatic reading can look worse without any real
decline. Report the change of method before reporting the change of value (see `od-context/references/provenance-and-source-catalogue.md`).

## AI agent operating notes

- **May do:** label every missing target with one of the section 3 words; map a fired "intervene from" to its rule type and the first
  question; assemble companion pairs; draft a definition proposal for a not-captured metric with start and stop events.
- **Inputs:** the Scorecard and the two reports (with read date), the lane metric notes, the acceptance protocols for evidence.
- **Evidence to cite:** source name, filter, read date.
- **Human gate:** a new or changed metric definition is approved by the OD lead before it enters the Scorecard; an agent never
  invents a target.
- **Hands over to:** `scorecard-structure.md` (the five-field discipline for a new metric), `od-retro` (the pattern across months),
  `od-risk-watch` (a persistent breach).
