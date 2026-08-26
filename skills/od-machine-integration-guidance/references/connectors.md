---
type: Skill Reference
title: Connectors
description: All 26 connectors with what each reaches, over which protocol, which PLCs, and - decisively - whether it is available at all.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [integration, connectors, opc-ua]
generated: { by: claude-code/1, at: 2026-08-26T00:00:00Z }
---

# Connectors

**Seven of the twenty-six cannot be used.** A connector appearing in the Overview is not a
route to data, and routing an engineer to one that does not exist costs a site visit. Every
table here carries availability, because that is the column that decides.

| | Count | Meaning |
|---|--:|---|
| `Productive` · `USE` | **18** | A real route today |
| `Idea` · `USE` | 1 | `DTQ-MODBUS-Connector` — the two fields disagree; see below |
| `Idea` · `NOT AVAILABLE` | 4 | Not started. A roadmap item, not a route |
| `Development` · `NOT AVAILABLE` | 2 | Being built. Not a route yet |
| `Productive` · `DO NOT USE` | 1 | Exists, works, and is forbidden — with a reason |

## The OPC UA direct connector

**`DTQ-OPCUA-Connector` — Productive, USE — is the one connector that is not like the
others.** Every other connector reaches a *machine* by speaking its PLC's own protocol. This
one reaches an **OPC UA server**, and it does not care what is behind it. That gives it two
completely different jobs:

| Job | Topology | What it talks to |
|---|---|---|
| **Direct** | ② PLC → connector → IIoT platform | The machine's **own embedded OPC UA server**, where the PLC has one |
| **Bridge** | ③ PLC → aggregation server → IIoT platform | The **Central OPC UA Aggregation Server** (`SFT-OPC-Suite`), which has already collected many machines |

`in: OPC-UA` → `out: MQTT`. The same container, the same configuration shape, two different
things on the other end. When somebody says "the machine is on OPC UA", ask which of the two
they mean — the Machine List row must name the aggregation server if there is one, because a
machine on the bridge path is reached by **two connectors in series** and both belong in the
row.

**It is also the standing fallback**, and this is the part most often missed: where a PLC has
no available native connector but does expose an OPC UA server, the OPC UA connector is the
route. That is not a workaround. It is how most of the B&R and Bachmann estate is integrated
today.

## Where the native connector does not exist

| PLC | Native connector | Its state | Machines | How they are actually integrated |
|---|---|---|--:|---|
| **B&R Industrial Automation** | `DTQ-B&R-Connector` | **Idea · NOT AVAILABLE** — *"Development to be started with Rollout in Dolne Vestenice"* | 32 (31 at Dolne Vestenice) | **29 INTEGRATED**, 30 of them via `Central OPCUA Aggregation Server` |
| **Bachmann Electronic** | `DTQ-Bachmann-Connector` | **Idea · NOT AVAILABLE** — same note | 63 (Northeim 24, Dolne Vestenice 20, Changshu 19) | **44 INTEGRATED**; 16 recorded as aggregation server, 47 with no method recorded |
| **Engel** | `DTQ-Engel EMI-Connector` | Idea · NOT AVAILABLE | 38 | Check per machine; Engel exposes OPC UA on current controllers |
| **Zwick** | `DTQ-ZWICK-Connector` | Idea · NOT AVAILABLE | — | No route today |
| **Windows file share** | `DTQ-SMB-Connector` | Development · NOT AVAILABLE | — | `DTQ-FTP2MIL-Connector` where the drop can be FTP |
| **SmartKlaus** | `DTQ-SmartKlaus-Connector` | Development · NOT AVAILABLE | — | No route today |

**The B&R and Bachmann rows are the lesson.** Both native connectors are unbuilt, and both
PLC families are largely integrated anyway — over OPC UA, through the aggregation server.
Reading "no connector" off the Overview and reporting a barrier would contradict 73 machines
that are already delivering data. Ask what the PLC *exposes* before concluding there is no
route.

24 machine rows carry the vendor `Bachmann OPC` rather than `Bachmann Electronic GmbH`, all
at Northeim, all with no protocol or method recorded. That is the same fleet described twice,
and it is why a vendor-string match alone is not a reliable way to find a machine's route.

## The one that is forbidden

**`SFT-SIMATIC S7-Connector` — Productive · DO NOT USE.** It works. It is not to be used, and
the Overview records why:

> 1. Softing Edge Connector is not developed cloud native — high time invest to make it run
>    with a wrapper around.
> 2. Softing Edge Connector **still does not support CYBER SECURITY compliant communication
>    to the PLC.**

The second reason is the one that ends the conversation: it is a security position, not a
preference, and it will not be waived because a project is in a hurry. For Siemens S7-300/400
on the edge, the route is `DTQ-S7-Connector`. Note that this restriction applies to Softing's
**edgeConnector** container, not to the dataFEED OPC Suite aggregation server (`SFT-OPC-Suite`,
Productive · USE), which is a different product on a different path.

## `DTQ-MODBUS-Connector` — the fields disagree

`status: Idea` and `utilization: USE`. Those cannot both be true, and the Overview offers no
tiebreaker; its only description is *"Default connector from the Edge Platform"*, which reads
like it ships with the platform rather than being developed for OESL. **Confirm with the IIAE
before promising a Modbus route**, and record the answer — 80 machines are on Modbus / TCP.

