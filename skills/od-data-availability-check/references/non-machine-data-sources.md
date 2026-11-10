---
type: Skill Reference
title: Non-machine data sources
description: Where requested data lives when it is not a PLC signal - laboratory and measurement software, camera systems, manual entry, energy loggers, legacy applications - with how to read the legacy application records, how reachable each class is, and the connectors and tools that exist for them. No counts.
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
1 to 4 run through a different object. This reference says which, and how to read the records
about each. It holds no counts: re-count on the live list and name the export date.

**Where the live truth lives.** The Legacy Application List, as quoted in the vault's
`Graph/Legacy Applications` notes; tool and connector facts in `Graph/Tools` and
`Graph/Connectors`. "Reading" marks an interpretation of this analysis, not a record.

## 1. How to read the legacy application records

Group the applications by **category** and read these fields for each group: network status
(IT / OT-IT / OT / standalone / blank), production criticality, cyber-security status, support
concept, licence status and supplier. Count each live.

Categories to expect: PLC programming / configuration, laboratory software, equipment
configuration, camera system configuration, custom SCADA, printer, quality software, internal
low-code apps, custom MES, material flow / logistics, SCADA, custom dashboarding, energy
monitoring.

**Readings (this analysis, not records):**

1. A **standalone** application has no network path. Its data reaches the data platform only
   by a file drop or manual export. Step 3 (is there a connector and concept) is then not a PLC
   question; look for the file connectors in section 3.
2. **Laboratory software** is where measurement data a use case wants most often lives, and it
   is usually networked. The records give no export interface for it; ask per application.
3. **PLC programming and configuration software** is where the PLC programs live. The
   integration guide stops every PLC route at "if you do not have the PLC program, we cannot
   connect the PLC" (`od-equipment-integration` (`../../../skills/od-equipment-integration/SKILL.md`)).
   Check the licence status of the program software and that the program can be opened before
   treating a machine as "program available".
4. **Camera system configuration** is often standalone. Image data from such systems needs the
   image path (section 3), not a signal path.
5. A **critical** application whose cyber-security status is "not started" is a data source
   whose connection will meet the Cyber Security / OT gate; plan for it (`od-cybersec-gate`).
6. **Blank is not a value.** Blank network status, support concept or licence is "not
   recorded". Do not read it as "none".

## 2. Per plant: where the legacy applications sit

Count the applications per plant live (a few applications are located at more than one plant,
and some have no plant). Where a plant has many legacy applications but few machine rows with
a status and no use cases, the application list is a better starting point for a data request
than the machine list. Compare the plant's application count with its Machine List completeness
(`machine-list-completeness.md`) before choosing.

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
| Manual quality entries | the Quality Feedback and Part Routing app (QFPR): SPC charts from manually collected data, reaction log, alerting on not-OK parts, scrap collection | Read the tool's rollout rows in `Graph/Tools` for which plants have it; cyber-security approval is a precondition for productive use |
| Images for model work | Manufacturing Image Library (MIL) | Read the rollout rows in `Graph/Tools`; some plants are recorded as `STOPPED (MANAGEMENT DECISION)` |
| Energy data | Energy Management (WiriTec): loggers read M-Bus, Modbus RTU, pulse counters and Ethernet protocols (Modbus TCP, BACnet/IP, Siemens RFC1006, Ethernet/IP), file, SQL, SNMP, REST, OPC-UA, MQTT | 1.0 is a local system; 2.0 is the cloud version; read the rollout rows and the "API available" notes per plant |
| Laboratory measurement | Quality-measurement-equipment initiative: integrate measurement equipment within the machine integration waves wherever possible (for example extrusion lines, laser welding machines); migrate cleanliness laboratory devices and their data integration | One-pager in the slide index, 2024 initiatives folder; status not recorded there |

Connector states in this table are the state at the time of writing: re-read `Graph/Connectors`
before reporting a step as passed.

Notes on the rows:

- The only connector with a documented behaviour for a non-PLC endpoint is the FTP one.
  Everything else: ask the IIAE.
- MIL and QFPR and the energy tool also appear in `od-system-fit-check`: whether the plant
  **has the tool** is a fit question there; whether the data **exists** is the question here.
- A data class with a `NOT AVAILABLE` connector is a data gap routed to the Information
  Integration lane as a named request (`../assets/data-gap-request.md`),
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

- Vault `Graph/Legacy Applications` (`LegacyApplication-List` export; take the date from the notes).
- Vault `Graph/Connectors` and `Graph/Tools` (notes for MIL 1.0, QFPR, Energy Management 1.0 and 2.0).
- Vault `Slide Index` (deck `OD Initiative - Quality Measurement Equipment Integration`, slide 1).
- Department note *Systems of record* (`_knowledge/10-Department/Systems of record.md`).
