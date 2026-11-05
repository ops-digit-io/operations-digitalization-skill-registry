---
type: Skill Reference
title: Connector fact sheets
description: One fact sheet per connector in the Connector Overview - what the record says it does, signal limits and sampling rates, linked machine counts, recorded enhancement or build estimates - and how to read the machine counts correctly.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Connector fact sheets

[`connectors.md`](connectors.md) answers "is the connector available?". This file adds what
the Connector Overview and the machine links record **beyond availability**: the technical
limits that decide whether a connector fits a machine, the machine counts, and the build or
enhancement estimates somebody wrote on the item.

**Source and date.** Vault `Graph/Connectors` (26 notes), quoting the `ConnectorOverview-List`
SharePoint export of 2026-08-24; machine counts from the `Graph/Machines` links, read
2026-11-05. Texts below are paraphrases of the Overview's own fields; prices are quoted
exactly as written (currency and wording as recorded, none audited).

## How to read the machine counts

"Connects to N machines" is a **graph link, made by controller family**, not a record of what
runs on the machine. Two signs: `DTQ-S7-Connector` and `SFT-SIMATIC S7-Connector` both show
the same 330 machines at the same 20 plants, although the second one is `DO NOT USE`; and
`DTQ-TIA-Connector` shows 416 machines, which is exactly the S7-1200 (250) plus S7-1500 (166)
rows in the Machine List. So:

- **Record count (2026-08-21 machines / 2026-08-24 connectors):** the number of machines of a
  family that *could* be reached by that connector.
- **Not recorded:** which connector a given machine *actually* uses. The Machine List's
  `integration_method` names the concept (edge or aggregation), not the connector. Name the
  connector in the Machine List row when you integrate (rule in [`SKILL.md`](../SKILL.md),
  Gate 4).

## Edge connectors for PLCs (DATATRONiQ, all `Productive`, `USE` unless stated)

| Connector | Input to output | Recorded facts | Linked machines (graph) |
|---|---|---|---|
| `DTQ-S7-Connector` | PROFINET IO to MQTT | PLCs: S7-300, S7-400. Documentation: no. Comment on the item (plant Somersworth): enhancement for frequent tool changes (named plants WHS and SOM) and for PLCs with a tool-based PLC data model, **price tag 10.875 € (offer attached)**. Image `datatron-cifx` | 330 at 20 plants: Vac 65, Mako 36, Carei 33, Changshu 28, Waltershausen 28, Subotica 23; of these 112 integrated, 86 not, 26 ongoing |
| `DTQ-TIA-Connector` | to MQTT | PLCs: S7-1200, S7-1500. Input protocol not recorded | 416 at 20 plants: Subotica 90, Mako 55, Tlalnepantla 45, Qingdao 39, Vac 32, Ponta Grossa 30; 196 integrated, 103 not, 5 ongoing |
| `DTQ-S7-NET-Connector` | to MQTT | "Low frequency data collector for Siemens S7 Profinet devices (or Profibus devices with Helmholz connector)". Comment: developed within the Carei project "Machine Connectivity Nader Area 2023" | not linked in the graph |
| `DTQ-SINUMERIK-Connector` | UDP/IP to MQTT | Controller: Siemens SINUMERIK. "Push" mode; signals from NCU/NCK (axis, R-values, G-code); **2 ms** sampling; **up to 30 signals**; needs a **custom function block inside the PLC program** and **custom G-code in the NCU/NCK**; the edge device receives from the PLC over UDP/IP | 27 at 4 plants: Ponta Grossa 11, Caluire 10, Subotica 3, Tlalnepantla 3; 12 integrated, 11 not |
| `DTQ-SINUVARS-Connector` | TCP/IP to MQTT | Signals from NCK/NCU and PLC; about **10 ms** sampling (10 ms for 10 signals, 100 ms for hundreds of signals); **up to 100 signals** (analog and digital); the edge device does request/response over TCP/IP | not linked in the graph |
| `DTQ-SIMOTIOND-Connectors` | to MQTT | Comment: SIMOTION D connector "to implement the remaining BLM SMART Machines" | not linked |
| `DTQ-Beckhoff-Connector` | ADS to MQTT | Controller: Beckhoff. Image `datatron-ads-collect` | 42 at 5 plants (Subotica 15, Somersworth 9, Waltershausen 8, Changshu 7, San Luis Potosi 3); 17 integrated, 22 not |
| `DTQ-EthercatIO-Connector` | to MQTT | "Ethercat Master Connector for Beckhoff Clamps (e.g. for BLM AST80)" | not linked; the 49 EtherCAT rows are the population |
| `DTQ-ALLENBRADLEY-ROCKWELL-Connector` | to MQTT | Rockwell / Allen-Bradley | 220 at 6 plants; 113 integrated, 58 not, 2 ongoing |
| `DTQ-OMRON FINS-Connector` | OMRON FINS to MQTT | OMRON FINS PLCs | 12 at 2 plants (Timisoara 8, Monterrey 4); all 12 integrated |
| `DTQ-OPCUA-Connector` | OPC-UA to MQTT | No PLC list, no comment. The bridge to the Central Aggregation Server and the direct reader of a machine's own server ([`connectors.md`](connectors.md)) | not linked |
| `DTQ-MODBUS-Connector` | Modbus TCP to MQTT | "Default connector from the Edge Platform"; status `Idea`, utilization `USE` | not linked; see [`vendor-protocol-routes.md`](vendor-protocol-routes.md) for the Modbus rows |

