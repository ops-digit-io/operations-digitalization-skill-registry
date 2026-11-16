---
name: comms-brief
description: >-
  Write the brief that Internal Communications can publish for a use case that comms-showcase cleared (Lane 4): one message, two to four sourced proof points with evidence class, audience variants, a call to action and the approvals list, then run the brief check script. Use when someone says "write the story for this use case", "brief Internal Communications", "draft the article or one-pager for the use case", or "check the claims in this draft story". Drafts only: the plant owner, OD lead and Internal Communications approve, and OD never publishes. Not for deciding whether a use case may be told (comms-showcase) or for follow-up after publication (comms-followup).
license: MIT
metadata:
  id: comms-brief
  aliases: [od-comms-brief]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: lane-4
  new_state_lane: "Lane 4 (42, 43)"
  new_state_step: "Brief Internal Communications and draft; review and publish"
  owner_role: Digital-Business-Value-Engineer (DBVE); Internal Communications publishes
  tags: [lane-4, practice, ready]
  authority_level: draft the brief and the assets and run the check; nothing is published by OD; the plant owner, the OD lead and Internal Communications approve
  status: ready
  requires: [dept-context]
  composes: [comms-showcase, comms-followup, catalog-usecase, bc-build]
  okf:
    type: Agent Skill
    title: Communications brief
    tags: [lane-4, practice, ready]
---

# Communications brief

## Purpose

- Turn a selected use case into the brief (and optional drafts) that Internal Communications (IC) can publish (Lane 4, steps 42 and 43).
- Use it after `comms-showcase` returns `go`, when a use-case story must be written for the company, or when a draft story needs its claims checked.
- Lane 4 is outbound and runs through IC, a department OD does not control: OD supplies a brief IC can use as it stands; IC decides channel, form and date.
- Read `dept-context` first.

## Terms used here

- **Brief**: the filled [`assets/comms-brief.md`](assets/comms-brief.md); it is the hand-over to IC.
- **Drafts**: optional help for IC (article, one-pager, slide, short post); they repeat the brief and add nothing.
- **Proof point**: one claim with its evidence class, source and wording status.

## Inputs and output

