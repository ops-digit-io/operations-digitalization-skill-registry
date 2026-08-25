---
name: od-handover-and-adoption
description: >-
  Close a use case properly — run the handover to the plant against its definition of
  done, confirm real adoption rather than delivery, and act on the gap between
  implemented and productive. Covers the three-question handover test, the utilization
  expectation, what to do about an asset nobody opens, and handing over the function
  itself rather than a single use case. Use when a use case is being handed to a plant,
  when someone asks whether something is actually in use, when utilization is low or
  `NEVER`, or when a role or portfolio is changing hands.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-handover-and-adoption
  tier: practice
  lane: all
  owner_role: Digital-Business-Value-Engineer (DBVE); the plant owns the adoption decision
  authority_level: draft and report; the plant decides PRODUCTIVE
  status: stable
  sources_read: 2026-08-10
  requires: [od-context]
  composes: [od-scorecard-reporting]
  derived_from:
    - ops-knowledge-graph/_knowledge/10-Department/Handover.md
    - ops-knowledge-graph/_knowledge/10-Department/Rituals.md
    - ops-knowledge-graph/_knowledge/10-Department/Use case lifecycle.md
  okf:
    type: Agent Skill
    title: Handover and adoption
    tags: [all, practice]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# Handover and adoption

Read `od-context` first.

Handover is a **tracked state** in this function, not a courtesy at the end of a build.
272 use cases record it `DONE` and 38 `ONGOING` — it trails development and implementation
by about thirty, consistently, which is exactly why it is measured.

## The rule

**Built is not handed over, and handed over is not in use.**

The three are separate states because they fail separately. A use case can be finished,
documented, and still not opened by anyone: **eight of the use cases that record a
utilization rate are recorded as `NEVER`.** That is a finding the function acts on, not a
number it hides.

## The three-question test

A handover is complete when the receiving side can answer all three **without asking the
person who built it**:

1. **What is this, and what decision does it support?** Not the tool — the moment in the
   day it belongs to. The daily Gemba walk is the single largest consumer of what this
   function builds; 125 of the 202 use cases that record a utilization rate are used
   daily. Shift checks and two-step Andon escalation are the other named moments.
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
is why `IMPLEMENTED` (129) and `PRODUCTIVE` (167) are separate statuses and why
utilization is tracked at all. The recipient-feedback loop for this lane is the
utilization rate on the Digitalization Scorecard.

⟨How plant adoption is confirmed and recorded is an open gap — to confirm.⟩ Until it is
closed, record adoption as what it is: the named plant owner's statement, dated.

## When utilization is low or `NEVER`

1. Ask whether it is consumed inside a ritual. If it belongs to no moment in the day, that
   is the finding.
2. Review with the requester — or **retire it**. Retiring an unused asset is a legitimate
   outcome and better than carrying it.
3. If the same asset is used at another plant, the gap is adoption, not the asset →
   `od-use-case-standardization`.

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

## Do not

- Do not record handover `DONE` because delivery happened.
- Do not report `IMPLEMENTED` counts as adoption.
- Do not close a handover with an unnamed plant owner.
- Do not hide a `NEVER` utilization row.
