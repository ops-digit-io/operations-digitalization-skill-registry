---
name: od-information-integration-service
description: >-
  Run the Information Integration Service lane — equipment assessment and integration
  roadmap per plant, integration investment planning, machine and equipment connection
  to the IIoT Edge, process-related signal standardization and data pipelines into the
  the data platform, interface and software integration consulting, acceptance testing, Manufacturing
  Software Suite rollout preparation, and keeping the Equipment Integration report and
  the readiness matrix current. Use when a machine needs connecting, signals need
  standardizing, a data model needs harmonizing, or someone asks why a use case has no
  data. Owner is the IIoT Interface & Automation Engineer (IIAE).
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-information-integration-service
  tier: lane
  lane: information-integration-service
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  capacity: 3 IIAE roles
  authority_level: read-only on production/edge; draft on roadmaps and reports; recommend on sequencing
  escalation: OD lead (Thomas Zipf) via COP
  status: stable
  sources_read: 2026-10-23
  requires: [od-context]
  composes: [od-requirements-breakdown, od-equipment-integration, od-signal-standardization, od-acceptance-test, od-scorecard-reporting]
  derived_from:
    - ops-knowledge-graph/.../20-lanes/information-integration-service/{playbook,skills,tasks,metrics,agent-brief}.md
    - ops-knowledge-graph/_knowledge/10-Department/Machine integration.md
    - this registry, cross-checked 2026-10-23 against the current state of every skill this lane composes into (each was a stub on 2026-08-25; all five are now documented or deep) — see references/lane-handoffs.md
  okf:
    type: Agent Skill
    title: Information Integration Service
    tags: [information-integration-service, lane]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Information Integration Service

Read `od-context` first.

## The reference is the substance

| File | Use it for |
|---|---|
| [`references/lane-handoffs.md`](references/lane-handoffs.md) | Each happy-path step matched to the real, current asset the composed skill now produces — confirmed 2026-10-23, not just named |

**Trigger.** An equipment-integration or data-model-harmonization need per the roadmap.
**Definition of done.** Machine or equipment integrated, signals standardized, data
landing on the data platform. **Customer.** Plant ME / plant IT. **Lead time:** ⟨to confirm⟩.

This lane gates a large part of the portfolio: a dashboard cannot show a cycle time
nobody is reading off the line.

## Happy path

| # | Step | Who | Control point |
|---|---|---|---|
| 1 | Equipment assessment and integration roadmap per plant | IIAE + Plant ME/IT | Equipment inventory and roadmap agreed — requirement via `od-requirements-breakdown` |
| 2 | Integration investment planning | IIAE + OD lead | Investment approved |
| 3 | Machine/equipment integration planning and execution (data acquisition) | IIAE | Machine connected to IIoT Edge |
| 4 | Process-related signal standardization; offload into the data platform | both | Signals standardized; data on the data platform |
| 5 | Interface and software integration consulting + acceptance testing | IIAE | Acceptance test passed |
| 6 | Prepare Manufacturing Software Suite rollout; equipment-integration training | IIAE | Rollout-ready; plant trained |
| 7 | Update the Equipment Integration report and readiness matrix | both | Scorecard updated |

Step 1 → `od-equipment-integration` (assessment route). Step 4 → `od-signal-standardization`.
Step 5 → `od-acceptance-test`. Step 7 → `od-scorecard-reporting`.

## The estate this lane works on

1,715 machines and PLCs, each recorded against a plant with vendor, PLC model, part
number, network protocol and criticality: **821 `INTEGRATED`**, **395 `NOT INTEGRATED`**,
**48 `INTEGRATION ONGOING`**. `NOT INTEGRATED` is not a backlog of failures — a large
part of it is machines nobody has needed data from yet. The field records the state, not
a judgement.

26 connectors, one per protocol or vendor family — 24 DATATRONiQ, 2 Softing Industrial.
Three integration concepts sit above them: a central OPC-UA server, container-based machine
integration, and an IIoT edge computing platform.

Those three are the three ways a PLC reaches the **IIoT Edge Platform**, which is the
terminus in all of them: via an **edge device** running the connector (Concept 3, 20 plants),
via a **connector with no device** at the machine (Concept 2, 1 plant, no written route), or
via the **Softing dataFEED aggregation server** bridged back over OPC UA with
`DTQ-OPCUA-Connector` (Concept 1, 11 plants). The aggregation shape needs both pieces. For a
specific machine, `od-equipment-integration` (guidance route) carries the routing, the
per-driver configuration patterns and the fallbacks when a path blocks.

## Error paths

- **Machine cannot connect** (legacy or protocol) → log the barrier in the landscape
  module; escalate into the roadmap.
- **Cyber Security sign-off missing** for an external connection → hold at the wait
  state. Never connect anyway.
- **Operations concept missing for the target system** (MSB / the data platform) → escalate to strategy
  as a tool-rollout decision.

## Wait states

Awaiting integration investment approval · awaiting Cyber Security / OT sign-off ·
awaiting a decision on shared tooling, licensing or signal standards — Plant ME / Plant IT.

## Recurring tasks

| Task | Trigger | Template |
|---|---|---|
| Equipment assessment & roadmap | New plant / integration wave | `od-equipment-integration`'s `assets/assessment-protocol.md` (Route A) |
| Integration investment planning | Roadmap agreed | ⟨investment plan template — to confirm⟩ |
| Machine integration execution | Investment approved | `od-equipment-integration`'s `assets/guidance-protocol.md` (Route B) |
| Signal standardization | Machine connected | Signal standard spec |
| Acceptance test | Integration complete | Acceptance test protocol |
| Equipment Integration report update | Monthly / ODEC | `OD-Report-Equipment_Integration` |
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
| Integrated equipment (year) | `OD-Report-Equipment_Integration` | 331 (year); 666 total | IS below target-to-date — 338 vs 331 on 2026-08-10, on/above |
| Integrated equipment per month | same · monthly bar | 25 / month (overshoot 30) | month below 25 |
| System / capability readiness | Scorecard · System Integration and Availability | Available at strategic plants | red at a strategic plant |
| Acceptance / rework rate | Not captured in any system today | No target set — nothing to measure against yet | rework rate rising |

## Handover / rework rule

Integrated and standardized data goes to the Use Case Support and Analytical lanes.
Equipment returns for rework if acceptance testing fails, or if the readiness dimension
does not turn "Available".
