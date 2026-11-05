---
type: Skill Reference
title: Acceptance by route
description: What to look at in a site acceptance of a machine integration, per route and connector, and the failure points that the Machine List, the Connector Overview and the tool notes actually record - each check marked as suggested (derived from a named record) or as an existing rule.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Acceptance by route

[`test-structure.md`](test-structure.md) gives the generic SAT/SIT frame and the six fields of a
test item. What it cannot say is *which items* a given route needs. This reference does,
using only what the department's records say about each route.

**Grades used in the tables.**

- **Rule**: already stated in a registry skill (cited).
- **Record**: something the Machine List, Connector Overview or a tool note records
  (counts as of the Machine List export of 2026-08-21 and the Connector and Tool Overview
  exports of 2026-08-24, counted 2026-11-05).
- **Suggested check**: this analysis turns a record into a test item. It is a proposal for
  the IIAE to confirm, not a department standard. Each names the record it comes from.

Acceptance is human-only; this file helps draft the protocol
([`../assets/acceptance-test-protocol.md`](../assets/acceptance-test-protocol.md)).

## 1. Checks that apply to every route

| # | Item | Grade | Source |
|---|---|---|---|
| 1 | The test runs along the **full path**: machine, connector, ingress variant, edge, offload, data platform, the asset the plant opens | Rule | [`SKILL.md`](../SKILL.md) |
| 2 | The Machine List row names **every connector in the chain** (two for the OPC UA bridge path); the route field is filled | Rule + Record | `od-equipment-integration` Gate 4; the route is blank on 542 of 1,715 rows |
| 3 | The row carries vendor, PLC model and network protocol | Suggested check | Record: model blank on 447 rows, protocol on 551; at Northeim all 87 rows are integrated with no model and no protocol |
| 4 | Write permission is **off** on an aggregation-server data source unless a use case writes to the PLC | Rule | `od-equipment-integration` guardrails |
| 5 | Tags follow the agreed data model, not the PLC's layout | Rule | `od-equipment-integration` guardrails ("CT Base"); the data-model blocker is the largest recorded (23 rows) |
| 6 | Cyber Security / OT sign-off exists for any external connection **before** the test | Rule | `od-equipment-integration`; `od-cybersec-gate` |
| 7 | An integration date is written; the status moves to `INTEGRATED` only after the pass | Rule | `SKILL.md`; record: 7 rows are `INTEGRATED` without a date |
| 8 | Any blocker text on the row is closed or restated before the pass | Suggested check | Record: 40 of 110 blocker texts sit on machines already `INTEGRATED` ([`blockers-and-waves.md`](../../od-equipment-integration/references/blockers-and-waves.md)) |

## 2. Edge route (variant 1): PLC, edge device, connector

| Item | Grade | Source and typical failure point |
|---|---|---|
| Edge device sits where the plan says; ETH1, 24 V, shop-floor Ethernet as in the cabinet work | Rule | `od-equipment-integration` Gate 3 |
| If the device is **shared** across machines, each machine behind it is tested on its own and the failure domain is recorded | Suggested check | Record: 12 Somersworth rows read "Edge Device [Same as BMnn device] via Siemens TCP/IP Ethernet Driver"; Karben notes "both BLM machines connected to 1 Edge Device"; "1x Edge Device dedicated to Module n needed" on 4 rows |
| Device count matches the plan | Suggested check | Record: Karben has 13 and Subotica 7 blocker rows about edge device allocation |
| S7-300/400 uses `DTQ-S7-Connector`; S7-1200/1500 uses `DTQ-TIA-Connector`; the Softing edge connector is **not** used | Rule + Record | `connectors.md`; `SFT-SIMATIC S7-Connector` is `DO NOT USE` |
| TIA project version is compatible | Suggested check | Record: "TIA V16 Upgrade necessary for TIA V17" on 12 Subotica rows, all `NOT INTEGRATED` |
| Firmware or vulnerability patch state confirmed | Suggested check | Record: firmware patching blocker on 13 Mako rows (8 integrated), vulnerability on 5 Tlalnepantla rows |
| CNC (Sinumerik): the PLC program carries the custom function block and the NCU carries the custom G-code; signal count and rate stay within 30 signals at 2 ms (Sinumerik connector) or 100 signals at about 10 ms (Sinuvars connector) | Suggested check | Record: [`connector-fact-sheets.md`](../../od-equipment-integration/references/connector-fact-sheets.md) |
| Beckhoff clamps: daisy-chained clamps behave as separate machines | Suggested check | Record: "Beckhoff Clamps (+Daisy Chain with other BLM AST80)" on 2 Subotica rows |
| Camera sharing the device: image flow tested **as well as** the signals | Suggested check | Record: "Edge (together with camera)" on 7 Subotica rows; "Camera Hardware and Integration" blocker on 2 |
| Machines needing a PLC program: the program is the one running on the machine | Suggested check | Record: "PLC Program missing, was wrong" (Karben); "multiple sub plc programs" (Karben) |

