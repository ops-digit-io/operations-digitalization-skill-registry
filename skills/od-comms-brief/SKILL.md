---
name: od-comms-brief
description: >-
  Turn a selected use case into a brief and draft pack Internal Communications can publish (Lane 4): message, sourced proof points, audiences, call to action. Use after od-showcase-selection says go.
license: MIT
metadata:
  id: od-comms-brief
  tier: practice
  lane: lane-4
  new_state_lane: "Lane 4 (42, 43)"
  new_state_step: "Brief Internal Communications and draft; review and publish"
  owner_role: Digital-Business-Value-Engineer (DBVE); Internal Communications publishes
  tags: [lane-4, practice, draft]
  authority_level: draft the brief and the assets and run the check; nothing is published by OD; the plant owner, the OD lead and Internal Communications approve
  status: draft
  requires: [od-context]
  composes: [od-showcase-selection, od-showcase-followup, catalog-usecase, od-benefit-calculation]
  okf:
    type: Agent Skill
    title: Communications brief
    tags: [lane-4, practice, draft]
---

# Communications brief

Read `od-context` first. Lane 4 is outbound and runs through Internal Communications (IC), a department OD does not control. OD supplies a brief that IC can use as it stands; IC decides channel, form and date. This skill covers steps 42 (brief and draft) and 43 (review and publish, the human part).

## Purpose

Turns a selected use case into the brief and draft pack Internal Communications can publish. Use it after `od-showcase-selection` returns `go`, when a use-case story must be written for the company, or when a draft story needs its claims checked.

## Inputs and output

- **In:** the selection record with a `go` from `od-showcase-selection` and the evidence behind each claim.
- **Out:** the filled [`assets/comms-brief.md`](assets/comms-brief.md) and the draft assets, checked with `scripts/check_comms_brief.py`, plus the approvals list for IC. The brief is the hand-over; the drafts are optional help.

## Procedure

0. **Objective and audience first.** Write one line: what the audience should know or do afterwards, and how OD would see it (a request, a question, a use case running elsewhere). Name the audiences before the message. No target figures.
1. **One message.** One sentence a colleague could repeat: what changed, where, for whom. No claim in it that the proof points do not carry.
2. **Proof points,** two to four. Each has the claim, an evidence class (`CALCULATION`, `ESTIMATION`, `not yet assessed`), a source and the wording status (result or claim). A saving is a result only with a registered plant savings project and a baseline ([`references/message-and-claims.md`](references/message-and-claims.md)).
3. **Audience variants.** One short variant per audience the selection named: other plants and key users (can I run it?), BA Operations leadership (value and progress), all employees (what changed), OPEX and PPI/ME (which method step it supports), and line and shift supervisors where the change touches how a line is run (what changes for me, what do I do). Every variant answers "what does this mean for me". Whether supervisors are an audience is a hypothesis from a public survey of frontline workers (managers and supervisors were their most-cited channel); Internal Communications confirms.
4. **Call to action** that leads somewhere: the plant requests the use case from the catalogue (`catalog-usecase`), or asks for a definition if it is not catalogued. Name the contact as a role.
5. **Channels and timing** as Internal Communications states them in its intake ([`references/ic-handover.md`](references/ic-handover.md)); until the IC brief is supplied these stay open points, never guesses. The peer-sharing formats that exist (ODEC use-case slot, CoP best-practice slot, OPEX exchange call, Yokoten database) are listed there as options to confirm.
6. **Drafts** (article, one-pager, slide, short post) in English, in this shape: the problem the plant had, what was done, the measured result with its evidence class, then one quote with consent or a role-based statement. Write them in the house style once the brand template is available. Use the department's own formats where they fit: the CSP appetizer fields, the testimonial's four aspects, the ODEC story shapes ([`references/department-formats.md`](references/department-formats.md)). A draft repeats the proof points and adds no new claim.
6a. **People content.** A photo, video or quote of a member of staff needs the person's consent or a documented balancing of interests; otherwise the story uses roles and screenshots only. Fill the section in the brief.
7. **Run the check:** `python3 scripts/check_comms_brief.py MyBrief.md`. Exit 2 blockers, 1 warnings, 0 ready.
8. **Approvals** (human, in this order): plant owner, OD lead, Internal Communications. The agent never publishes and never marks an approval as given.

## What the check catches

A proof point without a source, a figure without an evidence class, a saving worded as a result without a registered project, a missing call to action or approvals list, a missing objective (warning), a host name, address or link to an internal system, a named individual, photo, video or quote content without a people-content statement, and superlatives. It does not judge whether the story is true: that is the plant owner's approval.

## Human gate and AI-agent notes

- **Agent may:** draft the brief and assets, run the check, list what is missing. **Humans decide:** every approval, the channel, the date, whether to publish.
- **Evidence to cite:** the source per proof point, the check output, the approvals received.
- IC's own process, templates and lead times are not recorded in the knowledge base. Do not describe them from memory; ask for the IC brief.

## Pitfalls

- A headline stronger than the best proof point.
- Telling all audiences the same thing. Leaders want value, plants want a next step.
- A call to action that has no owner or no place to go.
- Copying the business-case figure instead of the registered one.
- A statistic taken from a marketing blog or agency page instead of the department's own register; a public figure needs a source the department has opened.
- Publishing the story and never updating it when the use case changes.

## Available Scripts

| Script | Purpose | Arguments |
|---|---|---|
| `scripts/check_comms_brief.py` | Check the form of a brief: sources, evidence classes, call to action, approvals, sensitive items. Exit 2 blockers, 1 warnings, 0 ready | `<Brief.md>` (exactly one file) |
| `scripts/test_check_comms_brief.py` | Unit tests for the check | none; run `python3 test_check_comms_brief.py` |

An agent runs a script with its code or shell tool (`run_script` in tools that expose it) and reads the exit code and output.

## Example

Fictional example; the claim is made up for illustration.

```text
$ python3 scripts/check_comms_brief.py Brief.md
BLOCKER  proof point "Stops fall noticeably" has no source and no evidence class
exit 2   -> add the source and the class, then run again until exit 0
```

If the check reports a blocker, the brief does not leave OD. A failed or incomplete section is fixed in the brief, not argued with the script.

## Definition of done

The check exits 0 (or reports only warnings that are explained); every proof point has a source and an evidence class; the approvals list names roles and their real status; a human hands the brief to Internal Communications. Nothing is published by OD.

## References

| File | Open when |
|---|---|
| [`references/message-and-claims.md`](references/message-and-claims.md) | Wording a claim, the evidence classes, the style rules |
| [`references/department-formats.md`](references/department-formats.md) | The department's existing story formats (appetizer, testimonial, ODEC shapes, OPEX exchange call) and their status |
| [`references/ic-handover.md`](references/ic-handover.md) | What OD hands to Internal Communications, the channels that exist, and what is still unknown |
| [`assets/comms-brief.md`](assets/comms-brief.md) | The brief template |
| [`scripts/check_comms_brief.py`](scripts/check_comms_brief.py) | The check; `scripts/test_check_comms_brief.py` tests it |
