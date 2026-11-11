---
name: od-ai-generation-playbook
description: >-
  The cross-cutting rulebook for using AI agents safely along the OD process chain - the department
  context layer as precondition, the multi-step generation pipeline with its human gate and visual-QA
  loop, AI signal selection and dashboard generation from fixed-structure inputs (missing-signal table
  up front, expert validation on the running dashboard), GenAI proof-of-concept and agentic-workflow
  governance, the intake path for AI-built apps, evidence and citation rules, and the list of decisions
  that stay human. Names the process step where each rule applies. Use before an agent drafts, generates
  or checks anything in a lane, when someone proposes an AI assistant, agent or generated app, or when
  asked what an AI agent may do at a step and who must sign.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-ai-generation-playbook
  tier: practice
  lane: all
  new_state_lane: "Spine"
  new_state_step: "Supporting spine"
  owner_role: human:jakob.gabriel
  authority_level: recommend - drafts and checks only; every gate named here is a human gate
  status: draft
  origin: plan-draft
  requires: [od-context]
  composes: [od-context-freshness, od-analytics-asset-build, od-signal-standardization, od-prototype-poc, od-cybersec-gate, deploy-appstore, od-data-availability-check, od-system-fit-check, od-template-resolution, od-handover-and-adoption]
  okf:
    type: Agent Skill
    title: AI generation playbook
    tags: [all, practice, new-state, draft, ai]
---

# AI generation playbook

Read `od-context` first. This skill adds no new service. It is the one rulebook for the places in the
chain where an AI agent drafts, classifies, generates or checks something, so that every step uses the
same safe pattern: **fixed-structure inputs, an importable or reviewable output, a named evidence trail,
a human gate before anything leaves the team.**

Everything below is process guidance from the decks. Where a rule is this skill's own synthesis it is
marked `PROPOSAL`; unknowns are `<...>`. The owner has not confirmed the `PROPOSAL` rules.

## Where it sits in the chain

| Step id | Where the agent helps | Rule / reference |
|---|---|---|
| spine | Keep the context layer current; reject stale sources | R1; `od-context-freshness` |
| i1 | Classify an incoming request, pre-fill the intake | R6; [`ai-governance`](references/ai-governance.md) |
| 21 | Draft the one-pager, rewrite the request, pre-fill the canvas | R2, R5 |
| 22 | Signal selection from a datapoint export | R3, R4; [`generation-pipeline`](references/generation-pipeline.md) section 2 |
| 23 | Dashboard config, click-dummy, guided ML analyser | R3, R4; `generation-pipeline` sections 3-4 |
| 24 | Draft calculation rows, flag missing inputs | R2, R5 (ranking sign-off is human) |
| 25 | Assemble scenario tables, completeness check on the request | R2, R5 |
| 26 | Monitor utilisation, draft the savings evaluation | R2, R5 |
| 1a2 | Apply a template to a connected machine with the same pattern as step 23 | R3 |
| 31, 32 | Fit check against AI platform criteria; GenAI and agent proposals | R8, R9 |
| 3a4-3a6 | Deployment set from a template; AI-built app intake | R10; `deploy-appstore`, `od-cybersec-gate` |
| 3b4-3b6 | Tag-selection list, flow documentation, cyber-security package draft | R3, R6 |

## The rules

**R1 - Context layer first (spine; precondition for every step).** An agent works only on a department
description that is current and structured: one named person per section, a review date that flags stale
sections, fields instead of prose (trigger, owner, source, threshold), missing values marked open. If the
section an agent needs is stale or has no owner, it stops and reports that (`od-context-freshness`) and
does not fill the gap from memory. Read the context by relevance, not all of it.

**R2 - Honesty rule for generated output (all steps).** Every element of a generated artefact traces to a
source field. Open items ("to confirm") stay out of the artefact and go on a separate open-item list.
The `od-context` honesty rules apply to every figure: tracked is not proven, absence is not zero, no
figure without a nameable source.

**R3 - Fixed-structure inputs, importable output (steps 22, 23, 1a2, 3b4).** Generation is safest when the
input has a fixed structure and the output is a config that can be imported and tested. Name the input
set before starting; for a dashboard: a tag list (labels), a requirements text, optionally a reference
dashboard. Time-series values are not needed to generate. The agent returns the output **and** a binding
table (which tag fed which panel, which query pattern a panel uses).

**R4 - Missing-signal table up front (steps 22, 23).** Anything the requirements need that is not yet
collecting is reported first, before the dashboard, as `signal id | label | why needed`. It goes to the
information-integration lane and is never approximated by a similar signal. The verdict of
`od-data-availability-check` still decides. The expert validates the proposal on the **running
dashboard**, not on a spreadsheet.

**R5 - Human gate before the audience (all steps that produce a deliverable).** Choices the context cannot
derive are asked of a human (for example lane, depth, language, or a ranking); the agent never fills
them by guess. A person reviews the output before anyone outside the team sees it, closes the open items
and confirms that cited figures are still current.

