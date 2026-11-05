---
name: od-equipment-integration
description: >-
  Two entry routes to one protocol. Assessment — inventory a plant's or wave's machines,
  decide per machine which integration concept and connector applies, size and sequence the
  wave. Guidance — for one machine already assessed, route it to the IIoT Edge Platform or
  the Softing dataFEED Central OPC-UA Aggregation Server, walk the configuration pattern,
  clear the preparation gates, and take the right fallback when blocked. Use when a plant or
  wave starts, a machine's route is unclear, a use case is blocked for want of machine data,
  or someone asks how to connect a Siemens / Rockwell / Beckhoff / B&R / Omron / Mitsubishi /
  Modbus / OPC-UA device, configure a Softing dataFEED data source, or what to specify when
  ordering a new machine.
license: MIT
metadata:
  id: od-equipment-integration
  tier: technical
  lane: information-integration-service
  owner_role: IIoT Interface & Automation Engineer (IIAE)
  authority_level: draft on assessments and roadmaps; recommend a route and a configuration; never connect, never approve an external connection
  status: stable
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-signal-standardization, od-acceptance-test, od-decision-routing, od-node-red-flow-builder]
  derived_from:
    - ops-knowledge-graph/_knowledge/10-Department/Machine integration.md
    - ops-knowledge-graph/_knowledge/20-Done/Equipment integration guide.md
    - ops-knowledge-graph/.../20-lanes/information-integration-service/{playbook,tasks}.md
    - ops-knowledge-graph/_knowledge/_apps/machine-integration-guidance-app/rules.json
    - ops-knowledge-graph/_knowledge/_apps/machine-integration-guidance-app/rules-next.json
    - ops-knowledge-graph/_knowledge/machine-integration-guidance-app/dataFEEDOPCSuite_de.pdf (Softing dataFEED OPC Suite V5.70 manual, 2026-02-16)
    - ops-knowledge-graph/_knowledge/90-Sources/generated/kg_nodes.csv
    - interview with human:jakob.gabriel, 2026-09-17 (barrier-classes elicitation)
    - Work vault (Work-OpsDigit-Knowledge), Graph/Machines (Machine-List export 2026-08-21), Graph/Connectors, Graph/Plants and Graph/Tools, read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), ODEC Facts staging notes (Triage, Department KPIs and Roadmap Status, Plant - Carei, Plant - Auburn), AI-extracted and unverified, read 2026-11-05
  okf:
    type: Agent Skill
    title: Equipment integration — assessment and guidance
    tags: [information-integration-service, technical]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-09-17T00:00:00Z }
---

# Equipment integration

Read `od-context` first. Merger of the former `od-equipment-integration-assessment` and
`od-machine-integration-guidance` skills, 2026-09-17 — they were already sequential in
practice; this makes the handoff explicit instead of a cross-skill reference.

## Two entry routes

- **No assessment yet for this plant or wave?** → **Route A — Assessment.** Inventory the
  machines, decide per machine which integration concept and connector applies, size the
  investment, sequence the wave. Output: `assets/assessment-protocol.md`.
- **Assessment already done — one machine needs a route, a connector and a configuration?**
  → **Route B — Guidance.** Route this machine through the four gates, walk the
  configuration pattern, clear it to connect. Output: `assets/guidance-protocol.md`.

Route A hands each machine in its wave to Route B. Route B assumes a Route A inventory
already exists for the machine in front of you — if it doesn't, start at Route A instead of
guessing scope.

The authoritative interactive form of Route B's decision is the **Equipment integration
guide** (`_apps/machine-integration-guidance-app`, a Streamlit app whose tree lives in
`rules.json`). This skill is that tree made walkable, plus the assessment step ahead of it
and the configuration detail behind each route. When the two disagree, `rules.json` wins —
it is the maintained artefact.

---

## Route A — Assessment

Most use cases need data a machine is already producing and nobody is reading. Getting at
it is its own discipline with its own rollout, its own status vocabulary and its own
blockers — and it gates a large part of the portfolio.

### The estate

