---
name: od-capital-request
description: >-
  Package a use case's value and cost into a capital request (the eCR) so the human approvers can decide - work
  out which spend gate and approver the amount hits, assemble the evidence, the value rows from
  od-benefit-calculation with their firmness, the cost side, options, risks, dependencies and a validation plan
  for the funded phase, and record the dependency and the outcome. Drafts only: submission and approval are human.
  Use when a Lane 2 use case has passed its business case and needs investment, when a Lane 3 system or connector
  needs funding before demand is handed to IT, or when a saving is waiting on ECR CREATION or ECR APPROVAL.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-capital-request
  tier: practice
  lane: [lane-2, lane-3]
  new_state_lane: "Lane 2 (25), Lane 3 front-end (33)"
  new_state_step: "Capital request if investment is needed; Business case, prioritization, capital request"
  department_names: ["bc-capital-request", "ecr-builder", "capital-request-builder", "eCR"]
  owner_role: human:jakob.gabriel
  authority_level: draft the request; submission and approval are human
  status: draft
  sources_read: 2026-11-10
  requires: [od-context]
  composes: [od-benefit-calculation, od-decision-routing, od-prototype-poc, od-portfolio-and-savings-analysis, od-use-case-solution-evaluation, od-system-fit-check, od-investment-input, od-cybersec-gate, it-demand-package, od-handover-and-adoption]
  derived_from:
    - "Work vault, OD Department Knowledge/OD-instance/30-skills/ecr-builder.zip (SKILL.md, reference/*, assets/build_ecr.py, render_qa.sh), read 2026-11-10"
    - "Work vault, Document Texts/Department Documents/OESL 'stand-alone'- eCR Approval Flow 2026.03.02.md, read 2026-11-10"
    - The new-state flow (docs/new-state-flow.md, docs/new-state-conformance.md and the skill-map table docs/new-state/OD_NewState_VSM_SkillMap.html), Lane 2 step 5, Lane 3 step 3 and the gap register, read 2026-11-05
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/08-decision-rights.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/15-resources.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/10-Department/Decision rights.md
    - ops-knowledge-graph/_knowledge/10-Department/Savings and value tracking.md
    - ops-knowledge-graph/_knowledge/90-Sources/du-overview/OneDrive_1_21.8.2026/260818_DU_Setup_Timeplan.md
    - Work vault (Work-OpsDigit-Knowledge), Graph/Business Cases, all notes mined as a pattern for what a business case holds, read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Graph/Registers Blocker Register and Savings Basis Register, the eCR mentions, read 2026-11-05
    - Skills od-decision-routing and od-benefit-calculation, read 2026-11-05
    - "Work vault, OD Department Knowledge/OD-instance/eCR_Management_Summary_inventory.md, read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/skills-inventory-and-roadmap.md and OD_Skill_Naming_Convention.md, read 2026-11-10"
  okf:
    type: Agent Skill
    title: Capital request
    tags: [use-case-support-service, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---

# Capital request

Read `od-context` first.

This is the department's `od-capital-request` (its package `ecr-builder`), the last link of
its business-case chain: value from `od-benefit-calculation`, cost from `od-investment-input`, assessment
verdict, then this package for the approval route. It does not recalculate value, set thresholds or approve.

**The form and the builder.** The department's inventory of the eCR management summary (sections, enums, governance
conditionals) is in [`references/ecr-management-summary.md`](references/ecr-management-summary.md); the department's
eCR builder package (`30-skills/ecr-builder.zip`, the master) is transcribed in full: its five-step workflow
([`ecr-builder-workflow.md`](references/ecr-builder-workflow.md)), the backbone and conditional rules
([`backbone-and-conditionals.md`](references/backbone-and-conditionals.md)), the colour-coded honesty layer
([`grounding-and-color-coding.md`](references/grounding-and-color-coding.md)), the refusal gate, de-risk question bank
and closing slide ([`open-items-and-conflicts.md`](references/open-items-and-conflicts.md)) and the renderer
([`build-engine.md`](references/build-engine.md), [`scripts/build_ecr.py`](scripts/build_ecr.py),
[`scripts/render_qa.sh`](scripts/render_qa.sh); the neuwerk template `_nw_template.pptx` comes from the package).
**Who approves** is in [`references/ecr-approval-matrix.md`](references/ecr-approval-matrix.md) (by role, tier and case
type). Still not in the sources: the system the eCR is filed in, who files it, how long approval takes. The investment planning template that the project-support lane lists as an asset is
⟨to confirm or create⟩ in the resources registry (`00-core/15-resources.md`).