- **In:** the selection record with a `go` from `comms-showcase` and the evidence behind each claim.
- **Out:** the filled brief, optional drafts, the check output, and the approvals list for IC.
- Output contract: [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- Requires Python 3 (standard library only) to run the check.

## Procedure

1. **Objective and audience first.** Write one line: what the audience should know or do afterwards, and how OD would see it (a request, a question, a use case running elsewhere). Name the audiences before the message. No target figures.
2. **One message.** One sentence a colleague could repeat: what changed, where, for whom. No claim in it that the proof points do not carry.
3. **Proof points,** two to four. Each has the claim, an evidence class (`CALCULATION`, `ESTIMATION`, `not yet assessed`), a source and the wording status (result or claim).
   - A saving is a result only with a registered plant savings project and a baseline, because an unregistered saving is a claim IC cannot defend (`references/message-and-claims.md`).
4. **Audience variants.** One short variant per audience the selection named:
   - other plants and key users (can I run it?), BA Operations leadership (value and progress), all employees (what changed), OPEX and PPI/ME (which method step it supports),
   - and line and shift supervisors where the change touches how a line is run (what changes for me, what do I do).
   - Every variant answers "what does this mean for me".
   - Supervisors as an audience is a hypothesis from a public survey of frontline workers; IC confirms.
5. **Call to action** that leads somewhere: the plant requests the use case from the catalog (`catalog-usecase`), or asks for a definition if it is not catalogued. Name the contact as a role.
6. **Channels and timing** as IC states them in its intake (`references/ic-handover.md`); until the IC brief is supplied these stay open points, never guesses.
   - The peer-sharing formats that exist (ODEC use-case slot, CoP best-practice slot, OPEX exchange call, Yokoten database) are listed there as options to confirm.
7. **People content.** A photo, video or quote of a member of staff needs the person's consent or a documented balancing of interests; otherwise the story uses roles and screenshots only. Fill the section in the brief.
8. **Drafts** (optional) in English, in this shape: the problem the plant had, what was done, the measured result with its evidence class, then one quote with consent or a role-based statement.
   - Write them in the house style once the brand template is available.
   - Use the department's own formats where they fit: the CSP appetizer fields, the testimonial's four aspects, the ODEC story shapes (`references/department-formats.md`).
   - A draft repeats the proof points and adds no new claim.
9. **Run the check and loop:** `python3 scripts/check_comms_brief.py Brief.md`. Fix every blocker, run again, until exit 0 or only explained warnings.
10. **Approvals** (human, in this order): plant owner, OD lead, Internal Communications. The agent never publishes and never marks an approval as given.

## What the check catches

- A proof point without a source, a figure without an evidence class, a saving worded as a result without a registered project.
- A missing call to action or approvals list, a missing objective (warning).
- A host name, address or link to an internal system, a named individual, photo, video or quote content without a people-content statement.
- Superlatives.
- It does not judge whether the story is true: that is the plant owner's approval.

## Example

```text
$ python3 scripts/check_comms_brief.py Brief.md
x BLOCKER proof-without-source
    A proof point has no source: | Stops fall noticeably | ... (fictional)
-> add the source and the class, then run again until exit 0
exit 2 = blockers, 1 = warnings only, 0 = ready, 3 = file unreadable or wrong usage
```

```text
Proof point (fictional): "Shift lead reviews downtime in the daily meeting on one line"
Evidence class: not yet assessed | Source: handover record | Worded as: result
Weak version: "Downtime is slashed" - no source, no class, superlative: blocked.
```

## Human gate and AI-agent notes

- **Agent may:** draft the brief and drafts, run the check, list what is missing.
- **Humans decide:** every approval, the channel, the date, whether to publish. Nothing is published by OD.
- **Evidence to cite:** the source per proof point, the check output, the approvals received.
- IC's own process, templates and lead times are not recorded in the knowledge base. Do not describe them from memory; ask for the IC brief.

## Pitfalls

- A headline stronger than the best proof point: IC publishes it and the plant is held to it.
- Telling all audiences the same thing: leaders want value, plants want a next step.
- A call to action that has no owner or no place to go.
- Copying the business-case figure instead of the registered one.
- A statistic from a marketing blog or agency page instead of the department's own register; a public figure needs a source the department has opened.
- Publishing the story and never updating it when the use case changes; `comms-followup` keeps it true.

## Available Scripts

| Script | Purpose | Arguments |
|---|---|---|
| `scripts/check_comms_brief.py` | Check the form of a brief. Exit 2 blockers, 1 warnings, 0 ready, 3 unreadable file or wrong usage. Standard library only | `<Brief.md>` (exactly one file); `--help` |
| `scripts/test_check_comms_brief.py` | Unit tests for the check | none; run `python3 test_check_comms_brief.py` |

- An agent runs a script with its code or shell tool and reads the exit code and output.

## Errors and validation

- **Check exits 1 (blockers):** fix the named line in the brief and run the check again; do not hand over a brief with a blocker.
- **Check exits 3 (file unreadable or wrong usage):** pass the path of the brief file as the only argument; `--help` shows the usage.
- **A figure has no source or evidence class:** remove the claim or mark it a claim; never round it up to pass the check.

## Definition of done

- The check exits 0 (or reports only warnings that are explained).
- Every proof point has a source and an evidence class.
- The approvals list names roles and their real status.
- A human hands the brief to IC.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/message-and-claims.md`](references/message-and-claims.md) | Step 2 and 3: wording a claim, the evidence classes, the style rules |
| [`references/department-formats.md`](references/department-formats.md) | Step 8: the department's existing story formats (appetizer, testimonial, ODEC shapes, OPEX exchange call) and their status |
| [`references/ic-handover.md`](references/ic-handover.md) | Step 6 and 10: what OD hands to IC, the channels and formats that exist, who approves what |
| [`assets/comms-brief.md`](assets/comms-brief.md) | Step 1: the brief template to fill |
| [`scripts/check_comms_brief.py`](scripts/check_comms_brief.py) | Step 9: the check; [`scripts/test_check_comms_brief.py`](scripts/test_check_comms_brief.py) tests it |
| [`references/background.md`](references/background.md) | Context, rationale and open points; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
