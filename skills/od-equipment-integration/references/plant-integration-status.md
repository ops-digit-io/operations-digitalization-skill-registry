---
type: Skill Reference
title: Plant integration status
description: Plant-by-plant table of machine counts, integration status, route recorded, controller vendors, concepts rolled out, free-text blockers and legacy applications, with flags where the record cannot be read at face value.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Plant integration status

**Record counts, not rules.** Every number in the table is a count of Machine List rows
(`Graph/Machines`, 1,715 notes; the notes quote the SharePoint `Machine-List` export of
2026-08-21) grouped by plant, plus the Tool Overview concept rows (`ToolOverview-List`,
export of 2026-08-24) and the Legacy Application List (export of 2026-08-24). The vault was
read on 2026-11-05. Nothing was re-counted in the source lists; the counts come from the
vault notes. Re-run the count on the live list before quoting a figure in a decision.

How to read a column:

- **Status columns** are the `integration_status` field: `INTEGRATED`, `NOT INTEGRATED`,
  `INTEGRATION ONGOING`, or blank (`no status`). Blank is not "not integrated" (see
  [`od-data-availability-check`](../../od-data-availability-check/SKILL.md)).
- **Route recorded** is the `integration_method` field: `Edge` = IIoT Edge Computing Platform,
  `Aggr.` = Central OPCUA Aggregation Server, `Eval.` = `EVALUATION ONGOING` (the route is
  still undecided for that machine), `none` = field blank.
- **Concepts in Tool Overview**: C1 = Concept 1 central OPC-UA server, C2 = Concept 2
  container-based machine integration, C3 = Concept 3 IIoT edge computing platform, with
  status `AVAILABLE` in the rollout table. A plant can show machines routed to a concept the
  Tool Overview does not list for it (and the reverse); that is a record mismatch to clear
  with the IIAE, not proof either way.
- **Blocker rows** = machines with free text in `integration_blockers`; the text is classified
  in [`blockers-and-waves.md`](blockers-and-waves.md).
- **Legacy apps** = Legacy Application List entries located at the plant
  ([`od-system-fit-check`](../../od-system-fit-check/references/legacy-applications-landscape.md)).

## The table (28 plants with machine rows)

