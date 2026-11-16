---
name: funnel-prototype
description: >-
  Prove a new use case cheaply before the business case: choose click-dummy (mock-up), proof of concept (PoC) or no prototype, write the pass criterion first, show it to the plant users and record the result in a validation record, never as "proven". Use when a defined Lane 2 use case has an open question such as "will the shift read this", "does the data separate good from bad" or "can we run a pilot", when someone asks for a mock-up, click-dummy, PoC or quick test with the plant. Drafts only; the plant confirms the value. Not for costing value (bc-build), the capital request (bc-capital-request), dashboard build (ops-dashboard-engine) or the requirement (funnel-requirements).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: funnel-prototype
  aliases: [od-prototype-poc, click-dummy]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: lane-2
  new_state_lane: "Lane 2 (23)"
  new_state_step: "Prototype / click-dummy, validated with the recipient"
  department_names: ["funnel-prototype", "prototype-builder", "click-dummy"]
  owner_role: human:jakob.gabriel
  tags: [use-case-support-service, practice, new-state, ready]
  authority_level: draft the prototype and the validation record; the plant confirms the value
  status: ready
  requires: [dept-context]
  composes: [funnel-use-case, funnel-requirements, mi-data-availability, ops-analytics-asset, ops-dashboard-engine, bc-build, bc-capital-request, deploy-acceptance, dept-decision-rights, deploy-handover]
  okf:
    type: Agent Skill
    title: Prototype and proof of concept
    tags: [use-case-support-service, practice, new-state, ready]
---

# Prototype and proof of concept

- Read `dept-context` first.

- Status is ready (awaiting sign-off) and this is not a validated OD method: nothing in the sources says OD has run this step to a stated standard.
- Provenance, what rests on the single Gemba App pilot and what is inference: `references/background.md`.

## Purpose

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- Use this skill when a defined Lane 2 use case has an open question about usability or about whether the data or model works,
- and that question is cheaper to answer with a mock-up or a narrow proof of concept than with a build.
- It returns a validation record that feeds the business case, never a claim of proven value.

## Inputs and output

- **In:** a defined use case, requirements with acceptance criteria, a data verdict that is not "dies at step N".
- **Out:** a filled [`assets/prototype-validation-record.md`](assets/prototype-validation-record.md) and, for a
  click-dummy, the mock-up and its handover note.

- Short example of the record's shape (fictional example; the use case and the values are invented):

```text
Question:   Will the shift supervisor read the downtime view at the Gemba? (usability)
Type:       click-dummy
Criterion:  written before the build; 3 of 4 supervisors finish the task unaided within one shift check
Validator:  plant ME (role)
Result:     passed | failed | inconclusive
Label:      mock-up (not PoC, not pilot, not "proven")
Open items: data for the second view not yet checked
```

- If the inputs are missing or the criterion is not written first, treat the result as invalid and return to step 1 of the procedure.

## Terms used in this skill

| Term | Meaning here |
|---|---|
| Prototype | Umbrella word for any early version built to answer one open question |
| Click-dummy (also mock-up) | Prototype without real data or backend; answers usability and scope questions |
| PoC | Prototype on real data in a narrow case; answers data or model questions |
| Four-stage ladder | PoC, prototype, pilot, rollout (strategy material): a PoC maps to the PoC label, a click-dummy to the mock-up label, then pilot and rollout |

## Pilot, PoC and rollout are three different claims

- State which one you mean, every time.
- The department's own AI decks use these labels ([`references/status-labels.md`](references/status-labels.md)).

| Label | What it claims | What it does not claim |
|---|---|---|
| **Click-dummy / mock-up** | A user can see and react to the idea. No real data, no backend | That the data exists, that it works, that anyone will use it |
| **PoC** (proof of concept) | The technical idea works on real data in a narrow case | Value in euros, plant adoption, repeatability |
| **Pilot** | It runs with real users in one place for a time-boxed period | That it scales; that the saving is real |
| **Rollout** | It is deployed and used at more than the pilot site | Proven value: that is only SPRINT (`bc-build`) |

- The ladder: PoC validates feasibility, the prototype the benefit with real users, the pilot operational scalability ([`references/process-chain-practice.md`](references/process-chain-practice.md)).
- A prototype outside the standard needs a path to the reference architecture.
- A pilot or PoC result is evidence for the business case, never "proven", because value is only proven by the savings process (`bc-build`).
- The two AI decks disagree on the same items; quote the label with its deck and date.

## References

