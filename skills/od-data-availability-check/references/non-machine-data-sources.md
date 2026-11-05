---
type: Skill Reference
title: Non-machine data sources
description: Where requested data lives when it is not a PLC signal - laboratory and measurement software, camera systems, manual entry, energy loggers, legacy applications - with the recorded counts of what those applications are, how reachable they are, and the connectors and tools that exist for them.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Non-machine data sources

The six steps start at the machine. A good share of the data people ask for is not on a PLC:
a leak-test value in the tester's own software, a measurement in a laboratory application, an
image on a camera PC, a paper checklist, a kWh reading in the energy logger. For those, steps
1 to 4 run through a different object. This reference says which, and what the records
carry about each.

**Grades.** Counts are from the Legacy Application List as quoted in the vault's
`Graph/Legacy Applications` notes (268; export of 2026-08-24), counted 2026-11-05. Tool and
connector facts are from `Graph/Tools` and `Graph/Connectors` (exports of 2026-08-24).
"Reading" marks an interpretation of this analysis, not a record.

## 1. What the 268 legacy applications are (record counts)

| Application category | Apps | Network status (IT / OT-IT / OT / standalone / blank) | Production criticality (critical / other) | Cyber-security status |
|---|--:|---|---|---|
| PLC programming / configuration | 73 | 9 / 2 / 3 / 29 / 30 | 38 critical | 41 not started, 31 blank, 1 standalone |
| Laboratory software | 52 | 23 / 15 / 4 / 9 / 1 | 23 critical | 41 not started, 11 blank |
| Equipment configuration | 33 | 4 / 1 / 2 / 20 / 6 | 13 critical | 28 not started, 4 standalone |
| Camera system configuration | 25 | 3 / 1 / 1 / 15 / 5 | 14 critical | 13 not started, 6 standalone, 1 in progress |
| Custom SCADA | 15 | 2 / 1 / 4 / 2 / 6 | 3 critical | 6 not started, 2 approved |
| Printer | 12 | 5 / 0 / 0 / 3 / 4 | 5 critical | 7 not started |
| Quality software | 10 | 5 / 0 / 2 / 3 / 0 | 2 critical | 3 not started |
| Internal Mendix apps | 9 | 2 / 0 / 1 / 6 / 0 | 1 critical | 3 approved, 6 not started |
| Custom MES | 8 | 4 / 0 / 1 / 0 / 3 | 2 critical | 7 not started |
| Material flow / logistics | 6 | 1 / 3 / 1 / 0 / 1 | 2 critical | 5 not started |
| SCADA | 6 | 0 / 1 / 1 / 4 / 0 | 3 critical | 3 not started |
| Custom dashboarding, energy monitoring, MES, uncategorised | 19 | | | |

Across all 268: network status **standalone 94**, IT 65, OT/IT 25, OT 21, blank 63;
production criticality **critical 109**; customer impact critical 110; cyber-security status
**not started 172**, approved 7, in progress 3, not applicable (standalone) 15, blank 71.
Support concept: internal 86, maintenance and run concept 33, external contract 35, blank 114.
Licence: unknown 128, no licence required 67, local licence available 57, OESL licence
required 15. Supplier counts of the largest suppliers: Keyence 31, Siemens 18, internal 13,
ContiTech 12, Mitsubishi 11, Hexagon 8.

**Readings (this analysis, not records):**

1. A **standalone** application (94) has no network path. Its data reaches the data platform
   only by a file drop or manual export. Step 3 (is there a connector and concept) is then not a
   PLC question; look for the file connectors in section 3.
2. **Laboratory software (52)** is the largest group that is networked (IT or OT/IT: 38). This
   is where measurement data a use case wants most often lives. The records give no export
   interface for any of them; ask per application.
3. **PLC programming and configuration software (73)** is where the PLC programs live. The
   integration guide stops every PLC route at "if you do not have the PLC program, we cannot
   connect the PLC" ([`od-equipment-integration`](../../od-equipment-integration/SKILL.md)). For
   those 73, licence status is unknown on 34, local licence on 30, OESL licence on 1: check
   the program can be opened before treating a machine as "program available".
4. **Camera system configuration (25)**: 15 standalone. Image data from such systems needs the
   image path (section 3), not a signal path.
5. A **critical** application with cyber-security status "not started" (70 apps) is a
   data source whose connection will meet the Cyber Security / OT gate; plan for it
   (`od-cybersec-gate`).

## 2. Per plant: where the legacy applications sit (record counts)

