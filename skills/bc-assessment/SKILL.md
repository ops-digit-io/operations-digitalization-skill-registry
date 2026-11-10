---
name: bc-assessment
description: >-
  Score a business case against the OD house rubric and give its maturity-gate verdict - the
  department's bc-assessment, the governance step between od-benefit-calculation (value) plus od-investment-input (cost) and
  od-capital-request. Checks that every figure carries a grounding tag, value and cost stay apart,
  the headline is the grounded expected value, high-impact low-confidence levers are de-banked, the
  milestones are gated and SMART, and sources do not conflict; returns pass / partial / gap per
  criterion, a ranked list of open questions and a verdict. Use when a business case is drafted and
  before a capital request, when a reviewer asks whether a case is signable, or when two cases must be
  compared on the same rubric.
license: MIT
metadata:
  id: bc-assessment
  tier: practice
  lane: [lane-2, lane-3]
  new_state_lane: "Lane 2 (24), Lane 3 front-end (33)"
  new_state_step: "Business case (value and cost), assessment, ranking; Business case, prioritization, capital request"
  department_names: ["bc-assess", "bc-assessment", "business-case-assessor"]
  owner_role: OD lead (separation of duties - not the person who built the case)
  authority_level: recommend - scores and gives a verdict; the approvers decide
  status: draft
  sources_read: 2026-11-10
  requires: [od-context]
  composes: [od-benefit-calculation, od-investment-input, od-capital-request]
  derived_from:
    - "Work vault, OD Department Knowledge/OD-instance/skills-inventory-and-roadmap.md (bc-assessment: traditional process, features, improvement vector), read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/OD_Skill_Naming_Convention.md §3-4 (bc-assessment renamed bc-assessment; chain od-benefit-calculation -> bc-assessment -> od-capital-request; od-investment-input feeds bc-assessment; governance separate from build), read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/Business-Cases (README house standard, _template), read 2026-11-10"
  okf:
    type: Agent Skill
    title: Business case assessment
    tags: [department-core, lane-2, lane-3]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Business case assessment

Read `od-context` first. The department's `bc-assessment`: it scores a case, it does not build one. **Governance stays
separate from build** (department naming convention): the person who built the case in `od-benefit-calculation` does not
assess it. The full house rubric (core gates C1 to C5 and the D and E criteria) is in the department's
`bc-assessment` package, which is the master; this skill runs the checks the department documents name and
marks the rubric items it cannot see as ⟨to transcribe from the package⟩.

## Inputs and output

- **Inputs:** the value backbone (`od-benefit-calculation`, `business-case-backbone.md`), the investment estimate (`od-investment-input`).
- **Output:** a scored assessment (pass / partial / gap per criterion, with the reason visible), a ranked open-question
  list, and a maturity-gate verdict. The department renders it as its standard one-pager deck plus a provenance and
  conflict backup slide.

## The checks (from the department's house standard)

| Check | Pass when |
|---|---|
| Grounding | Every figure carries `[input]`, `[assumption]`, `[market]` or `[unknown]` |
| Value and cost apart | Cost lives in the investment estimate; nothing netted into the value headline |
| Headline | `~ EXPECTED / plant / yr (min / potential)`; expected is the grounded, bankable value |
| Lever register | Every euro has a lever ID (H1…, O1…) with formula and driver; no lump sums |
| De-banking | No banked number on a high-impact lever resting on an `[unknown]`; it is a ring-fenced sensitivity and the top open question |
| Hard and optional apart | Never summed into one headline |
| Bankable vs assumption-dependent | Stated apart, with the investment envelope, minimum viable rollout, maximum scale-out and TCO (OD x IT, 2026-09-11) |
| Milestones | SMART, gated, with the gate at which each lever's value unlocks; dates after approval |
| Provenance and conflicts | Every source listed; every conflict between sources visible with an owner |
| Core gates C1-C5, criteria D and E | ⟨to transcribe from the bc-assessment package⟩ |

## Procedure

1. Confirm the case was built by someone else; if not, name a different assessor.
2. Run every check above against the backbone and the estimate; record pass / partial / gap with the reason.
3. Rank the open questions by normalized influence (0 to 100, the biggest swing = 100) and group them into blocks one
   conversation can close.
4. Give the verdict: **signable** (all core gates pass), **sign the floor** (the grounded part only), or **not ready**
   (a core gate fails). Recommendation only.
5. Hand a signable case to `od-capital-request` if money is needed.

## Do not

- Do not fix the case while assessing it; return it to `od-benefit-calculation` with the findings.
- Do not pass a figure without a grounding tag, or a headline that sums hard and optional levers.
- Do not present the transcribed checks as the complete department rubric.
