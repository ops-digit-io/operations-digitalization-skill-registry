---
type: Skill Asset
title: Prioritization record
description: The output of od-use-case-prioritization - one record per plant round holding the candidates, the agreed criteria and weights, the scores with evidence, the unscored bucket and the Plant ME sign-off.
resource: ../procedure.md
status: draft
tags: [use-case-support-service, practice, template]
---
# Prioritization record — ⟨plant / region and category⟩ — ⟨round date⟩

Copy once per round. Fill with facts from the use case records; write `⟨not recorded⟩` where a
field is empty. Authority: **recommend** (DBVE with Plant ME, Tandem). Nothing here commits money,
integration or a connection.

| | |
|---|---|
| Comparison set | ⟨one plant roadmap, or one category in one region⟩ |
| DBVE | ⟨role holder⟩ |
| Plant ME | ⟨role holder⟩ |
| Inputs of this round | ⟨technical inputs · latest workshop · latest plant priority⟩ |
| Roadmap / strategic-plant scope checked | ⟨yes/no, where⟩ |

## 1 · Candidates and intake result

| # | Use case | Plant | Capability / process group | Category | Intake (admit / return) | Reason if returned |
|---|---|---|---|---|---|---|
| 1 | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨standard cross / standard per process / non-standard / AI⟩ | ⟨⟩ | ⟨⟩ |

Returned candidates are listed here and go back to the demand owner with the written reason.

## 2 · Criteria and weights agreed for this round

| Criterion | Weight | Agreed with Plant ME on |
|---|---|---|
| Saving potential (tracked rows, reliability) | ⟨⟩ | ⟨date⟩ |
| Generalization potential | ⟨⟩ | |
| Roadmap fit | ⟨⟩ | |
| Effort: dependencies, data readiness, category, solution fit | ⟨⟩ | |

Weights come from OD lead and Plant ME; none are given by the sources (see `SKILL.md`).

## 3 · Evidence per candidate

| # | Saving rows (amount, year, reliability, proven?) | Case group and stage per plant | Group savings basis | Dependencies and owner | Data ready? | Fit check done? |
|---|---|---|---|---|---|---|
| 1 | ⟨or "not recorded"⟩ | ⟨CG-xx; Delivered n / Planned n / Idea n⟩ | ⟨Weak / Very weak / None⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

Do not merge tracked and proven euros in any column.

## 4 · Ranked list (scored candidates only)

| Rank | Use case | Score or quadrant | Main reason | Open dependency / wait state | Next step and owner |
|---|---|---|---|---|---|
| 1 | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨Cyber Security sign-off / investment approval / none⟩ | ⟨⟩ |

## 5 · Unscored bucket (reported next to the list, not at its bottom)

| Use case | What is missing (priority / potential / saving / objective) | Who can supply it |
|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ |

## 6 · Recommendation and agreement

| Item | Entry |
|---|---|
| Recommended order for the next planning window | ⟨⟩ |
| Plant ME agrees? | ⟨yes / yes with change / no⟩ |
| Changes requested by the Plant ME and why | ⟨⟩ |
| Evidence-collection items passed to `deploy-handover` | ⟨delivered use cases without a recorded saving⟩ |
| Money questions passed to `bc-cost` | ⟨⟩ |
| Escalation to OD lead needed? | ⟨blocked use case: missing system or operations concept, no business case, failed acceptance⟩ |

## 7 · Open points

⟨what the sources and the use case records could not answer, and who can supply it⟩
