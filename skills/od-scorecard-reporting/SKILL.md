---
name: od-scorecard-reporting
description: >-
  Fetch, assess and report OD's numbers — the Digitalization Scorecard and the Use Case
  and Equipment Integration Power BI reports — against their targets and intervention
  thresholds, and prepare and follow up the ODEC and COP rounds. Covers which report is
  authoritative for which figure, the current targets and actuals with their read date,
  when a number crosses into "intervene", and the recipient-feedback loop per lane. Use
  when monthly or ODEC reporting is due, when someone asks how OD is tracking, when a
  metric needs a source, or when a round needs preparing or following up.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-scorecard-reporting
  tier: practice
  lane: all
  owner_role: OD lead (Thomas Zipf); DBVE for use-case metrics, IIAE for equipment metrics
  authority_level: read-only on sources; draft on reports
  status: stable
  sources_read: 2026-08-10
  valid_until: 2026-11-10
  requires: [od-context]
  derived_from:
    - ops-knowledge-graph/.../00-core/07-metrics.md
    - ops-knowledge-graph/.../00-core/06-operating-rhythm.md
    - ops-knowledge-graph/.../20-lanes/*/metrics.md
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

## Sources, and which one wins

| Source | Authoritative for |
|---|---|
| **Digitalization Scorecard** (`MPEE-OD-Plant_Scorecard`) | Targets vs. actuals ("Actual Year" figures), readiness RAG matrix, use-case utilization |
| `OD-Report-Use_Case_Integration` | Use-case counts by month, region and process; asset mix |
| `OD-Report-Equipment_Integration` | Equipment counts by month, region and process |

Where they disagree, **the Scorecard "Actual Year" figures are authoritative.** A known
example: the Use-Case gauge showed 88 of ~140 under the 2026 filter while the Scorecard
showed IS 101 of 153 for the year. Report the Scorecard figure and say which filter the
other came from.

## The metrics

Values read **2026-08-10**. They **will drift** — refetch from Power BI before acting on
any of them, and state the read date with any figure you publish.

| Metric | Formula | Source | Target | Intervene from | Cadence |
|---|---|---|---|---|---|
| Integrated Use Cases (year) | Count, current year | Scorecard · Digital Use Cases · IS | **153** (year); 279 total | IS below target-to-date — **101 vs 153** | monthly |
| Integrated Use Cases per month | Count in month | Use_Case_Integration · monthly bar | **12/month** (overshoot 14) | month below 12 (red bar) | monthly |
| Integrated Equipment (year) | Count, current year | Scorecard · Equipment Integration · IS | **331** (year); 666 total | IS below target-to-date — **338 vs 331, on/above** | monthly |
| Integrated Equipment per month | Machines in month | Equipment_Integration · monthly bar | **25/month** (overshoot 30) | month below 25 (red bar) | monthly |
| System / capability readiness | RAG per dimension × location | Scorecard · System Integration and Availability | Available at strategic plants | red at a strategic plant | quarterly |
| Use-case utilization rate | Integrated use cases by utilization rate | Scorecard · Digital Use Case Utilization | ⟨to confirm⟩ | low-utilization share rising | monthly |
| Use-case asset mix | Share by asset | Use_Case_Integration · asset pie | ⟨to confirm⟩ | portfolio indicator | quarterly |
| Value delivery cycle | Demand → live use case | ⟨system — to confirm⟩ | ⟨to confirm⟩ | ⟨threshold — to confirm⟩ | — |

**The honest headline today:** equipment integration is on or above target; use-case
integration is behind. Report both. A summary that leads with the equipment number alone
is the version that gets found out.

## Recipient feedback — the loop acceptance does not cover

| Lane | Recipient | Feedback metric | Source |
|---|---|---|---|
| Use Case Support | Plant ME / operations | Use case adopted into the daily process (utilization rate) | Scorecard · Use Case Utilization |
| Information Integration | Plant IT / use-case teams | Integrated equipment vs. target; readiness turning green | Equipment Integration report; readiness matrix |

## The rounds

| Rhythm | What | Input | Output |
|---|---|---|---|
| **ODEC** (monthly) | *Why* we prioritize: strategy and Smart Factory tools | Project/process issues and feedback; scaling potentials; new use-case sprints and machines connected | Central strategy updates; roadmaps, rollouts, workshops; priorities and deadlines |
| **COP** (monthly) | *How* we do it: technical implementation of machine integration, data models, use cases | Technical issues and feedback; connector updates; new use-case ideas | Data-model/connector updates; rollout guidance; technical Cyber Security aspects |
| **Retro** (at least monthly) | What did we learn → **one** change | Incidents, metrics, ODEC/COP feedback | 1 decided adjustment |
| Use Case Definition / Integration Workshops | Define and integrate with plant teams | Plant demand, process diagnostics | Prioritized use cases; integration plan |

⟨Escalation windows for ODEC and COP are not defined — to confirm.⟩

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

## Do not

- Do not publish a figure without its read date and source.
- Do not reconcile two reports by picking the more favourable one.
- Do not report the annual target as though it were the position today.
- Do not fill in `⟨to confirm⟩` targets with plausible numbers.
