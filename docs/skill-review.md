---
type: Design Record
title: Skill review
description: "The review of all 51 skills against Anthropic's skill authoring best practices and the Agent Skills specification - measured facts, a judgement per criterion with a quote as evidence, an overall rating, and how it compares with the SkillEvaluator rating."
status: draft
owner: human:jakob.gabriel
tags: [skills, review, anthropic]
generated: { by: claude-code/1, at: 2026-11-16T00:00:00Z }
---
# Skill review

Reviewed 2026-11-16 against [`skill-review-rubric.md`](skill-review-rubric.md). **an AI reviewer reading each skill; not a human review.** The rubric is taken from Anthropic's published best practices and the open Agent Skills specification; each criterion carries its source quote there.

- **Measured facts** (`scripts/skill_facts.py`) are computed from the files and checked against the limits the sources state.
- **Judgements** are a reviewer's reading of the skill text per criterion, each with a quote as evidence and, for a weakness, one concrete change. The overall rating is the reviewer's, with a reason. Nothing is a formula.
- **Not measured:** whether the skill makes an agent behave better. The sources ask for evaluations with and without the skill; none of the skills has any (see the facts).
- **Evidence check:** 741 of 762 evidence quotes were found word for word in the skill's own files by a script; the rest mix a quote with a description, or are plain statements of absence (17 of those). A reviewer can be wrong: confirm a rating before acting on it.

## Overall

| | strong | adequate | needs-work |
|---|---|---|---|
| All 51 skills | 13 | 37 | 1 |
| 26 core skills | 6 | 20 | 0 |

## Measured facts

| Fact (source key) | Result |
|---|---|
| F1 name valid (AS, AB) | 51 of 51 |
| F2 description non-empty, at most 1024 characters (AB, AS) | 51 of 51; longest 957 |
| F3 body under 500 lines (AB, AS) | 51 of 51; longest 488 lines |
| F4 body under about 5,000 tokens, estimated (AS) | 50 of 51; over: ops-dashboard-engine |
| F5 references one level deep (AB, AS) | 41 of 51; nested links in: bc-cost, bc-portfolio, catalog-compatibility, deploy-cybersec, deploy-project-order, dept-context-freshness, dept-plant-onboarding, dept-retro, dept-risk, know-training |
| F6 long references have a table of contents (AB) | 18 of 51 |
| F7 forward slashes only (AB) | 51 of 51 |
| F9 evaluations exist (AB, AE) | 0 of 51 |

## Criteria across all skills

| Criterion | meets | partly | gap | n/a |
|---|---|---|---|---|
| J1 Description says what and when | 28 | 23 | 0 | 0 |
| J2 Description: one point of view, user intent | 33 | 18 | 0 | 0 |
| J3 Concise: only what the agent lacks | 11 | 40 | 0 | 0 |
| J4 Specificity matches fragility | 50 | 0 | 1 | 0 |
| J5 Procedures over declarations | 44 | 7 | 0 | 0 |
| J6 Defaults, not menus | 45 | 6 | 0 | 0 |
| J7 Gotchas in SKILL.md | 43 | 8 | 0 | 0 |
| J8 Output templates | 49 | 1 | 1 | 0 |
| J9 Concrete examples | 22 | 15 | 14 | 0 |
| J10 Checklist, validation loop, plan-validate-execute | 34 | 17 | 0 | 0 |
| J11 Progressive disclosure: says when to read what | 28 | 22 | 1 | 0 |
| J12 Consistent terminology | 12 | 39 | 0 | 0 |
| J13 Explains the why | 33 | 18 | 0 | 0 |
| J14 Scripts solve, handle errors, state dependencies | 6 | 7 | 1 | 37 |
| J15 One coherent unit | 31 | 20 | 0 | 0 |
| J16 Grounded in real expertise | 29 | 21 | 1 | 0 |

Where most skills fall short, by gaps first: J9 Concrete examples (14 gap, 15 partly); J3 Concise: only what the agent lacks (0 gap, 40 partly); J12 Consistent terminology (0 gap, 39 partly); J11 Progressive disclosure: says when to read what (1 gap, 22 partly); J1 Description says what and when (0 gap, 23 partly).

## Per skill, next to the SkillEvaluator rating

