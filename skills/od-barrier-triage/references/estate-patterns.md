---
type: Skill Reference
title: Estate patterns
description: What the 1,715 machine records show about where integration is stuck - status by vendor and protocol, concentration by plant, the recorded blocker texts grouped by class, and the data gaps that stop a triage.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice, aggregate]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Estate patterns

Aggregates of the 1,715 `Machine` records in the bundle file `kg_nodes.csv` (read 2026-11-05). Machine notes
in the work vault are data records, so they are read as patterns, not one by one. Counts describe what was
recorded, not what is true on the line. The 26 connector records are summarised in `od-equipment-integration`
(`connectors`).

## Status

| Integration status | Machines |
|---|--:|
| `INTEGRATED` | 821 |
| `NOT INTEGRATED` | 395 |
| `INTEGRATION ONGOING` | 48 |
| No status recorded | 451 |

The existing skill states the first three; the fourth is the remainder. A triage that counts only the
395 misses machines nobody has classified.

## Where `NOT INTEGRATED` sits

By PLC vendor (all machines of the vendor, then of those `NOT INTEGRATED`):

| Vendor | Machines | `NOT INTEGRATED` | Note |
|---|--:|--:|---|
| Siemens | 1,032 | 232 | 402 integrated; 359 with no status |
| Rockwell Automation (Allen Bradley) | 220 | 58 | 113 integrated |
| No vendor recorded | 133 | 23 | |
| Beckhoff | 42 | 22 | 17 integrated; no ADS driver on the aggregation server |
| Delta Electronic | 14 | 14 | none integrated |
| Bachmann Electronic | 39 | 10 | a separate "Bachmann OPC" vendor entry: 24, all integrated |
| Philips | 9 | 9 | none integrated |
| Mitsubishi Electric | 17 | 8 | 3 integrated, 6 with no status |
| Engel | 38 | 6 | 32 integrated |
| B&R Industrial Automation | 32 | 1 | 29 integrated |

Delta and Philips are 23 machines, all `NOT INTEGRATED`: they sit at the bottom of the difficulty ranking
(`barrier-classes`: Delta 11th, Philips 12th), and the table agrees. B&R is 6th in the ranking yet 29 of 32
are integrated: the rate reflects the historical aggregation route and not the ease of a new machine, which
is the point of that reference. Do not use this table to promise an easy B&R machine.

By field network (machines of the protocol, then `NOT INTEGRATED`, then `INTEGRATED`):

| Protocol | Machines | `NOT INTEGRATED` | `INTEGRATED` |
|---|--:|--:|--:|
| PROFINET | 445 | 81 | 210 |
| TCP / IP | 220 | 75 | 143 |
| Ethernet / IP | 186 | 54 | 110 |
| Modbus / TCP | 80 | 0 | 78 |
| PROFIBUS | 56 | 34 | 11 |
| EtherCAT | 49 | 19 | 24 |
| MPI | 43 | 11 | 9 |
| No protocol recorded | 551 | 116 | 200 |

PROFIBUS is the weak spot: 34 of 56 not integrated and 11 integrated (the ranking puts Siemens S7 PROFIBUS
10th). Modbus / TCP shows 78 of 80 integrated through the aggregation route, and the edge connector for
Modbus is only an idea: that is the "Modbus contradiction" in `barrier-classes`, not an easy protocol.

By plant, of the 395 `NOT INTEGRATED`: Subotica 142, Changshu 78, Monterrey 56, then Tanger 19 and Korbach
16. Three plants carry 276 of 395. A plant-level triage should start there and not spread evenly.

Planned method of the 395: IIoT Edge Platform 225, Central Aggregation Server 58, evaluation ongoing 57,
none recorded 55.

## What the recorded blocker texts say

125 machines carry free text in the integration blockers field. Grouped by keyword by this skill (not a
recorded taxonomy):

| Group of text | Machines | Class (`classes-and-routes`) |
|---|--:|---|
| Data model standardization (CT Base) | 23 | C7 |
| Firmware patching for cyber security (13); vulnerability to patch before integration (5) | 18 | C3, and C2 or C6 behind it |
| Edge device notes (one device dedicated to a module, device for a standalone machine) | 13 | C4 (edge hardware planning) |
| TIA V16 upgrade needed for V17, to be discussed with a plant | 12 | `⟨class to confirm⟩`: the text does not say why V17 is required |
| Robot or laser-welding signals possibly available in the related machine or PLC | 11 | substitution, ladder rung 6 |
| Camera hardware and integration | 7 | substitution, rung 7 |
| PLC program missing or wrong; "when the PLC program is available, integration is possible"; no source code | 5 | C1 |
| PLC type unknown ("no PLC, which type is used") | 2 | facts first, then classify |
| Other: machine ids, copied hardware lists, unclear text | 34 | not classifiable |

Two things follow. First, only **21** of the 395 `NOT INTEGRATED` machines carry any blocker text; 374 carry
none, so for most of them the reason is not in the data and the triage has to collect it. Second, 48 of
the 125 texts sit on machines already `INTEGRATED`: the field is partly a history of blockers that were
cleared, so a recorded blocker is not proof the machine is stuck now.

## Gaps that stop a triage

Of 1,715 machines: no PLC vendor 133, no network protocol 551, no PLC model 447, no part number 687. A
machine without protocol and model cannot be placed in the ranking or routed; the first action is a site
visit or a Plant ME / Plant IT answer, not a decision. The field `production criticality` is empty on every
machine, and the network-status and cyber-security-status fields are empty on every machine: the
"criticality" of the assessment protocol has no data behind it in this export.

## Landscape facts the exits rely on

`landscape.md` (module, last verified 2026-08-10): strategic plants run the IIoT Edge Platform and the data
platform offload where deployed; known barriers there are "operations concepts missing for several tools"
and "limited internal IT knowledge". MES-pilot plants: MES in progress, ERP / S4HANA dependent. Plants with
high demand for the Manufacturing Image Library: not yet deployed, and "depends on the data platform;
licensing to clarify". These are the C4 cases that go to strategy.
