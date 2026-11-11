---
name: od-prototype-poc
description: >-
  Prove a new use case cheaply before the business case: choose click-dummy, proof of concept or neither, and record the result. Not for costing value (od-benefit-calculation) or dashboards.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-prototype-poc
  tier: practice
  lane: lane-2
  new_state_lane: "Lane 2 (23)"
  new_state_step: "Prototype / click-dummy, validated with the recipient"
  department_names: ["funnel-prototype", "prototype-builder", "click-dummy"]
  owner_role: human:jakob.gabriel
  author: human:jakob.gabriel
  tags: [use-case-support-service, practice, new-state, draft]
  authority_level: draft the prototype and the validation record; the plant confirms the value
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-use-case-definition, od-requirements-breakdown, od-data-availability-check, od-analytics-asset-build, od-benefit-calculation, od-capital-request, od-acceptance-test, od-decision-routing, od-handover-and-adoption]
  derived_from:
    - "Department knowledge base (skills/click-dummy/SKILL.md, references/build-patterns.md), read 2026-11-10"
    - The new-state flow (docs/new-state-flow.md, docs/new-state-conformance.md and the skill-map table docs/new-state/OD_NewState_VSM_SkillMap.html), Lane 2 step 3 and the gap register, read 2026-11-05
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/AI_Where_We_Apply_Today.pptx
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/AI_Board_TwoPager.pptx
    - Department knowledge base, Gemba App project folder (README, quick_start_guide, click_dummy_template_prompt, example_production_dashboard_spec), the Claude project export that holds the click-dummy prompt system, read 2026-11-05
    - Department archive (read-only), 13-AI_Activities/2026-08-AI_Initiatives_Pitch/04-AI based Requirements Engineering Mockup Creation, the Gemba App initiative deck, read 2026-11-05
    - Department knowledge base Cases, the validation plan and MVP scope of 29 AI business cases and the note AI Requirements Engineering Pipeline, read 2026-11-05
    - Department knowledge base SPEC-00 and SPEC-03 and the Hannover Stoecken KKA and Pulp Mixer requirements and summary, and Graph/Use Case Views Dashboard Use Cases Overview and Andon Board, read 2026-11-05
    - Skills od-analytics-asset-build, od-use-case-definition, od-requirements-breakdown, od-benefit-calculation and od-decision-routing, read 2026-11-05
  okf:
    type: Agent Skill
    title: Prototype and proof of concept
    tags: [use-case-support-service, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Prototype and proof of concept

Read `od-context` first.

**Status: draft.** The new-state flow lists "Prototype / validate" (Lane 2, step 3) as a thin spot. It credits
`od-analytics-asset-build` with "click-dummy only", but that skill has no prototype, click-dummy or
proof-of-concept content (`docs/new-state-conformance.md`). This skill is grounded in what the knowledge base actually
holds: one AI pilot (the Gemba App), PoC labels in two AI decks, business cases that each carry a
validation plan, and the dashboard specs. It is **not** a validated OD method: nothing in the sources says
OD has run this step to a stated standard.

## Purpose

Use this skill when a defined Lane 2 use case has an open question about usability or about whether the data or
model works, and that question is cheaper to answer with a mock-up or a narrow proof of concept than with a
build. It returns a validation record that feeds the business case, never a claim of proven value.

## Inputs and output

- **In:** a defined use case, requirements with acceptance criteria, a data verdict that is not "dies at step N".
- **Out:** a filled [`assets/prototype-validation-record.md`](assets/prototype-validation-record.md) and, for a
  click-dummy, the mock-up and its handover note.

Short example of the record's shape (fictional example; the use case and the values are invented):

```text
Question:   Will the shift supervisor read the downtime view at the Gemba? (usability)
Type:       click-dummy
Criterion:  written before the build; 3 of 4 supervisors finish the task unaided within one shift check
Validator:  plant ME (role)
Result:     passed | failed | inconclusive
Label:      mock-up (not PoC, not pilot, not "proven")
Open items: data for the second view not yet checked
```

If the inputs are missing or the criterion is not written first, treat the result as invalid and return to step 1 of the procedure.

## Pilot, PoC and rollout are three different claims

State which one you mean, every time. The department's own AI decks use these labels
([`references/status-labels.md`](references/status-labels.md)).

| Label | What it claims | What it does not claim |
|---|---|---|
| **Click-dummy / mock-up** | A user can see and react to the idea. No real data, no backend | That the data exists, that it works, that anyone will use it |
| **PoC** (proof of concept) | The technical idea works on real data in a narrow case | Value in euros, plant adoption, repeatability |
| **Pilot** | It runs with real users in one place for a time-boxed period | That it scales; that the saving is real |
| **Rollout** | It is deployed and used at more than the pilot site | Proven value: that is only SPRINT (`od-benefit-calculation`) |

The strategy material works with four working stages - PoC, prototype, pilot, rollout - where the PoC validates feasibility, the prototype the benefit with real users and the pilot
validates operational scalability ([`references/process-chain-practice.md`](references/process-chain-practice.md)). A prototype outside the
standard needs a path to the reference architecture. A pilot or PoC result is evidence for the business case. It is never "proven". The two AI decks even disagree
on the same items; quote the label with its deck and date.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/status-labels.md`](references/status-labels.md) | The label ladder the decks use, how labels mislead (disagreement between decks, "rollout" is not proven value), and the rule for quoting one |
| [`references/gemba-app-pilot.md`](references/gemba-app-pilot.md) | The Gemba App requirements-to-mockup pilot as a method: process, click-dummy prompt system, what to copy, what the sources do not show |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | **How the step runs in the chain**: the PoC, prototype, pilot, rollout stages, scope-limiting as a gate strategy, AI-assisted mock-ups, handoff contract, AI agent operating notes |
| [`references/validation-patterns.md`](references/validation-patterns.md) | How the AI business cases define a validation plan and pass criterion; wording patterns to copy (placeholder thresholds) |
| [`references/click-dummy.md`](references/click-dummy.md), [`references/build-patterns.md`](references/build-patterns.md) | The department package's click-dummy stage (`funnel-prototype`, master): eight stages, verification, fidelity ledger, handover; layout, navigation, states and data-stub patterns |
| [`assets/click-dummy-brief.md`](assets/click-dummy-brief.md) | The brief to write before anyone builds a mock-up |
| [`assets/prototype-validation-record.md`](assets/prototype-validation-record.md) | The record this skill produces; `od-benefit-calculation` and `od-capital-request` read it next |

## Where it sits

Lane 2 runs definition, features and data check, **prototype / validate**, business case, capital request,
implement and graduate (`docs/new-state-flow.md`). This step comes after `od-use-case-definition`,
`od-requirements-breakdown` and `od-data-availability-check`, and before `od-benefit-calculation`. The flow
marks it as touched by both human and agent: an agent can draft the mock-up and the record, the plant says
whether it shows what they need.

## Procedure

1. **Check the inputs exist.** A defined use case (`od-use-case-definition`), requirements with acceptance
   criteria (`od-requirements-breakdown`), and a data verdict (`od-data-availability-check`). If the data
   verdict is "dies at step N", stop: a prototype on missing data proves nothing.
2. **Check the library first.** If a proven reference solution already answers the need
   (`od-use-case-standardization`), adopt it and skip the prototype (`od-analytics-asset-build`, "when not to build").
3. **Name the open question.** One sentence, in the plant's words: "will the shift supervisor read this at
   the Gemba?" is a usability question, "does the signal separate good from bad?" is a data question,
   "is the saving big enough?" is a value question. A prototype answers the first two only.
4. **Pick the type.** Usability or scope question -> click-dummy. Data or model question -> PoC on real
   data. Both -> click-dummy first, PoC only if the plant wants it. Neither -> no prototype; say why.
5. **Write the pass criterion before building**, with a number, a scope, a time box and a named validator
   ([`references/validation-patterns.md`](references/validation-patterns.md)). Without a criterion there is no
   validation, only a demo.
6. **Brief and build.** For a click-dummy run the department's click-dummy stage
   ([`references/click-dummy.md`](references/click-dummy.md), the master): scope from the feature book, pick the
   shape, define done before building, state and data first, shell first then sections, verify in a real browser
   (can the user do the job, does the demo make the case), keep a fidelity ledger, write the handover document.
   Build patterns in [`references/build-patterns.md`](references/build-patterns.md). Fill
   [`assets/click-dummy-brief.md`](assets/click-dummy-brief.md) first; the
   Gemba App pilot generated mock-ups from a written brief with an AI model, and a human reviewed them
   ([`references/gemba-app-pilot.md`](references/gemba-app-pilot.md)). For a dashboard-type asset, the build
   mechanics stay in `od-analytics-asset-build` and `build-grafana-ops-dashboard`: do not rebuild them here.
7. **Show it to the people who will use it**, in the plant, at the moment of use (the Gemba, the shift
   check). Record what they said and what they did, not only what they liked.
8. **Judge against the criterion** and write the result in
   [`assets/prototype-validation-record.md`](assets/prototype-validation-record.md): passed, failed, or
   inconclusive. A failed prototype is a valid, cheap result: record it and stop or re-scope.
9. **Hand on.** Passed: the record goes to `od-benefit-calculation` as evidence for the rows (it does not
   replace the methodology field) and to `od-capital-request` if money is needed. Failed: back to
   `od-use-case-definition` or close the use case. Acceptance of a later build stays with
   `od-acceptance-test`.

## Human gate and AI-agent notes

- **Agent may:** check the inputs, propose the open question and the prototype type, draft the brief, the
  mock-up and the validation record, and quote labels with deck and date.
- **Only roles decide:** the plant representative confirms or declines the value; the OD lead decides any time box,
  budget or sign-off rule; the responsible human releases a mock-up outside the department.

## Definition of done

A validation record exists with: the question, the type, the criterion written before the build, the
validator (a role), the result, the status label (mock-up, PoC or pilot) and the open items. The plant
representative has confirmed or declined the value in writing. Nothing in it says "proven".

## What is still open

- ⟨Whether OD has a standard prototype time box, budget or sign-off rule⟩: not in any source. OD lead.
- ⟨Where finished mock-ups are stored and who can open them⟩: not stated. OD lead.
- ⟨Whether the Gemba App pilot reached a result⟩: the knowledge base holds the brief and the initiative request, not an
  outcome ([`references/gemba-app-pilot.md`](references/gemba-app-pilot.md)). Gemba App initiative owner.
- ⟨Touch time and queue time of this step⟩: placeholders in the skill-map table. OD data.
- Whether the click-dummy stack in the Gemba App export (React with Tailwind) fits the department's small
  footprint rule, or the Mendix low-code route named in the initiative deck, is undecided. OD lead with IT.

## Do not

- Do not call a pilot or PoC "proven", or put a euro figure on a mock-up. Value goes through `od-benefit-calculation`.
- Do not prototype on data that `od-data-availability-check` says is not there.
- Do not build a prototype without a written pass criterion and a named plant validator.
- Do not use real plant data, credentials or personal data in a mock-up; mock-ups carry invented example values, marked as such.
- Do not add a tool: the strategy is a small operational footprint (`od-analytics-asset-build`).
- Do not publish a mock-up outside the department without the responsible human.
