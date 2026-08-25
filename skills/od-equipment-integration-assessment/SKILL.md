---
name: od-equipment-integration-assessment
description: >-
  Assess a plant's equipment and build its integration roadmap — inventory the machines
  and PLCs with vendor, protocol and criticality, decide per machine which of the three
  integration concepts and which of the 26 connectors applies, size the investment, and
  sequence the wave. Use when a new plant or integration wave starts, when a specific
  machine needs connecting and the route is unclear, when a use case is blocked for want
  of data from a machine, or when the integrated-equipment target needs a credible plan
  behind it.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-equipment-integration-assessment
  tier: practice
  lane: information-integration-service
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  authority_level: draft on assessments and roadmaps; recommend on sequencing; never connect
  status: stable
  sources_read: 2026-08-10
  requires: [od-context]
  composes: [od-signal-standardization, od-acceptance-test, od-decision-routing]
  derived_from:
    - ops-knowledge-graph/_knowledge/10-Department/Machine integration.md
    - ops-knowledge-graph/_knowledge/20-Done/Equipment integration guide.md
    - ops-knowledge-graph/.../20-lanes/information-integration-service/{playbook,tasks}.md
  okf:
    type: Agent Skill
    title: Equipment integration assessment and roadmap
    tags: [information-integration-service, practice]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Equipment integration assessment and roadmap

Read `od-context` first.

Most use cases need data a machine is already producing and nobody is reading. Getting at
it is its own discipline with its own rollout, its own status vocabulary and its own
blockers — and it gates a large part of the portfolio.

## The estate

**1,715 machines and PLCs** are tracked, each against a plant, with vendor, PLC model,
part number, network protocol and criticality recorded.

| Integration status | Machines |
|---|--:|
| `INTEGRATED` | 821 |
| `NOT INTEGRATED` | 395 |
| `INTEGRATION ONGOING` | 48 |

**`NOT INTEGRATED` is not a backlog of failures.** A large part of it is machines nobody
has needed data from yet. The field records the state, not a judgement — do not report it
as a gap without first checking whether any use case wants that data.

## The two things that get chosen

**Connector** — 26 of them, one per protocol or vendor family: S7, TIA, Beckhoff, Modbus,
OPC-UA, EtherCAT, Allen-Bradley/Rockwell, B&R, Bachmann, Omron FINS, Sinumerik, Simotion,
RS232, and vendor-specific ones for Engel, Piovan, Keyence, Zwick and Optris. A connector
only ever reaches a machine. It is not a system a plant uses, which is why it is kept
distinct from a tool.

These 26 are the **edge** connector set. The Central Aggregation Server has its own driver
list, and it is not the same one — notably it has **no Beckhoff / ADS driver**. Do not
assume a machine routable on one platform is routable on the other; check per machine in
`od-machine-integration-guidance`.

**Integration concept** — three sit above the connectors and are recorded as tools in their
own right: a **central OPC-UA server**, **container-based machine integration**, and the
**IIoT edge computing platform**. Which one applies depends on the machine.

The Equipment integration guide routes to two of them, under its own names: the
**IIoT Edge Platform** and the **Central Aggregation Server** (running Softing dataFEED OPC
Suite; legacy Kepware) — the latter being the central OPC-UA server concept seen from the
route side. Container-based integration is recorded as a concept with **no written route**.

**They are not separate destinations.** The three concepts are the three ways a PLC reaches
the **IIoT Edge Platform**, which is the terminus in all of them:

| Concept | Ingress shape | Plants |
|---|---|--:|
| Concept 3 — IIoT Edge Computing Platform | PLC → **edge device** with connector → platform | 20 |
| Concept 2 — container-based Machine Integration | PLC → **connector** → platform (no device at the machine) | 1 |
| Concept 1 — Central OPC-UA Server | PLC → **aggregation server** → platform, over OPC UA via `DTQ-OPCUA-Connector` | 11 |

The aggregation shape therefore needs **both** pieces — a Softing server with no edge
platform behind it delivers nothing. Eight plants carry both the edge and the aggregation
concept, so this is a per-machine decision rather than a plant policy. Per-machine routing,
the configuration patterns and the fallbacks are in `od-machine-integration-guidance`.

That decision was turned into a guided questionnaire — the **Equipment integration
guide**, a Streamlit app over a rules file (`_apps/machine-integration-guidance-app`,
tree in `rules.json`). Use it rather than re-deriving the decision: the rules are data, so
the tree changes without touching the app, and it asks the questions in the order they
actually arise on the floor.

## Procedure

1. **Inventory** the plant's machines against the Machine List — vendor, PLC model, part
   number, network protocol, criticality, current integration status.
2. **Filter by demand.** Which machines does an accepted or planned use case actually need
   data from? Integration without a use case behind it is capacity spent on `NOT
   INTEGRATED` rows that nobody was waiting for.
3. **Route each machine** through the equipment integration guide → integration concept +
   connector. Record barriers where no route exists (legacy, unsupported protocol).
4. **Sequence the wave** against the plant roadmap and the readiness matrix — strategic
   plants first, then where a capability is red.
5. **Size the investment** and take it through integration investment planning; the
   go-ahead is `execute-with-approval`, Tandem with Plant ME / Plant IT.
6. **Confirm the Cyber Security / OT gate** for anything involving an external
   connection, before it is scheduled — not after.
7. Hand to execution, then `od-signal-standardization`, then `od-acceptance-test`.

Reference standard for the requirement spec: **PRS — Requirement Specification for
Machines & Equipment**, Doc ID 215534 (OESL Engineering Standards library).

## Error paths

- **No route exists for a machine** → log the barrier in the landscape module and escalate
  it into the roadmap. Do not leave it as a silent omission in the wave.
- **Cyber Security sign-off missing** → the machine waits. There is no expedited path.
- **Operations concept missing for the target system** (MSB / the data platform) → escalate to strategy
  as a tool-rollout decision; the machine can be connected and still have nowhere to send
  data.

## Definition of done

Equipment inventory and integration roadmap agreed with Plant ME / Plant IT; each machine
in scope carries a concept, a connector and a sequence position; barriers are logged;
the investment is planned and the Cyber Security gate identified.

## Targets to plan against

**331 integrated machines this year (666 total), 25 per month** with an overshoot target
of 30. On 2026-08-10 the actual stood at **338 against 331 — on or above target**. This
lane is currently the one that is ahead; do not plan as though it were the constraint.

## Do not

- Do not record a machine as integrated before its acceptance test passes.
- Do not claim a readiness dimension is "Available" without evidence.
- Do not change signal or data-model standards to make a machine easier — that is a
  Consultation decision ⟨counterpart to confirm⟩, not a per-machine convenience.
