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
- **Evidence check:** 777 of 777 evidence quotes were found word for word in the skill's own files by a script; the rest mix a quote with a description, or are plain statements of absence (2 of those). A reviewer can be wrong: confirm a rating before acting on it.

## Overall

| | strong | adequate | needs-work |
|---|---|---|---|
| All 51 skills | 25 | 26 | 0 |
| 26 core skills | 12 | 14 | 0 |

## Measured facts

| Fact (source key) | Result |
|---|---|
| F1 name valid (AS, AB) | 51 of 51 |
| F2 description non-empty, at most 1024 characters (AB, AS) | 51 of 51; longest 810 |
| F3 body under 500 lines (AB, AS) | 51 of 51; longest 283 lines |
| F4 body under about 5,000 tokens, estimated (AS) | 50 of 51; over: mi-flow |
| F5 references one level deep (AB, AS) | 51 of 51; nested links in: none |
| F6 long references have a table of contents (AB) | 51 of 51 |
| F7 forward slashes only (AB) | 51 of 51 |
| F9 evaluations exist (AB, AE) | 51 of 51 |

## Criteria across all skills

| Criterion | meets | partly | gap | n/a |
|---|---|---|---|---|
| J1 Description says what and when | 51 | 0 | 0 | 0 |
| J2 Description: one point of view, user intent | 41 | 10 | 0 | 0 |
| J3 Concise: only what the agent lacks | 21 | 30 | 0 | 0 |
| J4 Specificity matches fragility | 51 | 0 | 0 | 0 |
| J5 Procedures over declarations | 49 | 2 | 0 | 0 |
| J6 Defaults, not menus | 49 | 2 | 0 | 0 |
| J7 Gotchas in SKILL.md | 49 | 2 | 0 | 0 |
| J8 Output templates | 51 | 0 | 0 | 0 |
| J9 Concrete examples | 50 | 1 | 0 | 0 |
| J10 Checklist, validation loop, plan-validate-execute | 42 | 9 | 0 | 0 |
| J11 Progressive disclosure: says when to read what | 48 | 3 | 0 | 0 |
| J12 Consistent terminology | 31 | 20 | 0 | 0 |
| J13 Explains the why | 48 | 3 | 0 | 0 |
| J14 Scripts solve, handle errors, state dependencies | 12 | 2 | 0 | 37 |
| J15 One coherent unit | 33 | 18 | 0 | 0 |
| J16 Grounded in real expertise | 32 | 19 | 0 | 0 |

Where most skills fall short, by gaps first: J3 Concise: only what the agent lacks (0 gap, 30 partly); J12 Consistent terminology (0 gap, 20 partly); J16 Grounded in real expertise (0 gap, 19 partly); J15 One coherent unit (0 gap, 18 partly); J2 Description: one point of view, user intent (0 gap, 10 partly).

## Per skill, next to the SkillEvaluator rating

