---
type: Skill Reference
title: Backout plan proposal
description: PROPOSAL. Structure of a back-out plan for a migration stage - the decks hold only diagrams of the actors, so the content here is synthesis to be confirmed by the owner of the back-out process.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [migration, template, proposal]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Back-out plan (PROPOSAL)

**What the sources give:** back-out plans exist per platform component (edge container, whole VM, service bus on Linux and on Windows, MES vendor tools, energy monitoring). The decks show two actors only, central IT and central engineering, as diagrams. No steps, triggers or timings. Everything below is `PROPOSAL`; the owner confirms or replaces it.

## Structure (one plan per stage and component)

1. **Scope**: component, location, stage, version before and after.
2. **Actors and roles**: central IT, central engineering, local key user, local IT, application owner; who decides, who executes. `<decision owner>`.
3. **Trigger criteria**: the observable conditions that start the back-out, agreed before the window (for example a verification item red at the checkpoint, data flow missing, interface down). `<criteria>`.
4. **Decision point and time-box**: the latest moment to decide inside the outage window so the way back still fits. `<time>`.
5. **Points of no return**: steps after which going back is no longer possible or costs data (for example old data cleaned, licence key reset, old VM released). Mark them; do not cross them before verification.
6. **Preparation**: backup or snapshot taken and restore tested, old configuration saved, licence key kept, DNS and certificate old values noted, old server left intact until the end of the observation period.
7. **Back-out steps**: ordered, per component, each with executor and expected result.
8. **Verification after back-out**: the same key-user list as the cutover, run on the old system.
9. **Communication**: who is told, when (production, customer-facing contacts, Cyber Security); templates.
10. **After a back-out**: lessons, root cause, new date, updated risk row; the location returns to red until re-planned.

## Rehearsal

Read the plan with the executing people before the window. Where possible rehearse the restore on a test instance. A back-out nobody has read counts as missing.

## Ties to other skills

Cyber Security and deployment review may require the plan as a deployment artefact (`od-cybersec-gate`, `deploy-appstore`); the form of that requirement is `<to confirm>`.