The estate is tracked in the Machine List: every machine and PLC against a plant, with vendor, PLC
model, part number, network protocol and criticality. **Count live before quoting any figure**
(filter the Machine List export by plant and status; the number goes stale quickly).

| Integration status | Meaning |
|---|---|
| `INTEGRATED` | Data flows and the acceptance test passed |
| `NOT INTEGRATED` | Nobody has connected it yet |
| `INTEGRATION ONGOING` | Work in progress |
| (blank) | No status recorded - a data-quality gap, not a finding |

**`NOT INTEGRATED` is not a backlog of failures.** A large part of it is machines nobody
has needed data from yet. The field records the state, not a judgement - do not report it
as a gap without first checking whether any use case wants that data. A blank status is not
"not integrated" either.

### The two things that get chosen

**Connector** — one per protocol or vendor family: S7, TIA, Beckhoff, Modbus,
OPC-UA, EtherCAT, Allen-Bradley/Rockwell, B&R, Bachmann, Omron FINS, Sinumerik, Simotion,
RS232, and vendor-specific ones for Engel, Piovan, Keyence, Zwick and Optris. A connector
only ever reaches a machine. It is not a system a plant uses, which is why it is kept
distinct from a tool.

The connectors in that catalogue are the **edge** connector set. The Central Aggregation Server has its own driver
list, and it is not the same one — notably it has **no Beckhoff / ADS driver**. Do not
assume a machine routable on one platform is routable on the other; check per machine in
Route B.

**Integration concept** — three sit above the connectors and are recorded as tools in their
own right: a **central OPC-UA server**, **container-based machine integration**, and the
**IIoT edge computing platform**. Which one applies depends on the machine — see § *The
topology* below.

### Assessment procedure

1. **Inventory** the plant's machines against the Machine List — vendor, PLC model, part
   number, network protocol, criticality, current integration status.
2. **Filter by demand.** Which machines does an accepted or planned use case actually need
   data from? Integration without a use case behind it is capacity spent on `NOT
   INTEGRATED` rows that nobody was waiting for.
3. **Classify the barrier tier per machine** — `references/barrier-classes.md` for the
   practitioner difficulty ranking, which disagrees with a raw read of the integration-rate
   figures in specific, known ways.
4. **Route each machine** into Route B, gate by gate, to get an integration concept and a
   connector. Record barriers where no route exists (legacy, unsupported protocol).
5. **Sequence the wave** against the plant roadmap and the readiness matrix — strategic
   plants first, then where a capability is red.
6. **Size the investment** and take it through integration investment planning; the
   go-ahead is `execute-with-approval`, Tandem with Plant ME / Plant IT.
7. **Confirm the Cyber Security / OT gate** for anything involving an external
   connection, before it is scheduled — not after. Treat controller patch status and the
   sign-off scope as a **precondition of the wave**: open patches blocked the second wave
   in practice (`references/process-chain-practice.md`).
8. Hand to execution, then `od-signal-standardization`, then `od-acceptance-test`.

Reference standard for the requirement spec: **PRS — Requirement Specification for
Machines & Equipment**, Doc ID 215534 (OESL Engineering Standards library).

### Error paths — Route A

- **No route exists for a machine** → log the barrier in the landscape module and escalate
  it into the roadmap. Do not leave it as a silent omission in the wave.
- **Cyber Security sign-off missing** → the machine waits. There is no expedited path.
- **Operations concept missing for the target system** (MSB / the data platform) → escalate to
  strategy as a tool-rollout decision; the machine can be connected and still have nowhere to
  send data.

### Definition of done — Route A

Equipment inventory and integration roadmap agreed with Plant ME / Plant IT; each machine
in scope carries a concept, a connector and a sequence position; barriers are logged;
the investment is planned and the Cyber Security gate identified.

### Targets to plan against

The integration target (machines per year and per month) and the actual are kept in the department
KPI and roadmap status. Look up the current figures there (owner: OD lead) and say which date they
are from. Check whether this lane is ahead of or behind its target before planning around it: do
not assume it is the constraint, and do not plan from remembered numbers.

---

## Route B — Guidance

Guides **one machine**. If it's a whole plant or wave, start at Route A and come back here
per machine.

### The references are the substance