## The references are the substance

| File | Use it for |
|---|---|
| [`references/ecr-management-summary.md`](references/ecr-management-summary.md) | The eCR section map, enums and governance conditionals, and the builder's house rules (refusal gate, grounding, open items, maturity verdict) |
| [`references/ecr-builder-workflow.md`](references/ecr-builder-workflow.md) and its four references | The department's builder: ingest, refusal gate, grounded backbone, honesty deck, verdict, rendering |
| [`references/ecr-approval-matrix.md`](references/ecr-approval-matrix.md) | The approver chain by amount tier and case type (IT invest, expansion, R&D, real estate) |
| [`references/spend-route.md`](references/spend-route.md) | How to find the spend gate and approver for an amount, the ambiguity to resolve with the OD lead, how it sits in Lane 2 and Lane 3, what a booked saving waits on |
| [`references/business-case-structure.md`](references/business-case-structure.md) | What a business case holds, mined from the vault notes: sections, ranges, scores, validation plans, prerequisites, what is typically missing (no figures) |
| [`assets/capital-request-package.md`](assets/capital-request-package.md) | The package this skill produces and the human submits |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Management-summary shape, decisions with risk of not doing, pilot and scope-limiting patterns, mandatory sensitivity, the offer-eCR-contract consistency check, and what an agent may draft |

## Where it sits

- **Lane 2, step 5**: "Capital request (if invest needed): package value and cost for approval." Waits on MPEE /
  BA Operations approval; the queue time is a placeholder in the skill-map table.
- **Lane 3, shared front-end, step 3**: "Business case and capital request: value and cost; capital request if
  needed; hand off once demand is clear." Waits on IT commitment and MPEE approval.
- Upstream: `od-benefit-calculation` (value rows), `od-portfolio-and-savings-analysis` (ranking),
  `od-prototype-poc` (validation record), `od-use-case-solution-evaluation` / `od-system-fit-check` (verdict).
- Downstream: the human approvers; then `od-handover-and-adoption` and the build.
- Not the same as `od-investment-input` (planned): that one is the investment planning input pack for equipment
  integration in the Information Integration lane (skill-map row II-07). Whether the two merge is open.

## Procedure

1. **Confirm a request is needed.** Is there money to commit (hardware, licences, external work, headcount)? If
   the work is within the plant roadmap and spends nothing new, no capital request: record that and stop.
1b. **Refusal / de-risk gate** ([`open-items-and-conflicts.md`](references/open-items-and-conflicts.md)). If the value
   backbone, the investment estimate or the assessment verdict is missing or too thin to carry the amount, stop and
   return the de-risk questions from its question bank, not a package.
2. **Collect the inputs.** The use case record, the benefit rows (`od-benefit-calculation`), the validation
   record (`od-prototype-poc`), the solution-evaluation verdict, the Plant ME agreement on priority.
3. **Route first** (`od-decision-routing`): read the amount against the tiers of the approval matrix
   ([`ecr-approval-matrix.md`](references/ecr-approval-matrix.md)), classify the case (IT invest, expansion, R&D, real
   estate) and list the approvers by role. If the recorded
   ladder is ambiguous for the amount, do not pick a side silently
   ([`references/spend-route.md`](references/spend-route.md)). Also name the other gates the spend touches: IT
   demand (`it-demand-package`), Cyber Security (`od-cybersec-gate`, `od-equipment-integration`).
