---
name: deploy-handover
description: >-
  Closes a use case: runs the handover to the plant against its definition of done (three-question test, named owner, data path to the machine), confirms real adoption with the strongest available evidence, and acts when utilization is low or NEVER (ADKAR diagnostic, review or retire). Use when a use case is handed to a plant, when someone asks whether it is really in use, when the dashboard is delivered but nobody opens it, when an owner or role changes, or when an application moves to IT. Drafts and reports; the plant decides PRODUCTIVE. Not for building (ops-analytics-asset), cataloguing (catalog-usecase) or the acceptance test (deploy-acceptance).
license: MIT
metadata:
  id: deploy-handover
  aliases: [od-handover-and-adoption]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Lane 1a (1a3), Lane 1b (1b4), Lane 2 (26), Lane 3a (3a6)"
  new_state_step: "Guardrails, go live, confirm adoption; Standardized deployment, go live, confirm adoption; Implement, evaluate impact, ensure adoption, catalogue; Rollout and adoption; ownership on formal acceptance"
  owner_role: Digital-Business-Value-Engineer (DBVE); the plant owns the adoption decision
  tags: [all, practice]
  authority_level: draft and report; the plant decides PRODUCTIVE
  status: stable
  origin: derived
  requires: [dept-context]
  composes: [deploy-acceptance, metrics-scorecard, catalog-standardization, catalog-usecase]
  okf:
    type: Agent Skill
    title: Handover and adoption
    tags: [all, practice]
---

# Handover and adoption

- Read `dept-context` first.
- Three kinds of handover, named apart: **use-case handover** (to a plant, the main procedure here), **application transfer** (to IT or another team) and **function succession** (a successor takes over the department's work).

## Purpose

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- Closes a use case properly: it runs the handover to the plant against the definition of done, confirms real adoption rather than delivery, and acts on the gap between `IMPLEMENTED` and `PRODUCTIVE`.
- Use it when a use case is handed to a plant, when someone asks whether it is in use, when utilization is low or `NEVER`, or when a role or portfolio changes hands.

## Inputs and output

- **Inputs**: the use case record (output asset, business process, utilization expectation), the acceptance protocol from `deploy-acceptance`, the data path to the machine, the named plant owner, and the utilization field.
- **Output**: the filled [`assets/handover-protocol.md`](assets/handover-protocol.md), including the three-question result, the ADKAR barrier point and the evidence-of-adoption tier.

## Procedure

1. Pull the acceptance result from `deploy-acceptance`; do not re-ask it.
2. Run the three-question test (section below) with the receiving side.
3. Check that the people the change affects (the shift, the line, their supervisors) were told **before** go-live what changes for them and what they do, not after it took effect.
   - Record who told them, when and how; if nobody did, that is the first action and the Awareness barrier in the ADKAR diagnostic.
   - People told only after the change took effect do not adopt it, so a use case that goes live without them stalls at Awareness.
4. Check the definition of done (section below): data path to the machine, named plant owner, use in a real shift, dependencies on the record.
5. Record the adoption tier with the strongest evidence available ([`references/evidence-of-adoption.md`](references/evidence-of-adoption.md)).
6. If utilization is low or `NEVER`, follow the section "When utilization is low or `NEVER`".
7. For an application or a function changing owner, use the two handing-over sections below.
8. Fill the protocol and hand it to the plant owner; reopen it on every scorecard cadence.

## The references are the substance

| File | Open when |
|---|---|
| [`references/adkar-diagnostic.md`](references/adkar-diagnostic.md) | A use case sits between `IMPLEMENTED` and `PRODUCTIVE` or utilization is low: why it stalls between `IMPLEMENTED` and `PRODUCTIVE` — the ADKAR barrier-point diagnostic, mapped onto this function's own lifecycle, with a worked example |
| [`references/evidence-of-adoption.md`](references/evidence-of-adoption.md) | You record the adoption tier: what counts as evidence of adoption, strongest first |
| [`references/ownership-and-handover-gates.md`](references/ownership-and-handover-gates.md) | An application or the function changes owner: who runs it and when ownership moves (OD x IT): build-and-run, formal acceptance, handover checklist, shared responsibility, criticality gates, self-assessment |
| [`references/od-impact-evaluation/procedure.md`](references/od-impact-evaluation/procedure.md) | Step 26 or Lane 1 step 6 closes: absorbed, evaluate the impact of a live use case and prepare the adoption confirmation record, with the saving's firmness (formerly `od-impact-evaluation`) |
| [`references/od-utilization-review/procedure.md`](references/od-utilization-review/procedure.md) | Something is deployed but not used: absorbed, the utilization table per use case and site, the no-saving decision route (formerly `od-utilization-review`) |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | You prepare go-live or hand over a dashboard: pre-go-live checklist from rollout lessons, the operations-concept gate, handing over a dashboard or data product, the use-case exchange with OPEX, and what an agent may draft |

## The rule

- **Built is not handed over, and handed over is not in use.**

- The three are separate states because they fail separately.
- A use case can be finished, documented, and still not opened by anyone: **use cases that record a utilization rate of `NEVER` exist.** That is a finding the function acts on, not a number it hides.

## The three-question test

- A handover is complete when the receiving side can answer all three **without asking the person who built it**:

1. **What is this, and what decision does it support?** Not the tool — the moment in the day it belongs to.
   - The daily Gemba walk is typically the largest consumer of what this function builds (check the utilization field for the current picture).
   - Shift checks and two-step Andon escalation are the other named moments.
2. **Where does its data come from, and what breaks it?** Which machines, which connector,
   which tool — written down to the machine, so a silent dashboard is diagnosable by the
   plant rather than only by the builder.
3. **Who owns it now, and who do they call?** Named, at the plant.

## Definition of done

- The use case's record carries its **output asset**, its **business process** and its
  **utilization expectation** — not just a title.
- The **data path is written down to the machine**.
- The **plant owner is named** and has used it **in a real shift, not a demonstration**.
- The people affected were **told before go-live** what changes for them, and the record says by whom and when.
- Anything the use case is still waiting on is recorded as a **dependency on the record
  itself**, so it stays visible after the builder has moved on.

## Adoption is the plant's decision

- OD can deliver something and hand it over; **only the plant can make it productive.** That is why `IMPLEMENTED` and `PRODUCTIVE` are separate statuses and why utilization is tracked at all.
- The recipient-feedback loop for this lane is the utilization rate on the Digitalization Scorecard.

- **How plant adoption is confirmed and recorded:** `references/evidence-of-adoption.md`'s three-tier evidence ranking (system usage log, named owner's dated statement, third-party observation) is confirmed — none of which is "handover marked `DONE`."

