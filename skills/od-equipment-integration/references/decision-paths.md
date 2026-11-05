---
type: Skill Reference
title: Decision paths
description: How a machine is routed to one of the three ingress variants, what the fallback is at each branch, and what decides it.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [integration, opc-ua, decision]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Decision paths

How a machine is routed to an integration pattern, what the fallback is at each branch,
and where a path genuinely dead-ends. Source: the Equipment integration guide's
`rules.json` (live, 25 questions / 27 recommendations) and `rules-next.json` (next, 35 / 31).
`rules.json` is authoritative for an answer today.

Read this first, then the pattern file for the route you land on:

- **Central Aggregation Server** → [`softing-datafeed.md`](softing-datafeed.md), with
  [`softing-tag-syntax.md`](softing-tag-syntax.md) for tag identifiers and
  [`softing-data-targets.md`](softing-data-targets.md) for how the data leaves
- **IIoT Edge Platform** → [`iiot-edge-platform.md`](iiot-edge-platform.md)
- **Blocked** → [`fallbacks.md`](fallbacks.md)

Canonical names for the three variants, and their aliases, are in the skill's *Terminology*
section. In short: **Central Aggregation Server** is the guide's name for the route that the
department notes call the *central OPC-UA server* concept, and it runs **Softing dataFEED
OPC Suite**.

> **Two rows below correct the OESL guidance against the product manual.** dataFEED OPC
> Suite V5.70 has **no Beckhoff data source**, and the **NetLink protocol was discontinued
> in V5.38** — both are still in the OESL recommendation text. See
> [`softing-datafeed.md`](softing-datafeed.md) § *Where the OESL guidance does not match the
> product*.

---

## Gate 0 — What is already installed at this plant

The tree starts with what the plant already has, not with the PLC — that decides which
patterns are available at all.

| Answer | Route | If it turns out to be wrong |
|---|---|---|
| **IIoT Edge Platform** available | → Gate 1, variants ① and ② | If no edge device exists → edge-device hardware path first. Note ② needs no device at the machine, but it has no written route |
| **Edge device on hand, not installed** | → Edge device hardware installation | Only the **large** device is approved — see below |
| **Central Aggregation Server** (Softing dataFEED; legacy Kepware) available | → Gate 1, variant ③ | **③ also needs the IIoT Edge Platform** — the server is a concentrator, not a destination. Without the server ③ is closed; without the edge it delivers nothing |
| **Not sure what is installed** | → *Plant Capabilities & System Availability & Rollout* list | Then a ≤30 min call with MPEE OD |
| **Nothing standard installed** | → Rollout preparation, not integration | Bring: the urgent need and use case, a Machine List, a Use Case List, and calculated benefits |
| **Ordering a new machine** | → *Electrical Standard — Equipment Integration Extension* in Compliance Quest | Not an integration path at all |

Specifying connectivity at purchase is the cheapest integration there is. The new-machine
branch exists so a machine never arrives without the clauses that make it connectable. Route
a purchase question here, not into the PLC tree.

### Edge device hardware — a live constraint

`rules.json` answers both the **medium** and **small** edge device with the same warning:

> *There is no approved small edge device available; go with the large edge device or with
> a low-frequency data-collection method.*

So the hardware branch has exactly two live options — **large device**, or **low-frequency
collection**. Anyone planning a wave around medium or small devices is planning around
hardware that does not exist yet. Confirm current status with the IIAE before quoting it;
this is the kind of line that changes without the tree changing.

---

## Gate 1 — PLC family → available variants

The question at this gate is **not** "which platform" — the edge is the terminus in all three
shapes. It is:

> **Which of ①, ② or ③ reaches this PLC?**

① and ③ are both used at scale for Siemens and Rockwell, and **eight plants have both**, so
this is a per-machine decision — not a vendor policy and not a plant policy. ② has one
deployment and no written route; treat it as an IIAE conversation rather than a column in the
table below.

