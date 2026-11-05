---
type: Skill Reference
title: IIoT edge platform
description: "The edge pattern: a DATATRONiQ edge device in the machine cabinet, what it speaks, and where its data lands."
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [integration, edge, iiot]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
# Pattern — IIoT Edge Computing Platform

The edge pattern: a DATATRONiQ edge device sits in or beside the machine cabinet, speaks
the PLC's protocol through a connector, and publishes to the platform. The cost sits in
hardware, cabinet work and a shopfloor network drop — and in exchange there is no shared
server that every machine depends on.

**Valid for BROWNFIELD and GREENFIELD** — the only OESL route that covers new machines.

Pairs with [`decision-paths.md`](decision-paths.md) for routing and
[`fallbacks.md`](fallbacks.md) when a step blocks. The other route is
[`softing-datafeed.md`](softing-datafeed.md).

## What "the platform" actually is

Three things travel under one name, and confusing them causes most of the
cross-conversation friction on this route:

| Layer | What it is | Where it appears |
|---|---|---|
| **Edge device** | The hardware in or beside the machine cabinet. Currently one approved size | Edge Device List; the hardware branch of the guide |
| **Connector** | The protocol driver reaching the PLC — 26 of them, 24 DATATRONiQ, 2 Softing | Connector Overview list; [`decision-paths.md`](decision-paths.md) |
| **Platform** | The DATATRONiQ dashboard and server cluster the devices register into, on the plant Kubernetes runtime | Steps 6 and 9 of the hardware sequence |

A machine is integrated only when all three are done. Cabled and addressed but not
registered in the dashboard and not in the cluster is a device that reports nothing and
looks, from the cabinet, entirely healthy.

**Where the connector name surfaces later:** the driver family becomes a segment of the MQTT
topic the platform publishes on — `datatroniq/data/protob/plc/<edge-device>/<driver>/<id>`,
with `<driver>` observed across the estate as `dqcdc`, `cifx`, `tia`, `ads`, `abrock`. The
connector chosen here is visible in every Node-RED flow downstream, and the edge device name
chosen at registration is the `<edge-device>` segment. See `od-node-red-flow-builder`.

---

## Phase 1 — Budget

| Item | Note |
|---|---|
| Edge device | Only the **large** device is approved today |
| Other OT hardware | Switches, cabling, and any gateway (e.g. Helmholz NetLink) |
| IT infrastructure | Software subscriptions; cabling from the edge device to the OT switch |
| Template | Use the budget planning template — ask MPEE OD if you do not have it |

Budget is listed first in every recommendation for a reason: it is the block that slips a
wave without anything being technically wrong.

## Phase 2 — Infrastructure preconditions

- IT infrastructure, **especially cabling**, available.
- **Power supply** for the edge device confirmed — check the device datasheet, do not
  assume 24 V is spare in that cabinet.

## Phase 3 — PLC / machine preparation — the breakpoint block

This is the block that decides whether the integration happens at all.

1. **Machine details in the Machine List** — interfaces, PLC types, and other endpoints
   such as HMIs. Not just the PLC.
2. **A machine-specific integration plan** — a network diagram with endpoints, protocols
   and connections. One per machine, not one per plant.
3. **The PLC program**, entire, in an appropriate format — including the **`.S7P`** for
   Siemens.
4. If it is not available, **request it from the machine supplier** — start this early,
   lead times are weeks and it is sometimes a commercial conversation.

   > **Breakpoint, quoted verbatim:** *"In case you do not have the PLC program or you
   > did not request the PLC program / you did not receive the PLC program, we CAN NOT
   > connect the PLC!"*

5. **The capability to adjust the PLC program** — implement the function block, adjust the
   hardware configuration. Having the program is not enough; somebody must be able to
   change and redeploy it, which usually means a maintenance window.
6. **Upload the PLC program to the Machine CV.**
7. **Export the tags** from the program using the available export tools.
8. **Provide the PLC IP address and connection details.**
9. **Add the edge device to the Edge Device List.**

