---
type: Skill Asset
title: Workshop agenda and preread
description: Agenda skeletons for a definition workshop and an integration workshop, distilled from OD's past agendas, plus the pre-read checklist that goes out to the plant before the workshop.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice, template]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Workshop agenda and pre-read — ⟨plant⟩ — ⟨format⟩

This is a working version distilled from past OD agendas (see `../references/workshop-formats.md`).
The official SharePoint templates ("Standard Agenda — Use Case Workshop", "Use Case Integration
Workshop agenda") were not available; replace this with them when you have them.

## 1 · Header (fill first)

| | |
|---|---|
| Plant | ⟨⟩ |
| Format | ⟨Definition · Integration · Equipment integration · Machine integration · Savings⟩ |
| Workshop purpose (3 to 6 bullets) | ⟨what is defined · which status is followed up · what is prioritized · which project it starts⟩ |
| Preferred window and agreed window | ⟨dates; "aligned with the plant on ⟨date⟩"⟩ |
| OD participants (roles) | ⟨DBVE · IIAE · OD lead · IT⟩ |
| Plant participants (roles) | ⟨Plant ME · Production · Quality · Project Manager MSB · Machine Integration Lead · IT · OPEX · Engineering · key users⟩ |
| Who schedules the invitation | ⟨role⟩ |

## 2A · Definition workshop skeleton (three days; trim what the plant knows)

| Day | Block | Time | Lead | Output |
|---|---|---|---|---|
| 1 | Intro to OD, service lines and COP (ODEC decks as history) | ⟨⟩ | ⟨OD lead⟩ | shared picture |
| 1 | Smart Factory tools, only those relevant to the plant | ⟨⟩ | ⟨DBVE / IIAE⟩ | tool awareness |
| 1 | Use case creation process (canvas, benefits, standardization) | ⟨⟩ | ⟨DBVE⟩ | |
| 1 | Use case library and analytics library walk-through | ⟨⟩ | ⟨DBVE⟩ | candidates to reuse |
| 2 | Plant tour of priority machines (time-box it; past agendas kept it short) | ⟨⟩ | ⟨DBVE with Production, Quality, Machine Integration Lead⟩ | tour notes |
| 2 | Collection of use case demand | ⟨⟩ | ⟨DBVE⟩ | demand list, canvases |
| 3 | Pre-evaluation of found use cases (savings) | ⟨⟩ | ⟨DBVE⟩ | pre-evaluation rows |
| 3 | Assessment of tools needed | ⟨⟩ | ⟨DBVE⟩ | tool status and recommendation |
| 3 | Assessment of machine integration demands | ⟨⟩ | ⟨IIAE⟩ | machine list, wave proposal |
| 3 | Open points, obstacles, pain points; wrap-up and feedback | ⟨⟩ | all | |

## 2B · Integration workshop skeleton (two days on site)

| Block | Lead | Output |
|---|---|---|
| Project status; formal closure or handover of the connectivity project, if due | ⟨IIAE / project manager⟩ | status table: machines connected against roadmap target |
| Use case requirements collection per area | ⟨DBVE⟩ | requirement lines per use case (feed `od-requirements-breakdown`) |
| Integration sessions on the connected equipment | ⟨IIAE / DBVE with key users⟩ | dashboards or flows agreed, signals missing |
| Tool training sessions with key users | ⟨⟩ | trained key users (`od-rollout-training`) |
| Feedback from OPEX, Engineering, Production | ⟨⟩ | feedback list |
| Use case utilization: who, how often, which actions | ⟨DBVE⟩ | utilization table (OD template) |
| Wireless, network or IT topics that block integration | ⟨IT⟩ | open IT items with owner |
| Wrap-up | all | follow-up list |

## 3 · Pre-read checklist (send with the invitation)

- [ ] Agenda with purpose, window, and who must attend which day (Required / Recommended)
- [ ] One-page: what OD does and the service lines (so no time is lost on day 1)
- [ ] Blank Use Case Canvas (challenge, solution idea, dependencies, current state, obstacles and
      risks, requirements and gaps, data, infrastructure, stakeholders and roles, scalability,
      success criteria) and a note that Urgency and Importance are rated 1 to 4
- [ ] Savings pre-evaluation template with its examples; request that plants arrive with a first
      idea of losses (scrap, downtime, setup, reporting effort) and the name of whoever can give a
      baseline
- [ ] Use case utilization template (who, related process, method, rate, impact, management
      relevance) for use cases already live at the plant
- [ ] Request: existing use case list for the plant, machine list with PLC types, list of priority
      machines, known pain points
- [ ] Tool availability table for the plant (to be reviewed in the workshop, not decided in advance)
- [ ] Reminder of the wait states: Cyber Security sign-off runs in parallel and blocks only go-live of an external
      machine connection (start the package early); investment is decided elsewhere (OD lead with BA Operations)
- [ ] Logistics: room, plant tour access, safety requirements, remote participants
      ⟨not covered by the sources⟩
- [ ] Contact for questions before the workshop (role)

## 4 · Facilitator's own check before the day

- [ ] I read the plant's rows in the case groups and know what is Delivered, Planned, Idea and
      white space there (white space is not demand)
- [ ] I know which use cases at this plant have no saving recorded and what baseline exists
- [ ] I have the questionnaire of `od-use-case-definition` at hand
- [ ] The capture sheet is open and the follow-up list skeleton is prepared
