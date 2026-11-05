---
type: Skill Reference
title: Plant landscape
description: The 33 plants with region, recorded machines, integration share, use cases and main controller and integration method, plus the four starting profiles that decide where onboarding begins; open it to place a plant.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Plant landscape

**Source:** the 33 plant notes of the work vault (`Graph/Plants`, plant-profile blocks), which are built from the SharePoint
machine, use case and tool lists (enriched 2026-09-25, full text 2026-11-05) and summarised here on 2026-11-05. Figures are
**as entered in the lists, not audited**, and they drift: refetch the Machine List before relying on a row. "Main" means
the entry with the most machines. "-" means not recorded.

Totals: 33 plants (Europe 20, Americas 9, Asia 4), 1,715 machines recorded, 821 integrated (48%). The use-case column sums to
618 across the plant notes, against 650 use cases in the list; the notes read do not say where the difference sits.
The "Productive" column sums to 167.

| Plant | Country | Region | Machines | Integrated | Share | Use cases | Productive | Main controller | Main integration method |
|---|---|---|--:|--:|--:|--:|--:|---|---|
| Andrezieux | France | Europe | 0 | - | - | 0 | 0 | - | - |
| Auburn | United States | Americas | 60 | 57 | 95% | 8 | 8 | Rockwell Automation - Allen Bradley | - |
| Caluire | France | Europe | 33 | 24 | 72% | 8 | 2 | Siemens | Central OPCUA Aggregation Server |
| Carei | Romania | Europe | 81 | 29 | 35% | 50 | 11 | Siemens | IIoT Edge Computing Platform |
| Changchun | China | Asia | 43 | 21 | 48% | 27 | 0 | Siemens | Central OPCUA Aggregation Server |
| Changshu | China | Asia | 99 | 21 | 21% | 72 | 12 | Siemens | EVALUATION ONGOING |
| Dannenberg | Germany | Europe | 0 | - | - | 0 | 0 | - | - |
| Delicias | Mexico | Americas | 51 | 22 | 43% | 29 | 9 | Siemens | IIoT Edge Computing Platform |
| DolneVestenice | Slovakia | Europe | 59 | 48 | 81% | 20 | 3 | B&R Industrial Automation | Central OPCUA Aggregation Server |
| HannMuenden | Germany | Europe | 9 | 9 | 100% | 6 | 0 | Siemens | IIoT Edge Computing Platform |
| HannoverStoecken | a country that is not recorded | Europe | 17 | 2 | 11% | 1 | 0 | Siemens | IIoT Edge Computing Platform |
| Jeonju | South Korea | Asia | 0 | - | - | 0 | 0 | - | - |
| Karben | Germany | Europe | 46 | 23 | 50% | 36 | 10 | Siemens | IIoT Edge Computing Platform |
| Korbach | Germany | Europe | 16 | 0 | 0% | 1 | 0 | Siemens | Central OPCUA Aggregation Server |
| Kranj | Slovenia | Europe | 0 | - | - | 0 | 0 | - | - |
| Mako | Hungary | Europe | 128 | 71 | 55% | 54 | 14 | Siemens | IIoT Edge Computing Platform |
| Montemorelos | Mexico | Americas | 51 | 0 | 0% | 0 | 0 | Rockwell Automation - Allen Bradley | EVALUATION ONGOING |
| Monterrey | Mexico | Americas | 82 | 25 | 30% | 24 | 7 | Rockwell Automation - Allen Bradley | IIoT Edge Computing Platform |
| Northeim | Germany | Europe | 87 | 83 | 95% | 8 | 0 | Engel | IIoT Edge Computing Platform |
| Oedelsheim | Germany | Europe | 0 | - | - | 0 | 0 | - | - |
| Ostrava | Czechia | Europe | 1 | 0 | 0% | 0 | 0 | - | - |
| PontaGrossa | Brazil | Americas | 75 | 62 | 82% | 20 | 7 | Siemens | Central OPCUA Aggregation Server |
| Qingdao | China | Asia | 74 | 59 | 79% | 39 | 4 | Siemens | IIoT Edge Computing Platform |
| Rennes | France | Europe | 58 | 58 | 100% | 8 | 8 | Schneider Electric | - |
| SanLuisPotosi | Mexico | Americas | 16 | 0 | 0% | 20 | 0 | Siemens | IIoT Edge Computing Platform |
| Somersworth | United States | Americas | 26 | 26 | 100% | 36 | 28 | Siemens | IIoT Edge Computing Platform |
| Subotica | Serbia | Europe | 181 | 27 | 14% | 31 | 9 | Siemens | IIoT Edge Computing Platform |
| SunPrairie | United States | Americas | 39 | 39 | 100% | 15 | 11 | Rockwell Automation - Allen Bradley | Central OPCUA Aggregation Server |
| Tanger | Morocco | Europe | 20 | 0 | 0% | 0 | 0 | Siemens | EVALUATION ONGOING |
| Timisoara | Romania | Europe | 91 | 26 | 28% | 31 | 2 | Siemens | IIoT Edge Computing Platform |
| Tlalnepantla | Mexico | Americas | 82 | 0 | 0% | 16 | 0 | Siemens | Central OPCUA Aggregation Server |
| Vac | Hungary | Europe | 103 | 20 | 19% | 14 | 5 | Siemens | IIoT Edge Computing Platform |
| Waltershausen | Germany | Europe | 87 | 69 | 79% | 44 | 17 | Siemens | IIoT Edge Computing Platform |

