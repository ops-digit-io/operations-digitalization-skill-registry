---
type: Skill Reference
title: Plant landscape
description: Guidance, no figures - how to read the plant records (region, recorded machines, integration share, use cases, main controller and integration method), how to obtain them live, and the four starting profiles that decide where onboarding begins; open it to place a plant.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---

# Plant landscape

This file holds **no figures** about the estate. Plant data drifts and is entered by the plants; a skill that quoted it would
be stale at once. It explains where the data lives, what each field means and how to place a plant.

## Where the live data is

- The plant notes of the department knowledge base (`Graph/Plants`, plant-profile blocks), built from the SharePoint machine, use case and
  tool lists. Figures there are **as entered in the lists, not audited**.
- The SharePoint Machine List, Use Case list and Tool list themselves (read them with `od-sharepoint-list-export`).
- Always re-read the Machine List on the day you place a plant, and note the date in the onboarding tracker.

## Fields to read per plant

| Field | Meaning | How to read it |
|---|---|---|
| Region | Europe, Americas or Asia | Grouping only; says nothing about readiness |
| Machines recorded | Machines entered in the Machine List for the plant | Zero means "not recorded", not "no machines" |
| Integrated / share | Machines with a recorded, working integration, as a share of those recorded | A blank status is not "not integrated"; check the status column before counting |
| Use cases / productive | Use cases recorded against the plant, and those in productive status | Totals across plant notes may not match the list; count on the list, not the notes |
| Main controller | The controller vendor with the most machines | "Main" is the entry with the most machines, not the only one |
| Main integration method | The ingress route with the most machines (IIoT Edge Computing Platform, central OPC UA aggregation server, evaluation ongoing) | "-" means not recorded |

Re-count on the live list before quoting any figure, and say which list and date it came from.

## Starting profiles

The profile decides which stage of the path begins the onboarding. Place the plant from the live Machine List.

| Profile | Rule | Where onboarding begins |
|---|---|---|
| A. No machines recorded | Machines = 0 | Stage 1: record the plant first. Nothing can be graded or compared yet. A plant may have workshop material in the archive but no machine or use-case records: that does not make it profile B or C |
| B. Machines recorded, none integrated | Integrated = 0 | Stage 2 (assessment and roadmap), then Lane 1b / Lane 3b. Typical trap: most machines carry the integration method "evaluation ongoing"; choosing the ingress variant is then part of stage 2 |
| C. Partly integrated | 0 < share < 100% | Stage 3 (Lane 1 first wins for connected machines), with Stage 2 for the remainder. Read the share against the size of the estate: low share with a large estate means stages 2 and 5 dominate |
| D. Fully integrated | Share = 100% | Stage 3 and 5: the use-case catalog and Lane 2; no integration roadmap needed for recorded machines. Check that "100%" is not simply a small recorded subset |

## What differs underneath

A plant's starting profile says how far it has got; it does not say how its machines are built. For that, use the grid in
`od-cross-plant-compatibility` (`references/plant-differences.md`): controller vendors, field networks, the three ingress
variants, tool versions available.

## Material family

Every use case is recorded against a plant, one of four material families (Rubber, Plastic, Metal, Assembly) and one of
the capabilities listed in `od-context`. The plant notes list the process areas recorded per plant; use them to place the
plant's machines on the process groups (process-group notes sit in the department knowledge base under `Graph/Process Groups`).

## Strategic plants

The landscape module names a group of strategic plants "and others"; the complete list is not in the material read:
`⟨strategic-plant list, to confirm with the OD lead role⟩`. Workshop locations on record are listed in the same module.
