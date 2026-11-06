---
type: Skill Reference
title: Process chain practice
description: How the prototype step is run inside the new process chain - the PoC to prototype to pilot to rollout maturity stages, scope-limiting as a gate strategy, AI-assisted mock-ups and dashboards, decision rules, handoff contract, pitfalls, and AI agent operating notes. Process guidance only; no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [prototype, process-chain, ai-agent, maturity]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice

Derived from the Operations Digitalization slide decks, abstracted into process guidance. Examples are illustrative and use
`<placeholders>`. Own synthesis is marked `PROPOSAL`; unknowns are `<...>`.

## Where it sits

Step **23** (prototype and validate), after the data check (22) and before the business case (24). It also touches **25** (a pilot
request is the capital request that follows a passed PoC) and **26** (graduation). The AI-built-app path (prompt to prototype,
IT takeover, Cyber Security approval) runs between lane 2 and lane 3a (`it-demand-package`, `od-cybersec-gate`).

## Handoff contract

| Receives | From | Must be there |
|---|---|---|
| Defined case, named owner, moment of use | `od-use-case-definition` | Challenge, objective, success criterion |
| Requirements as stories | `od-requirements-breakdown` | Atomic, testable, one vocabulary |
| Data verdict, missing-signal table | `od-data-availability-check` | No prototype on missing data |

| Hands on | To | What it carries |
|---|---|---|
| Validation record with the stage label | `od-benefit-calculation`, `od-capital-request` | Evidence, never "proven" |
| Passed dashboard-type prototype | `od-analytics-asset-build` | Inputs, tag-to-panel table |
| Failed or inconclusive | `od-use-case-definition` or close | Recorded reason (kill or cancel with reason so it is not re-raised) |
| Pilot that shows benefit | `od-handover-and-adoption`, `od-use-case-promotion` | Reference plant, maturity, next call to action |

## The maturity stages: PoC, prototype, pilot, rollout

The decks use four stages, each with a purpose, an owner and a resource rule. Plant and OD are responsible together, OD guides
the early stages.

| Stage | Purpose | Typical shape | Resource rule |
|---|---|---|---|
| **PoC** | Validate feasibility: reduce a risk with a minimal test | Days to weeks | Minimal waste |
| **Prototype** | Validate the benefit with real users | About a sprint; may have gaps for scale and operations | Minimal waste |
| **Pilot** | Validate operational scalability | Real users, the support concept in use | Sufficient resources |
| **Rollout** | Scale out | Effects planned empirically | Sufficient resources |

The click-dummy of this skill sits before the PoC (a usability question). The ladder in `references/status-labels.md` is the
labelling of items; this ladder is the working sequence. PoC and prototype are two separate stages.
For each item keep the standing question per stage: reference plant, maturity, where applied, next call to action.

**Strategy rules for any prototype:** new software follows the reference architecture; new use cases use existing templates;
legacy systems may run while Cyber Security assesses them and interface compatibility is assured; a prototype outside the
standard is allowed only if a path to the reference architecture exists, it is piloted there once benefit shows, and central
functions are informed. A custom case is acceptable only if the value is very high, may be prototyped, and is folded into the
standard systems before it counts as mature.

## Method in practice

1. **Screen by value and risk.** High value, low risk: build. High risk: build the cheapest possible test that teaches the most
   important thing. Low value: do not test or build. Less sophistication often yields more value.
2. **Sketch several radical alternatives, then classify** (approved for technical support, business support, advanced support, rejected).
   The most valuable result was often the simplest design.
3. **One prompt, one mock-up.** A written brief carrying the refined requirements yields a clickable HTML mock-up and a short
   product video, instead of "a specification everyone reads differently". Mock-ups carry invented values.
4. **A dashboard prototype** follows the generative-AI process in `od-analytics-asset-build` (tag list, requirements, optional
   reference JSON, configuration out, import and test, iterate); the prototype needs no time-series to generate.
5. **Guided analyzers** (for example a cycle-time analyzer): raw signals plus business context (machine, production-relevant groups
   such as part number, recipe, tool, plausibility range) lead to signal proposals for cycle start and stop, then a model, then
   a productive model giving cycle time and ranked influencers. The user's interaction and decisions are mandatory at tuning and
   deployment; the tool proposes, a person confirms.