| Plant | Region | Machines | Integr. | Not integr. | Ongoing | No status | Edge | Aggr. | Eval. | none | Controller vendors (top 3) | Concepts in Tool Overview | Blocker rows | Legacy apps | Flags (computed) |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|---|--:|--:|---|
| Auburn | AMERICAS | 60 | 57 | 3 | 0 | 0 | 0 | 0 | 0 | 60 | Rockwell 60 | - | 0 | 1 | method blank on 60; no concept in Tool Overview |
| Caluire | EMEA WEST | 33 | 24 | 8 | 1 | 0 | 4 | 29 | 0 | 0 | Siemens 20, MRA 7, ASI 4 | C1/C3 | 23 | 16 |  |
| Carei | EMEA EAST | 81 | 29 | 8 | 15 | 29 | 53 | 4 | 0 | 24 | Siemens 70, no vendor 11 | C2/C3 | 0 | 2 |  |
| Changchun | APAC | 43 | 21 | 4 | 0 | 18 | 1 | 26 | 0 | 16 | Siemens 33, Mitsubishi 6, INOVANCE 3 | C1 | 0 | 4 |  |
| Changshu | APAC | 99 | 21 | 78 | 0 | 0 | 0 | 30 | 36 | 33 | Siemens 44, Bachmann 19, Philips 9 | C1 | 0 | 3 | route under evaluation for 36; not integrated 78 of 99 |
| Delicias | AMERICAS | 51 | 22 | 0 | 14 | 15 | 36 | 10 | 5 | 0 | Siemens 36, Rockwell 12, no vendor 2 | C3 | 4 | 9 |  |
| Dolne Vestenice | EMEA EAST | 59 | 48 | 0 | 0 | 11 | 8 | 41 | 0 | 10 | B&R 31, Bachmann 20, Siemens 8 | C3 | 0 | 0 |  |
| Hann. Münden | EMEA WEST | 9 | 9 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | Siemens 9 | - | 0 | 3 | no concept in Tool Overview |
| Hannover Stöcken | EMEA WEST | 17 | 2 | 15 | 0 | 0 | 17 | 0 | 0 | 0 | Siemens 17 | - | 0 | 48 | not integrated 15 of 17; no concept in Tool Overview |
| Karben | EMEA WEST | 46 | 23 | 0 | 0 | 23 | 46 | 0 | 0 | 0 | Siemens 34, keyence 12 | C3 | 22 | 6 | status blank on 23 of 46 |
| Korbach | EMEA WEST | 16 | 0 | 16 | 0 | 0 | 5 | 11 | 0 | 0 | Siemens 16 | C1 | 0 | 0 | not integrated 16 of 16 |
| Mako | EMEA EAST | 128 | 71 | 0 | 5 | 52 | 58 | 44 | 0 | 26 | Siemens 101, no vendor 27 | C1/C3 | 17 | 6 |  |
| Montemorelos | AMERICAS | 51 | 0 | 0 | 0 | 51 | 2 | 0 | 45 | 4 | Rockwell 47, Versa 1, Mitsubishi 1 | - | 0 | 22 | status blank on 51 of 51; route under evaluation for 45; no concept in Tool Overview |
| Monterrey | AMERICAS | 82 | 25 | 56 | 1 | 0 | 60 | 15 | 7 | 0 | Rockwell 75, Omron 4, Siemens 2 | C3 | 0 | 37 | not integrated 56 of 82 |
| Northeim | EMEA WEST | 87 | 83 | 4 | 0 | 0 | 14 | 0 | 0 | 73 | Engel 31, Bachmann OPC 24, Siemens 11 | C3 | 0 | 1 | method blank on 73 |
| Ostrava | EMEA EAST | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | no vendor 1 | C1 | 0 | 1 | status blank on 1 of 1; method blank on 1 |
| Ponta Grossa | AMERICAS | 75 | 62 | 13 | 0 | 0 | 0 | 75 | 0 | 0 | Siemens 68, no vendor 3, STANGE Elektronik GmbH 2 | C1 | 0 | 38 |  |
| Qingdao | APAC | 74 | 59 | 12 | 0 | 3 | 54 | 19 | 0 | 1 | Siemens 48, Delta 12, Rockwell 11 | C1 | 0 | 6 |  |
| Rennes | EMEA WEST | 58 | 58 | 0 | 0 | 0 | 0 | 0 | 0 | 58 | Schneider 32, no vendor 26 | - | 0 | 1 | method blank on 58; no concept in Tool Overview |
| San Luis Potosi | AMERICAS | 16 | 0 | 0 | 0 | 16 | 10 | 0 | 0 | 6 | Siemens 12, Beckhoff 3, PIOVAN S.p.A. 1 | C3 | 6 | 1 | status blank on 16 of 16 |
| Somersworth | AMERICAS | 26 | 26 | 0 | 0 | 0 | 26 | 0 | 0 | 0 | Siemens 15, Beckhoff 9, Engel 1 | C1/C3 | 4 | 2 |  |
| Subotica | EMEA EAST | 181 | 27 | 142 | 0 | 12 | 172 | 0 | 0 | 9 | Siemens 134, no vendor 21, Beckhoff 15 | C3 | 21 | 45 | not integrated 142 of 181 |
| Sun Prairie | AMERICAS | 39 | 39 | 0 | 0 | 0 | 0 | 39 | 0 | 0 | no vendor 24, Rockwell 15 | C1 | 0 | 6 |  |
| Tanger | EMEA WEST | 20 | 0 | 19 | 1 | 0 | 0 | 0 | 15 | 5 | Siemens 20 | - | 0 | 0 | route under evaluation for 15; not integrated 19 of 20; no concept in Tool Overview |
| Timisoara | EMEA EAST | 91 | 26 | 0 | 1 | 64 | 29 | 0 | 0 | 62 | Siemens 81, Omron 8, BLM Custom Software 1 | C3 | 1 | 4 | status blank on 64 of 91; method blank on 62 |
| Tlalnepantla | AMERICAS | 82 | 0 | 10 | 0 | 72 | 6 | 7 | 0 | 69 | Siemens 81, Weidec 1 | - | 12 | 2 | status blank on 72 of 82; method blank on 69; no concept in Tool Overview |
| Vac | EMEA EAST | 103 | 20 | 0 | 0 | 83 | 25 | 0 | 0 | 78 | Siemens 99, KEBA Industrial Automation 3, SIGMATEK GmbH 1 | C3 | 0 | 15 | status blank on 83 of 103; method blank on 78 |
| Waltershausen | EMEA WEST | 87 | 69 | 7 | 10 | 1 | 37 | 34 | 9 | 7 | Siemens 72, Beckhoff 8, no vendor 3 | C1/C3 | 0 | 4 |  |
| **All 28 plants** | | 1715 | 821 | 395 | 48 | 451 | 672 | 384 | 117 | 542 | | | 110 | 283 | |

