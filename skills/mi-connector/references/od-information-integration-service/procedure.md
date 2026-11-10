---
type: Skill Reference
title: Procedure
description: Formerly the skill od-information-integration-service, absorbed into mi-connector on 2026-11-10 to remove duplication against the department context. Run the Information Integration Service lane — equipment assessment and integration roadmap per plant, integration investment planning, machine and equipment connection to the IIoT Edge, process-related signal standardization and data pipelines into the the data platform, interface and software integration consulting, acceptance testing, Manufacturing Software Suite rollout preparation, and keeping the Equipment Integration report and the readiness matrix current. Use when a machine needs connecting, signals need standardizing, a data model needs harmonizing, or someone asks why a use case has
resource: ../../SKILL.md
status: stable
owner: human:jakob.gabriel
tags:
- information-integration-service
- lane
- absorbed
derived_from:
- ops-knowledge-graph/.../20-lanes/information-integration-service/{playbook,skills,tasks,metrics,agent-brief}.md
- ops-knowledge-graph/_knowledge/10-Department/Machine integration.md
- this registry, cross-checked 2026-10-23 against the current state of every skill this lane composes into (each was a stub on 2026-08-25; all five are now documented or deep) — see references/lane-handoffs.md
- Work vault (Work-OpsDigit-Knowledge), Graph/Tools (incl. archive-evidence blocks), Graph/Machines, Graph/Plants and Graph/Connectors, counted and read 2026-11-05
- Work vault (Work-OpsDigit-Knowledge), Slide Index (master note, slide-decks.jsonl, slide-manifest.jsonl; deck Operation Concept IIoT and Edge Computing) and ODEC Facts staging notes, AI-extracted and unverified, read 2026-11-05
- Department notes Systems of record, Machine integration, and 20-Done MSB rollout projects (ops-knowledge-graph _knowledge), read 2026-11-05
generated:
  by: claude-code/1
  at: 2026-08-25 00:00:00+00:00
---
# Information Integration Service

> **Absorbed.** This was the skill `od-information-integration-service`. It now runs as a mode of [`mi-connector`](../../SKILL.md) (merged 2026-11-10, see `log.md`). Its authority stays as it was: read-only on production/edge; draft on roadmaps and reports; recommend on sequencing.

Read `dept-os` first.

## The reference is the substance

| File | Use it for |
|---|---|
| [`references/lane-handoffs.md`](references/lane-handoffs.md) | Each happy-path step matched to the real asset the composed skill produces, not just named |
| [`references/tool-fact-sheets.md`](references/tool-fact-sheets.md) | How to read the tool records for each shop-floor tool: what to look up (rollout, architecture, cost and hardware, status, open blockers), where, and the prerequisites per tool |
| [`references/roles-and-support-model.md`](references/roles-and-support-model.md) | The roles around the IIoT edge platform (local key user, business-area key user, governance board, central key user, divisional engineering, divisional and local IT, platform provider) and the incident, change and security-incident flows |
| [`references/task-chain-and-tool-use.md`](references/task-chain-and-tool-use.md) | The lane's recurring tasks as a trigger chain (starts when, needs, tool, leaves behind, feeds), why each tool has its access, metric hooks, signal-standardization rule and record-reading traps |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | The lane's operating rhythm in the AI-driven chain: wave cadence and plant status, the community-call pack, plant tiering, integration workshop, recurring blockers, handoffs, agent notes |
| [`references/finding-decks.md`](references/finding-decks.md) | How to search the Slide Index and a topic-to-deck map for the lane |
| [`assets/plant-status-input.md`](assets/plant-status-input.md) | One-page plant input for a status request on equipment integration |

**Trigger.** An equipment-integration or data-model-harmonization need per the roadmap.
**Definition of done.** Machine or equipment integrated, signals standardized, data
landing on the data platform. **Customer.** Plant ME / plant IT. **Lead time:** ⟨to confirm⟩.

This lane gates a large part of the portfolio: a dashboard cannot show a cycle time
nobody is reading off the line.

## Happy path

| # | Step | Who | Control point |
|---|---|---|---|
| 1 | Equipment assessment and integration roadmap per plant | IIAE + Plant ME/IT | Equipment inventory and roadmap agreed — requirement via `funnel-requirements` |
| 2 | Integration investment planning | IIAE + OD lead | Investment approved |
| 3 | Machine/equipment integration planning and execution (data acquisition) | IIAE | Machine connected to IIoT Edge |
| 4 | Process-related signal standardization; offload into the data platform | both | Signals standardized; data on the data platform |
| 5 | Interface and software integration consulting + acceptance testing | IIAE | Acceptance test passed |
| 6 | Prepare Manufacturing Software Suite rollout; equipment-integration training | IIAE | Rollout-ready; plant trained |
| 7 | Update the Equipment Integration report and readiness matrix | both | Scorecard updated |

Step 1 → `mi-connector` (assessment route). Step 4 → `od-signal-standardization`.
Step 5 → `od-acceptance-test`. Step 7 → `od-scorecard-reporting`.

## The estate this lane works on

