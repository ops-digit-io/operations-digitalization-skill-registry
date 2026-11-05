---
type: Skill Reference
title: Gemba App pilot
description: What the vault and the department archive hold on the Gemba App, the AI requirements-to-mockup pilot - the process, the click-dummy prompt system, the initiative request and what none of it shows.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [use-case-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Gemba App pilot

The only worked example of a prototype in the department's own material. Label: **pilot**
(`AI_Where_We_Apply_Today.pptx`). Read it as a method worth copying and an outcome nobody has recorded.

## Sources read (2026-11-05)

| Source | What it is |
|---|---|
| Personal vault, `AI-Brain/Claude Projects/Gemba App/` (README, quick start guide, click-dummy template prompt, example production dashboard spec; two long Gemba management knowledge files not read in full) | A Claude project export: a prompt system for generating click-dummies. Dated 2024-02-06 in its version history; the project export record is dated 2026-02-07 |
| Department archive (read-only), `13-AI_Activities/2026-08-AI_Initiatives_Pitch/04-AI based Requirements Engineering Mockup Creation/`, the initiative deck (15 slides) and a generated HTML mock-up | The initiative request, dated 12 August 2026 |
| Work vault, `Graph/Business Cases/AI Requirements Engineering Pipeline.md` (archive link, medium confidence, AI-curated) | Describes the process in slide 10 of an August 2026 AI usage deck |

The HTML mock-up file was not opened.

## The process (as described, not as measured)

1. Requirements are collected **once, globally**, from the Gemba walk standard, a forms survey and shopfloor
   reality, with site and language scope stated.
2. They are refined: solution bias removed, requirements made atomic and testable, plant conflicts resolved, one
   vocabulary, assumptions parked.
3. One generative-AI prompt turns them into a clickable HTML mock-up (and, per the business-case note, a product video).

That is `od-requirements-breakdown` followed by a mock-up. The skill that owns steps 1 and 2 is
`od-requirements-breakdown`; this skill starts at 3.

## The initiative request (archive deck, 12 August 2026)

- **Problem:** plants follow different standards for production output on the whiteboard; some plants have a
  local digital solution that is not standardized; data on the physical board is lost; top-down feedback to line
  leaders is weak.
- **Target:** one standard for all locations for hourly production monitoring (manual and automated, linked to
  machine data through an API endpoint where possible), stoppages and breakdowns (linked to the downtime app) and
  Gemba management (level management, actual issues and countermeasures, escalated topics).
- **Actions on the slide:** requirements collection including data model and mock-ups, a functional prototype,
  evaluation and iteration, kick-off with IT for low-code apps. The deck names a low-code framework (Mendix) in
  the title slide.
- **Not part of the project:** rollout activity and hardware purchasing.
- **Plan and money:** timing "to be planned / estimated with IT", budget "to be defined", planned bottom up;
  "end of Q1 / requirements" is the one date given. Savings and KPIs are empty ("-").
- **Value:** the last slide records that regional OpEx colleagues said the value in euros is "not so evident",
  while the effect on communication between levels, reaction time and structured problem solving is expected to
  be large. No number.
- **Survey:** a short forms survey asks each location whether it wants a standardized digital Gemba solution,
  whether it already uses one, which, what challenges it has, and for a screenshot.
- **Risks named:** budget availability, acceptance by locations, involvement of location management; dependencies
  on budget and IT.

## The click-dummy prompt system (vault export)

A template (`click_dummy_template_prompt`) and a worked example (`example_production_dashboard_spec`: a production
monitoring dashboard with overview, machine detail, a downtime-logging modal and a history view). What it fixes:

- **Output:** one standalone HTML file, no backend, no real API calls, no authentication; invented but realistic
  example data; a target size under 5 MB.
- **Brief structure:** application context (type, users, purpose, features), required screens each with purpose,
  components and user actions, a data structure for the mock data, an interaction flow, technical and style rules.
- **Must show:** loading, empty and error states, light and dark mode, mobile layout.
- **Quality checklist:** all screens reachable, buttons have feedback, forms show validation, empty states designed,
  text readable. Success is stated as "understandable without explanation".

[`assets/click-dummy-brief.md`](../assets/click-dummy-brief.md) is the distilled version of that structure, written
so it also works with a tool other than the one in the export.

## What the sources do not show

- **No result.** No pass criterion, no user test, no count of locations that saw the mock-up, no decision to go to
  build. "Pilot" is a status label, not an outcome. ⟨Outcome of the Gemba App pilot⟩: the initiative owner.
- **No cost and no benefit.** Budget and savings are empty on the request; value is described as not easily
  quantified. Do not quote a figure for it.
- **Tool route unclear.** The export prescribes React, TypeScript, Tailwind and a build to one HTML file; the
  initiative deck names a low-code framework for the real app. They may be two stages (mock-up, then app); the
  sources do not say. ⟨Which tool builds the production app⟩: OD lead with IT.
- **The mock-up is not the data.** The example dashboard spec uses invented machines and values. A mock-up
  shows layout and flow; it says nothing about whether the signals exist (`od-data-availability-check`).

## What to copy

- A requirements brief written before the mock-up, with atomic and testable requirements.
- Invented example data, clearly marked, so no one mistakes the mock-up for a live view.
- A survey of the people who will use it, before and after.
- An explicit "not part of the project" list (rollout and hardware here).

## What to add

The pilot record has no pass criterion. Add one before the build ([`validation-patterns.md`](validation-patterns.md)).
