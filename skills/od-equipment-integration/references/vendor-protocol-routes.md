---
type: Skill Reference
title: Vendor protocol routes
description: Per controller vendor, PLC model and network protocol - how many machines, what the Machine List records as status and route, which connector the Connector Overview names, and what the records do and do not say about how each family is reached.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Vendor and protocol routes

Use this when someone says "we have 40 Rockwell machines, what happens to them?". It gives
the **written-down status** per family. It does not rank difficulty (that is
[`barrier-classes.md`](barrier-classes.md), an elicited judgement) and it does not give the
configuration (that is [`decision-paths.md`](decision-paths.md) and the Softing and edge
references).

**Everything in the tables is a record count.** Source: the `Graph/Machines` notes, which quote
the `Machine-List` SharePoint export of 2026-08-21; counted by script on 2026-11-05. Columns:
`Edge` = route `IIoT Edge Computing Platform`; `Aggr.` = `Central OPCUA Aggregation Server`;
`Eval.` = `EVALUATION ONGOING`; `no route` = field blank. Statements marked **Rule** are
rules and cite where they come from.

## Reading rules

1. **Rule (existing `SKILL.md`):** a blank is not a no. Blank status, route or protocol means
   nobody filled the field.
2. **Rule (this analysis, from the tables below):** read a family by status, by route **and**
   by plant. A family whose integrated machines all sit in one plant (Schneider in Rennes, Engel
   in Northeim, Keyence in Karben, Omron in Timisoara and Monterrey) shows that plant's
   decision, not that the family is easy.