Steps 5 and 6 are the ones that get skipped. Step 5 because it is a scheduling problem
rather than a document; step 6 because the program is already "somewhere". Both surface
later as an integration that cannot be reproduced by anyone but the person who did it.

## Phase 4 — IT tasks

- Provide an **IP address** for the edge device.
- Configure that address on **ETH1**.

`ETH1` matters: the edge device has more than one interface and the shopfloor-facing address
goes on ETH1.

## Phase 5 — Machine tasks

- **Connect the PLC to the edge device**, per the linked documentation.
- **Mount the edge device in the machine cabinet**, 24 V to the device.

## Phase 6 — Hardware installation, in full

The dedicated hardware branch spells out the order, and the order matters — the DATATRONiQ
registration steps come after the network is up, not before:

1. Mount the edge device into the machine cabinet.
2. Supply **24 V** power.
3. Connect shopfloor Ethernet from the edge device to the central access switch.
4. Obtain the IP address from local IT.
5. Configure the IP on ETH1.
6. Set up the edge device in the DATATRONiQ dashboard.
7. Connect the edge device to the PLC (e.g. Siemens S7-300/400).
8. Follow the PLC-type-specific integration steps.
9. Incorporate the edge device into the DATATRONiQ server cluster.

Steps 6 and 9 are the platform-side registration. A device that is cabled, powered and
addressed but not in the dashboard and not in the cluster is a device that will report
nothing and look, from the cabinet, entirely healthy.

### Device sizing — one live option

`rules.json` answers **both** the medium and the small edge device with the same warning:

> *There is no approved small edge device available; go with the large edge device or with
> a low-frequency data-collection method.*

So the two live options are:

| Option | When |
|---|---|
| **Large edge device** | Default, and currently the only approved hardware |
| **Low-frequency collection** | Where a large device cannot be justified or does not fit — on Siemens this is the S7 Net / low-frequency route and its `DTQ-S7-NET-Connector` |

Plan a wave against these two. Anything sized around a medium or small device is sized
against hardware that is not approved. Confirmed still current with the IIAE, 2026-10-22 —
this is the kind of line that changes without the tree changing, so re-check it rather than
trusting the date.

---

## The three integration concepts = the three ingress variants

The knowledge graph records three integration concepts as tools in their own right, and the
department numbers them. They are exactly the three shapes a machine can take into the
platform:

| Concept (Tool Overview) | Variant | Shape | Plants |
|---|---|---|--:|
| **Concept 3 — IIoT Edge Computing Platform** | **①** | PLC → **edge device** with connector → IIoT platform. Device per machine or cell; the only variant for cameras | **20** |
| **Concept 2 — container-based Machine Integration** | **②** | PLC → **connector** → IIoT platform. The connector runs without a dedicated edge device at the machine | **1** (Carei) |
| **Concept 1 — Central OPC-UA Server** | **③** | PLC → **aggregation server** → IIoT platform. Softing dataFEED concentrates the drivers; the edge reads its address space — see [`softing-datafeed.md`](softing-datafeed.md) | **11** |

These are not three destinations. The IIoT Edge Platform is the terminus in all three;
① and ② differ only in *where the connector runs*, and ③ adds a concentrator in front,
bridged back by `DTQ-OPCUA-Connector` — see § *The bridge* above.

The term is ambiguous: "IIoT Edge Computing Platform" is both the name of Concept 3 (variant
①, *use an edge device*) and the name of the platform that terminates all three. When
somebody says "we're on the edge platform" they may mean either — ask which.

Similarly, "central OPC-UA server" (Concept 1, as the department names it) and "Central
Aggregation Server" (as the guide labels the route) are the same thing seen from two sides.
Prefer the guide's wording when handing someone a procedure — it is the label on their
screen.

### Variant ② — real, and barely deployed

Concept 2 is recorded at **one plant, Carei**, which also runs ①. The Equipment integration
guide has **no written route for it**. That combination — a live concept with a single
deployment and no procedure — means: do not offer ② as a standard option, and do not invent
the procedure. If a machine looks like a ② candidate, it is an IIAE conversation.