| PLC family | Sub-choice | ① edge device | ③ via aggregation server | Notes on choosing |
|---|---|---|---|---|
| **Siemens** | S7 (300/400/1200/1500) | ✅ | ✅ | Both fully documented. Aggregation avoids cabinet work; edge avoids a server dependency |
| | S7 Net / low frequency | ✅ | — | The low-frequency answer to "no approved small edge device" |
| | TIA | ✅ | ✅ | On Softing use protocol **Siemens S7-2** — S7-1200/1500 **only**, and the one protocol with per-connection advanced settings |
| | S5 | — | driver exists | dataFEED has a full S5 driver and syntax; the OESL tree does not route it. `rules-next` adds an S5 question |
| **Siemens NCU** | Sinumerik 840D / 840 UDP | ✅ | ✅ *(next)* | Dedicated connector on the edge side |
| | Sinuvars | ✅ | ✅ *(next)* | Edge only in the live tree |
| **Beckhoff** | — | ⚠️ `TODO` | ❌ **no driver** | **Neither route works as written.** dataFEED has no Beckhoff/ADS data source; the edge body is unwritten. Reach it via Modbus TCP, or a TwinCAT OPC UA / OPC DA server. IIAE question |
| **B&R** | INA2000 / Automation PC | — | ✅ **in use** | `DTQ-B&R-Connector` is **Idea · NOT AVAILABLE**, so there is no edge route. 30 of 32 B&R machines are integrated via the aggregation server today; dataFEED has a B&R driver. The written body is still `TODO`, but the route is real |
| **Bachmann** | MX213 / MX220 | — | ✅ **in use** | `DTQ-Bachmann-Connector` is **Idea · NOT AVAILABLE**. 44 of 63 machines integrated; reached over OPC UA. 24 rows carry the vendor `Bachmann OPC`, which is the same fleet named differently |
| **Omron** | NJ / CJ | ⚠️ `TODO` | ✅ *(next)* | Edge body is a task stub, no procedure |
| **Rockwell / Allen Bradley** | CLX · SLC / PLC-5 | ✅ | ✅ | Aggregation procedure is fully written in `rules-next` |
| **Modbus** | TCP / RTU | ⚠️ `TODO` | ✅ | **Aggregation is the documented route.** Also the practical route for a Beckhoff or Wago PLC that speaks Modbus TCP |
| **Mitsubishi** | Melsec-Q | — | ✅ (task list only) | Aggregation only |
| **OPC-UA server** already present | — | ✅ **this is the bridge** | ✅ *(next)* | Cheapest path in the tree — see above |
| **Anything else** | — | by exception | — | → *Integration of Other PLCs*: connector development, long lead times |

⚠️ `TODO` means the guide has the branch but not the procedure. **Do not compose one.**
Route it to the IIAE and say which branch is unwritten.

### The three variants, and the bridge

All three end at the IIoT Edge Platform — it is the terminus, and the data platform is
reached only through it. The department numbers the three shapes itself, in the Tool Overview:

```text
 ①  PLC ──► edge device ──(connector)──►  IIoT ──MQTT──► Node-RED ──► data platform
                                        Platform          Concept 3, 20 plants
 ②  PLC ──────(connector)─────────────►  IIoT
                                        Platform          Concept 2, 1 plant (Carei)
 ③  PLC ──► OPC-UA aggregation server ─►  IIoT
            (Softing dataFEED)  OPC UA   Platform          Concept 1, 11 plants
            └ DTQ-OPCUA-Connector ┘
```

① and ② differ in where the connector runs — on a dedicated edge device at the machine, or
without one. ③ puts a protocol concentrator in front, and the link back to the edge is the
`DTQ-OPCUA-Connector`.

② is barely deployed — one plant, and no written route in the guide. If a machine looks
like a ② candidate, that is an IIAE conversation. The estate's *"Low Cost — Direct
Connection"* (50 machines) and *"Low Cost — Helmholz"* (19) approaches are what ② looks like
in the field; the "low cost" is the absence of edge-device hardware.