| File | Open when |
|---|---|
| [`references/status-labels.md`](references/status-labels.md) | You must quote a label (PoC, pilot, rollout) and need to know how labels mislead |
| [`references/gemba-app-pilot.md`](references/gemba-app-pilot.md) | You build a mock-up with an AI model from a written brief and want the one known pilot as a method |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | You need the stages, scope-limiting as a gate strategy, the handoff contract or agent notes |
| [`references/validation-patterns.md`](references/validation-patterns.md) | You write the pass criterion (step 5) and need wording patterns |
| [`references/click-dummy.md`](references/click-dummy.md) | The type is click-dummy: the eight build stages, verification, fidelity ledger, handover |
| [`references/build-patterns.md`](references/build-patterns.md) | You are in the build stage: layout, navigation, states, data stubs, verification script |
| [`references/background.md`](references/background.md) | You need status, provenance or the output table; never an instruction |
| [`assets/click-dummy-brief.md`](assets/click-dummy-brief.md) | Before anyone builds a mock-up |
| [`assets/prototype-validation-record.md`](assets/prototype-validation-record.md) | You write the result; `bc-build` and `bc-capital-request` read it next |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |

## Procedure

- Copy this checklist and tick it off:

```text
[ ] 1 Inputs exist (use case, requirements, data verdict)
[ ] 2 Library checked, no proven solution
[ ] 3 Open question named in the plant's words
[ ] 4 Type picked: click-dummy, PoC or none
[ ] 5 Pass criterion written BEFORE building
[ ] 6 Brief filled, mock-up or PoC built
[ ] 7 Shown to the plant users at the moment of use
[ ] 8 Result judged, record written
[ ] 9 Handed on or stopped
```

1. **Check the inputs exist.** A defined use case (`funnel-use-case`), requirements with acceptance
   criteria (`funnel-requirements`), and a data verdict (`mi-data-availability`). If the data
   verdict is "dies at step N", stop: a prototype on missing data proves nothing.
2. **Check the library first.** If a proven reference solution already answers the need
   (`catalog-standardization`), adopt it and skip the prototype (`ops-analytics-asset`, "when not to build").
3. **Name the open question.** One sentence, in the plant's words:
   - "will the shift supervisor read this at the Gemba?" is a usability question, "does the signal separate good from bad?" is a data question, "is the saving big enough?" is a value question.
   - A prototype answers the first two only.
4. **Pick the type.** Usability or scope question -> click-dummy. Data or model question -> PoC on real
   data. Both -> click-dummy first, PoC only if the plant wants it. Neither -> no prototype; say why.
5. **Write the pass criterion before building**, with a number, a scope, a time box and a named validator
   ([`references/validation-patterns.md`](references/validation-patterns.md)). Without a criterion there is no
   validation, only a demo.
6. **Brief and build.** For a click-dummy run the department's click-dummy stage ([`references/click-dummy.md`](references/click-dummy.md), the master):
   - scope from the feature book, pick the shape, define done before building, state and data first, shell first then sections, verify in a real browser (can the user do the job, does the demo make the case),
   - keep a fidelity ledger, write the handover document.
   - Build patterns in [`references/build-patterns.md`](references/build-patterns.md).
   - Fill [`assets/click-dummy-brief.md`](assets/click-dummy-brief.md) first; the Gemba App pilot generated mock-ups from a written brief with an AI model, and a human reviewed them ([`references/gemba-app-pilot.md`](references/gemba-app-pilot.md)).
   - For a dashboard-type asset, the build mechanics stay in `ops-analytics-asset` and `ops-dashboard-engine`: do not rebuild them here.
7. **Show it to the people who will use it**, in the plant, at the moment of use (the Gemba, the shift
   check). Record what they said and what they did, not only what they liked.
8. **Judge against the criterion** and write the result in
   [`assets/prototype-validation-record.md`](assets/prototype-validation-record.md): passed, failed, or
   inconclusive. A failed prototype is a valid, cheap result: record it and stop or re-scope.
9. **Hand on.** Passed: the record goes to `bc-build` as evidence for the rows (it does not replace the methodology field) and to `bc-capital-request` if money is needed.
   - Failed: back to `funnel-use-case` or close the use case.
   - Acceptance of a later build stays with `deploy-acceptance`.

## Human gate and AI-agent notes

- **Agent may:** check the inputs, propose the open question and the prototype type, draft the brief, the
  mock-up and the validation record, and quote labels with deck and date.
- **Only roles decide:** the plant representative confirms or declines the value; the OD lead decides any time box,
  budget or sign-off rule; the responsible human releases a mock-up outside the department.

## Definition of done

- A validation record exists with: the question, the type, the criterion written before the build, the validator (a role), the result, the status label (mock-up, PoC or pilot) and the open items.
- The plant representative has confirmed or declined the value in writing.
- Nothing in it says "proven".

## Do not

- Do not call a pilot or PoC "proven", or put a euro figure on a mock-up, because a demo cannot show value. Value goes through `bc-build`.
- Do not prototype on data that `mi-data-availability` says is not there, because the result would prove nothing.
- Do not build without a written pass criterion and a named plant validator, because without them any result can be read as success.
- Do not use real plant data, credentials or personal data in a mock-up, because mock-ups get shown and forwarded; use invented values marked as such.
- Do not add a tool, because the strategy is a small operational footprint (`ops-analytics-asset`).
- Do not publish a mock-up outside the department without the responsible human.
- Do not let the plant validate by saying "looks good" only: record what they did, because liking is not use.
- Do not build a PoC when the open question is a value question; it cannot be answered by a prototype.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).
