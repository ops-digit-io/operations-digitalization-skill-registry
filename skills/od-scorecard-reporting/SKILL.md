---
name: od-scorecard-reporting
description: >-
  Fetch, assess and report OD's numbers — the Digitalization Scorecard and the Use Case
  and Equipment Integration Power BI reports — against their targets and intervention
  thresholds, and prepare and follow up the ODEC and COP rounds. Covers which report is
  authoritative for which figure, how to read targets and actuals live with their read date,
  when a number crosses into "intervene", and the recipient-feedback loop per lane. Holds
  method and sources only, no current targets or actuals (look those up live). Use
  when monthly or ODEC reporting is due, when someone asks how OD is tracking, when a
  metric needs a source, or when a round needs preparing or following up.
license: MIT
metadata:
  id: od-scorecard-reporting
  tier: practice
  lane: all
  owner_role: OD lead; DBVE for use-case metrics, IIAE for equipment metrics
  authority_level: read-only on sources; draft on reports
  status: stable
  sources_read: 2026-10-22
  valid_until: 2026-11-10
  requires: [od-context]
  composes: [od-benefit-calculation]
  derived_from:
    - ops-knowledge-graph/.../00-core/07-metrics.md
    - ops-knowledge-graph/.../00-core/06-operating-rhythm.md
    - ops-knowledge-graph/.../20-lanes/*/metrics.md
    - "ISO 22400-2:2014, Automation systems and integration — Key performance indicators for manufacturing operations management — Part 2: Definitions and descriptions. The KPI-definition discipline (formula, elements, time behaviour, unit, user group); equipment KPIs reference IEC 62264 work units."
    - Kaplan, R.S., Norton, D.P. (1992). The Balanced Scorecard — Measures That Drive Performance. Harvard Business Review, 70(1), 71-79. The four-perspective structure and the leading/lagging cause-effect chain.
    - personal vault, Work-OpsDigit-Knowledge/ODEC Facts/ODEC Facts - Department KPIs and Roadmap Status.md (AI-extracted archive staging, not human-reviewed; used only for the recurring regional-breakout report shape, not for any specific figure, which the live Scorecard supersedes)
  okf:
    type: Agent Skill
    title: Scorecard and ODEC reporting
    tags: [all, practice]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Scorecard and ODEC reporting

Read `od-context` first.

A metric without a nameable source is not measured but felt. Every figure below carries
its source, its target and the value at which somebody intervenes.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/scorecard-structure.md`](references/scorecard-structure.md) | Why the metrics split into build/delivery/adoption/value, the discipline (formula, elements, time behaviour, unit, user group) a new metric must meet before it joins the table, and the IEC 62264 work-unit basis of the equipment KPIs |
| [`references/readiness-evidence.md`](references/readiness-evidence.md) | What actually moves a readiness-matrix cell to "Available" — never a status update, always a recorded `od-acceptance-test` pass — and what red/amber/green mean here |
| [`references/metric-reading-guide.md`](references/metric-reading-guide.md) | How to read a lane metric row and the rule behind each "intervene from"; labels for a missing target; lane metric definitions incl. not-yet-captured ones with proposed start and stop events; companion pairs |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | How a round is prepared and followed up in practice: forums and agenda blocks, call for action, status colours, KPI-basis discipline, utilization next to delivery count, handoff contract, agent notes |
| [`references/rounds-and-escalation.md`](references/rounds-and-escalation.md) | ODEC/COP's real recurring content shape (regional breakout, not a blended total), how to prepare and follow up each, and where the escalation-window gap actually sits |

## Sources, and which one wins

| Source | Authoritative for |
|---|---|
| **Digitalization Scorecard** (`MPEE-OD-Plant_Scorecard`) | Targets vs. actuals ("Actual Year" figures), readiness RAG matrix, use-case utilization |
| `OD-Report-Use_Case_Integration` | Use-case counts by month, region and process; asset mix |
| `OD-Report-Equipment_Integration` | Equipment counts by month, region and process |

Where they disagree, **the Scorecard "Actual Year" figures are authoritative.** A known
trap of this kind: a report gauge filtered to the current year can show a different count
than the Scorecard's year figure because the two apply different filters or scopes. Report
the Scorecard figure and say which filter the other came from.

## The metrics

This table holds **no values**. Targets, actuals and read dates live in the Scorecard and
the two reports; refetch from Power BI before acting, and state the read date and source
with any figure you publish.

| Metric | Formula | Source | Target (look up) | Intervene from | Cadence |
|---|---|---|---|---|---|
| Integrated Use Cases (year) | Count, current year | Scorecard · Digital Use Cases · IS | Annual target on the Scorecard | IS below target-to-date | monthly |
| Integrated Use Cases per month | Count in month | Use_Case_Integration · monthly bar | Monthly target on the report | month below the monthly target (red bar) | monthly |
| Integrated Equipment (year) | Count, current year | Scorecard · Equipment Integration · IS | Annual target on the Scorecard | IS below target-to-date | monthly |
| Integrated Equipment per month | Machines in month | Equipment_Integration · monthly bar | Monthly target on the report | month below the monthly target (red bar) | monthly |
| System / capability readiness | RAG per dimension × location | Scorecard · System Integration and Availability | Available at strategic plants | red at a strategic plant | quarterly |
| Use-case utilization rate | Integrated use cases by utilization rate | Scorecard · Digital Use Case Utilization | No fixed target - trend only | low-utilization share rising | monthly |
| Use-case asset mix | Share by asset | Use_Case_Integration · asset pie | No target - descriptive portfolio indicator | portfolio indicator | quarterly |
| Value delivery cycle | Demand → live use case | Not captured in any system today | No target - nothing to measure against yet | — | — |

**The honest headline rule:** report the leading and the lagging metrics side by side,
including whichever is behind. A summary that leads with only the favourable number
(typically the one that is on target) is the version that gets found out. A count of delivered
use cases is a delivery figure, not a value figure: show utilization next to it, and state the basis
(system landscape, filter, date) a count was made on.

## Recipient feedback — the loop acceptance does not cover

| Lane | Recipient | Feedback metric | Source |
|---|---|---|---|
| Use Case Support | Plant ME / operations | Use case adopted into the daily process (utilization rate) | Scorecard · Use Case Utilization |
| Information Integration | Plant IT / use-case teams | Integrated equipment vs. target; readiness turning green | Equipment Integration report; readiness matrix |

## The rounds

| Rhythm | What | Input | Output |
|---|---|---|---|
| **ODEC** (monthly; cadence `<to confirm>`, some decks show the strategy call as quarterly) | *Why* we prioritize: strategy and Smart Factory tools | Project/process issues and feedback; scaling potentials; new use-case sprints and machines connected | Central strategy updates; roadmaps, rollouts, workshops; priorities and deadlines |
| **COP** (monthly) | *How* we do it: technical implementation of machine integration, data models, use cases | Technical issues and feedback; connector updates; new use-case ideas | Data-model/connector updates; rollout guidance; technical Cyber Security aspects |
| **Retro** (at least monthly) | What did we learn → **one** change | Incidents, metrics, ODEC/COP feedback | 1 decided adjustment |
| Use Case Definition / Integration Workshops | Define and integrate with plant teams | Plant demand, process diagnostics | Prioritized use cases; integration plan |

**Escalation window: one round.** An item unresolved at one ODEC or COP cycle escalates
into the next — both rounds are monthly, so "escalate" means it carries forward with that
label, not that it waits past the next occurrence of its own round.

Preparing and following up a round is the most rewarding agent task here, because each has
a named input and a named output. Prepare against the input column; follow up against the
output column.

The retro is **mandatory, not optional**, and its output is exactly one decided
adjustment. A retro that produces a list has not produced a decision.

## Procedure

1. Refetch each figure from its authoritative source; note the read date.
2. Compare against target-to-date, not the annual target — a month at 11 against a 12
   target is red even in a good year.
3. Flag every metric past its intervention threshold, with the lane owner named.
4. Assemble the round input; after the round, record the output and the one retro change.
5. Where a source does not exist, say **⟨to collect⟩**. An honest gap does not block the
   field.

## Output — the protocol

Fill [`assets/scorecard-update-protocol.md`](assets/scorecard-update-protocol.md) once per
cycle. It takes `od-handover-and-adoption`'s adoption/utilization findings and
`od-portfolio-and-savings-analysis`'s savings roll-up as its two named inputs, refreshes
every metric with a read date, and produces the round-ready regional breakout and headline
— the document that is actually handed to ODEC/COP, not a summary reconstructed from memory
afterward.

## Do not

- Do not publish a figure without its read date and source.
- Do not reconcile two reports by picking the more favourable one.
- Do not report the annual target as though it were the position today.
- Do not fill in `⟨to confirm⟩` targets with plausible numbers.