| File | Use it for |
|---|---|
| [`references/barrier-classes.md`](references/barrier-classes.md) | The practitioner difficulty ranking (easy → hard) against the raw integration-rate figures, the resolved Modbus/aggregation-route question, pre-assessment tells not in the Machine List, and named-blocker root causes |
| [`references/decision-paths.md`](references/decision-paths.md) | Routing: the four gates, PLC family → available routes, connector selection, and where a path dead-ends |
| [`references/connectors.md`](references/connectors.md) | All connectors with what each reaches, over which protocol, which PLCs — and whether it is available. **Some cannot be used**, including the B&R and Bachmann connectors; the OPC UA direct connector is the fallback |
| [`references/softing-datafeed.md`](references/softing-datafeed.md) | The **Central Aggregation Server** pattern from the dataFEED V5.70 manual — the real driver list, licensing, per-driver settings for Siemens, Rockwell, Modbus and OPC-UA sources, and where the OESL guidance does not match the product |
| [`references/softing-tag-syntax.md`](references/softing-tag-syntax.md) | Tag identifier syntax per family — S7 areas and bit masking, Modbus areas with the UnitID and Group prefixes, PLC-5 / SLC file types, arrays and suffixes |
| [`references/softing-data-targets.md`](references/softing-data-targets.md) | How the data leaves dataFEED — the OPC UA path the edge reads, Store and Forward, the Preprocessing Engine, and the MQTT capability that has no OESL route |
| [`references/iiot-edge-platform.md`](references/iiot-edge-platform.md) | The **IIoT Edge** pattern in detail — the six phases, the hardware sequence, device sizing, non-PLC endpoint classes |
| [`references/fallbacks.md`](references/fallbacks.md) | The eight ways an integration blocks, what to try before declaring each one blocked, and when to stop |
| [`references/plant-integration-status.md`](references/plant-integration-status.md) | How to build a plant-by-plant status view from the Machine List and the Tool Overview: which fields to read, the computed flags, the typical record mismatches between the two, and how to count live |
| [`references/vendor-protocol-routes.md`](references/vendor-protocol-routes.md) | Per vendor, PLC model and network protocol: which route and connector applies, which combinations have no route recorded, and how to read the Machine List for them |
| [`references/connector-fact-sheets.md`](references/connector-fact-sheets.md) | Per connector: signal limits and sampling rates as product facts, file and camera endpoints, written build estimates (as a kind of source), and how to read connector-to-machine links |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | How the wave is run in the chain (1b3, 3b4, 3b5): weekly capital-request micro-process, Cyber Security as wave precondition, per-plant planning workflow, data classes with default hub and leading system, energy-monitoring and MES lessons, agent notes |
| [`references/blockers-and-waves.md`](references/blockers-and-waves.md) | Kinds of recorded blocker and their root causes, project references and waves, the eCR step, and where department roadmap figures live (staging, unverified) |

### Terminology — one name per thing

The sources use several names for the same things. These are canonical in this registry;
the aliases are listed because you will meet them in the guide, the manual and the
department notes.