6. **Scope-limit to stay out of the heavy gate (a gate strategy).** A PoC that states "no machine connectivity, no production
   gateway, deployment unchanged" stays out of the heavier OT security path. Keep two lists side by side: **used in the PoC**
   and **deferred, needs further Cyber Security approval**. Foundations to prove first: cyber assessment status, data
   protection, AI protection (no customer data used for model training), alignment with purchasing.
7. **Frame the pilot request** as time-bound, software-only where possible, with a named user group, explicit capacity (users,
   storage, shared compute) and an **evaluation date** that feeds the scale or funding decision. Add a budget buffer for lost
   early-offer discounts so the pilot needs no re-submission; state what is excluded.
8. **Prefer a staged scope** when the benefit of the first step stands alone (for example, a first step without a system
   integration, a second step with it).

## Decision rules

- Which test: usability or scope question, click-dummy; data or model question, PoC on real data; both, click-dummy first.
- Rule-based per-machine logic needs hours of exploration per machine, its own rule set, no plausibility check, no "why"; a learned
  approach is justified where generalization and influencers are the value. `<to confirm: the boundary of generalization is not
  stated; an early priorities deck proposed a generic stability use case that was later dropped for process-specific analytics>`
- A prototype that works for one plant needs a containerized, more flexible algorithm to scale; iterations add scope
  (operator times, loading times), so freeze the scope per stage.
- **AI use cases against the maturity of the plant.** AI becomes useful from the higher levels of data maturity; do not rank an AI
  prototype above basic data-model and reporting work in a plant that has not reached reporting. Triage grid for AI topics: low
  barrier and high potential, mid barrier and high potential, high barrier and mid potential.
- **Prompt-to-prototype for applications** shows value fast, but the path is generated solution, IT takeover, Cyber Security
  approval; assume supplier code is partly AI-generated.
- **Knowledge assistants** (troubleshooting, documentation) are low barrier but fall outside the classic use-case definition (a
  before and after state with savings); decide case by case at intake: with a measurable before and after, take the use-case route (savings only with a documented basis); without one, track
  them as an initiative with an owner and a usage measure (`PROPOSAL: assistant`), not as a counted saving, and say so. Good fit: a repetitive task, a public or general skill set, good internal documentation. The answer is
  advice only; a parameter change is a human decision by the process engineer.

## Pitfalls and lessons

- A mock-up approved by people who will not use it; show it at the moment of use.
- A pilot without a pass criterion, owner and evaluation date is a demo.
- Calling a PoC "proven" or reporting a pilot count as value.
- Prototypes outside the standard with no path to the reference architecture.
- Time-boxed AI pilots succeed on narrow scope: one input format, one trigger, read-only extraction.

## Questions to ask

- What is the one open question, in the plant's words, and which stage answers it?
- What pass criterion, scope, time box and validator were written before building?
- What is excluded, and does that keep it out of the OT security path?
- If it passes, which reference architecture and which template does it join?

## Definition of done

The stage label is stated with its source; the pass criterion preceded the build; the validator is a named role; the result is
passed, failed or inconclusive; the deferred list is written; the plant has confirmed or declined value in writing; nothing says
"proven".

## AI agent operating notes

- **Can do:** draft the click-dummy brief, generate the mock-up and the video from the refined requirements, generate a dashboard
  configuration on a test instance, write the validation record, draft the pilot request fields, list the used-in-PoC and
  deferred lists, check that a pass criterion exists.
- **Chain rule (PROPOSAL):** an agent step starts only when a human has named the process owner, the data source and the review
  point. A minimal version without a review screen is acceptable only for read-only extraction.
- **Evidence it must cite:** the requirement each screen answers, the tags that fed each panel, the criterion and its source.
- **Human gate:** the plant validates the value; the OD lead decides whether a stage is passed; Cyber Security approval and IT
  takeover are never implied.
- **Hands over:** the validation record to `od-benefit-calculation` and `od-capital-request`.
