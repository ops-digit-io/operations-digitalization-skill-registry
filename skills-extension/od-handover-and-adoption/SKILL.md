---
name: od-handover-and-adoption
description: >-
  Close a use case properly — run the handover to the plant against its definition of
  done, confirm real adoption rather than delivery, and act on the gap between
  implemented and productive. Covers the three-question handover test, the utilization
  expectation, what to do about an asset nobody opens, and handing over the function
  itself rather than a single use case. Use when a use case is being handed to a plant,
  when someone asks whether something is actually in use, when utilization is low or
  `NEVER`, or when a role or portfolio is changing hands. Also covers the OD x IT ownership rules
  (build-and-run, ownership moves only on formal acceptance, the handover checklist, recurring
  self-assessment), the impact evaluation and adoption confirmation record of a live use case
  (formerly od-impact-evaluation) and the utilization review "deployed is not used" per site
  (formerly od-utilization-review).
license: MIT
metadata:
  id: od-handover-and-adoption
  tier: practice
  lane: all
  new_state_lane: "Lane 1a (1a3), Lane 1b (1b4), Lane 2 (26), Lane 3a (3a6)"
  new_state_step: "Guardrails, go live, confirm adoption; Standardized deployment, go live, confirm adoption; Implement, evaluate impact, ensure adoption, catalogue; Rollout and adoption; ownership on formal acceptance"
  owner_role: Digital-Business-Value-Engineer (DBVE); the plant owns the adoption decision
  authority_level: draft and report; the plant decides PRODUCTIVE
  status: stable
  origin: derived
  sources_read: 2026-11-10
  requires: [dept-os]
  composes: [od-acceptance-test, od-scorecard-reporting, od-use-case-standardization, it-demand-package, catalog-usecase]
  derived_from:
    - ops-knowledge-graph/_knowledge/10-Department/Handover.md
    - ops-knowledge-graph/_knowledge/10-Department/Rituals.md
    - ops-knowledge-graph/_knowledge/10-Department/Use case lifecycle.md
    - Prosci. The Prosci ADKAR Model. prosci.com/methodology/adkar. Retrieved 2026-10-22. Industry framework, not peer-reviewed — used for the individual-adoption diagnostic, not for the delivery-status facts above it.
    - Prosci. Individual Barriers to Change and What to Do About Them. prosci.com/blog/individual-barriers-to-change-and-what-to-do-about-them. Retrieved 2026-10-22. Source of the "barrier point" diagnostic.
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/Transcripts/2026-09-11_OD-IT-alignment_meeting-notes.txt, read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT (README, lane 1-3), read 2026-11-10"
  okf:
    type: Agent Skill
    title: Handover and adoption
    tags: [all, practice]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Handover and adoption

