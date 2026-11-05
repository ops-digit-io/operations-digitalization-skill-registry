---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for template resolution, abstracted from the Operations Digitalization slide decks - the template types the chain uses and at which step, the seven-step pipeline for a template-bound generated deliverable, placeholder-leak and residue checks. Names template types only; locations come from the register.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - which template at which step

Deck-derived practice for the spine and for every step that fills an artefact. This file names **template types** the decks use; it states no location, owner or approval. Those come from the register (`master-register.md`). `PROPOSAL` = registry synthesis.

## 1. Method in practice

1. Name the step (process id) and the artefact; look up the type in section 2; then resolve the master as in `SKILL.md`.
2. **Seven-step pipeline for a template-bound generated deliverable** (the decks' reference):
   1. read the department context by relevance;
   2. read the brand template and its layouts;
   3. **human gate** on what cannot be derived (lane, depth, language);
   4. map fields to template elements, each with a source;
   5. apply the honesty rules ("to confirm" gaps stay out of the output; every element traces to a source field);
   6. build, render, inspect and fix (overflow, invisible text, low contrast, clipped bullets);
   7. deliver editable with a validation and **placeholder-leak check**.
3. Record in the resolution record which template, which version date, which gate answers.

## 2. Template types by step (types, not files)

| Step | Artefact type the decks use | Core content |
|---|---|---|
| i1 intake | problem statement, quick charter | SMART statement; business problem, benefit, deadline and why, sponsor, risk if not solved, obstacles, modify-or-new |
| 21 define | use-case canvas (plant-filled and as-is / to-be variants) | challenge, current state, solution idea, stakeholders, scalability, dependencies, success criteria, obstacles, requirements and gaps, data, infrastructure, change, urgency x importance, cost / benefit; per process step a data table "from machine / from checklist / from system" |
| 21 workshop | agenda with audience matrix; capture sheet; summary deck | agenda items x roles (required / recommended / optional); output split into local and central next steps |
| 21 / 26 | use-case one-pager and library card | problem, situation, digital support, identified in, machine integration used, development, link, can it replace a manual practice |
| 22 | user story; requirement list; signal list | "As `<role>` I want `<function>` to accomplish `<value>`" with acceptance criteria; signal id, label, source, why needed |
| 24 | savings table; benefit data model | per row: process area, base situation, improved by, saving factor, yearly effect, basis label |
| 25 / 33 | capital-request management summary; demand-request one-pager; project order | what / why / how, current versus future, investment by category, risks and opportunities, alternatives, timeline, safety statement; decisions as *decision - proposal - risk of not doing* |
| 31 | legacy assessment pack; kick-off agenda | as-is / to-be canvases, component inventory, risk table, impact table, component mapping |
| 3a4 | demand package; supplier question sheet | demand-management questions; same agenda for every supplier |
| 23 / sprint | sprint review, one-page initiative sheet | scope, target, value add, KPIs, savings, actions, lead, team, sponsor, documents location |
| 26 / 3a6 | utilization table; handover record; closure report | use case, who uses it, related process, utilization method, frequency, value, in use yes / no; closure checklist incl. "handover completed?" |
| spine | round agenda; plant status table; regional roadmap; plant management one-pager | see `od-scorecard-reporting` |

Where a type has no registered master, the gap rule in `SKILL.md` applies: draft clearly labelled, never presented as the template.

## 3. Decision rules

- **A finished deliverable is not a master** (restated); a deck from a similar earlier case is reference material only.
- **Not-applicable pages are hidden or moved to the back, not deleted** (project forms).
- **Never leave required fields blank in a form that has a rule:** budget is never left open, even for internal work (an educated guess, labelled); timing has at least start, end, first version and the first three milestones; out-of-scope is written out.
- **Language variants** of a canvas exist; use the language of the audience and say so.
- **A figure in a template is a placeholder until a source is named.** Identical placeholder figures across unrelated records are a copy signal.
- **Human gate on the underivable:** lane, depth, language, audience.

## 4. Handoff contract

| Receives | From |
|---|---|
| the step id and artefact name | the calling skill |
| register row and location | `master-register.md` |

| Hands on | To |
|---|---|
| resolution record: master, location, owner, date, outcome | the calling skill, attached to the deliverable |
| gap sentence naming the supplier role | the register owner (OD lead role) |

## 5. Pitfalls and lessons

- **Template residue:** leftover plan / forecast / actual tables with identical numbers survived into several initiative sheets; hidden sample data can leak into a deliverable.
- **Placeholder text left in a rendered deliverable** (visible or invisible); run the leak check after rendering.
- **Several competing forms for one purpose** (project order variants, canvas variants) lead to forks; pick the newer variant only if the register says so, otherwise show both with dates.
- **Template unused because nobody knows it exists:** the library of prompts, agents and skills works only if it is shared and findable.

## 6. Questions to ask and definition of done

Which step and which audience? Which language? Which register row? What can the context derive and what must a human decide? Which fields are still open?

**Done:** record filled; master opened at its location; leak check done; every field has a source or `<...>`.

## 7. AI agent operating notes

- **Can do:** map artefact to template type; look up the register row; fill fields from context with a source each; run the leak and residue check; list open fields.
- **Needs:** register rows, the master at its location, context files.
- **Human gate:** choice of template where two claim to be master; approval of any template; language and depth.
- **Must cite:** register row, master version date, source field per element.
- **Hands over:** the deliverable plus the resolution record.