The guide's recommendation for the second case is `IIoT Edge Platform → OPC-UA Server`,
reached when the plant has the edge platform and the PLC type is *OPC-UA Server*. Its eight
tasks are the bridge itself: machines connected to the Softing server, endpoint details (IP,
credentials, certificates), the server's address-space structure known, the edge installed
with all endpoints known, *"establish the connection between the OPC-UA Aggregation Server
and the IIoT Edge Platform"*, OT cyber-security rules, inform MPEE OD.

If the machine is already on an OPC-UA server, that is the whole procedure — no PLC
program, no tag export, no cabinet work. **Always ask whether an OPC-UA server already fronts
the machine before entering the PLC branch.** It is the single largest cost difference in
this tree and it is easy to skip past.

> **The aggregation path needs both pieces.** The guide states it in the Siemens S7
> aggregation recommendation: you cannot connect the PLCs *"when you have chosen the OPC-UA
> server as the connectivity framework **and you don't have the IIoT Edge Computing Platform
> available**"*. A Softing server with no edge platform behind it delivers nothing onward.

---

## Gate 2 — Which connector

The connector is the driver that actually reaches the machine. A connector reaches a
machine; a **tool** is a system a plant uses; they are never the same row.

### Edge platform — DATATRONiQ connectors

Full catalogue, with availability and container images, in
[`connectors.md`](connectors.md). Seven of the twenty-six cannot be used, so check
availability before naming one.

`DTQ-OPCUA-Connector` (Productive · USE) is not like the other connectors. Every other
connector reaches a *machine* by speaking its PLC's protocol; this one reaches an OPC UA
server and does not care what is behind it. That is two jobs in one container:

- **Direct** (topology ②) — the machine's own embedded OPC UA server.
- **Bridge** (topology ③) — the Central Aggregation Server, which has already collected many
  machines.

It is also the standing fallback wherever a native connector does not exist, which is how
most of the B&R and Bachmann estate is integrated today.

| Connector | Reaches | Via | Available? |
|---|---|---|---|
| **DTQ-OPCUA-Connector** | **Any OPC UA server — a machine's own, or the Aggregation Server** | **OPC-UA** | ✅ |
| DTQ-S7-Connector | Siemens S7-300 / S7-400 | PROFINET IO | ✅ |
| DTQ-TIA-Connector | Siemens S7-1200 / S7-1500 | ⟨not recorded⟩ | ✅ |
| DTQ-S7-NET-Connector | Siemens S7, low frequency | ⟨not recorded⟩ | ✅ |
| DTQ-SINUMERIK-Connector | Sinumerik NCU | UDP/IP | ✅ |
| DTQ-SINUVARS-Connector | Sinuvars | TCP/IP | ✅ |
| DTQ-SIMOTIOND-Connectors | Simotion D | ⟨not recorded⟩ | ✅ |
| DTQ-Beckhoff-Connector | Beckhoff | ADS | ✅ |
| DTQ-ALLENBRADLEY-ROCKWELL-Connector | Rockwell | ⟨not recorded⟩ | ✅ |
| DTQ-OMRON FINS-Connector | Omron | OMRON FINS | ✅ |
| DTQ-EthercatIO-Connector | EtherCAT I/O | ⟨not recorded⟩ | ✅ |
| DTQ-RS232-Connector | Serial — Keyence TM-3000 | RS232 | ✅ |
| DTQ-MODBUS-Connector | Modbus device | Modbus TCP | ⚠️ `Idea` but marked `USE` — confirm with the IIAE |
| DTQ-B&R-Connector | B&R | ⟨not recorded⟩ | ❌ **NOT AVAILABLE** — use OPC UA |
| DTQ-Bachmann-Connector | Bachmann | ⟨not recorded⟩ | ❌ **NOT AVAILABLE** — use OPC UA |

### Edge platform — non-PLC connectors

These need no PLC program. If the "machine" really exposes a file, an image or a web
service, one of these is the route and the whole PLC branch is irrelevant.

