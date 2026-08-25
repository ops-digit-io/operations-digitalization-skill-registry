# The equipment integration decision tree

The tree that the Equipment integration guide walks
(`_apps/machine-integration-guidance-app/rules.json` — 25 questions, 27 recommendations).
The rules are **data**: the tree changes without touching the app, so this file is a
readable snapshot, not a second implementation. `rules.json` is authoritative.

## Question graph

```
preconditions
├─ IIoT Edge Platform ─────────────────────────────► plc_type
├─ IIoT Edge Platform — Edge Device Hardware
│  Installation ───────────────────────────────────► edge_device_hardware_installation
│                                                     ├─ Large Edge Device   → recommendation
│                                                     ├─ Medium Edge Device  → recommendation
│                                                     └─ Small Edge Device   → recommendation
├─ Central Aggregation Server
│  (Softing DataFEED; legacy: Kepware) ────────────► plc_type
└─ "I want to order a new machine and I need a
    Standard Document" ───────────────────────────► recommendation (requirement spec)

plc_type
├─ Siemens PLCs ──────────► siemens_plcs ├─ Siemens S7                  → siemens_s7
│                                        ├─ Siemens S7 Net / low freq   → siemens_s7_net_low_freq   [edge only]
│                                        └─ Siemens TIA                 → siemens_tia
├─ Siemens NCUs ──────────► siemens_ncus ├─ Sinuvars                    → sinuvars                  [edge only]
│                                        └─ Sinumerik 840D / 840 UDP    → sinumerik_ncu
├─ Beckhoff ──────────────► beckhoff                                    (confirm Yes/No)
├─ B&R PLCs ──────────────► b_r_plcs                                    (INA2000)
├─ Omron ─────────────────► omron_plcs   ├─ Omron NJ  └─ Omron CJ        [edge only in rules.json]
├─ Rockwell / Allen Bradley ► rockwell_allen_bradley_plcs ├─ CLX  └─ SLC / PLC-5
├─ OPC-UA Server ─────────► (direct recommendation)
├─ Modbus PLC ────────────► modbus                                      (confirm Yes/No)
├─ Mitsubishi PLC ────────► mitsubishi_plcs                             (Melsec-Q)
└─ Other PLC ─────────────► others_plc                                  [edge only, by exception]
```

Every leaf question is a **confirmation** (`Yes` / `No`) before a recommendation is
emitted. That is deliberate: it forces the answerer to state the PLC family out loud
before receiving a procedure written for it.

## Recommendations present in `rules.json`

**IIoT Edge Platform:** Siemens S7 · Siemens TIA · Sinuvars · Sinumerik 840D / 840 UDP NCU ·
Beckhoff *(body marked `TODO`)* · Omron NJ · Omron CJ · Rockwell CLX · Rockwell SLC / PLC-5 ·
OPC-UA Server · Modbus *(body marked `TODO`)*

**Central OPC-UA Aggregation Server:** Siemens S7 · Siemens TIA · Beckhoff · B&R INA2000 ·
Rockwell CLX · Rockwell SLC / PLC-5 · OPC-UA Server *(`TODO`)* · Modbus · Mitsubishi Melsec-Q

**Other:** Integration of Other PLCs · order-a-new-machine standard document ·
large / medium / small edge-device hardware installation · two "no standard systems
installed" rollout-precondition paths

**Three recommendation bodies are `TODO`** — Beckhoff on edge, Modbus on edge, OPC-UA on
the aggregation server. Route the question to the IIAE. Do not compose a procedure for a
branch the guide has not written.

## The standard checklist inside an edge-platform recommendation

Every edge route repeats the same five blocks. Quoting the Siemens S7 recommendation,
which is the fullest:

**Process valid for:** BROWNFIELD · GREENFIELD

**Budget planning**
- Budget for the edge device plus other OT devices (switches, cabling, …)
- Budget for IT infrastructure (software subscriptions, cabling from edge device to OT switch)
- Use the available budget planning template

**Infrastructure preconditions**
- IT infrastructure, especially cabling, available
- Power supply for the edge device available — check the device datasheet

**PLC / machine-specific preparation**
1. Machine details (interfaces, PLC types, other endpoints such as HMIs) provided in the **Machine List**
2. A machine-specific **integration plan** — network diagram with endpoints, protocols, connections
3. **PLC programs available in an appropriate format** — the entire program including an `.S7P` file
4. If unavailable, request the PLC program from the machine supplier
5. > *"In case you do not have the PLC program or you did not request the PLC program / you did not receive the PLC program, we CAN NOT connect the PLC!"*
6. Capability to **adjust the PLC program** — implement function block, adjust hardware configuration
7. Upload the PLC program in the **Machine CV**
8. **Export the tags** based on the PLC program using the available export tools
9. Provide **IP address and connection details** for the PLC
10. Add edge-device details to the **Edge Device List**

**IT-specific tasks**
- Provide an IP address for the edge device
- Configure that IP on the edge device at **ETH1**

**PLC / machine-specific tasks**
- Connect the PLC to the edge device (per the linked documentation)
- Mount the edge device in the machine cabinet, 24 V power to the edge device

## The OPC-UA aggregation route differs

**Process valid for:** BROWNFIELD only.

- Budget for OT devices (connectors, e.g. Helmholz NetLink; switches; cabling) and IT infrastructure
- Machines already connected to the **OPC-UA server (Softing DataFEED OPC Suite)**
- Connection details for the server endpoint: IP addresses, credentials, certificates
- The server's **structure known** for the integrated machines
- IIoT Edge Platform installed and all endpoints known
- Establish the OPC-UA ↔ IIoT Edge connection per the linked instructions
- Endpoints connected according to **OT Cyber Security rules**
- **Inform the MPEE Operations Digitalization team**

Note what is absent: no PLC program, no tag export, no cabinet work. Where a machine is
already on the aggregation server, this route is dramatically cheaper — which is why the
first question is about installed systems, not about the PLC.

## What `rules-next.json` adds

A newer tree beside the live one: **35 questions, 31 recommendations**. Not live — use
`rules.json` for an answer today, and read this as direction.

**New endpoint classes:** camera systems and remote sensors, on both platforms.

**Completed routes on the aggregation server:** Rockwell / Allen Bradley (merged into one),
Omron NJ, Omron CJ, Sinuvars, Sinumerik 840D / 840 UDP NCU.

**New assessment questions** — the tree stops being purely about connectivity and starts
asking what the connection is *for*: `data_acquisition` · `data_buffering` ·
`local_dashboarding_hmi` · `rule_engine_transformation` · `analytics_use_cases` ·
`plc_hardware_standardization` · `plc_software_standardization` · `process_complexity` ·
`process_maturity` · `strategic_priorities` · `standard_systems_installed` · `siemens_s5`.

That shift matters: it turns the guide from *how do I connect this* into *should I, and to
what end* — which is the question the department's own portfolio findings say is missing.
