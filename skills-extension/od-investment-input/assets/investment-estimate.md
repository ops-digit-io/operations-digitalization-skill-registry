---
type: Skill Asset
title: Investment estimate
description: "The department's investment and effort estimate template (the cost side of a business case, od-investment-input): one-time build, licences and hardware, recurring run cost, cost summary against bankable value, payback. Never netted into the value headline."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [cost, business-case, template, department-standard]
derived_from:
  - "Department knowledge base, OD Department Knowledge/OD-instance/Business-Cases/_template/investment-estimate-template.md, read 2026-11-10 (the knowledge base file is the master)"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Investment & Effort Estimate — ⟨case name⟩

> Separate from the business case on purpose: the backbone (`od-benefit-calculation`) is value-only.
> When both are filled, value minus cost is the payback the case is decided on.

| Field | Value |
|---|---|
| Case ID | ⟨slug⟩ |
| Linked business case | ⟨link⟩ |
| Estimate status | ⟨not provided / market-based placeholder / quoted / actual⟩ |
| Operating model assumed | ⟨dashboard in production / daily reaction routine / …⟩ |
| Scenario | ⟨minimum viable rollout · maximum scale-out⟩ |
| Owner · last updated | ⟨…⟩ |

Ground rules: tag every figure `[quote]`, `[assumption]` or `[market]`; never state a cost as fact unless
quoted or actual; floor and upside from named drivers, not a single point; run cost depends on the
operating model; scale with the same multiplier as the value side. Ask IT for cloud and run cost drivers
(IT carries them centrally today).

## 1. One-time build effort
| Item | Driver (hours × loaded rate) | Basis | Floor–upside |
|---|---|---|---|
| OD / development effort | ⟨…⟩ | ⟨…⟩ | ⟨…⟩ |
| Key-user / area effort | ⟨…⟩ | ⟨…⟩ | ⟨…⟩ |
| Integration (systems, data) | ⟨…⟩ | ⟨…⟩ | ⟨…⟩ |
| Rollout / training per site | ⟨…⟩ | ⟨…⟩ | ⟨…⟩ |

## 2. Licences and hardware
| Item | Driver | Basis | Amount |
|---|---|---|---|

## 3. Recurring run cost per year
| Item | Driver | Basis | Amount |
|---|---|---|---|
| Hosting / infrastructure / cloud | ⟨ask IT⟩ | ⟨…⟩ | ⟨…⟩ |
| Support / maintenance (who runs it: build-and-run) | ⟨…⟩ | ⟨…⟩ | ⟨…⟩ |

## 4. Cost summary, TCO and payback
| | Floor | Base | Upside |
|---|---|---|---|
| One-time | | | |
| Annual run | | | |
| Multi-year TCO | | | |
| vs bankable value | | | |
| Payback | | | |

## 5. Open items
- ⟨which figures are placeholders and who firms them⟩
