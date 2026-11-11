---
type: Skill Reference
title: Gemba App pilot
description: The Gemba App requirements-to-mockup pilot as a method to copy - the process, the click-dummy prompt system, what an initiative request for a prototype should contain, and what the sources do not show. No dates, budgets or status of the live initiative.
resource: ../SKILL.md
status: draft
tags: [use-case-support-service, practice]
---
# Gemba App pilot

The only worked example of a prototype in the department's own material. Label: **pilot**
(`AI_Where_We_Apply_Today.pptx`; check the current label there). Read it as a method worth copying and an outcome nobody has
recorded.

## Where to read it live

| Source | What it is |
|---|---|
| Department knowledge base project folder (README, quick start guide, click-dummy template prompt, example production dashboard spec) | A Claude project export: a prompt system for generating click-dummies |
| Department archive (read-only), `13-AI_Activities/2026-08-AI_Initiatives_Pitch/04-AI based Requirements Engineering Mockup Creation/` | The initiative deck and a generated HTML mock-up. Read it for the current problem, target, plan and budget state; do not copy them into a skill |
| Department knowledge base (AI-curated) | Describes the process in an AI usage deck |

## The process (as described, not as measured)

1. Requirements are collected **once, globally**, from the Gemba walk standard, a forms survey and shopfloor
   reality, with site and language scope stated.
2. They are refined: solution bias removed, requirements made atomic and testable, plant conflicts resolved, one
   vocabulary, assumptions parked.
3. One generative-AI prompt turns them into a clickable HTML mock-up (and, per the business-case note, a product video).

That is `funnel-requirements` followed by a mock-up. The skill that owns steps 1 and 2 is
`funnel-requirements`; this skill starts at 3.

## What an initiative request for a prototype should contain (pattern seen in the archive deck)

- **Problem:** what differs between plants today (standards, local digital solutions, data lost on a physical board,
  weak top-down feedback).
- **Target:** one standard across locations for the process in scope, and which signals link to machine data where possible.
- **Actions:** requirements collection including data model and mock-ups, a functional prototype, evaluation and
  iteration, kick-off with IT if a low-code route is chosen.
- **Not part of the project:** an explicit list (rollout activity and hardware purchasing in this example).
- **Plan and money:** timing and budget fields exist; in the example they were still open. Savings and KPIs may be empty
  at this stage - leave them empty rather than inventing a figure.
- **Value:** where the value is not easily quantified, say so and describe the expected effect (communication between
  levels, reaction time, structured problem solving) without a number.
- **Survey:** a short forms survey asks each location whether it wants the standardized solution, whether it already uses
  one, which, what challenges it has, and for a screenshot.
- **Risks named:** budget availability, acceptance by locations, involvement of location management; dependencies on
  budget and IT.

## The click-dummy prompt system (knowledge base export)

A template (`click_dummy_template_prompt`) and a worked example (`example_production_dashboard_spec`: a production
monitoring dashboard with overview, machine detail, a downtime-logging modal and a history view). What it fixes:

- **Output:** one standalone HTML file, no backend, no real API calls, no authentication; invented but realistic
  example data; a size cap for the single file.
- **Brief structure:** application context (type, users, purpose, features), required screens each with purpose,
  components and user actions, a data structure for the mock data, an interaction flow, technical and style rules.
- **Must show:** loading, empty and error states, light and dark mode, mobile layout.
- **Quality checklist:** all screens reachable, buttons have feedback, forms show validation, empty states designed,
  text readable. Success is stated as "understandable without explanation".

`assets/click-dummy-brief.md` (`../assets/click-dummy-brief.md`) is the distilled version of that structure, written
so it also works with a tool other than the one in the export.

## What the sources do not show

- **No result.** No pass criterion, no user test, no record of how many locations saw the mock-up, no decision to go to
  build. "Pilot" is a status label, not an outcome. ⟨Outcome of the Gemba App pilot⟩: the initiative owner.
- **No cost and no benefit.** Budget and savings are open on the request; value is described as not easily
  quantified. Do not quote a figure for it.
- **Tool route unclear.** The export prescribes a web front-end stack built to one HTML file; the initiative deck names a
  low-code framework for the real app. They may be two stages (mock-up, then app); the sources do not say.
  ⟨Which tool builds the production app⟩: OD lead with IT.
- **The mock-up is not the data.** The example dashboard spec uses invented machines and values. A mock-up
  shows layout and flow; it says nothing about whether the signals exist (`mi-data-availability`).

## What to copy

- A requirements brief written before the mock-up, with atomic and testable requirements.
- Invented example data, clearly marked, so no one mistakes the mock-up for a live view.
- A survey of the people who will use it, before and after.
- An explicit "not part of the project" list.

## What to add

The pilot record has no pass criterion. Add one before the build (`validation-patterns.md`).