What ② looks like in the field is visible in the estate's `integration_approach` values:
**"Low Cost — Direct Connection"** (50 machines) and **"Low Cost — Helmholz"** (19), alongside
bare protocol entries like "TCP/IP Ethernet driver" (30). The *low cost* is precisely the
absence of edge-device hardware.

**Both rows are Concept ②, confirmed with the IIAE.** A Helmholz gateway is hardware at the
machine, but it does not count as an **edge device** in the department's sense — "edge
device" means the DATATRONiQ hardware that runs a connector under Concept ①/③. A protocol
gateway in front of a PLC with no Ethernet of its own is a different thing, and it does not
move a machine out of ②.

### Which variants a plant has

Not one per plant. Of the 23 plants with any concept recorded:

| | Plants |
|---|--:|
| ① only | 11 — Auburn, Delicias, Dolne Vestenice, Hann. Münden, Karben, Monterrey, Northeim, San Luis Potosi, Subotica, Timisoara, Vac |
| ③ only | 3 — Ostrava, Ponta Grossa, Sun Prairie |
| **① and ③ both** | **8** — Caluire, Changchun, Changshu, Korbach, Mako, Qingdao, Somersworth, Waltershausen |
| ② | 1 — Carei, alongside ① |

Eight plants carry both ① and ③, so *"which platform does this plant have"* is often the
wrong question. Ten of the 33 plants have no concept recorded at all — there the first
conversation is rollout, not integration.

## Choosing between the two, when both are open

Gate 0 usually settles this — a plant has one platform, not both. Where both are genuinely
available:

All three end at the edge — this is a choice of *how the PLC reaches it*, not of
destination. ② is excluded here because it has no written route.

| Favours **①** — an edge device | Favours **③** — via the aggregation server |
|---|---|
| Greenfield machine, or a new machine being ordered | Brownfield, at density — many machines at one site |
| Camera, remote sensor, file drop or vendor-specific endpoint | Machine already fronted by an OPC UA server |
| Cabinet space and 24 V available | No cabinet work possible or permitted |
| A shared failure domain is unacceptable — one device, one machine | Cabinet access is the expensive part, not the licence |
| The driver exists as a DTQ connector but not as a dataFEED data source — **Beckhoff / ADS is exactly this** | The driver exists in dataFEED but the edge branch is unwritten — **Modbus is exactly this** |

That last row cuts both ways: neither platform covers everything, and for some machines the
honest answer is that no route is fully written. Say that rather than forcing one.

Failure domains differ between the two routes. An edge device failing takes one machine off
— or one cell, where a device is shared, and the estate does record shared devices (*"Edge
Device [Same as BM11 device] via Siemens TCP/IP Ethernet Driver"*, Beckhoff I/O clamps
daisy-chained into one device). An aggregation server failing takes every machine behind it
off at once, which is why its "operate" phase, cyclic-read budget and licence headroom
matter in a way ①'s do not. Where a device is shared, record it — the failure domain is no
longer one machine.

---

## The bridge — `DTQ-OPCUA-Connector`

All three ingress variants terminate at the IIoT Edge Platform: a machine reached by an edge
device (①), by a connector with no device (②), or through the Central Aggregation Server (③)
all arrive at the edge and leave on MQTT.

The link from the aggregation server is the `DTQ-OPCUA-Connector`, and it is the one
connector in the set that does not reach a machine — it reaches an OPC UA server:

```text
PLC ──Softing driver──► Central Aggregation Server ──OPC UA──► IIoT Edge ──MQTT──► Node-RED
                        (dataFEED OPC Suite)                     Platform
                        server side: SFT-OPC-Suite       edge side: DTQ-OPCUA-Connector
```

A machine on that path is reached by **two connectors in series** — the Softing driver on
the server and the OPC-UA connector on the edge — and both belong in its Machine List row.
The same connector also reaches a machine's own embedded UA server, which is why the guide
treats "OPC-UA Server" as a PLC type in its own right.

