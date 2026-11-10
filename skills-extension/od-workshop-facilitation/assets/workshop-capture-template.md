---
type: Skill Asset
title: Workshop capture template
description: The sheet to fill during a definition or integration workshop - use case demand with canvas fields, savings pre-evaluation, tool availability, machine demands, utilization and decisions - so output can be read by someone who was not in the room.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice, template]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Workshop capture — ⟨plant⟩ — ⟨format⟩ — ⟨dates⟩

Fill live. Write `⟨not recorded⟩` instead of guessing. Roles, not names. Every figure carries its
basis. Sections follow the order of OD's own workshop blocks.

## 1 · Plant tour notes (day 2, block 2.1)

| Area / process | Priority machines seen | Current projects (for example MSB rollout, QFPR rollout) | Pain points heard | Custom connector or SCADA topics |
|---|---|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

## 2 · Demand list (day 2, block 2.2) — one row per need

Check each need against the existing use case list and the library first. Questions to ask are in
`od-use-case-definition`'s questionnaire (is it one need, how often, same problem for five people,
already logged).

| # | Need in one sentence | Process / area | Moment in the day it belongs to | Already logged? (id) | Library precedent | Category (standard cross / per process / non-standard / AI) | Plant owner (role) |
|---|---|---|---|---|---|---|---|
| 1 | ⟨⟩ | ⟨⟩ | ⟨Daily Gemba · Troubleshooting · Activity Tracking · Utilization Improvement · Process Improvement · Quality Improvement · Traceability · Energy Reporting⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

A need raised once, as an incident, with no recurrence is a first-aid case: log it for
`od-first-aid-kit`.

## 3 · Use Case Canvas per promising need (fields of OD's canvas)

| Field | Entry |
|---|---|
| Description of challenge (manufacturing task supported; processes and steps; question or challenge; objective; strategic manufacturing goal; external customer requirement?) | ⟨⟩ |
| Current state of affairs (how the task is done now; who does what; objective of the current process; where the same process applies) | ⟨⟩ |
| Solution idea (how data and analytics help; components; techniques; value proposition) | ⟨⟩ |
| Obstacles / risks | ⟨⟩ |
| Requirements / gaps | ⟨⟩ |
| Data | ⟨signals, source machines, quality records⟩ |
| Infrastructure | ⟨network, edge, servers⟩ |
| Stakeholders / roles (who is involved, who uses it, who is the customer, capacity) | ⟨⟩ |
| Scalability (where else, can it be generalized, effort, what could block it) | ⟨⟩ |
| Dependencies (other use cases, projects, goals) | ⟨⟩ |
| Success criteria (how success and failure are measured; how business impact is quantified) | ⟨⟩ |
| Urgency (1 to 4) / Importance (1 to 4) | ⟨⟩ / ⟨⟩ |
| Cost/Benefit remark; incremental value if not all objectives are reached | ⟨⟩ |

## 4 · Savings pre-evaluation (day 3, block 3.1)

OD's rule: every saving is linked to a concrete use case in the plant's list; compiled per use case;
a first realistic estimate is allowed if labelled; calculation follows with OD's calculator
(`od-benefit-calculation`). Categories on OD's template: productivity, quality, maintenance.

| Use case # | Mechanism (loss that disappears) | Category | Inputs named (for example machines, shifts, minutes per entry, days) | First figure and period | Basis (`CALCULATION` / `ESTIMATION` / ⟨none⟩) | Baseline exists? who measures | Dependency |
|---|---|---|---|---|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨or "open"⟩ | ⟨⟩ | ⟨⟩ | ⟨ECR APPROVAL · MACHINE INTEGRATION · PLANT · OTHERS · none⟩ |

Date by which OD sends the calculated first number: ⟨date⟩.

## 5 · Tool availability (day 3, block 3.2)

| Tool | Status at plant (DONE / ONGOING / NOT AVAILABLE) | Recommended (planned year / needed for multiple use cases / not necessary / not recommended now) | Use cases that need it |
|---|---|---|---|
| IIoT Edge platform | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| Manufacturing Service Bus / MQTT broker | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| Data integration rule engine | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| MES | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| QFPR (quality feedback app) | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| Recipe management | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| Manufacturing image library | ⟨⟩ | ⟨⟩ | ⟨⟩ |
| Data Science Factory | ⟨⟩ | ⟨⟩ | ⟨⟩ |

## 6 · Machine integration demands (day 3, block 3.3) — hand to the Information Integration lane

| Machine / line | PLC type and program available? | Network / interface | Connected now? | Wave proposed | Cyber Security status | Remark |
|---|---|---|---|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

## 7 · Use case utilization (integration workshop; OD template)

| Use case | Who shall use it | Related process | Utilization method (1 to 3 sentences, with initial state) | Rate (Daily / Weekly / Monthly / On-Demand / Never) | Impact (Low / Medium / High) | Plant management relevant |
|---|---|---|---|---|---|---|
| ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ | ⟨⟩ |

## 8 · Decisions, disagreements and non-decisions

| Item | Decision taken (who, when) · or disagreement · or deferred to ⟨role⟩ |
|---|---|
| ⟨⟩ | ⟨⟩ |

Money, equipment integration go-ahead and external connection are not decided here; write who
decides and by when.

## 9 · Open questions for after the workshop

| Question | Who can answer |
|---|---|
| ⟨⟩ | ⟨role⟩ |
