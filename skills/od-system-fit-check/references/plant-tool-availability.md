---
type: Skill Reference
title: Plant tool availability
description: Matrix of the sixteen tool rows against the plants that carry them (available, ongoing, stopped, planned, not available, with rollout year), how many use cases name each tool, and how the matrix disagrees with the per-workshop snapshots - for step 3 of the system fit check.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Plant tool availability

Step 3 of the check is "check this plant's actual availability, not the estate average". This
reference gives the estate-wide record in one table, so the first lookup takes a minute and
the question to the plant is already specific.

**Record counts.** Source: the Tool Overview as quoted in the vault's `Graph/Tools` notes (16
tools; `ToolOverview-List` export of 2026-08-24; each note carries a "Rollout History" line and
a rollout table), merged by this analysis on 2026-11-05. The "used by" counts come from the use
case links (`UseCase-List`, export of 2026-08-21). Where the two forms of one tool note differ
(the rollout table of Energy Management 2.0 lacks Monterrey; the table of Energy Management 1.0
lacks three plants whose rollout year is missing) the union is shown.

**Reading the cells.** Letter = status, number = rollout year (last two digits), `?` = year
missing. `A` available, `O` ongoing, `S` stopped (management decision), `P` planned next year
(not started), `N` not available. Empty = **no row for this plant**, which is not the same as
"not available": it means nobody recorded a decision. Tool abbreviations: C1 Concept 1
central OPC-UA server, C2 Concept 2 container-based machine integration, C3 Concept 3 IIoT
edge computing platform, MDA1/2/3 MDA/PDA versions, MSB1/2/4 Manufacturing Service Bus
versions, MES, MIL Manufacturing Image Library, QFPR Quality Feedback and Part Routing, RE2
RuleEngine 2.0, EM1/EM2 Energy Management (WiriTec) versions, DSF Data Science Factory.

## The matrix (27 plants with at least one tool row)

| Plant | C1 | C2 | C3 | MDA1 | MDA2 | MDA3 | MSB1 | MSB2 | MSB4 | MES | MIL | QFPR | RE2 | EM1 | EM2 | DSF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Andrezieux |  |  |  |  |  |  |  |  |  |  |  |  |  |  | A23 |  |
| Auburn |  |  | A? |  |  | A? |  |  | P? |  |  |  | P? |  | N23 |  |
| Caluire | A21 |  | A21 |  | A21 | A23 |  | A21 |  |  |  |  | A23 |  | A22 |  |
| Carei |  | A22 | A22 |  | A22 |  |  |  | A22 |  |  |  | A22 | A18 | A23 | S24 |
| Changchun | A22 |  |  | A22 |  |  | A22 |  | O24 |  |  |  | A22 |  |  |  |
| Changshu | A22 |  |  | A22 |  |  | A22 |  | O24 |  |  |  | A22 |  | A19 |  |
| Dannenberg |  |  |  |  |  |  |  |  |  |  |  |  |  | A? | A23 |  |
| Delicias |  |  | A22 |  | A22 |  |  | A22 |  |  | S23 |  | A22 |  | A23 |  |
| Dolne Vestenice |  |  | A24 |  | A24 |  |  |  | A24 |  | S24 |  | A24 |  |  |  |
| Hann. Münden |  |  |  |  |  |  |  |  |  |  |  |  |  | A18 |  |  |
| Karben |  |  | A22 |  | A22 |  |  |  | A22 |  |  |  | A22 | A16 |  |  |
| Korbach | A22 |  |  |  |  | A22 | A22 |  |  | A22 |  |  |  |  | A25 |  |
| Mako | A20 |  | A23 | A20 | A23 |  |  | A20 | A24 |  | S22 |  | A23 |  | A22 |  |
| Monterrey |  |  | A22 |  | A22 |  |  | A22 |  |  |  | O23 | A22 |  | A22 |  |
| Northeim |  |  | A25 |  | A25 |  |  |  | A25 |  | O23 |  | A25 | A25 | A23 | O23 |
| Oedelsheim |  |  |  |  |  |  |  |  |  |  |  |  |  | A18 |  |  |
| Ostrava | A25 |  |  |  |  |  |  |  |  |  |  |  |  |  | A25 |  |
| Ponta Grossa | A20 |  |  | A20 |  |  |  | A20 |  |  |  |  | A20 |  | A23 |  |
| Qingdao | A22 |  |  | A22 |  |  |  | A22 | O24 |  |  |  | A22 |  | A23 |  |
| Rennes |  |  |  |  |  |  |  |  |  |  |  |  |  | A? |  |  |
| San Luis Potosi |  |  | A25 |  | A25 |  |  | A25 |  |  |  |  | A25 |  |  |  |
| Somersworth | A25 |  | A22 |  | A22 |  |  | A22 |  |  |  |  | A22 |  | A23 |  |
| Subotica |  |  | A22 |  | A22 |  |  | A22 |  |  |  |  | A22 |  | A23 |  |
| Sun Prairie | A22 |  |  | A22 |  |  |  | A22 |  |  |  |  | A22 |  | A23 |  |
| Timisoara |  |  | A22 |  | A22 |  |  | A22 |  |  |  |  | A22 |  | A23 |  |
| Vac |  |  | A23 |  | A23 |  |  | A23 |  |  |  |  | A23 |  |  |  |
| Waltershausen | A23 |  | A19 |  | A19 | A23 |  | A19 | A23 |  |  | A21 | A21 |  | A23 | S24 |

