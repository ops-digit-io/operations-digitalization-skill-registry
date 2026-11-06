---
name: od-investment-input
description: >-
  Prepare the investment planning input pack once an integration roadmap or a use-case plan is agreed
  and budget is needed - cost lines per machine or system, the benefit side taken from the benefit
  case, the gates the spend must pass, and the open figures - so the OD lead and BA Operations can
  decide. Covers the cost template for a standardized system (Lane 1b), the wave pack after an
  equipment assessment, and the cost side handed to a capital request (Lane 2 step 5, Lane 3 step 3).
  It prepares the input; it never approves or commits spend. Use when a roadmap is agreed and the plant
  asks "what does this cost and who approves it", when an assessment lists machines that need hardware,
  or before a capital request is written.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-investment-input
  tier: practice
  lane: information-integration-service
  new_state_lane: Lane 1b (cost template), Lane 2 step 5, Lane 3 step 3
  new_state_step: "Investment input: cost and approval"
  owner_role: human:jakob.gabriel
  authority_level: recommend
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-equipment-integration, od-decision-routing, od-benefit-calculation, od-system-fit-check, od-cybersec-gate, od-capital-request, catalog-systems, od-information-integration-service]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/08-decision-rights.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/information-integration-service/playbook.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/information-integration-service/tasks.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/project-support-consultancy/skills.md
    - New-state flow (docs/new-state-flow.md and docs/new-state/OD_NewState_VSM_SkillMap.html), the Lane 1b cost-template step, the Lane 2 capital-request step and the Lane 3 shared front-end, read 2026-11-05
    - Skills od-decision-routing and od-benefit-calculation (the spend ladder, the dependency values), od-equipment-integration (assessment protocol section 3, edge-device hardware constraint) and od-system-fit-check (tool boundaries with their recorded cost references), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Graph/Business Cases notes Sensor-Upgrade Decision Frame and PLC Evergreening, and Case Groups - Overview, read 2026-11-05
    - Work vault bundle file kg_nodes.csv, Machine records read as an aggregate (integration status, priority, method), 2026-11-05
  okf:
    type: Agent Skill
    title: Investment input pack
    tags: [information-integration-service, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Investment input pack

Read `od-context` first.

**Plan row II-07** (`OD_Skill_Map.md`): trigger "roadmap agreed, budget needed"; output "investment
planning input pack"; runs regionally; authority `recommend`; wave 2. The Skill Map lists "digitalization
investment approval" under *explicitly not skills*: "Skills may prepare the input (II-07), never the
approval." The decision stays central.

## Purpose and definition of done

Turn an agreed plan into a pack the deciders can read in one sitting: **what is bought, for which
machines or systems, what it costs (each figure with its source), what it is expected to return (tracked,
not proven), which gates it must pass, and what is still unknown.** The pack is done when every cost line
has a figure with a source or an open marker, the benefit side points at a `od-benefit-calculation`
record, the gate route is named, and the pack is handed over with a `od-decision-routing` decision
request. It is never "done" by approval: approval is not this skill's.

## Where it sits

| Where | Plan step | What the pack is |
|---|---|---|
| **Integration lane, step 2** | "Integration investment planning", IIAE with OD lead, control point "Investment approved" (`information-integration-service/playbook.md`) | The wave pack after an equipment assessment (Route A of `od-equipment-integration`, its protocol section 3 "Investment") |
| **Lane 1b** | Fill cost template and lightweight approval: "standardized, pre-priced spend, template, not a full business case" (VSM skill map) | The cost template for a standardized system from `catalog-systems` |
| **Lane 2 step 5, Lane 3 step 3** | Capital request, business case and capital request | The cost side that `od-capital-request` packages together with the value side |

The recurring-task table of the lane still lists the investment plan template as "⟨to confirm⟩"
(`information-integration-service/tasks.md`; also `project-support-consultancy/skills.md`, "investment
planning templates: author"). [`assets/investment-input-pack.md`](assets/investment-input-pack.md) is a
proposed form until the OD lead confirms it.

## References and assets

| File | Use it for |
|---|---|
| [`references/cost-lines.md`](references/cost-lines.md) | The cost lines an integration or system pack can carry, where each line's figure must come from, where the reference figures live, and how to size a wave from the live machine records |
| [`references/approval-route.md`](references/approval-route.md) | Who decides what, how to find the current spend ladder, the open threshold and the overlap in the ladder as written, and the dependencies to record |
| [`assets/investment-input-pack.md`](assets/investment-input-pack.md) | The pack itself |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Planning workflow and cost build-up, cost calculator before the project, staged scope, wave-decision checks, and what an agent may draft |

## Procedure

1. **Confirm the plan is agreed.** Wave pack: the roadmap is agreed with Plant ME / Plant IT (control
   point of step 1). Template pack: the match record of `catalog-usecase` / `catalog-systems` exists. Cost
   cannot be planned for a scope that is still moving; if scope is open, stop and say which part.
2. **Run the demand filter.** Keep only machines or systems that an accepted or planned use case needs
   (`od-equipment-integration`, assessment step 2). A `NOT INTEGRATED` machine nobody waits for is not a
   line in the pack.
3. **Check the footprint.** If any line is a system outside the lean footprint, run `od-system-fit-check`
   first; a line that adds a tool is a tool-rollout decision, not an investment line (see the approval
   route).
4. **Build the cost lines** from [`references/cost-lines.md`](references/cost-lines.md). One row per line,
   each with a figure and a source, or `⟨not known: who can supply⟩`. Do not average, do not fill from a
   similar plant without saying so, do not price internal effort unless the OD lead says so
   (some notes, such as `Case Groups - Overview`, take costs as zero by an owner statement, which is a
   convention of that note and not a rule for this pack).
5. **Put the benefit side next to it.** Link the `od-benefit-calculation` rows. Show **tracked** and
   **proven** euros separately and never add them. If no saving row exists, write "to be collected" and
   stop short of a payback figure.
6. **Name the gates.** Spend through eCR (approver per the current approval policy, look up:
   `od-decision-routing` and the OD lead); the budget threshold of the *digitalization investment planning* decision is
   still `⟨to confirm⟩` and is not guessed here. Add Cyber Security / OT (`od-cybersec-gate`) for any
   external connection, IT demand if the item touches a platform OD does not own.
7. **Record the dependencies** on the use case or saving rows (`ECR APPROVAL`, `ECR CREATION`, `MACHINE
   INTEGRATION`), so the wait is visible.
8. **State the open items** and who can close them (section "Still open" of the pack).
9. **Hand over.** Fill a decision request (`od-decision-routing`, `assets/decision-request.md`): row
   "Digitalization investment planning", owner OD lead, together with BA Operations, mode Consultation,
   approval yes, not reversible, `authority_level` `recommend`. For Lane 2 and Lane 3, pass the cost side
   to `od-capital-request`.

## Output

The filled pack. Its cost table and gate table are the parts a decider reads first; everything else is
traceability.

## Still open

- `⟨Budget threshold of the digitalization investment planning decision⟩` - the decision-rights table
  leaves it open. Supplier: OD lead.
- `⟨Unit costs for edge devices, OT hardware, licences, connector development⟩` - none are recorded in
  the sources read. Supplier: IIAE, from supplier quotes.
- `⟨The "lightweight approval" limit for a Lane 1b standardized system⟩` - the new-state flow says
  "small budget approval"; no amount or approver is named.
- `⟨Confirmed template⟩` for the investment plan.

## Do not

- Do not plan a wave without checking that the plant can execute, the layout is stable and controller patch status is on the plan.
- Do not price a return before a baseline exists; the first line is the measurement layer.
- Do not approve, commit, order, allocate resources or promise a budget; the pack recommends.
- Do not invent or interpolate a threshold, a unit price or a payback; use `⟨…⟩` and name who supplies it.
- Do not add tracked and proven euros, or present a benefit as proven (`od-benefit-calculation`).
- Do not plan a wave around the medium or small edge device: the recorded guidance says no approved
  small device exists (see `od-equipment-integration`, decision paths).
- Do not include a connection that has no Cyber Security route as "ready to schedule".