The SkillEvaluator rating checks a fixed set of rules and headings (the registry's configuration); this review judges the text against the published practices. They measure different things.

| Skill | Library | Review | Gaps | Partly | SkillEvaluator | Description chars | Body lines | Evals |
|---|---|---|---|---|---|---|---|---|
| [`bc-assess`](#bc-assess) | core | adequate | 1 | 6 | A 96.5 | 172 | 96 | no |
| [`bc-build`](#bc-build) | core | adequate | 0 | 7 | A 90.5 | 196 | 179 | no |
| [`bc-capital-request`](#bc-capital-request) | core | adequate | 0 | 6 | A 96.5 | 174 | 145 | no |
| [`bc-cost`](#bc-cost) | extension | adequate | 1 | 8 | B 84.0 | 957 | 104 | no |
| [`bc-portfolio`](#bc-portfolio) | extension | adequate | 1 | 4 | B 84.0 | 699 | 126 | no |
| [`catalog-compatibility`](#catalog-compatibility) | extension | adequate | 1 | 4 | B 80.2 | 665 | 101 | no |
| [`catalog-guardrails`](#catalog-guardrails) | core | adequate | 0 | 7 | A 96.5 | 183 | 96 | no |
| [`catalog-standardization`](#catalog-standardization) | extension | adequate | 1 | 7 | B 82.2 | 753 | 117 | no |
| [`catalog-systems`](#catalog-systems) | core | adequate | 0 | 9 | A 96.5 | 198 | 89 | no |
| [`catalog-template`](#catalog-template) | extension | strong | 1 | 2 | B 85.5 | 619 | 115 | no |
| [`catalog-usecase`](#catalog-usecase) | core | adequate | 0 | 8 | A 96.5 | 196 | 144 | no |
| [`comms-brief`](#comms-brief) | core | strong | 0 | 4 | A 94.0 | 190 | 104 | no |
| [`comms-followup`](#comms-followup) | core | adequate | 0 | 4 | A 94.0 | 193 | 85 | no |
| [`comms-showcase`](#comms-showcase) | core | adequate | 0 | 5 | A 96.5 | 151 | 86 | no |
| [`deploy-acceptance`](#deploy-acceptance) | core | strong | 0 | 3 | A 96.5 | 169 | 118 | no |
| [`deploy-appstore`](#deploy-appstore) | core | adequate | 0 | 8 | A 94.0 | 182 | 116 | no |
| [`deploy-cybersec`](#deploy-cybersec) | extension | adequate | 0 | 6 | B 86.5 | 604 | 119 | no |
| [`deploy-handover`](#deploy-handover) | core | adequate | 0 | 4 | A 96.5 | 192 | 159 | no |
| [`deploy-migration`](#deploy-migration) | extension | adequate | 1 | 4 | B 85.8 | 670 | 132 | no |
| [`deploy-project-order`](#deploy-project-order) | extension | adequate | 1 | 8 | B 82.8 | 836 | 113 | no |
| [`dept-context`](#dept-context) | core | adequate | 1 | 5 | A 96.5 | 194 | 212 | no |
| [`dept-context-freshness`](#dept-context-freshness) | extension | strong | 0 | 3 | C 77.5 | 590 | 105 | no |
| [`dept-decision-rights`](#dept-decision-rights) | core | adequate | 0 | 3 | A 96.5 | 175 | 142 | no |
| [`dept-governance`](#dept-governance) | extension | adequate | 1 | 5 | B 85.5 | 821 | 92 | no |
| [`dept-intake`](#dept-intake) | core | strong | 0 | 3 | A 96.5 | 179 | 142 | no |
| [`dept-plant-diagnosis`](#dept-plant-diagnosis) | extension | adequate | 0 | 6 | B 87.8 | 752 | 142 | no |
| [`dept-plant-onboarding`](#dept-plant-onboarding) | extension | adequate | 1 | 8 | B 81.5 | 647 | 98 | no |
| [`dept-retro`](#dept-retro) | extension | strong | 0 | 4 | B 81.8 | 584 | 104 | no |
| [`dept-risk`](#dept-risk) | extension | strong | 1 | 2 | B 85.2 | 549 | 97 | no |
| [`funnel-evaluation`](#funnel-evaluation) | extension | adequate | 0 | 6 | B 86.5 | 821 | 108 | no |
| [`funnel-features`](#funnel-features) | extension | strong | 0 | 3 | C 77.2 | 564 | 49 | no |
| [`funnel-first-aid`](#funnel-first-aid) | extension | adequate | 0 | 7 | B 86.8 | 793 | 109 | no |
| [`funnel-prototype`](#funnel-prototype) | core | adequate | 0 | 6 | A 96.5 | 174 | 130 | no |
| [`funnel-requirements`](#funnel-requirements) | core | strong | 0 | 5 | A 96.5 | 175 | 130 | no |
| [`funnel-use-case`](#funnel-use-case) | core | adequate | 0 | 4 | A 96.5 | 181 | 190 | no |
| [`funnel-workshop`](#funnel-workshop) | extension | adequate | 0 | 3 | B 85.5 | 645 | 110 | no |
| [`invest-screen`](#invest-screen) | core | adequate | 0 | 5 | A 96.5 | 185 | 169 | no |
| [`know-ai-generation`](#know-ai-generation) | extension | adequate | 1 | 8 | B 82.8 | 762 | 130 | no |
| [`know-sharepoint-export`](#know-sharepoint-export) | extension | strong | 0 | 2 | C 78.5 | 578 | 82 | no |
| [`know-skill-authoring`](#know-skill-authoring) | extension | strong | 0 | 1 | B 87.5 | 733 | 91 | no |
| [`know-training`](#know-training) | extension | adequate | 1 | 4 | B 83.0 | 576 | 103 | no |
| [`metrics-scorecard`](#metrics-scorecard) | extension | adequate | 0 | 7 | B 84.2 | 763 | 115 | no |
| [`mi-data-availability`](#mi-data-availability) | core | strong | 0 | 3 | A 96.5 | 182 | 164 | no |
| [`mi-equipment`](#mi-equipment) | core | adequate | 0 | 6 | A 96.5 | 192 | 161 | no |
| [`mi-flow`](#mi-flow) | core | adequate | 0 | 6 | A 94.2 | 175 | 257 | no |
| [`mi-signals`](#mi-signals) | core | strong | 0 | 4 | A 96.5 | 181 | 127 | no |
| [`ops-analytics-asset`](#ops-analytics-asset) | core | adequate | 0 | 5 | A 96.5 | 181 | 171 | no |
| [`ops-dashboard-datatron`](#ops-dashboard-datatron) | extension | needs-work | 5 | 7 | B 84.2 | 600 | 49 | no |
| [`ops-dashboard-engine`](#ops-dashboard-engine) | core | adequate | 0 | 4 | A 90.5 | 192 | 488 | no |
| [`ops-event-model`](#ops-event-model) | extension | adequate | 0 | 6 | B 86.5 | 746 | 114 | no |
| [`process-derivation`](#process-derivation) | core | adequate | 0 | 7 | A 95.2 | 208 | 129 | no |

**Where the two disagree:** `catalog-template` (SkillEvaluator B, review strong), `dept-context-freshness` (SkillEvaluator C, review strong), `dept-retro` (SkillEvaluator B, review strong), `dept-risk` (SkillEvaluator B, review strong), `funnel-features` (SkillEvaluator C, review strong), `know-sharepoint-export` (SkillEvaluator C, review strong), `know-skill-authoring` (SkillEvaluator B, review strong).

## House rules against the published practices

- `bc-assess`: Structure-only SKILL.md keeps the skill short (96 lines) and the criteria table scannable, which helps J3 and J5.
- `bc-assess`: Rationale moved to background.md, but background.md here mostly repeats the outputs table, so the why behind 'C gap blocks signing' is in neither place; this works against J13.
- `bc-assess`: outputs.yaml duplicates the Outputs and Definition of done text in SKILL.md; harmless but redundant.
- `bc-build`: Structure-only rule is only partly applied here: SKILL.md still holds long definitional prose (tracked vs proven, dependencies), so J3 suffers while background.md holds little of the why.
- `bc-build`: The heading 'The references are the substance' sits oddly with the rule that SKILL.md is structure only; the useful reasons (review-checklist) sit in a reference, which helps J11 but hides J13 content.
- `bc-build`: outputs.yaml 'to_roles: then' and 'signoff: then' look like a parsing artefact of the word 'then'.
- `bc-capital-request`: The refusal gate and the outputs.yaml output 'refusal-with-de-risk-questions' make the stop condition explicit, which supports J4 and J10.
- `bc-capital-request`: The structure-only rule is not fully applied: the 'The form and the builder' paragraph is narrative, hurting J3.
- `bc-capital-request`: outputs.yaml done_when per output helps J5, but the 'Still not in the sources' open items live in SKILL.md, not background.md.
- `bc-cost`: Moving rationale to background.md helped less than expected: Plan-row and skill-map notes remain in SKILL.md (J3).
- `bc-cost`: outputs.yaml gives five outputs with done_when, which compensates for the missing example in J8 but not J9.
- `bc-cost`: The still-open list is honest (supports J16) but is itself in SKILL.md rather than background.
- `bc-portfolio`: The no-counts, read-live rule suits the structure-only SKILL.md and avoids stale figures (helps J16).
- `bc-portfolio`: Absorbing od-use-case-prioritization kept its folder under references/, which creates nested reference links and hurts J11 and J15.
- `bc-portfolio`: Even with rationale moved out, reasons stay in SKILL.md here, so J13 still meets.
- `catalog-compatibility`: Rationale was supposed to move to background.md, but Why a check is needed stays in SKILL.md; it does explain the why (J13) while costing J3.
- `catalog-compatibility`: outputs.yaml done_when lines (unknown never rounded to consumable) reinforce J4 and J13.
- `catalog-compatibility`: Draft status and to-confirm placeholders in the skill are honest but limit J16.
- `catalog-guardrails`: Structure-only rule suits a checklist skill: the guardrail table is the core and stays in SKILL.md (helps J5, J10).
- `catalog-guardrails`: Moving rationale to background.md left only a one-paragraph 'If it fails' note there, so the why behind each guardrail is recorded nowhere (works against J13).
- `catalog-guardrails`: outputs.yaml 'to_roles: or / then' fragments look like parsing artefacts.
- `catalog-standardization`: Structure-only SKILL.md should have pushed the explanatory portfolio findings to background.md, but they remain in the body (J3).
- `catalog-standardization`: Moving substance to references works for J16 (clusters.md carries sources) but puts the working detail one file away from the procedure (J11).
- `catalog-systems`: Structure-only SKILL.md helps J3 and J5 (procedure and Do-not lists are lean) but moves the reason for each gate to background.md, which works against J13.
- `catalog-systems`: The outputs.yaml contract gives a clear done-when for J10, but the SKILL.md itself contains no validation step.
- `catalog-template`: The structure-only rule helps J5 and J4 (table and numbered steps) but excludes worked examples that would help J9.
- `catalog-template`: The outputs.yaml and the resolution record template give a firm done-when.
- `catalog-usecase`: Moving rationale to background.md leaves SKILL.md lean for J3, but the leftover split text shows structure-only rules do not prevent stale content.
- `catalog-usecase`: outputs.yaml gives a precise done-when for the match record, which supports J10 and J8.
- `comms-brief`: The house rule of an outputs.yaml with a runnable check command (check.cmd) fits J10 well: the validation loop is part of the contract.
- `comms-brief`: Moving rationale to background.md leaves J13 thin in SKILL.md; the reasons for the evidence classes are not stated there.
- `comms-brief`: The 40-word list-item cap shows in dense step 3.
- `comms-followup`: Moving rationale to background.md helps J3 (short body) but the closing-check rule ended up in background.md, away from J10.
- `comms-followup`: The one-log-per-story outputs.yaml contract keeps J8 concrete.
- `comms-showcase`: Structure-only SKILL.md keeps it short, but the rule 'rationale lives in background.md' leaves the why of gates 4 to 6 unstated where it would change behaviour (J13).
- `comms-showcase`: outputs.yaml duplicates the done criteria of the gate, which helps J10 verifiability.
- `deploy-acceptance`: Moving context to background.md keeps SKILL.md procedural (helps J5), but the 'references are the substance' table means most content sits one hop away, so J3 depends on the agent opening them.
- `deploy-acceptance`: outputs.yaml makes the sign-off rule checkable (helps J10).
- `deploy-appstore`: Structure-only SKILL.md left bare 'to be supplied' markers where the moved rationale would have helped J13.
- `deploy-appstore`: outputs.yaml stop condition mirrors the release gate, which supports J10.
- `deploy-cybersec`: The 'draft, standard not collected' status is stated openly in SKILL.md, which fits the registry honesty rules and supports J16.
- `deploy-cybersec`: Moving rationale to background.md keeps the body procedural, yet the many placeholders show what the sources could not supply.
- `deploy-handover`: Absorbing od-impact-evaluation and od-utilization-review as nested references keeps the body short but makes the skill broad (J15).
- `deploy-handover`: The structure-only rule is not followed for the survey statistic and the function-handover essay, which are context (J3).
- `deploy-handover`: Run record and outputs.yaml enforce the DONE-versus-adopted distinction (helps J10).
- `deploy-migration`: Provenance and PROPOSAL marking are stated openly, which fits the honesty rules but pushes uncertainty into the body (J16).
- `deploy-migration`: The structure-only rule is only partly met: Questions to ask and Provenance are context that background.md could hold (J3).
- `deploy-project-order`: Moving rationale and the small-change rule to background.md left step 1 pointing at a rule that is no longer in SKILL.md (works against J11 and J5).
- `deploy-project-order`: The assets template plus outputs.yaml done_when list give a concrete output contract and a pre-send check (helps J8 and J10).
- `deploy-project-order`: Rationale moved out leaves the Do-not rules without reasons (works against J13).
- `dept-context`: Structure-only SKILL.md still carries about 4,200 tokens of tables, close to the F4 limit (works against J3).
- `dept-context`: The outputs.yaml output contract names chat replies as outputs but gives no format (leaves J8 thin).
- `dept-context`: The shared 10-line Run record section repeats in every skill and adds weight here (works against J3).
- `dept-context-freshness`: outputs.yaml done_when plus the hygiene-report template turn the report into a checkable output (helps J8 and J10).
- `dept-context-freshness`: Moving rationale to background.md kept SKILL.md small (about 2,000 tokens) while the central rule of dates stayed in SKILL.md (neutral for J13).
- `dept-decision-rights`: Moving rationale to background.md leaves the heading 'The references are the substance' with only a table in SKILL.md (works against J13 and J11).
- `dept-decision-rights`: outputs.yaml lists the deciding roles by splitting a comma-list, so the sign-off reads 'The deciding role named in the table (for example DBVE' (a data defect in the contract).
- `dept-decision-rights`: The decision-request template makes the output checkable (helps J8 and J10).
- `dept-governance`: Rationale moved to background.md leaves the five decision rules as bare directives (works against J13).
- `dept-governance`: outputs.yaml sign-off fields are truncated by comma splitting ('OD lead (approves'), weakening the output contract.

## The skills

### bc-assess

**adequate**: A clear, well-bounded scoring skill with a worked example and a human gate, but its deck script is a hard-coded one-off, the criteria count is inconsistent and it has no evals. (1 gap, 6 partly; core library)

Improve first:
1. Rewrite scripts/build_bc_short.py as a parameterised tool (args, template check, valid colours) or drop it from the skill.
2. Reconcile D1-D8 vs D1-D9 and the pass/partial/gap vs verdict vocabulary across SKILL.md and criteria-checklist.md.
3. Add a pitfalls list and a short reason for why a C gap blocks signing.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md: "Score a business case against the OD house rubric and return a pass/partial/gap verdict per criterion before a capital request." | Add the trigger words a user would say (signable, maturity gate, compare two cases) to the description. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "The rubric below is the department package's own (`30-skills/bc-assessment.zip`, transcribed into `references/`); the package stays the master." | Move provenance remarks about the source zip out of the SKILL.md body into background.md. |
| J7 Gotchas in SKILL.md | partly | SKILL.md: "Do not fix the case while assessing it; return it to `bc-build` with the findings." | Add a pitfalls list of typical scoring errors (passing an untagged figure, scoring from the summary instead of the inputs) with the reason for each. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md: "run and QA loop in `build-engine.md`" | Add a pre-verdict check (every criterion scored, every score has file and section) so the report itself has a validation step, not only the deck. |
| J12 Consistent terminology | partly | references/criteria-checklist.md: "deck-renderable structure D1-D8" | Reconcile the rubric size: SKILL.md lists D1-D9, the checklist description says D1-D8; also use pass/partial/gap for criteria and Ready to sign only for the gate. |
| J13 Explains the why | partly | SKILL.md: "Governance stays separate from build" | Say why a C gap blocks signing and why the builder may not assess (unsupported figures reach approvers), not only that they do. |
| J14 Scripts solve, handle errors, state dependencies | gap | build_bc_short.py: SRC = '/sessions/awesome-vigilant-hopper/mnt/outputs/_nw_template.pptx' (hard-coded session path, no arguments, no help, no check that the template exists; DEEP is set to the placeholder '<n>' which is not a valid colour; content is the Gemba case) | Take template and output paths as arguments, check the template exists with a clear message, fix the DEEP colour value and read case content from the backbone instead of hard-coding Gemba. |

Facts: No evals (F9 false).; worked-example-gemba.md is 108 lines without a table of contents (F6).; Date 2026-09-11 in body is an OD x IT rule reference, not time-sensitive guidance.; Script has no argument parsing, help or exit codes (F8).

### bc-build

**adequate**: Strong on honesty rules, concrete arithmetic and reasons, but it carries two overlapping procedures, vocabulary drift and steps that belong to neighbouring skills. (0 gap, 7 partly; core library)

Improve first:
1. Merge the five-step estimate and the 0-9 Procedure into one default flow and drop steps 5-6 that belong to other skills.
2. Unify bankable/assumed/assumption-dependent terminology and remove the duplicated governance-gate sentence.
3. Add TOCs to the long references and phrase the reference table as read-when.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md: "Build the value side of an OD business case and keep the savings ledger honest: grounded figures, bankable vs assumed value, saving rows." | Add an explicit Use when clause (a use case is prioritized and needs a business case, a saving must be recorded or defended). |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Two of the values are governance gates and one is machine integration." | Delete the duplicated sentence about governance gates and move the long definitions of tracked, proven and dependencies to background.md. |
| J6 Defaults, not menus | partly | SKILL.md: "First estimate in five steps (for anybody with an idea)" | Name one default path: the five-step estimate and the 0-9 Procedure overlap, so say when to use which. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md: "Assess before it goes on" | Add a fix-and-recheck loop: until every figure is tagged and every row has methodology or an ESTIMATION label, do not hand to bc-assess. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md: "Why the methodology field is usually the one missing, the three fixes tried before the current one, and the smell test that follows from it" | Phrase the reference table as read X when Y and add a table of contents to the four references over 100 lines. |
| J12 Consistent terminology | partly | SKILL.md: "bankable vs assumed value" | Use one term pair throughout (bankable vs assumption-dependent, or banked vs de-banked) instead of mixing bankable, assumed, assumption-dependent and banked. |
| J15 One coherent unit | partly | SKILL.md: "Route the spend through eCR; the approver for the amount follows the current approval" | Move prioritization (step 5) and eCR routing (step 6) to bc-portfolio and bc-capital-request and keep this skill on value and the ledger. |

Facts: No evals (F9 false).; Four references over 100 lines have no TOC: deck-structure, funnel-business-case, process-chain-practice, savings-model (F6).; Body 179 lines, about 3,144 tokens: within limits.; Date 2026-09-11 in body is a rule reference.

### bc-capital-request

**adequate**: The most complete of the batch (refusal gate, template, example, scripts, recorded approval matrix) but SKILL.md carries narrative, inconsistent step numbers and a cost-side overlap with bc-cost. (0 gap, 6 partly; core library)

Improve first:
1. Clean the numbering and the stale bc-cost note, and move transcription and where-it-sits prose to background.md.
2. Make build_ecr.py consistent with its docs (template path, errors, input file) and add a dependency check to render_qa.sh.
3. Delegate the cost section to bc-cost so there is one cost definition.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md: "Package a use case's value and cost into a capital request (eCR) for human approvers: spend gate, evidence, options, risks." | Add Use when triggers (a Lane 2 use case needs investment; a saving waits on ECR CREATION or ECR APPROVAL) to the description. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Still not in the sources: the system the eCR is filed in, who files it, how long approval takes." | Move the transcription notes, the Where it sits section and the open-source remarks to background.md and fix the stale 'bc-cost (planned)' line. |
| J12 Consistent terminology | partly | SKILL.md: "Lane 2, step 5" | Use one step numbering (the skill says Lane 2 step 5, background says step 25 and 26) and drop the stale 'bc-cost (planned)' wording; the numbered list also has stray '1b.' and '10b.' fragments. |
| J13 Explains the why | partly | SKILL.md: "do not print NPV or IRR when no measured baseline exists; fund the baseline first." | Add a short because-clause to the other Do-not rules (why offer, eCR and contract must agree; why no splitting). |
| J14 Scripts solve, handle errors, state dependencies | partly | build_ecr.py: SRC = os.path.join(HERE, '_nw_template.pptx') (docstring and SKILL.md say the template is in assets/; no CLI arguments, case edited inside the file); render_qa.sh has a usage line and set -euo pipefail | Reconcile the template location with the docs, add a clear error when the template is missing and let the script read the CASE from a JSON path argument; render_qa.sh does not check that soffice and pdftoppm exist. |
| J15 One coherent unit | partly | SKILL.md: "`bc-build` is thin on cost (the conformance page notes it once); this section is where the cost side lives." | Point step 6 at bc-cost's investment estimate instead of re-defining the cost side here. |

Facts: No evals (F9 false).; Three references over 100 lines without TOC: business-case-structure, ecr-builder-workflow, process-chain-practice (F6).; 13 reference files; none nest further (no nested links).; build_ecr.py has no arg parsing or --help (F8).

### bc-cost

**adequate**: Careful and honest about open figures, but the description is bloated, there is no example, and three different products share one skill with a still-unconfirmed template. (1 gap, 8 partly; extension library)

Improve first:
1. Shorten the description to the user need and add a router for wave pack vs Lane 1b template vs single-case estimate.
2. Add one fictional example cost table.
3. Move skill-map and where-it-sits notes to background.md and unify the pack/estimate naming.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | SKILL.md: "Covers the cost template for a standardized system (Lane 1b), the wave pack after an" | Rewrite the 957-character description around the user's need and drop internal lane and step numbers and the self-reference to the department's bc-cost. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "The Skill Map lists "digitalization investment approval" under *explicitly not skills*" | Move the Plan row II-07 and Skill Map notes and the Where it sits table to background.md. |
| J6 Defaults, not menus | partly | SKILL.md: "For a single use case or system, fill `assets/investment-estimate.md`:" | State a default output: three forms (wave pack, Lane 1b template, estimate) are presented side by side; add a router saying which to produce when. |
| J9 Concrete examples | gap | absent: no Example section or sample cost row in SKILL.md; checked the whole file and outputs.yaml | Add a short fictional cost-line table (line, figure, tag, source) as an example. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md: "Cost cannot be planned for a scope that is still moving; if scope is open, stop and say which part." | Add a pre-handover check against the done_when items (every line has a figure and source or open marker, gates named) before step 9. |
| J12 Consistent terminology | partly | SKILL.md: "Investment input pack" | Pick one name for the deliverable: the skill is bc-cost, its title is Investment input pack, and it also produces an investment estimate, wave pack and cost template. |
| J13 Explains the why | partly | SKILL.md: "Do not price a return before a baseline exists; the first line is the measurement layer." | Add reasons for the other Do-nots, e.g. why internal effort is not priced unless the OD lead says so. |
| J15 One coherent unit | partly | SKILL.md: "/ **Lane 1b** / Fill cost template and lightweight approval" | Separate or clearly route the three products (integration wave pack, Lane 1b template, single-case estimate for the capital request) so one invocation has one job. |
| J16 Grounded in real expertise | partly | SKILL.md: "Confirmed template" | Obtain the confirmed template and real unit costs from IIAE quotes; the skill currently lists unit costs, thresholds and the template as open. |

Facts: No evals (F9 false).; Description is 957 characters, close to the 1024 limit (F2).; Nested reference link: process-chain-practice.md -> cost-lines.md (F5 breach).; process-chain-practice.md is 108 lines without TOC (F6).; allowed-tools is 'Read Grep Glob' only, yet the skill fills asset files; no write tool listed.

### bc-portfolio

**adequate**: Excellent on pitfalls and reasoning, but it has no example and bundles two jobs, with a nested sub-skill folder behind the absorbed section. (1 gap, 4 partly; extension library)

Improve first:
1. Add a worked example of a dated, denominated, labelled portfolio read.
2. Separate the prioritization job (own trigger or skill) from the portfolio-read job.
3. Move standing findings and shape commentary to background.md and add a pre-publication check.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | SKILL.md: "Also ranks competing candidate use cases for a plant or region into a prioritization record (formerly od-use-case-prioritization)." | Drop the legacy-name aside and the without-being-wrong framing; state user intent only. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Pattern to expect: the tracker was actively maintained for a period and then largely abandoned" | Move narrative standing findings and regional commentary to background.md and keep only the checks the agent must run. |
| J9 Concrete examples | gap | absent: no Example section or worked read in SKILL.md; only a status table; checked the whole file | Add a fictional mini-read showing capture date, denominator, tracked vs proven label and a blank field stated as unknown. |
| J10 Checklist, validation loop, plan-validate-execute | partly | outputs.yaml: "Denominator on every rate" | Add a pre-publication check (date, denominator, tracked/proven label, unknown vs nil) as a numbered gate before step 7. |
| J15 One coherent unit | partly | SKILL.md: "It keeps its own references and assets under that folder and the authority it had." | Split use-case prioritization back into its own skill or give it a clearly separate trigger; two jobs share one description. |

Facts: No evals (F9 false).; Description 699 characters, fine but long.; Nested links: process-chain-practice.md -> prioritization.md and rollup-method.md (F5).; Deep sub-folder references/od-use-case-prioritization with its own references and assets.

### catalog-compatibility

**adequate**: A tightly scoped, well-reasoned check with a clear decision table, but it lacks an example, keeps rationale in SKILL.md and rests on partly unrecorded source data. (1 gap, 4 partly; extension library)

Improve first:
1. Add a worked three-plant example grid.
2. Move the Why a check is needed rationale to background.md and add a completion check for the verdicts.
3. Fill the open evidence items (consumer inventory, tag language) from a real run.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Plan item P-08 of the department's skill map." | Move the Why a check is needed section and the plan-item and decision-rights preamble into background.md; plant-fact claims there go stale. |
| J9 Concrete examples | gap | absent: no Example section or sample grid row in SKILL.md; checked the whole file | Add a fictional three-plant grid row with verdicts including one consumable with mapping and one unknown. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md: "Refresh any figure from the live lists (Machine List, Tool Overview) if you rely on it for a verdict" | Add a completion check (every plant in scope has exactly one of the four verdicts) before step 7. |
| J12 Consistent terminology | partly | SKILL.md: "Each of the eleven cross-plant capability templates has an instance at" | Define standard under test once (signal set, data model, flow, dashboard, library entry are all called the standard) and align the eleven templates with catalog-standardization's C01-C12. |
| J16 Grounded in real expertise | partly | SKILL.md: "is recorded nowhere as a field; infer from the signal list with `mi-signals`." | Run it against one real signal standard and replace the to-collect items (consumer inventory, COP lead time) with sourced facts. |

Facts: No evals (F9 false).; Nested reference link: compatibility-tests.md -> plant-differences.md (F5).; allowed-tools is 'Read Grep Glob' only although the skill produces a filled check file.; Body 101 lines, about 2,043 tokens: within limits.

### catalog-guardrails

**adequate**: A usable, concretely exemplified checklist skill, but half of its guardrails are unconfirmed candidates, the G-range is inconsistent and reasons are thin. (0 gap, 7 partly; core library)

Improve first:
1. Get the OD lead to confirm or remove G8-G19 and P1-P7 and align the range (G18 vs G19).
2. Add a fix-and-recheck step and a clear open-technical-guardrails-when trigger.
3. Add a one-clause reason to each guardrail and trim the new-state preamble.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md: "Run the go-live self-check and technology guardrails on a use case a plant applied itself (Lane 1)." | Add trigger phrases to the description (a plant wants to go live, a new guardrail is proposed, steps 1a3 and 1b4 in plain words). |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "The nearest existing skill is `deploy-handover`, run by OD; Part C is the plant-run version of the part that can be." | Delete the background paragraph on the new state and the seeded-guardrail history; move it to background.md. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md: "All passed - report it." | Add the re-run step: after a failed guardrail is fixed, repeat the check until every guardrail passes or is marked not applicable. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md: "Do one deep dive against the paper process before declaring the screen live" | Say when to open references/technical-guardrails.md (when a plant built the screen itself) and fix the Part C link, which points into another skill and has a stray bracket. |
| J12 Consistent terminology | partly | references/technical-guardrails.md: "Candidate guardrails G8 to G18" | Align the range: SKILL.md says G8 to G19, the reference says G8 to G18; also use go-live check, self-check and guardrails consistently. |
| J13 Explains the why | partly | SKILL.md: "Self-service stays inside pre-approved guardrails; anything outside them is not self-service." | Give each guardrail in the table a one-clause reason (what goes wrong without it), not only the failure routing. |
| J16 Grounded in real expertise | partly | SKILL.md: "the OD lead has not confirmed them." | Have the OD lead confirm or drop the candidate guardrails G8-G19 and P1-P7, which come from AI-drafted specs. |

Facts: No evals (F9 false).; Description 183 characters: short, no trigger phrases.; Body 96 lines, about 1,774 tokens; four reference files, no nesting.; No scripts folder (J14 n/a).

### catalog-standardization

**adequate**: Substantive and well sourced, but it reads as a declaration, has no example, mixes two jobs and leaves the classifier it relies on unspecified. (1 gap, 7 partly; extension library)

Improve first:
1. Add a worked example and turn sections 1 to 3 into steps with named inputs and outputs.
2. Locate or ship the cluster classifier (script or documented command) and say how to run it.
3. Separate promotion of an ad-hoc asset from standardization or give it its own trigger.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | SKILL.md states findings the agent need not be told: «the catalogue is built to standardize and has not scaled.» | Move portfolio findings and the C12 commentary to background.md and keep only instructions. |
| J5 Procedures over declarations | partly | SKILL.md sections 1 to 3 are declarations; the Procedure has only six short steps starting «Before specifying anything» | Expand the procedure so each step names the input, the file to open and the output field, and shrink the declarative sections. |
| J7 Gotchas in SKILL.md | partly | SKILL.md Do not: «Do not treat a `No` at the CSP gate as a rejection of the use case» | Add a gotchas list with the cause and effect (blank CSP read as No, C12 growth read as idiosyncrasy, deployment count read as adoption). |
| J9 Concrete examples | gap | absent: SKILL.md has no Example section or worked case (read the whole body). | Add one worked example from a use case to the review with placement, cluster tag and CSP verdict. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md step 5: «methods and actions written down, evidence it works at its first plant.» | Add a checklist before the CSP-readiness verdict listing the evidence that must exist. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md: «The references are the substance» with a table, but four promotion files sit in nested folders and clusters.md (306 lines) has no TOC. | Add a TOC to clusters.md and process-family-patterns.md and state in the procedure when to open each file. |
| J12 Consistent terminology | partly | SKILL.md uses «capability», «template», «cluster», «library entry» and «standard use case» together, and both catalogue and catalog. | Define each term once in a short glossary line and keep to one spelling. |
| J15 One coherent unit | partly | SKILL.md: «Absorbed: Promote a recurring ad-hoc asset into a standard use case (formerly od-use-case-promotion)» | Split promotion back into its own skill or give it a clear trigger; two jobs in one skill hurts precise activation. |

Facts: No evals (F9 false).; Description is 753 characters, long but within 1024.; clusters.md (306 lines) and process-family-patterns.md (114 lines) lack a TOC (F6).; Promotion files live in references/od-use-case-promotion/..., deeper than references/, though not flagged as nested links.

### catalog-systems

**adequate**: Clear single-purpose procedure with a good template and refusal rules, but repetitive, with broken references and thin examples and gotchas. (0 gap, 9 partly; core library)

Improve first:
1. Fix and consolidate references (decision-paths.md, ../catalog-usecase links with stray parentheses) and give each a read-when trigger.
2. Cut duplicated Purpose/Inputs/Pick text and unify the term for standardized system.
3. Add a 'no standard system' example and a gotchas list.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md description: «Match a catalogued use case to a standard system or connection kit a plant can order itself (Lane 1b)» | Add an explicit 'Use when a plant wants a catalogued use case on a machine that is not connected yet' trigger to the description (it exists only in the body). |
| J3 Concise: only what the agent lacks | partly | SKILL.md repeats the gate in Purpose, Inputs and Pick sections: «Only standardized systems qualify for 1b; anything non-standard goes to Lane 3.» | Say the 1b/Lane 3 rule once and delete the duplicated Purpose/Inputs/Pick bullets. |
| J7 Gotchas in SKILL.md | partly | SKILL.md Do not: «Do not offer a system that is not standardized; route it to Lane 3.» | Add a short Gotchas list (heavy request disguised as a dashboard, TODO or stub route read as standard, kit price from memory) with the failure each causes. |
| J9 Concrete examples | partly | SKILL.md Example: «kit "see kit list" (price and lead time: <missing>); Cyber Security status open;» | Add a second example for the 'no standard system' outcome (route TODO, hand to invest-screen and Lane 3). |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md Definition of done: «every field set or marked missing» | Add a pre-handoff check (all fields set or marked missing, route class A confirmed, tool boundary tested) before the record goes to dept-decision-rights. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md steps cite «`decision-paths.md`» which is not in this skill's references, and cross-links use ../catalog-usecase paths with a stray ')'. | Make the reference table name each file with a 'read when' trigger, fix the broken paths and point step 3 at validated-routes.md. |
| J12 Consistent terminology | partly | SKILL.md mixes «standard system», «standardized system», «route candidate» and «kit» for the thing being matched. | Pick one term (standardized system) and define route candidate and kit once against it. |
| J13 Explains the why | partly | SKILL.md: «Operations-concept gate:» a tool without a named operations owner, service and support level is not matched for rollout. | Add the one-clause reason for each gate (e.g. why a TODO or stub route is not a standard system) next to the rule. |
| J16 Grounded in real expertise | partly | SKILL.md: route candidates are «written in full and proven in at least two plants»; none «has a kit, price or lead time on record». | State which validated-routes entries rest on a real kit list so the match is not a scaffold; none exists in the sources yet. |

Facts: No evals (F9 false).; Six reference files, no nested reference links, body about 1750 tokens.; Description is only 198 characters and has no 'Use when' clause.

### catalog-template

**strong**: A tight lookup skill with a decision table, leak check and clear refusal rules; missing only a worked example and consistent terminology. (1 gap, 2 partly; extension library)

Improve first:
1. Add a worked example of a resolution record.
2. Update the 'planned' mentions (deploy-cybersec, dept-context-freshness), which now exist, or move them out of the body.
3. Add a TOC to master-register.md (102 lines).

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | SKILL.md includes status-like content: «Kinds of gap to expect» listing which register rows have been gaps. | Move the gap-pattern list to background.md; the live register already says which rows are open. |
| J9 Concrete examples | gap | absent: SKILL.md has no worked example (read all sections). | Add one example resolving a business case to its register row and one of the four outcomes. |
| J12 Consistent terminology | partly | SKILL.md uses «artefact» and «deliverable», and «master», «template» and «standard» for the same thing. | Define master versus template and use deliverable throughout. |

Facts: No evals (F9 false).; master-register.md (102 lines) has no TOC (F6).; SKILL.md frontmatter includes allowed-tools; description 619 characters.; Body mentions deploy-cybersec and dept-context-freshness as planned, which may be out of date.

### catalog-usecase

**adequate**: Sound routing logic with strong honesty rules, but it carries stale Part B/C remnants after the split, misdirected references and a single fall-through example. (0 gap, 8 partly; core library)

Improve first:
1. Remove the leftovers of the split (title, Part B/C, systems and guardrail references, status paragraph).
2. Add examples of a catalogued match and a graduation.
3. Fix the broken ../catalog-systems reference links.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md description: «Match a plant request to a proven catalogued use case (Lane 1), or say it is not catalogued and route it to Lane 2/3» | Add concrete trigger phrases (a plant asks for something another plant already has; a Lane 2 result should graduate) to the description. |
| J3 Concise: only what the agent lacks | partly | SKILL.md still carries split-off content: «Split into their own department skills (2026-11-10)» | Delete Part B/C remnants, the 'Merged from' line and the status paragraph so only match and graduation remain. |
| J9 Concrete examples | partly | SKILL.md Example: «Request : "show scrap per shift on line X" (fictional)» | Add an example of a successful catalogued match and one graduation proposal, not only the fall-through case. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md reference table cites «`references/validated-routes.md`](../catalog-systems/references/validated-routes.md))» and other files that belong to split-off skills. | Remove references to catalog-systems and catalog-guardrails files, fix the broken links and keep only those that serve matching and graduation. |
| J12 Consistent terminology | partly | SKILL.md title «Catalog: use cases, standard systems, go-live guardrails» but the body now covers only use cases; 'catalogue' and 'catalog' both occur. | Retitle to the use-case match and graduation and use one spelling. |
| J13 Explains the why | partly | SKILL.md: «A "Yes" without evidence counts as "not checked".» | Add the reason where it changes behaviour (why a Yes needs a source and read date; why a prototype is only a candidate). |
| J15 One coherent unit | partly | SKILL.md: «This skill keeps the catalog of use cases and the graduation into it.» yet the references table still lists system and guardrail material. | Finish the split: move system and guardrail references out so the skill is only match plus graduation. |
| J16 Grounded in real expertise | partly | SKILL.md: «No catalog data set, kit list (kits, prices, lead times) or finished guardrail set exists in the sources.» | Mark which of the four conditions are sourced and which are still proposals, and cite where each is read live. |

Facts: No evals (F9 false).; Ten reference files; process-chain-practice.md (256 lines) and template-coverage.md (102 lines) have no TOC (F6).; A date in the body (2026-11-10) is the split note; time-sensitive text.; Several links point into other skills' folders (catalog-systems, catalog-guardrails).

### comms-brief

**strong**: Clear Lane 4 procedure with a script-backed validation loop, template, pitfalls and honest open points; small gaps in terminology and script error handling. (0 gap, 4 partly; core library)

Improve first:
1. Make the script robust (missing file, --help) and state its Python/stdlib prerequisite in SKILL.md.
2. Add the reason behind the evidence-class rules in one line each.
3. Replace the open Internal Communications points with the real intake once available.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J12 Consistent terminology | partly | SKILL.md uses «brief», «draft pack», «drafts», «story» and «assets» for overlapping things. | Define brief (the hand-over) and drafts (optional help) once and use only those words. |
| J13 Explains the why | partly | SKILL.md step 2: «A saving is a result only with a registered plant savings project and a baseline» | Add one clause saying why (an unregistered saving is a claim IC cannot defend) next to the evidence-class rules. |
| J14 Scripts solve, handle errors, state dependencies | partly | scripts/check_comms_brief.py main: «findings = analyze(open(argv[1], encoding="utf-8").read())» with no handling of a missing or unreadable file. | Catch OSError in main and print a one-line message with exit 2, and accept --help explicitly. |
| J16 Grounded in real expertise | partly | SKILL.md Human gate: «IC's own process, templates and lead times are not recorded in the knowledge base.» | Replace the open IC points with the real Internal Communications intake once supplied, and cite it in ic-handover.md. |

Facts: No evals (F9 false).; Script has argument parsing, usage doc and exit codes per facts; a test script is present.; SKILL.md has a stray '- 6a.' fragment after step 8.

### comms-followup

**adequate**: Compact, coherent close-the-loop skill with good routing and pitfalls, but no validation step, a measure set that is only proposed and no evals. (0 gap, 4 partly; core library)

Improve first:
1. Add a closing validation of the log (route and review date per reaction).
2. Trim or relocate the measures table and mark which are measurable today.
3. Unify reaction/request/demand terms.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | SKILL.md has a seven-row measures table: «Measures of the lane (definitions, proposed; no targets)» | Cut the measures table to the few the log actually records, or move it to a reference. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md Definition of done: «every reaction has a route, the answers stay within the story's promise, a review date is set» | Add a closing check in the procedure (each log entry has route and review date) as the background note already says. |
| J12 Consistent terminology | partly | SKILL.md uses «reaction», «request», «demand» and «intake request» for what a plant sends. | Use reaction for the raw input and request for the routed item, and say so once. |
| J16 Grounded in real expertise | partly | SKILL.md: «Measures of the lane (definitions, proposed; no targets)» built on the AMEC framework. | Replace proposed measures with ones tested on at least one real published story and record where they were read. |

Facts: No evals (F9 false).; A date in the body (2026-01-01) is inside a fictional example, not a time-sensitive claim.; One reference file plus the log template; no nested links.

### comms-showcase

**adequate**: Tight, clear gate with verdicts and a template, but the description lacks triggers, examples show only the Go path and no evals exist. (0 gap, 5 partly; core library)

Improve first:
1. Add 'Use when' triggers to the description.
2. Add Hold and No example blocks.
3. Fix the five-versus-six gate count and cite the consent source.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md description: "Decide which use case is ready to be told company-wide and which claims it may carry (Lane 4): go, hold or no." | Add a 'Use when' clause (use case gone productive, someone asks to publicise a result) to the description; it exists only in the Purpose section. |
| J9 Concrete examples | partly | SKILL.md example: "Claim: \"saves 1,000 EUR per year\" - ESTIMATION (fictional figure), no baseline registered -> worded as a claim" | Add a short Hold and a No example next to the Go example so the failure branches are shown. |
| J12 Consistent terminology | partly | references/readiness-gate.md description: "The five gate criteria for telling a use case outwards" vs SKILL.md 'six gate steps' | Make the reference say six gate steps (or state how the five map to the six). |
| J13 Explains the why | partly | SKILL.md: "Implemented is not adopted; a use case with utilization `NEVER` is not a story yet." Reason given for gate 1 only. | Add one-line reasons for the sensitivity screen and the people-content step, where an agent may be tempted to skip them. |
| J16 Grounded in real expertise | partly | SKILL.md: "A balancing of interests lists the employer's reasons, the employees' counter-reasons and the weighing"; no source named in SKILL.md. | Name the source of the consent and balancing-of-interests rule (policy or legal basis) in readiness-gate.md. |

Facts: No evals (F9).; No scripts, so J14 is n/a.; Body about 1,342 tokens; no nested reference links.

### deploy-acceptance

**strong**: A clear procedure with a protocol template, a strong human-only gate, rework routing and good references, held back by a trigger-less description and no evals. (0 gap, 3 partly; core library)

Improve first:
1. Add a 'Use when' clause to the description.
2. Unify lane vocabulary in the rework table.
3. Add tables of contents to the four long references.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md description: "Author and run the acceptance test that closes an integration or delivered solution; route failures into rework." | Add a 'Use when' clause with user keywords (FAT, SAT, UAT, ready to be declared done); it sits only in the Purpose section. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Acceptance is the gate between \"we built it\" and \"it is yours\"." Also an aside that the protocol is 'the source system rather than a separate tool'. | Drop the aside on the protocol as source system; it changes no action. |
| J12 Consistent terminology | partly | SKILL.md: "Integration fails acceptance (Information Integration lane)" while metadata uses "Lane 3a (3a5), Lane 3b (3b6)" | Use one lane vocabulary (Lane 3a/3b or the playbook names) in the rework table. |

Facts: No evals (F9).; Four reference files over 100 lines without table of contents (F6).; No scripts; J14 n/a.; Body about 1,886 tokens.

### deploy-appstore

**adequate**: Sound gate and package with a firm human sign-off boundary, but a terminology contradiction, unfilled placeholders and a build-pattern reference outside scope weaken it. (0 gap, 8 partly; core library)

Improve first:
1. Resolve the platform and edge-runtime contradiction.
2. Fill or link the placeholders (containerization, lead time).
3. Trim repeats and move microservice-app-pattern.md out.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md description: "Prepare and gate deployment of a manufacturing app (Lane 3a): sourcing route, deployment package, release gate with Cyber Security sign-off" | Add a 'Use when' clause (after the Lane 3 front-end, before rollout); it is only in the Purpose section. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "It does not deploy." appears in Purpose, step 5, Do not and background; long 'Which platform' naming discussion. | Cut the repeated no-deploy statements and move the platform naming to platform-and-pilot-status.md. |
| J5 Procedures over declarations | partly | SKILL.md: "⟨Containerization requirements, image and registry rules, resource limits⟩ - to be supplied." | Fill or link the containerization and lead-time placeholders so the package step is executable. |
| J7 Gotchas in SKILL.md | partly | SKILL.md Do not: "Treat a missing Cyber Security sign-off as optional, or grant it." Migration and cutover pitfalls live only in references/process-chain-practice.md. | Move the top three pitfalls from process-chain-practice.md into the Do not list. |
| J12 Consistent terminology | partly | SKILL.md: "use both terms as synonyms." vs Do not: "Assume the container platform of the flow is the IIoT Edge runtime." | Resolve the contradiction on whether the Container Orchestration Platform equals the edge runtime and fix one term. |
| J13 Explains the why | partly | SKILL.md: "Never describe the app store or the platform as more mature than it is." No reason given. | Add the reason (pilot status changes, old claims mislead sponsors) next to the maturity rule. |
| J15 One coherent unit | partly | SKILL.md: "Package and gate; the build is not covered here" yet references include microservice-app-pattern.md, a build design proposal. | Move microservice-app-pattern.md to the skill that owns app building. |
| J16 Grounded in real expertise | partly | SKILL.md: "The department has a drafted engine skill for this step" and the manifest is a "design proposal, not the pilot's procedure". | Mark which parts are department fact and which are design proposals, with a source per rule. |

Facts: No evals (F9).; process-chain-practice.md and microservice-app-pattern.md over 100 lines without table of contents (F6).; No scripts; J14 n/a.; Body about 2,017 tokens.

### deploy-cybersec

**adequate**: A disciplined, honest procedure for a gate whose standard is not collected, but its description, nested links and missing example limit it, and the skill is still draft. (0 gap, 6 partly; extension library)

Improve first:
1. Collect the sign-off standard and fill the placeholders.
2. Add one worked package example to SKILL.md.
3. Shorten the description and fix nested reference links.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | SKILL.md description: "Assemble the sign-off package ... Drafts and recommends only" mixes imperative and third-person, and lists procedure steps. | Rewrite in one voice and state the user need, not the internal steps. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Pre-evaluate before the formal review. Run this skill's package as a repeatable pre-evaluation"; the decision table repeats the procedure. | Delete the decision-table rows that restate procedure and move the OD x IT notes to background.md. |
| J9 Concrete examples | partly | absent in SKILL.md: no filled or fictional package example; references/precedents.md describes real patterns (Groot2B programme). | Add a short fictional filled package excerpt (case class, data leaving the network, answer record) to SKILL.md. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md references table gives 'Use it for' per file, but package-contents.md -> gate-rules.md and precedents.md -> gate-rules.md are nested links (F5). | Link gate-rules.md only from SKILL.md or inline the needed rules. |
| J12 Consistent terminology | partly | SKILL.md: "This skill therefore builds the **request package** and the **wait-state record**." vs outputs 'sign-off package'. | Use one name for the package (sign-off package) in SKILL.md and outputs. |
| J16 Grounded in real expertise | partly | SKILL.md: "the sign-off standard itself is not collected" (lists it as `⟨standard doc - to collect, with Cyber Security⟩`). | Collect the Cyber Security sign-off standard and cite it; until then keep the open-items list at the top. |

Facts: No evals (F9).; Description is 604 characters, long but under 1024.; Nested links: package-contents.md and precedents.md point to gate-rules.md (F5).; Date 2026-09-11 in body is a time-sensitive candidate (F10).; process-chain-practice.md over 100 lines without table of contents (F6); no scripts; body about 2,518 tokens.

### deploy-handover

**adequate**: Strong rules, template, example and diagnostics, but it is broad (three kinds of handover, two absorbed skills) and carries context and dated items in the body. (0 gap, 4 partly; core library)

Improve first:
1. Split application and function handover from use-case handover.
2. Remove the survey statistic and dated notes from the body.
3. Add 'Use when' triggers to the description.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md description: "Close a use case: hand over to the plant against its definition of done, confirm real adoption, act on low utilization." | Add a 'Use when' clause (use case handed to a plant, utilization NEVER, owner changes); it is only in Purpose. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "(A public vendor survey of 1,000 U.S. frontline manufacturing workers found 79% learned of updates only after they went into effect" | Remove the vendor-survey statistic and the 'handing over the function' essay from the body. |
| J12 Consistent terminology | partly | SKILL.md has "Handing over an application to IT or another team" and "Handing over the function, not a use case" besides use-case handover. | Name the three handover kinds distinctly (use-case handover, application transfer, function succession). |
| J15 One coherent unit | partly | SKILL.md: "## Handing over the function, not a use case" and "## Handing over an application to IT or another team" besides use-case handover and two absorbed skills. | Split application transfer to IT and function succession into their own skill or reference. |

Facts: No evals (F9).; Dates in body (2026-09-11, 2026-10-22) are time-sensitive candidates (F10).; process-chain-practice.md over 100 lines without table of contents (F6).; Body about 3,364 tokens, 159 lines, largest of the batch; no scripts.

### deploy-migration

**adequate**: A well-structured staged-cutover procedure with strong decision rules and honest provenance, but it lacks an example, carries a duplicated skill name and its back-out core is a proposal. (1 gap, 4 partly; extension library)

Improve first:
1. Add a worked example row (inventory, risk, checklist).
2. Fix duplicated invest-screen references and shorten the description.
3. Get the back-out plan structure confirmed by its owner.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | SKILL.md description lists artefacts: "as-is/to-be canvas, per-component risk and recovery-impact tables, OT application inventory" | Replace the artefact list with the user intent (move a legacy system safely, with a way back). |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Provenance: the assessment and per-location parts come from workshop and migration decks." Plus a long Questions to ask section. | Move the provenance and the Questions to ask section to background.md or the assessment reference. |
| J9 Concrete examples | gap | absent: SKILL.md has no example block of an inventory row, risk row or checklist item; looked in SKILL.md and the asset listing only. | Add one fictional inventory-and-risk row and one checklist item with RAG to SKILL.md. |
| J12 Consistent terminology | partly | SKILL.md: "`invest-screen` and `invest-screen` decide *whether* to replace, integrate or keep an application" | Fix the duplicated skill name (likely a rename artefact) in the intro, step 1 and the handoff table. |
| J16 Grounded in real expertise | partly | SKILL.md: "The **back-out plan content is a `PROPOSAL`**: the decks hold only diagrams of who does what, no content." | Have the owner of the back-out process confirm or replace the proposal structure. |

Facts: No evals (F9).; Description 670 characters, long but valid.; No scripts; J14 n/a; body about 2,743 tokens, 132 lines.; Status draft; origin plan-draft.

### deploy-project-order

**adequate**: A clear, gated drafting procedure with a template and pre-send check, but no worked example, a dangling small-change pointer and no evals. (1 gap, 8 partly; extension library)

Improve first:
1. Restore or relink the small-change rule that step 1 refers to as 'above' (it now lives only in references/background.md).
2. Add one worked example: a filled 30-second main target and a pre-send check result.
3. Add evals and shorten the agent notes and handoff tables that duplicate the procedure and outputs.yaml.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | write the main target as a 30-second message, never leave the budget blank, split requesting side (SKILL.md description) | Rewrite the description around what the user wants (a project order they can send) and drop the chapter-level rules. |
| J3 Concise: only what the agent lacks | partly | draft the order from the initiative one-pager and prior projects; fill chapters (SKILL.md, AI agent operating notes) | Cut the Can-do/Required-inputs/Hand-over notes and the Handoff tables where they repeat the procedure and outputs.yaml. |
| J6 Defaults, not menus | partly | the standard and extended variant, and the one-page short form for small initiatives (references/order-structure.md description) | Name the default variant in SKILL.md and the one condition that switches to the extended or short form. |
| J7 Gotchas in SKILL.md | partly | Do not present an earlier project's cost as this project's cost without saying so. (SKILL.md, Do not) | Add a short pitfalls list in SKILL.md with the reason behind each item; the Pitfalls and lessons section sits only in references/kickoff-and-reports.md. |
| J9 Concrete examples | gap | absent: no worked example in SKILL.md or the first 40 lines of references/background.md; only the phrase pattern for the target | Add one filled 30-second main target and one pre-send check result as an example. |
| J11 Progressive disclosure: says when to read what | partly | Is it a project?** Apply the small-change rule above. (SKILL.md, Procedure step 1) | Step 1 points to a small-change rule that is no longer in SKILL.md (moved to background.md); restore the one-line rule or link it, and say per step when to open each reference. |
| J12 Consistent terminology | partly | put the eCR in it (the money request itself is `bc-capital-request`) (SKILL.md, Procedure step 7) | Use one term (eCR or capital request) for the funding document throughout, not eCR, money request and capital request side by side. |
| J13 Explains the why | partly | Out of scope: write it, to avoid grey zones. (SKILL.md, Procedure step 4) | Add a clause of reason to the Do-not items, for example why the budget is never blank even for an internal project. |
| J16 Grounded in real expertise | partly | The check against empty fields and the customer-program variant are this skill's proposals (marked PROPOSAL in the references). (SKILL.md, Still open) | Name the source documents the chapter rules come from in background.md, so proposals can be told from sourced rules. |

Facts: Nested reference link: order-structure.md -> roles-risks-procurement.md (F5).; No evals (F9). No scripts.; Description is 836 characters (limit 1024); body about 2010 tokens, 113 lines.

### dept-context

**adequate**: A sourced, well-reasoned foundation with strong honesty rules, but no examples, near the token ceiling and partly duplicating dept-decision-rights. (1 gap, 5 partly; core library)

Improve first:
1. Add a worked example and a reply template for the resolved term, route or source outputs.
2. Trim to leave headroom under 5,000 tokens: collapse duplicate vocabulary rows, the retired-lines table and the Who-decides table.
3. Remove time-stamped statements (Lane 4 'added 2026-11-10', ODEC 'until 2025-12') or move them to background.md; add TOCs to three long references and evals.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | / Parquet / The main file format on the storage account / — / (SKILL.md, vocabulary table) | Merge the Databricks, Azure Storage Account and Parquet rows into the Data platform row and drop the retired-service-line table, which dept-intake repeats. |
| J5 Procedures over declarations | partly | Load this skill before any OD work; take terms only from the vocabulary table or its reference (SKILL.md, Procedure step 1) | Most of the body is declarations (vocabulary, lanes, lists); add a short how-to for resolving a term, a lane or a figure end to end. |
| J8 Output templates | partly | Chat reply, taken from the vocabulary table or its reference (outputs.yaml, resolved-term-lane-or-gate form) | Give the reply a three-line template (term or gate, meaning or route, source and date). |
| J9 Concrete examples | gap | absent: no worked example of resolving a term, a gate or a figure in SKILL.md or the first 40 lines of references/background.md | Add one short example that goes from a quoted figure to its list, export date and to-confirm marker. |
| J11 Progressive disclosure: says when to read what | partly | Reading the knowledge graph: node kinds, relations, provenance of descriptions (SKILL.md, References table, Open when column) | Phrase the Open-when column as conditions and add a table of contents to the three references over 100 lines. |
| J15 One coherent unit | partly | Full routing: `dept-decision-rights`. (SKILL.md, Who decides) | The Who-decides table and spend gates restate dept-decision-rights; keep a pointer and remove the table so one skill owns it. |

Facts: Body about 4232 tokens estimated (F4 limit about 5000); 212 lines.; Three references over 100 lines have no table of contents (F6): process-chain-practice, provenance-and-source-catalogue, swot-and-dependency-seams.; Time-sensitive dates in body: 2026-11-10 and 'until 2025'. No evals; no scripts.

### dept-context-freshness

**strong**: A focused, read-only, script-backed workflow with defaults, a report template and honest limits; the main gaps are no evals and an external helper script. (0 gap, 3 partly; extension library)

Improve first:
1. Add evals, including a run against a fixture bundle with one expired file.
2. Make the script report a missing path clearly, and bring check_no_figures.py (named in step 6) into this skill or state where it lives.
3. Tie fact-triage-and-generated-registers.md to a step or move it out; add a TOC to it.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | Read-only on the registry; includes a small stdlib script. (SKILL.md description) | Drop the implementation remark about the stdlib script from the description and keep what the user gets. |
| J11 Progressive disclosure: says when to read what | partly | Triage pattern for a staging pile of extracted facts (verdicts, plant buckets) (SKILL.md, References table) | No step says when to open fact-triage-and-generated-registers.md, and it covers extracted-fact staging, not quarterly freshness; add the trigger or move it. |
| J14 Scripts solve, handle errors, state dependencies | partly | Standard library only. The front matter is read line by line, not with a YAML parser (scripts/context_freshness.py docstring) | Add explicit handling and a clear message when --skills, --bundle or --registry points to a missing path; the first 60 lines show only argparse errors. |

Facts: Nested reference link: triage-and-actions.md -> staleness-signals.md (F5).; One reference over 100 lines without TOC (F6): fact-triage-and-generated-registers.md.; No evals (F9). Script: arg parsing, help, exit codes, no interactive input (F8). Description is 590 characters.

### dept-decision-rights

**adequate**: A precise routing skill with a template and example, held back by an expired source table, a split reference list and no evals. (0 gap, 3 partly; core library)

Improve first:
1. Re-verify the decision rights source (valid-until 2026-11-10 has passed) and remove the dated note once done.
2. Add the trigger ('Use when ...') to the description and merge the two reference tables with open-when conditions.
3. Add evals: one for each case (row found, gate outside OD, no row fits).

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | Answer "am I allowed to do this, and who decides?" for OD work: map a decision to its owner, approval and authority level. (SKILL.md description) | Add an explicit trigger such as 'Use before committing spend, approving a connection or changing a standard'; it exists only in the body. |
| J11 Progressive disclosure: says when to read what | partly | ## The references are the substance (SKILL.md, with a final References table that lists only background.md) | Merge the two reference tables into one and state conditions for opening each file; the first table says what each covers, not when to open it. |
| J16 Grounded in real expertise | partly | That file's `valid-until` was 2026-11-10. (SKILL.md, decision rights note) | The source table has expired (review date 2026-11-16); re-verify it with the OD lead or mark every row unverified in the skill output. |

Facts: Time-sensitive dates in body: 2026-09-11 and 2026-11-10 (F10); the valid-until 2026-11-10 is already past.; One reference over 100 lines without TOC (F6): process-chain-practice.md. No evals (F9).; SKILL.md links across skills (../bc-capital-request/references/ecr-approval-matrix.md); body about 2704 tokens.

### dept-governance

**adequate**: Concise, with good gates and honest forum status, but one skill covers six routines with a procedure for only one and no example. (1 gap, 5 partly; extension library)

Improve first:
1. Split or narrow the scope: sprint runbook and training programme are separate routines that each need their own procedure.
2. Add one worked example (status row plus call for action) and evals.
3. Align terminology with dept-context (no 'service line', one spelling of CoP/COP) and add reasons to the decision rules.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | Holds method only, no dates, counts or plant statuses. (SKILL.md description) | State the user's goal at the front, and cut the inventory of internal parts and the remark about the skill's own content. |
| J5 Procedures over declarations | partly | ## Procedure: prepare and follow up a round (SKILL.md; the only procedure) | Sprint, demand routing, roadmap and training have no steps in SKILL.md, only pointers; add a short step list for each or split them out. |
| J9 Concrete examples | gap | absent: no example of a call for action, status row or sprint plan in SKILL.md or the first 40 lines of references/background.md | Add one filled status row and one numbered call-for-action line as an example. |
| J12 Consistent terminology | partly | route each to its owning service line (SKILL.md, Procedure step 6) | dept-context says the four service lines are retired; replace 'service line' with the owning role and use CoP or COP in one spelling. |
| J13 Explains the why | partly | Rollout continues only where an **operations concept** (owner, SLA, support level) exists. (SKILL.md, Decision rules) | Add a clause of reason to each decision rule, for example why a not-connected machine goes into a wave first. |
| J15 One coherent unit | partly | / Training programme / 1a3, 3a6, 26 / `know-training` / (SKILL.md, Where it sits in the chain) | Six unrelated routines (rounds, roadmap, routing, sprint, training, community) share one skill; split the sprint runbook and training programme into their own skills. |

Facts: Eight reference files; description is 821 characters, long but under 1024 (F2).; One reference over 100 lines without TOC (F6): forums-and-roadmap.md. No evals (F9). No scripts.; Time-sensitive date text in body: 'until 2025' (F10).

### dept-intake

**strong**: A clear entrance skill with a decision order, output record, example and refusal rules; small gaps in the description trigger and evals. (0 gap, 3 partly; core library)

Improve first:
1. Add the 'Use when' trigger to the description.
2. Reorder step 2: the refusal bullets sit before their 'Refuse:' lead-in, and link refusal-playbook.md there.
3. Add evals (one accept, one refuse, one fall-through) and a TOC to process-chain-practice.md.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | Decide what OD does with an incoming request: accept into one of three lanes, refuse, or route to the owner. (SKILL.md description) | Add the trigger to the description: use when a request, demand or idea arrives; it is only in the body. |
| J3 Concise: only what the agent lacks | partly | When a requester names an old line, translate it with this crosswalk (`dept-context`). (SKILL.md, step 3) | Remove the retired-service-line bullets that restate dept-context and keep only the pointer. |
| J11 Progressive disclosure: says when to read what | partly | Request patterns that look legitimate but should be refused or re-scoped (references/refusal-playbook.md description) | Point to refusal-playbook.md at step 2 where a refusal is decided, not only in the table, and add a TOC to the 152-line process-chain-practice.md. |

Facts: One reference over 100 lines without TOC (F6): process-chain-practice.md (152 lines).; Time-sensitive date in body: 2026-10-22. No evals (F9). No scripts.; Description is 179 characters, with no 'when to use' trigger.

### dept-plant-diagnosis

**adequate**: Sound ordered method with strong human gates and pitfalls, but no worked example, no evals and the key working rule sits only in background.md. (0 gap, 6 partly; extension library)

Improve first:
1. Restore the 'equal effort, unequal saving points to people and method' rule in SKILL.md (J13).
2. Add a worked example diagnosis and roadmap row (J9).
3. Add an explicit pre-handover validation step tied to outputs.yaml done_when (J10).

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | SKILL.md: "read the gap across four Ishikawa branches (people, method, machine and IT, environment)" | Open the description with the user question (why do similar plants save unequally) and cut the method detail. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "/ Plant placed by starting profile, machine and use-case lists read on the day / `dept-plant-onboarding`, `know-sharepoint-export` /" | Drop the handoff tables from SKILL.md; outputs.yaml already holds receives_from and next. |
| J9 Concrete examples | partly | SKILL.md: "(for example whether the plant owns its machine programs in-house)" | Add one filled mini-diagnosis (two plants, branches, tier, one roadmap row) as a worked example. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md: "Do not set a roadmap row to green without evidence; a missing close-loop update is yellow." | Add a final pre-handover checklist step that ticks each done_when line of outputs.yaml. |
| J13 Explains the why | partly | references/background.md: "equal integration effort with little or no saving points to people and method, not to technology" | Put the one-sentence working rule (equal effort, unequal saving points to people and method) back into SKILL.md next to step 3. |
| J16 Grounded in real expertise | partly | references/background.md: "The decks' working rule:" | Name the source decks and gap analysis (title, date) in SKILL.md so the diagnosis rules can be traced. |

Facts: No evals (F9 false).; About 2641 tokens, 142 lines, 7 reference files, no nested links, no scripts.; Description 752 chars.

### dept-plant-onboarding

**adequate**: A clear stage path with honest open points, but no worked example, provenance filler in the body, a mixed stage vocabulary and no evals. (1 gap, 8 partly; extension library)

Improve first:
1. Add a worked example plant with filled tracker rows (J9).
2. Unify vocabulary (stage, plant record) and cut the provenance bullets (J12, J3).
3. Add open-when cues and a TOC to the references and remove the nested link (J11).

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | SKILL.md: "Lay out the onboarding path of one plant through the OD skill set, in order" | Lead with the user need (where does this plant start and what comes next) and drop 'OD skill set' and 'three new-state lanes' wording. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Plan item O-09 of the department's skill map." | Delete the provenance and skill-map bullets; the agent does not need them to run the path. |
| J7 Gotchas in SKILL.md | partly | SKILL.md: "Do not connect a machine to an external system without Cyber Security / OT sign-off." | Group the Do-not list under a Pitfalls heading and give a reason to the items that lack one (hardest machine types, first plant). |
| J9 Concrete examples | gap | absent: no filled example in SKILL.md or references/background.md; the profile table is abstract and assets/ was not opened | Add a short worked example: one plant placed as profile C with its filled tracker rows. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md: "each stage in the table below has its artefact filed, or an explicit `⟨reason it does not apply⟩`" | Add a stage-gate check before moving to the next stage (artefact filed, owner named) instead of one end-state definition. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md: "How to read the plant records (region, machines, integrated share, use cases, main controller and integration method) and how to obtain them live" | Add open-when cues to the references table, add a TOC to process-chain-practice.md (110 lines) and remove its nested link to plant-landscape.md. |
| J12 Consistent terminology | partly | SKILL.md: "## Step 0: place the plant" | Use one unit (stage) throughout: Step 0 vs Stages 1-8 and 'plant record' vs 'Machine List' vs 'lists' mix. |
| J13 Explains the why | partly | SKILL.md: "The sign-off runs in parallel with planning and build and blocks only go-live: start the package early." | Give a reason for the other bare rules (do not start with the hardest machine types, do not start with a use case first). |
| J16 Grounded in real expertise | partly | SKILL.md: "**no Department OS document describes plant onboarding**" | State which playbooks and plant records each stage rule comes from, since no source document exists. |

Facts: Nested link: process-chain-practice.md -> plant-landscape.md (F5).; process-chain-practice.md is 110 lines without a TOC (F6).; No evals (F9 false).; About 2293 tokens, 98 lines, 5 reference files, no scripts.

### dept-retro

**strong**: Tight decision rule, explicit preference order, decision table and reasons; weakened by missing example, provenance filler and no evals. (0 gap, 4 partly; extension library)

Improve first:
1. Add one filled retro record as a worked example (J9).
2. Cue references from procedure steps and unify 'learning/evidence list' (J11, J12).
3. Move provenance and open-questions text to background.md (J3).

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Plan item O-06 of the department's skill map (wave 3)." | Cut the plan-item and operating-rhythm provenance bullets and the open-questions block from the body; keep them in background.md. |
| J9 Concrete examples | partly | SKILL.md: "/ Same item appeared in two months / It, ahead of newer items /" | Add one filled retro record (three inputs, learning list, the one adjustment) as an example. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md: "/ `references/reading-change-logs.md` / What the generated use-case change logs record" | Cue each reference from the step that needs it (change logs at step 2) and remove the nested process-chain-practice.md -> retro-inputs.md link. |
| J12 Consistent terminology | partly | SKILL.md: "**Write the learning list.**" | Use one term: SKILL.md says learning list, outputs.yaml and the record say evidence list. |

Facts: Nested link: process-chain-practice.md -> retro-inputs.md (F5).; No evals (F9 false).; About 1939 tokens, 104 lines, 6 reference files, no scripts.

### dept-risk

**strong**: Focused read-and-classify method whose key rule (unreadable is not clear) is explained and enforced; lacks a worked reading, a completeness check and evals. (1 gap, 2 partly; extension library)

Improve first:
1. Add a filled sample reading (J9).
2. Add a completeness check before the draft goes to the OD lead (J10).
3. Move provenance and open-points text out of the body (J3).

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Plan item O-07 of the department's skill map." | Move the plan-item, register-design and open-points text to background.md; keep statuses, procedure and the decision table. |
| J9 Concrete examples | gap | absent: no filled sample reading in SKILL.md or references/background.md; assets/risk-reading.md was not opened | Add one filled risk reading with six rows, including one unreadable and one on-watch indicator. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md: "**Check the register for staleness:** a risk whose indicator has been *Unreadable* three months in a row" | Add a completeness check that all six risks carry value, source, date, trigger and status before the reading goes to the OD lead. |

Facts: Nested link: process-chain-practice.md -> risk-indicators.md (F5).; No evals (F9 false).; About 1680 tokens, 97 lines, 5 reference files, no scripts.

### funnel-evaluation

**adequate**: Strong method, script, verdict rules and pitfalls, but it carries a second absorbed skill, mixed terminology, heavy reference table and thin script error handling. (0 gap, 6 partly; extension library)

Improve first:
1. Split or clearly fence the absorbed od-maturity-assessment sub-skill and trim the references table (J15, J3).
2. Add error handling to evaluate_fit.py (J14).
3. Add TOCs to the two long references and unify area terminology (J11, J12).

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | SKILL.md: "profile its complexity (27 drivers), find which of 16 IT/OT capability areas it depends on" | Lead with the question (does this solution fit the need) and push the 27-driver and 16-area mechanics into the body. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "/ `references/od-maturity-assessment/references/model-caveats.md` /" | Collapse the five absorbed od-maturity-assessment rows into one pointer to procedure.md to shorten the references table. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md: "/ `references/focus-areas.md` / Steps 2-3: 16 areas, levels, evidence, target setting /" | Add a TOC to focus-areas.md (205 lines) and process-chain-practice.md (108 lines) and limit the absorbed sub-skill to one level. |
| J12 Consistent terminology | partly | SKILL.md: "Each high/dominant driver maps to one or more of 16 focus areas" | Use one term for the areas (focus areas vs capability areas) and one for the output (protocol, evaluation, report). |
| J14 Scripts solve, handle errors, state dependencies | partly | scripts/evaluate_fit.py: "No dependencies beyond the standard library." | Catch missing or malformed input JSON and print a usage message; the file has no except or stderr handling. |
| J15 One coherent unit | partly | SKILL.md: "Also profiles the as-is maturity of one machine, system or application on the same 16 areas" | Keep the absorbed maturity profile as its own skill or give it its own trigger, since two tasks share one skill. |

Facts: No evals (F9 false) although status is stable.; focus-areas.md is 205 lines and process-chain-practice.md 108 lines, both without a TOC (F6).; About 2657 tokens, 108 lines, 8 reference files plus an od-maturity-assessment subfolder; no nested links flagged.; Script flags: arg parsing, --help, no interactive input, exit codes present.

### funnel-features

**strong**: Short, focused skill with a worked example, template and a script that encodes a measured failure pattern; minor description and terminology issues and no evals. (0 gap, 3 partly; extension library)

Improve first:
1. Rewrite the description around the user outcome and drop the funnel self-reference (J2).
2. Unify stage and step terminology (J12).
3. Add a TOC to epic-and-user-stories.md (161 lines) and state a default story cut (J6).

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | SKILL.md: "the department's funnel-features, stage 2 of the product funnel between funnel-requirements and the business case and prototype" | Drop the self-referential 'department's funnel-features' phrase and the funnel position; state what the user gets. |
| J6 Defaults, not menus | partly | SKILL.md: "Cut at least two stories by moment and role or by existing signals, never by technical layer." | Name one default way to cut stories (for example by moment and role) and mention the signal-based cut as the alternative. |
| J12 Consistent terminology | partly | SKILL.md: "Stage 2 of the department's product funnel" | Use one position term: SKILL.md mixes stage 2 and Lane 2 step 22, and calls the same file handoff file, epic file and epic-and-stories. |

Facts: No evals (F9 false).; epic-and-user-stories.md is 161 lines without a TOC (F6).; About 734 tokens, 49 lines, 4 reference files, no nested links.; Script flags: arg parsing, --help, no interactive input, exit codes.

### funnel-first-aid

**adequate**: Usable intake and routing method with real reasons, but it is a draft with unresolved placeholders in the procedure, a self-referencing route and a bundled absorbed lane. (0 gap, 7 partly; extension library)

Improve first:
1. Fix the routing row that points to this same skill and resolve or relocate the open placeholders.
2. Shorten the description and remove the absorbed-lane sentence.
3. Add one inline good-versus-bad S.M.A.R.T. example.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | SKILL.md: "Also absorbs the retired Analytical Support Service lane: ad-hoc analytics now routes to Lane 1 self-service, Lane 2 or external support." | Drop the registry-history sentence from the description and keep only user-intent triggers. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "The service catalogue lists the Smart Factory Use Case Support Service "(incl." | Cut the catalogue-provenance paragraph and move the 'What is still open' placeholders to background.md. |
| J9 Concrete examples | partly | SKILL.md: "see the difference between "diameter oscillates" and a question a dataset can answer" | Inline one filled good-versus-bad S.M.A.R.T. pair in SKILL.md instead of only pointing to references. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md: "/ `references/background.md` / Context, rationale, examples and notes moved out of this file; never an instruction /" | List first-aid-offering.md and process-chain-practice.md in the References table with 'read when' triggers. |
| J12 Consistent terminology | partly | SKILL.md: "/ One-off question, data readable, insight is the answer / `funnel-first-aid` (step 1 scoping, then `mi-data-availability`)" | Fix the routing row that routes to this same skill, and use one name for the one-off route (Analytical Support vs first aid vs Lane 1 self-service). |
| J15 One coherent unit | partly | SKILL.md: "when an ad-hoc analytical request needs the old lane's composed artefacts and task chain;" | Separate first-aid scoping and routing from the absorbed ad-hoc analytics delivery lane, or state which entry applies when. |
| J16 Grounded in real expertise | partly | SKILL.md: "It is a draft for the DBVE to adopt or replace." | Resolve the open placeholders (template, queue, closing rule) with the DBVE, or move them out of the procedure. |

Facts: Description 793 characters, under the 1024 limit but long.; Status draft; no scripts and no evals (F9).; Nested od-analytical-support-service folder holds the absorbed lane.

### funnel-prototype

**adequate**: Clear decision procedure, record template and honest labels, but it states itself not a validated method and carries status prose and an overlong reference set. (0 gap, 6 partly; core library)

Improve first:
1. Add use-when triggers to the description and read-when triggers to the reference table.
2. Move the status and provenance prose out of SKILL.md and add tables of contents to the long references.
3. Run it on one real use case and add evals, so the 'not validated' disclaimer can be lifted.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md: "Prove a new use case cheaply before the business case: choose click-dummy, proof of concept or neither, and record the result." | Add a 'Use when' clause with user words (mock-up, PoC, pilot, validate with the plant) to the description. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "It is **not** a validated OD method: nothing in the sources says OD has run this step to a stated standard." | Move the status and provenance bullets (lines 32-35) and the label discussion that repeats status-labels.md into references. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md: "The label ladder the decks use, how labels mislead (disagreement between decks, "rollout" is not proven value)" | Reword the references table as 'read X when Y' triggers and add a table of contents to click-dummy.md and build-patterns.md (296 and 324 lines). |
| J12 Consistent terminology | partly | SKILL.md: "The strategy material works with four working stages - PoC, prototype, pilot, rollout" | Pick one umbrella term (prototype vs click-dummy vs mock-up) and state how the four-stage ladder maps to the label table. |
| J13 Explains the why | partly | SKILL.md: "stop: a prototype on missing data proves nothing." | Add a one-clause reason to the other Do-not rules (named validator, no real plant data, no added tool). |
| J16 Grounded in real expertise | partly | SKILL.md: "This skill is grounded in what the knowledge base actually holds: one AI pilot (the Gemba App), PoC labels in two AI decks" | Mark which method steps rest on the single Gemba pilot and which are the author's inference, and collect one validated run. |

Facts: No evals (F9).; Three references over 100 lines have no table of contents (F6).; Nine reference files; no nested reference links.

### funnel-requirements

**strong**: Best-equipped of the batch: procedure, checker script with exit codes, pitfalls, reasons and a handoff schema, held back by a missing triggers clause and a broken step 10. (0 gap, 5 partly; core library)

Improve first:
1. Repair step 10 (orphan '5a.', dated meeting reference) and add use-when triggers to the description.
2. Add a short filled example requirement and a default entry mode and lane.
3. Add tables of contents to the five long references and write evals.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md: "Turn an accepted demand into a requirement another lane can act on: signals, testable acceptance criteria, handover packet and epic." | Add 'Use when' triggers (a demand has been accepted, a lane hand-over is due, a requirement needs checking) to the description. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "**Fix the boundaries** (§6a, from the OD x IT alignment of 2026-09-11)" | Repair the orphaned '5a.' line under step 10, drop the dated meeting reference, and move dated provenance into background.md. |
| J6 Defaults, not menus | partly | SKILL.md: "idea mode or as-is mode; in as-is mode map the current process" | State which entry mode and which lane variant is the default when the demand does not say. |
| J9 Concrete examples | partly | SKILL.md: "BLOCKER: signal list not verified (fictional output)" | Add a short filled example of one good and one bad acceptance criterion or signal row to SKILL.md. |
| J12 Consistent terminology | partly | SKILL.md: "an integration request without signal list and acceptance is a conversation, not a work item" | Use one noun for the unit (demand, request, need or requirement) and define the others once. |

Facts: Body contains the date 2026-09-11 (F10 candidate).; Five references over 100 lines have no table of contents (F6).; No evals (F9).; One script, with argparse, help and exit codes.

### funnel-use-case

**adequate**: Strong four-phase method with control points and reasons, but it bundles a lay-user idea check, the lane flow and workshops in one skill and uses two step numberings. (0 gap, 4 partly; core library)

Improve first:
1. Rewrite the description with plain triggers and drop the step number.
2. Split or clearly separate the lane flow, idea check and workshops, since workshops overlap funnel-workshop.
3. Unify step and row numbering and the use-case/demand terms.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md: "Define a plant use case so it can be built, standardized, handed over and measured (step 21), and run definition workshops." | Replace '(step 21)' with plain triggers (a plant has an idea or an accepted demand, an onboarding workshop is due). |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Provenance: merged from the lane's playbook and the use-case knowledge base pages." | Move the lane-flow table, state tracking and provenance into lane-service-flow.md, keeping the four phases in SKILL.md. |
| J12 Consistent terminology | partly | SKILL.md: "Step 21 = rows 1 and 2." | Use one step numbering (flow step or table row) and use 'demand' and 'use case' for distinct things only. |
| J15 One coherent unit | partly | SKILL.md: "The rest of this skill is the DBVE's full method for the same idea once it goes ahead." | Separate the lay-user idea check, the DBVE definition method and the workshops table, since workshops overlap funnel-workshop. |

Facts: Second-largest reference set of the batch (12 files); one without a table of contents.; No evals (F9).; Frontmatter has no allowed-tools.

### funnel-workshop

**adequate**: Complete before/during/after procedure with templates and sourced reasons, but it leans on source-document narrative, has placeholders inside steps and no inline example. (0 gap, 3 partly; extension library)

Improve first:
1. Add one filled capture-sheet example.
2. Clean the placeholders and the broken step 12 formatting, and move source narrative to background.md.
3. Fix the workshop naming so each format has one name.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | SKILL.md: "The lane's recurring tasks (`tasks.md`) include two workshops: the **Use Case Definition Workshop**" | Move the source-document narrative and the 'What is still open' placeholders to background.md and keep the procedure lean. |
| J9 Concrete examples | partly | SKILL.md: "See the plant-agenda example in the formats reference." | Inline a short filled example of one capture-sheet row (demand, savings basis, owner). |
| J12 Consistent terminology | partly | SKILL.md: "which comes first, a Machine Integration workshop or a Use Case workshop" | Define the workshop names once (Use Case Definition, Use Case Integration, Machine Integration) and use only those. |

Facts: Status draft; no scripts and no evals (F9).; One reference over 100 lines without a table of contents (process-chain-practice.md).; Description 645 characters.

### invest-screen

**adequate**: Sharp guardrails, concrete example and reasoned verdicts, but the skill spans four jobs, runs two verdict vocabularies and has a duplicated procedure and pitfalls. (0 gap, 5 partly; core library)

Improve first:
1. Split whole-list screening and application consulting from the intake check and Lane 3 gate.
2. Unify the fits/redesign/escalate and Go/PoC-first/Hold vocabularies.
3. Remove the Pitfalls and Procedure duplication and fix the truncated to_roles in outputs.yaml ('The calling skill (').

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md: "Intake fit check and Lane 3 tool-decision gate: catch requests needing a system outside the lean footprint; route make/buy/integrate/connect." | Add 'Use when' triggers in user words (a request sounds like scheduling or traceability, someone asks make or buy, an invest list needs screening). |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "The guardrails above are the pitfalls:" | Delete the Pitfalls section that restates the guardrails and the Procedure that restates 'The check', and trim the definition of done. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md: "What each lightweight tool (QFPR, MDA/PDA, MIL, Camline, WiriTec) is and is not for" | Say at which step each reference is opened, and add tables of contents to the four reference files over 100 lines. |
| J12 Consistent terminology | partly | SKILL.md: "one verdict (fits, redesign, escalate; in Lane 3 also the route and a Go / PoC-first / Reduce-complexity / Hold / Blocked verdict)" | Merge the two verdict vocabularies (and the stray 'Reject') into one scheme, and name the artefact consistently (fit check, intake check, gate). |
| J15 One coherent unit | partly | SKILL.md: "When the input is the MPEE Invest and Cost Planning list rather than one demand, run the department's `investment-checking` workflow" | Split the whole-list investment screen and the absorbed application-consulting procedure from the intake fit check and Lane 3 gate. |

Facts: Highest reference count of the batch (17), including a nested od-application-consulting folder with its own references.; Four references over 100 lines have no table of contents (F6).; Body 3830 tokens estimate, within F4; no evals (F9).

### know-ai-generation

**adequate**: A useful single rulebook for agent limits, but it is declarative, has no worked example, and its rules are unconfirmed proposals. (1 gap, 8 partly; extension library)

Improve first:
1. Add a worked step card and a filled missing-signal/binding table.
2. Put the generation-pipeline stages as numbered steps in SKILL.md.
3. Get the owner to confirm the PROPOSAL rules and add a one-clause reason to bare rules.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | SKILL.md description: "the multi-step generation pipeline with its human gate and visual-QA loop" | Open the description with the user's question (what may an agent do here, who signs) and drop the list of internal mechanisms. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Do not deliver a generated artefact with open items inside it or without citations." | Delete the Do-not items that only restate R2, R5 and R9. |
| J5 Procedures over declarations | partly | SKILL.md R3: "Generation is safest when the input has a fixed structure and the output is a config that can be imported and tested." | Put the numbered stages of the generation pipeline in SKILL.md instead of leaving them only in references/generation-pipeline.md. |
| J9 Concrete examples | gap | absent: no worked example in SKILL.md or in references/background.md (first 40 lines) | Add one short filled step card for a dashboard-generation case. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md R1: "If the section an agent needs is stale or has no owner, it stops and reports that" | Add an explicit check-and-repeat loop for the visual-QA stage in SKILL.md rather than only in the reference. |
| J12 Consistent terminology | partly | SKILL.md R2: "R2 - Honesty rule for generated output (all steps)." (elsewhere the same thing is called an artefact) | Use one noun (output or artefact) throughout and one marker for unknowns (`<to confirm>`). |
| J13 Explains the why | partly | SKILL.md R10: "A prompt-to-prototype shows value fast; it is not a deployment." | Add one clause of reason to R4, R5 and R8, which are stated as bare rules. |
| J15 One coherent unit | partly | SKILL.md: "It is the one rulebook for the places in the chain where an AI agent drafts, classifies, generates or checks something" | Keep the rules here and move AI-app intake and the maturity ladder to the skills that own them. |
| J16 Grounded in real expertise | partly | SKILL.md: "The owner has not confirmed the `PROPOSAL` rules." | Have the owner confirm or strike each PROPOSAL rule and cite the deck behind the rest. |

Facts: No evals (F9).; references/generation-pipeline.md is 103 lines without a table of contents (F6).; Description is 762 characters, long but under the limit; body about 2,549 tokens.

### know-sharepoint-export

**strong**: Small, procedural, with a real validation step, stated limits and a reason for its key rule; only the script's error handling and examples are thin. (0 gap, 2 partly; extension library)

Improve first:
1. Harden check_export_schema.py: error messages and exit codes for bad input.
2. Add a sample run-log entry and schema-check output.
3. Add a table of contents to export-procedure.md (125 lines).

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J9 Concrete examples | partly | SKILL.md: "Proven against the SmartFactory UseCase Savings list, which has both item history and attachments." | Add a filled sample run-log line and sample schema-check output to SKILL.md. |
| J14 Scripts solve, handle errors, state dependencies | partly | scripts/check_export_schema.py docstring: "No dependencies beyond the standard library. Exit code 1 on any drift or a non-advancing checkpoint, 0 otherwise" | Catch missing or invalid JSON files and wrong argument counts with a message and a non-zero exit code (now it prints the docstring and exits 0, or raises a traceback). |

Facts: No evals (F9).; references/export-procedure.md is 125 lines without a table of contents (F6).; One script, argument parsing and exit codes present (F8).

### know-skill-authoring

**strong**: A clear nine-step method with control points, pitfalls, templates and a working scaffold; weak spots are the off-convention example and that it ships no evals itself. (0 gap, 1 partly; extension library)

Improve first:
1. Add the skill's own evals (step 8 asks for them) and a filled sample brief.
2. Fix the example name to a registry family prefix.
3. Repair outputs.yaml, where 'Department owner (DBVE; the OD lead approves publication)' is split into two list entries.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J9 Concrete examples | partly | SKILL.md code block: "python3 scripts/scaffold_skill.py od-example-check --tier practice --lane all \" | Replace the invented example name (it uses the old od- prefix, not a registry family) and add one short filled brief. |

Facts: No evals (F9) although step 8 of this skill requires them.; Has a test script (test_scaffold_skill.py), excluded from J14.; outputs.yaml: the to_roles/signoff text 'Department owner (DBVE' is broken by a semicolon (observed in the file, not in facts.json).

### know-training

**adequate**: Honest and well bounded, but the content is mostly proposals on thin sources, with no worked example. (1 gap, 4 partly; extension library)

Improve first:
1. Obtain the real training formats and competence standard from the OD lead.
2. Add a worked example (filled package row and checklist row).
3. Remove the nested reference link and the status paragraph from SKILL.md.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | SKILL.md: "**Status: draft, and the thinnest-sourced skill in the registry.**" | Move the status and sourcing paragraph to background.md and keep only the decision table and open list. |
| J6 Defaults, not menus | partly | SKILL.md step 4: "**Choose modules and the hands-on form.**" | Name a default minimum module set per plant role instead of leaving the choice open. |
| J9 Concrete examples | gap | absent: no worked example in SKILL.md or in the first 40 lines of references/background.md | Add one filled competence-checklist row for a concrete solution and role. |
| J11 Progressive disclosure: says when to read what | partly | references/curriculum-modules.md row: "The module catalogue (M0 to M7): audience, what the trainee must be able to do" | Inline the process-chain-practice.md link to curriculum-modules.md so references stay one level deep, and drop the second references table. |
| J16 Grounded in real expertise | partly | SKILL.md: "They do **not** give a training standard, a list of modules or a competence model." | Get the standard training formats and competence model from the OD lead and replace the proposals. |

Facts: No evals (F9).; Nested reference link: process-chain-practice.md -> curriculum-modules.md (F5).; No scripts.

### metrics-scorecard

**adequate**: Sound source-authority and honesty rules, but it overlaps the retro and governance skills and gives no steps for the fetching it promises. (0 gap, 7 partly; extension library)

Improve first:
1. Add concrete steps and a filled example for fetching and reading a metric.
2. Remove retro and round material that other skills own.
3. Renew valid_until (2026-11-10 has passed) and rewrite the 'until 2025-12' sentence as a dated record.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | SKILL.md description: "(the COP and any round held on request; ODEC is a historical source)" | Remove the ODEC parenthesis from the description and keep the user-facing triggers. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "The retro is **mandatory, not optional**, and its output is exactly one decided adjustment." | Leave retro and round mechanics to dept-retro and dept-governance and link to them. |
| J5 Procedures over declarations | partly | SKILL.md Procedure: "Refetch each figure from its authoritative source; note the read date." | Give the concrete steps to fetch a figure from the Scorecard and the two Power BI reports, since the description promises 'Fetch'. |
| J9 Concrete examples | partly | SKILL.md Procedure: "a month at 11 against a 12 target is red even in a good year" | Add one filled row of the protocol to show a read date, source and flag. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md Procedure: "Flag every metric past its intervention threshold, with the lane owner named." | Add a pre-handover check that every row has a read date and source, and loop back if not. |
| J12 Consistent terminology | partly | SKILL.md: "Report the Scorecard figure and say which filter the other came from." (figure, metric and number are used interchangeably) | Use one term for a reported value and one name for each report. |
| J15 One coherent unit | partly | SKILL.md: "Preparing and following up a round is the most rewarding agent task here" | Split round preparation and follow-up from metric reading, or hand it to dept-governance. |

Facts: No evals (F9).; dates_in_body: 'until 2025' (a historical ODEC statement); frontmatter valid_until 2026-11-10 is before today (2026-11-16).; references/metric-reading-guide.md is 125 lines without a table of contents (F6).; No scripts; no allowed-tools key.

### mi-data-availability

**strong**: A focused diagnostic with a script, traps, a worked example and templates; the very short description is its main weakness. (0 gap, 3 partly; core library)

Improve first:
1. Rewrite the description with triggers and user words.
2. Rename the six availability steps so they do not clash with process step ids.
3. Add tables of contents to the three reference files over 100 lines.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md description: "Check whether the data a use case needs exists, is reachable and fit for use before anything is promised; name the step it fails at." | Add a Use-when clause with the words a user would say (plant, machine, signals, Machine List, can we get this data). |
| J3 Concise: only what the agent lacks | partly | SKILL.md Purpose: "Finds out which of the six availability steps a data request dies at, before anyone promises an answer the data cannot support." | Delete the Purpose paragraph and the second references table row that repeat the intro. |
| J12 Consistent terminology | partly | SKILL.md: "This is step 2 of the Analytical lane" (while the six availability steps are also called step 2, 4, 5) | Call the six checks 'checks A1 to A6' or 'path steps' so they are not confused with process steps and lane names. |

Facts: No evals (F9).; Three references over 100 lines without a table of contents: data-needs-by-capability.md, non-machine-data-sources.md, process-chain-practice.md (F6).; Description 182 characters; 11 reference files; one script with arguments, help and exit codes (F8).

### mi-equipment

**adequate**: Deep, well-sourced and procedural, but the description misstates the skill's authority and the SKILL.md plus reference tree is heavy. (0 gap, 6 partly; core library)

Improve first:
1. Rewrite the description: accurate verb (recommend), triggers and user words.
2. Add tables of contents to the 14 long references and trim the absorbed sub-trees.
3. Move connector-specific pitfalls out of SKILL.md.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md description: "Assess and connect machines to the platform: plan a wave, route a machine to IIoT Edge or dataFEED" | Say 'Recommend how to connect machines' and add a Use-when clause with user words (machine will not connect, which connector, plan a wave). |
| J2 Description: one point of view, user intent | partly | SKILL.md description: "Assess and connect machines to the platform" (the skill itself says an agent never connects) | Replace 'connect' with 'recommend a route for connecting' and describe the user need before the product names. |
| J3 Concise: only what the agent lacks | partly | SKILL.md Pitfalls: "`DTQ-B&R-Connector` and `DTQ-Bachmann-Connector` do not exist (`Idea`); those machines go over OPC UA via the aggregation server." | Move connector-specific facts from Pitfalls into references/connectors.md and keep the rule in SKILL.md. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md references table: "Before recording a machine as blocked" (good), but 14 long files have no table of contents and about 20 more sit in three absorbed sub-trees | Add a table of contents to each reference file over 100 lines and list the three absorbed sub-trees once instead of file by file. |
| J12 Consistent terminology | partly | SKILL.md Route A step 4: "**Route each machine** through the Route B gates for concept and connector; log a barrier where no route exists." (route, variant, pattern, concept used for related things) | Define route, variant, connector and concept once and use them consistently; rename Route A/B to Mode A/B. |
| J15 One coherent unit | partly | SKILL.md: "Two entry routes to one protocol" (plus three absorbed modes: wave plan, barrier triage, former lane) | Split barrier triage and the former-lane material into their own skills or keep them as clearly separate references. |

Facts: No evals (F9); 17 reference files, 14 over 100 lines without a table of contents (decision-paths 348, softing-datafeed 408 lines).; Body estimated 4,641 tokens, close to the 5,000 guide (F4).; dates_in_body: 2026-11-06 is an owner decision date, not time-sensitive information.

### mi-flow

**adequate**: Strong, corpus-derived content with a working analyser and Done-when bar, held back by a description without triggers, a bloated Files section near the token ceiling, and no evals. (0 gap, 6 partly; core library)

Improve first:
1. Add 'Use when' triggers to the description and cut the repeated Files/References/example tables to get clear headroom under 5000 tokens.
2. Split or clearly mode-gate the rule-engine workflow, and add tables of contents to the 14 long references.
3. Write 3 evals (build a P1 delta gate, diagnose a silent flow, port a flow) and add a concrete before/after fragment to the Example.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md: "Build, review, document, troubleshoot and port Node-RED flows to the OESL estate standard (MQTT, protobuf, topics, error handling)." | Add an explicit 'Use when' clause with the user's own symptoms (flow publishes nothing, dashboard is flat, new machine needs a flow). |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Rule-engine production example" | The Files table lists 14 identical 'Rule-engine production example' rows and repeats the references table; collapse them to one row pointing at the folder, and drop the duplicated Files/References tables to save tokens (body is 4951 of 5000). |
| J9 Concrete examples | partly | SKILL.md: "BLOCKER systime-not-repacked" | The only inline example is analyser output; add one short before/after function-node snippet (or point at the BROKEN/FIXED rule-engine example) so a concrete flow fragment is visible in SKILL.md. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md: "read `deployable-flow.md` before generating a file." | Most pointers carry a read-when trigger, but the Files table lumps six references into one row with no trigger, and 14 long references have no table of contents; split the row and add TOCs. |
| J12 Consistent terminology | partly | SKILL.md: "`mi-equipment` / `mi-equipment`" | Fix the duplicated skill name and use one term each for the edge platform (IIoT Edge Platform / edge platform / DATATRON / datatroniq are mixed). |
| J15 One coherent unit | partly | SKILL.md: "A Node-RED flow is the **transformation stage** between a connected machine and a use case." | Build, troubleshoot and the rule-engine generator (20 reference files) share one skill; consider splitting the rule-engine workflow into its own skill or state clearly which mode a request loads. |

Facts: Body estimate 4951 tokens, 49 under the 5000 F4 threshold.; 14 reference files over 100 lines have no table of contents (F6).; No evals (F9). 20 reference files plus 14 rule-engine example JSONs; no nested reference links.; Scripts: analyze_flow.py and build_flow.py have args/help/exit codes; e2e_test.sh, simulate.js, e2e_runner.js are helper tools.

### mi-signals

**strong**: One coherent, evidence-derived procedure with clear decision rules, a working analyser and templates; weaker only on description triggers, a thin example and missing evals. (0 gap, 4 partly; core library)

Improve first:
1. Put the 'use it when' triggers into the description.
2. Replace the two-tag example with a realistic multilingual-tag mapping row and add a re-run-until-clean loop.
3. Add evals (raw PLC tag, local-language name, collision) and tables of contents on the 11 long references.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md: "Analyse a machine's signals and standardize them so a second plant can use them: names, collisions, gaps, public data models." | Move the 'Use it when a machine is newly connected, when a use case cannot be built because a signal is missing' triggers from the Purpose section into the description. |
| J9 Concrete examples | partly | SKILL.md: "u2 = raw PLC tag -> blocker, analyser exit code 2; u1 = canonical, no finding" | The example has two invented tags; add one realistic row showing a local-language tag mapped to a canonical name with alias, unit and collection method. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md: "is invalid input; fix the export and run again." | The analyser loop is only stated for bad input; add an explicit re-run after steps 8-9 (renames, registered outputs) until no blockers remain. |
| J12 Consistent terminology | partly | SKILL.md: "edge-platform data points (`{uuid, label}`) or a tag/symbol export" | Pick one term among tag, signal, data point and point and define it once; the handoff table also repeats `mi-equipment` in two rows. |

Facts: Body 2614 tokens, 127 lines; well under limits.; 11 reference files over 100 lines lack a table of contents (F6).; No evals (F9). No nested reference links.

### ops-analytics-asset

**adequate**: Strong ritual-first gate and clear procedure, but the description lacks triggers, a pointer is broken, and scope overlaps heavily with the dashboard-build skills. (0 gap, 5 partly; core library)

Improve first:
1. Resolve the scope overlap: keep asset-type choice, ritual gate and validation here; move the DATATRON build package out or behind one pointer.
2. Fix the broken `technical-guardrails.md` pointer and add read-when triggers plus TOCs to the long references.
3. Add triggers to the description and a real Gotchas section; write evals (asset-type choice, action-owner refusal).

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md: "Design and build the dashboard, report, workflow, app or agent a plant actually opens, tied to a daily routine." | Add explicit triggers ('Use when asked for a dashboard, report or app, or choosing between them') and name the daily-ritual terms plants use. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "The department's DATATRON dashboard package `ops-grafana-dashboards` (master) is transcribed in" | The Lane 1a paragraph re-describes a 634-line reference and the estate section restates the baseline file; cut both to one pointer line each. |
| J7 Gotchas in SKILL.md | partly | SKILL.md: "- Do not present unvalidated insight as fact." | The 'Do not' list is generic; promote the real traps (delivery without explanation leading to NEVER utilization, paper reconciliation, literal UUID binding) into a named Gotchas section. |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md: "(`catalog-usecase`, `references/technical-guardrails.md`)" | This pointer does not resolve inside this skill's references folder; fix it, and add read-when triggers to the 10-row table (it only says 'Use it for') and a table of contents to the 634-line ops-grafana-dashboards.md. |
| J15 One coherent unit | partly | SKILL.md: "the extension skills `ops-dashboard-datatron` and `ops-dashboard-engine` hold the deeper builder" | Scope blurs with the dashboard-build skills: the description says 'Not for the Grafana JSON build' yet the body hosts the 634-line Grafana package and a Lane 1a build mode; move the build content to ops-dashboard-datatron and keep this skill on asset choice and ritual (note engine is a core skill, not an extension). |

Facts: Body 3346 tokens, 171 lines; fine.; 7 reference files over 100 lines have no table of contents; ops-grafana-dashboards.md is 634 lines.; No evals (F9). No scripts.; Description 181 chars, no trigger clause.

### ops-dashboard-datatron

**needs-work**: A 633-token stub: gates are stated but the patterns, checklist, template and example it depends on are explicitly not yet in the skill. (5 gap, 7 partly; extension library)

Improve first:
1. Transcribe (or link into) the query/variable patterns, scaled-PLC handling and QA checklist so the steps are executable.
2. Add a UUID-enablement list template, a QA result template and one worked example.
3. Rewrite the 600-character description in one point of view and decide whether this skill and ops-analytics-asset's Lane 1a section are one unit.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | SKILL.md: "the department's ops-dashboard-datatron, the engine of" | Rewrite to one point of view and user intent; drop internal names and implementation (PostgreSQL / TimescaleDB, scaled PLC values) and cut from 600 characters. |
| J4 Specificity matches fragility | gap | SKILL.md: "- ⟨Query and variable patterns, scaled-PLC handling, the QA checklist⟩ - transcribe from `ops-grafana-dashboards.zip`." | The fragile parts (query and variable patterns, scaled-PLC handling, QA checklist) have no steps; transcribe them or link them to ops-analytics-asset/references/ops-grafana-dashboards.md. |
| J5 Procedures over declarations | partly | SKILL.md: "**Build with the proven patterns** (queries, variables, scaled-PLC handling) through `ops-dashboard-engine`." | Each step names an outcome but not how; add the concrete how for signal selection and UUID enablement (what to look at in the tag list, what the enablement list looks like). |
| J7 Gotchas in SKILL.md | partly | SKILL.md: "Do not extend a catalogued template locally; route the new need to Lane 2." | The three 'Do not' items are process rules; add real gotchas (scaled PLC values, disabled UUIDs, two time-filter dialects). |
| J8 Output templates | gap | absent: no template or format for the datapoint UUID list or the QA result in SKILL.md, outputs.yaml or references. | Add a template for the 'UUIDs to enable' list and the QA result record. |
| J9 Concrete examples | gap | absent: no example in SKILL.md; references/background.md has none. | Add one worked example (signal selection, UUID list, QA result for one press centre). |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md: "**Run the QA checklist**; it is the objective approval gate." | The gate is named but the checklist itself is 'not yet here'; include it so the validation loop is executable. |
| J11 Progressive disclosure: says when to read what | gap | absent: references/ holds only background.md, outputs.md and index.md; SKILL.md points to `ops-grafana-dashboards.zip` outside the skill and never to the transcribed ops-analytics-asset/references/ops-grafana-dashboards.md. | Move or link the DATATRON package into references/ and say when to read each part. |
| J12 Consistent terminology | partly | SKILL.md: "**Select the signals** from the DATATRON tag list for the equipment family (KKA cooling, press centre, utilities)." | Use one term for signal / datapoint / tag, and keep DATATRON for the system only. |
| J13 Explains the why | partly | SKILL.md: "Disabled signals are made explicit before the build starts; the plant" | State why (a panel on a disabled signal renders flat or empty) so the agent applies the rule in edge cases. |
| J15 One coherent unit | partly | SKILL.md: "The package holds the query and variable patterns and the QA checklist and is the master; this skill carries the procedure and the gates." | The skill is a shell around content that lives elsewhere and duplicates the Lane 1a mode of ops-analytics-asset; either absorb the package here or merge the shell into the sibling. |
| J16 Grounded in real expertise | gap | SKILL.md: "- ⟨Query and variable patterns, scaled-PLC handling, the QA checklist⟩ - transcribe from `ops-grafana-dashboards.zip`." | No expertise is in the skill itself and status is draft; transcribe the department package with its sources before marking the skill stable. |

Facts: Description 600 chars (long, valid, mixed point of view).; Body 633 tokens, 49 lines; status: draft.; No evals (F9). Only 3 reference files, none substantive.; No scripts.

### ops-dashboard-engine

**adequate**: Expert, rule-driven skill with a real audit checklist and builder, but 7280 tokens, repeated rules, a wrong Pattern cross-reference and broken list fragments from conversion. (0 gap, 4 partly; core library)

Improve first:
1. Cut the body below 5000 tokens by moving Step 3 patterns, variable defaults, Archetype detail and the 8-row example table to references, keeping hard rules, steps and the checklist.
2. Fix the Pattern D/E cross-reference and the dangling 'Signs:' / 'Choose between:' items, and add a 'Use when' clause to the description.
3. Add TOCs to the 9 long references, validation to dashboard_builder.py, and evals (downtime manager view, telemetry analyst view, portability failure).

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md: "Build importable Grafana JSON dashboards over SQL for operations data, with portable queries, variables and ECharts panels." | Add a 'Use when' clause with user words (Grafana dashboard JSON, downtime, telemetry, import); only the negative scope is stated. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "that bypasses macro expansion and is a Rule 1 violation." | At about 7280 tokens the body is over the 5000 recommendation and restates the two hard rules in Rule 1, Pattern A, Step 6, the closing note and troubleshooting; move Step 3 patterns, variable defaults and the example file table into references. |
| J12 Consistent terminology | partly | SKILL.md: "`generate_series` + `LEFT JOIN` (Pattern D)" | The table cites Pattern D for zero-fill but zero-fill is Pattern E (D is nullable end times); also repair the dangling 'Signs:' and 'Choose between:' lines left by list conversion. |
| J14 Scripts solve, handle errors, state dependencies | partly | references/dashboard_builder.py: "Designed for PostgreSQL/TimescaleDB datasources, the bilibala-echarts-panel plugin," | The generator lives in references/ not scripts/, has no input validation or error messages (duplicate panel ids, bad variables) and hard-codes pluginId postgres although the skill requires DuckDB portability; add validation and a usage line. |

Facts: Body estimate 7280 tokens, over the 5000 F4 threshold; 488 of 500 lines.; 9 reference files over 100 lines have no table of contents (F6); troubleshooting.md 372 lines.; No evals (F9). No scripts folder; the generator is references/dashboard_builder.py (497 lines).; Vendored/portable skill with OD-INTEGRATION.md and usage_guide.md outside references/ (one level deep, linked from SKILL.md).

### ops-event-model

**adequate**: A clear, coherent method with canvas templates and good gotchas, but draft status, deck-only grounding, no inline example or check, and a long implementation-heavy description. (0 gap, 6 partly; extension library)

Improve first:
1. Add a fully filled worked example and a pass/fail check before handover.
2. Link each procedure step to the reference to open, and add because-clauses to the Do-not list.
3. Shorten the description to user intent, and ground the method in a public source plus one real plant case.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | SKILL.md: "Reduce a plant request that looks unique to the objects, events and time axis it is really about" | Lead with the user's intent in one short sentence and drop the archetype/method/ETL implementation detail; 746 characters is long. |
| J9 Concrete examples | partly | references/worked-examples.md: "All examples are illustrative, built from request patterns in the decks. Names are `<placeholders>`." | Inline one fully filled reduction (carrier-in-oven) in SKILL.md with real-looking tags instead of placeholders only in a reference. |
| J10 Checklist, validation loop, plan-validate-execute | partly | SKILL.md: "- the request is restated as object(s), event(s) and time axis, in the" | The done-criteria are orphaned list fragments, not a check; add a pass/fail checklist before handover (every signal classified, every event source/derived with method). |
| J11 Progressive disclosure: says when to read what | partly | SKILL.md: "Cross-process, per-process or unique (see the reference) and the action that" | Procedure steps point at 'the reference' without naming the file; link object-event-reduction.md at step 3 and archetype-method-etl.md at steps 6-8, and say when to open worked-examples.md. |
| J13 Explains the why | partly | SKILL.md: "Do not hide ETL effort; do not model every signal, only those the question needs." | Most 'Do not' lines are bare directives; add the because-clause (e.g. why a sensor value is not an event) in SKILL.md, not only in the reference. |
| J16 Grounded in real expertise | partly | references/object-event-reduction.md: "Source basis: Operations Digitalization decks on object-driven event mining and on transaction versus" | Add public event-log sources (e.g. process-mining event-log standards) and a real plant case, since the basis is internal decks and several points stay '<to confirm>' (status: draft). |

Facts: Description 746 chars (long, valid).; Body 2005 tokens, 114 lines; status draft.; No evals (F9). References under 100 lines, so no TOC finding.; No scripts.

### process-derivation

**adequate**: The best-structured procedure of the batch (gate, control points, checker, example), but self-declared unvalidated draft with a description lacking triggers and no evals or real run. (0 gap, 7 partly; core library)

Improve first:
1. Run it on one real validated prototype record, add 3 evals (gate refusal, BPMN with missing exception path, adoption plan) and record what changed.
2. Add 'Use when' triggers and user-intent wording to the description.
3. Harden check_derivation.py (file errors, record verification) and trim textbook method restatement from SKILL.md.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J1 Description says what and when | partly | SKILL.md: "Derive a lived business process from a validated use case: gate on request, demand and passed prototype;" | Add a 'Use when' clause (a prototype passed and the plant asks what process now changes) and the words a requester would use. |
| J2 Description: one point of view, user intent | partly | SKILL.md: "Derive a lived business process from a validated use case" | Reword the internal vocabulary ('lived business process', 'gate on request, demand') into the user's goal: turn a passed prototype into a process the plant can run and keep. |
| J3 Concise: only what the agent lacks | partly | SKILL.md: "Phases follow the BPM lifecycle: identify, discover, analyse, redesign, implement, monitor [PD1]." | Textbook BPM, ADKAR and Kotter restatement adds tokens the model already knows; keep the gate, control points and house-specific rules and leave the method names to references. |
| J12 Consistent terminology | partly | SKILL.md: "A requirement with acceptance criteria and growth boundaries, recorded as demand" | 'Demand' and 'requirement', and 'adoption and embedding plan' / 'change plan', are used interchangeably; fix one term for each. |
| J13 Explains the why | partly | SKILL.md: "a process derived from a click-dummy that nobody validated is a guess with a diagram" | Only the gate and a few pitfalls carry a reason; add a short because-clause to the control points (why owner role not person, why design the monitoring now). |
| J14 Scripts solve, handle errors, state dependencies | partly | scripts/check_derivation.py: "Exit code 0 prints READY; 1 prints the findings. Nothing is changed." | Reading a missing or unreadable file raises an uncaught traceback and only cell contents are checked (a typed 'passed' satisfies the gate); catch OSError with a clear message and state in --help that it checks structure, not truth of the records. |
| J16 Grounded in real expertise | partly | SKILL.md: "No public source was found for this exact trigger; the composition is this skill's own inference." | Honest sourcing, but nothing is validated by a real run or plant practitioner and some sources were only read in part (e.g. abstract only); run it on one real prototype record and record the result. |

Facts: Body 2720 tokens, 129 lines; description 208 chars.; No evals (F9); status draft; sources_read 2026-11-16.; Scripts folder contains committed __pycache__ .pyc files.; References are short; no TOC findings; no nested links.
