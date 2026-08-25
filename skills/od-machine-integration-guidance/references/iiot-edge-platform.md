# Pattern — IIoT Edge Computing Platform

The edge pattern: a DATATRONiQ edge device sits in or beside the machine cabinet, speaks
the PLC's protocol through a connector, and publishes to the platform. The cost sits in
hardware, cabinet work and a shopfloor network drop — and in exchange there is no shared
server that every machine depends on.

**Valid for BROWNFIELD and GREENFIELD** — the only OESL route that covers new machines.

Pairs with [`decision-paths.md`](decision-paths.md) for routing and
[`fallbacks.md`](fallbacks.md) when a step blocks.

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

   > ★ **BREAKPOINT — quoted verbatim:** *"In case you do not have the PLC program or you
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

`ETH1` is specific and worth repeating: the edge device has more than one interface and the
shopfloor-facing address goes on ETH1.

## Phase 5 — Machine tasks

- **Connect the PLC to the edge device**, per the linked documentation.
- **Mount the edge device in the machine cabinet**, 24 V to the device.

## Phase 6 — Hardware installation, in full

The dedicated hardware branch spells out the order, and the order matters — the DATATRONiQ
registration steps come after the network is up, not before:

1. Mount the edge device into the machine cabinet.
2. Supply **24 V** power.
3. Connect **shopfloor Ethernet** from the edge device to the **central access switch**.
4. Obtain the **IP address from local IT**.
5. Configure the IP on **ETH1**.
6. **Set up the edge device in the DATATRONiQ dashboard.**
7. **Connect the edge device to the PLC** (e.g. Siemens S7-300/400).
8. Follow the **PLC-type-specific** integration steps.
9. **Incorporate the edge device into the DATATRONiQ server cluster.**

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
| **Low-frequency collection** | Where a large device cannot be justified or does not fit — on Siemens this is the **S7 Net / low-frequency** route and its `DTQ-S7-NET-Connector` |

Plan a wave against these two. Anything sized around a medium or small device is sized
against hardware that is not approved. ⟨Confirm current device approval status with the
IIAE — this is the kind of line that changes without the tree changing.⟩

---

## The three integration concepts

The edge platform is one of three concepts recorded as tools in their own right:

| Concept | Shape | Choose when |
|---|---|---|
| **IIoT edge computing platform** | Device per machine or cell, connector per protocol | Greenfield; no aggregation server; camera and sensor endpoints; where a shared-server dependency is unwanted |
| **Central OPC-UA server** | One server, driver connections, one address space | Brownfield at density; no cabinet work possible; machine already speaks OPC-UA — see [`softing-datafeed.md`](softing-datafeed.md) |
| **Container-based machine integration** | Containerised connector | ⟨Route not written up in the guide — IIAE question⟩ |

The third is recorded in the estate as a concept but the Equipment integration guide does
not route to it. Do not invent the procedure; ask.

---

## Connecting an existing OPC-UA server to the edge — the short path

When the machines are **already** on an OPC-UA server, the edge route collapses to eight
tasks and no cabinet work:

1. Machine details in the Machine List.
2. Machines confirmed connected to the OPC-UA server (Softing dataFEED OPC Suite).
3. **Endpoint connection details** available — IP addresses, credentials, certificates.
4. The server's **address-space structure** known, for the machines in question.
5. IIoT Edge Platform installed and all endpoints known.
6. Establish the OPC-UA ↔ edge connection per the linked instruction.
7. Endpoints connected per **OT cyber-security rules** (Connext Wiki).
8. **Inform MPEE Operations Digitalization.**

Note what is absent: no PLC program, no tag export, no `.S7P`, no mounting, no 24 V.
**Always test for this case before entering the PLC branch** — it is the largest single
cost difference available in the guide.

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

**None of these hit the PLC-program breakpoint.** When a machine's PLC program is
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
| No cabinet space or no 24 V | Low-frequency collection, or the aggregation route if a server exists |
| Legacy PLC, **no protocol** in the connector set | *Integration of Other PLCs* — connector development, long OT/IT cyber-security lead times. Name the dependent use cases |
| Device cabled but reporting nothing | Check dashboard registration (step 6) and cluster membership (step 9) before suspecting the PLC |
| Cyber-security sign-off missing | The machine waits. No expedited path |