## When utilization is low or `NEVER`

1. **Run the ADKAR barrier-point diagnostic** (`references/adkar-diagnostic.md`) before assuming the asset is the problem — rate Awareness, Desire, Knowledge, Ability, Reinforcement in order and act on the first one that is insufficient.
   - A `NEVER` row is as often a Desire problem (nobody asked for it) as a Knowledge problem (nobody was trained), and the fix for each is different.
2. Ask whether it is consumed inside a ritual. If it belongs to no moment in the day, that
   is the finding.
3. Review with the requester — or **retire it**. Retiring an unused asset is a legitimate
   outcome and better than carrying it.
4. If the same asset is used at another plant, the gap is adoption, not the asset →
   `catalog-standardization`.

## Application transfer to IT or another team

- When an application (not a use case to a plant) changes owner, the builder runs it until **formal acceptance** and closes missing logging first; rules in `references/ownership-and-handover-gates.md`.
- The OpenSpec package that carries this into IT is OpenSpec IT demand (external).

## Impact and utilization after go-live

- Lane 2 step 7 and Lane 1 step 6 end with "adopted": run the absorbed [impact evaluation](references/od-impact-evaluation/procedure.md) for the adoption confirmation record and the saving's firmness, and the absorbed [utilization review](references/od-utilization-review/procedure.md) per site when something is deployed but not used.
- A proven, repeatable result then goes to `catalog-standardization` and `catalog-usecase` for cataloguing.

## Function succession

- A successor needs how the department works and what has been delivered, not a task list; the knowledge graph indexes both.
- Anything in flight is looked up live in the systems of record, never frozen into the knowledge base; details in `references/ownership-and-handover-gates.md`.

