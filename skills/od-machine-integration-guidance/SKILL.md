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
    - ops-knowledge-graph/_knowledge/machine-integration-guidance-app/dataFEEDOPCSuite_de.pdf (Softing dataFEED OPC Suite V5.70 manual, 1,540 pp., 2026-02-16)
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
| [`references/softing-datafeed.md`](references/softing-datafeed.md) | The **Central Aggregation Server** pattern from the dataFEED V5.70 manual — the real driver list, licensing, per-driver settings for Siemens, Rockwell, Modbus and OPC-UA sources, and **where the OESL guidance does not match the product** |
| [`references/softing-tag-syntax.md`](references/softing-tag-syntax.md) | Tag identifier syntax per family — S7 areas and bit masking, Modbus areas with the UnitID and Group prefixes, PLC-5 / SLC file types, arrays and suffixes |
| [`references/softing-data-targets.md`](references/softing-data-targets.md) | How the data leaves dataFEED — the OPC UA path the edge reads, Store and Forward, the Preprocessing Engine, and the MQTT capability that has no OESL route |
| [`references/iiot-edge-platform.md`](references/iiot-edge-platform.md) | The **IIoT Edge** pattern in detail — the six phases, the hardware sequence, device sizing, non-PLC endpoint classes |
| [`references/fallbacks.md`](references/fallbacks.md) | The eight ways an integration blocks, what to try before declaring each one blocked, and when to stop |

## Terminology — one name per thing

The sources use several names for the same things. These are canonical in this registry;
the aliases are listed because you will meet them in the guide, the manual and the
department notes.

| Canonical | Also called | Is |
|---|---|---|
| **IIoT Edge Platform** | IIoT Edge Computing Platform; "the edge"; iiot edge platform | The route: DATATRONiQ edge devices on the plant Kubernetes runtime, one connector per protocol |
| **Central Aggregation Server** | Central OPC-UA Aggregation Server; Softing OPC-UA Aggregation Server; **central OPC-UA server** (the department's name for the *concept*); legacy: Kepware | The route: one server running **Softing dataFEED OPC Suite**, exposing all its drivers as one OPC UA address space |
| **Softing dataFEED OPC Suite** | dataFEED; DataFeed; the Suite | The product that runs on the Central Aggregation Server. Version documented here: **V5.70** |
| **Connector** | driver; DTQ connector | Reaches a machine. 24 DATATRONiQ + 2 Softing |
| **Data source** | driver connection | dataFEED's term for a connection that *defines* datapoints. Does **not** mean "upstream" |
| **Tool** | — | A system a plant uses. Never the same row as a connector |

"Central OPC-UA server" and "Central Aggregation Server" are the same thing seen from two
sides — the department records the *integration concept*, the guide labels the *route*. Use
the guide's wording when handing someone a procedure: it is the label on their screen.

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

## ⚠ Two things the OESL guidance gets wrong

Checked against the **Softing dataFEED OPC Suite V5.70 manual**, now in the bundle. Both
sit in the happy path of a route somebody will try this month.

**There is no Beckhoff data source.** The recommendation *Central Aggregation Server —
Beckhoff Integration* says to select **Beckhoff** and choose the **ADS** protocol. dataFEED
V5.70 has neither; "Beckhoff" appears once in 1,540 pages, as an example of a vendor whose
controllers speak **Modbus**. Reach a Beckhoff PLC via Modbus TCP, or via a TwinCAT OPC UA /
OPC DA server. The native ADS path is the **edge** connector — and that branch is `TODO`.
**Beckhoff therefore has no fully-written route on either platform.** Say so; take it to the
IIAE.

**NetLink is discontinued.** The Siemens recommendations list `Netlink` as a protocol
option. It was discontinued in V5.38, is retained only for legacy configurations, and
Softing strongly recommends migrating them to `Siemens S7`. A **Helmholz NetLink gateway**
is still the right hardware for a PLC with no Ethernet of its own — you address it with the
Siemens S7 protocol. The guidance conflates the hardware with the protocol name.

Both are recorded as open gaps in `registry.yaml`: the source of truth is `rules.json`, and
fixing them is a change there, not here.

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

**Softing does more than the OESL tree routes.** Data sources with no route: FANUC CNC,
database read (ODBC), MQTT Broker and MQTT Publisher as *sources*, file read, OPC Classic,
OPC Classic Tunnel. Siemens S5 has a full driver and no route either. A capability is not an
approved route: put it to the IIAE, and if adopted it becomes a change to `rules.json`.
Note also that **each PLC family needs its own licence** (`dataFEED OPC Server Siemens /
CNC / Rockwell / Mitsubishi / Modbus / B&R`) unless Suite Extended is in place — check that
before promising a route, and remember the server runs at most **50 concurrent
configurations** of a possible 100.

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

## Sourcing

**Product behaviour** — the **Softing dataFEED OPC Suite V5.70 operating manual** (German,
1,540 pp., dated 2026-02-16) at
`_knowledge/machine-integration-guidance-app/dataFEEDOPCSuite_de.pdf` in the knowledge
bundle. `softing-datafeed.md` and `softing-tag-syntax.md` carry page references throughout,
so any claim can be checked against the source. The manual is a Git-LFS object — `git lfs
pull` before expecting to read it.

**OESL process** — the Equipment integration guide's `rules.json` (live) and
`rules-next.json` (next), which also reference two OESL guideline documents by name:
*"Machine Integration — Softing DataFeed — Siemens S7-300/400/1200/1500"* and
*"… — Beckhoff PLC Integration"*.

Where the manual and the OESL guidance disagree, the disagreement is stated rather than
resolved: `rules.json` is authoritative for **what OESL permits**, the manual for **what the
product does**, and a procedure that names a menu item the product does not have cannot be
followed by anyone.

⟨To attach: the two OESL guideline documents themselves — this skill points at them but
does not contain them. Also unverified: whether any OESL plant still runs a NetLink
configuration, and the German manual's own contradiction over which unsigned-type mode is
the default.⟩