**The dependency runs both ways.** The aggregation path needs the edge platform, not just
the server: the guide's Siemens S7 aggregation recommendation says you cannot connect the
PLCs *"when you have chosen the OPC-UA server as the connectivity framework and you don't
have the IIoT Edge Computing Platform available"*. A Softing server with nothing behind it
delivers nothing onward.

## Connecting an existing OPC-UA server to the edge — the short path

This is the bridge procedure, and it is also what a machine with its own embedded UA server
takes. When the machines are **already** on an OPC-UA server, the route collapses to eight
tasks and no cabinet work:

1. Machine details in the Machine List.
2. Machines confirmed connected to the OPC-UA server (Softing dataFEED OPC Suite).
3. Endpoint connection details available — IP addresses, credentials, certificates.
4. The server's address-space structure known, for the machines in question.
5. IIoT Edge Platform installed and all endpoints known.
6. Establish the OPC-UA ↔ edge connection per the linked instruction.
7. Endpoints connected per OT cyber-security rules (Connext Wiki).
8. Inform MPEE Operations Digitalization.

Note what is absent: no PLC program, no tag export, no `.S7P`, no mounting, no 24 V.
**Always test for this case before entering the PLC branch** — it is the largest single
cost difference available in the guide.

Task 4 is the one that gets skipped and should not be. *"The structure on the OPC-UA Server
is clear and known"* means the address space is an interface: node ids are
`<connection name>.<tag name>`, so the connection names chosen on the Softing side are what
the edge subscribes to. Rename a connection later and every subscription breaks. See
[`softing-data-targets.md`](softing-data-targets.md).

The budget block still applies, and still names OT devices such as Helmholz NetLink,
switches and cabling: "already on an OPC-UA server" does not always mean "already reachable
from where the edge device sits".

---

## Endpoint classes beyond PLCs

The edge route reaches things the aggregation server cannot. From the connector set and
from `rules-next.json`:

| Endpoint | Route | PLC program needed |
|---|---|---|
| **Camera systems** | Edge **only** — explicitly *not connectable* to any aggregation server | No |
| **Remote sensors** | Edge or aggregation *(next tree)* | No |
| Keyence camera | `DTQ-KEYENCECAM-Connector`, FTP | No |
| File drop / share | `DTQ-FTP2MIL-Connector`, `DTQ-SMB-Connector` | No |
| Vendor systems — Engel, Piovan, Zwick, Optris, Multicon | Vendor-specific connector | No |
| Serial device | `DTQ-RS232-Connector` | Depends |

None of these hit the PLC-program breakpoint. When a machine's PLC program is
unavailable, the first question is whether the data is reachable another way — see
[`fallbacks.md`](fallbacks.md).

---

## Fallbacks specific to this pattern

| Situation | Do this |
|---|---|
| No edge device on site | Take the edge-device hardware branch first; it is a prerequisite, not part of the integration |
| Medium or small device planned | Not approved — large device, or low-frequency collection |
| **PLC program unavailable** | [`fallbacks.md`](fallbacks.md) — check the non-PLC routes before declaring it blocked |
| PLC program available, **nobody can modify it** | Blocked at step 5. This is a resourcing escalation, not an engineering one |
| No cabinet space or no 24 V | Low-frequency collection, or reach the PLC via the aggregation server and bridge it back with `DTQ-OPCUA-Connector` — the edge device is still needed, just not at the machine |
| Legacy PLC, **no protocol** in the connector set | *Integration of Other PLCs* — connector development, long OT/IT cyber-security lead times. Name the dependent use cases |
| Device cabled but reporting nothing | Check dashboard registration (step 6) and cluster membership (step 9) before suspecting the PLC |
| Cyber-security sign-off missing | The machine waits. No expedited path |
| **Beckhoff PLC** | The `DTQ-Beckhoff-Connector` (ADS) is the native path, but the edge recommendation body is `TODO` — and dataFEED has no Beckhoff driver at all, so the aggregation server is not a fallback here. Modbus TCP or a TwinCAT OPC UA server, else IIAE |