Six plants of the 33 have no tool row at all: Jeonju, Kranj, Tanger, Tlalnepantla,
Montemorelos, Hannover Stöcken. Four of them have machines in the Machine List (Tanger 20,
Tlalnepantla 82, Montemorelos 51, Hannover Stöcken 17). For them, "which tools are available"
has no record, and the answer is a question to the plant, not a finding.

## Per tool: plants and use cases (record counts)

| Tool | Plant rows (distinct plants in the matrix) | Use cases naming the tool | Plants of those | Status of those use cases |
|---|---|--:|--:|---|
| Concept 3, IIoT edge computing platform | 14 (15 with Auburn's comment row) | 200 | 16 | productive 74, implemented 55, planned 37, idea 34 |
| Concept 1, central OPC-UA server | 11 | 24 | 6 | idea 15, productive 5, implemented 2, planned 2 |
| Concept 2, container-based machine integration | 1 (Carei) | 85 | 13 | idea 49, planned 18, productive 12, implemented 6 |
| MSB 2.0 | 13 | 184 | 18 | idea 77, productive 49, planned 30, implemented 28 |
| MSB 4.0 | 9 (available 6, ongoing 3) plus Auburn planned | 90 | 10 | productive 35, implemented 29, planned 22, idea 2 |
| MSB 1.0 | 3 | 31 | 6 | planned 9, idea 8, implemented 8, productive 6 |
| RuleEngine 2.0 | 19 plus Auburn planned | 203 | 18 | productive 70, idea 61, planned 38, implemented 34 |
| MDA/PDA 2.0 | 14 | 28 | 11 | idea 21, productive 3, implemented 2, planned 2 |
| MDA/PDA 1.0 | 6 | 12 | 4 | idea 10, implemented 1, planned 1 |
| MDA/PDA 3.0 | 3 plus Auburn | 20 | 5 | idea 17, productive 1, implemented 1, planned 1 |
| Energy Management 2.0 | 19 plants, 24 records (23 available, 1 not available) | 6 | 5 | idea 6 |
| Energy Management 1.0 | 4 table rows, 7 plants in the history line | 1 | 1 | productive 1 |
| QFPR | 2 (Waltershausen available, Monterrey ongoing) | 27 | 8 | idea 19, planned 3, implemented 3, productive 2 |
| MIL 1.0 | 1 ongoing (Northeim); stopped at 3 | 19 | 9 | idea 14, implemented 3, planned 1, productive 1 |
| Data Science Factory | 1 ongoing (Northeim); stopped at 2 | 6 | 4 | productive 4, implemented 1, planned 1 |
| MES 1.0 | 1 (Korbach, 2022) | not recorded in the note | | |

**Readings (this analysis):**

1. **The tool a use case names is not the tool the plant has.** MIL 1.0 is named by 19 use
   cases at 9 plants but is `ONGOING` at one plant and `STOPPED (MANAGEMENT DECISION)` at three.
   QFPR is named by 27 use cases at 8 plants and has two plant rows. Energy Management 2.0 is
   available at 18 plants and named by 6 use cases, all at idea status. Concept 2 is named by 85
   use cases at 13 plants although only Carei has a Concept 2 row. Before accepting a use
   case that "uses" a tool, check the plant row above.
2. **MES: one plant.** Only Korbach carries a row (MES 1.0, available 2022). This matches the
   non-bet "no standardized MES rollout" and the "not available" lines in
   [`deployment-reality.md`](deployment-reality.md).
3. **Stopped means a recorded management decision, with the reason in the comment:** MIL at
   Delicias (2023), Mako (2022), Dolne Vestenice (2024; comment "Alternative for Delicias
   (Tesla)"); Data Science Factory at Carei (2024; comment "Energy Management Use Cases as
   Enabler") and Waltershausen (2024). Treat these as constraints on a new request for the
   same tool at the same plant, and route a challenge through `od-decision-routing`'s tool or
   system rollout decision row.
4. **Ongoing is not available.** Ongoing rows: MSB 4.0 at Changchun, Changshu and Qingdao
   (2024); QFPR at Monterrey (comment "eCR review and iteration done - December 2023"); MIL
   and Data Science Factory at Northeim (2023; MIL comment "Highlighted to IT"; Data Science
   Factory comment "Conjunction with MIL").
5. **Planned next year, not started:** MSB 4.0 and RuleEngine 2.0 at Auburn. Auburn's other
   rows: Concept 3 "Ignition SCADA System", MDA/PDA 3.0 "Dashboarding AddOn with SQL", Energy
   Management 2.0 not available.

6. **The EMS discrepancy in `SKILL.md`, in counts.** `non-bets.md` says EMS rollout is stopped.
   The Tool Overview carries an Energy Management row for 23 plants (versions 1.0 and 2.0
   together; 22 `AVAILABLE`, Auburn "Not Available"), and the tool notes record a 2025
   migration of WiriTec instances from ContiTech-managed to OESL-managed servers (13 of 17
   locations done by 2025-10-20; staging-grade source). Whether the "stopped" statement applies
   only to new plants is not stated in any note read.
   ⟨Which of the two is the current department position. Who could supply it: OD lead.⟩ Keep
   asking, as `SKILL.md` instructs.

### Comments on rollout rows worth knowing (as written)

| Plant and tool | Comment on the row |
|---|---|
| Delicias, Concept 3 | "Handover: 12.12.2023" |
| Vac, Concept 3 / MDA/PDA 2.0 / MSB 2.0 / RuleEngine 2.0 | "approved via eSign (2024-08-28)", with an approval list identifier |
| Dolne Vestenice, Concept 3 and others | "Available as per 18.03.2025" |
| Caluire, MDA/PDA 3.0 | "Handover done - with open topics" |
| Ostrava, Concept 1 and Energy Management 2.0 | "New Rollout 2025 - taken over from CT" |
| Somersworth, Concept 1 | "Migration from CT to OESL" |
| Mako, MSB 2.0 | "MSB will be upgraded during 2022 to include the MQTT and the LFT" |
| Karben, Carei, Hann. Münden, Energy Management 1.0 | "Still Local System > Potential for Cloud" |
| Korbach, Energy Management 2.0 | "Migration from CT to OESL + Special Case Utilization" |
| Changshu, Energy Management 2.0 | "Cloud Migration in 2025 + System Upgrade" |
| Sun Prairie, Energy Management 2.0 | "Re-activation during Migration CT to OESL" |
| Somersworth, Energy Management 2.0 | "API might not be available" |

## The matrix against the three workshop snapshots in `deployment-reality.md`

The snapshots in [`deployment-reality.md`](deployment-reality.md) are statements of one
workshop summary at one date. The Tool Overview is an export of 2026-08-24. They do not agree
everywhere, and the differences are the reason the check says "this plant, dated":

| Tool and plant | Workshop snapshot | Tool Overview export 2026-08-24 |
|---|---|---|
| QFPR, Subotica and Carei | "Ongoing - needed for multiple use cases" (May 2024) | No QFPR row for Subotica or Carei. The QFPR tool note records test instances at Carei, Delicias, Monterrey and Somersworth during 2024 and Carei and Monterrey as first-mover plants |
| IIoT edge platform and MSB, San Luis Potosi | "Ongoing - planned 2023" (Dec 2023) | Concept 3, MSB 2.0, MDA/PDA 2.0 and RuleEngine 2.0 `AVAILABLE` 2025 |
| Data Science Factory, Timisoara | "Ongoing - planned 2025" (Jul 2024) | No row for Timisoara; Northeim ongoing, Carei and Waltershausen stopped |
| MIL, Subotica and Timisoara | demo or test system deployed, "No use cases yet" | No MIL row for either plant (rows only at Northeim, Delicias, Mako, Dolne Vestenice) |
| MES | not available, "not necessary" or "not recommended as of now" at all three | One row, Korbach |

**Rule (existing `SKILL.md`):** when the table and the workshop disagree, the verdict states
both with their dates and asks the plant. Neither wins by being newer.

## Using it in the check

1. Take the tool the need maps to (step 2 of the check).
2. Read the row for the plant. Letter `A` with a year: available in the record. Empty: no
   record, ask. `S`, `O`, `P` or `N`: say so, and do not call it available.
3. Note the machine side: a tool that needs machine data (MDA/PDA, MSB, RuleEngine) needs the
   plant's machines integrated ([`plant-integration-status.md`](../../od-equipment-integration/references/plant-integration-status.md)).
4. Write the plant, the cell value and the export date into
   [`../assets/system-fit-check.md`](../assets/system-fit-check.md).

⟨Whether the Tool Overview is the department's reference for "available at plant", or the
workshop tool-availability tables. Who could supply it: OD lead.⟩

## Sources

- Vault `Graph/Tools` (16 notes), read 2026-11-05; `Graph/Plants` rollout blocks.
- Registry reference [`deployment-reality.md`](deployment-reality.md).
