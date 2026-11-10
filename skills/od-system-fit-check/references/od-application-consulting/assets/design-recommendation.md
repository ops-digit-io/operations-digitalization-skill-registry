---
type: Skill Asset
title: Design recommendation
description: The form for one application consulting answer - need, footprint verdict, existing apps, data path, build path, gates, run owner, open items; a proposed form until the lane confirms its session template.
resource: ../procedure.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice, template]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Application design recommendation - ⟨question, one line⟩

Proposed form: the lane's "application consultancy session" template is still `⟨to confirm⟩`. This is a
recommendation; the plant and the OD lead decide.

| | |
|---|---|
| **Asked by / plant** | ⟨role⟩ · ⟨plant⟩ |
| **Date / prepared by** | ⟨date⟩ · ⟨role⟩ |
| **Project it belongs to** | ⟨investment project, use case id, or none⟩ |

## 1 The need

In the requester's words: ⟨⟩. In plain words, naming no system: ⟨⟩. Requirement spec: ⟨link to
`od-requirements-breakdown` output⟩.

## 2 Footprint verdict (`od-system-fit-check`)

| Check | Result |
|---|---|
| Tool boundary crossed? | ⟨which tool's "is not" line, or none⟩ |
| Available at this plant, dated | ⟨tool · status · date⟩ |
| Verdict | ⟨fits · redesign onto a lighter tool · escalate as exception⟩ |

## 3 Existing apps considered

| Candidate | Where it runs | Does it cover the need? | Support / licence / network | Keep · integrate · replace |
|---|---|---|---|---|
| ⟨library reference solution⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| ⟨plant-local application⟩ | ⟨⟩ | ⟨⟩ | ⟨unknowns as ⟨⟩⟩ | ⟨⟩ |

## 4 Data path

| Data object | Single source | On the path today? | Gap routed to |
|---|---|---|---|
| ⟨⟩ | ⟨edge · data platform · MSB · other⟩ | ⟨yes/no, verified by `od-data-availability-check`⟩ | ⟨integration lane · none⟩ |

## 5 Recommended build path

⟨3a.1 reuse · 3a.2 self-develop · 3a.3 external development · 3a.4 integrate a foreign app⟩, because
⟨selecting answer⟩. Alternatives rejected and why: ⟨⟩.

## 6 Cross-plant compatibility

⟨Do the signals and interfaces stay consumable by every plant's instance of the capability? Cluster or
capability template: ⟨⟩. Plant-specific parts kept as deltas: ⟨⟩.⟩

## 7 Gates

| Gate | Needed? | Route / skill | State |
|---|---|---|---|
| Tool / system rollout decision | ⟨⟩ | `od-decision-routing` | ⟨⟩ |
| IT demand | ⟨⟩ | `it-demand-package` | ⟨⟩ |
| Cyber Security / OT | ⟨⟩ | `od-cybersec-gate` | ⟨⟩ |
| Spend (eCR) | ⟨⟩ | `od-investment-input` | ⟨⟩ |
| Licensing | ⟨owner to confirm⟩ | | ⟨⟩ |

## 8 After go-live

Plant owner: ⟨role⟩. Support: ⟨internal · external contract · maintenance and run concept · open⟩. Data
path written down to the machine (`od-handover-and-adoption`, question 2): ⟨yes/no⟩. Acceptance:
`od-acceptance-test`, signed off by humans.

## 9 Value and cost

Benefit: ⟨link to `od-benefit-calculation` rows, tracked and proven shown separately, or "to be
collected"⟩. Cost: ⟨`od-investment-input` pack or open⟩.

## 10 Still open

⟨What is unknown, who can supply it⟩

## 11 Recommendation

⟨One paragraph.⟩
