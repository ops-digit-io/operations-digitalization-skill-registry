---
type: Skill Asset
title: Investment input pack
description: The pack handed to the OD lead and BA Operations - scope, cost lines with sources, benefit side, gates, dependencies and open items; a proposed form until the lane confirms its investment plan template.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice, template]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Investment input - ⟨plant · wave or system⟩

Proposed form. The lane's own investment plan template is still `⟨to confirm⟩`. Fill each cell with a
figure and its source, or with `⟨not known: who can supply⟩`. Nothing in this pack is an approval.

| | |
|---|---|
| **Pack type** | ⟨wave pack · Lane 1b cost template · cost side for a capital request⟩ |
| **Plant / region** | ⟨⟩ |
| **Prepared by / date** | ⟨role⟩ · ⟨date⟩ |
| **Agreed plan it rests on** | ⟨assessment protocol / roadmap / catalog match record, with date and who agreed⟩ |
| **Decider (recommendation goes to)** | OD lead, together with BA Operations (Consultation) |

## 1 Scope after the demand filter

| Machine or system | Use case that needs it | Planned variant (edge / aggregation / vendor) | Barrier tier | Sequence |
|---|---|---|---|---|
| ⟨⟩ | ⟨accepted or planned use case⟩ | ⟨⟩ | ⟨per barrier-classes⟩ | ⟨n of m⟩ |

Left out because no use case waits for it: ⟨which and why⟩.

## 2 Cost lines

| Line | Quantity | Figure | Source and date | Open: who supplies |
|---|--:|---|---|---|
| Edge device (large) | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨IIAE⟩ |
| OT hardware, cabling, network drop | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨Plant ME / IT⟩ |
| IT infrastructure and licences | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨Plant IT⟩ |
| Connector development | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨IIAE⟩ |
| PLC program (supplier) or PLC program change | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨Plant ME⟩ |
| Sensors or camera instead of reading the machine | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| Cyber Security / OT review | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| Training and rollout | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| Internal effort | ⟨priced or not, per OD lead⟩ | ⟨⟩ | ⟨⟩ | ⟨OD lead⟩ |
| **Total** | | ⟨sum of sourced lines only; list the unsourced lines beside it⟩ | | |

Total amount and its scope (per item / plant / programme): ⟨⟩. Route: eCR ⟨approver per the current approval policy; route open where the recorded limits
overlap⟩. Digitalization investment planning threshold: ⟨to confirm⟩.

## 3 Benefit side

| Use case | Saving rows (link) | Tracked EUR | Proven EUR | Reliability | Dependency recorded |
|---|---|--:|--:|---|---|
| ⟨⟩ | ⟨od-benefit-calculation record⟩ | ⟨⟩ | ⟨⟩ | ⟨CALCULATION / ESTIMATION / not recorded⟩ | ⟨ECR APPROVAL · ECR CREATION · MACHINE INTEGRATION · other⟩ |

Tracked and proven are never added. Where no row exists: "to be collected", no payback stated.

## 4 Alternatives considered

| Option | Cost | Why not chosen or chosen |
|---|---|---|
| Cheaper route per the decision paths (OPC-UA server already present; vendor connector; file drop) | ⟨⟩ | ⟨⟩ |
| Substitution or retrofit (see `od-barrier-triage`) | ⟨⟩ | ⟨⟩ |
| Do nothing | | ⟨use case stays blocked: which⟩ |

## 5 Gates

| Gate | Needed? | Owner | State |
|---|---|---|---|
| Spend (eCR) | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| Cyber Security / OT | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| IT demand | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| Tool / system rollout | ⟨⟩ | ⟨⟩ | ⟨⟩ |

## 6 Still open

| Item | Who can supply | Needed before |
|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ |

## 7 Recommendation

⟨One paragraph: go, go with changes, hold, with the reason. Recommendation only; the decision is the OD
lead's.⟩ Decision request filed (`od-decision-routing`): ⟨reference⟩.
