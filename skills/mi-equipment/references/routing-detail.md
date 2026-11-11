---
type: Skill Reference
title: Routing detail
description: The detail behind Route A and Route B - estate and status vocabulary, terminology, the three ingress variants and how to choose, the breakpoint, connector availability traps, the two OESL guidance errors, live constraints and what the estate means for a routing decision.
resource: ../SKILL.md
status: stable
tags: [integration, routing, topology]
---
# Routing detail

Moved out of `SKILL.md`. The authoritative interactive form of the Route B decision is the Equipment integration guide
(`rules.json`); when it and this file disagree, `rules.json` wins. Where the Softing manual and the OESL guidance disagree, the
disagreement is stated, not resolved: `rules.json` is authoritative for what OESL permits, the manual for what the product does.

## The estate (Route A)

The estate is tracked in the Machine List: every machine and PLC against a plant, with vendor, PLC model, part number, network
protocol and criticality. **Count live before quoting any figure** (filter the export by plant and status).

| Integration status | Meaning |
|---|---|
| `INTEGRATED` | Data flows and the acceptance test passed |
| `NOT INTEGRATED` | Nobody has connected it yet |
| `INTEGRATION ONGOING` | Work in progress |
| (blank) | No status recorded - a data-quality gap, not a finding |

**`NOT INTEGRATED` is not a backlog of failures.** A large part of it is machines nobody has needed data from yet. Do not report
it as a gap without first checking whether any use case wants that data. A blank status is not "not integrated" either.

**Connector** - one per protocol or vendor family: S7, TIA, Beckhoff, Modbus, OPC-UA, EtherCAT, Allen-Bradley/Rockwell, B&R,
Bachmann, Omron FINS, Sinumerik, Simotion, RS232, plus vendor-specific ones for Engel, Piovan, Keyence, Zwick and Optris. A
connector only ever reaches a machine; it is not a system a plant uses, which is why it is kept distinct from a tool. These are
the **edge** connector set. The Central Aggregation Server has its own driver list, and it has **no Beckhoff / ADS driver**.
Never assume a machine routable on one platform is routable on the other.

**Integration concept** - three sit above the connectors and are recorded as tools: a central OPC-UA server, container-based
machine integration, and the IIoT edge computing platform.

Targets: the integration target (machines per year and per month) and the actual are kept in the department KPI and roadmap
status. Look up the current figures (owner: OD lead), say which date they are from, check whether this lane is ahead of or
behind target before planning around it. Do not assume it is the constraint; do not plan from remembered numbers.

Reference standard for the requirement spec: **PRS - Requirement Specification for Machines & Equipment**, Doc ID 215534
(OESL Engineering Standards library).

## Terminology - one name per thing

