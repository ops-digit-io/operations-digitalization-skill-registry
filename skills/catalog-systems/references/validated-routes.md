---
type: Skill Reference
title: Validated routes
description: The integration routes that are both written down and proven in the field, by controller family, with machine counts and plant counts from the Machine List - the evidence base for a standard-system entry. Open it before you say "there is a standard system for this machine".
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Validated routes

A route is a **standard-system candidate** when it is (a) written down in full in the equipment-integration guide and (b) proven by machines recorded as `INTEGRATED` through it. The third part of a standard system, a purchasable kit with price and lead time, is **not recorded anywhere** the skill could read, so no row below is a finished standard system. Rows are ranked by evidence.

Sources, all read 2026-11-05:
- Machine List aggregate: the 1,715 notes in vault `Graph/Machines` (fields `plc_vendor`, `plc_model`, `network_protocol`, `integration_status`, `integration_method`), counted by script. 28 plants appear. The list is a SharePoint export of 2026-08-24; 451 machines carry no integration status and 542 carry no method.
- Route status: skill `od-equipment-integration`, `references/decision-paths.md` (rules.json live tree and rules-next.json).
- Connector status: vault `Graph/Connectors` (26 notes) and `references/connectors.md` of the same skill.
- Method names in the list: `IIoT Edge Computing Platform` = Concept 3 (edge route, topologies 1 and 2 of the guide); `Central OPCUA Aggregation Server` = Concept 1 (topology 3); `EVALUATION ONGOING` = 117 machines not yet decided.

## Class A - written route, proven in at least two plants (standard-system candidates)

| Controller family | Route | Machines `INTEGRATED` through it | Plants | Connector (status) | Notes |
|---|---|---:|---:|---|---|
| Siemens S7 / TIA (S7-300, S7-1200, S7-1500) | edge device + `DTQ-S7` / `DTQ-TIA` / `DTQ-S7-NET` | 223 (S7-1500: 76, S7-300: 62, S7-1200: 50; 32 without a model) | 17 | Productive, USE | Only the large edge device is approved; no approved small device (decision-paths). Low-frequency S7-NET is the answer where a device is not wanted |
| Siemens S7 / TIA | Central Aggregation Server (Softing dataFEED) + bridge `DTQ-OPCUA-Connector` | 178 (S7-1200: 56, S7-300: 49, S7-1500: 14, 29 without a model; also S7-200: 15, Sinumerik: 11, LOGO: 4) | 8 | SFT-OPC-Suite Productive; `DTQ-OPCUA` Productive | Needs the edge platform behind the server. `SFT-SIMATIC S7-Connector` is DO NOT USE (no cyber-security-compliant PLC communication) |
| Rockwell / Allen Bradley | edge device + `DTQ-ALLENBRADLEY-ROCKWELL` | 36 (plus 57 with no method recorded, one plant) | 3 | Productive, USE | |
| Rockwell / Allen Bradley | Central Aggregation Server | 20 | 2 | as above | Procedure fully written in rules-next |

Observations: in the Machine List 17 plants have machines integrated through the edge, 11 through the aggregation server and 8 through both (the guide also states eight plants with both), so the choice is per machine, not per plant (`od-equipment-integration`). Of the Machine List's 821 integrated machines, 343 are recorded through the edge, 286 through the aggregation server, 1 under evaluation and 191 with **no method recorded** (4 plants).

## Class B - proven in the field, but the guide's procedure is unwritten (`TODO` or stub)

| Controller family | Route | Machines `INTEGRATED` | Plants | Connector (status) | Why it is not yet a standard system |
|---|---|---:|---:|---|---|
| Beckhoff | edge + `DTQ-Beckhoff` (ADS) | 17 | 2 | Productive, USE; documentation not available | The edge procedure body is `TODO`; Softing has **no Beckhoff driver**; 22 further Beckhoff machines (of 42) are `NOT INTEGRATED` - 15 of them recorded on the edge route, 7 with no method |
| Omron NJ / CJ | edge + `DTQ-OMRON FINS` | 12 | 2 | Productive, USE | Edge body is a task stub; aggregation only "next" |
| Modbus TCP | aggregation server (documented route) | 20 on aggregation, 58 with no method recorded (one plant) | 2 (aggregation) | `DTQ-MODBUS` status `Idea` but utilization `USE` - confirm with the IIAE | Edge body `TODO` |
| Keyence camera / sensor | edge + `DTQ-KEYENCECAM` (FTP) | 12 | 1 | Productive, USE | Non-PLC connector, one plant |

