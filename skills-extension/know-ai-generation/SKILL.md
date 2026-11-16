---
name: know-ai-generation
description: >-
  Answers "what may an AI agent do at this step, and who must sign?" along the OD process chain.
  Use before an agent drafts, classifies, generates or checks something in a lane, when someone
  proposes an AI assistant, agent, generated dashboard or AI-built app, when signals or a dashboard
  are to be generated from a tag list, or when a generated output needs citations and a human
  review. Sets the safe pattern (fixed-structure input, reviewable output, evidence trail, human
  gate), the missing-signal table and the list of decisions that stay human. Not for what to build
  (ops-analytics-asset), signal naming (mi-signals) or Cyber Security sign-off (deploy-cybersec).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: know-ai-generation
  aliases: [od-ai-generation-playbook]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Spine"
  new_state_step: "Supporting spine"
  owner_role: human:jakob.gabriel
  authority_level: recommend - drafts and checks only; every gate named here is a human gate
  status: draft
  origin: plan-draft
  requires: [dept-context]
  composes: [dept-context-freshness, ops-analytics-asset, mi-signals, funnel-prototype, deploy-cybersec, deploy-appstore, mi-data-availability, invest-screen, catalog-template, deploy-handover]
  okf:
    type: Agent Skill
    title: AI generation playbook
    tags: [all, practice, new-state, draft, ai]
---

# AI generation playbook

## Purpose

- Read `dept-context` first. This skill adds no new service.
- It is the one rulebook for the places in the chain where an AI agent drafts, classifies, generates or checks something.
- Every step uses the same safe pattern: **fixed-structure inputs, a reviewable or importable output, a named evidence trail, a human gate before anything leaves the team.** Reason: a generated output nobody can trace or check is read as fact.
- Everything below is process guidance from the decks. Rules that are this skill's own synthesis are marked `PROPOSAL`; unknowns are `<to confirm>`. The owner has not confirmed the `PROPOSAL` rules.
- Terms used throughout: **output** is anything the agent generates; **open item** is anything marked `<to confirm>`.

## Inputs and output

- **Inputs:** the fixed-structure input set of the step (tag list, requirements text, template, request) plus the relevant, current context section.
- **Output:** the step card [`assets/ai-step-card.md`](assets/ai-step-card.md), the output with its evidence table, the open-item list and, for signal and dashboard steps, the missing-signal and binding table.
- [`outputs.yaml`](outputs.yaml) lists required outputs, criteria, checks and sign-offs.

## Where it sits in the chain

| Step id | Where the agent helps | Rule / reference |
|---|---|---|
| spine | Keep the context layer current; reject stale sources | R1; `dept-context-freshness` |
| i1 | Classify an incoming request, pre-fill the intake | R6; `ai-governance` |
| 21 | Draft the one-pager, rewrite the request, pre-fill the canvas | R2, R5 |
| 22 | Signal selection from a datapoint export | R3, R4; `generation-pipeline` section 2 |
| 23 | Dashboard config, click-dummy, guided ML analyser | R3, R4; `generation-pipeline` sections 3-4 |
| 24 | Draft calculation rows, flag missing inputs | R2, R5 (ranking sign-off is human) |
| 25 | Assemble scenario tables, completeness check on the request | R2, R5 |
| 26 | Monitor utilisation, draft the savings evaluation | R2, R5 |
| 1a2 | Apply a template to a connected machine with the same pattern as step 23 | R3 |
| 31, 32 | Fit check against AI platform criteria; GenAI and agent proposals | R8, R9 |
| 3a4-3a6 | Deployment set from a template; AI-built app intake | R10; `deploy-appstore`, `deploy-cybersec` |
| 3b4-3b6 | Tag-selection list, flow documentation, cyber-security package draft | R3, R6 |

## Procedure

- Run these stages for any template-bound output (document, deck, dashboard config); detail in the `generation-pipeline` reference.

