---
type: Design Record
title: Department context conformance
description: "The 53 skills checked against the OD Department Knowledge folder (new-state lane drafts, decision rights, intake, the 2026-09-11 OD x IT alignment, the skill naming convention): where the skills follow the department flows, where they do not, and where the department material contradicts itself or the owner's decisions."
status: draft
owner: human:jakob.gabriel
tags: [process-flow, lanes, conformance, department-os]
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Department context conformance

**Source checked against.** Personal vault, `Work-OpsDigit-Knowledge/OD Department Knowledge/OD-instance/`, read
2026-11-10: `20-lanes-newstate-DRAFT/` (README, lane 1, 2 and 3, `Transcripts/INDEX.md` for the 2026-09-11 OD x IT
alignment), `00-core/04-service-catalog.md`, `05-intake.md`, `08-decision-rights.md`,
`10-modules/smart-factory-use-case/systems-of-record.md`, `OD_Skill_Naming_Convention.md`,
`skills-inventory-and-roadmap.md`, `od-department-transformation.md`, `machine-integration-transformation.md`.
No skill or doc in this registry cited any of these files before this check.

**Method and limits.** Keyword matrix over every `SKILL.md` and its references for each rule the department files set,
then reading the hits. A zero count is evidence, not proof. The new-state lane files are marked DRAFT by the department
("not a locked spec"); findings that depend on them are decisions, not defects. AI assessment, not reviewed by a human.

**Structural checks** (`validate_registry.py`, `agent_skills_spec.py`, `verify_okf.py`, `check_no_figures.py`): pass,
apart from the known `PHASE1-ELICITATION.md` frontmatter gap. The `check_no_figures` hits in `od-workshop-facilitation`
are agenda numbers, not figures.

## Where the skills follow the department flows

- **Lane order.** `docs/new-state/process.yaml` matches the three lane files step for step: Lane 1 branches 1a/1b with
  fall-through, Lane 2 funnel (define, requirements and features, prototype, business case, capital request, implement,
  catalogue), Lane 3 shared front-end then 3a and 3b.
- **Authority.** No skill claims more than `08-decision-rights.md` allows. Every lane "may not" (commit investment,
  approve integration, bypass Cyber Security, push an under-specified demand) is held: `od-capital-request`,
  `it-demand-package`, `od-cybersec-gate`, `deploy-appstore` and `od-equipment-integration` all stop at a human.
- **Never invent figures.** Enforced by `od-context`, `check_no_figures.py` and the grounding tags in
  `od-benefit-calculation`.
- **Clear demand before hand-off.** `it-demand-package` step 1 stops when the front-end is incomplete, as Lane 3 requires.
- **Catalogue graduation.** `od-catalog` and `od-use-case-standardization` carry the Lane 2 -> Lane 1 graduation.

## Where the skills do not follow them

| # | Rule in the department files | The skills | Severity |
|---|---|---|---|
| 1 | Lane 3 step 2: the tool-decision / IT-footprint gate `investment-screening` (`invest-screen`) is **mandatory** and routes 3a.1-3a.4 or 3b | No skill names it. `od-system-fit-check` (placed on step 32) gives fits / redesign / escalate against the lean footprint; it does not route make, buy, integrate or connect and has no IT-footprint hard gate. The department already has the gate packaged (`30-skills/investment-checking.zip`) | High |
| 2 | Intake classifies each demand into exactly one of Lane 1, 2 or 3 | `od-use-case-intake-triage` SKILL.md step 3 still routes into the four old service lines; its own `references/process-chain-practice.md` routes to Lane 1/2/3. The skill contradicts itself. `od-context` also frames "the four service lines" | High (pending adoption of the new state) |
| 3 | Old lanes resolved: Analytical Support retired; Project Support becomes the Lane 3 front-end; Information Integration becomes 3b | The three lane orchestrators ship in the extension library and `docs/new-state-flow.md` calls their future open. The department draft answers it | Medium |
| 4 | Business case (OD x IT, 2026-09-11): separate bankable impact from assumption-dependent benefit; state investment envelope, minimum viable rollout, maximum scale-out, TCO. Cost kept apart from value (`bc-cost` feeds `bc-assess`) | None of these terms in `od-benefit-calculation` or `od-capital-request`. `od-benefit-calculation` has no cost side; `od-capital-request` notes it. `od-capital-request` says nothing packages the eCR, but the department holds `ecr-builder` (`bc-capital-request`) and `bc-assessment` | High |
| 5 | Application ownership (OD x IT): build-and-run; ownership moves only on formal acceptance; handover checklist (legacy status, backlog, version currency, architecture, business logic, logging, observability) | Absent from `od-handover-and-adoption`, `it-demand-package`, `deploy-appstore` | High |
| 6 | Technology guardrails (OD x IT): Python/FastAPI/SQL, k8s/CMO deployment, approved OT interfaces (MQTT/Edge), observability; self-assessment every 6-12 months; requirements fix objective, scope, interfaces and growth boundaries (mission creep) | Not in `od-catalog` guardrails or `od-requirements-breakdown`. The IT side still owns publishing them (action item 6), so the skills can only point to them | Medium |
| 7 | Lane 1a: the plant applies the standard dashboard in self-service mode | `od-analytics-asset-build` and `build-grafana-ops-dashboard` still describe OD building it. No DATATRON-specific skill (`ops-dashboard-datatron`) in the registry | Medium |
| 8 | Lane 1b: cost template, approved by the plant budget owner | `od-decision-routing` (step 1b2) has no row for the plant budget owner; no cost template (the department also marks it a gap) | Medium |
| 9 | Cyber Security: pre-evaluation and platform-level approval on CMO (OD x IT action items 3, 4) | `od-cybersec-gate` is per case only. The approach is not defined yet; add a pointer once it is | Low |
| 10 | `deploy-appstore` exists as a drafted engine (GitOps/ArgoCD, k8s manifests, PostgreSQL StatefulSet, Traefik sub-path ingress, reference instance HDAS) | The registry skill calls itself a scaffold whose "platform procedure is not recorded". The department has the procedure | Medium |
| 11 | Every skill sits on a new-state lane | 23 skills (the original core) had only the old `lane:` value | **Fixed** in this change: `new_state_lane` / `new_state_step` added from `docs/new-state/process.yaml` |
| 12 | Naming convention (2026-09-21): `<family>-<object>` (`funnel-`, `bc-`, `catalog-`, `mi-`, `deploy-` ...) | Registry uses `od-<object>`. A naming decision, not a flow defect | Decision |

