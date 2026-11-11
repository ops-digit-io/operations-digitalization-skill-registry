---
type: Skill Reference
title: Acceptance by route
description: Guidance, no figures. What to look at in a site acceptance of a machine integration, per route and connector, and the failure patterns the Machine List, the Connector Overview and the tool notes typically show - each check marked as suggested (derived from a kind of record) or as an existing rule.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Acceptance by route

`test-structure.md` gives the generic SAT/SIT frame and the six fields of a
test item. What it cannot say is *which items* a given route needs. This reference does,
using what the department's records say about each route. It carries no counts: to see how
often a pattern occurs, count it on the live Machine List (see "How to measure" below).

**Grades used in the tables.**

- **Rule**: already stated in a registry skill (cited).
- **Record pattern**: something the Machine List, Connector Overview or a tool note typically
  records.
- **Suggested check**: this analysis turns a record pattern into a test item. It is a proposal
  for the IIAE to confirm, not a department standard. Each names the kind of record it comes from.

Acceptance is human-only; this file helps draft the protocol
(`../assets/acceptance-test-protocol.md`).

## 1. Checks that apply to every route

| # | Item | Grade | Source |
|---|---|---|---|
| 1 | The test runs along the **full path**: machine, connector, ingress variant, edge, offload, data platform, the asset the plant opens | Rule | [`SKILL.md`](../SKILL.md) |
| 2 | The Machine List row names **every connector in the chain** (two for the OPC UA bridge path); the route field is filled | Rule + Record pattern | `od-equipment-integration` Gate 4; a blank route field is common on integrated machines |
| 3 | The row carries vendor, PLC model and network protocol | Suggested check | Record pattern: model and protocol are often blank, sometimes on every row of a plant that is fully integrated |
| 4 | Write permission is **off** on an aggregation-server data source unless a use case writes to the PLC | Rule | `od-equipment-integration` guardrails |
| 5 | Tags follow the agreed data model, not the PLC's layout | Rule | `od-equipment-integration` guardrails ("CT Base"); missing data-model alignment is the commonest recorded blocker class |
| 6 | Cyber Security / OT sign-off exists for any external connection **before go-live**; a test that needs the live connection waits for it | Rule | `od-equipment-integration`; `od-cybersec-gate` |
| 7 | An integration date is written; the status moves to `INTEGRATED` only after the pass | Rule | `SKILL.md`; record pattern: rows `INTEGRATED` without a date |
| 8 | Any blocker text on the row is closed or restated before the pass | Suggested check | Record pattern: blocker texts that sit on machines already `INTEGRATED` (`../../../skills/od-equipment-integration/references/blockers-and-waves.md`) |

## 2. Edge route (variant 1): PLC, edge device, connector

| Item | Grade | Source and typical failure point |
|---|---|---|
| Edge device sits where the plan says; ETH1, 24 V, shop-floor Ethernet as in the cabinet work | Rule | `od-equipment-integration` Gate 3 |
| If the device is **shared** across machines, each machine behind it is tested on its own and the failure domain is recorded | Suggested check | Record pattern: rows reading "Edge Device [same as other device] via Siemens TCP/IP Ethernet Driver"; notes such as "both machines connected to 1 Edge Device"; "1x Edge Device dedicated to <module> needed" |
| Device count matches the plan | Suggested check | Record pattern: edge device allocation is a recurring blocker class at plants with many machines per line |
| S7-300/400 uses `DTQ-S7-Connector`; S7-1200/1500 uses `DTQ-TIA-Connector`; the Softing edge connector is **not** used | Rule + Record | `connectors.md`; `SFT-SIMATIC S7-Connector` is `DO NOT USE` |
| TIA project version is compatible | Suggested check | Record pattern: "TIA V16 upgrade necessary for TIA V17" style rows, typically `NOT INTEGRATED` |
| Firmware or vulnerability patch state confirmed | Suggested check | Record pattern: firmware patching or vulnerability blockers, some on rows already marked integrated |
| CNC (Sinumerik): the PLC program carries the custom function block and the NCU carries the custom G-code; signal count and rate stay within the connector limits (Sinumerik connector: 30 signals at 2 ms; Sinuvars connector: 100 signals at about 10 ms) | Suggested check | Technical limits per `../../../skills/od-equipment-integration/references/connector-fact-sheets.md` |
| Beckhoff clamps: daisy-chained clamps behave as separate machines | Suggested check | Record pattern: "Beckhoff Clamps (+Daisy Chain with other ...)" |
| Camera sharing the device: image flow tested **as well as** the signals | Suggested check | Record pattern: "Edge (together with camera)"; "Camera Hardware and Integration" blocker |
| Machines needing a PLC program: the program is the one running on the machine | Suggested check | Record pattern: "PLC program missing, was wrong"; "multiple sub PLC programs" |

