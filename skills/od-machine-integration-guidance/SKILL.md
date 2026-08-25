---
name: od-machine-integration-guidance
description: >-
  Decide how to connect a specific machine to the OESL Smart Factory architecture and say
  what has to be true before it can happen — pick between the IIoT Edge Computing Platform
  and the Central OPC-UA Aggregation Server, map the PLC vendor and protocol onto one of
  the 26 connectors, and work the preparation checklist (budget, infrastructure, PLC
  program, tag export, Machine List, Machine CV, edge-device list, Cyber Security). Use
  when someone asks how to connect a machine or PLC, which integration route or connector
  applies to a Siemens / Rockwell / Beckhoff / B&R / Omron / Mitsubishi / Modbus / OPC-UA
  device, why a machine cannot be connected, what an integration wave needs, or what to
  specify when ordering a new machine.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-machine-integration-guidance
  tier: technical
  lane: information-integration-service
  scope: od
  origin: derived
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  authority_level: recommend a route; never connect, never approve an external connection
  status: stable
  last_verified: 2026-08-25
  requires: [od-context]
  composes: [od-equipment-integration-assessment, od-signal-standardization, od-acceptance-test, od-node-red-flow-builder]
  derived_from:
    - ops-knowledge-graph/_knowledge/_apps/machine-integration-guidance-app/rules.json
    - ops-knowledge-graph/_knowledge/_apps/machine-integration-guidance-app/rules-next.json
    - ops-knowledge-graph/_knowledge/90-Sources/generated/kg_nodes.csv (1,715 Machine + 26 Connector nodes)
    - ops-knowledge-graph/_knowledge/10-Department/Machine integration.md
    - ops-knowledge-graph/_knowledge/20-Done/Equipment integration guide.md
---

# Machine integration guidance

Read `od-context` first. This skill answers one machine's question. For a whole plant or
wave, start at `od-equipment-integration-assessment` and come back here per machine.

The authoritative interactive form of this decision is the **Equipment integration guide**
(`_apps/machine-integration-guidance-app`, a Streamlit app whose tree lives in
`rules.json`). This skill is the same tree in readable form plus what the Machine List
says about the estate it is applied to. When the two disagree, `rules.json` wins — it is
the maintained artefact.

## Step 1 — Which precondition applies

The first question is not about the PLC. It is about what is already installed:

| Answer | Goes to |
|---|---|
| **IIoT Edge Platform** | PLC type → an edge-platform route |
| **IIoT Edge Platform — Edge Device Hardware Installation** | Large / Medium / Small edge device install guidance |
| **Central Aggregation Server** (Softing DataFEED; legacy: Kepware) | PLC type → an aggregation-server route |
| **No standard systems installed** | Rollout preconditions first — there is nothing to connect to yet |
| **Ordering a new machine, need a standard document** | The requirement-spec route (PRS), not an integration route |

The last one matters more than its position suggests: **specifying connectivity at
purchase is the cheapest integration there is.** A machine bought without the PLC program
clause is a machine that may never be connectable — see the hard gate below.

## Step 2 — PLC type → route

| PLC family | Sub-choice | IIoT Edge | Central OPC-UA Aggregation Server |
|---|---|---|---|
| **Siemens** | S7 | yes | yes |
| | S7 Net / low frequency | yes | — (edge only) |
| | TIA | yes | yes |
| **Siemens NCU** | Sinumerik 840D / 840 UDP | yes | yes *(in `rules-next`)* |
| | Sinuvars | yes | yes *(in `rules-next`)* |
| **Beckhoff** | — | yes | yes |
| **B&R** | INA2000 | — | yes |
| **Omron** | NJ / CJ | yes | yes *(in `rules-next`)* |
| **Rockwell / Allen Bradley** | CLX | yes | yes |
| | SLC / PLC-5 | yes | yes |
| **OPC-UA Server** | — | yes | ⟨route documented as TODO in `rules.json`⟩ |
| **Modbus** | — | ⟨TODO in `rules.json`⟩ | yes |
| **Mitsubishi** | Melsec-Q | — | yes |
| **Other PLC** | — | edge only, by exception | — |

Two entries in `rules.json` are explicitly `TODO` (Beckhoff on edge, Modbus on edge,
OPC-UA on the aggregation server). Say so rather than inventing the procedure — an unwritten
route is a question for the IIAE, not a gap to fill.

The full tree, including the edge-device hardware branch and what `rules-next.json` adds,
is in [`references/decision-tree.md`](references/decision-tree.md).

## Step 3 — Which connector

26 connectors exist, one per protocol or vendor family — 24 from DATATRONiQ, 2 from
Softing Industrial. A connector only ever reaches a machine; it is **not** a system a
plant uses, which is why it is kept distinct from a tool. Full table with input protocols:
[`references/connectors.md`](references/connectors.md).

## Step 4 — The preparation checklist

