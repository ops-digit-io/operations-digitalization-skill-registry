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

Fictional example (invented numbers, not a company figure):

If it fails: when the value backbone, the estimate or the verdict is missing, the refusal gate returns the de-risk questions, not a package. An invalid or unsourced figure is marked ⟨to be collected⟩ with the role who supplies it.

## Outputs and hand-off: the text before outputs.yaml

`bc-capital-request` delivers a draft capital request (eCR) package for human approvers. It drafts only: a human reviews and
submits, and the agent never submits, signs or approves.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Capital request package | `assets/capital-request-package.md`, filled | Human who submits; approvers named in the approval matrix | Complete or its gaps are named with a role who closes them; the ask in one line (amount, what it buys, phase, decision date); route and approver written next to the amount; tracked and proven euros shown separately, never summed; options include a smaller version and do-nothing |
| Management summary deck | Deck from the eCR builder; last slide Open items and conflicts | Human who submits | Every figure carries its grounding chip; closed with one maturity verdict (Ready to sign, Sign the floor, or Not ready) |
| Gate dependency on use case and saving rows | Dependency entry (`ECR CREATION`, then `ECR APPROVAL` once filed) with owner | DBVE (owns the savings ledger) | Recorded on the use case and on each affected saving row; updated with the outcome after the decision |
| Refusal with de-risk questions | Reply listing the de-risk questions, instead of a package | Requester | Issued when the value backbone, investment estimate or assessment verdict is missing or too thin; no package is produced |

## Handoff

- **Receives from:** `bc-build` (saving rows), `bc-cost` (cost side), `bc-assess` (verdict),
  `funnel-prototype` (validation record), `dept-decision-rights` (route and approvers), and `funnel-evaluation` (verdict).
- **Next in the flow:** the human approvers decide, then `deploy-handover` (step 26) and the build. This is the end
  of the business-case chain (step 25). Other gates the spend touches: OpenSpec IT demand (external), `deploy-cybersec`.
- **Stops here when:** no money needs committing (record that and stop), the value backbone, estimate or verdict is
  missing (refusal gate), or the package has been handed to a human to review and submit.

## Where it sits in the lanes

- Lane 2, step 25: capital request if investment is needed (package value and cost for approval). It waits on MPEE / BA Operations approval; the queue time is a placeholder in the skill-map table.
- Lane 3, shared front-end, step 33: business case and capital request (value and cost; capital request if needed; hand off once demand is clear). It waits on IT commitment and MPEE approval.
- Upstream: `bc-build` (value rows), `bc-cost` (cost side), `bc-assess` (verdict), `bc-portfolio` (ranking), `funnel-prototype` (validation record), `funnel-evaluation` and `invest-screen` (verdict).
- Downstream: the human approvers, then `deploy-handover` and the build.
- `bc-cost` is the investment estimate and the investment planning input pack for equipment integration; this skill takes its output and does not define the cost side a second time.

## Source notes

- The department's eCR builder package (`30-skills/ecr-builder.zip`) is the master; this skill transcribes it (workflow, backbone and conditionals, grounding and colour coding, refusal gate, renderer). The neuwerk template `_nw_template.pptx` comes from that package and is not stored here.
- The inventory of the eCR management summary (sections, enums, governance conditionals) is in `ecr-management-summary.md`.
- Open points the sources do not answer: the system the eCR is filed in, who files it, how long approval takes.
- The investment planning template that the project-support lane lists as an asset is still to confirm or create in the resources registry (`00-core/15-resources.md`).
- The rule "do not split one investment into several requests to land under a threshold" is a proposed rule, not stated in the sources.
