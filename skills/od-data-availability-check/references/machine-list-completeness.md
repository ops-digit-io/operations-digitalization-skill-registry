---
type: Skill Reference
title: Machine list completeness
description: How many Machine List rows carry each field, plant by plant, and which plants cannot answer step 2 (is the machine integrated) from the list - so a blank is never read as a no.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Machine list completeness

Step 2 of the six steps asks "is the machine integrated?" and answers from the Machine List.
That answer is only as good as the field behind it. This reference gives the fill rate of
the fields the six steps use, per plant, so you know **before you run the check** whether the
list can speak for the plant at all.

**Record counts.** Source: `Graph/Machines` notes (1,715), quoting the `Machine-List`
SharePoint export of 2026-08-21; counted 2026-11-05. A cell is the number of rows (of the
plant's rows) with a non-empty value. The two last columns of the verdict are computed from
the status column only. A blank is not a "no": see the trap in [`SKILL.md`](../SKILL.md).

| Field | Rows filled (of 1,715) | Share |
|---|--:|--:|
| Controller vendor | 1,582 | 92% |
| PLC model | 1,268 | 74% |
| PLC part number | 1,027 | 60% |
| Network protocol | 1,164 | 68% |
| Integration status | 1,264 | 74% |
| Integration route (method) | 1,173 | 68% |
| Priority | 1,241 | 72% |
| Integration date | 816 | 48% |
| Process area | 1,171 | 68% |
| Project reference | 687 | 40% |
| Free-text approach | 265 | 15% |
| Free-text blockers | 110 | 6% |
| Planned integration date | 84 | 5% |
| Production criticality, cyber-security status, input protocol, machine blockers (typed fields) | 0 | 0% |

## Per plant

| Plant | Rows | Vendor | Model | Protocol | Status | Route | Priority | Integration date | Verdict for step 2 (computed) |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| Auburn | 60 | 60 | 60 | 60 | 60 | 0 | 60 | 57 | status known on all rows |
| Caluire | 33 | 32 | 24 | 30 | 33 | 33 | 0 | 24 | status known on all rows |
| Carei | 81 | 70 | 56 | 55 | 52 | 57 | 42 | 29 | status known on 64% of rows |
| Changchun | 43 | 43 | 26 | 25 | 25 | 27 | 4 | 15 | status known on 58% of rows |
| Changshu | 99 | 98 | 45 | 71 | 99 | 66 | 85 | 21 | status known on all rows |
| Delicias | 51 | 49 | 44 | 23 | 36 | 51 | 36 | 22 | status known on 71% of rows |
| Dolne Vestenice | 59 | 59 | 59 | 38 | 48 | 49 | 59 | 48 | status known on 81% of rows |
| Hann. Münden | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | status known on all rows |
| Hannover Stöcken | 17 | 17 | 17 | 17 | 17 | 17 | 17 | 2 | status known on all rows |
| Karben | 46 | 46 | 39 | 37 | 23 | 46 | 39 | 23 | status known on 50% of rows |
| Korbach | 16 | 16 | 16 | 16 | 16 | 16 | 16 | 0 | status known on all rows |
| Mako | 128 | 101 | 98 | 52 | 76 | 102 | 57 | 72 | status known on 59% of rows |
| Montemorelos | 51 | 50 | 50 | 9 | 0 | 47 | 11 | 0 | status blank on all rows - step 2 cannot be answered from the list |
| Monterrey | 82 | 81 | 75 | 40 | 82 | 82 | 82 | 25 | status known on all rows |
| Northeim | 87 | 79 | 0 | 0 | 87 | 14 | 87 | 83 | status known on all rows |
| Ostrava | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | status blank on all rows - step 2 cannot be answered from the list |
| Ponta Grossa | 75 | 72 | 74 | 71 | 75 | 75 | 20 | 62 | status known on all rows |
| Qingdao | 74 | 71 | 71 | 45 | 71 | 73 | 74 | 59 | status known on 96% of rows |
| Rennes | 58 | 32 | 32 | 58 | 58 | 0 | 58 | 58 | status known on all rows |
| San Luis Potosi | 16 | 16 | 7 | 9 | 0 | 10 | 10 | 0 | status blank on all rows - step 2 cannot be answered from the list |
| Somersworth | 26 | 26 | 25 | 25 | 26 | 26 | 26 | 26 | status known on all rows |
| Subotica | 181 | 160 | 129 | 145 | 169 | 172 | 173 | 27 | status known on 93% of rows |
| Sun Prairie | 39 | 15 | 37 | 39 | 39 | 39 | 39 | 39 | status known on all rows |
| Tanger | 20 | 20 | 20 | 20 | 20 | 15 | 20 | 0 | status known on all rows |
| Timisoara | 91 | 91 | 28 | 28 | 27 | 29 | 29 | 26 | status known on 30% of rows |
| Tlalnepantla | 82 | 82 | 80 | 79 | 10 | 13 | 82 | 0 | status known on 12% of rows |
| Vac | 103 | 103 | 103 | 103 | 20 | 25 | 103 | 20 | status known on 19% of rows |
| Waltershausen | 87 | 84 | 43 | 60 | 86 | 80 | 2 | 69 | status known on 99% of rows |
| **All** | 1715 | 1582 | 1268 | 1164 | 1264 | 1173 | 1241 | 816 | |

## Reading the table

**Plants where step 2 cannot be answered from the list (record counts):**

- **No machine rows at all (5 plants):** Andrezieux, Dannenberg, Jeonju, Kranj, Oedelsheim.
  This is step 1 (does a machine produce the signal) and the list has no inventory. The
  answer comes from the plant, not from the list.
- **Status blank on every row:** Montemorelos (51 rows), San Luis Potosi (16), Ostrava (1).
- **Status blank on most rows:** Tlalnepantla (72 of 82), Vac (83 of 103), Timisoara (64 of 91),
  Changchun (18 of 43), Mako (52 of 128), Carei (29 of 81), Delicias (15 of 51), Karben (23 of
  46). Do not report these as "not integrated"; they are "not recorded".

**Plants where status is complete but the list cannot support a second engineer:**

- **Northeim:** 87 of 87 status values, 83 of them `INTEGRATED`, but PLC model and network
  protocol are empty on every row and the route is empty on 73. Step 2 is answered; steps 3
  and 4 (which connector, which route) are not.
- **Rennes:** status and protocol on all 58 rows, but no route recorded and no Tool Overview
  concept row.
- **Auburn:** vendor, model, protocol, status all filled, but no route; the plant's Concept 3
  row in the Tool Overview has no year and the comment "Ignition SCADA System".
- **Ponta Grossa:** status on all rows, priority on 20 of 75.
- **Waltershausen:** priority on 2 of 87.

**Fields that are empty everywhere:** production criticality, cyber-security status, input
protocol and machine blockers as typed fields are empty on all 1,715 rows (the blocker
free text is a different field, filled on 110 rows; see
[`blockers-and-waves.md`](../../od-equipment-integration/references/blockers-and-waves.md)).
So the question "is this machine critical" or "is its cyber-security status approved"
cannot be answered from the list for any machine.

**Dates.** 816 rows carry an integration date; 7 rows are `INTEGRATED` with no date and 2
rows have a date but are not `INTEGRATED`. A date is the best evidence that a machine has
been delivering data since then, but the list does not say it still does (step 5, fitness
for use, is unchanged: always unproven from the bundle).

## Procedure for a key user

1. Look up the plant in the table above. If the status column is below 100%, say in the
   verdict that step 2 is "not recorded" for the share of rows missing.
2. For the machines the request needs, ask the Plant ME for the actual status and record it
   in the Machine List (the SharePoint list is the write surface; a correction made in the
   knowledge graph does not travel, per the department's *Systems of record* note).
3. Where the list shows `INTEGRATED` but vendor, model or route is blank, treat steps 3 and
   4 as unproven and ask the IIAE for the connector chain before promising a signal.
4. Match a vendor by all its spellings (`Bachmann Electronic GmbH` and `Bachmann OPC`, `Keba`
   and `KEBA Industrial Automation`, `VIPA` and `Vipa`, and 59 further rows in other
   spellings). A single-string match undercounts.
5. If the Machine List row looks tidied (`-`), the narrative may be in the version history:
   the department's note on the SharePoint lists says text was often written during active
   work and then tidied back; the vault's `SharePoint record (full text)` block of the
   machine note shows earlier values when they exist.

## What the script does with these gaps

[`scripts/check_availability.py`](../scripts/check_availability.py) reports *unproven* for a
step it cannot answer and never *absent*. For plants in the blank-status groups above, expect
step 2 to come back unproven for most machines. That is the correct result and not a defect
of the check: the remedy is a Machine List update by the plant, which is a data request, not
an integration request.

⟨Whether the Machine List is audited for completeness anywhere (a periodic check or an
owner per plant). Who could supply it: OD lead.⟩

## Sources

- Vault `Graph/Machines` (1,715 notes; `Machine-List` export 2026-08-21), counted 2026-11-05.
- Department note *Systems of record* (`_knowledge/10-Department/Systems of record.md`):
  write surface, version history, absence is not a zero.
