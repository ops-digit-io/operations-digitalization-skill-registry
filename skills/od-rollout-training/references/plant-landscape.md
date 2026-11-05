---
type: Skill Reference
title: Plant landscape
description: How a plant is organised for rollout training - the roles, the tools a plant actually has, and the training and workshop history recorded in the ODEC and COP decks - with counts, dates and where each fact was read.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Plant landscape

What the sources say about the plant side of a rollout, read 2026-11-05. The ODEC Facts notes are extracts of call
slides (some lines are cut off in the export); the Graph notes are generated from the SharePoint lists and are not
audited. Use the numbers as dated records, not as targets.

## 1. The estate in one paragraph

33 plants in three regions (20 Europe, 9 Americas, 4 Asia), per `od-context`. Each plant note in the vault's
Graph/Plants holds its machine count, controller vendors, field networks, integration methods, use-case status mix
and the tool rollouts recorded for it. The Carei note is a good pattern: 81 machines, 29 recorded integrated (35%),
Siemens controllers on 70, integration through the IIoT Edge Computing Platform on 53 and the central OPC UA
aggregation server on 4, and seven tool rollouts recorded as available between 2018 and 2023. Open the plant's own
note before planning: **the training content follows what is actually rolled out at that plant**, not the full list
of tools.

## 2. Who is in the plant

| Role | What the sources say | Source |
|---|---|---|
| Plant ME (Manufacturing Engineering) | Counterpart of the IIAE in the integration go-ahead (Tandem). Local ME teams were trained in Node-RED and Grafana at an Americas plant | `08-decision-rights.md`; ODEC Facts - Plant - Delicias |
| Plant IT | Counterpart in the same decision. Rollout workshops include a visit of the plant network infrastructure; the migration slides name tasks on the server and network team side | `08-decision-rights.md`; ODEC Facts - Plant - San Luis Potosi |
| Plant manager and department managers | A first-wave MSB kick-off workshop lists plant manager and department managers for OPEX, Quality, Production, Maintenance and PPI | ODEC Facts - Plant - San Luis Potosi, 2025-05-21 |
| Local key user, BA/BU key user, central key user | Roles defined in the platform's operations concept alongside Governance Board, Divisional Engineering Support, Divisional IT, Local IT and the platform service provider | Graph/Tools Concept 3 (archive evidence) |
| Key users in a migration | In the 2025 migration status, "all key users will receive a location specific meeting invitation" with a checklist per location; 13 of 17 locations done as of the Oct 2025 slide | ODEC Facts - Tools and Systems (WiriTec migration slides) |
| Shift lead, operator | Consumers of dashboards and Andon boards; the Gemba walk is the largest consumer of what OD builds (125 of 202 use cases that record utilization are used daily) | `od-handover-and-adoption` |

The sources give no job description for a key user and no count of key users per plant:
⟨key-user responsibilities and number per plant⟩ (OD lead).

## 3. The tools a plant may have

16 shop-floor tools are listed in the vault's tool overview. For training, the ones most used by recorded use
cases are below (Graph/Tools notes: rollout records and "used by" counts; read 2026-11-05):

| Tool | Plants with rollout record | Use cases using it | Plants using it |
|---|---|---|---|
| IIoT Edge Computing Platform (Concept 3) | 14, all Available | 200 | 16 |
| RuleEngine 2.0 | 19, all Available | 203 | 18 |
| MSB 2.0 | 13, all Available | 184 | 18 |
| MSB 4.0 | 9: Available 6, Ongoing 3 | 90 | 10 |
| Concept 2 (container-based machine integration) | 1 | 85 | 13 |
| Central OPC UA server (Concept 1) | 11, all Available | 24 | 6 |
| QFPR (Quality Feedback and Part Routing) | 2: Ongoing 1, Available 1 | 27 | 8 |

A plant can have a use case on a tool whose rollout is not yet "Available" there; the two counts are separate
records. Check both before choosing a module.

