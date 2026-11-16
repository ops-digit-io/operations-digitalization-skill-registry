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

Fictional example (all values invented for illustration):

If it fails: a failed or unvalidated guardrail means no go-live; route back as the table in "The guardrails" says. A guardrail with no evidence is "not checked", not "passed".

## Outputs and hand-off: the text before outputs.yaml

`catalog-guardrails` delivers the go-live check record for a catalogued use case a plant applied itself. It reports; the plant decides whether the use case goes live.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Go-live check record | `assets/go-live-check-record.md`, filled | Plant owner, who decides `PRODUCTIVE` | Every guardrail (G1 to G7 and G7a) has a result (passed / failed / not checked), evidence, date and answering role; use case, plant and plant owner at the top; final line "go-live decision: the plant's" |
| Utilization expectation | Written into the go-live check record before go-live | Plant owner, then `deploy-handover` | Stated in the record: who uses the screen, in which meeting, which action follows |
| Routing of failed guardrails | Named in the record | `mi-data-availability`, `invest-screen`, `deploy-handover` or `deploy-cybersec`, as the failure says | Each failure is routed back with the target skill named; none is passed as a warning where it is marked block |

## Handoff

- **Also receives from:** `ops-dashboard-datatron`: QA checklist result.
- **Receives from:** `catalog-usecase` (match record), `catalog-systems` (system match record, branch 1b), `mi-data-availability` (verdict), `deploy-handover` (handover record).
- **Next in the flow:** step 1a3 and step 1b4 end with the plant's go-live decision; adoption is then checked by `deploy-handover`.
- **Stops here when:** any guardrail failed or has no evidence (it counts as "not checked"), or an external connection lacks Cyber Security sign-off (G7). No go-live; the skill never sets `PRODUCTIVE` and never marks a failed guardrail as passed.