1. **Admit the step.** Fill section 1 of the step card. No named process owner, data source and review point: stop, no start (R9).
2. **Read the context by relevance** (R1). A stale or ownerless section stops the run; report it, never fill the gap from memory.
3. **Read the template** from the approved master via `catalog-template`, never a copy.
4. **Ask the human** for what the context cannot derive: lane, depth, language, audience, ranking (R5). Do not guess.
5. **Map fields to template elements, one source per element** (R2, R3). An element without a source stays empty.
6. **Report missing signals first** (R4), then build the output and the binding table.
7. **Visual-QA loop:** render, inspect against the checklist, fix, render again. Stop only on a clean render and a clean placeholder-leak check.
8. **Deliver editable** with evidence (R7), the open-item list and the card; a person reviews before the output leaves the team.

### Visual-QA loop checklist

- [ ] No overflow, clipped text or invisible text; contrast readable.
- [ ] Units on every number; no leftover `<...>` placeholder in the visible output.
- [ ] Every element has a source field; every open item is on the list, not in the output.
- [ ] If the agent cannot render the output, it says so and does not claim the check was done.

### Example: dashboard generation

```text
AI step card - 23 Dashboard config - Plant X, press line P-7 (fictional)
Admission: owner = process engineer (role); source = datapoint export, read 2026-03-02; review = domain expert on the running dashboard
Task:      draft dashboard config from tag list + requirements text
Missing signals (reported first):
  S-104 | Coolant temp | requirement R3 "alarm above limit" -> information-integration lane, not approximated
Binding table:
  R1 cycle time | tag T-211 "Press1.CycleTime" | rule: label suffix scoped to device | trend | panel 2 | seconds
Open items: scaling of T-340 unknown <to confirm> - process engineer
Label: draft. Visual QA: done. Placeholder leak check: done.
Gate: expert verdict on the running dashboard - pending. Not done on purpose: nothing connected, written or approved.
```

## The rules

| Rule | Statement and reason |
|---|---|
| R1 Context layer first (spine) | An agent works only on a current, structured description: one named person per section, review date, fields instead of prose, missing values open. Stale or ownerless: stop and report (`dept-context-freshness`). Read by relevance, not all of it. Reason: an agent fills gaps from memory. |
| R2 Honesty rule (all steps) | Every element of a generated output traces to a source field. Open items stay out of the output, on a separate list. The `dept-context` honesty rules apply: tracked is not proven, absence is not zero, no figure without a source. |
| R3 Fixed-structure inputs, importable output (22, 23, 1a2, 3b4) | Name the input set before starting; for a dashboard: tag list (labels), requirements text, optionally a reference dashboard. Time-series values are not needed. Return the output and a binding table. Reason: a fixed structure can be imported and tested. |
| R4 Missing-signal table up front (22, 23) | Report first, as `signal id / label / why needed`, everything the requirements need that is not collecting; it goes to the information-integration lane. Never approximate by a similar signal: the dashboard would look right and be wrong. `mi-data-availability` still decides. The expert validates on the running dashboard, not a spreadsheet. |
| R5 Human gate before the audience (all deliverables) | Ask a human for choices the context cannot derive (lane, depth, language, ranking). A person reviews before anyone outside the team sees the output, closes open items, confirms cited figures are current. Reason: the agent cannot know what is still true. |
| R6 Advice versus change (i1, 23, 3b4) | An agent may advise, classify or propose. A machine parameter change, PLC write or process-acting configuration is a human or process-engineer action. External connections go through `deploy-cybersec`. Cyber Security sign-off blocks only go-live, not planning or build: start the package early. |
| R7 Evidence the agent must cite | Per step: the source rows, entries or documents the output rests on, with read date (`evidence-and-human-decisions`). An output without citations is labelled a draft. |
| R8 Fit check for AI platforms (31, 32) | Criteria seen in the decks: governed model operations with audit trail, no company data used for model training, single-sourcing rule of purchasing, cyber-security baseline. A tool failing one is not scaled until closed; the verdict is `invest-screen`'s and human. Reason: company data would leave control. |
| R9 Time-boxed pilots, named owner (31, 32, 23) | GenAI proofs of concept and agentic workflows run time-boxed with a named process owner, data source and review point. Any of the three missing: no start (`ai-governance`). Reason: unowned pilots never end. |
| R10 AI-built apps take the normal road (3a4-3a6) | A prompt-to-prototype shows value fast; it is not a deployment. Generated solutions go through IT takeover and Cyber Security approval; supplier code is assumed partly AI-generated. |

