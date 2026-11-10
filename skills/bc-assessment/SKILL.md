---
name: bc-assessment
description: >-
  Score a business case against the OD house rubric and give its maturity-gate verdict - the
  department's bc-assessment, the governance step between od-benefit-calculation (value) plus the cost estimate and
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
    - "Work vault, OD Department Knowledge/OD-instance/30-skills/bc-assessment.zip (SKILL.md, reference/*, assets/build_bc_short.py), read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/BC-Assessment-Skill/use-case-input-questionnaire.md, read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/Business-Cases/gemba-app/bc-assessment-report.md, read 2026-11-10"
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
assess it. The rubric below is the department package's own (`30-skills/bc-assessment.zip`, transcribed into
[`references/`](references/)); the package stays the master.

## Inputs and output

- **Inputs:** the value backbone `business-case.md` (`od-benefit-calculation`, `business-case-backbone.md`), the
  investment estimate (`od-investment-input`), the raw inputs of the case (transcripts, mockups, reference drafts,
  cross-checks), and if present the intake questionnaire [`assets/use-case-input-questionnaire.md`](assets/use-case-input-questionnaire.md) (sections A-L).
- **Output:** `bc-assessment-report.md` next to the case: the scorecard (criterion, verdict, evidence, note), the
  conflict register, the maturity-gate verdict and the ranked open questions; optionally the standard one-pager deck
  (9 slides plus the provenance backup slide). All generated files in English.

## The rubric ([`references/criteria-checklist.md`](references/criteria-checklist.md))

Score every criterion **pass / partial / gap** with evidence (file and section). A gap on any C criterion blocks signing.

| Group | Criteria |
|---|---|
| **C - core integrity** | C1 value-only separation (cost in the investment estimate, never netted) · C2 grounding tag on every figure · C3 expected and potential kept apart (`~ EXPECTED (min / potential)`) · C4 de-banking of big movers resting on an `[unknown]` · C5 auditable arithmetic (`value x driver`, hard floor derivable by hand) |
| **D - deck-renderable structure** | D1 lever register (H hard, O optional IDs) · D2 contribution matrix min / expected / max with confidence · D3 sub-cases with effort to realize · D4 value vs. dependencies · D5 abstracted before / after · D6 SMART gated milestones M0-M4, dates after approval · D7 soft / strategic clusters kept qualitative · D8 ranked refinement questions with worked examples · D9 overall picture slide |
| **E - discipline** | E1 factual language · E2 tilde convention for estimated euros · E3 market value tagged `[market]` where input is missing · E4 baseline honesty (representative plant) · E5 per-plant value and rollout scope on separate axes · E6 neuwerk brand |

Substance behind the criteria: [`grounding-discipline.md`](references/grounding-discipline.md),
[`lever-model.md`](references/lever-model.md). OD x IT (2026-09-11) adds one check to C1: bankable vs.
assumption-dependent stated apart, with investment envelope, minimum viable rollout, maximum scale-out and TCO.

## Procedure

1. **Assessor.** Confirm the case was built by someone else; if not, name a different assessor.
2. **Read everything** - backbone, every input file, the questionnaire. Map which fact came from which file.
3. **Score** every criterion of the rubric with evidence.
4. **Provenance and conflicts** ([`provenance-and-conflicts.md`](references/provenance-and-conflicts.md)): list every
   input, what the case drew from it, and every conflict between sources with how it was resolved and why.
5. **Verdict** (maturity gate): **Ready to sign** (all C pass, expected floor grounded) · **Sign the floor, validate the
   upside** (C pass, a de-banked lever awaits its input) · **Not ready** (any C gap; name the missing input and its owner).
   Recommendation only; the approvers decide.
6. **Report** `bc-assessment-report.md`: scorecard, conflict register, verdict, ranked open questions (normalized
   influence 0-100, grouped into blocks one conversation can close). Pattern: [`worked-example-gemba.md`](references/worked-example-gemba.md).
7. **Deck (optional)** with [`scripts/build_bc_short.py`](scripts/build_bc_short.py) - slide sequence in
   [`deck-spec.md`](references/deck-spec.md), run and QA loop in [`build-engine.md`](references/build-engine.md). The
   script needs the neuwerk template `_nw_template.pptx` beside it (department package `bc-assessment.zip` or
   `neuwerkbrand.zip`; not stored here).
8. Hand a signable case to `od-capital-request` if money is needed.

## Do not

- Do not fix the case while assessing it; return it to `od-benefit-calculation` with the findings.
- Do not pass a figure without a grounding tag, or a headline that sums hard and optional levers.
- Do not let the builder assess their own case.