Column sums equal the department totals quoted elsewhere in this registry: 1,715 rows,
821 `INTEGRATED`, 395 `NOT INTEGRATED`, 48 `INTEGRATION ONGOING`, 451 without status. The
legacy column sums to 283 because 10 applications are located at more than one plant (268
applications).

## Record mismatches to clear before using a plant row

These are **counts**, computed on 2026-11-05 from the vault notes. They show where two
records of the same plant disagree. They do not say which one is right.

| Mismatch | Plants |
|---|---|
| Machines routed to the IIoT Edge Computing Platform, but Concept 3 is not in the plant's Tool Overview rows | Changchun (1 machine), Hann. Münden (9), Hannover Stöcken (17), Korbach (5), Montemorelos (2), Qingdao (54), Tlalnepantla (6) |
| Machines routed to the Central OPCUA Aggregation Server, but Concept 1 is not in the plant's Tool Overview rows | Carei (4), Delicias (10), Dolne Vestenice (41), Monterrey (15), Tlalnepantla (7) |
| Concept 1 listed `AVAILABLE`, but no machine carries the aggregation route | Ostrava (its only row has no method), Somersworth (all 26 machines carry the edge route; the Tool Overview note says "Migration from CT to OESL") |

Counting plants by machine route gives **21 plants with at least one edge-routed machine, 14
with at least one aggregation-routed machine, 11 with both**. The Tool Overview rows give
Concept 3 at 14 plants (plus Auburn, whose row carries the comment "Ignition SCADA System"
and no year), Concept 1 at 11 and Concept 2 at 1. The "20 / 11 / 8 plants" figures in
[`SKILL.md`](../SKILL.md) were written on an earlier export and could not be re-derived
here; use the table above for the current record and ask the IIAE which plant list is the
reference. ⟨Which of the two records the department treats as the reference for "plant has
concept X". Who could supply it: IIAE.⟩

## Plants without machine rows

Five of the 33 plant notes carry no machine at all: Andrezieux, Dannenberg, Jeonju, Kranj,
Oedelsheim (plant profile text "no machine list entries"). Andrezieux and Dannenberg have an
Energy Management 2.0 rollout row; Oedelsheim has an Energy Management 1.0 row; Jeonju and
Kranj have no tool row. A plant with no machine row has **no integration record**, not an
integration of zero: the first conversation is an inventory (Route A in
[`SKILL.md`](../SKILL.md)).

## What the table says plant by plant (record readings, dated)

- **Subotica (181 machines)** is the largest plant and the largest open volume: 142
  `NOT INTEGRATED`. 154 rows carry the project reference "Machine Integration Next Wave 2 -
  2025" and 5 carry "… 2026". The `integration_approach` field there records the low-cost
  shapes — "Low Cost - Direct Connection" on 50 machines, "Low Cost - Helmholz" on 19, plain
  "Edge" on 10, "Edge (together with camera)" on 7, Beckhoff clamps on 5 (a Helmholz gateway
  addresses a PLC without Ethernet; see [`decision-paths.md`](decision-paths.md)). 12 rows
  carry the blocker "TIA V16 Upgrade necessary for TIA V17" (11 on S7-1500, 1 on S7-1200, all `NOT
  INTEGRATED`). 45 legacy applications are located here.
- **Changshu (99)**: 78 `NOT INTEGRATED`, 36 with route `EVALUATION ONGOING`, 30 on the
  aggregation server. Vendor mix Siemens 44, Bachmann 19, Philips 9 (Philips rows are all
  `NOT INTEGRATED`, see [`vendor-protocol-routes.md`](vendor-protocol-routes.md)). Seven
  rows record "Prefered Integration with Softing OPC-UA DataFeed Suite". MSB 4.0 is `ONGOING`
  in the Tool Overview.
- **Monterrey (82)**: 56 `NOT INTEGRATED`, 60 edge-routed, Rockwell 75 of 82. Wave project
  reference "Machine Integration Wave 2 - Monterrey" on 57 rows. 37 legacy applications.
- **Montemorelos (51)**: no status on any of the 51 rows, route `EVALUATION ONGOING` on 45,
  Rockwell 47, 22 legacy applications and no use case. The plant has no Tool Overview row.
  This is a plant at the start of the conversation, not a plant with a 0% result.
