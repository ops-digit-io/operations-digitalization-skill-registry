---
type: Skill Reference
title: ECR management summary
description: "The eCR management summary as the department recorded it (section map, governance conditionals, enum fields) and the house rules of its capital-request builder (bc-capital-request, formerly ecr-builder): refusal / de-risk gate, grounding tags, open items and conflicts, maturity verdict."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [ecr, capital-request, department-standard, lane-2, lane-3]
derived_from:
  - "Work vault, OD Department Knowledge/OD-instance/eCR_Management_Summary_inventory.md (content inventory of the blank eCR management-summary template), read 2026-11-10"
  - "Work vault, OD Department Knowledge/OD-instance/skills-inventory-and-roadmap.md (bc-capital-request features), read 2026-11-10"
  - "Work vault, OD Department Knowledge/OD-instance/OD_Skill_Naming_Convention.md (ecr-builder renamed bc-capital-request; chain bc-build → bc-assess → bc-capital-request), read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# eCR management summary

The department has a capital-request builder of its own (`ecr-builder`, `bc-capital-request` under its
naming convention) and an inventory of the blank eCR management-summary template. This file carries
both, so the registry's draft no longer has to guess the form.

## Section map (keep the numbering, it is the governance backbone)

| # | Section | Purpose |
|---|---|---|
| — | Cover | Project title, location, company |
| 1 | Executive summary | Decision on one page: What? Why? How? plus request type, investment class, request amount (GPA, non-GPA, total) and key figures (IRR, RoS, payback) |
| 2a / 2b | Current / planned situation | Baseline and target state |
| 3 | Investment data | Capex split GPA / non-GPA |
| 4a / 4b / 4c | Volume and capacity · savings · price and cost development | The evidence behind the numbers |
| 5 / 5a | Key financial figures · sensitivity | Financial verdict; robustness |
| 6 | Risks and opportunities | Risk or opportunity, action, level, sensitivity case |
| 7 | Alternative solutions | Options weighed, including doing nothing |
| 8 | Plant / production layout | If applicable |
| 9 | Project timeline | Milestones |
| B1-B3 | Backup | Customer project / PCIS data, P&L and cash flow, growth / value field |

**Enums.** Request type: Capital Request · Operational Supplement · FX Supplement · Scope Change · ICO
Asset Transfer · Expense Request (IT only). Investment class: Expansion · Cost Reduction · Other · Data
Processing · Spare Parts.

**Governance conditionals.**
- Expansion → fill the growth / value field (executive summary and backup B3).
- Right of use → report IIR alongside IRR.
- Sensitivity (5a) is mandatory above the amount or realization-time threshold the template states
  (read it from the current template; do not quote it from memory).
- Layout, PCIS data and growth field are "if applicable".

## House rules of the builder

1. **Ingest with an inventory.** List every source used (quotes, mails, spreadsheets, the business-case
   backbone, the investment estimate).
2. **Refusal / de-risk gate.** If the inputs are too thin to carry the request, stop and return the
   de-risk questions instead of a deck. A thin case is not pushed to approval.
3. **Grounding on every figure** with the same tags as the business case (`[input]`, `[assumption]`,
   `[market]`, `[unknown]`), shown visibly in the summary.
4. **Open items and conflicts** close the summary: every conflict between sources and every open figure,
   with its owner.
5. **Maturity verdict**, one of: **Ready to sign** · **Sign the floor** (approve the grounded part only)
   · **Not ready**. It is a recommendation; the approvers decide.
6. **Value comes from `bc-build`, cost from `bc-cost`**; the summary never
   nets them silently and never upgrades a de-banked lever.