Every edge-platform route in `rules.json` carries the same five-block checklist. The
blocks are not advisory; they are what an integration slips on.

**Budget planning** — edge device plus OT hardware (switches, cabling); IT infrastructure
(software subscriptions, cabling edge → OT switch). Use the budget planning template.

**Infrastructure preconditions** — IT cabling present; power supply for the edge device
confirmed against its datasheet.

**PLC / machine preparation** — this is where integrations die:

1. Machine details (interfaces, PLC types, HMIs and other endpoints) recorded in the
   **Machine List**.
2. A machine-specific **integration plan** — network diagram with endpoints, protocols,
   connections.
3. **The PLC program**, in an appropriate format (the entire program including the `.S7P`
   for Siemens). If it is not available, request it from the machine supplier.
   > **Hard gate, quoted from the guide: without the PLC program the PLC cannot be
   > connected.** Not "harder", not "later" — not at all. Raise this at the first
   > conversation, not at the integration date.
4. The capability to **adjust the PLC program** — implement the function block, adjust the
   hardware configuration.
5. Upload the PLC program to the **Machine CV**.
6. **Export the tags** from the PLC program using the available export tools.
7. Provide the **PLC IP address and connection details**.
8. Add the edge device to the **Edge Device List**.

**IT tasks** — provide the edge-device IP; configure it on ETH1.

**Machine tasks** — connect PLC to edge device; mount the edge device in the machine
cabinet with 24 V supply.

The OPC-UA aggregation route differs: it is **brownfield only**, needs the machines already
on the Softing DataFEED OPC Suite, needs the server endpoint details (IP, credentials,
certificates) and a known server structure, and ends by informing the MPEE Operations
Digitalization team.

## Step 5 — Record it, then hand on

The **Machine List is the record**, not a form to fill afterwards. Update integration
status (`INTEGRATED` / `NOT INTEGRATED` / `INTEGRATION ONGOING`) only after
`od-acceptance-test` passes. Then the signals go to `od-signal-standardization`, and the
data-path build to `od-node-red-flow-builder`.

## What the estate actually looks like

1,715 machines. Full breakdown: [`references/estate.md`](references/estate.md).

| | |
|---|--:|
| `INTEGRATED` | 821 |
| `NOT INTEGRATED` | 395 |
| `INTEGRATION ONGOING` | 48 |
| status not recorded | 451 |

**Siemens is 1,032 of 1,715 machines** — 60 % of the estate, dominated by SIMATIC S7-300
(324), S7-1200 (264) and S7-1500 (171). Rockwell/Allen-Bradley is the second family at 220.
Route chosen where recorded: **IIoT Edge 672 · Central OPC-UA Aggregation Server 384 ·
evaluation ongoing 117**, with 542 machines carrying no method yet.

**`NOT INTEGRATED` is not a backlog of failures.** A large part of it is machines nobody
has needed data from yet. Check whether a use case wants the data before reporting it as a
gap. Equally, `production_criticality`, `cyber_security_status` and `machine_blockers` are
**empty on all 1,715 rows** — those fields exist and have never been populated. Do not
read an empty criticality as "not critical".

## Recorded blockers, in the estate's own words

125 machines carry an integration blocker. The recurring ones:

| Blocker | Machines |
|---|--:|
| Data model standardization (CT Base) | 23 |
| Firmware patching required for cyber security | 13 |
| TIA V16 → V17 upgrade needed | 12 |
| Cyber-security vulnerability, patch before integration | 5 |
| Robot signals possibly available via the related PLC — unconfirmed | 5 |
| Camera hardware and integration | 2 |
| No PLC on an IM151-1 standard — PLC type unknown | 2 |

Three of the top four are **not** connectivity problems: they are a data-model decision, a
firmware policy and a toolchain upgrade. That matches the department's wider finding —
what stalls is almost never the engineering.

## Guardrails

- **Never connect a machine and never approve an external connection.** Both are human,
  `execute-with-approval`, Tandem with Plant ME / Plant IT, and external connections need
  Cyber Security / OT sign-off first. There is no expedited path.
- **Never change a signal or data-model standard** to make a machine easier — Consultation
  with ContiTech central, and interface compatibility is a standing constraint.
- **Never mark a machine `INTEGRATED`** before its acceptance test passes.
- **Never invent a route** for a branch `rules.json` marks TODO.
- **Never claim a readiness dimension "Available"** without evidence.

## What is coming

`rules-next.json` is the newer tree beside the live one — 35 questions against 25, 31
recommendations against 27. It adds routes for **camera systems** and **remote sensors** on
both platforms, completes Rockwell, Omron, Sinuvars and Sinumerik on the aggregation
server, and adds assessment questions the current tree does not ask: data acquisition, data
buffering, local dashboarding / HMI, rule-engine transformation, analytics use cases, PLC
hardware and software standardization, process complexity and maturity, strategic
priorities. It is **not** the live tree; treat it as the direction, and use `rules.json`
for an answer today.