## Four starting profiles

The profile decides which stage of the path begins the onboarding. Placement is by the Machine List snapshot above.

| Profile | Rule | Plants (count) | Where onboarding begins |
|---|---|---|---|
| A. No machines recorded | Machines = 0 | Andrezieux, Dannenberg, Jeonju, Kranj, Oedelsheim (5) | Stage 1: record the plant first. Nothing can be graded or compared yet. Andrezieux has a use-case workshop folder in the archive index (2025) but no machine or use-case records in the plant note |
| B. Machines recorded, none integrated | Integrated = 0 | Korbach, Montemorelos, Ostrava, SanLuisPotosi, Tanger, Tlalnepantla (6) | Stage 2 (assessment and roadmap), then Lane 1b / Lane 3b. Montemorelos and Tanger record the integration method as "evaluation ongoing" for most machines (45 of 51 and 15 of 20) |
| C. Partly integrated | 0 < share < 100% | 18 plants, from Subotica (14%) to Auburn and Northeim (95%) | Stage 3 (Lane 1 first wins for connected machines), with Stage 2 for the remainder |
| D. Fully integrated | Share = 100% | HannMuenden, Rennes, Somersworth, SunPrairie (4) | Stage 3 and 5: the use-case catalog and Lane 2; no integration roadmap needed for recorded machines |

Profile C in detail: Auburn 95%, Northeim 95%, DolneVestenice 81%, PontaGrossa 82%, Waltershausen 79%, Qingdao 79%,
Caluire 72%, Mako 55%, Karben 50%, Changchun 48%, Delicias 43%, Carei 35%, Monterrey 30%, Timisoara 28%, Changshu 21%,
Vac 19%, Subotica 14%, HannoverStoecken 11%.

## What differs underneath

A plant's starting profile says how far it has got; it does not say how its machines are built. For that, use the grid in
`od-cross-plant-compatibility` (`references/plant-differences.md`): controller vendors, field networks, the three ingress
variants (IIoT Edge Computing Platform at 21 plants, central OPC UA aggregation server at 14, evaluation ongoing at 6),
tool versions available.

## Material family

Every use case is recorded against a plant and one of four material families (Rubber, Plastic, Metal, Assembly) and one of
eleven capabilities (`od-context`). The plant notes list the process areas recorded per plant (for example Carei: Assembly,
Silicon - Assembly, Extrusion, Post vulcanization - Tempering, ERS). Use them to place the plant's machines on the
process groups; the process-group notes sit in the work vault under `Graph/Process Groups`.

## Strategic plants

The landscape module names the strategic plants as Carei, Mako, Subotica, Timisoara, Karben, Northeim "and others"; the
complete list is not in the material read: `⟨strategic-plant list, to confirm with the OD lead role⟩`. The same module
lists the example workshop locations on record (Northeim, Dolne Vestenice, Carei, Timisoara, Andrezieux, Subotica, Karben).