## Human gate and AI-agent notes

- **Stays human** (full list in `evidence-and-human-decisions`): accepting a requirement or problem statement; the domain-expert verdict on a generated dashboard; any ranking or go / no-go; assumptions and baselines of a benefit; scope and scenario of a decision.
- **Also human:** anything that commits budget or a connection; Cyber Security sign-off; deployment into a shared platform; promotion to the catalog; confirming a savings status.
- **Allowed:** draft, pre-fill, classify, extract, summarise, check completeness, monitor, document.
- **Start condition (`PROPOSAL` as a chain rule):** a human has named the process owner, the data source and the review point. No name, no start.
- **Never:** invent a value, hide an open item, approximate a missing signal, write to a machine, approve or submit anything, or present a generated figure as proven.

## Pitfalls

- **Approximated signal:** the missing-signal table is empty although the requirements mention signals not in the export. Compare requirements against the export before matching.
- **Open items filled quietly:** search the output for values with no source field.
- **First delivery treated as final:** requirements change; schedule an explicit iteration after first delivery.
- **Prototype read as value:** a click-dummy or generated dashboard is not proven value (`funnel-prototype` status labels).
- **Fast build, skipped gates:** a quickly generated app still needs IT takeover and Cyber Security approval.
- **Unfit tool:** do not use company data with a tool that fails the R8 criteria.
- **Wrong priority:** do not rank AI use cases above basic data-model and reporting work in a plant that has not reached reporting.
- **Dashboard without action owner:** a build smell (`ops-analytics-asset`); name the moment of use before the build.

## Still open

- An AI knowledge or troubleshooting assistant is decided case by case at intake: ask for a measurable before/after.
- With a measurable it goes the use-case route (savings only with documented basis); without one it is tracked as an initiative with a named owner and a usage measure, not as a counted saving.
- `<to confirm>` Whether general-purpose assistants are low impact (one deck) or already useful for deployment sets (another). Safer reading: allowed as a drafting aid, never as a gate.
- `<to confirm>` Time-box lengths, accuracy thresholds and the champion-user group for pilots: not in the sources.

## Definition of done

- The step card is filled and a human has named the owner, data source and review point.
- Every output element traces to a source with read date, or the output is labelled a draft.
- Open items are on the list, missing signals are reported first, and the visual-QA loop ended clean (or "not possible" is stated).
- The human gate is named with its holder and outcome; nothing was connected, written, approved or submitted.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/generation-pipeline.md`](references/generation-pipeline.md) | You run the seven-stage pipeline, select signals, or generate a dashboard, click-dummy, analyser or deployment set |
| [`references/ai-governance.md`](references/ai-governance.md) | Someone proposes a GenAI proof of concept, an agentic workflow, an AI-built app or an assistant |
| [`references/evidence-and-human-decisions.md`](references/evidence-and-human-decisions.md) | You need the citation rule for a step or the full human-decision list |
| [`references/ai-initiative-maturity-ladder.md`](references/ai-initiative-maturity-ladder.md) | An AI initiative claims savings or value and its evidence level must be placed (idea to proven) |
| [`assets/ai-step-card.md`](assets/ai-step-card.md) | You admit an agent step and record evidence and gate |
| [`assets/missing-signal-and-binding-table.md`](assets/missing-signal-and-binding-table.md) | A signal or dashboard step starts: missing-signal and binding tables |
| [`references/background.md`](references/background.md) | You need context and rationale; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
| [`references/outputs.md`](references/outputs.md) | The output contract in full (generated from outputs.yaml) |

## Neighbours

- `dept-context` (honesty rules), `dept-context-freshness` (stale sources), `ops-analytics-asset` (what to build, ritual of use), `mi-signals` (naming and data model).
- `funnel-prototype` (four stages: PoC for feasibility, prototype for benefit with real users, pilot, rollout; each is its own claim), `deploy-cybersec` (sign-off package), `deploy-appstore` (deployment package and release gate).