## 4. What the use-case estate teaches

Delivered use cases cluster in a few templates (Case Groups, 40 groups, generated 2026-11-04, not reviewed):

| Case group | Plant use cases | Delivered | Plants with delivery |
|---|---|---|---|
| Process Values - Rubber | 62 | 39 | 7 |
| Andon Board - Assembly | 44 | 27 | 10 |
| Process Values - Plastic | 34 | 23 | 6 |
| Process Values - Assembly | 45 | 17 | 8 |
| Andon Board - Rubber | 32 | 17 | 7 |

Use for training: a plant's first training should cover the template it actually received (process values or an
Andon board), at the screen it will use, rather than a general course.

## 5. Training and workshop history in the decks

| Fact | Date or deck | Source note |
|---|---|---|
| Training content available for 8 formats; 40 training sessions and 80 participants in 2023; plan for 2024: schedule trainings once participants are registered, improve recorded sessions, extend by 3 more formats | End of 2023 status on COP calls 2024 #1 and #2 | ODEC Facts - Department KPIs and Roadmap Status |
| Americas workshop roadmap 2025, each "Workshop (MI/UC)" (machine integration and use case): San Luis Potosi Q1, Montemorelos Q1, Delicias Q2, Ponta Grossa Q3, Somersworth Q4 | ODEC 2024 #10, slide 8 | ODEC Facts - Plant notes of those plants |
| First-wave MSB workshop agenda at one plant: kick-off with plant manager and department managers, visit of the current network infrastructure, marketing of MSB and use cases (list of use cases), trainings in machine integration and use-case tools (Grafana, Node-RED, Jupyter Notebook); the rest of the line is cut off | ODEC slide dated 2025-05-21 | ODEC Facts - Plant - San Luis Potosi |
| "Training for local ME team in Node Red and Grafana" listed as a highlight, with a visit of the machines of the first and second wave | ODEC 2024 #10, slide 9 | ODEC Facts - Plant - Delicias |
| "Trainings for equipment integration conducted" as a key achievement of the China plants (22 of a plan of 66 integrated at the time); blocking point: infrastructure harmonization | ODEC 2025 #4, slide 19 | ODEC Facts - Plant - Qingdao, Changchun, Changshu |
| "Machine Integration Workshop done in San Luis Potosi" as a key achievement; blocking point: hardware suppliers delayed infrastructure installation (19 of a plan of 85) | ODEC 2025 #4, slide 22 | ODEC Facts - Plant - Sun Prairie |
| A Qingdao dashboard slide states the dashboards "shall be utilized within daily Gemba meetings for close follow up" | ODEC 2025, 2025-08-20 | ODEC Facts - Plant - Qingdao |
| QFPR basic training exists ("QFPR - Basic Training / Introduction"); "in case of interest, basic training can be carried out" | ODEC 2024 | ODEC Facts - Plant - Monterrey |
| Initiative "Secure Critical Automation Software": success criteria "80% of all Key Equipment Knowhow secured" and "Workflow trained internally" | ODEC 2025-08-19 | ODEC Facts - Other |

What these show: training has been run **as workshops tied to a rollout wave**, by OD, with tool training (Node-RED,
Grafana, Jupyter Notebook) and machine integration as the recurring content. They show no competence test, no
recorded pass criteria and no sustainment step. That is the gap this skill addresses.

## 6. Wave structure (for scheduling)

Americas connectivity roadmap 2024: San Luis Potosi is Wave 1; Delicias, Monterrey and Ponta Grossa are Wave 2
(ODEC 2024 #8 slide "eCR Status Connectivity Roadmap 2024"). Schedule training after the plant's infrastructure and
machine wave are real, not before. The 2025 status shows plants "on track" and "behind" per region; the plants behind
had infrastructure delays, so training dates move with infrastructure.

## 7. Language

The sources record no language or translation policy for training material:
⟨language and translation policy for training material⟩ (OD lead).