| Connector | Reaches | Via | Available? |
|---|---|---|---|
| DTQ-FTP2MIL-Connector | File drop, Cognex cameras | FTP → direct S3 | ✅ |
| DTQ-KEYENCECAM-Connector | Custom Keyence camera | FTP | ✅ |
| DTQ-IROPTRIS-Connector | Optris IR camera | ⟨not recorded⟩ | ✅ |
| DTQ-PIOVAN-Connector | Piovan drying systems | SOAP | ✅ |
| DTQ-Multicon CMC131-Connector | Multicon controller | HTTP(S) | ✅ |
| DTQ-Engel EMI-Connector | Engel injection moulding | Engel-specific | ❌ **NOT AVAILABLE** |
| DTQ-ZWICK-Connector | Zwick testing machine | ⟨not recorded⟩ | ❌ **NOT AVAILABLE** |
| DTQ-SMB-Connector | Windows file share | SMB → direct S3 | ❌ **NOT AVAILABLE** (in development) |
| DTQ-SmartKlaus-Connector | SmartKlaus | ⟨not recorded⟩ | ❌ **NOT AVAILABLE** (in development) |

Where a vendor-specific connector exists *and is available*, use it rather than reaching
the vendor's PLC generically. Piovan, Keyence, Optris and Multicon qualify. Engel and Zwick
do not — 38 Engel machines have no vendor connector, so check what the controller exposes;
current Engel controllers serve OPC UA.

### Aggregation server — Softing connectors

| Connector | Reaches | Available? |
|---|---|---|
| SFT-OPC-Suite | The dataFEED OPC Suite itself, aggregating all its data sources | ✅ Productive · USE |
| SFT-SIMATIC S7-Connector | Siemens SIMATIC S7-300/400, from the Softing server | ❌ **DO NOT USE** |

`SFT-SIMATIC S7-Connector` is forbidden. The Overview records why: it is not developed
cloud-native, and it *"still does not support CYBER SECURITY compliant communication to the
PLC."* The second reason ends the conversation — that is a security position, not a
preference, and it is not waived because a project is in a hurry. For S7-300/400 on the edge
the route is `DTQ-S7-Connector`. The restriction is on Softing's edgeConnector container,
not on the dataFEED OPC Suite aggregation server, which is a different product on a different
path.

These two are the *server* side of the concentrator. The *edge* side of the same link is
`DTQ-OPCUA-Connector`. A machine on this path is reached by two connectors in series, and
both belong in its Machine List row.

Softing's driver set is broader than these two rows suggest. From the V5.70 manual the
data sources are: Siemens (S7 · S7-2 · S5 · Send/Receive) · SINUMERIK CNC · Modbus ·
Rockwell · B&R · Mitsubishi · FANUC CNC · OPC UA Server · OPC Server (Classic) · OPC
Classic Tunnel Server · database read (ODBC) · MQTT Broker · MQTT Publisher · file read ·
local datapoints.

**No Beckhoff. No ADS.** Five of the rest — FANUC, database read, MQTT as a source, file
read, OPC Classic — have no OESL route. A product capability is not an approved route:
put the case to the IIAE, and if adopted it becomes a change to `rules.json`. Each PLC
family also needs its own licence (`dataFEED OPC Server Siemens / CNC / Rockwell /
Mitsubishi / Modbus / B&R`) unless Suite Extended is in place — check that before promising
a route.

Input protocol is unrecorded on 11 of the 26 connector rows. That is the export's state,
not a claim that the connector is protocol-free — confirm before quoting one.

---

## Gate 3 — The preparation gates, in the order they bite

Every route runs the same five blocks. They fail in a predictable order.

```text
1. Budget           ── edge device + OT hardware; IT infrastructure and licences
       ↓ fails → wave slips; nothing technical is wrong
2. Infrastructure   ── cabling; power; IP address assigned by IT
       ↓ fails → OT/IT work order, not an integration task
3. PLC program      ── breakpoint: entire program, .S7P for Siemens
       ↓ fails → see fallbacks.md — the most common integration killer
4. Tags             ── export from the program, record in Machine CV
       ↓ fails → cannot define items; connection may still come up and carry nothing
5. Cyber security   ── OT sign-off per the Connext Wiki rules
       ↓ fails → the machine waits. There is no expedited path
```