## The full catalogue

### PLC connectors — edge platform

| Connector | Reaches | Via | PLCs recorded | State | Image |
|---|---|---|---|---|---|
| **DTQ-OPCUA-Connector** | **Any OPC UA server: a machine's own, or the aggregation server** | **OPC-UA** | — | ✅ Productive · USE | — |
| DTQ-S7-Connector | Siemens S7 | PROFINET IO | S7-300, S7-400 | ✅ Productive · USE | `datatron-cifx` |
| DTQ-TIA-Connector | Siemens TIA | ⟨not recorded⟩ | S7-1200, S7-1500 | ✅ Productive · USE | `datatron-tia-collect` |
| DTQ-S7-NET-Connector | Siemens S7, low frequency | ⟨not recorded⟩ | — | ✅ Productive · USE | — |
| DTQ-SINUMERIK-Connector | Sinumerik NCU | UDP/IP | Siemens SINUMERIK | ✅ Productive · USE | `sinumerik-data-receiver` |
| DTQ-SINUVARS-Connector | Sinuvars | TCP/IP | — | ✅ Productive · USE | `datatron-sinuvars-collect` |
| DTQ-SIMOTIOND-Connectors | Simotion D | ⟨not recorded⟩ | — | ✅ Productive · USE | `datatron-simotion-collect` |
| DTQ-Beckhoff-Connector | Beckhoff | ADS | Beckhoff | ✅ Productive · USE | `datatron-ads-collect` |
| DTQ-ALLENBRADLEY-ROCKWELL-Connector | Rockwell / Allen-Bradley | ⟨not recorded⟩ | — | ✅ Productive · USE | `datatron-abrock-collect` |
| DTQ-OMRON FINS-Connector | Omron | OMRON FINS | OMRON FINS PLCs | ✅ Productive · USE | `datatron-omron-collect` |
| DTQ-EthercatIO-Connector | EtherCAT I/O | ⟨not recorded⟩ | — | ✅ Productive · USE | — |
| DTQ-MODBUS-Connector | Modbus device | Modbus TCP | — | ⚠️ Idea · USE — **confirm** | — |
| DTQ-B&R-Connector | B&R | ⟨not recorded⟩ | — | ❌ Idea · NOT AVAILABLE | — |
| DTQ-Bachmann-Connector | Bachmann | ⟨not recorded⟩ | — | ❌ Idea · NOT AVAILABLE | — |

### Non-PLC connectors — the overlooked fallback

**These need no PLC program.** Where the "machine" really exposes a file, an image or a web
service, one of these is the route and the whole PLC branch is irrelevant.

| Connector | Reaches | Via | State |
|---|---|---|---|
| DTQ-FTP2MIL-Connector | File drop, Cognex camera systems | FTP → direct S3 upload | ✅ Productive · USE — the only one with documentation on file |
| DTQ-KEYENCECAM-Connector | Custom Keyence camera system | FTP | ✅ Productive · USE |
| DTQ-RS232-Connector | Serial device — Keyence TM-3000 | RS232 | ✅ Productive · USE |
| DTQ-IROPTRIS-Connector | Optris IR camera | ⟨not recorded⟩ | ✅ Productive · USE |
| DTQ-PIOVAN-Connector | Piovan drying systems | SOAP | ✅ Productive · USE |
| DTQ-Multicon CMC131-Connector | Multicon controller | HTTP(S) | ✅ Productive · USE |
| DTQ-Engel EMI-Connector | Engel injection moulding | Engel-specific | ❌ Idea · NOT AVAILABLE |
| DTQ-ZWICK-Connector | Zwick testing machine | ⟨not recorded⟩ | ❌ Idea · NOT AVAILABLE |
| DTQ-SMB-Connector | Windows file share | SMB → direct S3 upload | ❌ Development · NOT AVAILABLE |
| DTQ-SmartKlaus-Connector | SmartKlaus | ⟨not recorded⟩ | ❌ Development · NOT AVAILABLE |

**Where a vendor-specific connector exists and is available, use it** rather than reaching the
vendor's PLC generically. Piovan, Keyence, Optris and Multicon all have one. Engel and Zwick
do not, whatever the Overview's row implies.

### Aggregation server — Softing

| Connector | Reaches | State |
|---|---|---|
| SFT-OPC-Suite | The dataFEED OPC Suite itself, aggregating all its data sources | ✅ Productive · USE — documentation and presentation on file |
| SFT-SIMATIC S7-Connector | Siemens SIMATIC S7-300/400, from the Softing server | ❌ Productive · **DO NOT USE** — see above |

These are the *server* side. The *edge* side of the same link is always
`DTQ-OPCUA-Connector`.

## Reading the Overview without being misled

1. **Check `utilization` before `status`, and check both.** They disagree once, and where they
   do the answer is a question for the IIAE, not a guess.
2. **A missing `input_protocol` is not an absent protocol** — 9 connectors record none. It
   means nobody filled the field.
3. **`documentation_available` is `NO` on 24 of 26.** Only `DTQ-FTP2MIL-Connector` and
   `SFT-OPC-Suite` have anything written down. Plan for the driver's behaviour to be
   discovered on site.
4. **An unavailable native connector does not mean an unreachable PLC.** Ask what the machine
   exposes. If it serves OPC UA, `DTQ-OPCUA-Connector` reaches it today.
