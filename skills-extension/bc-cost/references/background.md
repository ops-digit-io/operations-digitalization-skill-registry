---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Purpose and definition of done

Turn an agreed plan into a pack the deciders can read in one sitting: **what is bought, for which
machines or systems, what it costs (each figure with its source), what it is expected to return (tracked,
not proven), which gates it must pass, and what is still unknown.** The pack is done when every cost line
has a figure with a source or an open marker, the benefit side points at a `bc-build`
record, the gate route is named, and the pack is handed over with a `dept-decision-rights` decision
request. It is never "done" by approval: approval is not this skill's.

## Where it sits

The recurring-task table of the lane still lists the investment plan template as "⟨to confirm⟩"
(`information-integration-service/tasks.md`; also `project-support-consultancy/skills.md`, "investment
planning templates: author"). `assets/investment-input-pack.md` (`assets/investment-input-pack.md`) is a
proposed form until the OD lead confirms it.

## Outputs and hand-off: the text before outputs.yaml

`bc-cost` delivers the cost side of a business case or a wave, ready for the deciders to read in one sitting.
It prepares the input only; approval is never its output.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Investment input pack | `assets/investment-input-pack.md`, filled | OD lead together with BA Operations | Every cost line has a figure with a source or an open marker; the gate route is named; open items are listed with who can close them |
| Investment estimate for one use case or system | `assets/investment-estimate.md`, filled | `bc-capital-request` (Lane 2 and Lane 3), plant budget owner (Lane 1b cost template) | One-time build, licences and hardware, recurring run cost and multi-year TCO for the minimum viable rollout and the maximum scale-out; every figure tagged `[quote]`, `[assumption]` or `[market]` |
| Benefit side reference | Link to the `bc-build` rows inside the pack | `bc-capital-request` | Tracked and proven euros shown separately and never added; if no saving row exists, "to be collected" is written and no payback figure is given |
| Dependencies and gates | Gate table and dependency list in the pack | `dept-decision-rights` | Gates named (eCR, Cyber Security / OT, IT demand where it applies); dependencies (`ECR APPROVAL`, `ECR CREATION`, `MACHINE INTEGRATION`) recorded |
| Decision request | Filled `assets/decision-request.md` of `dept-decision-rights`, row "Digitalization investment planning" | `dept-decision-rights` | Owner OD lead with BA Operations, mode Consultation, approval yes, not reversible, `authority_level` `recommend` |

## Handoff

- **Receives from:** `mi-equipment` (assessment and wave scope), `catalog-usecase` (match record for a standardized system), `bc-build` (the benefit rows), `invest-screen` (footprint check for any line outside the lean footprint).
- **Next in the flow:** `dept-decision-rights` (step 1b2, cost template and approval), `bc-capital-request` (step 25, cost side packaged with the value side), `deploy-cybersec` for any external connection (step 1b3). On step 24 the cost side sits next to `bc-build` and `bc-assess`.
- **Stops here when:** the scope is still moving, a line is a system outside the lean footprint with no fit check, a connection has no Cyber Security route, or a figure would have to be invented. Mark it `⟨not known: who can supply⟩`, say which part is open, and do not hand over a payback or a threshold.

## Plan row and skill map notes

- Plan row II-07 (`OD_Skill_Map.md`): trigger "roadmap agreed, budget needed"; output "investment planning input pack"; runs regionally; authority `recommend`; wave 2.
- The skill map lists "digitalization investment approval" under *explicitly not skills*: "Skills may prepare the input (II-07), never the approval." The decision stays central.

## Where the cost side sits (table)

| Where | Plan step | What the pack is |
|---|---|---|
| Integration lane, step 2 | "Integration investment planning", IIAE with OD lead, control point "Investment approved" (`information-integration-service/playbook.md`) | The wave pack after an equipment assessment (Route A of `mi-equipment`, its protocol section 3 "Investment") |
| Lane 1b | Fill cost template and lightweight approval: "standardized, pre-priced spend, template, not a full business case" (VSM skill map) | The cost template for a standardized system from `catalog-usecase` |
| Lane 2 step 25, Lane 3 front-end step 33 | Capital request, business case and capital request | The cost side that `bc-capital-request` packages together with the value side |

## Convention note

- Some knowledge notes (for example a case-groups overview) take costs as zero by an owner statement. That is a convention of that note, not a rule for this skill.
- Open: the confirmed template for the investment plan and real unit costs from IIAE quotes are not available in the sources read.
