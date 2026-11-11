---
type: Skill Reference
title: Outputs
description: The outputs od-investment-input must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-investment-input` delivers the cost side of a business case or a wave, ready for the deciders to read in one sitting.
It prepares the input only; approval is never its output.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Investment input pack | `assets/investment-input-pack.md`, filled | OD lead together with BA Operations | Every cost line has a figure with a source or an open marker; the gate route is named; open items are listed with who can close them |
| Investment estimate for one use case or system | `assets/investment-estimate.md`, filled | `od-capital-request` (Lane 2 and Lane 3), plant budget owner (Lane 1b cost template) | One-time build, licences and hardware, recurring run cost and multi-year TCO for the minimum viable rollout and the maximum scale-out; every figure tagged `[quote]`, `[assumption]` or `[market]` |
| Benefit side reference | Link to the `od-benefit-calculation` rows inside the pack | `od-capital-request` | Tracked and proven euros shown separately and never added; if no saving row exists, "to be collected" is written and no payback figure is given |
| Dependencies and gates | Gate table and dependency list in the pack | `od-decision-routing` | Gates named (eCR, Cyber Security / OT, IT demand where it applies); dependencies (`ECR APPROVAL`, `ECR CREATION`, `MACHINE INTEGRATION`) recorded |
| Decision request | Filled `assets/decision-request.md` of `od-decision-routing`, row "Digitalization investment planning" | `od-decision-routing` | Owner OD lead with BA Operations, mode Consultation, approval yes, not reversible, `authority_level` `recommend` |

## Handoff

- **Receives from:** `od-equipment-integration` (assessment and wave scope), `catalog-usecase` (match record for a standardized system), `od-benefit-calculation` (the benefit rows), `od-system-fit-check` (footprint check for any line outside the lean footprint).
- **Next in the flow:** `od-decision-routing` (step 1b2, cost template and approval), `od-capital-request` (step 25, cost side packaged with the value side), `od-cybersec-gate` for any external connection (step 1b3). On step 24 the cost side sits next to `od-benefit-calculation` and `bc-assessment`.
- **Stops here when:** the scope is still moving, a line is a system outside the lean footprint with no fit check, a connection has no Cyber Security route, or a figure would have to be invented. Mark it `⟨not known: who can supply⟩`, say which part is open, and do not hand over a payback or a threshold.
