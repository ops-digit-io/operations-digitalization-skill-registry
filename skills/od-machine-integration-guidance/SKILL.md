---
name: od-machine-integration-guidance
description: >-
  Guide a machine integration end to end in the OESL Smart Factory architecture — route the
  machine to the IIoT Edge Computing Platform or the Softing dataFEED Central OPC-UA
  Aggregation Server, walk the detailed configuration pattern for that route (driver,
  protocol variant, addressing, read optimization, cyclic read, tag definition), clear the
  preparation gates, and take the right fallback when a path is blocked. Use when someone
  asks how to connect a machine or PLC, which route or connector applies to a Siemens /
  Rockwell / Beckhoff / B&R / Omron / Mitsubishi / Modbus / OPC-UA device, how to configure
  a data source in Softing dataFEED, why a machine cannot be connected, or what to specify
  when ordering a new machine.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-machine-integration-guidance
  tier: technical
  lane: information-integration-service
  scope: od
  origin: derived
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  authority_level: recommend a route and a configuration; never connect, never approve an external connection
  status: stable
  last_verified: 2026-08-25
  requires: [od-context]
  composes: [od-equipment-integration-assessment, od-signal-standardization, od-acceptance-test, od-node-red-flow-builder]
  derived_from:
    - ops-knowledge-graph/_knowledge/_apps/machine-integration-guidance-app/rules.json
    - ops-knowledge-graph/_knowledge/_apps/machine-integration-guidance-app/rules-next.json
    - OESL guideline "Machine Integration — Softing DataFeed — Siemens S7-300/400/1200/1500" (referenced by the guide)
    - OESL guideline "Machine Integration — Softing dataFEED — Beckhoff PLC Integration" (referenced by the guide)
    - ops-knowledge-graph/_knowledge/90-Sources/generated/kg_nodes.csv (1,715 Machine + 26 Connector nodes)
    - ops-knowledge-graph/_knowledge/10-Department/Machine integration.md
    - ops-knowledge-graph/_knowledge/20-Done/Equipment integration guide.md
---

# Machine integration guidance

Read `od-context` first. This skill guides **one machine**. For a whole plant or wave,
start at `od-equipment-integration-assessment` and come back here per machine.