Read `dept-os` first.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/adkar-diagnostic.md`](references/adkar-diagnostic.md) | Why a use case stalls between `IMPLEMENTED` and `PRODUCTIVE` — the ADKAR barrier-point diagnostic, mapped onto this function's own lifecycle, with a worked example |
| [`references/evidence-of-adoption.md`](references/evidence-of-adoption.md) | What counts as evidence of adoption, strongest first — confirmed 2026-10-22, closing "how is adoption confirmed and recorded" |
| [`references/ownership-and-handover-gates.md`](references/ownership-and-handover-gates.md) | Who runs it and when ownership moves (OD x IT, 2026-09-11): build-and-run, formal acceptance, handover checklist, shared responsibility, criticality gates, self-assessment |
| [`references/od-impact-evaluation/procedure.md`](references/od-impact-evaluation/procedure.md) | Absorbed: evaluate the impact of a live use case and prepare the adoption confirmation record, with the saving's firmness (formerly `od-impact-evaluation`) |
| [`references/od-utilization-review/procedure.md`](references/od-utilization-review/procedure.md) | Absorbed: the utilization table per use case and site, the no-saving decision route (formerly `od-utilization-review`) |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Pre-go-live checklist from rollout lessons, the operations-concept gate, handing over a dashboard or data product, the use-case exchange with OPEX, and what an agent may draft |

Handover is a **tracked state** in this function, not a courtesy at the end of a build.
Use cases record it as `DONE` or `ONGOING`; it typically trails development and
implementation, which is exactly why it is measured (count the lag live on the use-case list).

## The rule

**Built is not handed over, and handed over is not in use.**

The three are separate states because they fail separately. A use case can be finished,
documented, and still not opened by anyone: **use cases that record a
utilization rate of `NEVER` exist.** That is a finding the function acts on, not a
number it hides.

## The three-question test

A handover is complete when the receiving side can answer all three **without asking the
person who built it**:

1. **What is this, and what decision does it support?** Not the tool — the moment in the
   day it belongs to. The daily Gemba walk is typically the largest consumer of what this
   function builds (check the utilization field for the current picture). Shift checks and two-step Andon escalation are the other named moments.
2. **Where does its data come from, and what breaks it?** Which machines, which connector,
   which tool — written down to the machine, so a silent dashboard is diagnosable by the
   plant rather than only by the builder.
3. **Who owns it now, and who do they call?** Named, at the plant.

## Definition of done

- The use case's record carries its **output asset**, its **business process** and its
  **utilization expectation** — not just a title.
- The **data path is written down to the machine**.
- The **plant owner is named** and has used it **in a real shift, not a demonstration**.
- Anything the use case is still waiting on is recorded as a **dependency on the record
  itself**, so it stays visible after the builder has moved on.

## Adoption is the plant's decision

OD can deliver something and hand it over; **only the plant can make it productive.** That
is why `IMPLEMENTED` and `PRODUCTIVE` are separate statuses and why
utilization is tracked at all. The recipient-feedback loop for this lane is the
utilization rate on the Digitalization Scorecard.

**How plant adoption is confirmed and recorded, closed 2026-10-22:**
`references/evidence-of-adoption.md`'s three-tier evidence ranking (system usage log,
named owner's dated statement, third-party observation) is confirmed — none of which is
"handover marked `DONE`."

## When utilization is low or `NEVER`

1. **Run the ADKAR barrier-point diagnostic** (`references/adkar-diagnostic.md`) before
   assuming the asset is the problem — rate Awareness, Desire, Knowledge, Ability,
   Reinforcement in order and act on the first one that is insufficient. A `NEVER` row is as
   often a Desire problem (nobody asked for it) as a Knowledge problem (nobody was trained),
   and the fix for each is different.
2. Ask whether it is consumed inside a ritual. If it belongs to no moment in the day, that
   is the finding.
3. Review with the requester — or **retire it**. Retiring an unused asset is a legitimate
   outcome and better than carrying it.
4. If the same asset is used at another plant, the gap is adoption, not the asset →
   `od-use-case-standardization`.

## Handing over an application to IT or another team

When an application (not a use case to a plant) changes owner, the OD x IT rules apply
([`references/ownership-and-handover-gates.md`](references/ownership-and-handover-gates.md)): the team that
builds it runs it; ownership moves only on **formal acceptance**; until then the builder supports it; the
builder closes missing logging or observability first; the receiving team checks legacy status, backlog,
version currency, architecture, business logic, logging and observability. The OpenSpec package that
carries this into IT is `it-demand-package`.

## Impact and utilization after go-live

Lane 2 step 7 and Lane 1 step 6 end with "adopted": run the absorbed
[impact evaluation](references/od-impact-evaluation/procedure.md) for the adoption confirmation record and
the saving's firmness, and the absorbed [utilization review](references/od-utilization-review/procedure.md)
per site when something is deployed but not used. A proven, repeatable result then goes to
`od-use-case-standardization` and `catalog-usecase` for cataloguing.

## Handing over the function, not a use case

The same rule applies one level up. A successor does not need a task list — stale within
a week, and it lives in the source systems anyway. They need two things: **how the
department works** and **what has already been delivered**. The knowledge graph is the
index into both: open a plant and it shows what exists there; open a capability and it
shows which plants have it and which do not.

Anything genuinely in flight — open decisions, current status, this week's queue — is
looked up live in the systems of record. It is deliberately **not** written into the
knowledge base, because a frozen copy of a moving thing is worse than no copy: it is a
copy people trust.

## Output — the protocol

Fill [`assets/handover-protocol.md`](assets/handover-protocol.md) once per use case. It
pulls its first section straight from `od-acceptance-test`'s protocol (no re-asking), adds
the three-question test, the ADKAR barrier point and the evidence-of-adoption tier, and its
last section is what `od-scorecard-reporting` reads back on every cadence — reopen it, do
not file it away after one good week.

## Do not

- Do not accept a handover without a named operations owner; for a dashboard or data product also without documented transformation, an owned workspace, access control and a named successor.
- Do not let old and new process run in parallel without an end date and a person assigned to switch the old one off.
- Do not record handover `DONE` because delivery happened.
- Do not report `IMPLEMENTED` counts as adoption.
- Do not close a handover with an unnamed plant owner.
- Do not hide a `NEVER` utilization row.
- Do not apply a Knowledge-element fix (more training) to a Desire-element barrier point
  (nobody wanted it) — see `references/adkar-diagnostic.md`.
- Do not record an adoption tier stronger than the evidence actually available.
