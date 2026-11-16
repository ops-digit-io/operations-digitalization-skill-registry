---
name: metrics-scorecard
description: >-
  Read, assess and report OD's figures: the Digitalization Scorecard and the Use Case and
  Equipment Integration Power BI reports, against their targets and intervention thresholds,
  and prepare the scorecard update that feeds a reporting round. Use when reporting is
  requested or due on the department's own schedule, when someone asks how OD is tracking or
  whether a metric is on target, when a figure needs a source and a read date, when two reports
  disagree, or when a round needs its numbers prepared or its output recorded. Holds method
  and sources only, no current targets or actuals (look those up live). Not for the savings
  roll-up (bc-portfolio), the adoption diagnosis (deploy-handover) or the monthly retro
  (dept-retro).
license: MIT
metadata:
  id: metrics-scorecard
  aliases: [od-scorecard-reporting]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Spine"
  new_state_step: "Supporting spine"
  owner_role: OD lead; DBVE for use-case metrics, IIAE for equipment metrics
  authority_level: read-only on sources; draft on reports
  status: stable
  valid_until: 2026-11-10
  requires: [dept-context]
  composes: [bc-build]
  okf:
    type: Agent Skill
    title: Scorecard and round reporting
    tags: [all, practice]
---

# Scorecard and round reporting

## Purpose

- Read `dept-context` first.
- A metric without a nameable source is not measured but felt.
- Every figure carries its source, its target and the value at which somebody intervenes.
- Terms: a **metric** is the definition (formula, source, threshold); a **figure** is a value read from a source on a read date.
- The **Scorecard** is `MPEE-OD-Plant_Scorecard`; the **Use Case report** and **Equipment report** are the two Power BI reports below.
- Round and retro mechanics belong to neighbouring skills: this skill supplies the numbers. Round preparation: `dept-governance`; the monthly retro: `dept-retro`.

## Inputs and output

- **In:** the handover findings (`deploy-handover`), the savings roll-up (`bc-portfolio`), readiness changes with their acceptance records (`deploy-acceptance`).
- **Out:** one filled [`assets/scorecard-update-protocol.md`](assets/scorecard-update-protocol.md) per cycle: refreshed figures with read dates, intervention flags, the regional breakout and the honest headline.
- [`outputs.yaml`](outputs.yaml) lists required outputs, criteria, checks and sign-offs.

## Sources, and which one wins

| Source | Authoritative for |
|---|---|
| **Scorecard** (`MPEE-OD-Plant_Scorecard`) | Targets vs. actuals ("Actual Year" figures), readiness RAG matrix, use-case utilization |
| **Use Case report** (`OD-Report-Use_Case_Integration`) | Use-case counts by month, region and process; asset mix |
| **Equipment report** (`OD-Report-Equipment_Integration`) | Equipment counts by month, region and process |

- Where they disagree, **the Scorecard "Actual Year" figures are authoritative.**
- Known trap: a report gauge filtered to the current year can show a different count than the Scorecard's year figure, because the two apply different filters or scopes.
- Report the Scorecard figure and say which filter the other came from.

## The metrics

- This table holds **no values**. Targets, actuals and read dates live in the Scorecard and the two reports; read them live before acting.

| Metric | Formula | Source | Target (look up) | Intervene from | Cadence |
|---|---|---|---|---|---|
| Integrated Use Cases (year) | Count, current year | Scorecard · Digital Use Cases · IS | Annual target on the Scorecard | IS below target-to-date | monthly |
| Integrated Use Cases per month | Count in month | Use Case report · monthly bar | Monthly target on the report | month below the monthly target (red bar) | monthly |
| Integrated Equipment (year) | Count, current year | Scorecard · Equipment Integration · IS | Annual target on the Scorecard | IS below target-to-date | monthly |
| Integrated Equipment per month | Machines in month | Equipment report · monthly bar | Monthly target on the report | month below the monthly target (red bar) | monthly |
| System / capability readiness | RAG per dimension × location | Scorecard · System Integration and Availability | Available at strategic plants | red at a strategic plant | quarterly |
| Use-case utilization rate | Integrated use cases by utilization rate | Scorecard · Digital Use Case Utilization | No fixed target - trend only | low-utilization share rising | monthly |
| Use-case asset mix | Share by asset | Use Case report · asset pie | No target - descriptive portfolio indicator | portfolio indicator | quarterly |
| Value delivery cycle | Demand → live use case | Not captured in any system today | No target - nothing to measure against yet | — | — |

- **The honest headline rule:** report the leading and the lagging metrics side by side, including whichever is behind. Reason: a summary that leads with only the favourable figure is the version that gets found out.
- A count of delivered use cases is a delivery figure, not a value figure: show utilization next to it, and state the basis (system landscape, filter, date) the count was made on.

## Procedure

- Copy this checklist per cycle:

- [ ] 1. Read each figure from its authoritative source (steps below) and note the read date.
- [ ] 2. Compare against target-to-date, not the annual target. A month at 11 against a 12 target is red even in a good year.
- [ ] 3. Flag every metric past its intervention threshold, with the lane owner named.
- [ ] 4. Pre-handover check: every row has a value, a read date and a source. If one is missing, go back to step 1 for that row.
- [ ] 5. Assemble the round input; after the round, record the output and the one retro change.
- [ ] 6. Where a source does not exist, write **⟨to collect⟩**. An honest gap does not block the field.

### Reading one figure

1. Find the metric row above; open its named source (Scorecard page or report page).
2. Read the "Actual Year" figure or the monthly bar; write down the active filters (year, region, process) and the date you read it.
3. Read the target from the same source; if none is shown, use a label from `metric-reading-guide` section 3, never a number.
4. Compute target-to-date (the pro-rata share of the annual target to date) and compare with the figure.
5. Check the intervene-from rule for that metric; its reading is in `metric-reading-guide` section 2.
6. If you have no access to the source, ask the requester for a dated screenshot or export and mark the figure with that origin; do not recall one.

### Example: one protocol row (fictional)

```text
Metric: Integrated Use Cases (year)
Value: 18 (fictional)   Read date: 2026-03-04 (fictional)   Source: Scorecard · Digital Use Cases · IS
Filters on screen: year = current, all regions
Target-to-date: 20 of 60 annual target (fictional)   Status: below target-to-date -> intervene
Lane owner named: DBVE (role)
Other source: Use Case report gauge shows 17 with a different region filter - Scorecard figure reported
```

## The rounds

- Reporting happens on request or on the department's own schedule; no fixed ODEC month cycle is claimed. ODEC is a historical forum, no longer held; its past reports are a source of information.
- The metric cadence column above is the data granularity of a source, not a meeting rhythm.

| Round | What | Input | Output |
|---|---|---|---|
| **COP** (technical round; look up the current schedule) | *How* we do it: technical implementation of machine integration, data models, use cases | Technical issues and feedback; connector updates; new use-case ideas | Data-model/connector updates; rollout guidance; technical Cyber Security aspects |
| **Retro** (on the department's own schedule; method in `dept-retro`) | What did we learn → **one** change | Incidents, metrics, COP feedback | 1 decided adjustment |
| Use Case Definition / Integration Workshops | Define and integrate with plant teams | Plant demand, process diagnostics | Prioritized use cases; integration plan |

- **Escalation window: one round.** An item unresolved at one round carries forward into the next with the label "escalated". Where no round is scheduled, the item goes to the OD lead directly.
- Prepare against the input column; follow up against the output column.
- The retro is mandatory and its output is exactly one decided adjustment. A retro that produces a list has not produced a decision.

## Recipient feedback: the loop acceptance does not cover

| Lane | Recipient | Feedback metric | Source |
|---|---|---|---|
| Use Case Support | Plant ME / operations | Use case adopted into the daily process (utilization rate) | Scorecard · Use Case Utilization |
| Information Integration | Plant IT / use-case teams | Integrated equipment vs. target; readiness turning green | Equipment report; readiness matrix |

## Human gate and AI-agent notes

- **Authority:** read-only on sources; draft on reports. The agent never edits the Scorecard or a report.
- **Humans decide:** the round (or requester) accepts the protocol; the OD lead signs it; lane owners (DBVE, IIAE) act on flags.
- The agent drafts the round input and the follow-up record; it does not decide the one retro change.

## Pitfalls

- Do not publish a figure without its read date and source.
- Do not reconcile two reports by picking the more favourable one.
- Do not report the annual target as though it were the position today.
- Do not fill in `⟨to confirm⟩` targets with plausible numbers.
- Do not carry a figure forward from the previous cycle unread.
- Do not put a descriptive metric (asset mix) into a red-amber-green status.

## Definition of done

- Every metric is read from its authoritative source with a read date and compared against target-to-date.
- Every metric past its intervene-from threshold is flagged with the lane owner named.
- The regional breakout and the honest headline are present; the round output and the one retro change are recorded after the round.
- Open gaps are marked ⟨to collect⟩ or ⟨to confirm⟩ and carried into the next cycle.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/metric-reading-guide.md`](references/metric-reading-guide.md) | You read a metric row, need the rule behind an "intervene from", a label for a missing target, or a lane metric definition |
| [`references/scorecard-structure.md`](references/scorecard-structure.md) | A new metric is proposed (the discipline it must meet), or you need why metrics split into build, delivery, adoption and value |
| [`references/readiness-evidence.md`](references/readiness-evidence.md) | A readiness-matrix cell changes colour: what counts as evidence and what red, amber and green mean |
| [`references/rounds-and-escalation.md`](references/rounds-and-escalation.md) | You prepare or follow up a round, build the regional breakout, or look at the escalation-window gap |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | You need agenda blocks, call for action, status colours, KPI-basis discipline or the handoff contract |
| [`assets/scorecard-update-protocol.md`](assets/scorecard-update-protocol.md) | You start a cycle: the protocol to fill |
| [`references/background.md`](references/background.md) | You need context and rationale; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
| [`references/outputs.md`](references/outputs.md) | The output contract in full (generated from outputs.yaml) |