## Connectors for non-PLC endpoints

| Connector | Input to output | Recorded facts | Linked machines |
|---|---|---|---|
| `DTQ-FTP2MIL-Connector` | FTP to direct S3 upload | Docker-based; pulls images and metadata generated by an **end-of-line testing camera** (Cognex camera systems) and transfers them to an Azure Blob Storage remote store. **The only connector with documentation (YES)** besides `SFT-OPC-Suite` | not linked |
| `DTQ-KEYENCECAM-Connector` | FTP to MQTT | Collects **measurement data from CSV files on an FTP server**; "custom integration for complex turnkey camera system solution in Waltershausen" | 12 at Karben, all integrated (note the description names Waltershausen, the machines are linked at Karben: confirm which plant runs it) |
| `DTQ-RS232-Connector` | RS232 to MQTT | Connects the Keyence TM-3000 measurement system. Comment (plant Monterrey): enhancement necessary to bring the connector to the edge platform, esp. for Mexican plants; **price tag 5000 € (estimation)** | 12 at Karben, all integrated |
| `DTQ-IROPTRIS-Connector` | not recorded | Custom connector for **Optris IR camera** image data to S3 storage (not direct Azure upload) | not linked |
| `DTQ-PIOVAN-Connector` | SOAP to MQTT | Collects data from the SOAP interface of **Piovan drying systems**. Comment (plant Somersworth): idea for development, esp. for Somersworth and Waltershausen; **estimation 10k €** | 2 Piovan rows (Somersworth, San Luis Potosi), 1 integrated |
| `DTQ-Multicon CMC131-Connector` | HTTP(S) to MQTT | "Multicon devices are used to connect multiple autoclaves in Mako. Possibility to bundle many autoclaves at once." | not linked |
| `DTQ-Engel EMI-Connector` | Engel-specific to MQTT | `Idea`, `NOT AVAILABLE`. Comment: consider a custom connector for Engel machines, high-frequency time series (EMI) | 38 Engel machines (Northeim 31, Changshu 6, Somersworth 1); 32 integrated, 6 not |
| `DTQ-ZWICK-Connector` | not recorded | `Idea`, `NOT AVAILABLE`. "Custom connector to collect high-frequency data from zs2 files from Zwick" (example: pull-off tests). Comment (plant Waltershausen I and II): **estimation 10k €** | not linked |
| `DTQ-SMB-Connector` | SMB file share to direct S3 upload | `Development`, `NOT AVAILABLE`. "Development to be started based on Laser Welding Machine Integration in Timisoara." Comment: has priority based on feedback of 2025-07-09; in preparation to move ahead with eCR / funding and development | not linked |
| `DTQ-SmartKlaus-Connector` | to MQTT | `Development`, `NOT AVAILABLE`. "Custom connector for Smart Klaus systems". The Vac vision system whose missing connection to the MSB is a stated blocker for result feedback (see [`blockers-and-waves.md`](blockers-and-waves.md)) | not linked |
| `DTQ-B&R-Connector`, `DTQ-Bachmann-Connector` | none recorded | `Idea`, `NOT AVAILABLE`; "Development to be started with Rollout in Dolne Vestenice" | B&R 32 (Dolne Vestenice 31, Waltershausen 1); Bachmann 63 (Northeim 24, Dolne Vestenice 20, Changshu 19) |