## 3. Aggregation route (variant 3): PLC, Softing server, `DTQ-OPCUA-Connector`

| Item | Grade | Source and typical failure point |
|---|---|---|
| The data source's driver exists and its licence is in place | Rule | `od-equipment-integration` (each PLC family needs its own licence unless Suite Extended; at most 50 concurrent configurations) |
| Edge platform is present behind the server | Rule | A Softing server with no edge platform delivers nothing to the data platform |
| Both hops tested: server to edge (OPC UA address space), and edge onward | Suggested check | Record: the Machine List row names both connectors; 384 rows record this route |
| For a protocol whose route field is blank, how the data reaches the platform is written into the protocol | Suggested check | Record: 59 of 80 Modbus / TCP rows (58 at Rennes) have no route recorded ([`vendor-protocol-routes.md`](../../od-equipment-integration/references/vendor-protocol-routes.md)) |
| Beckhoff on the aggregation server is **not** accepted as "ADS" | Rule | The server has no Beckhoff driver |
| Mitsubishi: driver and licence confirmed | Suggested check | Record: 7 of 17 Mitsubishi rows have the route under evaluation |
| Rockwell via RSLinx OPC-UA: gateway versus direct path written down | Suggested check | Record: "RSLinx OPC-UA TCP/IP" on 24 Sun Prairie rows; Rockwell has 52 rows still under route evaluation |

## 4. Non-PLC endpoints: files, images, serial, web services

| Endpoint | Items to test | Grade and source |
|---|---|---|
| End-of-line camera images (FTP to blob) | Images **and** metadata arrive; the naming convention is as agreed; the retention of the source is known | Suggested check. Record: `DTQ-FTP2MIL-Connector` pulls images and metadata; at Monterrey the vision system stores images per part under a PLC-generated name (part number, serial ID, side, timestamp) and storage fills "roughly every two weeks" needing manual backup (tool note `MIL 1.0`, archive-based) |
| Keyence measurement CSV on an FTP server | A file with the expected content arrives for each part; rows parse | Suggested check. Record: `DTQ-KEYENCECAM-Connector`; 12 Karben machines |
| Serial measurement system | Values match the instrument's display | Suggested check. Record: `DTQ-RS232-Connector` (Keyence TM-3000); enhancement for the edge platform recorded as needed |
| Piovan, Multicon | Value read over the web service equals the device display | Suggested check. Record: SOAP and HTTP(S) connectors |
| Smart Klaus system | Today: reports and images pulled by USB with about a week's delay; the acceptance question is whether the automated path now replaces that | Record: tool note `MIL 1.0`; connector `DTQ-SmartKlaus-Connector` is `Development`, `NOT AVAILABLE` |

## 5. Energy loggers and plant-side tools

| Item | Grade | Source |
|---|---|---|
| Network separation between office and shop-floor LAN and certificate-based communication are in place before the cloud energy tool is accepted | Record + Suggested check | Tool note `Energy Management 2.0` (prerequisite) |
| Cutover per location is planned with the expected outage of about a day while loggers are reconfigured; a per-location checklist is ticked | Record | Same note: 13 of 17 locations done by 2025-10-20, tracked with a per-location colour-coded checklist |
| QFPR: cyber-security approval exists before a productive acceptance; test instance is not accepted as productive | Record + Suggested check | Tool note `QFPR` |

## 6. Failure points that recur in the records (record counts)

| Failure point | Where | Count |
|---|---|--:|
| Data model standardization not done | Caluire | 23 rows |
| Firmware patch or vulnerability patch missing | Mako 13, Tlalnepantla 5 | 18 |
| Engineering software version (TIA V16 to V17) | Subotica | 12 |
| Edge device allocation or camera hardware unresolved | Karben 13, Subotica 7 | 20 |
| PLC program missing, wrong or PLC unidentified | Karben 4, Subotica 2 | 6 |
| Route blank on integrated machines | all plants, notably Northeim 73, Rennes 58, Timisoara 62, Vac 78 | see [`plant-integration-status.md`](../../od-equipment-integration/references/plant-integration-status.md) |
| Dry run accepted as a pass | Northeim image pilot: a 10,000-image dry run is recorded as "not productive" | 1 case |

These are what the acceptance should look for first. They are not a ranking of causes.

⟨Acceptance results of past integrations. The vault carries no acceptance protocol, no pass or
fail record per machine, and the lane's acceptance/rework rate is "not captured in any system"
([`od-information-integration-service`](../../od-information-integration-service/SKILL.md)).
Who could supply it: the IIAEs, from their own files.⟩

## Sources

- Vault `Graph/Machines` (1,715), `Graph/Connectors` (26), `Graph/Tools` (16), counted or read 2026-11-05.
- Registry references [`connectors.md`](../../od-equipment-integration/references/connectors.md) and the guardrails in [`od-equipment-integration`](../../od-equipment-integration/SKILL.md).