The SkillEvaluator rating checks a fixed set of rules and headings (the registry's configuration); this review judges the text against the published practices. They measure different things.

| Skill | Library | Review | Gaps | Partly | SkillEvaluator | Description chars | Body lines | Evals |
|---|---|---|---|---|---|---|---|---|
| [`bc-assess`](#bc-assess) | core | adequate | 0 | 3 | A 91.8 | 625 | 121 | yes |
| [`bc-build`](#bc-build) | core | adequate | 0 | 2 | B 89.2 | 627 | 176 | yes |
| [`bc-capital-request`](#bc-capital-request) | core | adequate | 0 | 2 | A 91.8 | 598 | 135 | yes |
| [`bc-cost`](#bc-cost) | extension | adequate | 0 | 4 | B 88.5 | 678 | 126 | yes |
| [`bc-portfolio`](#bc-portfolio) | extension | adequate | 0 | 3 | B 88.5 | 651 | 144 | yes |
| [`catalog-compatibility`](#catalog-compatibility) | extension | strong | 0 | 2 | B 88.5 | 707 | 118 | yes |
| [`catalog-guardrails`](#catalog-guardrails) | core | strong | 0 | 1 | A 95.2 | 618 | 104 | yes |
| [`catalog-standardization`](#catalog-standardization) | extension | adequate | 0 | 4 | B 89.0 | 758 | 129 | yes |
| [`catalog-systems`](#catalog-systems) | core | strong | 0 | 4 | A 95.2 | 720 | 110 | yes |
| [`catalog-template`](#catalog-template) | extension | adequate | 0 | 2 | A 91.0 | 778 | 120 | yes |
| [`catalog-usecase`](#catalog-usecase) | core | adequate | 0 | 3 | A 95.2 | 810 | 141 | yes |
| [`comms-brief`](#comms-brief) | core | strong | 0 | 2 | A 91.8 | 672 | 124 | yes |
| [`comms-followup`](#comms-followup) | core | strong | 0 | 2 | A 91.8 | 681 | 103 | yes |
| [`comms-showcase`](#comms-showcase) | core | adequate | 0 | 3 | A 95.2 | 514 | 106 | yes |
| [`deploy-acceptance`](#deploy-acceptance) | core | strong | 0 | 1 | A 95.2 | 571 | 123 | yes |
| [`deploy-appstore`](#deploy-appstore) | core | adequate | 0 | 4 | A 95.2 | 683 | 111 | yes |
| [`deploy-cybersec`](#deploy-cybersec) | extension | adequate | 0 | 3 | B 89.8 | 662 | 132 | yes |
| [`deploy-handover`](#deploy-handover) | core | adequate | 0 | 3 | A 95.2 | 657 | 155 | yes |
| [`deploy-migration`](#deploy-migration) | extension | strong | 0 | 4 | B 87.5 | 748 | 141 | yes |
| [`deploy-project-order`](#deploy-project-order) | extension | strong | 0 | 2 | B 87.5 | 807 | 138 | yes |
| [`dept-context`](#dept-context) | core | adequate | 0 | 3 | A 91.5 | 598 | 219 | yes |
| [`dept-context-freshness`](#dept-context-freshness) | extension | strong | 0 | 2 | B 85.2 | 731 | 142 | yes |
| [`dept-decision-rights`](#dept-decision-rights) | core | adequate | 0 | 3 | A 91.5 | 651 | 144 | yes |
| [`dept-governance`](#dept-governance) | extension | adequate | 0 | 3 | A 93.5 | 810 | 155 | yes |
| [`dept-intake`](#dept-intake) | core | strong | 0 | 2 | A 91.5 | 715 | 154 | yes |
| [`dept-plant-diagnosis`](#dept-plant-diagnosis) | extension | strong | 0 | 1 | B 89.5 | 705 | 136 | yes |
| [`dept-plant-onboarding`](#dept-plant-onboarding) | extension | adequate | 0 | 3 | B 86.0 | 692 | 114 | yes |
| [`dept-retro`](#dept-retro) | extension | strong | 0 | 1 | B 86.2 | 662 | 103 | yes |
| [`dept-risk`](#dept-risk) | extension | strong | 0 | 0 | B 89.8 | 681 | 102 | yes |
| [`funnel-evaluation`](#funnel-evaluation) | extension | strong | 0 | 2 | B 86.5 | 805 | 129 | yes |
| [`funnel-features`](#funnel-features) | extension | strong | 0 | 0 | B 81.5 | 590 | 80 | yes |
| [`funnel-first-aid`](#funnel-first-aid) | extension | adequate | 0 | 4 | A 93.5 | 764 | 136 | yes |
| [`funnel-prototype`](#funnel-prototype) | core | adequate | 0 | 3 | A 95.2 | 684 | 149 | yes |
| [`funnel-requirements`](#funnel-requirements) | core | strong | 0 | 3 | A 95.2 | 676 | 142 | yes |
| [`funnel-use-case`](#funnel-use-case) | core | adequate | 0 | 4 | A 95.2 | 666 | 192 | yes |
| [`funnel-workshop`](#funnel-workshop) | extension | adequate | 0 | 2 | A 91.0 | 695 | 131 | yes |
| [`invest-screen`](#invest-screen) | core | adequate | 0 | 3 | A 95.2 | 804 | 156 | yes |
| [`know-ai-generation`](#know-ai-generation) | extension | adequate | 0 | 5 | B 88.2 | 666 | 141 | yes |
| [`know-sharepoint-export`](#know-sharepoint-export) | extension | strong | 0 | 1 | B 86.5 | 625 | 108 | yes |
| [`know-skill-authoring`](#know-skill-authoring) | extension | strong | 0 | 2 | A 90.0 | 762 | 110 | yes |
| [`know-training`](#know-training) | extension | adequate | 0 | 3 | A 93.5 | 699 | 124 | yes |
| [`metrics-scorecard`](#metrics-scorecard) | extension | strong | 0 | 1 | A 91.0 | 728 | 142 | yes |
| [`mi-data-availability`](#mi-data-availability) | core | strong | 0 | 1 | A 91.8 | 665 | 150 | yes |
| [`mi-equipment`](#mi-equipment) | core | adequate | 0 | 3 | A 95.2 | 725 | 175 | yes |
| [`mi-flow`](#mi-flow) | core | adequate | 0 | 3 | A 93.0 | 655 | 283 | yes |
| [`mi-signals`](#mi-signals) | core | strong | 0 | 1 | A 95.2 | 648 | 140 | yes |
| [`ops-analytics-asset`](#ops-analytics-asset) | core | strong | 0 | 2 | A 95.2 | 612 | 154 | yes |
| [`ops-dashboard-datatron`](#ops-dashboard-datatron) | extension | adequate | 0 | 3 | A 93.5 | 615 | 116 | yes |
| [`ops-dashboard-engine`](#ops-dashboard-engine) | core | strong | 0 | 1 | B 89.2 | 633 | 252 | yes |
| [`ops-event-model`](#ops-event-model) | extension | strong | 0 | 1 | A 92.0 | 729 | 134 | yes |
| [`process-derivation`](#process-derivation) | core | strong | 0 | 1 | A 95.2 | 645 | 141 | yes |

**Where the two disagree:** `catalog-compatibility` (SkillEvaluator B, review strong), `deploy-migration` (SkillEvaluator B, review strong), `deploy-project-order` (SkillEvaluator B, review strong), `dept-context-freshness` (SkillEvaluator B, review strong), `dept-plant-diagnosis` (SkillEvaluator B, review strong), `dept-retro` (SkillEvaluator B, review strong), `dept-risk` (SkillEvaluator B, review strong), `funnel-evaluation` (SkillEvaluator B, review strong), `funnel-features` (SkillEvaluator B, review strong), `know-sharepoint-export` (SkillEvaluator B, review strong), `ops-dashboard-engine` (SkillEvaluator B, review strong).

## House rules against the published practices

- `bc-assess`: Rationale restricted to a Why column in tables and background.md keeps J13 reasoning thin for the procedure steps.
- `bc-build`: Short why-columns in tables stand in for reasoning; several rules (ledger counts) carry no reason.
- `bc-portfolio`: The structure-only rule favours definition tables over procedural teaching in the portfolio read.
- `catalog-standardization`: The ban on prose paragraphs pushes the rationale for the Do-not rules into background.md, away from where the agent decides.
- `catalog-systems`: The structure-only rule leaves the Human gate, Do not and Pitfalls sections restating one another.
- `catalog-template`: Structure-only form pushes the owner and gap explanations into several short sections.
- `catalog-usecase`: Structure-only form makes the human-gate rules appear in three sections.
- `comms-brief`: Structure-only form forces the audience variants into long list items.
- `comms-showcase`: Structure-only form leaves the Procedure as a one-line pointer to the gate.
- `deploy-acceptance`: Structure-only body leaves the rationale for the FAT/SAT/UAT choice in references; the reader needs one more hop
- `deploy-appstore`: The status-ready-awaiting-sign-off block is process metadata that the structure-only body must carry as list items
- `deploy-cybersec`: Marked-unknown placeholders are required by the honesty rule but make the body hard to act on
- `deploy-handover`: Structure-only body forces the three-question test and the rule into terse list items
- `deploy-migration`: Structure-only body turns decision rationale into one-line rules
- `deploy-project-order`: Structure-only body keeps only one example of a good target and flag list
- `dept-context`: Structure-only body forces the lane and vocabulary content into long tables and fragment bullets, which makes the body large.
- `dept-context-freshness`: Structure-only body pushes the explanation of the rule into one-line bullets; acceptable here.
- `dept-decision-rights`: Structure-only body turns the explanation of the stale-row rule into repeated bullets.
- `dept-governance`: No-prose body keeps each routine terse; the five procedures add up to one long body.
- `dept-intake`: Structure-only body turns the one-line record into a prose-like bullet instead of a literal template.
- `dept-plant-diagnosis`: Structure-only body reduces the signature and questions to bullets, which still read clearly.
- `dept-plant-onboarding`: The structure-only body leaves stage rows listing skills without saying why each is needed; the why sits in background.md.
- `funnel-evaluation`: The no-prose rule pushes the score logic into dense bullet lists.
- `funnel-prototype`: Structure-only body forces the rationale for the label ladder into references, so the why is thin in SKILL.md.
- `funnel-requirements`: Structure-only body leaves many steps without rationale (J13).
- `funnel-use-case`: Structure-only body strips reasons from list items (J13).
- `invest-screen`: Structure-only body pushes mode-specific detail into many reference files, lengthening the reference table.
- `know-training`: The ban on prose and the placeholder convention push open questions into a long list in the body.
- `mi-equipment`: The structure-only rule favours dense tables and list items, which pushes term definitions and rationale into body tables instead of background.
- `mi-flow`: Listing every reference file in the SKILL.md table produced 13 near-identical example rows that add length without saying when to open each.
- `mi-signals`: The required outputs pointer and Purpose block repeat description content.
- `ops-dashboard-engine`: Listing every reference file in the SKILL.md table adds eight example rows with the same trigger text.

## The skills

### bc-assess

**adequate**: Clear, well-gated scoring procedure with checklist and example, held back by a code-heavy description, duplicated do-not text and a script that needs hand-editing. (0 gap, 3 partly; core library)

Improve first:
1. Rewrite the description around user intent without criterion codes
2. Remove the Do-not block duplicating Pitfalls
3. Let build_bc_short.py take case content from input instead of editing the script

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | Scores a drafted business case against the OD house rubric (C1-C5 core integrity, D1-D9 structure, E1-E6 discipline) | Lead with the user intent (check whether a case is signable) and drop the criterion codes C1-E6 from the description; keep them in the body. |
| J3 Concise: only what the agent lacks | partly | Do not fix the case while assessing it; return it to `bc-build` with the findings. | The Do-not block repeats three Pitfalls rows almost word for word; keep one of the two lists. |
| J14 Scripts solve, handle errors, state dependencies | partly | The script carries the Gemba App worked-example text with placeholders. Replace the slide text with the case's own figures | The deck script hard-codes the example slide text and defers case content to hand-editing; read the figures from the backbone or a --case JSON. |

### bc-build

**adequate**: Strong honesty rules, example and checklist, but long and mixing three jobs (first estimate, backbone, ledger) with duplicated lists. (0 gap, 2 partly; core library)

Improve first:
1. Merge the first-estimate steps into the Procedure
2. Delete the Do-not block that repeats Pitfalls
3. Consider moving ledger row rules to a reference

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | the first estimate is its steps 1-3 in short form | The five-step first estimate restates Procedure steps 1-3 and the Do-not block repeats Pitfalls; merge them to cut length. |
| J15 One coherent unit | partly | Builds and records the value side of an OD business case and keeps the savings ledger honest | One skill covers a casual first estimate, the backbone and the ledger row rules; consider splitting the ledger rules from the case build. |

### bc-capital-request

**adequate**: Well-structured 14-step procedure with route, refusal gate and checks, but a heavy reference set of 12 files, repeated prohibitions and a script that needs editing. (0 gap, 2 partly; core library)

Improve first:
1. Cut the Do-not block to non-obvious rules
2. Make build_ecr.py take full case content as input
3. Consolidate overlapping reference files (build-engine and ecr-builder-workflow)

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Do not split one investment into several requests to land under a threshold. | The Do-not list has nine items, several repeating Pitfalls and the Human gate section; keep only the non-obvious ones. |
| J14 Scripts solve, handle errors, state dependencies | partly | The slide content inside `build_ecr.py` is the illustrative worked example; edit it for the case before showing the deck. | build_ecr.py bakes in example content and only overrides a few fields via --case; accept the full deck content as JSON. |

### bc-cost

**adequate**: Honest, gated cost procedure with example and open markers, but three products in one skill, blurry terminology and duplicated do-not text. (0 gap, 4 partly; extension library)

Improve first:
1. Fix one term per product
2. Remove Do-not items repeated in Pitfalls
3. Split or clearly branch the three products

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | Prepares the cost side of an OD business case and the investment input pack: one-time build, licences and hardware | The description is long and lists deliverable parts; shorten to the user intent plus triggers. |
| J3 Concise: only what the agent lacks | partly | Do not plan a wave around the medium or small edge device. | Do-not items repeat Pitfalls and the Still open list; remove duplicates. |
| J12 Consistent terminology | partly | Naming: the skill is `bc-cost`; its deliverables are the **investment input pack** (a wave), the **Lane 1b cost template** | Pack, wave pack, estimate, template and cost side all name overlapping things; fix one term per product and use it everywhere. |
| J15 One coherent unit | partly | Wave pack (investment input pack) | Three products (wave pack, Lane 1b template, case estimate) with different approvers share one skill; consider splitting or sharper separation. |

### bc-portfolio

**adequate**: Strong on data-misreading guardrails and example, but two jobs in one skill and a body that is partly declarative field reference. (0 gap, 3 partly; extension library)

Improve first:
1. Split prioritization into its own skill
2. Move field-definition tables to a reference
3. Drop Do-not items repeated in Pitfalls

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | / `IDEA` / Recorded, not yet committed to a plan / | Field-definition tables explain statuses the data already documents; keep only the cuts that mislead. |
| J5 Procedures over declarations | partly | Cut by plant / region / capability / cluster / status / asset; never by one dimension alone | Much of the body declares what fields mean; reorder as a procedure with the field notes in a reference. |
| J15 One coherent unit | partly | Second job with its own trigger: ranks competing candidate use cases | Analysis and prioritization are two jobs with separate references; split prioritization into its own skill. |

### catalog-compatibility

**strong**: Tight single-purpose procedure with a four-value verdict, decision table, example and honest open items; only the description and some duplication need trimming. (0 gap, 2 partly; extension library)

Improve first:
1. Rewrite the description around the user question
2. Remove Do-not lines repeated in Pitfalls
3. Move What is still open to background.md

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | Builds the plant grid (controller vendor, field network, ingress variant, tool versions, tag language, instance state) | Replace the implementation detail of grid columns with the question a user asks, "will this hold at the other plants". |
| J3 Concise: only what the agent lacks | partly | Do not decide the data-model change yourself: you recommend; the decision route is in `dept-decision-rights`. | Do-not restates Pitfalls and the Human gate section; remove the duplicates. |

### catalog-guardrails

**strong**: A compact guardrail table with a why and failure consequence per row, a clear check-and-re-run loop, example and honest status of unconfirmed rules. (0 gap, 1 partly; core library)

Improve first:
1. Align the G8-G18/G19 range
2. Replace the undefined 'Part A match record' with a link
3. Add a second example with a failed hard-stop guardrail

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J12 Consistent terminology | partly | candidate guardrails G8 to G18 | The text says G8 to G19 in one place and G8 to G18 in the references table; align the range. |

### catalog-standardization

**adequate**: Good adoption-based framing and a worked example, but two jobs in one skill, a mixed description and missing why on the Do-not rules. (0 gap, 4 partly; extension library)

Improve first:
1. Split promotion mode into its own skill or sharply branch it
2. Add a completion check for the five review sections
3. Add reasons to the Do-not rules

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | Check one use case against the cross-plant capability templates and the reference | The description opens in the imperative while the rest is declarative and lists implementation (C01-C12 tags); use one point of view and state the user's goal. |
| J10 Checklist, validation loop, plan-validate-execute | partly | Any unticked box means the verdict is "not ready, missing: ...", never "rejected". | The CSP checklist exists but there is no loop that checks all five review sections before handoff; add a completion check. |
| J13 Explains the why | partly | Do not create a new capability or process group to accommodate one plant. | The Do-not list gives most rules without a reason; add a because clause to each. |
| J15 One coherent unit | partly | A second job lives here: decide whether a recurring ad-hoc asset becomes a standard use case | Standardization and promotion are two jobs with their own sub-skill folder; consider two skills. |

### catalog-systems

**strong**: Clear gated procedure with checklist, examples, pitfalls and reasons, held back by some repetition and term drift. (0 gap, 4 partly; core library)

Improve first:
1. Say the no-price-from-memory rule once.
2. Unify the terms standardized system / standard system / route candidate.
3. Cite sources behind route classes and tool boundaries.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | look up the machine's route, test the tool boundary, and write the system match record with kit, cost-template inputs and Cyber Security status | Cut the procedure-like clause and state the user outcome (can the plant order a standard kit, yes or no). |
| J3 Concise: only what the agent lacks | partly | An agent never quotes a kit price or lead time that is not in the kit list. | State the no-price-from-memory rule once instead of in Pitfalls, Human gate and Do not. |
| J12 Consistent terminology | partly | **Route candidate**: a route written in full and proven in at least two plants, but with no kit, price or lead time on record. | Use one term for the system (standardized system, not also standard system or candidate standardized system) and one for the record. |
| J16 Grounded in real expertise | partly | absent: SKILL.md cites no source documents for route classes or tool boundaries; grounding lives only in the reference files | Name in the table the source (guide, machine list) each reference is derived from. |

### catalog-template

**adequate**: Sound lookup procedure with decision table and reasons, but no closing checklist and some repeated sections. (0 gap, 2 partly; extension library)

Improve first:
1. Add a closing checklist.
2. Remove the When-to-use section duplicating the description.
3. State the fallback owner once confirmed.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | When another OD skill names a deliverable and asks you to fill it (almost all of them do). | Drop the When-to-use section that repeats the description and Purpose. |
| J10 Checklist, validation loop, plan-validate-execute | partly | run the leak check in `references/process-chain-practice.md`: no placeholder text and no sample figure from the master remains. | Add a short closing checklist (master opened at location, fork check, leak check, record attached) in SKILL.md. |

### catalog-usecase

**adequate**: Strong procedure, checklist, examples and pitfalls, but it covers two jobs, repeats rules and two of four catalogued conditions are unconfirmed proposals. (0 gap, 3 partly; core library)

Improve first:
1. Resolve the two proposal conditions.
2. Trim repeated gate statements.
3. Clarify scope of graduation versus catalog-standardization.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Taking the CSP decision, approving a connection, signing off Cyber Security, or deciding go-live for the plant. | Remove restatements of the human-gate rules in Pitfalls and Human gate; keep them in Shared rules. |
| J15 One coherent unit | partly | Also sets what a proven Lane 2 result needs to graduate into the catalog. | Consider moving the graduation procedure (step 26) into catalog-standardization, which already owns the CSP step, or state why it stays. |
| J16 Grounded in real expertise | partly | Conditions 1 and 4 come from the sources; **2 and 3 are proposals** to confirm with the OD lead. | Confirm conditions 2 and 3 with the OD lead and cite the source of all four. |

### comms-brief

**strong**: Concrete procedure with a validated script loop, examples, gotchas and honest handling of unknown IC details. (0 gap, 2 partly; core library)

Improve first:
1. Unify proof point / claim / result wording.
2. Replace hypotheses with the IC brief once supplied.
3. Trim step 4 audience list.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J12 Consistent terminology | partly | - **Drafts**: optional help for IC (article, one-pager, slide, short post); they repeat the brief and add nothing. | Use one term for the unit (proof point vs claim vs result) and spell IC consistently. |
| J16 Grounded in real expertise | partly | Supervisors as an audience is a hypothesis from a public survey of frontline workers; IC confirms. | Replace hypotheses (supervisor audience, IC channels) with confirmed IC intake once available. |

### comms-followup

**strong**: Short, coherent skill with routing, checklist, example, pitfalls and reasons; measures are still proposals. (0 gap, 2 partly; core library)

Improve first:
1. Align title and terminology with the skill name.
2. Ground or confirm the measures.
3. Add a second, harder example (restated saving).

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J12 Consistent terminology | partly | # Showcase follow-up | Align the title and terms with the skill name (comms-followup) and replace outputs.yaml wording 'promotion' with 'story'. |
| J16 Grounded in real expertise | partly | ## Measures the log records (no targets) | Ground the four measures in a source or confirm them with the OD lead; the full set is only proposed. |

### comms-showcase

**adequate**: Good gate with reasons, verdict table and three examples, but section order is odd, Purpose duplicates the opening, and there is no checklist. (0 gap, 3 partly; core library)

Improve first:
1. Remove the duplicated Purpose and Procedure sections.
2. Add a closing checklist.
3. Confirm the consent rule.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Work the six gate steps in order ("The gate, in order"), fill the selection record, and give one verdict from the table above. | Delete the Purpose section and the one-line Procedure, which restate the opening and the gate. |
| J10 Checklist, validation loop, plan-validate-execute | partly | Work the six gate steps in order ("The gate, in order") | Add a closing checklist per gate step and say what to do when a step is unknown versus failed. |
| J16 Grounded in real expertise | partly | Gate source status: the consent or balancing rule is proposed, not confirmed; see `references/readiness-gate.md`. | Confirm the consent and balancing rule with the data-protection owner and cite it. |

### deploy-acceptance

**strong**: Procedural, with a template, a validation loop, reasoned rules and clear references; main weakness is repetition between sections. (0 gap, 1 partly; core library)

Improve first:
1. Merge the repeated protocol-before-build statements in Purpose, Procedure and Definition of done
2. Add one fuller worked protocol item (a failing one) to the body
3. Give the two reference tables one place, not two

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Acceptance is the gate between "we built it" and "it is yours". | Purpose, Inputs and output, Procedure and Definition of done restate the same protocol-before-build idea several times; merge them into one short sequence. |

### deploy-appstore

**adequate**: The gate and package are clear and honest about gaps, but the skill is thin on verified content, lacks a check loop and carries off-topic Do-not items. (0 gap, 4 partly; core library)

Improve first:
1. Add a package-check loop against release gate R1 to R11 in the Procedure
2. Move migration and prototype Do-not items out; keep only deployment-package pitfalls
3. Replace proposals with the confirmed CMO/GitOps standard once collected

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | **Status: ready (awaiting sign-off).** | The status block and the Do-not items on migration, new installations and prototypes are off-topic for packaging an app; cut them or move them to the migration skill and background. |
| J9 Concrete examples | partly | App: demo-dashboard, owner role: DBVE, sponsor: plant X (fictional) | The only example is four lines and shows no filled gate table or open-question list; add one complete package excerpt. |
| J10 Checklist, validation loop, plan-validate-execute | partly | If a field is missing or the sign-off is not granted, the package is invalid for release: list the gap with its owner and stop. | The release-gate checklist R1 to R11 sits only in a reference; add an explicit check-the-package, fix, recheck loop in the Procedure. |
| J16 Grounded in real expertise | partly | Containerization requirements, image and registry rules and resource limits are not recorded in the sources | Core content (manifest, rollout lead time, image rules) is still a proposal or open; collect the IT/CMO standard and replace the proposals. |

### deploy-cybersec

**adequate**: A sound hold-and-route procedure with good reasoning, but the standard is uncollected so much is placeholder, there is no pre-submit check, and the body has formatting slips. (0 gap, 3 partly; extension library)

Improve first:
1. Add a pre-submit completeness checklist with a recheck loop
2. Collect the Cyber Security standard and replace the marked unknowns
3. State the missing standard once; fix stray '- -' and '**' marks

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | - This skill therefore builds the **sign-off package** and the **wait-state record**. | The status block, the Open list and many inline marked-unknown items restate that the standard is missing; state it once and keep the unknowns in one list. |
| J10 Checklist, validation loop, plan-validate-execute | partly | **Fill the package** from existing outputs, not from memory | There is no completeness check before submission in the body; add a short pre-submit checklist (all package-contents items present or flagged) with a fix-and-recheck loop. |
| J16 Grounded in real expertise | partly | the sign-off standard itself is not collected | The central rule content is missing; collect the Cyber Security standard, lead time and submission channel with the OD lead and replace the marked unknowns. |

Facts: Stray '- -' in step 2 and a stray '**' after 'no authority level that shortens it.' in The rule

### deploy-handover

**adequate**: Strong content with reasoning, examples and ADKAR grounding, but it bundles several handover kinds and the body is long with no recheck loop. (0 gap, 3 partly; core library)

Improve first:
1. Split application transfer and function succession from use-case handover
2. Add a recheck loop on the definition of done
3. Cut restating sections (The rule, Adoption is the plant's decision)

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | - The three are separate states because they fail separately. | Three handover kinds plus absorbed impact and utilization procedures make the body long; The rule, Adoption-is-the-plant's-decision and Function-succession sections restate. Trim to what the agent would get wrong. |
| J10 Checklist, validation loop, plan-validate-execute | partly | Fill the protocol and hand it to the plant owner; reopen it on every scorecard cadence. | The procedure has no explicit check-and-rerun loop when the definition of done fails; add one: failed item, named owner, recheck date, repeat. |
| J15 One coherent unit | partly | Three kinds of handover, named apart | Use-case handover, application transfer, function succession, impact evaluation and utilization review are bundled; consider splitting application transfer and function succession into their own skill. |

### deploy-migration

**strong**: Clear staged procedure with a checklist, validation loop, back-out plan and reasoned rules; minor menu and unconfirmed-content issues. (0 gap, 4 partly; extension library)

Improve first:
1. Pick one default alternative to big-bang
2. Have the back-out process owner confirm the proposal
3. Trim the repeated chain and handoff tables

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | - No existing skill owns the move itself. | The chain table, Handoff contract and Where-it-sits repeat what the reference table and procedure already say; trim to the decision rules and pitfalls. |
| J6 Defaults, not menus | partly | prefer risk-based prioritisation, evergreening or redeployment of the application to the target app platform, staged. | Three alternatives are offered side by side; name one default (staged redeployment) and mention the rest briefly. |
| J12 Consistent terminology | partly | a way back: inventory | The skill alternates 'way back', 'back-out' and 'recovery', and 'scenario' and 'decision'; pick one term for the back-out and use it throughout. |
| J16 Grounded in real expertise | partly | the back-out plan content is not confirmed by the owner of the back-out process | Back-out content is synthesis; get the back-out process owner to confirm it and drop the PROPOSAL marker. |

### deploy-project-order

**strong**: Procedural with a checklist, a rerun loop, a template, a fictional example and reasoned pitfalls; scope is broad but coherent. (0 gap, 2 partly; extension library)

Improve first:
1. Fix terminology (order, PREQ, plan)
2. Decide whether the customer-mandate intake variant is a separate skill
3. Add a second example (milestone or closure report)

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J12 Consistent terminology | partly | Drafts the project order (PREQ) a steering committee sends to a project team | 'order', 'PREQ', 'plan', 'initiative' and 'project' are used interchangeably; fix one term per concept. |
| J15 One coherent unit | partly | Also covers a customer-mandated program. | Order drafting, kick-off, milestone reports, closure and a customer-mandate intake variant sit in one skill; consider a separate skill or a short reference for the intake variant. |

### dept-context

**adequate**: Precise vocabulary, honesty rules and a clear reply template, but the body is broad and repeats material owned by neighbouring skills. (0 gap, 3 partly; core library)

Improve first:
1. Reduce scope: drop sections duplicated in dept-decision-rights and dept-intake
2. State the description in user terms
3. Give the data path and lane table their own reference files

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | Gives every OD skill the same ground truth | Open with the user-facing task (resolve a term, lane or figure) instead of what the skill gives other skills. |
| J3 Concise: only what the agent lacks | partly | The function proposes; other people decide. Most gates sit outside OD, because OD does not own spend, IT platforms or the plant's daily use. | Cut the Who decides and Handoff sections that repeat dept-decision-rights; keep one pointer. |
| J15 One coherent unit | partly | one vocabulary, the three new-state lanes, who decides what, where the truth lives, and the honesty rules | Move the lane model, the data path and the gates into their own references and keep the vocabulary and honesty rules as the core. |

### dept-context-freshness

**strong**: Clear read-only procedure with an exact script, exit-code handling, decision table and pitfalls; only reference triggers and source terms are loose. (0 gap, 2 partly; extension library)

Improve first:
1. Rewrite the reference table with 'Open when' triggers
2. Unify the term for the source layers
3. Add a short gotcha on the figure finder living outside the skill

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J11 Progressive disclosure: says when to read what | partly | / File / Use it for / | Change the column to 'Open when' and say which step needs each reference; the table now describes content, not a trigger. |
| J12 Consistent terminology | partly | Note the date stamps of knowledge base notes you relied on | Use one term for the source layer (bundle, knowledge base, knowledge graph are mixed) and define it once. |

Facts: Script skimmed only for argparse and exit codes; J14 judged from SKILL.md statements.

### dept-decision-rights

**adequate**: Solid routing table and procedure, but the content rests on an expired source and the same caveat is repeated instead of stated once. (0 gap, 3 partly; core library)

Improve first:
1. Re-verify the decision-rights source with the OD lead
2. State the re-verification rule once
3. Add a Pitfalls section

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Until the OD lead role re-verifies the decision rights, every row is used at most at `recommend`. | State the pending-re-verification rule once; it is repeated in four places (table note, notes, Do not, example line). |
| J7 Gotchas in SKILL.md | partly | Do not read a table row as an approval already given | Add a Pitfalls section with the common wrong routings (treating a row as an approval, naming a threshold from memory) and a reason each. |
| J16 Grounded in real expertise | partly | The source's `valid-until` has passed, so the rows are pending re-verification by the OD lead. | Re-verify the source or replace the table with a current source; three rows rest on lane drafts that the source note lacks. |

### dept-governance

**adequate**: Clear procedures, decision rules with reasons and a pitfalls list, but five routines in one skill and a plan-draft origin. (0 gap, 3 partly; extension library)

Improve first:
1. Split or narrow scope
2. Resolve the Still open placeholders
3. Ground the routines in recorded rounds

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | It does not repeat the metrics and thresholds (`metrics-scorecard`), the decision rights and escalation (`dept-decision-rights`) | Cut the Purpose and Where it sits sections to one pointer each; the neighbour list is stated twice. |
| J15 One coherent unit | partly | Training programme / 1a3, 3a6, 26 / `know-training` | Five routines (round, demand routing, sprint, roadmap, training) sit in one skill; split the sprint runbook and training offer into their own skills or state a single trigger for the whole unit. |
| J16 Grounded in real expertise | partly | origin: plan-draft | Ground the routines in real rounds, decks or sprint records and close the Still open placeholders. |

### dept-intake

**strong**: A tight decision procedure with examples, a refusal playbook and a self-check; only the missing pitfalls section and mixed request/demand terms hold it back. (0 gap, 2 partly; core library)

Improve first:
1. Add a Pitfalls section
2. Use one term for request and demand
3. Show a record in the exact one-line field order

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J7 Gotchas in SKILL.md | partly | Do not read "just a small tile" as Lane 1: check that the use case is catalogued and the machine connected | Add a Pitfalls section for the common misroutings (small tile read as Lane 1, urgency read as priority, silent refusal) beside the Do not list. |
| J12 Consistent terminology | partly | Use it whenever a request, demand or idea arrives | Pick one term (request or demand) and use it throughout; define the other once. |

### dept-plant-diagnosis

**strong**: A coherent diagnostic procedure with a worked example, validation step, pitfalls and reasons; weaknesses are a malformed reference table and open placeholders. (0 gap, 1 partly; extension library)

Improve first:
1. Repair the references table
2. Close the Still open threshold placeholders
3. Add a second example for the interview-evidence route

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J11 Progressive disclosure: says when to read what | partly | / `evals/evals.json` / Test cases and trigger queries to run with and without this skill / | The references table is broken by the Not repeated here list, so the evals row sits outside it; move the list above or below the table. |

### dept-plant-onboarding

**adequate**: Clear route with profiles, stage gate, example and pitfalls, but the content is an unconfirmed proposal with open placeholders and long skill lists per stage without defaults. (0 gap, 3 partly; extension library)

Improve first:
1. Name one default skill per stage and make the others conditional
2. Confirm scope rule, owner per lane and done criteria with the OD lead and drop the open list from SKILL.md
3. Trim basis and aim lines that do not change agent action

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | No department document describes plant onboarding, so this is a route through existing skills, not a new method; | Move the basis and aim lines and the "What is still open" list to references/background.md; keep only what changes the next action. |
| J6 Defaults, not menus | partly | `catalog-usecase`, `catalog-compatibility` (is the standard consumable here?), `ops-analytics-asset`, `ops-dashboard-engine`, `catalog-usecase` | Name one default skill per stage and list the others as conditional; remove the duplicated catalog-usecase in stage 4. |
| J16 Grounded in real expertise | partly | Done (proposal, not a source rule): each stage in the path table has its artefact filed | Get the OD lead to confirm the scope rule, plant-side owners and done criteria, then replace the open placeholders with confirmed, cited text. |

### dept-retro

**strong**: Focused, decision-oriented procedure with a decision table, concrete example, final check and pitfalls; only the decider role and choice order remain unconfirmed. (0 gap, 1 partly; extension library)

Improve first:
1. Confirm decider role and choice order with the OD lead
2. Fix step 5 layout so options a, b and c read as one list
3. Add a short worked "no adjustment" example

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J16 Grounded in real expertise | partly | a working rule of this skill, not of the Department OS | Confirm the preference order and the decider role with the OD lead and cite the source, or mark the order as a proposal in the output contract. |

### dept-risk

**strong**: Tight, well-scoped procedure with explicit statuses, routing table, example and completeness check grounded in the department risk register. (0 gap, 0 partly; extension library)

Improve first:
1. Define "close by any reasonable reading" for on watch more precisely
2. Show a risk triggered two months running in the example to illustrate the retro hand-off
3. Add a gotcha on a stale register versus a stale indicator

### funnel-evaluation

**strong**: Rigorous procedure with a script that validates and scores, clear verdict table and pitfalls, held back by the absorbed second task and some density. (0 gap, 2 partly; extension library)

Improve first:
1. Separate the as-is maturity profile from the fit evaluation
2. Trim definitions and score description that the script output already carries
3. Drop the filler line "Open points: none recorded"

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | - Terms used throughout: **focus area** (one of 16 IT/OT areas, F1 to F16) | Split the absorbed maturity-profile path into its own skill or reduce it to a pointer; trim the score explanation the script already prints. |
| J15 One coherent unit | partly | Use this path only when the task is the as-is profile of one machine, system or application | Keep the as-is profile as a separate skill with its own trigger, since it has a different input, output and procedure. |

### funnel-features

**strong**: Small, focused skill with a default cut, a validating script, a worked example and pitfalls grounded in a measured failure pattern. (0 gap, 0 partly; extension library)

Improve first:
1. Add a second example showing a failing check and its fix
2. Say how many warnings may remain at handover
3. State what to do when the requester cannot name a role or hour

### funnel-first-aid

**adequate**: Clear checklist, routing table and pitfalls, but mixed description voice, drifting terminology, an absorbed second mode and an explicitly unconfirmed draft status. (0 gap, 4 partly; extension library)

Improve first:
1. Unify the description voice and terms
2. Split the absorbed analysis delivery into its own skill
3. Close the open questions with the DBVE

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | Capture an ad-hoc plant process issue | Rewrite the description in one point of view: change the imperative opening to third person ("Captures ...") to match the rest of the catalog. |
| J12 Consistent terminology | partly | / A process issue now, no use case, plant wants insight / Yes / / | Pick one term for the unit of work (request, first-aid request, ad-hoc analysis, one-off analysis) and use it throughout. |
| J15 One coherent unit | partly | ## Absorbed mode: ad-hoc analytics delivery | Keep scoping and routing here and move running the analysis into its own skill with its own trigger. |
| J16 Grounded in real expertise | partly | it is a draft for the DBVE to adopt or replace. | Close the open questions (template, queue, closing rule, who pays) with the DBVE and cite the source for the routing rule. |

### funnel-prototype

**adequate**: Clear, procedural, well gated, but grounded in a single pilot and repeats label content. (0 gap, 3 partly; core library)

Improve first:
1. Remove repeated label/ladder content from Purpose and Terms
2. Ground the method in more than one real pilot
3. Fix one term set for mock-up/click-dummy/prototype

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Short example of the record's shape (fictional example; the use case and the values are invented): | The Purpose section, the Terms table and the ladder bullets restate the label table and the type rule; cut the duplicates. |
| J12 Consistent terminology | partly | Click-dummy (also mock-up) | Click-dummy, mock-up, prototype and pilot are used interchangeably in steps and Do-not list; fix one term per claim level and keep it throughout. |
| J16 Grounded in real expertise | partly | this is not a validated OD method: nothing in the sources says OD has run this step to a stated standard. | Add a second real prototype case beyond the single Gemba App pilot to ground the method. |

### funnel-requirements

**strong**: Procedural, scripted validation loop, concrete example and pitfalls; minor density and terminology drift. (0 gap, 3 partly; core library)

Improve first:
1. Unify handover/handoff/request vocabulary
2. Add why-clauses to the bare procedure steps
3. Trim lane routing detail from the body

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Chain detail (category to method to data job, object/event/metadata checks, AI-assisted signal selection, rubrics) | Decision rules, handoff and process-chain pointers carry lane-routing detail the agent could read on demand; trim the body. |
| J12 Consistent terminology | partly | Terms: a **demand** is what intake accepts; the **requirement** is the document this skill writes about it | Handover packet, handoff file, handover and request overlap; pick one word for the artefact crossing a lane and use it everywhere. |
| J13 Explains the why | partly | Anything beyond the line is a new requirement through intake, not an edit; this is the guard against mission creep | Most numbered steps give no reason; add a short because-clause to steps 3, 7 and 9. |

### funnel-use-case

**adequate**: Solid four-phase method with control points and examples, but broad scope, duplication of lane flow and thin rationale. (0 gap, 4 partly; core library)

Improve first:
1. Cut lane-flow and chaining duplicates from the body
2. Separate idea-check path from DBVE method or tighten scope
3. Add rationale to bare directives

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Flow steps (the one numbering used here): intake, 21 define, 22 requirements and data check, 23 prototype, 24 business case | Lane flow, states and chaining sections duplicate lane-service-flow.md; keep only what step 21 needs. |
| J12 Consistent terminology | partly | Terms: a **demand** is the plant's request as logged at intake; a **use case** is what this skill defines from it. | Capability, coordinate, category and output asset are overlapping labels; use one term per concept and define them in one place. |
| J13 Explains the why | partly | No named change = a technical enabler that reaches `IMPLEMENTED` and stalls before `PRODUCTIVE`. | Most Collect, Assess and Decision-rule items are bare directives; add reasons where behaviour would otherwise differ. |
| J15 One coherent unit | partly | The rest of this skill is the DBVE's full method for the same idea once it goes ahead. | Two audiences (any plant person via idea-check, and DBVE method) plus lane flow and workshops share one skill; split lane flow out or sharpen scope. |

### funnel-workshop

**adequate**: Coherent, concrete procedure with honest gaps; draft status and coarse checklist keep it from strong. (0 gap, 2 partly; extension library)

Improve first:
1. Itemise the checklist and add a pre-send completeness check
2. Resolve open questions on lead times and the follow-up window
3. Add a second, filled example for an integration workshop

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J10 Checklist, validation loop, plan-validate-execute | partly | [ ] 12-15 After: summary, routed items, owners and dates, utilization session booked | The checklist groups 15 steps into three lines and has no check that the plant file or pre-read is complete; itemise key gates and add a pre-send check. |
| J16 Grounded in real expertise | partly | The window is not set anywhere; agree it with the OD lead. | Status is draft with several open questions on lead times and outcomes; confirm them with a real workshop and record them. |

### invest-screen

**adequate**: Strong procedure, verdict tables and pitfalls, but four modes in one skill, a long reference list and mixed verdict vocabularies. (0 gap, 3 partly; core library)

Improve first:
1. Split or slim the whole-list and application-consulting modes
2. Unify verdict vocabulary across modes
3. Resolve the EMS discrepancy instead of leaving it in the body

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Four modes, one skill; pick the mode first, because each has its own input and verdict. | Whole-list screen and application consulting are separate jobs with their own references; trim them to pointers or split them off. |
| J12 Consistent terminology | partly | Terms: **fit check** is the three-step check below; **gate** is the Lane 3 tool-decision step | Verdict words differ per mode (Fits/Redesign/Escalate vs Go/Hold/...), plus footprint, lean footprint and screen; keep one vocabulary table and name the modes consistently. |
| J15 One coherent unit | partly | Four modes, one skill; pick the mode first | Four modes with distinct inputs and verdicts make activation less precise; split whole-list screen and application consulting or justify the bundle. |

### know-ai-generation

**adequate**: Clear safety pattern with reasons, example and loop, but broad scope, draft status and unconfirmed rules. (0 gap, 5 partly; extension library)

Improve first:
1. Confirm PROPOSAL rules and time-box values
2. Narrow scope or split by step family
3. Turn rules into per-step procedures

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Everything below is process guidance from the decks. | The chain-position table and Neighbours section list many steps the agent can read elsewhere; trim. |
| J5 Procedures over declarations | partly | Run these stages for any template-bound output (document, deck, dashboard config); detail in the `generation-pipeline` reference. | Half the body is a rules table (R1-R10), declarative; show how to apply the rules per step type in the procedure. |
| J12 Consistent terminology | partly | **output** is anything the agent generates; **open item** is anything marked `<to confirm>`. | Output also names the outputs.yaml contract and the delivered deliverable; use distinct words for generated content and skill outputs. |
| J15 One coherent unit | partly | It is the one rulebook for the places in the chain where an AI agent drafts, classifies, generates or checks something. | Covers every chain step from intake to connectors in one rulebook; scope narrowly or split per step family. |
| J16 Grounded in real expertise | partly | The owner has not confirmed the `PROPOSAL` rules. | Confirm the PROPOSAL rules with the owner and record real run evidence to move off draft. |

### know-sharepoint-export

**strong**: Tight, procedural, with a validation loop, pitfalls and a script that reports usable errors; only the implementation-led description opening is weak. (0 gap, 1 partly; extension library)

Improve first:
1. Rewrite the description to open with the user need rather than the REST API method.
2. Add a short second worked example (an incremental run that hits the list view threshold).
3. Reduce the date literals in the body example or label them clearly as fictional.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | Export a full SharePoint Online list (current items, complete version history, attachment metadata and binaries) from the browser console with the REST API | Lead the description with the user need (get the full list with its history out of SharePoint) and move the REST API and browser-console method into the body. |

Facts: Dates in the body are fictional run-log values inside the example.

### know-skill-authoring

**strong**: A clear nine-step method with control points, a brief template, a worked example and a tested scaffold script; the description over-lists implementation and a few terms vary. (0 gap, 2 partly; extension library)

Improve first:
1. Trim the description to need, trigger and boundary.
2. Fix one word for the quality result and one for the checks.
3. Add a second example showing a rework of a weak skill, not only a new one.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | passes the gates in order (registry checks, Agent Skills specification export, OKF, no invented figures, the SkillEvaluator quality rating) | Shorten the description to need, trigger and boundary; move the list of gates into the body. |
| J12 Consistent terminology | partly | a skill rates below B or reads vague | Use one term for the quality result (rating, grade or score) in the description, steps and definition of done, and one term for the checks (gates or checks). |

### know-training

**adequate**: Well-bounded and honest about its gaps, but the catalogue is unconfirmed proposal, there is no validation loop and some rationale sits in the body. (0 gap, 3 partly; extension library)

Improve first:
1. Add a pre-handover validation loop for the checklist.
2. Move call-deck rationale and the Open list out of SKILL.md.
3. Ground the module catalogue in cited sources.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Infrastructure is a recorded cause of delay: call decks give "infrastructure harmonization" (China) | Move the call-deck evidence and the long Open list to references or background; keep only the rule the agent acts on. |
| J10 Checklist, validation loop, plan-validate-execute | partly | If not ready, say so in the package and do not schedule training on a demo environment. | Add a pre-handover checklist or validation loop before step 8: every competence has evidence, a plant-owner confirmation and a second person; if one is missing, go back to step 3. |
| J16 Grounded in real expertise | partly | The module catalogue and the hand-down model are proposals, not a department standard | Record the sources that support each module in curriculum-modules and replace proposal labels with a cited source as the OD lead supplies the training formats. |

### metrics-scorecard

**strong**: Method with a clear authority rule, a validation step, an example and pitfalls; the rounds section drifts into territory owned by neighbouring skills. (0 gap, 1 partly; extension library)

Improve first:
1. Move the rounds table out of the body.
2. Add a second example with two disagreeing reports.
3. Refresh valid_until, which has passed.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J15 One coherent unit | partly | Round and retro mechanics belong to neighbouring skills: this skill supplies the numbers. | Cut the rounds and recipient-feedback tables from the body, or move them to rounds-and-escalation; they overlap dept-governance and dept-retro. |

Facts: metadata valid_until 2026-11-10 is before the review date 2026-11-16; the skill is past its own freshness date.

### mi-data-availability

**strong**: Distinctive verdict (which path step fails), explained reasoning, traps, script and example; only the verdict step lacks an explicit pre-handover check. (0 gap, 1 partly; core library)

Improve first:
1. Add a pre-verdict checklist.
2. Link each trap to the specific reference that resolves it.
3. Add a third example for a non-machine request.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J10 Checklist, validation loop, plan-validate-execute | partly | Walk the six path steps in order (section "Walk the path, in this order"), watching the traps listed after it. | Add a short checklist before the verdict: script run, six steps answered or marked unproven, freshness checked, gap routed; return to the open step if one is missing. |

### mi-equipment

**adequate**: Strong content and a validation loop, but the body is the largest of the six, mixes three absorbed procedures and uses blocker, barrier and gate loosely. (0 gap, 3 partly; core library)

Improve first:
1. Shrink the body and move detail into references.
2. Unify barrier, blocker and gate terminology.
3. Decide whether Mode A and Mode B, or the absorbed procedures, belong in separate skills.

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | / Route / The whole path of a machine's data to the platform: variant plus connector (or driver) plus pattern / | Cut the body toward 3,000 tokens: move the Terms table, the Lane 3b section and the Decision rules detail to references, and keep the procedures. |
| J12 Consistent terminology | partly | **Gate 3 - clear preparation blocks in order**: budget, infrastructure, **PLC program**, tags, cyber security. | Use one word for what stops a machine (barrier or blocker) and keep gate for the Mode B steps only; the body mixes blocked, blocker, barrier, block and gate. |
| J15 One coherent unit | partly | / Former lane / `references/od-information-integration-service/procedure.md` / | Consider splitting assessment (Mode A) and per-machine guidance (Mode B), or confirm via evals that the three absorbed procedures do not hurt activation precision. |

Facts: Body estimate is about 4,480 tokens, near the 5,000 guidance.

### mi-flow

**adequate**: Strong, evidenced content, but the body exceeds the token guide, mixes three modes and carries a long repetitive reference table. (0 gap, 3 partly; core library)

Improve first:
1. Cut the body below 5,000 tokens by moving build and rule-engine detail into references
2. Collapse the 13 example rows of the reference table into one folder pointer
3. Align the mode names (two in the table, three in the procedure) and one term per concept

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Letting a rule-engine calculation run before all inputs are stored (wait-for-all-inputs bug): see the BROKEN and FIXED examples. | Body is 283 lines and about 5,900 tokens, over the 5,000 recommendation; move build and rule-engine detail into references and replace the 13 identical example rows in the reference table with one folder pointer. |
| J12 Consistent terminology | partly | / **3b4** connector and pipeline to the data platform (flow design to the standard base model); also 22 and 26 / **Build** / | The opening table has two modes (Build, Troubleshoot) but the procedure has three (adds Rule engine), and the body mixes datatron, IIoT Edge Platform and data point; name the modes once and use one term per concept. |
| J15 One coherent unit | partly | builds calculated datapoints with the rule engine, and diagnoses a flow that is broken, silent or producing wrong values. | One skill covers build, port, review, rule-engine generation and troubleshooting; consider splitting rule engine and troubleshooting into their own skills, or state why the bundle is one task. |

### mi-signals

**strong**: Clear procedure with a re-run loop, concrete example, defined terms and public standards; only mild repetition in the Purpose section. (0 gap, 1 partly; core library)

Improve first:
1. Remove the repeated trigger text in the Purpose section
2. Move the archived-PLC-project gotcha into step 3 where it applies
3. Add the invalid-input fix as a numbered step rather than a bullet under the example

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Use it when a machine is newly connected, when a use case cannot be built because a signal is missing or ambiguous | The Purpose section repeats the description's trigger list and states the standardization idea twice; cut the repeated 'use it when' line. |

### ops-analytics-asset

**strong**: Clear decision logic with a validation loop, concrete examples and grounded estate facts; terminology and a slightly broad scope hold it back from top marks. (0 gap, 2 partly; core library)

Improve first:
1. Unify the terms for the skill and the product (asset or dashboard)
2. Move Lane 1a self-service and estate detail out of the body into references
3. Add a short decision-record template for the asset-type choice

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J12 Consistent terminology | partly | Scope: this skill chooses the asset type, names the ritual, validates and hands off | The body switches between 'this skill', 'this function', 'asset', 'dashboard' and 'delivery asset'; pick one term for the skill and one for what it produces. |
| J15 One coherent unit | partly | ## Lane 1a self-service mode | The skill mixes asset choice, ritual design, Grafana estate knowledge and Lane 1a template application; move the Lane 1a and estate sections to references or to the datatron skill so the body keeps one job. |

### ops-dashboard-datatron

**adequate**: Concrete, well-gated procedure with templates and example, but it depends on a draft transcription held in another skill and has a status fragment in its description. (0 gap, 3 partly; extension library)

Improve first:
1. Link the exact query-pattern reference from step 4
2. Remove 'Draft.' from the description
3. Verify the QA checklist against the master package and record the source check

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J2 Description: one point of view, user intent | partly | Draft. Not for new dashboard types or the asset choice (ops-analytics-asset, ops-dashboard-engine) or a need the template does not cover (Lane 2). | The fragment 'Draft.' in the description is a status note, not user intent; keep status in metadata only. |
| J11 Progressive disclosure: says when to read what | partly | / `ops-analytics-asset`, `references/ops-grafana-dashboards.md` / Writing a query: schema, value extraction, time-filter dialects, variable chain, panel recipes, equipment context / | The query and variable patterns sit in another skill's reference and are not linked as a file; link the exact file and section from step 4 or keep a copy here so the skill is self-contained. |
| J16 Grounded in real expertise | partly | The department master package (`ops-grafana-dashboards.zip`) is not in the registry; the transcription in `ops-analytics-asset` is the source and is itself draft. | The source is a draft transcription; confirm the QA checklist against the master package or a verified dashboard and record the check date. |

### ops-dashboard-engine

**strong**: Exact rules where fragile, reasons stated, a script-backed audit and worked examples; the body is near the token limit and partly repetitive. (0 gap, 1 partly; core library)

Improve first:
1. Trim repeated pitfalls and example rows to bring the body well under 5,000 tokens
2. Put the builder script under an Available Scripts heading
3. Add a hint for when validate exits 2 (unreadable file)

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J3 Concise: only what the agent lacks | partly | Building on a guessed schema: skipped Step 0 is the commonest cause of a rebuild. | Body is 252 lines and about 4,750 tokens, near the limit; the Pitfalls repeat the hard rules and Step 6 checklist, and eight example rows repeat one trigger text; cut them. |

### ops-event-model

**strong**: Focused procedure with checklist, handoff contract, reasons and a worked example; the evidence base for the archetypes is still draft. (0 gap, 1 partly; extension library)

Improve first:
1. Cite the sources for the cross-process, per-process and unique archetypes
2. Resolve or date the open items in 'Still open'
3. Add a second example for a derived event

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J16 Grounded in real expertise | partly | The decks assess an object-centric event log as an affordable option; no deck states a platform decision for it. | Open items on the platform decision and share of use cases are unverified; resolve them or cite a source for the three archetype classes. |

### process-derivation

**strong**: Gate, ten controlled steps, a script-checked model, refusal path and honest sourcing; only the coded citation keys slow reading. (0 gap, 1 partly; core library)

Improve first:
1. Spell out method names beside the [PDn] keys in the procedure
2. Add a second example for the rework of an existing process
3. Validate the composition on a real plant case and record the result

| Criterion | Rating | Evidence | Change |
|---|---|---|---|
| J12 Consistent terminology | partly | Phases follow the BPM lifecycle [PD1]; keys [PDn] and the method names are in `references/public-methods.md`. | The body relies on coded keys [PD1] to [PD13] decoded only in a reference; spell the method name beside each key at first use. |