**R6 - Advice versus change (i1, 23, 3b4).** An agent may advise, classify or propose. A parameter change
on a machine, a PLC write or a configuration that acts on a process is a human or process-engineer
action; external connections go through `od-cybersec-gate`. The Cyber Security sign-off runs in parallel
with planning and build and blocks only go-live (the live connection or live operation), not planning,
build or the preparation of an integration wave: start the package early.

**R7 - Evidence the agent must cite.** Per step, the source rows, list entries, library entries or
documents the output rests on, with the read date
([`evidence-and-human-decisions`](references/evidence-and-human-decisions.md)). An output without citations
is a draft and is labelled so.

**R8 - Fit check for AI platforms and tools (31, 32).** Criteria seen in the decks are governed model
operations with audit trails, no company data used for model training, alignment with the single-sourcing
rule of purchasing, the cyber-security baseline. A tool failing one is not scaled until the gap is closed;
the verdict is `od-system-fit-check`'s and human.

**R9 - Time-boxed pilots and a named owner (31, 32, 23).** GenAI proofs of concept and agentic workflows
run time-boxed, with a named process owner, a named data source and a named review point; with any of the
three missing, no start ([`ai-governance`](references/ai-governance.md)).

**R10 - AI-built apps take the normal road (3a4-3a6).** A prompt-to-prototype shows value fast; it is not
a deployment. Generated solutions go through IT takeover and Cyber Security approval like any app, and
supplier code is assumed to be partly AI-generated (`ai-governance`).

## What stays a human decision

Full list in [`evidence-and-human-decisions`](references/evidence-and-human-decisions.md). In short:
accepting a requirement or problem statement; the domain-expert verdict on a generated dashboard; any
ranking or go / no-go; assumptions and baselines of a benefit; scope and scenario of a decision; anything
that commits budget or a connection; Cyber Security sign-off; deployment into a shared platform;
promotion to the catalog; confirming a savings status.

## AI agent operating notes

- **Allowed:** draft, pre-fill, classify, extract, summarise, check completeness, monitor, document.
- **Start condition (`PROPOSAL` as a chain rule):** a human has named the process owner, the data source
  and the review point. No name, no start.
- **Inputs:** the fixed-structure input set of the step plus the relevant context section; take the
  template from `od-template-resolution`, never from a copy.
- **Hand over with:** the output, the binding or evidence table, the open-item list and the
  missing-input table, on the step card [`assets/ai-step-card.md`](assets/ai-step-card.md).
- **Never:** invent a value, hide an open item, approximate a missing signal, write to a machine, approve
  or submit anything, or present a generated figure as proven.

## References and assets

| File | Use it for |
|---|---|
| [`references/generation-pipeline.md`](references/generation-pipeline.md) | The generation pipeline with human gate and visual-QA loop; signal selection; dashboard, mock-up, analyser and deployment-set generation |
| [`references/ai-governance.md`](references/ai-governance.md) | GenAI PoC governance, agentic workflows, AI-built app intake, assistants, the AI maturity check |
| [`references/evidence-and-human-decisions.md`](references/evidence-and-human-decisions.md) | Citation rules per step and the full human-decision list |
| [`references/ai-initiative-maturity-ladder.md`](references/ai-initiative-maturity-ladder.md) | The evidence ladder for AI initiatives (idea to proven), the rule that PoC claims are not savings, pilot design pattern, failure modes |
| [`assets/ai-step-card.md`](assets/ai-step-card.md) | The card that admits an agent step and records its evidence and gate |
| [`assets/missing-signal-and-binding-table.md`](assets/missing-signal-and-binding-table.md) | The missing-signal table and the signal-to-panel binding table |

## Neighbours (not repeated here)

`od-context` (honesty rules), `od-context-freshness` (stale sources), `od-analytics-asset-build` (what to
build, ritual of use), `od-signal-standardization` (naming and data model), `od-prototype-poc` (four stages: PoC for
feasibility, prototype for benefit with real users, pilot, rollout; each is its own claim), `od-cybersec-gate` (sign-off package), `deploy-appstore` (deployment
package and release gate).

## Still open

- An AI knowledge or troubleshooting assistant is decided case by case at intake: ask for a measurable
  before/after. With one it goes the use-case route (savings only with documented basis); without one it is
  tracked as an initiative with a named owner and a usage measure, not as a counted saving.
- `<to confirm>` Whether general-purpose assistants are low impact (one deck) or already useful for
  deployment sets (another). Safer reading: allowed as a drafting aid, never as a gate.
- `<...>` Time-box lengths, accuracy thresholds and the champion-user group for pilots: not in the sources.

## Do not

- Do not let an agent start without a named owner, data source and review point.
- Do not deliver a generated artefact with open items inside it or without citations.
- Do not treat a prototype, a click-dummy or a generated dashboard as proven value.
- Do not skip IT takeover and Cyber Security approval because an app was generated quickly.
- Do not use company data with a tool that fails the fit criteria of R8.
- Do not rank AI use cases above basic data-model and reporting work in a plant that has not reached
  reporting.