| Canonical | Also called | Is |
|---|---|---|
| **IIoT Edge Platform** | IIoT Edge Computing Platform; "the edge" | The route: DATATRONiQ edge devices on the plant Kubernetes runtime, one connector per protocol |
| **Central Aggregation Server** | Central OPC-UA Aggregation Server; Softing OPC-UA Aggregation Server; **central OPC-UA server** (the department's name for the *concept*); legacy: Kepware | The route: one server running **Softing dataFEED OPC Suite**, exposing all its drivers as one OPC UA address space |
| **Softing dataFEED OPC Suite** | dataFEED; DataFeed; the Suite | The product on the Central Aggregation Server. Version documented: **V5.70** |
| **Connector** | driver; DTQ connector | Reaches a machine - or, for `DTQ-OPCUA-Connector`, an OPC UA **server**. Most are DATATRONiQ connectors, a few are Softing |
| **`DTQ-OPCUA-Connector`** | the OPC-UA connector | **The bridge.** How the IIoT Edge Platform reads the Central Aggregation Server's address space |
| **Data source** | driver connection | dataFEED's term for a connection that *defines* datapoints. Does **not** mean "upstream" |
| **Tool** | - | A system a plant uses. Never the same row as a connector |

"Central OPC-UA server" and "Central Aggregation Server" are the same thing seen from two sides (department: concept; guide:
route). Use the guide's wording when handing someone a procedure.

## The topology - three ingress variants, one terminus

Every machine reaches the data platform through the **IIoT Edge Platform**. Three shapes, numbered by the department as Concept 1-3
in the Tool Overview.

```text
 1  PLC --> edge device --(connector)-->  IIoT --MQTT--> Node-RED
                                        Platform      |
                                                   offload v  Databricks --> Azure Storage (Parquet)
 2  PLC ------(connector)------------->  IIoT Platform
 3  PLC --> OPC-UA aggregation server (Softing dataFEED) --OPC UA, DTQ-OPCUA-Connector--> IIoT Platform
```

| # | Shape | Department's name |
|---|---|---|
| **1** | PLC -> edge device with connector -> IIoT platform. A DATATRONiQ edge device in or beside the cabinet runs the connector | **Concept 3 - IIoT Edge Computing Platform** |
| **2** | PLC -> connector -> IIoT platform. The connector runs without a dedicated edge device at the machine | **Concept 2 - container-based Machine Integration** |
| **3** | PLC -> OPC-UA aggregation server -> IIoT platform. A Softing dataFEED server concentrates the drivers; the edge reads its address space over OPC UA | **Concept 1 - Central OPC-UA Server** |

The edge platform is the terminus in all three. 1 and 2 differ in *where the connector runs*, not where the data goes. 3 puts a
protocol concentrator in front; the link back is `DTQ-OPCUA-Connector`, the one connector that reaches a *server* rather than a
machine. The guide's recommendation for 3 is `IIoT Edge Platform -> OPC-UA Server`, reached when the plant has the edge platform
and the PLC type is *OPC-UA Server*; its tasks are the bridge itself (machines connected to the Softing server, endpoint details,
address-space structure known, edge installed, then "establish the connection between the OPC-UA Aggregation Server and the IIoT
Edge Platform").

> **3 needs both pieces.** The Siemens S7 aggregation recommendation says you cannot connect the PLCs "when you have chosen the
> OPC-UA server as the connectivity framework **and you don't have the IIoT Edge Computing Platform available**". A Softing
> server with no edge platform behind it delivers nothing to the data platform.

**Variant 2 is real but rarely deployed** - a live concept with no written route; a 2 candidate is an IIAE conversation. The
estate's *"Low Cost - Direct Connection"* and *"Low Cost - Helmholz"* approaches are the shape 2 takes in practice (low cost = no
edge-device hardware).

### Which variants a plant has

Not one platform per plant. The Tool Overview records concepts per plant; read it live
(`plant-integration-status.md`). Expect: plants with 1 only, 3 only, or **both** (then the choice is per machine, not per
plant); variant 2 alongside 1; plants with **no concept recorded** (first conversation is rollout, not integration - check whether
"none recorded" means none exists or only that nobody recorded it).

### Choosing the variant for one machine

| | **1 edge device** | **2 connector, no device** | **3 via aggregation server** |
|---|---|---|---|
| Needs | Edge Platform + approved edge device | Edge Platform | Edge Platform **and** the Softing server |
| Valid for | Brownfield and greenfield | Brownfield and greenfield | Brownfield (OPC-UA data source also greenfield) |
| Cabinet work | Mount, 24 V, shopfloor Ethernet, ETH1 | None at the machine | None at the machine |
| PLC program | Yes, for a PLC endpoint | Yes | Yes, for a PLC data source (symbol file) |
| Cameras | Yes - the only variant | No | No. Cameras cannot be connected to any aggregation server |
| File drops, vendor systems, sensors | Yes, dedicated connectors, no PLC program | - | Not routed |
| Failure domain | One machine, or one cell where a device is shared | Per connector | Every machine behind that server |
| Driver gaps that decide it | Beckhoff has a connector here, no Softing driver | - | Modbus has a driver here, an unwritten edge branch |
| Maturity | Fully routed | No written route | Fully routed |

The driver-gap row is the practical decider more often than any principle. An edge device is not always one per machine: devices
are shared across a cell (*"Edge Device [Same as BM11 device] via Siemens TCP/IP Ethernet Driver"*) and Beckhoff I/O clamps are
daisy-chained into one device. Sharing changes the failure domain; record it.

## The breakpoint, quoted

Every PLC route carries the same gate, and people negotiate with it, so quote it:

> **"In case you do not have the PLC program or you did not request the PLC program / you did not receive the PLC program, we CAN NOT connect the PLC!"**

Raise it at the first conversation, not at the integration date. Requesting a program from a machine supplier takes weeks and is
sometimes a commercial negotiation. Before declaring a machine blocked on it, work the seven non-PLC rungs in
`fallbacks.md` section 1; many "no program" machines are file-drop, vendor-interface or already-on-OPC-UA machines
nobody checked.

## Before naming a connector, check it exists

Some are `Idea · NOT AVAILABLE`, in development, or `Productive · DO NOT USE`. Naming one costs a site visit. Catalogue:
`connectors.md`. The three that come up most:

- **`DTQ-B&R-Connector` and `DTQ-Bachmann-Connector` do not exist.** Both `Idea`, both noted "Development to be started with
  Rollout in Dolne Vestenice". Machines of both families are integrated anyway, mostly over OPC UA through the Central
  Aggregation Server. An unavailable native connector is not an unreachable PLC; ask what the machine exposes before raising a barrier.
- **`SFT-SIMATIC S7-Connector` is `DO NOT USE`**: not developed cloud-native and "still does not support CYBER SECURITY compliant
  communication to the PLC." A security position, not a preference. For S7-300/400 on the edge use `DTQ-S7-Connector`. The
  restriction is on Softing's edgeConnector, not on the dataFEED OPC Suite aggregation server (different product, different path).
- **`DTQ-OPCUA-Connector` (Productive · USE) is the standing fallback.** It reaches any OPC UA server: a machine's own embedded
  server (variant 2, direct) or the Central Aggregation Server (variant 3, bridge). On the bridge path the machine is reached by
  two connectors in series, so the Machine List row must name both.

`DTQ-MODBUS-Connector` is `status: Idea` and `utilization: USE`, which disagree. Confirm with the IIAE before promising a Modbus
route (Modbus / TCP machines are common) and record the answer.

## Two things the OESL guidance gets wrong

Checked against the Softing dataFEED OPC Suite V5.70 manual. Both sit in the happy path of a route somebody will try this month.

**There is no Beckhoff data source.** The recommendation *Central Aggregation Server - Beckhoff Integration* says to select
Beckhoff and choose the ADS protocol. dataFEED V5.70 has neither; "Beckhoff" appears only as an example of a vendor whose
controllers speak Modbus. Reach a Beckhoff PLC via Modbus TCP, or via a TwinCAT OPC UA / OPC DA server. The native ADS path is the
edge connector, and that branch is `TODO`. Beckhoff has no fully-written route on either platform: say so, take it to the IIAE.

**NetLink is discontinued.** The Siemens recommendations list `Netlink` as a protocol option. Discontinued in V5.38, retained only
for legacy configurations; Softing recommends migrating to `Siemens S7`. A Helmholz NetLink gateway is still the right hardware
for a PLC with no Ethernet of its own - address it with the Siemens S7 protocol. The guidance conflates hardware and protocol name.

Both are recorded as open gaps in `registry.yaml`; fixing them is a change to `rules.json`, not here.

## Live constraints to know before planning

**Edge device sizes.** At the last reading, `rules.json` answered both the medium and the small device with: *there is no
approved small edge device available; go with the large edge device or with a low-frequency data-collection method.* A wave sized
around medium or small devices may be sized around hardware that does not exist yet. Re-confirm with the IIAE (look up:
`rules.json`, IIAE).

**Unwritten branches.** Beckhoff on edge, Modbus on edge, and OPC-UA-server on the aggregation server were `TODO` in `rules.json`.
For the first two the aggregation path is fully documented and is the real answer; for the third `rules-next.json` has the
procedure. Re-check the live tree. Never compose a procedure for an unwritten branch.

**Softing does more than the OESL tree routes.** Data sources with no route: FANUC CNC, database read (ODBC), MQTT Broker and
MQTT Publisher as sources, file read, OPC Classic, OPC Classic Tunnel; Siemens S5 has a full driver and no route. A capability is
not an approved route: put it to the IIAE; if adopted it becomes a change to `rules.json`. Each PLC family needs its own licence
(`dataFEED OPC Server Siemens / CNC / Rockwell / Mitsubishi / Modbus / B&R`) unless Suite Extended is in place - check before
promising a route, and check the licensed number of concurrent server configurations against what is running (look up: Central
Aggregation Server licence record).

## What the estate means for a routing decision

Count live on the Machine List (status by vendor) before answering.

- Siemens dominates the estate, S7-300 well represented, so the S7 route, its PLC-program requirement and the TIA V16->V17
  upgrade come up more than anything. Rockwell is next and tends to carry the most `EVALUATION ONGOING` machines: its route
  decision is genuinely open more often.
- `production_criticality`, `cyber_security_status`, `machine_blockers` and `input_protocol` have been unpopulated in the export.
  Unpopulated, not "no machine is critical". Never read an empty field as a value.
- The recorded blockers (data-model standardization, recorded as *CT Base*; firmware patching; TIA V16->V17; cyber-security
  vulnerability) are mostly not connectivity problems. See `barrier-classes.md` for which is a symptom of what.

## Sourcing

Product behaviour: Softing dataFEED OPC Suite V5.70 operating manual (German, 2026-02-16), cited by title, version and page in
`softing-datafeed.md` and `softing-tag-syntax.md`. It is a Git-LFS object in the knowledge bundle (`git lfs pull`). OESL process:
the guide's `rules.json` (live) and `rules-next.json` (next), which reference two OESL guideline documents: *"Machine Integration
- Softing DataFeed - Siemens S7-300/400/1200/1500"* and *"... - Beckhoff PLC Integration"*.
