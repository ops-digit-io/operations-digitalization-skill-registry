---
type: Skill Reference
title: Order structure
description: The chapters of a project order (PREQ), the rule that applies to each chapter, the standard and extended variant, and the one-page short form for small initiatives.
resource: ../SKILL.md
status: draft
tags: [project-support-consultancy, practice]
---
# Order structure

The order is written from the steering committee's perspective. The project plan, produced at the
kick-off workshop, is the second artefact; its schedule is "part 2". Not-applicable chapters are hidden or
moved to the back, never deleted.

## Standard chapters

| Chapter | What goes in | Rule |
|---|---|---|
| Initial situation, history | Why now; earlier attempts | Reuse earlier projects to avoid double work; cite which |
| Requirements: scope | Expected results | Measurable; ties to the success criteria |
| Requirements: timing | Start, end, first version, first three milestones | That is the minimum; below it the plan is not a plan |
| Requirements: budget | Estimate of internal effort, external support, consultancy | Never blank, even for an internal project: "make an educated guess" |
| Benefit | Expected benefit | Taken from `bc-build` with its firmness; do not re-derive |
| Good practices, lessons learned | What to reuse | From earlier projects, with the source |
| Relationship to other projects | Dependencies and synergies | Anticipate critical areas |
| Out of scope | What the project will not do | Write it; it removes grey zones |
| Opportunities and risks | Classified lists | See [`roles-risks-procurement`](roles-risks-procurement.md) |
| Project organisation | Both sides, availability, training needs | Team availability and training needs are asked, not assumed |
| Approval | Who approved, date | Documented: signature, e-signature or e-mail |

## Newer variant adds

Initial situation, stakeholder expectations, a main-target proposal, boundary conditions, dependencies and
synergies, and an information-classification questionnaire.

## Extended order (larger or technical projects) adds

Project history; relationship to other projects; opportunities and risks with steering-committee boundary
conditions; value-add and cost analysis with MoSCoW; modular design for cost efficiency; a requirements
traceability matrix kept from requirements to validation; prototype and validation; a scale-up plan.

## Rules that decide quality

- **Main target as a 30-second message:** who does what for whom with which intention, phrased "at the end
  of the project we will have ...". Test: say it aloud once; if it needs a second breath, split or narrow.
- **Sub-targets:** each needs at least three work packages, otherwise the granularity is wrong. More than
  twelve sub-targets also means the granularity is wrong.
- **Success criteria:** fixed and agreed by all parties so progress is measurable. Not "better", but a
  measure with a baseline and a way to read it.
- **Budget and cost line:** always an estimate; say what it covers (internal effort, external support,
  consultancy). A line with `<...>` plus the owner who will fill it is allowed; a blank is not.
- **Unknown owners:** a project that cannot yet name sponsor, lead or team says so (`<...>` or "-"). An empty
  owner field on an initiative sheet is itself a risk to list.

## Short form (small initiative)

One page: scope, target, value add, KPIs, savings, actions (kick-off or definition, intermediate, closing or
wrap-up), lead, team, sponsor, documents location; results slide follows. A small initiative may carry a
"fast lane" tag. Critical points as open questions: who is responsible for setup, who for run, and from
when it can be used.

## Before it goes to approval (pre-send check)

Empty budget, timing below the minimum, no out-of-scope, no sponsor or lead, a high risk without
treatment, a sub-target with fewer than three work packages. Each is fixed or flagged `<...>` with an owner.
The sponsor's approval and the budget are human gates.

PROPOSAL: an AI agent runs this check and lists every finding at the top of the draft.