## Softing connectors (Softing Industrial)

| Connector | Recorded facts |
|---|---|
| `SFT-OPC-Suite` | `Productive`, `USE`, documentation: yes. "Softing OPC Suite". The graph links it to the 24 Northeim `Bachmann OPC` machines, all integrated |
| `SFT-SIMATIC S7-Connector` | `Productive`, `DO NOT USE`. The Softing dataFEED edgeConnector Siemens: a containerized SIMATIC S7 connectivity module adding an OPC UA server and MQTT publisher/subscriber; southbound and northbound set up via local GUI or REST. Reasons not to use: not developed cloud-native (high effort to wrap), and still no cyber-security-compliant communication to the PLC |

## Build and enhancement estimates written on the items

All four are free-text comments, not budgets. Treat them as a trace of who asked, not as a price.

| Connector | What the comment asks for | Written estimate |
|---|---|---|
| `DTQ-S7-Connector` | Frequent tool changes and tool-based PLC data model (Somersworth) | 10.875 € (offer attached) |
| `DTQ-RS232-Connector` | Bring the connector to the edge platform (Monterrey, Mexican plants) | 5000 € (estimation) |
| `DTQ-PIOVAN-Connector` | Development for Somersworth and Waltershausen | 10k € |
| `DTQ-ZWICK-Connector` | Waltershausen I and II | 10k € |

⟨Whether any of these was approved or built. The Overview has no date or decision field.
Who could supply it: IIAE with the connector vendor's account owner.⟩

## What to do with this

1. When a machine is a Siemens CNC (SINUMERIK 840D SL: 19 rows, 7 integrated, 8 not), check
   the signal budget first: 30 signals at 2 ms (UDP push, needs PLC program changes and G-code)
   versus 100 signals at about 10 ms (TCP request/response). A use case that needs more
   signals or faster sampling is outside both.
2. For camera and file endpoints (Cognex EOL camera, Keyence CSV on FTP, Optris IR, Zwick
   files, SMB shares) the route is a file or image connector, not the PLC branch. Only the
   FTP route has a connector in `Productive`.
3. Quote the exact connector name in the Machine List row and in
   `assets/guidance-protocol.md`; the count above will not tell the next engineer which one
   was used.
4. When the Overview field you need is empty (11 of 26 connector notes have no input protocol
   field; the existing skill's "9" was counted on an earlier export; 24 of 26 have no documentation), say "not recorded" and ask the IIAE; do not infer from the
   connector's name.

## Sources

- Vault `Graph/Connectors/*.md` (26 notes, including the `SharePoint record (full text)`
  blocks), read 2026-11-05.
- Vault `Graph/Machines` links, counted 2026-11-05.
- Registry reference [`connectors.md`](connectors.md) (availability) and
  [`vendor-protocol-routes.md`](vendor-protocol-routes.md).
