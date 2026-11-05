---
type: Skill Reference
title: Workshop formats
description: The workshop formats OD has actually run at plants (definition, integration, equipment integration, machine integration, savings), with purpose lines, day structure, audience, outputs and the workshops on record, for choosing and designing the next one.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Workshop formats

All facts below come from OD agenda and summary decks in the vault's `Slide Index` and
`Split Slides` (10-Workshops and 03-AMT_MI_Standard_Agenda_Use_Case_Workshop), read 2026-11-05.
They are presentations written for the plants, not rule documents; where a deck shows only an image
or table the text was not recoverable and is marked.

## 1 · Formats at a glance

| Format | Trigger (lane `tasks.md`) | Purpose in OD's words (paraphrased) | Typical length | Output |
|---|---|---|---|---|
| Use Case Definition Workshop | Plant onboarding or new demand wave | Define next use cases; follow up status of running projects; prioritize for a machine integration wave; starting point for a rollout project | Three days in the Standard Agenda (Carei 2024: preferred window 12 to 16 April 2024) | Use case list with canvases, priority by process, tool availability status, next steps local and central |
| Use Case Integration Workshop | Use case ready for integration | Project status and formal closure or handover of the connectivity project; integration based on available equipment connectivity; requirements collection; integration sessions; tool trainings with key users; feedback from OPEX, Engineering, Production; use case utilization | Two days on site (Dolne Vestenice 2025: calendar week 47, 18 to 19 November) | Roadmap status (machines connected against target), dashboard structure per area, requirements per use case, utilization table |
| Use Case Equipment Integration Workshop | Start of equipment integration for a priority area | Starting point for equipment integration (prio machines), plant tour of focus machines, PLC overview and machine list (program availability, interfaces, network infrastructure), target budget calculation and project plan | Agenda plus summary (Korbach, October and November 2025) | Machine baseline, use cases per area, IT preconditions, next steps toward the eCR |
| Machine Integration Workshop | Machine connectivity need | Concept and process of machine integration, standardization, data model integration | Single day at the start (Mako 2023, day 1) | Machine list and connectivity status |
| Combined Use Case and Machine Integration Workshop | Both needs at once | Joint days with the use case lead and the machine integration lead presenting alternately | Mako and Vac, January 2023: seven days across two plants | Status and savings of actual use cases, resource footprint, required systems, pain points |
| Savings Workshop | Need for quick progress on cost saving | On-site support to produce progress on use cases such as digital downtime recording, automatic OEE calculation, plan/fact deviation, hourly output | Two days (Mako and Subotica, 24 to 25 July 2024) | eCR next steps per plant (for example a downtime reporting app, machine integration wave 2) |

Rule on order (speaker notes on several decks): "Dependent on which workshop format is first >>
Machine Integration or Use Case Workshop." Decide it with the plant before the invitation.

## 2 · The Definition Workshop in detail (Standard Agenda, March 2024)

| Day | Block | Content (from the agenda slides) |
|---|---|---|
| 1 Introduction | 1.1 Intro to the OD organization | What OD is, strategic pillars (digitalization benefit analysis; system and connectivity assessment; system and connectivity roadmap; use case executive support; demands and iterations; enhanced process understanding and control), the two call formats ODEC (why prioritize) and COP (how are we doing) |
| | 1.2 Intro of Smart Factory tools | Tool by tool: IIoT Edge platform, Data Science Factory, MES, MDA/PDA, QFPR, recipe management, image library, rule engine, energy management system, trainings |
| | 1.3 Use case creation process | Process flow, Use Case Canvas, benefits analysis, savings calculation, standardization, maturity |
| | 1.4 Use case library | Proven reference solutions (see `od-use-case-definition`, library catalog) |
| | 1.5 Analytics use case library | Analytics examples |
| 2 Definition | 2.1 Plant tour with focus on priority machines | Support from the Project Manager MSB, Machine Integration Lead, Production, Quality; optional Maintenance, Process Engineering; overview of processes and machines against current projects; notes feed the later use case collection and savings calculation; minor topics such as custom connectors can be collected |
| | 2.2 Collection of use case demand | Everything goes into the current use case list; the library is for knowledge sharing; classification and priority by highest generalization potential, then highest saving potential; extra budget may be needed for custom use cases |
| 3 Detail evaluation | 3.1 Pre-evaluation of found use cases (savings) | Savings pre-evaluation template with examples: productivity (lot, setup optimization), quality (scrap and waste), maintenance (reaction and breakdown time) |
| | 3.2 Assessment of Smart Factory tools needed | Tool list per plant: capabilities and rollout status |
| | 3.3 Assessment of machine integration demands | Machine list and connectivity demands (slide content is an image; text not recoverable) |

Audience matrix (slide 2): roles Project Manager MSB, Machine Integration Lead, Quality,
Production, CBS (⟨expansion not in the deck⟩), IT, each marked Required or Recommended per block.
The text extraction of that table loses empty cells, so the per-block assignment is ⟨to read from
slide 2 of the deck⟩ and is not reproduced here.

## 3 · What a good output looked like (Carei 2024 summary)

The summary deck sent after the workshop held: the OD architecture reference as a reminder; the
list of tools with plant status (for example IIoT Edge platform, MSB broker and rule engine
"DONE", QFPR "ONGOING", MES "NOT AVAILABLE", with a recommendation per tool such as "needed for
multiple use cases" or "not necessary"); the top three to four use cases by current priority per
process (High: extrusion and vulcanization alerts and transparency; Medium: calendering; Low:
assembly, with the reason "infrastructure (cabling) and QFPR needed, so the time frame is longer");
the open task "savings estimation for use cases"; and next steps split into local (finish machine
integration, define wave 2, upload the eCR again, evaluate use cases for a savings-tracking project,
check the library) and central (enforce Cyber Security approval for QFPR, define a standard data
model for extrusion lines). One example in that deck quotes "~38k Savings in Labor" for a measure in
assembly; the basis is not shown, so treat it as a workshop estimate.

## 4 · Workshops on record (selection, from the 10-Workshops index)

Definition workshops: Timisoara (2021 summary; 2024), Karben (2023), Tlalnepantla (2023), San Luis
Potosi (2023), Carei (2024), Dolne Vestenice (2024), Northeim (2024), Subotica (2024), Vac (2024),
Waltershausen (2024), Andrezieux (2024). Integration workshops: Carei (2025-06), Dolne Vestenice
(2025-11), Korbach (equipment integration, 2025-10 and 2025-11). Machine integration: Mako and Vac
(2023), Vac summary (2024), Changchun and Qingdao agendas (2024). Savings: Mako and Subotica (2024).
Not every plant on the list has a recorded outcome; counts of resulting use cases were not traced.

## 5 · Lessons already written down

- Fitting savings calculation into the broader agenda "messed up the workshop" with too many
  domains on the table (`od-benefit-calculation`, review checklist). Book it as its own follow-up.
- A tool demoed at a plant does not put the use case in scope there (`od-use-case-intake-triage`,
  refusal playbook): read the tool availability table first.
- The 2025 integration workshops end with utilization: who uses it, how often, which actions.
  Utilization is asked at the workshop, not only on the Scorecard.
- Choose the examples "everybody understands" (the 2025 decks use SMED and digital Gemba) to link
  a digital use case to a method the plant already runs.