3. **Rule ([`connectors.md`](connectors.md)):** where the Overview's native connector is `NOT
   AVAILABLE`, ask what the machine exposes; `DTQ-OPCUA-Connector` reaches any OPC UA server.

## By controller vendor

| Controller vendor | Machines | Integr. | Not integr. | Ongoing | No status | Edge | Aggr. | Eval. | no route |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Siemens | 1032 | 402 | 232 | 39 | 359 | 451 | 251 | 51 | 279 |
| Rockwell Automation - Allen Bradley | 220 | 113 | 58 | 2 | 47 | 78 | 30 | 52 | 60 |
| (blank) | 133 | 91 | 23 | 4 | 15 | 54 | 32 | 4 | 43 |
| Beckhoff | 42 | 17 | 22 | 0 | 3 | 35 | 0 | 0 | 7 |
| Bachmann Electronic GmbH | 39 | 20 | 10 | 0 | 9 | 0 | 16 | 0 | 23 |
| Engel | 38 | 32 | 6 | 0 | 0 | 1 | 6 | 0 | 31 |
| B&R Industrial Automation | 32 | 29 | 1 | 0 | 2 | 0 | 30 | 0 | 2 |
| Schneider Electric | 32 | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 32 |
| Bachmann OPC | 24 | 24 | 0 | 0 | 0 | 0 | 0 | 0 | 24 |
| Mitsubishi Electric | 17 | 3 | 8 | 0 | 6 | 0 | 4 | 7 | 6 |
| Delta Electronic | 14 | 0 | 14 | 0 | 0 | 14 | 0 | 0 | 0 |
| keyence | 12 | 12 | 0 | 0 | 0 | 12 | 0 | 0 | 0 |
| Omron | 12 | 12 | 0 | 0 | 0 | 12 | 0 | 0 | 0 |
| Philips | 9 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 9 |

The 14 listed vendors cover 1,656 of 1,715 rows. 59 rows carry 20 other vendor spellings
(S7.Schnitt. 8, MRA 7, Keba 5, BLM Controller 4, VIPA 6 across two spellings, ASI 4, Inovance 3,
PMA 3, Sigmatek 3, Stange 2, Piovan 2, and single rows). The same vendor appears under two
spellings in three cases (`Keba` / `KEBA Industrial Automation`, `VIPA` / `Vipa`, `Bachmann
Electronic GmbH` / `Bachmann OPC`): count a family with all of its spellings.

### Vendor readings (counts, 2026-08-21 export)

| Family | What the record shows | Connector in the Overview (state) |
|---|---|---|
| Siemens, 1,032 rows (60%) | 402 integrated, 232 not, 39 ongoing, 359 without status; edge 451, aggregation 251, evaluation 51, none 279 | `DTQ-S7-Connector` (S7-300/400, Productive, USE; 330 machines at 20 plants), `DTQ-TIA-Connector` (S7-1200/1500, Productive, USE; 416 machines at 20 plants), `DTQ-SINUMERIK-Connector` (27 machines at 4 plants), `DTQ-SINUVARS`, `DTQ-SIMOTIOND`, `DTQ-S7-NET`; `SFT-SIMATIC S7-Connector` is `DO NOT USE` |
| Rockwell / Allen-Bradley, 220 | 113 integrated, 58 not, 2 ongoing, 47 without status; edge 78, aggregation 30, **evaluation 52**, none 60. Six plants: Monterrey 75, Auburn 60, Montemorelos 47, Sun Prairie 15, Delicias 12, Qingdao 11 | `DTQ-ALLENBRADLEY-ROCKWELL-Connector` (Productive, USE) |
| Beckhoff, 42 | 17 integrated, 22 not, 3 without status; all 35 routed rows are edge, none aggregation. Subotica 15, Somersworth 9, Waltershausen 8, Changshu 7, San Luis Potosi 3 | `DTQ-Beckhoff-Connector` (ADS, Productive, USE); the Central Aggregation Server has no Beckhoff driver ([`SKILL.md`](../SKILL.md)); `DTQ-EthercatIO-Connector` for Beckhoff clamps |
| Bachmann (two spellings), 63 | 44 integrated, 10 not, 9 without status. Northeim 24, Dolne Vestenice 20, Changshu 19. The 24 `Bachmann OPC` rows (Northeim) carry no route; 16 `Bachmann Electronic GmbH` rows say aggregation | `DTQ-Bachmann-Connector` is `Idea`, `NOT AVAILABLE`; `SFT-OPC-Suite` is recorded as connecting the 24 Northeim `Bachmann OPC` machines |
| B&R, 32 | 29 integrated, 1 not, 2 without status; 30 aggregation. Dolne Vestenice 31, Waltershausen 1 | `DTQ-B&R-Connector` is `Idea`, `NOT AVAILABLE` |
| Engel, 38 | 32 integrated (31 with no route recorded, 1 edge), 6 not (aggregation). Northeim 31, Changshu 6, Somersworth 1 | `DTQ-Engel EMI-Connector` is `Idea`, `NOT AVAILABLE`; its comment: consider a custom connector for high-frequency time series |
| Schneider, 32 | all 32 integrated, no route recorded; all at Rennes | none named |
| Mitsubishi, 17 | 3 integrated, 8 not, 6 without status; evaluation 7, aggregation 4. Changshu 8, Changchun 6, Ponta Grossa 2, Montemorelos 1 | none named; the aggregation server needs its own Mitsubishi licence ([`SKILL.md`](../SKILL.md)) |
| Delta, 14 | 0 integrated, 14 not, all routed to edge. Qingdao 12, Subotica 2; PLC model `DVP14SS2` on 12 rows | none named |
| Omron, 12 | 12 integrated, all edge. Timisoara 8, Monterrey 4 | `DTQ-OMRON FINS-Connector` (Productive, USE) |
| Keyence, 12 | 12 integrated, all edge, all at Karben | `DTQ-KEYENCECAM-Connector` and `DTQ-RS232-Connector` (both Productive, USE), each naming these 12 machines |
| Philips, 9 | 0 integrated, 9 not, no route; all at Changshu | none named |

### Model readings (counts)

| Vendor / model | Machines | Integr. | Not integr. | Ongoing | No status | Edge | Aggr. | Eval. | no route |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Siemens / SIMATIC S7-300 | 321 | 112 | 81 | 26 | 102 | 136 | 77 | 30 | 78 |
| Siemens / SIMATIC S7-1200 | 250 | 106 | 55 | 4 | 85 | 113 | 68 | 11 | 58 |
| Siemens / SIMATIC S7-1500 | 166 | 90 | 48 | 1 | 27 | 133 | 18 | 0 | 15 |
| Siemens / SIMATIC S7-200 | 19 | 15 | 2 | 2 | 0 | 2 | 17 | 0 | 0 |
| Siemens / SINUMERIK 840D SL | 19 | 7 | 8 | 0 | 4 | 2 | 17 | 0 | 0 |
| Siemens / SIMATIC ET200SP | 12 | 0 | 12 | 0 | 0 | 0 | 7 | 5 | 0 |
| Siemens / (model blank) | 189 | 61 | 13 | 4 | 111 | 44 | 35 | 3 | 107 |
| Rockwell / Compact Logix 5370 | 88 | 72 | 15 | 1 | 0 | 20 | 8 | 0 | 60 |
| Rockwell / PLC 5069-L306ER | 44 | 0 | 35 | 0 | 9 | 27 | 3 | 14 | 0 |
| Rockwell / Compact Logix | 15 | 13 | 2 | 0 | 0 | 15 | 0 | 0 | 0 |
| Rockwell / SLC5/05 | 12 | 12 | 0 | 0 | 0 | 11 | 1 | 0 | 0 |
| Bachmann Electronic GmbH / MX213 | 18 | 9 | 0 | 0 | 9 | 0 | 9 | 0 | 9 |
| B&R / Automation PC | 32 | 29 | 1 | 0 | 2 | 0 | 30 | 0 | 2 |
| Delta / DVP14SS2 | 12 | 0 | 12 | 0 | 0 | 12 | 0 | 0 | 0 |

Readings:

- **Siemens S7-300 is the largest single model (321)** and splits three ways: 112 integrated,
  81 not, 26 ongoing, 102 without status. Vac holds 61 of them, Mako 36, Carei 33.
- **Rockwell `PLC 5069-L306ER` (47 rows carry this model: Monterrey 38, Montemorelos 9; the
  table counts the 44 with the Rockwell vendor string)** has no integrated machine: 35 not
  integrated, 9 without status, 14 with the route under evaluation. `Compact Logix 5370` (88) is the opposite: 72
  integrated. The Rockwell question is model- and plant-specific, which is why the vendor line
  shows 52 on `EVALUATION ONGOING`.
- **`SIMATIC ET200SP` (12 rows: Ponta Grossa 6, Changshu 4, Tanger 2)** is not integrated on any
  row. ET200SP is a distributed I/O family: check which PLC sits above it before reading the
  row as a PLC. A free-text blocker says the same kind of thing: "IM151-1 Standard: No PLC.
  Which PLC-Type is used?" (2 rows).
- **S7-200 (19)** is mostly integrated (15) over the aggregation route (17); the protocol
  field says PPI on 8 rows, all at Ponta Grossa.

## By network protocol

The protocol field is free text with 18 distinct spellings (PROFIBUS appears as `PROFIBUS`,
`Profibus`, `PROFIBUS / MPI`, `Profibus / Profinet`, …). 551 rows (32%) have none.

| Network protocol (as written) | Machines | Integr. | Not integr. | Ongoing | No status | Edge | Aggr. | Eval. | no route |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| (blank) | 551 | 200 | 116 | 16 | 219 | 179 | 76 | 61 | 235 |
| PROFINET | 445 | 210 | 81 | 17 | 137 | 223 | 110 | 16 | 96 |
| TCP / IP | 220 | 143 | 75 | 0 | 2 | 105 | 55 | 0 | 60 |
| Ethernet / IP | 186 | 110 | 54 | 1 | 21 | 57 | 75 | 29 | 25 |
| Modbus / TCP | 80 | 78 | 0 | 1 | 1 | 0 | 21 | 0 | 59 |
| PROFIBUS | 56 | 11 | 34 | 5 | 6 | 36 | 3 | 10 | 7 |
| EtherCAT | 49 | 24 | 19 | 0 | 6 | 45 | 0 | 1 | 3 |
| MPI | 43 | 9 | 11 | 7 | 16 | 15 | 12 | 0 | 16 |
| PROFIBUS / MPI | 38 | 1 | 1 | 0 | 36 | 1 | 1 | 0 | 36 |
| Profibus | 14 | 6 | 0 | 1 | 7 | 7 | 2 | 0 | 5 |
| PPI | 8 | 6 | 2 | 0 | 0 | 0 | 8 | 0 | 0 |
| Profibus / Industrial ethernet | 7 | 5 | 2 | 0 | 0 | 0 | 7 | 0 | 0 |

Readings (counts):

- **Modbus / TCP: 78 of 80 integrated, but only 21 rows record the aggregation route and 59
  record no route.** 58 of the 80 are the Rennes rows (Schneider), 19 are Caluire. The existing
  statement that the high Modbus integration rate reflects the aggregation-server route
  ([`barrier-classes.md`](barrier-classes.md)) is therefore visible in the route field for 21
  rows and **not demonstrable from it for the other 59**. ⟨How the Rennes Modbus machines
  reach the data platform. Who could supply it: the IIAE responsible for Rennes.⟩ The edge
  `DTQ-MODBUS-Connector` is `Idea` with utilization `USE`, and no Modbus row records an edge
  route.
- **PROFIBUS, MPI and PPI (every spelling containing Profibus or MPI, 109 rows including mixed
  entries):** 28 integrated, 14 not, 8 ongoing, 59 without status. This fits the elicited
  ranking where S7 PROFIBUS is near the bottom. The `PPI` rows (8) and `Profibus / Industrial
  ethernet` rows (7) are all aggregation-routed.
- **EtherCAT (49):** 24 integrated, 19 not; 45 routed to edge. Largely the Beckhoff family
  (clamps via `DTQ-EthercatIO-Connector`).
- **Ethernet/IP (186)** is mainly the Rockwell protocol; 29 rows are under route evaluation.
- **PROFINET (445)** is the largest named protocol: 210 integrated, 223 edge-routed.

## What the records do not give

⟨Cost per machine by family. The ODEC connectivity-roadmap slide of 2024-08-26 (ODEC Facts
staging note, AI-extracted, not verified) shows "413,200 €" next to "39 PG + 30 Mty + 18 Del +
10 SL", ">20 Carei", ">20 Mako", "~5 Vac", "~5 Karben" and "40 between Changshu, Changchun and
Qingdao"; the slide's table structure did not survive extraction, so it cannot be turned into
a unit cost. Who could supply it: OD lead or regional IIAE, from the eCR calculation
templates.⟩

⟨Whether a Machine List row is brownfield or greenfield: not a field in the list.⟩

## Sources

- Vault `Graph/Machines` (1,715 notes; `Machine-List` export of 2026-08-21), counted 2026-11-05.
- Vault `Graph/Connectors` (26 notes; `ConnectorOverview-List`, export of 2026-08-24) for
  connector names, states and machine counts.
- Vault `ODEC Facts - Department KPIs and Roadmap Status` (staging, unverified) for the one
  cost slide.
- Registry references [`barrier-classes.md`](barrier-classes.md) and
  [`connectors.md`](connectors.md) for the rules cited.