The scaffold treated "Beckhoff on the edge platform" as a route with no record behind it. The Machine List shows **17 machines already integrated that way at two plants**. What is missing is the written procedure and its documentation, not a first deployment. The rule stays: a `TODO` route is not a standard system until the IIAE writes the procedure.

## Class C - proven only through a fallback or with a single plant

| Controller family | Route | Machines `INTEGRATED` | Plants | Connector (status) | Why it is not a candidate |
|---|---|---:|---:|---|---|
| B&R (Automation PC) | aggregation server (dataFEED has a B&R driver) | 29 (30 of 32 machines per decision-paths) | 1 (Dolne Vestenice; the list also holds B&R machines at Waltershausen) | `DTQ-B&R` status `Idea`, not available | Written body is `TODO`; one plant |
| Bachmann (MX213 / MX220) | aggregation server over OPC UA | 16 on aggregation + 28 with no method (includes 24 rows with the vendor spelled "Bachmann OPC") | 2 | `DTQ-Bachmann` status `Idea`, not available | Same; 10 Bachmann machines `NOT INTEGRATED` |
| Mitsubishi (Melsec-Q) | aggregation only | 3 | 2 | none | Task list only; 7 more under evaluation |
| Siemens S7-200 | aggregation | 15 | 2 | `DTQ-S7` covers S7-300/400 | The model is not in the guide's tree |
| Sinumerik NCU | edge + `DTQ-SINUMERIK` (UDP/IP), written in the live tree | 12 (edge 1, aggregation 11) | 2 across both | Productive, USE | Edge evidence is one machine; the aggregation column is marked "next" in the guide, yet 11 machines are recorded on it - the field is ahead of the guide's live tree |
| Engel injection moulding | no vendor connector (decision-paths notes that current Engel controllers serve OPC UA); 31 machines carry no method | 32 (31 with no method) | 2 | `DTQ-Engel EMI` status `Idea`, not available | 38 Engel machines in the list; 6 `NOT INTEGRATED` on aggregation |
| Schneider | no method recorded | 32 | 1 | none | Single plant, route not recorded |

## Class D - no route, or blocked

- **Delta Electronic** (14 machines, all `NOT INTEGRATED`, 2 plants), **Philips** (9, 1 plant), **Mitsubishi** beyond the 3 above (7 under evaluation): no route in the guide. Anything not in the tree is "Integration of Other PLCs": connector development, long lead times (decision-paths) - this is Lane 3b, not 1b.
- **Camera systems** cannot go through the aggregation server; edge only (rules-next).
- A machine **without the PLC program** cannot be connected; see `od-equipment-integration`, `references/fallbacks.md`.
- **Vendor not recorded** on 133 machines (91 of them integrated, 23 not): do not place a machine in a class until its controller is known.

## How to read a machine against this table

1. Controller vendor and model from the Machine List (a blank is unknown, not a "No").
2. Find the row. Class A: continue on branch 1b with that route; cost, lead time and kit are still ⟨to be supplied⟩ (see [standard-system-entry.md](../assets/standard-system-entry.md)).
3. Class B or C: say plainly "this has been done at N plants but the procedure is not written"; hand to the IIAE and `od-barrier-triage` / Lane 3b. Do not offer it as a standard system.
4. Class D or no row: no standard system; hand to `od-system-fit-check` and Lane 3b.

## Open

- ⟨The list of purchasable kits per route, prices and lead times⟩ - OD lead, IIAE, procurement; not in the vault notes read.
- ⟨Why 191 integrated machines (4 plants) carry no method⟩ and ⟨whether the 117 `EVALUATION ONGOING` machines will land on edge or aggregation⟩ - IIAE.
- ⟨Whether the guide's "TODO" for Beckhoff and Omron on the edge is still current⟩ given that 29 machines are integrated that way - IIAE.