## Where the department material contradicts itself or the owner's decisions

Fix these in the department folder, not in the skills.

- **MDL and ContiTech.** The lane drafts, `08-decision-rights.md` and `systems-of-record.md` still name the MDL as the data
  platform and ContiTech as counterpart. The owner retired both (`docs/derivation.md`: Databricks to Azure Storage Account,
  no ContiTech). The registry follows the owner.
- **Lane 2 order.** The lane 2 file puts prototype before the business case; `OD_Skill_Naming_Convention.md` §4 chains
  `bc-build` before `funnel-prototype`. The registry follows the lane file.
- **Cyber Security in 3b.** The lane 3 file puts sign-off before procurement; the owner decided "Cyber Security in parallel",
  sign-off blocking go-live (`log.md`, 2026-11-06). The registry follows the owner.
- **"3a.4".** In the department it is an option (integrate a foreign app); in `process.yaml` `3a4` is a step ("Package or
  build the app"). Same label, two meanings.
- **Freshness.** `08-decision-rights.md` is `valid-until: 2026-11-10`. Every skill that routes a decision inherits it;
  run `od-context-freshness` after re-verification.

## Resolved 2026-11-10

| # | Finding | Resolution |
|---|---|---|
| 1 | Tool-decision / IT-footprint gate missing | `od-system-fit-check` is the Lane 3 gate (step 32): IT-footprint hard gate, route to 3a.1-3a.4 or 3b, OD x IT sourcing principles, the department's verdict words (`references/tool-decision-gate.md`); absorbed `od-application-consulting` |
| 2 | Intake on the old four lines | `od-use-case-intake-triage` classifies into exactly one of Lane 1a/1b, 2, 3 with fall-through and chaining; `od-context` carries the three lanes and the old-to-new crosswalk |
| 3 | Retired lane orchestrators | Absorbed: Analytical Support into `od-first-aid-kit`, Project Support into `od-it-handover`, Information Integration into `od-equipment-integration` |
| 4 | Business-case rules | `od-benefit-calculation` carries the house standard (value-only backbone, grounding tags, de-banking, bankable vs assumption-dependent, envelope, rollout scenarios, assessment verdict); `od-investment-input` is the cost side and moved to core; `od-capital-request` carries the eCR section map and the builder's refusal gate and maturity verdict |
| 5 | Ownership and handover | `od-handover-and-adoption`: build-and-run, formal acceptance, handover checklist, criticality, self-assessment; new `od-it-handover` packages the handover as OpenSpec |
| 6 | Technology guardrails, mission creep | `od-catalog` technical guardrails; `od-requirements-breakdown` growth boundaries |
| 7 | Lane 1a self-service | `od-analytics-asset-build` self-service mode; `build-grafana-ops-dashboard` OD-INTEGRATION note |
| 8 | 1b plant budget owner | `od-decision-routing` rows for the 1b cost template, the Lane 3 gate and ownership transfer; `od-investment-input` cost template |
| 9 | Cyber Security pre-evaluation | `od-cybersec-gate` section on pre-evaluation, platform-level approval and the CMO route |
| 10 | App-Store procedure | `deploy-appstore` records the department's GitOps / ArgoCD deployment shape (`references/gitops-deployment-shape.md`) |
| 11 | Lane metadata | Every skill's `lane`, `new_state_lane` and `new_state_step` regenerated from `process.yaml` |
| 12 | Naming convention | Not changed: renaming every skill is a separate decision; the department names are recorded as aliases in the skills (`bc-build`, `bc-cost`, `bc-capital-request`, `invest-screen`, `ops-dashboard-engine`) |

**Duplicates.** Twelve skills were merged into the skill that owns the same capability (table in the README).
53 skills became 42 (27 core, 15 extension). **Flow.** `OD_NewState_Flow.mermaid` was redrawn to the lane
files; core equals the flow and the validator enforces it.

## Still to decide

- The department-side contradictions above (MDL and ContiTech in the lane drafts and decision rights, Lane 2
  order in the naming convention, Cyber Security ordering in the lane 3 file, the "3a.4" label) are fixed in
  the department folder, not here.
- Whether to adopt the department's family-prefix names (`funnel-`, `bc-`, `catalog-` ...).
- Re-verify `08-decision-rights.md` (valid-until 2026-11-10) and add the three new rows there.
- Whether IT adopts OpenSpec as its intake format (`od-it-handover`, open points).