4. **State the ask** in one line: amount, what it buys, what phase it funds, by when it must be decided.
5. **Pull the value in, do not rebuild it.** Take each saving row with amount, year, category, rationale,
   methodology, reliability and dependency. Show **tracked and proven separately, never summed**
   (`od-benefit-calculation`). Where a row has no methodology it is an estimation: label it so.
6. **Write the cost side.** One-time and recurring, split into people, hardware, licences, external, compute and
   IT demand ([`references/business-case-structure.md`](references/business-case-structure.md)). Every figure has a source
   and a date, or is ⟨to be collected⟩ with the role who supplies it. `od-benefit-calculation` is thin on cost
   (the conformance page notes it once); this section is where the cost side lives.
7. **Give options and the do-nothing case**, and for each decision its risk of not doing. At least: the request, a smaller or staged version, and not acting.
   Include the library alternative (adopt a proven solution) if one exists.
8. **State risks, sensitivity and dependencies.** The one assumption the case fails on, a range not a point where
   the value is asserted, an adoption haircut if people must act on the output, prerequisites that must exist.
9. **Define what the money buys and how it will be judged:** a validation plan or stage gate for the funded phase
   with a pass criterion, a validator and a date (pattern in `od-prototype-poc`).
10. **Record the gate as a dependency** on the use case and on each affected saving row (`ECR CREATION` while
    drafting, `ECR APPROVAL` once filed), with the owner (`od-benefit-calculation` dependency list).
10b. **Render** the management summary with the builder ([`build-engine.md`](references/build-engine.md)): every figure
    carries its grounding chip, the last slide is Open items and conflicts, and the reply mirrors it in one line.
11. **Hand the package to the human** to review and submit. Stop there. After the decision, record the outcome
    in the package and update the dependency.

## Maturity verdict

Close every package with the open items and conflicts and one verdict: **Ready to sign**, **Sign the
floor** (approve the grounded part only) or **Not ready**. Recommendation only.

## Definition of done

The package in [`assets/capital-request-package.md`](assets/capital-request-package.md) is complete or its gaps are
named with a role who closes them; the route and approver are written next to the amount; tracked and proven
euros are separate; the dependency is recorded on the saving rows; a human has been handed the package. Nothing
has been submitted or approved by the agent.

## What is still open

- ⟨System the eCR is filed in and who may file⟩: not in any source; the form content is the builder's backbone. OD lead with BA Operations / Finance.
- ⟨Whether the 2026-03-02 approval matrix (OESL stand-alone) still applies under neuwerk⟩. Finance.
- ⟨Approval lead time⟩: the skill-map queue is a placeholder. OD data.
- ⟨Cost rates (people, hardware, compute) the department should use⟩: the vault cases use their own FTE rates; none is
  an OD standard. Finance.
- ⟨The investment planning template⟩ and ⟨the use-case business-case template⟩ (`00-core/15-resources.md`). DBVE / OD lead.
- ⟨Whether this skill and `od-investment-input` merge⟩. OD lead.

## Do not

- Do not call the request ready before offer, eCR and contract agree on version and a named role drives purchasing (`references/process-chain-practice.md`).
- Do not net value against cost, and do not print NPV or IRR when no measured baseline exists; fund the baseline first.
- Do not submit, sign, approve or state that approval will be given. Those are human (`od-decision-routing`: an
  agent never commits investment or allocates resources).
- Do not put a threshold, a form field or an approval time in the package that no source gives.
- Do not add tracked and proven euros together, or present a saving that is waiting on this approval as booked.
- Do not turn a missing value into zero, or a range into its mid-point without saying so.
- Do not invent cost lines or rates; mark them ⟨to be collected⟩.
- Do not duplicate `od-benefit-calculation`: reference its rows, do not re-derive them.
- Do not split one investment into several requests to land under a threshold (a proposed rule, not stated in the sources).
