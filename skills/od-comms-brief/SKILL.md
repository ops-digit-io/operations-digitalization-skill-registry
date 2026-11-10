---
name: od-comms-brief
description: >-
  Turn a selected use case into the brief and the draft pack that Internal Communications can publish
  (new-state Lane 4, steps 42 and 43): one message, proof points that each carry a source and an evidence class,
  audience variants (other plants and key users, BA Operations leadership, all employees, OPEX and PPI/ME), a call to
  action that leads back into Lane 1, drafts of the article, one-pager, slide and short post in English, and the list of
  approvals. Checks the brief with a script before it leaves OD. Use after od-showcase-selection returns go, when a
  use-case story must be written for the company, or when a draft story needs its claims checked.
license: MIT
metadata:
  id: od-comms-brief
  tier: practice
  lane: lane-4
  new_state_lane: "Lane 4 (42, 43)"
  new_state_step: "Brief Internal Communications and draft; review and publish"
  owner_role: Digital-Business-Value-Engineer (DBVE); Internal Communications publishes
  authority_level: draft the brief and the assets and run the check; nothing is published by OD; the plant owner, the OD lead and Internal Communications approve
  status: draft
  sources_read: 2026-11-10
  requires: [od-context]
  composes: [od-showcase-selection, od-showcase-followup, catalog-usecase, od-benefit-calculation]
  derived_from:
    - "Owner request, 2026-11-10: a new outbound service lane for use-case marketing via the internal communications department; the Internal Communications brief is still to be supplied"
    - "Work vault, OD Department Knowledge/OD-instance/use-case-development-transformation.md (Teams channel, Use Case Library and SharePoint as the collaboration surface; reporting by execution), read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/00-core/03-objectives.md (Lean and Digital with OPEX), read 2026-11-10"
    - "Vault rules (CLAUDE.md sections 1.5 and 3): no invented figures, roles not individuals, English deliverables"
    - "Work vault, Deck Texts/D-Operations Digitalization/OD Initiative - Creation of Marketing Template for Use Cases.md (appetizer template, marketing pairing; results slide empty), read 2026-11-10"
    - "Work vault, Deck Texts/03-AMT_MI_Standard_Agenda_Use_Case_Works/9.0-Marketing_Slides-WIP.md (testimonial key aspects, slide 17), and Deck Texts/D-Operations Digitalization/2025 10-ODEC.md (story shapes, slides 9-11), read 2026-11-10"
    - "Work vault, Deck Texts/Smart Factory - Tools and Architecture/Berechtigtes Interesse.md (balancing of interests for employee photos, worked example of 2022), read 2026-11-10"
  okf:
    type: Agent Skill
    title: Communications brief
    tags: [lane-4, practice, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---

# Communications brief

Read `od-context` first. Lane 4 is outbound and runs through Internal Communications (IC), a department OD does not control. OD supplies a brief that IC can use as it stands; IC decides channel, form and date. This skill covers steps 42 (brief and draft) and 43 (review and publish, the human part).

## Inputs and output

- **In:** the selection record with a `go` from `od-showcase-selection` and the evidence behind each claim.
- **Out:** the filled [`assets/comms-brief.md`](assets/comms-brief.md) and the draft assets, checked with `scripts/check_comms_brief.py`, plus the approvals list for IC. The brief is the hand-over; the drafts are optional help.

## Procedure

1. **One message.** One sentence a colleague could repeat: what changed, where, for whom. No claim in it that the proof points do not carry.
2. **Proof points,** two to four. Each has the claim, an evidence class (`CALCULATION`, `ESTIMATION`, `not yet assessed`), a source and the wording status (result or claim). A saving is a result only with a registered plant savings project and a baseline ([`references/message-and-claims.md`](references/message-and-claims.md)).
3. **Audience variants.** One short variant per audience the selection named: other plants and key users (can I run it?), BA Operations leadership (value and progress), all employees (what changed), OPEX and PPI/ME (which method step it supports).
4. **Call to action** that leads somewhere: the plant requests the use case from the catalogue (`catalog-usecase`), or asks for a definition if it is not catalogued. Name the contact as a role.
5. **Channels and timing** as Internal Communications states them in its intake ([`references/ic-handover.md`](references/ic-handover.md)); until the IC brief is supplied these stay open points, never guesses. The peer-sharing formats that exist (ODEC use-case slot, CoP best-practice slot, OPEX exchange call, Yokoten database) are listed there as options to confirm.
6. **Drafts** (article, one-pager, slide, short post) in English, in the house style once the brand template is available. Use the department's own formats where they fit: the CSP appetizer fields, the testimonial's four aspects, the ODEC story shapes ([`references/department-formats.md`](references/department-formats.md)). A draft repeats the proof points and adds no new claim.
6a. **People content.** A photo, video or quote of a member of staff needs the person's consent or a documented balancing of interests; otherwise the story uses roles and screenshots only. Fill the section in the brief.
7. **Run the check:** `python3 scripts/check_comms_brief.py MyBrief.md`. Exit 2 blockers, 1 warnings, 0 ready.
8. **Approvals** (human, in this order): plant owner, OD lead, Internal Communications. The agent never publishes and never marks an approval as given.

## What the check catches

A proof point without a source, a figure without an evidence class, a saving worded as a result without a registered project, a missing call to action or approvals list, a host name, address or link to an internal system, a named individual, photo, video or quote content without a people-content statement, and superlatives. It does not judge whether the story is true: that is the plant owner's approval.

## Human gate and AI-agent notes

- **Agent may:** draft the brief and assets, run the check, list what is missing. **Humans decide:** every approval, the channel, the date, whether to publish.
- **Evidence to cite:** the source per proof point, the check output, the approvals received.
- IC's own process, templates and lead times are not recorded in the vault. Do not describe them from memory; ask for the IC brief.

## Pitfalls

- A headline stronger than the best proof point.
- Telling all audiences the same thing. Leaders want value, plants want a next step.
- A call to action that has no owner or no place to go.
- Copying the business-case figure instead of the registered one.
- Publishing the story and never updating it when the use case changes.

## References

| File | Open when |
|---|---|
| [`references/message-and-claims.md`](references/message-and-claims.md) | Wording a claim, the evidence classes, the style rules |
| [`references/department-formats.md`](references/department-formats.md) | The department's existing story formats (appetizer, testimonial, ODEC shapes, OPEX exchange call) and their status |
| [`references/ic-handover.md`](references/ic-handover.md) | What OD hands to Internal Communications, the channels that exist, and what is still unknown |
| [`assets/comms-brief.md`](assets/comms-brief.md) | The brief template |
| [`scripts/check_comms_brief.py`](scripts/check_comms_brief.py) | The check; `scripts/test_check_comms_brief.py` tests it |
