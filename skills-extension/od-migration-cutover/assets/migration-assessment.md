---
type: Skill Asset
title: Migration assessment
description: Template for the assessment of a legacy application or platform - scenarios, as-is/to-be canvas, component inventory, risk and recovery-impact table, OT application rating, target mapping and staged plan.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [migration, template]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Migration assessment - `<application or platform>` at `<location or kind of plant>`

| | |
|---|---|
| Prepared by / date | `<role>` / `<date>` |
| Status | Draft for the OD lead and the plant; ratings are confirmed by the local owner |
| Decision it follows | `<replace / integrate / keep>` from `<od-application-consulting record>` |

## 1 Scenarios
| Scenario | Consequences | Cost / risk |
|---|---|---|
| Continue as-is (mandatory baseline) | `<security, patching, know-how, support end>` | `<>` |
| `<migrate to target>` | `<>` | `<>` |
| `<alternative>` | `<>` | `<>` |

## 2 As-is / to-be canvas
| Use case / function | As-is | To-be | Preserve / change / drop | Users | Machines, interfaces |
|---|---|---|---|---|---|
| `<>` | `<>` | `<>` | `<>` | `<>` | `<>` |

Status rows: security `<as-is -> to-be>`; service bus `<>`; recipe management `<>`; MES `<>`.

## 3 Component inventory and target mapping
| Component | Owner | Interfaces | Version | Support / licence | To-be component | Replace / keep / merge / drop |
|---|---|---|---|---|---|---|
| `<>` | `<role>` | `<>` | `<>` | `<>` | `<>` | `<>` |

## 4 Risk and recovery impact
| Component | Risk and trigger | Likelihood | Recovery class (stop / traceability / data loss / convenience) | Recovery lead time | Mitigation | Owner |
|---|---|---|---|---|---|---|
| `<>` | `<>` | `<>` | `<>` | `<>` | `<>` | `<>` |

## 5 OT application rating (local owner confirms)
| Application | Interfaced machines | Production criticality (critical / moderate / minimal) | Reason | Customer impact | Reason | Support concept | Cyber status | Confirmed by / date |
|---|---|---|---|---|---|---|---|---|
| `<>` | `<>` | `<>` | `<>` | `<>` | `<>` | `<>` | `<>` | `<role / date>` |

## 6 Staged plan
| Stage | Content | Location / machine | Resources and roles | Cost | Risk | Exit criterion | Back-out ref |
|---|---|---|---|---|---|---|---|
| `<n>` | `<lowest-risk first>` | `<>` | `<>` | `<>` | `<>` | `<>` | `<>` |

## 7 Preconditions and open items
`<registry, repository, firewall, approvals, licences, fixed external dates>` - owner, due.