Hannover Stöcken 48, Subotica 45, Ponta Grossa 38, Monterrey 37, Montemorelos 22, Caluire 16,
Vac 15, Delicias 9, then Qingdao, Karben, Mako, Sun Prairie 6 each; the remaining plants
have 4 or fewer. 10 applications are located at more than one plant; 2 have no plant.
Montemorelos has 22 legacy applications, 51 machines with no status and no use case: for a
data request there, the application list is the better starting point than the machine list.

## 3. Reaching the data - what exists

| Data class | What exists (record) | State |
|---|---|---|
| Image or file from a camera system | `DTQ-FTP2MIL-Connector` (FTP to direct S3 upload; pulls images and metadata of an end-of-line camera, Cognex) | `Productive`, `USE`, documented |
| Measurement CSV on an FTP server | `DTQ-KEYENCECAM-Connector` | `Productive`, `USE` |
| Serial measurement system | `DTQ-RS232-Connector` (Keyence TM-3000) | `Productive`, `USE` |
| Infrared camera images | `DTQ-IROPTRIS-Connector` (to S3) | `Productive`, `USE` |
| Files on a Windows share | `DTQ-SMB-Connector` | `Development`, `NOT AVAILABLE` |
| Zwick test files (zs2) | `DTQ-ZWICK-Connector` | `Idea`, `NOT AVAILABLE` |
| Smart Klaus vision system | `DTQ-SmartKlaus-Connector` | `Development`, `NOT AVAILABLE` |
| Web or SOAP interface (Multicon controllers, Piovan dryers) | `DTQ-Multicon CMC131-Connector`, `DTQ-PIOVAN-Connector` | `Productive`, `USE` |
| Manual quality entries | the Quality Feedback and Part Routing app (QFPR): SPC charts from manually collected data, reaction log, alerting on not-OK parts, scrap collection | Rollout `AVAILABLE` at Waltershausen (2021), `ONGOING` at Monterrey (2023); first-mover plants named in the 2024 one-pager: Monterrey and Carei; cyber-security approval pending in 2024 |
| Images for model work | Manufacturing Image Library (MIL) | Rollout row: Northeim `ONGOING`; `STOPPED (MANAGEMENT DECISION)` at Delicias (2023), Mako (2022) and Dolne Vestenice (2024) |
| Energy data | Energy Management (WiriTec): loggers read M-Bus, Modbus RTU, pulse counters and Ethernet protocols (Modbus TCP, BACnet/IP, Siemens RFC1006, Ethernet/IP), file, SQL, SNMP, REST, OPC-UA, MQTT | 1.0 `AVAILABLE` at 4 plants (local system); 2.0 `AVAILABLE` at 17 and "Not Available" at 1 (Auburn); several 2.0 rows note "API available" |
| Laboratory measurement | Quality-measurement-equipment initiative: integrate measurement equipment within the machine integration waves wherever possible (extrusion lines at Carei, Mako, Waltershausen; laser welding machines at Timisoara); migrate cleanliness laboratory devices and their data integration | One-pager in the slide index, 2024 initiatives folder; status not recorded there |

Notes on the rows:

- The only connector with a documented behaviour for a non-PLC endpoint is the FTP one.
  Everything else: ask the IIAE.
- MIL and QFPR and the energy tool also appear in `od-system-fit-check`: whether the plant
  **has the tool** is a fit question there; whether the data **exists** is the question here.
- A data class with a `NOT AVAILABLE` connector is a data gap routed to the Information
  Integration lane as a named request ([`../assets/data-gap-request.md`](../assets/data-gap-request.md)),
  not a reason to approximate.

## 4. Where the Grafana and data platform split matters

The department's *Systems of record* note states: Grafana is a **local instance per plant**,
building that plant's dashboards from that plant's data; the global layer is the data platform
(machine, IIoT Edge Platform, MQTT and Node-RED, offload, Databricks, Azure Storage Account,
Parquet). A line-side dashboard belongs on the local instance; a cross-plant question belongs
on the data platform. **Rule:** do not answer a cross-plant request from one plant's Grafana,
and do not point a plant's Grafana at the global layer. Access paths, workspace and container
naming and the catalog layout of the data platform are not recorded
(⟨to collect; who could supply it: the owner of the data platform⟩).

## Sources

- Vault `Graph/Legacy Applications` (268 notes; `LegacyApplication-List` export 2026-08-24),
  counted 2026-11-05.
- Vault `Graph/Connectors` and `Graph/Tools` (notes for MIL 1.0, QFPR, Energy Management 1.0 and 2.0).
- Vault `Slide Index` (deck `OD Initiative - Quality Measurement Equipment Integration`, slide 1).
- Department note *Systems of record* (`_knowledge/10-Department/Systems of record.md`).