| Canonical | Also called | Is |
|---|---|---|
| **IIoT Edge Platform** | IIoT Edge Computing Platform; "the edge"; iiot edge platform | The route: DATATRONiQ edge devices on the plant Kubernetes runtime, one connector per protocol |
| **Central Aggregation Server** | Central OPC-UA Aggregation Server; Softing OPC-UA Aggregation Server; **central OPC-UA server** (the department's name for the *concept*); legacy: Kepware | The route: one server running **Softing dataFEED OPC Suite**, exposing all its drivers as one OPC UA address space |
| **Softing dataFEED OPC Suite** | dataFEED; DataFeed; the Suite | The product that runs on the Central Aggregation Server. Version documented here: **V5.70** |
| **Connector** | driver; DTQ connector | Reaches a machine — or, in the case of `DTQ-OPCUA-Connector`, reaches an OPC UA **server**. Most are DATATRONiQ connectors, a few are Softing |
| **`DTQ-OPCUA-Connector`** | the OPC-UA connector | **The bridge.** How the IIoT Edge Platform reads the Central Aggregation Server's address space |
| **Data source** | driver connection | dataFEED's term for a connection that *defines* datapoints. Does **not** mean "upstream" |
| **Tool** | — | A system a plant uses. Never the same row as a connector |

"Central OPC-UA server" and "Central Aggregation Server" are the same thing seen from two
sides — the department records the *integration concept*, the guide labels the *route*. Use
the guide's wording when handing someone a procedure: it is the label on their screen.

### How to use Route B

1. **Gate 0 — what is installed at this plant?** Not the PLC. The tree starts here because
   it decides which patterns are available at all. → `decision-paths.md`
2. **Ask the cheap question first: is the machine already on an OPC-UA server?** If yes the
   variant is ③, the bridge is `DTQ-OPCUA-Connector`, and neither the PLC program nor cabinet
   work is needed. Largest single cost difference in the guide, and the easiest to skip past.
3. **Gate 1 — decide the variant** for this PLC family: ① edge device, ② connector without a
   device, or ③ via the aggregation server. Both ① and ③ carry Siemens and Rockwell at scale,
   and several plants have both, so this is a per-machine decision rather than a vendor or
   plant policy.
4. **Gate 2 — pick the connector** (edge) or the **data source driver** (aggregation).
5. **Walk the pattern** in `softing-datafeed.md` or `iiot-edge-platform.md`.
6. **Gate 3 — clear the preparation blocks** in order: budget → infrastructure → **PLC
   program** → tags → cyber security.
7. **Blocked?** → `fallbacks.md` before recording it as blocked.
8. **Gate 4 — record it**: Machine List, Machine CV (mandatory vs optional tags), Edge
   Device List, inform MPEE OD. Status moves to `INTEGRATED` only after
   `od-acceptance-test` passes.

### The topology — three ingress variants, one terminus

Every machine reaches **the data platform** through the **IIoT Edge Platform**. What varies is
how the PLC gets to it, and there are exactly three shapes. The department numbers them
itself — they are recorded as tools in the Tool Overview as *Concept 1*, *2* and *3*.

```text
 ①  PLC ──► edge device ──(connector)──►  IIoT ──MQTT──► Node-RED
                                        Platform      │
                                                   offload ▼  Databricks ──► Azure Storage
                                                                              (Parquet)
                                        Platform
 ②  PLC ──────(connector)─────────────►  IIoT
                                        Platform
 ③  PLC ──► OPC-UA aggregation server ─►  IIoT
            (Softing dataFEED)  OPC UA   Platform
            └ DTQ-OPCUA-Connector ┘
```

| # | Shape | Department's name |
|---|---|---|
| **①** | **PLC → edge device with connector → IIoT platform.** A DATATRONiQ edge device in or beside the cabinet runs the connector | **Concept 3 — IIoT Edge Computing Platform** |
| **②** | **PLC → connector → IIoT platform.** The connector runs without a dedicated edge device at the machine | **Concept 2 — container-based Machine Integration** |
| **③** | **PLC → OPC-UA aggregation server → IIoT platform.** A Softing dataFEED server concentrates the drivers; the edge reads its address space over OPC UA | **Concept 1 — Central OPC-UA Server** |

The IIoT Edge Platform is the terminus in all three. ① and ② differ in *where the
connector runs*, not in where the data goes. ③ puts a protocol concentrator in front, and
the link back is the **`DTQ-OPCUA-Connector`** — the one connector in the set of 26 that
reaches a *server* rather than a machine.

The guide's recommendation for ③ is **`IIoT Edge Platform → OPC-UA Server`**, reached when
the plant has the edge platform and the PLC type is *OPC-UA Server*. Its tasks are the
bridge itself: machines connected to the Softing server, endpoint details available, the
server's address-space structure known, the edge installed with its endpoints known, then
*"establish the connection between the OPC-UA Aggregation Server and the IIoT Edge
Platform"*.

> **③ needs both pieces, and the guide says so.** The Siemens S7 aggregation recommendation
> states that you cannot connect the PLCs *"when you have chosen the OPC-UA server as the
> connectivity framework **and you don't have the IIoT Edge Computing Platform
> available**"*. A Softing server with no edge platform behind it delivers nothing to the
> data platform.

**Variant ② is real but rarely deployed** — treat it as a live concept with no written route in
the guide, not as a standard option: if a machine looks like a ② candidate, that is an IIAE
conversation. The estate's *"Low Cost — Direct Connection"* and *"Low Cost — Helmholz"*
approaches are the shape ② takes in practice — the "low cost" being the absence of edge-device
hardware.

### Which variants a plant actually has

Not one platform per plant. The Tool Overview records the concepts per plant; read it live
(`references/plant-integration-status.md` says how). Patterns to expect:

- Plants with ① only, plants with ③ only, and plants with **both ① and ③**. Where both are available,
  "which platform does this plant have" is the wrong question: the choice is per machine.
- Variant ② may appear alongside ① at a plant.
- Plants with **no concept recorded at all**; there, the first conversation is rollout, not integration.
  Check whether "none recorded" means none exists or only that nobody has recorded it.

### Choosing the variant for one machine

| | **① edge device** | **② connector, no device** | **③ via aggregation server** |
|---|---|---|---|
| Needs | IIoT Edge Platform + an approved edge device | IIoT Edge Platform | IIoT Edge Platform **and** the Softing server |
| Valid for | Brownfield and greenfield | Brownfield and greenfield — no cabinet or hardware dependency ties it to either | Brownfield (the OPC-UA data source is also greenfield) |
| Cabinet work | Mount, 24 V, shopfloor Ethernet, ETH1 | None at the machine | None at the machine |
| PLC program | Yes, for a PLC endpoint | Yes | Yes, for a PLC data source — it is where the symbol file comes from |
| Cameras | Yes — the only variant | No | No. Cameras cannot be connected to any aggregation server |
| File drops, vendor systems, sensors | Yes, dedicated connectors, no PLC program | — | Not routed |
| Failure domain | One machine, or one cell where a device is shared | Per connector | Every machine behind that server |
| Driver gaps that decide it | Beckhoff has a connector here and no Softing driver | — | Modbus has a driver here and an unwritten edge branch |
| Maturity | Fully routed | No written route | Fully routed |

The driver-gap row is the practical decider more often than any principle: Beckhoff has an
edge connector and no Softing driver; Modbus has a Softing driver and an unwritten edge
branch. No variant covers everything.

An edge device is not always one per machine — the estate records devices shared across a
cell (*"Edge Device [Same as BM11 device] via Siemens TCP/IP Ethernet Driver"*), and Beckhoff
I/O clamps daisy-chained into one device. Sharing changes the failure domain; record it.

### The breakpoint, quoted

Every PLC route in the guide carries the same gate, and people negotiate with it, so quote
it rather than paraphrasing:

> **"In case you do not have the PLC program or you did not request the PLC program / you
> did not receive the PLC program, we CAN NOT connect the PLC!"**

Raise it at the first conversation, not at the integration date. Requesting a program from
a machine supplier takes weeks and is sometimes a commercial negotiation. Before declaring
a machine blocked on it, work the seven non-PLC rungs in [`fallbacks.md`](references/fallbacks.md)
§1 — a great many "no program" machines turn out to be file-drop, vendor-interface or
already-on-OPC-UA machines that nobody checked.

### Before naming a connector, check it exists

Some connectors cannot be used: they are marked `Idea · NOT AVAILABLE`, are in development, or are
`Productive · DO NOT USE`. Naming one of them costs a site visit. Full catalogue with availability:
[`connectors.md`](references/connectors.md).

The three that come up most:

- **`DTQ-B&R-Connector` and `DTQ-Bachmann-Connector` do not exist.** Both are `Idea`, both noted
  *"Development to be started with Rollout in Dolne Vestenice"*. Machines of both families are
  integrated anyway, mostly over OPC UA through the Central Aggregation Server. An unavailable
  native connector is not an unreachable PLC. Ask what the machine exposes before raising a barrier.
- **`SFT-SIMATIC S7-Connector` is `DO NOT USE`**, because it is not developed cloud-native and
  *"still does not support CYBER SECURITY compliant communication to the PLC."* The second
  reason ends the conversation: it is a security position, not a preference. For S7-300/400 on
  the edge, use `DTQ-S7-Connector`. The restriction is on Softing's edgeConnector, not on
  the dataFEED OPC Suite aggregation server, which is a different product on a different path.
- **`DTQ-OPCUA-Connector` — Productive · USE — is the standing fallback.** It reaches any OPC
  UA server and does not care what is behind it: a machine's own embedded server
  (topology ②, direct) or the Central Aggregation Server (topology ③, bridge). Same
  container, two jobs — and on the bridge path the machine is reached by two connectors in
  series, so the Machine List row must name both.

One field pair disagrees with itself: `DTQ-MODBUS-Connector` is `status: Idea` and
`utilization: USE`. Confirm with the IIAE before promising a Modbus route - Modbus / TCP machines
are common - and record the answer.

### ⚠ Two things the OESL guidance gets wrong

Checked against the Softing dataFEED OPC Suite V5.70 manual, now in the bundle. Both sit
in the happy path of a route somebody will try this month.

**There is no Beckhoff data source.** The recommendation *Central Aggregation Server —
Beckhoff Integration* says to select Beckhoff and choose the ADS protocol. dataFEED
V5.70 has neither; "Beckhoff" appears only as an example of a vendor whose
controllers speak Modbus. Reach a Beckhoff PLC via Modbus TCP, or via a TwinCAT OPC UA /
OPC DA server. The native ADS path is the edge connector — and that branch is `TODO`.
Beckhoff therefore has no fully-written route on either platform. Say so; take it to the
IIAE.

**NetLink is discontinued.** The Siemens recommendations list `Netlink` as a protocol
option. It was discontinued in V5.38, is retained only for legacy configurations, and
Softing strongly recommends migrating them to `Siemens S7`. A Helmholz NetLink gateway
is still the right hardware for a PLC with no Ethernet of its own — you address it with the
Siemens S7 protocol. The guidance conflates the hardware with the protocol name.

Both are recorded as open gaps in `registry.yaml`: the source of truth is `rules.json`, and
fixing them is a change there, not here.

### Three live constraints worth knowing before you plan

**Check which edge device sizes are approved.** At the last reading, `rules.json` answered *both*
the medium and the small device with: *there is no approved small edge device available; go with
the large edge device or with a low-frequency data-collection method.* A wave sized around medium
or small devices is sized around hardware that may not exist yet. Re-confirm the current approval
with the IIAE before sizing (look up: `rules.json`, IIAE).

**Branches of the live tree can be unwritten** — Beckhoff on edge, Modbus on edge, and
OPC-UA-server on the aggregation server were `TODO` in `rules.json`. For the first two the
aggregation path is fully documented and is the real answer; for the third,
`rules-next.json` has the procedure. Re-check the live tree. Never compose a procedure for an
unwritten branch.

**Softing does more than the OESL tree routes.** Data sources with no route: FANUC CNC,
database read (ODBC), MQTT Broker and MQTT Publisher as *sources*, file read, OPC Classic,
OPC Classic Tunnel. Siemens S5 has a full driver and no route either. A capability is not an
approved route: put it to the IIAE, and if adopted it becomes a change to `rules.json`.
Note also that each PLC family needs its own licence (`dataFEED OPC Server Siemens /
CNC / Rockwell / Mitsubishi / Modbus / B&R`) unless Suite Extended is in place — check that
before promising a route, and check the licensed number of concurrent server configurations
against what is already running (look up: Central Aggregation Server licence record).

### What the estate means for a routing decision

Count live on the Machine List (status by vendor) before answering. Three patterns change how you
answer.

- `NOT INTEGRATED` is not a backlog of failures. A large part of it is machines nobody
  has needed data from yet. Check whether a use case wants the data before reporting a gap.
- Siemens dominates the estate, with the legacy S7-300 well represented, so
  the S7 route, its PLC-program requirement and the TIA V16→V17 upgrade come up more than
  anything else. Rockwell is the next large family and tends to carry the most
  `EVALUATION ONGOING` machines — its route decision is genuinely open more often.
- Fields such as `production_criticality`, `cyber_security_status`, `machine_blockers` and
  `input_protocol` have been unpopulated in the export. Unpopulated fields, not a statement that
  no machine is critical. Never read an empty one as a value; check the live list.

The recorded blockers say the same thing the department says everywhere else: the common classes
(data-model standardization, recorded as *CT Base*; firmware patching for cyber security; the
TIA V16→V17 upgrade; cyber-security vulnerability) are mostly not connectivity problems at all.
See `references/barrier-classes.md` for which one is a symptom of what.

### Error paths — Route B

- **No route exists for this machine** → log the barrier and escalate into the roadmap.
- **Cyber Security sign-off missing** → the machine waits. There is no expedited path.
- **Guide branch is `TODO`** → do not invent a procedure. Say which branch is unwritten and
  take the other platform's route if it's written, else escalate to the IIAE.

### Definition of done — Route B

Machine List, Machine CV (mandatory vs optional tags) and Edge Device List updated; MPEE OD
informed; integration status moves to `INTEGRATED` only after `od-acceptance-test` passes.

---

## Guardrails — both routes

- **Never connect a machine and never approve an external connection.** Both are human,
  `execute-with-approval`, Tandem with Plant ME / Plant IT; external connections need Cyber
  Security / OT sign-off **first**. There is no expedited path.
- **Never enable Write Permission** on an aggregation-server data source unless a use case
  writes to the PLC. Read-only is the default posture.
- **Never structure tags to the PLC's layout.** Structure to the agreed data model — the
  estate records this as *CT Base* (re-confirm the current name with the IIAE). This is the moment
  cross-plant comparability is decided.
- **Never change a signal or data-model standard** to make one machine easier — Consultation
  with Plant ME / Plant IT, not a per-machine convenience.
- **Never mark a machine `INTEGRATED`** before its acceptance test passes, and never claim a
  readiness dimension "Available" without evidence.
- **Never invent a route** for a branch the guide marks `TODO`.
- **Never record a machine as integrated without a barrier-tier judgement behind it** — an
  unavailable native connector is not the same as an unreachable PLC; check what the machine
  exposes first (`references/barrier-classes.md`, `references/connectors.md`).

## Output — the protocol

Neither route ends in prose advice. Fill the matching asset as the work happens, not
afterwards:

- **Route A** → [`assets/assessment-protocol.md`](assets/assessment-protocol.md) — one
  document per plant/wave, a machine-by-machine table, and a sign-off.
- **Route B** → [`assets/guidance-protocol.md`](assets/guidance-protocol.md) — one document
  per machine, the gates answered in order, and a hand-off to `od-acceptance-test`.
- **Before either route, at plant level** → [`assets/plant-readiness-brief.md`](assets/plant-readiness-brief.md) — the
  plant's row from the records, the flags to clear and the questions only the plant can answer.

Both are written so a plant engineer who wasn't in the room can pick up the finished
document and know exactly what was decided, why, and what's still open — a reusable record,
not a summary that only makes sense to whoever wrote it.

## Sourcing

**Product behaviour** — the Softing dataFEED OPC Suite V5.70 operating manual (German,
dated 2026-02-16), cited by title, version and page throughout
`softing-datafeed.md` and `softing-tag-syntax.md` so any claim can be checked against the
source. Internal path in `metadata.derived_from`, not in skill body prose. The manual is a
Git-LFS object in the knowledge bundle — `git lfs pull` before expecting to read it.

**OESL process** — the Equipment integration guide's `rules.json` (live) and
`rules-next.json` (next), which also reference two OESL guideline documents by name:
*"Machine Integration — Softing DataFeed — Siemens S7-300/400/1200/1500"* and
*"… — Beckhoff PLC Integration"*.

Where the manual and the OESL guidance disagree, the disagreement is stated rather than
resolved: `rules.json` is authoritative for what OESL permits, the manual for what the
product does, and a procedure that names a menu item the product does not have cannot be
followed by anyone.

⟨To attach: the two OESL guideline documents themselves — this skill points at them but
does not contain them. Also unverified: whether any OESL plant still runs a NetLink
configuration, and the German manual's own contradiction over which unsigned-type mode is
the default.⟩
