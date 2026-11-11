---
type: Skill Reference
title: Process chain practice
description: How impact evaluation (step 26) is run in the AI-driven chain - deployed is not used, the savings-forecast gate at sprint close, the utilisation table, dashboard-to-paper reconciliation, who attests value, and what an agent may draft. Pattern only, no figures.
resource: ../procedure.md
status: draft
tags: [use-case-support-service, practice, process-chain, draft]
---
# Process-chain practice

Distilled from the Operations Digitalization slide decks, abstracted into process guidance. No company figures. `PROPOSAL`
marks a synthesis; `<...>` is unknown. It adds to [`savings-proof-path.md`](savings-proof-path.md) and
[`evaluation-questions.md`](evaluation-questions.md).

## 1. Method in practice

**Deployed is not used.** Many use cases were scaled with no reported saving. Delivery count is not an impact indicator; a
high count can hide unreported impact or unused potential. The workshop question therefore turns from "what do we build next"
to "what is necessary so that the use cases we have are utilised". Track utilisation as its own result next to development
count.

**Savings-forecast gate at sprint close.** A use-case sprint (a few weeks, weekly review) does not close until:
- a savings baseline was defined at the start of the sprint (a review that starts without one "never reports the saving");
- a savings forecast exists for the plant, with its basis label (`calculated` / `estimated` / `none`);
- the saving is linked to a registered plant savings project and an owner role;
- the utilisation moment is named (who opens it, in which meeting, with which action).

If any item is missing, the sprint output is "implemented, no forecast / no project registered", and the plant owner is
asked to close the gap. Register a project for what is already implemented as a short-term measure; hand-registered savings
lag the work.

**Utilisation loop taught to plants.** Connect the relevant machines (high runners, trouble-makers) -> run the use cases ->
collect or select parameters -> analyse (parts produced, utilisation, downtime, parameter specification) -> find the root
cause with a known method -> create and calculate a cost-saving project and report it -> eliminate the deviation. Pair the
digital use case with the plant's own lean method and standard process (the OPEX standard method + digital standard use case +
standard process), so the dashboard feeds a recurring meeting that ends in an action.

**Reconcile with the paper process before accepting a dashboard.** Compare production records with the dashboard (downtime,
cycle-time records), explain every difference (breaks, shift changes, tolerance not yet applied), then settle signal selection
and categories. Run one deep dive with production and one with engineering. Check for organisational loss before proposing
technology (for example a feeder that cannot run during breaks).

## 2. Decision rules

- **Visibility alone does not create savings.** Process-value, alert, parameter-monitoring and andon dashboards were deployed
  widely without recorded savings; savings appeared where the dashboard drove a defined action. A dashboard without an action
  owner is a build smell: flag it.
- **Zero-saving scaled use case** is *to be evaluated until investigated*, not yet *no potential*. Only a human (the OD lead
  with the plant owner) may decide "no potential"; an agent never writes it.
- **Adoption** means "integrated into a standard operating procedure with dashboards and escalation flows", not "dashboard
  live" (see `od-handover-and-adoption`).
- **Who attests value:** the OPEX role plus the plant manufacturing-engineering role (a testimonial with the dashboards in
  production is the stated form), alongside the system usage record.
- **Countable** only with a condition before and after; no before/after, no saving.
- **Where the same use case saved at one plant and not at another** with equal integration effort, look first at people and
  method (who drives ideas, whether savings are calculated with controlling), then at technology.
- **A claim of impact needs the strongest evidence tier available** (`od-handover-and-adoption`); say which tier.

A use case with deployments and no reported saving stays "to be evaluated" until it is investigated.

## 3. Handoff contract

| Receives (from) | Hands on (to) |
|---|---|
| Handover protocol sections one to four (`od-handover-and-adoption`) | Evaluation record with each saving row at its true firmness, next step and owner |
| Benefit rows and the promise (`od-benefit-calculation`) | Rows ready for the SPRINT review, or the named gap (baseline, methodology) |
| Sprint close inputs (baseline, forecast, project id) from the sprint lead | "Implemented, no forecast / no project" list -> `od-scorecard-reporting`, `od-risk-watch` (value not materialising) |
| Utilisation table (see below) | Findings to `od-retro`; adoption gaps to `od-use-case-standardization`; training barrier to `od-rollout-training` |

**Utilisation table, columns:** use-case name (dashboard, app or analytics workflow); who uses it (department or team);
related process (for example the daily Gemba meeting); utilisation method in one to three sentences including the initial
state without digital support; utilisation rate (daily / weekly / monthly / on demand / never); impact or potential (low /
medium / high); plant-management relevant (yes / no).

## 4. Pitfalls and lessons

- Deploy without measuring utilisation means no value; causes named were culture and engagement, perceived value and cyber
  security.
- An automatic improvement metric per use case (for example output compared across time frames) was wanted and the technical
  concept was missing; do not promise it, ask the plant for the manual comparison.
- Low participation in community calls goes with low understanding and low savings: use it as a leading indicator.
- Pipeline can run empty if savings estimates are missing; a potential-estimation attribute with an own-judgement fallback
  keeps the entry alive but must be tagged as an estimate.

## 5. Questions to ask / definition of done

- Who uses it, how often, which action follows, what was the initial state, what would make people use it?
- Which processes improved by using data, and what were the hard savings? Which baseline? Who measured?
- Done when: the forecast gate items are all present or listed as open with an owner; each row shows its firmness; the
  adoption section is dated by the plant owner or marked pending.

## 6. AI agent operating notes

- **Can do:** monitor utilisation and savings-forecast completeness per sprint plant and flag "implemented, no forecast / no
  registered project"; draft the savings evaluation after go-live; `PROPOSAL`: fill utilisation-table rows from dashboard usage
  logs (the data source is not shown in the decks) and prepare the production-record versus dashboard reconciliation table.
- **Required inputs:** definition protocol and benefit rows, usage log or the plant owner's statement, baseline, project id.
- **Human gate:** the plant owner confirms adoption; finance (through SPRINT) proves savings; an agent never writes
  "adopted" or "proven".
- **Evidence to cite:** usage-log extract and date, ledger row id, project id, tier of evidence.
- **Hands over:** the evaluation record to the plant owner, findings to `od-retro`, firm rows to `od-benefit-calculation`.
