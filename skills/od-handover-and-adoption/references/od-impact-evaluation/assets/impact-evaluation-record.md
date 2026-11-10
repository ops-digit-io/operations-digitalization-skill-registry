---
type: Skill Asset
title: Impact evaluation record
description: The output of od-impact-evaluation - the drafted evaluation of a live use case with each saving shown at its true firmness, plus the adoption confirmation block that the plant owner signs.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice, template]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Impact evaluation and adoption confirmation — ⟨use case, plant, line⟩

Copy once per use case and evaluation date. Sections 1 to 5 are drafted by OD (authority: draft).
Section 6 is the plant owner's. Write `⟨not recorded⟩` rather than leaving a field silent. Do not
add tracked and proven euros.

| | |
|---|---|
| Use case / plant / capability / process group | ⟨⟩ |
| Live since | ⟨date⟩ |
| Evaluation date and trigger | ⟨date; why now (weeks live, Scorecard flag, SPRINT preparation, no saving recorded)⟩ |
| Handover record | ⟨reference to the `od-handover-and-adoption` protocol and date⟩ |

## 1 · The promise (from definition and business case)

| Item | Entry | Source record |
|---|---|---|
| Objective | ⟨⟩ | ⟨definition protocol⟩ |
| Benefit class (tangible/intangible, cashable/non-cashable) | ⟨⟩ | |
| Business or process change named, and who confirms it | ⟨⟩ | |
| Expected utilization | ⟨moment in the day⟩ | |
| Saving rows promised | ⟨count, labels⟩ | ⟨ledger⟩ |

If nothing was written at definition, state "promise not recorded".

## 2 · Usage evidence

| Tier | Evidence | Source | Date |
|---|---|---|---|
| ⟨1 system log · 2 owner's dated statement · 3 observation · none⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

## 3 · Utilization description (OD template fields)

| Field | Entry |
|---|---|
| Who uses it | ⟨⟩ |
| Related process | ⟨⟩ |
| Utilization method, including the initial state without digital support | ⟨1 to 3 sentences⟩ |
| Utilization rate | ⟨Daily / Weekly / Monthly / On-Demand / Never⟩ |
| Impact / potential | ⟨Low / Medium / High⟩ |
| Plant management relevant | ⟨yes/no, why⟩ |

## 4 · What changed

| Decision or action that now differs | Who | How often | Shown by (data or statement) |
|---|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

## 5 · Savings at their true firmness

| Row | Amount, year, period | Baseline | Methodology (formula, inputs) | Label (`CALCULATION` / `ESTIMATION` / none) | Dependency and owner | SPRINT link | Proven? | Next step, owner, date |
|---|---|---|---|---|---|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨or baseline not recorded⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨no unless SPRINT confirmed⟩ | ⟨⟩ |

Totals: tracked ⟨⟩ · proven ⟨⟩ — kept apart, never summed.

**Outcome** (one of, per `SKILL.md` step 7): ⟨adoption confirmed, rows to SPRINT · adoption confirmed,
saving unproven with named gap · no adoption claim, ADKAR diagnostic · adoption gap at other plants,
standardization · rework⟩

## 6 · Adoption confirmation (plant owner)

| Item | Entry |
|---|---|
| Plant owner (role and name as recorded in the plant) | ⟨⟩ |
| Statement | "I used this in a real shift on ⟨date⟩ for ⟨decision or action⟩." ⟨owner's own words⟩ |
| Confirmation | ⟨confirmed on ⟨date⟩ · pending, requested ⟨date⟩ · declined, reason⟩ |
| Retirement considered? | ⟨yes/no, why⟩ |

## 7 · Handed on

| To | What |
|---|---|
| `od-scorecard-reporting` | utilization rate and trend, reopen on the Scorecard cadence |
| `od-benefit-calculation` | rows ready for SPRINT; rows needing a baseline |
| `od-retro` | promise versus outcome |
| `od-use-case-standardization` | if the same asset is wanted at other plants |

## 8 · Open points

⟨what could not be evidenced and who can supply it⟩
