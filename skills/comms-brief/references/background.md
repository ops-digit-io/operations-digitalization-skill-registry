---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Example

Fictional example; the claim is made up for illustration.

If the check reports a blocker, the brief does not leave OD. A failed or incomplete section is fixed in the brief, not argued with the script.

## Outputs and hand-off: the text before outputs.yaml

`comms-brief` (steps 42 and 43) delivers the brief and draft pack that Internal Communications can publish as it stands.
OD publishes nothing; Internal Communications decides channel, form and date.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Communications brief | `assets/comms-brief.md`, filled | Internal Communications | Objective, audiences, one message, two to four proof points each with source, evidence class and wording status, an audience variant per audience, a call to action with a role as contact, channels and timing (open points until IC states them), and a people-content statement |
| Check output | Output of `scripts/check_comms_brief.py` | Internal Communications | Exit 0, or only explained warnings; no blocker |
| Approvals list | Approvals section of the brief | Plant owner, OD lead, Internal Communications | Roles named in order (plant owner, OD lead, Internal Communications) with their real status; none marked given by an agent |
| Draft assets (optional) | Article, one-pager, slide or short post | Internal Communications | Each draft repeats the proof points and adds no new claim |

## Handoff

- **Receives from:** `comms-showcase` (the selection record with a go and the evidence behind each claim).
- **Next in the flow:** Internal Communications reviews and publishes (step 43); then `comms-followup` (step 44), with the approved brief. The call to action points plants to `catalog-usecase`.
- **Stops here when:** the check reports a blocker (for example a proof point without source or evidence class, a saving worded as a result without a registered project, a named individual or an internal host or link). The brief does not leave OD until fixed. A human hands the brief over; the agent never publishes.

## Open questions

- Internal Communications' own intake, templates and lead times are not recorded in the knowledge base. Replace the open points in `references/ic-handover.md` once the IC brief is supplied. Supplier: Internal Communications.
- Whether line and shift supervisors are an audience is a hypothesis from a public survey of frontline workers; IC confirms.

## Sources used in the improvement run

- None added; no vault or archive claim was introduced in this run.