Gate 3, quoted verbatim from the guide:

> *"In case you do not have the PLC program or you did not request the PLC program / you did
> not receive the PLC program, we CAN NOT connect the PLC!"*

Raise it at the first conversation, not at the integration date. Asking a machine supplier
for a PLC program has a lead time measured in weeks and sometimes a commercial negotiation.

Note the asymmetry: the aggregation path still needs the PLC program for a PLC data source
(it is how tags are derived) but needs no cabinet work and no edge device. The
OPC-UA-server-already-present route needs neither.

---

## Gate 4 — Record and hand on

Same for every route:

1. **Machine List** — machine name, PLC IP, communication protocols, PLC type, PLC program.
   This is the record, not a form filled in afterwards.
2. **Machine CV** — the PLC program and the tag list, split into **mandatory** and
   **optional** tags.
3. **Edge Device List** — edge routes only.
4. **Inform MPEE Operations Digitalization.**
5. Integration status moves to `INTEGRATED` **only after the acceptance test passes** —
   `od-acceptance-test`.
6. Then `od-signal-standardization`, then `od-node-red-flow-builder`.

---

## Where the tree is going

`rules-next.json` completes the aggregation column (Rockwell, Omron NJ/CJ, Sinuvars,
Sinumerik), adds **camera systems** and **remote sensors** as endpoint classes, and adds
questions the current tree does not ask: data acquisition, data buffering, local
dashboarding / HMI, rule-engine transformation, analytics use cases, PLC hardware and
software standardization, process complexity, process maturity, strategic priorities.

That is a shift from *how do I connect this* to *should I, and to what end*. One answer in
it is already decisive:

> **Camera systems cannot be connected to any Central Aggregation Server.** Cameras are an
> edge-only endpoint class.

---

## A worked routing, end to end

*"We need cycle time off an S7-300 at a plant that has the aggregation server but no edge
devices. The machine builder is gone and nobody can find the PLC program."*

**Gate 0.** Softing server present, no edge devices. The aggregation path concentrates the
PLCs but still has to be bridged into the IIoT Edge Platform with `DTQ-OPCUA-Connector`, so
an edge device is needed somewhere — just not in this machine's cabinet. That is a budget
and lead-time conversation before anything else.

**The cheap question.** Is the machine already on the OPC UA server? No — it is not
connected at all. So the PLC branch it is.

**Gate 1.** Siemens → S7. Both platforms support it; only one is available. → Softing,
`Data Sources → Siemens`, application protocol **Siemens S7**. (Not S7-2: that is
S7-1200/1500 only. Not NetLink: discontinued in V5.38.)

**Gate 3, and it stops here.** No PLC program → the breakpoint. Before recording the
machine as blocked, work [`fallbacks.md`](fallbacks.md) §1:

1. Already on an OPC UA server? No.
2. Vendor-specific connector? Not applicable to a generic S7.
3. Writes a file? Worth checking — many older lines drop a shift log to a share, and
   `DTQ-SMB-Connector` needs no program. It runs on the edge, which this plant has to stand
   up regardless.
4. HTTP/SOAP? No.
5. Serial? No.
6. Is cycle time available on a neighbouring PLC? The line PLC may already count parts —
   the estate records exactly this pattern for robot signals on 5 machines. Check this
   before anything else, since it costs a conversation rather than a procurement.
7. Add a sensor instead? A part-present sensor into a remote-sensor endpoint would give
   cycle time without touching the machine at all — but again needs the edge.

**The honest answer**, if 3 and 6 come back negative: the machine is blocked pending the PLC
program, the supplier request goes out today, and the machine is recorded in the Machine
List with that blocker and its owner. Meanwhile the *use case* may still be servable from
the neighbouring PLC — which is a different machine, a different route, and a conversation
worth having before anyone waits three months.

The tree is short, the fallbacks are where the work is, and the answer that unblocks a use
case is often a different machine rather than a harder attempt at this one.