## 3. Aggregation route (variant 3): PLC, Softing server, `DTQ-OPCUA-Connector`

| Item | Grade | Source and typical failure point |
|---|---|---|
| The data source's driver exists and its licence is in place | Rule | `od-equipment-integration` (each PLC family needs its own licence unless Suite Extended; at most 50 concurrent configurations) |
| Edge platform is present behind the server | Rule | A Softing server with no edge platform delivers nothing to the data platform |
| Both hops tested: server to edge (OPC UA address space), and edge onward | Suggested check | The Machine List row names both connectors |
| For a protocol whose route field is blank, how the data reaches the platform is written into the protocol | Suggested check | Record pattern: Modbus / TCP rows frequently have no route recorded (`../../../skills/od-equipment-integration/references/vendor-protocol-routes.md`) |
| Beckhoff on the aggregation server is **not** accepted as "ADS" | Rule | The server has no Beckhoff driver |
| Mitsubishi: driver and licence confirmed | Suggested check | Record pattern: the route is often still "under evaluation" |
| Rockwell via RSLinx OPC-UA: gateway versus direct path written down | Suggested check | Record pattern: "RSLinx OPC-UA TCP/IP" rows; Rockwell routes are often still under evaluation |

## 4. Non-PLC endpoints: files, images, serial, web services

| Endpoint | Items to test | Grade and source |
|---|---|---|
| End-of-line camera images (FTP to blob) | Images **and** metadata arrive; the naming convention is as agreed; the retention of the source is known | Suggested check. Record: `DTQ-FTP2MIL-Connector` pulls images and metadata; a vision system can store images per part under a PLC-generated name (part number, serial ID, side, timestamp) and local storage can fill within weeks, needing manual backup (tool note `MIL 1.0`, archive-based) |
| Keyence measurement CSV on an FTP server | A file with the expected content arrives for each part; rows parse | Suggested check. Record: `DTQ-KEYENCECAM-Connector` |
| Serial measurement system | Values match the instrument's display | Suggested check. Record: `DTQ-RS232-Connector` (Keyence TM-3000); enhancement for the edge platform recorded as needed |
| Piovan, Multicon | Value read over the web service equals the device display | Suggested check. Record: SOAP and HTTP(S) connectors |
| Smart Klaus system | Reports and images may be pulled by USB with a delay; the acceptance question is whether the automated path now replaces that | Record: tool note `MIL 1.0`; check the connector's current status in the Connector Overview before promising it |

## 5. Energy loggers and plant-side tools

| Item | Grade | Source |
|---|---|---|
| Network separation between office and shop-floor LAN and certificate-based communication are in place before the cloud energy tool is accepted | Record + Suggested check | Tool note `Energy Management 2.0` (prerequisite) |
| Cutover per location is planned with an expected outage while loggers are reconfigured; a per-location checklist is ticked | Record | Same note: a per-location, colour-coded checklist |
| QFPR: cyber-security approval exists before a productive acceptance; a test instance is not accepted as productive | Record + Suggested check | Tool note `QFPR` |

## 6. Failure patterns that recur in the records

| Failure pattern | Where it tends to show | What to check |
|---|---|---|
| Data model standardization not done | Plants integrated before the data model was agreed | Tag names against the agreed model |
| Firmware or vulnerability patch missing | Plants with older S7-1200 / S7-300 estates | Patch state and a patch window with Plant IT |
| Engineering software version mismatch (TIA) | Plants with mixed TIA versions | Version compatibility before the test |
| Edge device allocation or camera hardware unresolved | Plants with many machines per line, or cameras on the same device | Device per machine versus shared; image flow |
| PLC program missing, wrong or PLC unidentified | Older machines | The program on the machine is the one tested against |
| Route blank on integrated machines | Any plant | Write the route and connector chain into the protocol and the Machine List |
| Dry run accepted as a pass | Image / vision pilots | A dry run on a test path is FAT-equivalent, not the gate |

These are what the acceptance should look for first. They are not a ranking of causes.

## How to measure the patterns live

Filter the Machine List export by the blocker text, by status `INTEGRATED` with a blank route,
model or protocol, and by integration date; count per plant; quote the export date with any
figure. See `../../../skills/od-equipment-integration/references/plant-integration-status.md`.

⟨Acceptance results of past integrations. The knowledge base carries no acceptance protocol, no pass or
fail record per machine, and the lane's acceptance/rework rate is "not captured in any system"
(`od-equipment-integration` (`../../../skills/od-equipment-integration/references/od-information-integration-service/procedure.md`)).
Who could supply it: the IIAEs, from their own files.⟩

## Sources

- Knowledge base `Graph/Machines`, `Graph/Connectors`, `Graph/Tools`, read 2026-11-05.
- Registry references `../../../skills/od-equipment-integration/references/connectors.md` and the guardrails in `od-equipment-integration` (`../../../skills/od-equipment-integration/SKILL.md`).
