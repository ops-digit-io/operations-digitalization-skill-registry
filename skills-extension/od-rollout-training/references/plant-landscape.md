---
type: Skill Reference
title: Plant landscape
description: Guidance, no figures - how a plant is organised for rollout training (roles, how to find the tools a plant actually has, what kinds of training and workshops the ODEC and COP decks record) and where to read the live data.
resource: ../SKILL.md
status: draft
tags: [project-support-consultancy, practice]
---
# Plant landscape

This file holds **no figures** about the estate or about training volumes. It says where the plant-side facts live and how
to read them. The ODEC Facts notes are extracts of call slides (some lines are cut off in the export); the Graph notes are
generated from the SharePoint lists and are not audited. Read them live and say which note and date a fact came from.

## 1. Find the plant before planning

Each plant note in the knowledge base's `Graph/Plants` holds the plant's machine count, controller vendors, field networks,
integration methods, use-case status mix and the tool rollouts recorded for it. Open the plant's own note before planning:
**the training content follows what is actually rolled out at that plant**, not the full list of tools. Place the plant by
its starting profile (`od-plant-onboarding`, `references/plant-landscape.md`).

## 2. Who is in the plant

| Role | What the sources say | Source |
|---|---|---|
| Plant ME (Manufacturing Engineering) | Counterpart of the IIAE in the integration go-ahead (Tandem). Local ME teams have been trained in Node-RED and Grafana | `08-decision-rights.md`; ODEC Facts plant notes |
| Plant IT | Counterpart in the same decision. Rollout workshops include a visit of the plant network infrastructure; migration slides name tasks on the server and network team side | `08-decision-rights.md`; ODEC Facts plant notes |
| Plant manager and department managers | A first-wave MSB kick-off workshop involves plant manager and department managers for OPEX, Quality, Production, Maintenance and PPI | ODEC Facts plant notes |
| Local key user, BA/BU key user, central key user | Roles defined in the platform's operations concept alongside Governance Board, Divisional Engineering Support, Divisional IT, Local IT and the platform service provider | Graph/Tools Concept 3 (archive evidence) |
| Key users in a migration | Migration status slides say every key user receives a location-specific invitation with a checklist per location | ODEC Facts - Tools and Systems |
| Shift lead, operator | Consumers of dashboards and Andon boards; the Gemba walk is the largest consumer of what OD builds | `od-handover-and-adoption` |

The sources give no job description for a key user and no number of key users per plant:
⟨key-user responsibilities and number per plant⟩ (OD lead).

## 3. The tools a plant may have

The knowledge base's tool overview lists the shop-floor tools; each `Graph/Tools` note carries rollout records per plant (status such
as Available or Ongoing) and "used by" links from use cases. To choose modules:

1. Open the plant note and list the tools with a rollout record there.
2. For each tool, read the rollout status and the use cases using it. These are two separate records: a plant can have a
   use case on a tool whose rollout is not yet "Available" there. Check both before choosing a module.
3. Typical tools to expect in training: the IIoT Edge Computing Platform, RuleEngine, MSB (versions 2.0 and 4.0), the
   container-based machine integration, the central OPC UA server, QFPR (Quality Feedback and Part Routing).

## 4. What the use-case estate teaches

Delivered use cases cluster in a few templates (the Case Groups notes in the knowledge base: process values and Andon boards per
material family). To see which cluster a plant received, read the Case Groups notes (generated, not reviewed) and filter by
plant. A plant's first training should cover the template it actually received (process values or an Andon board), at the
screen it will use, rather than a general course.

## 5. Kinds of training and workshop recorded in the decks

The ODEC and COP decks record training as a mix of the kinds below. Read the deck notes (`ODEC Facts - Department KPIs and
Roadmap Status`, the plant notes, `Other`) for dates and plants.

| Kind | What it typically contains | Where to read it |
|---|---|---|
| Rollout-wave workshops (machine integration and use case) | Kick-off with plant management, visit of the current network infrastructure, marketing of the platform and use cases, tool trainings (Grafana, Node-RED, Jupyter Notebook) | ODEC Facts plant notes |
| Local ME team tool training | Node-RED and Grafana for the local team, with a visit of the machines of a wave | ODEC Facts plant notes |
| Equipment integration trainings | Reported as a key achievement; typical blocking point: infrastructure harmonization or delayed hardware installation | ODEC Facts plant notes (status slides) |
| Gemba follow-up | Dashboards "shall be utilized within daily Gemba meetings for close follow up" | ODEC Facts plant notes |
| QFPR basic training | Introduction exists; offered on interest | ODEC Facts plant notes |
| Key-equipment know-how initiative ("Secure Critical Automation Software") | Success criteria on securing key equipment know-how and training the workflow internally | ODEC Facts - Other |
| Training-format statistics | Counts of formats, sessions and participants reported on COP calls, with plans to record sessions better | ODEC Facts - Department KPIs and Roadmap Status |

What these show: training has been run **as workshops tied to a rollout wave**, by OD, with tool training (Node-RED,
Grafana, Jupyter Notebook) and machine integration as the recurring content. They show no competence test, no recorded
pass criteria and no sustainment step. That is the gap this skill addresses.

## 6. Wave structure (for scheduling)

Connectivity roadmaps are organised in waves per region (see the eCR status connectivity roadmap slides in the ODEC
decks). Schedule training after the plant's infrastructure and machine wave are real, not before. Status slides mark plants
"on track" or "behind"; plants behind typically had infrastructure delays, so training dates move with infrastructure.

## 7. Language

The sources record no language or translation policy for training material:
⟨language and translation policy for training material⟩ (OD lead).