The authoritative interactive form of this decision is the **Equipment integration guide**
(`_apps/machine-integration-guidance-app`, a Streamlit app whose tree lives in
`rules.json`). This skill is that tree made walkable, plus the configuration detail behind
each route. When the two disagree, `rules.json` wins — it is the maintained artefact.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/decision-paths.md`](references/decision-paths.md) | Routing: the four gates, PLC family → available routes, connector selection, and where a path dead-ends |
| [`references/softing-datafeed.md`](references/softing-datafeed.md) | The **Central Aggregation Server** pattern in configuration detail — per-driver procedures for Siemens S7/TIA, Beckhoff, Rockwell, Modbus and OPC-UA sources |
| [`references/iiot-edge-platform.md`](references/iiot-edge-platform.md) | The **IIoT Edge** pattern in detail — the six phases, the hardware sequence, device sizing, non-PLC endpoint classes |
| [`references/fallbacks.md`](references/fallbacks.md) | The eight ways an integration blocks, what to try before declaring each one blocked, and when to stop |

## How to use this skill

1. **Gate 0 — what is installed at this plant?** Not the PLC. The tree starts here because
   it decides which patterns are available at all. → `decision-paths.md`
2. **Ask the cheap question first: is the machine already on an OPC-UA server?** If yes,
   neither the PLC program nor cabinet work is needed. It is the largest single cost
   difference in the guide and the easiest to skip past.
3. **Gate 1 — route the PLC family** to edge, aggregation, or both. Neither platform is a
   vendor default; both carry Siemens and Rockwell at scale.
4. **Gate 2 — pick the connector** (edge) or the **data source driver** (aggregation).
5. **Walk the pattern** in `softing-datafeed.md` or `iiot-edge-platform.md`.
6. **Gate 3 — clear the preparation blocks** in order: budget → infrastructure → **PLC
   program** → tags → cyber security.
7. **Blocked?** → `fallbacks.md` before recording it as blocked.
8. **Gate 4 — record it**: Machine List, Machine CV (mandatory vs optional tags), Edge
   Device List, inform MPEE OD. Status moves to `INTEGRATED` only after
   `od-acceptance-test` passes.

## The two routes, in one table

| | **IIoT Edge Computing Platform** | **Central Aggregation Server** (Softing dataFEED OPC Suite) |
|---|---|---|
| Shape | Device per machine or cell, connector per protocol | One server, driver connections, one OPC-UA address space |
| Valid for | **Brownfield and greenfield** | Brownfield (OPC-UA data source: also greenfield) |
| Cabinet work | Mount, 24 V, shopfloor Ethernet, ETH1 | **None** |
| PLC program needed | Yes, for a PLC endpoint | Yes, for a PLC data source — it is where the symbol file comes from |
| Cameras | **Yes — edge only** | **No.** Cameras cannot be connected to any aggregation server |
| File drops, vendor systems, sensors | Yes, via dedicated connectors — **no PLC program** | Not routed |
| Shared failure domain | One machine | **Every machine behind that server** |
| Blocks entirely if… | No approved edge device on site | **No Softing server at the plant — route closed, no workaround** |

## The breakpoint, quoted

Every PLC route in the guide carries the same gate, and people negotiate with it, so quote
it rather than paraphrasing:

> **"In case you do not have the PLC program or you did not request the PLC program / you
> did not receive the PLC program, we CAN NOT connect the PLC!"**

Raise it at the first conversation, not at the integration date. Requesting a program from
a machine supplier takes weeks and is sometimes a commercial negotiation. Before declaring
a machine blocked on it, work the seven non-PLC rungs in
[`fallbacks.md`](references/fallbacks.md) §1 — a great many "no program" machines turn out
to be file-drop, vendor-interface or already-on-OPC-UA machines that nobody checked.

## Three live constraints worth knowing before you plan

**Only the large edge device is approved.** `rules.json` answers *both* the medium and the
small device with: *there is no approved small edge device available; go with the large
edge device or with a low-frequency data-collection method.* A wave sized around medium or
small devices is sized around hardware that does not exist yet. ⟨Confirm current status
with the IIAE.⟩

**Three branches of the live tree are unwritten** — Beckhoff on edge, Modbus on edge, and
OPC-UA-server on the aggregation server are `TODO` in `rules.json`. For the first two the
**aggregation route is fully documented and is the real answer**; for the third,
`rules-next.json` has the procedure. Never compose a procedure for an unwritten branch.

**Softing can do more than the OESL tree routes** — S5, FANUC CNC, and file/database
sources are product capabilities with no OESL route. A capability is not an approved route:
put it to the IIAE, and if adopted it becomes a change to `rules.json`.

## What the estate means for a routing decision

1,715 machines: **821 `INTEGRATED`, 395 `NOT INTEGRATED`, 48 ongoing, 451 with no status
recorded.** Three things follow that change how you answer.

- **`NOT INTEGRATED` is not a backlog of failures.** A large part of it is machines nobody
  has needed data from yet. Check whether a use case wants the data before reporting a gap.
- **Siemens is 60 % of the estate** (1,032 machines, dominated by the legacy S7-300), so
  the S7 route, its PLC-program requirement and the TIA V16→V17 upgrade come up more than
  anything else. Rockwell is second at 220 and carries the most `EVALUATION ONGOING`
  machines — its route decision is genuinely open more often.
- **`production_criticality`, `cyber_security_status`, `machine_blockers` and
  `input_protocol` are empty on all 1,715 rows.** Unpopulated fields, not a statement that
  no machine is critical. Never read one as a value.

The recorded blockers say the same thing the department says everywhere else: of the top
four — data-model standardization (CT Base, 23 machines), firmware patching for cyber
security (13), TIA V16→V17 upgrade (12), cyber-security vulnerability (5) — **three are not
connectivity problems at all.**

## Guardrails

- **Never connect a machine and never approve an external connection.** Both are human,
  `execute-with-approval`, Tandem with Plant ME / Plant IT; external connections need Cyber
  Security / OT sign-off **first**. There is no expedited path.
- **Never enable Write Permission** on an aggregation-server data source unless a use case
  writes to the PLC. Read-only is the default posture.
- **Never structure tags to the PLC's layout.** Structure to the data model (CT Base). This
  is the moment cross-plant comparability is decided.
- **Never change a signal or data-model standard** to make one machine easier — Consultation
  with ContiTech central, and interface compatibility is a standing constraint.
- **Never mark a machine `INTEGRATED`** before its acceptance test passes, and never claim a
  readiness dimension "Available" without evidence.
- **Never invent a route** for a branch the guide marks `TODO`.

## Sourcing and what is missing

The Softing configuration patterns are the OESL integration guidance captured in
`rules-next.json`, which itself references the OESL guideline documents *"Machine
Integration — Softing DataFeed — Siemens S7-300/400/1200/1500"* and *"… — Beckhoff PLC
Integration"*.

**Softing's own product documentation was not reachable from the environment this was
written in** (`industrial.softing.com` and the mirrors are blocked by the network egress
policy). Vendor capability statements are marked as such in `softing-datafeed.md` and
should be checked against the current Softing manual before being relied on.

⟨To attach: the Softing dataFEED OPC Suite manual, and the two OESL guideline documents
themselves — this skill points at them but does not contain them.⟩
