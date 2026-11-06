---
name: od-utilization-review
description: >-
  Review whether a deployed or scaled-out use case is actually used and delivers value - "deployed is not used". Fills the
  utilization table per use case and site, asks "what would make it utilized?", flags the dashboard-without-action-owner smell,
  reconciles the dashboard with the paper record before it is accepted, decides between "to be evaluated" and "no potential"
  for a use case with deployments but no saving, and ends in a dated follow-up list. Feeds the savings-forecast gate at
  the close of a use-case sprint. Drafts the review; the plant owner confirms adoption and a human decides "no potential".
  Use when a use case has been live for a while, when a use case was implemented in a sprint without a forecast, when the
  scorecard shows low or NEVER utilization, when a scaled-out use case carries no saving, or when someone asks whether a
  delivered use case is really in use.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-utilization-review
  tier: practice
  lane: use-case-support-service
  new_state_lane: Lane 1 (step 1a3), Lane 2 (step 26), Lane 3a (step 3a6), Spine
  new_state_step: "Go live and adopt: utilization review"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  origin: plan-draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-impact-evaluation, od-handover-and-adoption, od-portfolio-and-savings-analysis, od-benefit-calculation, od-acceptance-test, od-retro, od-scorecard-reporting, od-use-case-standardization, od-rollout-training]
  derived_from:
    - Operations Digitalization slide decks (utilization tables, scaling lessons, dashboard acceptance, sprint close), abstracted into process guidance; no figures.
  okf:
    type: Agent Skill
    title: Utilization review
    tags: [use-case-support-service, practice, adoption, utilization, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Utilization review

Read `od-context` first.

A delivered use case is not a used use case, and a used use case is not yet a saving. The decks return to the same
finding: many scaled-out use cases ran with no reported saving, and a count of delivered use cases says nothing about
impact. This skill is the recurring check that nobody owned: **who uses it, how often, which action follows, what was the
state without it, what would make people use it** - and what to do with the answer.

## Where it sits in the chain

| Step | Role of this skill |
|---|---|
| `1a3` Validate and go live (Lane 1) | Start the utilization table for the use case; name the ritual of use before go-live |
| `26` Implement and graduate (Lane 2) | First review after a settling period; input to `od-impact-evaluation` and to graduation |
| `3a6` Rollout and adopt (Lane 3a) | Same review for a new system; `od-handover-and-adoption` hands the use over to it |
| Sprint close (Lane 2 / Spine) | Source of the savings-forecast completeness gate |
| Spine | Findings feed `od-scorecard-reporting` (utilization as its own result) and `od-retro` |

The step ids are the registry's proposal (`PROPOSAL`); the owner places the skill in `process.yaml`.

## Neighbours - what is not repeated here

| Skill | It owns | This skill adds |
|---|---|---|
| `od-impact-evaluation` | The adoption confirmation record, the evaluation questions, the firmness of a saving | The recurring review that decides when an evaluation is due, and the rule for a use case with no saving |
| `od-handover-and-adoption` | The handover test, ADKAR diagnostic, evidence-of-adoption ranking, retire-or-fix of a NEVER row | The table across use cases and sites, the smells, the dashboard-to-paper check |
| `od-portfolio-and-savings-analysis` | Ledger reading; tracked is not proven, implemented is not in use | The where-saved / deployed-without-saving / potential cut per use case |
| `od-retro` | One decided adjustment per month | A named input (utilization findings) |
| `od-scorecard-reporting` | Sources and thresholds for the numbers | The question each utilization number must answer |

## References and assets

| File | Use it for |
|---|---|
| [`references/utilization-method.md`](references/utilization-method.md) | Table columns, the "what makes it utilized?" questions, the action-owner smell, dashboard-to-paper reconciliation, the follow-up list |
| [`references/no-saving-decision.md`](references/no-saving-decision.md) | To-be-evaluated vs no-potential: the contradiction between decks, the safer reading, the decision rule, the sprint-close forecast gate |
| [`assets/utilization-table.md`](assets/utilization-table.md) | The table, one row per use case and site |
| [`assets/utilization-review-record.md`](assets/utilization-review-record.md) | The review record: verdict per use case, decision, follow-up list |

## Procedure

1. **Scope.** Name the use cases and sites under review. Start from the live list (`od-catalog`, ledger via
   `od-portfolio-and-savings-analysis`); read live, do not quote counts.
2. **Fill the table** per use case and site with the plant owner (`assets/utilization-table.md`). Unknown cells stay `<unknown>`.
3. **Ask the utilization questions** (method reference, section 3) - with Production, OPEX and Engineering, not with the builder alone.
4. **Run the smells** (action owner, ritual, paper reconciliation, parallel old process).
5. **Assign a verdict** per row: `USED-WITH-ACTION`, `USED-NO-ACTION`, `NOT-USED-FIXABLE`, `NOT-USED`, `UNKNOWN`.
6. **Decide the no-saving cases** with `references/no-saving-decision.md`: to be evaluated, re-scope, retire, or escalate.
7. **Write the follow-up list**: action, role, due, check date. Hand findings on (below).

## Handoff contract

- **In**: from `od-handover-and-adoption` the iterated tag list, process description, refined requirements, named ritual of use and
  utilization expectation; from `od-use-case-definition` the success criteria; from the ledger the saving status and its firmness.
- **Out**: confirmed rows to `od-impact-evaluation` (evaluation and saving proof path); no-saving cases and the forecast gap to
  `od-portfolio-and-savings-analysis` and the sprint close; adoption gaps with an ADKAR diagnosis to `od-handover-and-adoption`
  and `od-rollout-training`; a use case used at one site but not another to `od-use-case-standardization`; the one finding worth a
  process change to `od-retro`; utilization as a result to `od-scorecard-reporting`.

## AI agent operating notes

- **Can do**: draft table rows from usage logs where they exist (the decks do not show the data source - `PROPOSAL`, `<usage log source>`);
  compute the where-saved / deployed-without-saving / potential matrix; flag "implemented, no forecast, no project registered";
  check that a ritual of use is named; draft the follow-up list; draft the paper-versus-dashboard comparison grid.
- **Needs**: the live use-case list, the savings ledger with read date, the use-case definition, the plant owner's answers.
- **Must cite**: the log, ledger row or named statement behind each cell; label every saving tracked or proven.
- **Human gate**: the plant owner confirms adoption; a human (OD lead with the plant owner) decides "no potential" and any retirement.
  The agent never writes "no potential".
- **Hands over** with the record and the follow-up list; it does not close its own follow-ups.

## Do not

- Do not count delivered use cases as impact, or read `IMPLEMENTED` as in use.
- Do not read a missing saving as non-use, or a non-used asset as no potential (unreported saving and non-utilized potential are different).
- Do not accept a dashboard before it is reconciled with the paper record.
- Do not mark a use case "no potential" before it has been investigated.
- Do not hide a `NEVER` row, and do not quote current numbers, plants or people in this skill's outputs without a read date.