- **Tlalnepantla (82)**: status blank on 72, method blank on 69, no Tool Overview row; 5 rows
  carry "Cybersecurity Vulnerabilty - Needs to be patched before integration" (all S7-1500).
  The ODEC slide of 2025-11-19 lists Tlalnepantla under "Done in site" for the equipment
  integration regional roadmap (ODEC Facts staging note, AI-extracted, not verified).
- **Northeim (87)**: 83 `INTEGRATED`, but PLC model and network protocol are blank on all 87
  rows and the route is blank on 73. The plant mixes Engel (31), Bachmann OPC (24) and Siemens (11). It is integrated and undocumented at the level a
  second engineer would need ([`od-data-availability-check`](../../od-data-availability-check/references/machine-list-completeness.md)).
- **Vac (103)**: 83 without status, 78 without method, 20 `INTEGRATED`; 99 Siemens. Concept 3
  approved via eSign on 2024-08-28 (Tool Overview comment).
- **Karben (46)**: all edge-routed, 23 `INTEGRATED`, 23 without status; 22 blocker rows on 46 machines — mostly "1x Edge Device … dedicated to Module n needed",
  camera hardware and "PLC Program missing, was wrong" (see
  [`blockers-and-waves.md`](blockers-and-waves.md)). 12 Keyence rows are integrated through the
  RS232 and Keyence camera connectors.
- **Caluire (33)**: 29 aggregation-routed, 23 blocker rows, all of them "Data model
  Standardization (CT Base)" — recorded on rows whose controller is Schneider (11),
  SINUMERIK 840D SL (10) or other (2). 14 of the
  blocker rows sit on machines already `INTEGRATED`.
- **Korbach (16)**: all 16 `NOT INTEGRATED`, although Concept 1, MDA/PDA 3.0, MES 1.0 and MSB
  1.0 are `AVAILABLE` in the Tool Overview since 2022. The tools are there; the machines are
  not connected.
- **Tanger (20)**: 19 `NOT INTEGRATED`, 15 routes under evaluation, approach text on 12 rows
  (Ethernet / IP); one row carries the project reference "Tangier Plant Digitalization Road
  map 2026" with planned integration date 2026-07. No Tool Overview row.
- **Rennes (58)**: all `INTEGRATED` (integration date 2025), method blank on all rows,
  Schneider 32; no Tool Overview row except an Energy Management 1.0 row with "Rollout Year
  missing".
- **Sun Prairie (39)** and **Somersworth (26)**: all `INTEGRATED`. Sun Prairie is
  aggregation-routed ("RSLinx OPC-UA TCP/IP" on 24 rows); Somersworth edge-routed with
  edge devices shared across cells ("Edge Device [Same as BMnn device] via Siemens TCP/IP
  Ethernet Driver" on 12 rows).
- **Ponta Grossa (75)**: all 75 aggregation-routed, 62 `INTEGRATED`, 13 `NOT INTEGRATED`;
  Sinumerik is the largest connector family here (11 machines).
- **Auburn (60)**: 57 `INTEGRATED` (integration date 2025), 3 `NOT INTEGRATED`, Rockwell 60; no method or
  route recorded because the plant runs Ignition SCADA (Tool Overview comment). The Auburn
  MSB assessment workshop of 2025-05-21 (ODEC Facts staging, unverified) lists "Cyber
  Security Assessment for Ignition to be followed up" and states the IT/OT separation is
  done.

## Use

1. For a plant conversation, open the plant's row first, then the machine rows behind it.
2. Treat every **flag** as a question for the Plant ME / Plant IT, not as a finding.
3. When the plant is in a wave, the project reference in `integration_status`'s neighbour
   field names it; see [`blockers-and-waves.md`](blockers-and-waves.md).
4. Quote counts with their export date (machines: 2026-08-21; tools, plants, legacy:
   2026-08-24; vault read 2026-11-05).

## Not in the records

⟨Per-plant lead times, budget, and the date by which a plant's remaining machines are
planned. Planned integration dates exist on 84 rows only (Qingdao, Mako, Sun Prairie,
Changshu, Carei, Tanger); all are earlier than the export date and 63 of them already show
`INTEGRATED`. Who could supply it: OD lead and the regional IIAE.⟩

⟨Production criticality, cyber-security status and input protocol per machine: empty on all
1,715 rows (see [`SKILL.md`](../SKILL.md)).⟩
