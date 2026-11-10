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
`Split Slides` (10-Workshops and 03-AMT_MI_Standard_Agenda_Use_Case_Workshop). Re-open the decks before reusing a date or a day count.
They are presentations written for the plants, not rule documents; where a deck shows only an image
or table the text was not recoverable and is marked.

## 1 · Formats at a glance

| Format | Trigger (lane `tasks.md`) | Purpose in OD's words (paraphrased) | Typical length | Output |
|---|---|---|---|---|
| Use Case Definition Workshop | Plant onboarding or new demand wave | Define next use cases; follow up status of running projects; prioritize for a machine integration wave; starting point for a rollout project | Multi-day in the Standard Agenda (agree a preferred window with the plant) | Use case list with canvases, priority by process, tool availability status, next steps local and central |
| Use Case Integration Workshop | Use case ready for integration | Project status and formal closure or handover of the connectivity project; integration based on available equipment connectivity; requirements collection; integration sessions; tool trainings with key users; feedback from OPEX, Engineering, Production; use case utilization | Typically two days on site | Roadmap status (machines connected against target), dashboard structure per area, requirements per use case, utilization table |
| Use Case Equipment Integration Workshop | Start of equipment integration for a priority area | Starting point for equipment integration (prio machines), plant tour of focus machines, PLC overview and machine list (program availability, interfaces, network infrastructure), target budget calculation and project plan | Agenda plus summary | Machine baseline, use cases per area, IT preconditions, next steps toward the eCR |
| Machine Integration Workshop | Machine connectivity need | Concept and process of machine integration, standardization, data model integration | Single day at the start of a combined workshop | Machine list and connectivity status |
| Combined Use Case and Machine Integration Workshop | Both needs at once | Joint days with the use case lead and the machine integration lead presenting alternately | A multi-day format shared across two plants | Status and savings of actual use cases, resource footprint, required systems, pain points |
| Savings Workshop | Need for quick progress on cost saving | On-site support to produce progress on use cases such as digital downtime recording, automatic OEE calculation, plan/fact deviation, hourly output | Short, on-site | eCR next steps per plant (for example a downtime reporting app, machine integration wave 2) |

Rule on order (speaker notes on several decks): "Dependent on which workshop format is first >>
Machine Integration or Use Case Workshop." Decide it with the plant before the invitation.

## 2 · The Definition Workshop in detail (Standard Agenda)

| Day | Block | Content (from the agenda slides) |
|---|---|---|
| 1 Introduction | 1.1 Intro to the OD organization | What OD is, strategic pillars (digitalization benefit analysis; system and connectivity assessment; system and connectivity roadmap; use case executive support; demands and iterations; enhanced process understanding and control), the call format COP (how are we doing); ODEC (why prioritize) is a historical forum whose past decks are a source of information |
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

## 3 · What a good output looks like (plant summary deck)

The summary deck sent after a workshop holds, in this order: the OD architecture reference as a reminder; the
list of tools with the plant's status per tool (done, ongoing, not available) and a recommendation per tool such
as "needed for multiple use cases" or "not necessary"; the top few use cases by current priority per process
(high, medium, low), with the reason when the time frame is longer (for example "infrastructure and an app
needed first"); the open task "savings estimation for use cases"; and next steps split into local (finish machine
integration, define the next wave, re-upload the eCR, evaluate use cases for a savings-tracking project, check
the library) and central (enforce Cyber Security approval for a tool, define a standard data model for a process
family). A savings figure quoted in such a deck without a shown basis is a workshop estimate, not a calculation.

## 4 · Workshops on record: where to look

The list of past definition, integration, equipment integration, machine integration and savings workshops, with
plant and date, lives in the `Slide Index` of the vault folder `10-Workshops`. Read it live before naming a past
workshop as a precedent. Not every plant on the list has a recorded outcome; to find out which workshops led to
live use cases, filter the live use case list on its workshop or intake source rather than counting from decks.

## 5 · Lessons already written down

- Fitting savings calculation into the broader agenda "messed up the workshop" with too many
  domains on the table (`bc-build`, review checklist). Book it as its own follow-up.
- A tool demoed at a plant does not put the use case in scope there (`od-use-case-intake-triage`,
  refusal playbook): read the tool availability table first.
- Integration workshops end with utilization: who uses it, how often, which actions.
  Utilization is asked at the workshop, not only on the Scorecard.
- Choose the examples "everybody understands" (recent decks use SMED and digital Gemba) to link
  a digital use case to a method the plant already runs.