Every machine and PLC is recorded in the Machine List against a plant, with vendor, PLC
model, part number, network protocol and criticality, and an integration status:
`INTEGRATED`, `NOT INTEGRATED`, `INTEGRATION ONGOING`, or blank. `NOT INTEGRATED` is not a
backlog of failures — part of it is machines nobody has needed data from yet. A **blank status
is not "not integrated"**: it means nobody recorded it. The field records the state, not a
judgement. Count each status live on the current Machine List export before quoting a figure,
and name the export date.

Connectors exist one per protocol or vendor family (supplier families: DATATRONiQ and Softing
Industrial; list them from `Graph/Connectors`). Three integration concepts sit above them: a
central OPC-UA server, container-based machine integration, and an IIoT edge computing platform.

Those three are the three ways a PLC reaches the **IIoT Edge Platform**, which is the
terminus in all of them: via an **edge device** running the connector (Concept 3), via a
**connector with no device** at the machine (Concept 2, no written route), or via the
**Softing dataFEED aggregation server** bridged back over OPC UA with `DTQ-OPCUA-Connector`
(Concept 1). The aggregation shape needs both pieces. For a specific machine,
`mi-connector` (guidance route) carries the routing, the per-driver configuration
patterns and the fallbacks when a path blocks.

## Reading the records: traps

How many plants run which concept, and how many machines sit in each status, live in the Tool
Overview and the Machine List; the per-plant reading guide is `mi-connector`'s
[`plant-integration-status.md`](../plant-integration-status.md).
Patterns to expect:

- The **Tool Overview (plants with a concept)** and the **Machine List (plants with machines
  routed through it)** are two measures and rarely agree. Quote the one you used and its source.
- Some plants have no machine rows at all, and some have no status on any row: a gap in the
  record, not a finding about the plant.
- The scorecard's integrated-equipment figure and a count of machines with an integration date
  in the current year are different measures. ⟨Reconciliation. Who could supply it: the owner
  of `OD-Report-Equipment_Integration`.⟩

## Error paths

- **Machine cannot connect** (legacy or protocol) → log the barrier in the landscape
  module; escalate into the roadmap.
- **Cyber Security sign-off missing** for an external connection → hold at the wait
  state. Never connect anyway.
- **Operations concept missing for the target system** (MSB / the data platform) → escalate to strategy
  as a tool-rollout decision; do not roll the tool out on demand until a named operations owner and
  support level exist (`references/process-chain-practice.md`).

## Wait states

Awaiting integration investment approval · awaiting Cyber Security / OT sign-off ·
awaiting a decision on shared tooling, licensing or signal standards — Plant ME / Plant IT.

## Recurring tasks

| Task | Trigger | Template |
|---|---|---|
| Equipment assessment & roadmap | New plant / integration wave | `mi-connector`'s `assets/assessment-protocol.md` (Route A) |
| Integration investment planning | Roadmap agreed | ⟨investment plan template — to confirm⟩ |
| Machine integration execution | Investment approved | `mi-connector`'s `assets/guidance-protocol.md` (Route B) |
| Signal standardization | Machine connected | Signal standard spec |
| Acceptance test | Integration complete | Acceptance test protocol |
| Equipment Integration report update | On request or on the department's own schedule | `OD-Report-Equipment_Integration` |
| Readiness matrix update | Capability change | Scorecard readiness matrix |

## Systems and access

IIoT Edge Platform (deploy / configure) · data pipelines (write) · data platform —
Databricks → Azure Storage Account, Parquet (write via the offload) · MSB (configure ⟨scope to confirm⟩) · machine connectors and signal standards
(configure) · Equipment Integration report (read / update) · Scorecard readiness matrix
(read / update) · Cyber Security / OT interface (consult).

Reference standard: **Requirement Specification for Machines & Equipment (PRS)**,
Doc ID 215534, in the OESL Engineering Standards library.

## Autonomy

**May** — read the equipment inventory, the data platform and the Scorecard; draft equipment assessments
and integration roadmaps; update the Equipment Integration report and readiness matrix;
prepare acceptance-test protocols.
**May not** — connect machines or write to production systems; approve integration
investment; change signal or data-model standards; approve external connections.
**Guardrails** — never connect externally without Cyber Security / OT sign-off; never claim
a readiness dimension "Available" without
evidence.

## Metrics for this lane

| Metric | Source | Target | Intervene from |
|---|---|---|---|
| Integrated equipment (year) | `OD-Report-Equipment_Integration` | the year target in the report (look up: report owner) | actual below target-to-date |
| Integrated equipment per month | same · monthly bar | the monthly target in the report (look up: report owner) | month below the monthly target |
| System / capability readiness | Scorecard · System Integration and Availability | Available at strategic plants | red at a strategic plant |
| Acceptance / rework rate | Not captured in any system today | No target set — nothing to measure against yet | rework rate rising |

## Handover / rework rule

Integrated and standardized data goes to the Use Case Support and Analytical lanes.
Equipment returns for rework if acceptance testing fails, or if the readiness dimension
does not turn "Available".
