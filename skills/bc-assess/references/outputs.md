---
type: Skill Reference
title: Outputs
description: The outputs bc-assess must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`bc-assess` scores a business case against the OD house rubric and returns a maturity-gate verdict. It scores; it does
not build or fix the case. The verdict is a recommendation, the approvers decide.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Assessment report | `bc-assessment-report.md` next to the case: scorecard with criterion, verdict (pass, partial, gap), evidence and note | `bc-capital-request`; OD lead | Every rubric criterion scored with evidence (file and section); a criterion that cannot be scored is marked gap with the missing input named |
| Conflict register | Section of the report: every input, what the case drew from it, each conflict and how it was resolved | `bc-build` (case builder) | Every input file listed; every conflict between sources has a resolution and a reason |
| Maturity-gate verdict | Verdict line in the report: Ready to sign, Sign the floor and validate the upside, or Not ready | `bc-capital-request`; approvers | One verdict stated; Not ready names the missing input and its owner; the assessor is not the case builder |
| Ranked open questions | Section of the report, normalized influence 0-100, grouped into blocks one conversation can close | `bc-build` (case builder) | Questions ranked and grouped |

## Handoff

- **Receives from:** `bc-build` (the value backbone), `bc-cost` (the investment estimate), and the
  raw inputs of the case, with the intake questionnaire if present.
- **Next in the flow:** a signable case goes to `bc-capital-request` (step 25); an unsigned case goes back to
  `bc-build` with the findings.
- **Stops here when:** the assessor is the builder of the case (name a different assessor), or any C criterion is a gap
  (blocks signing). Do not fix the case while assessing it.