## Output — the protocol

- Fill [`assets/handover-protocol.md`](assets/handover-protocol.md) once per use case.
- It pulls its first section straight from `deploy-acceptance`'s protocol (no re-asking), adds the three-question test, the ADKAR barrier point and the evidence-of-adoption tier, and its last section is what `metrics-scorecard` reads back on every cadence
- — reopen it, do not file it away after one good week.

## Human gate and AI-agent notes

- **An agent may**: prepare the protocol, run the three-question test as a checklist against the record, rate the ADKAR elements from the evidence, and draft the impact and utilization tables.
- **Stays with roles**: the plant owner decides adoption and daily use; the receiving team formally accepts an application; the OD lead decides to retire an unused asset. An agent never marks a handover `DONE`.

## Example

```text
Input : use case "shift summary" (fictional), utilization = NEVER, handover = ONGOING
Output: three-question test: Q1 pass, Q2 fail (data path not written to the machine), Q3 pass
        ADKAR barrier point: Desire (nobody asked for it)
        adoption tier: none yet; action: review with requester or retire
```

## Do not

- Do not accept a handover without a named operations owner; for a dashboard or data product also without documented transformation, an owned workspace, access control and a named successor.
- Do not let old and new process run in parallel without an end date and a person assigned to switch the old one off.
- Do not record handover `DONE` because delivery happened: built, handed over and in use fail separately.
- Do not report `IMPLEMENTED` counts as adoption.
- Do not close a handover with an unnamed plant owner.
- Do not hide a `NEVER` utilization row: it is the finding the function acts on, and a hidden row hides the adoption gap from the scorecard.
- Do not apply a Knowledge-element fix (more training) to a Desire-element barrier point
  (nobody wanted it) — see `references/adkar-diagnostic.md`.
- Do not record an adoption tier stronger than the evidence actually available.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Use it for |
|---|---|
| [`references/background.md`](references/background.md) | Context, rationale, examples and notes moved out of this file; never an instruction |
| [`references/od-impact-evaluation/assets/impact-evaluation-record.md`](references/od-impact-evaluation/assets/impact-evaluation-record.md) | The output of od-impact-evaluation - the drafted evaluation of a live use case with each saving shown at its true firmness, plus the adoption confirmation block that the plant owner… |
| [`references/od-impact-evaluation/references/evaluation-questions.md`](references/od-impact-evaluation/references/evaluation-questions.md) | The questions to put to the plant owner and the records to read when evaluating a live use case, built from OD's own use case utilization template, the Use Case… |
| [`references/od-impact-evaluation/references/process-chain-practice.md`](references/od-impact-evaluation/references/process-chain-practice.md) | How impact evaluation (step 26) is run in the AI-driven chain - deployed is not used, the savings-forecast gate at sprint close, the utilisation table, dashboard-to-paper reconciliation, who attests value,… |
| [`references/od-impact-evaluation/references/savings-proof-path.md`](references/od-impact-evaluation/references/savings-proof-path.md) | The path a use case saving takes from a workshop pre-evaluation to a SPRINT-proven row as OD's own decks describe it, the firmness label at each step, and where it… |
| [`references/od-utilization-review/assets/utilization-review-record.md`](references/od-utilization-review/assets/utilization-review-record.md) | The record of one utilization review - scope, verdicts, smells, no-saving decisions, paper reconciliation and the dated follow-up list. |
| [`references/od-utilization-review/assets/utilization-table.md`](references/od-utilization-review/assets/utilization-table.md) | The utilization table, one row per use case and site, with the columns used in the decks plus verdict and basis. |
| [`references/od-utilization-review/references/no-saving-decision.md`](references/od-utilization-review/references/no-saving-decision.md) | What to do with a scaled-out use case that has deployments but no saving - the contradiction between decks (to be evaluated vs no potential), the safer reading, the decision… |
| [`references/od-utilization-review/references/utilization-method.md`](references/od-utilization-review/references/utilization-method.md) | The utilization table columns, the questions that find out what makes a use case utilized, the dashboard-without-action-owner smell, dashboard-to-paper reconciliation and the follow-up list. |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
