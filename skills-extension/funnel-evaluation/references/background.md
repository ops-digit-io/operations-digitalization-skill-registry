---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Purpose and where it sits

Answers the question `funnel-use-case` does not: does the envisioned solution fit what the plant has and the
problem needs, or does it quietly require more capability than anyone named? It serves Lane 2 step **22** (features
and data check), before the business case (step 24), and feeds the Lane 3 fit test. Key user: DBVE; an AI agent can
run the script and draft the protocol. It always ends in a visualized ranking and one evaluation score, never prose
alone. Read `dept-context` first.

## Outputs and hand-off: the text before outputs.yaml

`funnel-evaluation` delivers one evaluation protocol per use case, with the script output pasted in, a total score out of 100 and one of four verdicts. It never ends in prose alone and never approves an investment.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Evaluation protocol | `assets/evaluation-protocol.md`, filled, one per use case | `bc-build`, the owning skill of a gap, or `dept-decision-rights` (by verdict) | Step 0 case ranking is pasted; the script output (gap chart, score) is pasted, not re-described from memory |
| Per-area assessment | Section of the protocol | Receiver of the verdict | Every candidate area has an evidenced as-is level and a target with its driver; no target stands without a named driver or business need |
| Sequenced gaps with owner | Section of the protocol | `mi-equipment` (F9, F10), `mi-data-availability` (F11, F2), `mi-signals` (F16); the use case itself for the rest | Every gap is sequenced and classified with an owner and next skill; gaps staying with the use case are named for the scope and cost of `bc-build` |
| Verdict and total score | Verdict and score in the protocol | `bc-build` (ready), owning skill (capability first), `funnel-use-case` (over-engineered), `dept-decision-rights` (escalate) | One of the four verdicts is stated with the score recorded; the tool boundary sentence and operations-concept status sit next to it |

## Handoff

- **Receives from:** `funnel-use-case` (the scoped use case), `funnel-requirements` and `mi-data-availability` (requirement and signal verdicts).
- **Next in the flow:** Lane 2 step 22, before the business case at step 24. Ready goes to `bc-build`; a capability gap goes to its owning skill and returns here before the business case; over-engineered goes back to the definition; escalate goes to `dept-decision-rights`.
- **Stops here when:** a tool has no operations concept (owner, service level, support level), because the verdict is then escalate and never "ready to build"; or a target exceeds every driver rated high or dominant. Do not hand over a ready verdict on it.
