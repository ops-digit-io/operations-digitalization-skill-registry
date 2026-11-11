# Log

History of this bundle. Reserved under OKF §9: headings are ISO 8601 dates, and this file is
not a concept.

## 2026-11-11 — The IT demand follows the OpenSpec process, modelled in step 3a4

- Step 3a4 *Package / build* (routes 3a.3 and 3a.4) now has six sub-steps in `docs/new-state/process.yaml`, the flow
  diagram, the process page and the explorer: 3a4.1 explore + collect inputs, 3a4.2 propose the change, 3a4.3 validate +
  hand over (OD), 3a4.4 apply, 3a4.5 verify, 3a4.6 archive + sync specs (IT / external developer).
- Each sub-step names OpenSpec's own skills (`openspec`: chips without pages; the skills stay unchanged inside
  `deploy-it-demand`). The validator checks every named OpenSpec skill exists in the copy.
- `deploy-it-demand` is now only the OD part: inputs and attachments, the OD annex, OD's store config and the check
  (sub-steps 3a4.1 and 3a4.3). Writing, applying, verifying and archiving the change belong to OpenSpec's skills.

## 2026-11-11 — Skills renamed to the department's naming convention; Grafana engine moves to core

- Every skill name now follows the department's naming convention (`<family>-<object>[-<variant>]`). Where the convention
  names a skill, that name is used (for example `bc-assess`, `bc-capital-request`, `bc-build`, `funnel-requirements`,
  `funnel-prototype`, `invest-screen`, `bc-cost`, `ops-dashboard-engine`); the other skills were mapped to a family.
  The full old-to-new map is `config/skill-renames-2026-11-11.yaml`; each skill keeps its old name in
  `metadata.aliases`. Entries below this one use the old names.
- New family `comms-` for Lane 4 (use-case promotion), which came after the convention. The families are listed in
  `registry.yaml`; the validator and the scaffold reject a name outside them or with a `-builder`/`-tool`/`-skill` suffix.
- The Grafana dashboard skill (`ops-dashboard-engine`, formerly `build-grafana-ops-dashboard`) moves from the extension
  library to core, on steps 1a2 (Apply template) and 1b4 (Apply template & go live) of the process flow. Its rules and
  references are unchanged; core sections and file links were added.
- `deploy-handover` (formerly `od-handover-and-adoption`) carries two capabilities; the convention would split it.

## 2026-11-11 — Citations reduced, core descriptions shortened

- Source citations now read "Department knowledge base, read <date>": document paths and titles removed.
- The 25 core skill descriptions are 200 characters or fewer, each keeping its "Not for" boundary.
- The quality ratings predate these changes; rerun SkillEvaluator to refresh them.

## 2026-11-10 — Department packages transcribed into ten core skills

- The department's skill packages in the department knowledge base are now readable and are the master where transcribed:
  `bc-assessment.zip` → `bc-assessment` (full rubric C1-C5 / D1-D9 / E1-E6, lever model, grounding, provenance, deck spec, renderer; plus the intake questionnaire and the Gemba assessment as worked example, money masked);
  `ecr-builder.zip` → `od-capital-request` (workflow, refusal gate and de-risk questions, honesty layer, renderer) plus the eCR approval matrix by role and tier → also `od-decision-routing`;
  `investment-checking.zip` → `od-system-fit-check` (8-point footprint gate, six criteria, whole-list screen, region-grouped review);
  `product-funnel-skills.zip` → `od-requirements-breakdown` (requirements funnel, handoff schema), `od-prototype-poc` (click-dummy stages, build patterns), `od-benefit-calculation` (business-case stage, savings model, deck);
  `ops-rule-engine.skill` → `od-node-red-flow-builder` (calculated datapoints: workflow, patterns, standard flow, 13 production examples with the API host scrubbed, generator and tests) and `od-signal-standardization` (normalization-in-flows);
  `ops-grafana-dashboards.zip` → `od-analytics-asset-build`.
- Not stored: the neuwerk `_nw_template.pptx` the renderers need (in the packages / `neuwerkbrand.zip`). The unnamed files `zi0XqsQv` and `ziwJsyMF` are older copies of `investment-checking` and `product-funnel-skills`.

## 2026-11-10 — Core = the owner's process flow

- `OD_NewState_ProcessFlow.html` restored to the owner's version (skills & gaps) and made the reference; the generated variant and `scripts/build_process_flow.py` are removed. Gap chips that are now built show as drafts; PoC skill = `od-prototype-poc`, capital request = `od-capital-request`.
- Skill names follow that page: `funnel-requirements` → `od-requirements-breakdown`, `bc-build` → `od-benefit-calculation`, `invest-screen` → `od-system-fit-check`, `mi-connector` → `od-equipment-integration`, `ops-pipeline` → `od-node-red-flow-builder`, `bc-assess` → `bc-assessment`, `funnel-prototype` → `od-prototype-poc`, `bc-capital-request` → `od-capital-request`, `dept-os` → `od-context`, `bc-cost` → `od-investment-input`, `ops-dashboard-engine` → `build-grafana-ops-dashboard`. Department names stay as aliases (`department_names`).
- Core (21) = the skills on the page's steps; moved to core: intake triage, analytics asset build, decision routing, use-case definition, data availability check, handover and adoption, signal standardization, acceptance test. Moved to extension: `od-context`, `od-investment-input`, `build-grafana-ops-dashboard`, `funnel-features`, `ops-dashboard-datatron`.

## 2026-11-10

- **Core = department skills, registry 2.0.0, 47 skills (core 18, extension 29).** The core library is now exactly the
  department's skills from its process map and naming convention: `dept-os`, `catalog-usecase`, `catalog-systems`,
  `catalog-guardrails`, `bc-cost`, `ops-dashboard-datatron`, `ops-dashboard-engine`, `funnel-requirements`,
  `funnel-features`, `funnel-prototype`, `bc-build`, `bc-assess`, `bc-capital-request`, `invest-screen`,
  `it-demand-package`, `deploy-appstore`, `mi-connector`, `ops-pipeline`. Twelve registry skills were renamed into
  them (table in the README), four split out, `ops-dashboard-datatron` new; all other skills moved to extension and
  sit on the steps they deepen. Every skill now requires `dept-os`. `process.yaml` and the Mermaid name only
  department skills on the steps.
- **Department context applied, registry 1.13.0, 42 skills (core 27, extension 15).** Fixed every finding of
  `docs/department-context-conformance.md` from the department knowledge base and the OD x IT
  meeting notes of 2026-09-11. Merged twelve duplicate or retired-lane skills into their owners, each kept as
  `references/<old-name>/procedure.md`: `od-analytical-support-service` → `od-first-aid-kit`;
  `od-project-support-consultancy`, `it-demand-package` → `od-it-handover`; `od-information-integration-service`,
  `od-machine-integration-plan`, `od-barrier-triage` → `od-equipment-integration`; `od-application-consulting` →
  `od-system-fit-check`; `od-impact-evaluation`, `od-utilization-review` → `od-handover-and-adoption`;
  `od-use-case-promotion` → `od-use-case-standardization`; `od-use-case-prioritization` →
  `od-portfolio-and-savings-analysis`; `od-maturity-assessment` → `od-use-case-solution-evaluation`. New core skill
  `od-it-handover`: the Lane 3 handover as an OpenSpec change package, with scaffold and check scripts (the example
  passes OpenSpec's own validator in strict mode). `od-investment-input` moved to core, `od-sharepoint-list-export` to
  extension. `process.yaml` and `OD_NewState_Flow.mermaid` redrawn to the department lanes (step 34 added, step ids
  kept); `validate_registry.py` now fails when core and flow disagree.
- **Department context conformance.** Checked all 53 skills against the department knowledge base
  (new-state lane drafts, decision rights, intake, OD x IT alignment of 2026-09-11, naming convention); result in
  `docs/department-context-conformance.md`. Added `new_state_lane` / `new_state_step` to the 23 skills that only carried the
  old `lane:` value, from `docs/new-state/process.yaml`. No other skill content changed.

## 2026-11-06

- **Core library merged, registry 1.12.0, 53 skills (core 27, extension 26).** Related core skills that the process does not keep apart were merged:
  `catalog-usecase`, `catalog-systems` and `catalog-guardrails` into `od-catalog`; `od-node-red-flow-builder` and `od-node-red-flow-troubleshooting` into
  `od-node-red-flows`; `od-use-case-support-service` into `od-use-case-definition`. Every rule, reference, asset and the `analyze_flow.py` script moved over;
  the four original New-State files keep the old names and `docs/new-state-flow.md` maps them.
- Applied the owner's second round of decisions (deputy, rollout tandem, ladder overlap, dashboard standard, data model, MES overlap, tool scale, platform names,
  KI assistants, customer programmes, rule engine) and the first round (wave allocation, ODEC as history, savings first, Cyber Security in parallel, plant evaluates).

## 2026-11-05 (libraries)

- **Two skill libraries.** The registry now separates a **core library** (`skills/`, 29 skills: every skill the four New-State process files name on a step or on
  the supporting spine) from an **extension library** (`skills-extension/`, 28 skills: all others, optional add-ons). `registry.yaml` carries `library: core|extension`;
  `scripts/skillpaths.py` is the one place that knows both folders; `validate_registry.py` checks library against folder; the generators, the spec export, the site
  (core and extension downloads, extension skills switchable on the map) and `check_no_figures.py` use it. Cross-skill links across the two folders were rewritten.
  No skill content changed. Core skills require no extension skill; three `composes` entries point from core to extension and are optional.

## 2026-11-05 (wave 2)

- **Registry 1.11.0, 57 skills.** Folded the knowledge base notes that no skill drew on into the skills as patterns, without figures: the IT/IoT
  maturity model became the draft skill `od-maturity-assessment` (with maturity-profile references in `od-system-fit-check` and
  `od-application-consulting`); process-family patterns, the microservice-app pattern, tool boundaries, business-case archetypes, the AI
  initiative maturity ladder and strategic-initiative savings rules went into the catalog, standardization, prioritization, portfolio and AI
  skills; rituals, SWOT seams, knowledge-graph and source-catalogue reading, metric-reading rules, change-log reading, fact triage and
  dashboard spec patterns went into the governance, context, scorecard, retro, freshness, analytics and lane skills.
- Removed the remaining company figures from `docs/derivation.md` and this log.

## 2026-11-05 (later)

- **No company figures in skills.** Removed counts, spend, savings, per-plant status, dated snapshots and real example values from
  all skills; snapshot references became how-to-read / how-to-count-live guides. Added `scripts/check_no_figures.py` (heuristic, read-only).
- **Registry 1.10.0, 56 skills.** Abstracted process knowledge from the Operations Digitalization slide decks (workshops, governance,
  integration and tools, analytics, AI activities, business case and rollout) and merged it: every enriched skill gained
  `references/process-chain-practice.md` (method, decision rules, handoff contract, pitfalls, questions, AI-agent operating notes) and
  eight draft skills were added: `od-project-order`, `od-utilization-review`, `od-migration-cutover`, `od-machine-integration-plan`,
  `od-event-object-modelling`, `od-plant-diagnosis`, `od-ai-generation-playbook`, `od-governance-cadence`. Contradictions between decks are
  written as the safer reading with `<to confirm>` and listed under `open_gaps`.

## 2026-11-05

- Added the **new-state flow** as the process the skills are gauged against: `docs/new-state/` (Mermaid flowchart, process
  flow, BPMN, VSM skill map, copied unchanged), `docs/new-state-flow.md` and `docs/new-state-conformance.md`, which checks every
  skill the flow names against its own text. The conformance check found three things to act on: `od-use-case-intake-triage`
  still classifies into the four service lines; no skill speaks of self-service; the Cyber Security gate the flow attributes to
  `od-acceptance-test` is written in `od-equipment-integration` and `od-decision-routing`.
- Added five **draft** skills the flow lists as net-new: `catalog-usecase`, `catalog-systems`, `catalog-guardrails`,
  `deploy-appstore`, `it-demand-package` (registry 1.8.0, 30 skills). Each is sourced and marks every unrecorded fact as
  an open gap; `registry.yaml` carries them with `origin: new-state` and `status: draft`.
- **Registry 1.9.0, 48 skills.** Built the 18 skills that were missing: 16 from the department's own skill plan (`od-cybersec-gate`, `od-rollout-training`, `od-context-freshness`, prioritization, impact evaluation, workshop facilitation, first-aid kit, investment input, barrier triage, application consulting, promotion, template resolution, cross-plant compatibility, retro, risk watch, plant onboarding) and the flow's two thin spots (`od-prototype-poc`, `od-capital-request`), all as drafts with their open questions in `open_gaps`. Enriched 18 existing or draft skills with references and templates mined from the department knowledge base (integration, data and flow skills, and the five new-state drafts). A recount showed 72 of 825 Node-RED flows disabled, not 0; `od-node-red-flow-builder/references/instances.md` is corrected.
- Added the process flow as data and as a site: `docs/new-state/process.yaml`, `docs/new-state-skill-map.md`, `scripts/build_site.py` (interactive process map, one page per skill, specification page, spec-strict downloads per lane), `docs/agent-skills-spec.md` and `scripts/agent_skills_spec.py`. CI builds the site on every push; the Pages workflow is manual and not switched on.
- Listed the registry skills the new-state files do not place, in `docs/new-state-flow.md`: two in none of the four files and eleven only in the skill-map table. The four files themselves are unchanged.
- `scripts/build_process_overview.py` skips skills with `origin: new-state`: the page draws the four service lanes of the old model.
- Declared `allowed-tools` on the eight skills that ship scripts or author files; tagged 69 code fences without a language
  as `text` in 23 files outside the vendored skill; "fill" became "complete" in one sentence of `od-signal-standardization`;
  a final newline in `od-use-case-solution-evaluation/scripts/model_data.json`.

## 2026-10-24

- Added `docs/process-overview.html`, an interactive BPMN-style view of the four service lanes from
  the department-on-a-page deck (`OD_One-Pagers.pptx`): seven steps per lane, error-path gateways,
  wait states, and the hand-offs between lanes. Each step and gateway carries the skills that serve
  it; click a skill to see everywhere it is used. Generated by `scripts/build_process_overview.py`
  (`--check` for staleness), which fails if a registry skill is not placed on the flow. The step
  wording is the deck's; the step-to-skill assignment is this registry's and is open to review.
  Steps with only a partial skill are marked: qualification and training, application consultancy,
  investment planning.

## 2026-10-22

- **Mined the full flow corpus again**, this time for function/change/switch node bodies
  rather than structure, to extend `od-node-red-flow-builder` beyond the original ten
  transformation patterns. Added three new patterns — **P11 OEE chain** (availability ×
  performance × quality), **P12 windowed extremum capture** (peak value while a threshold
  holds), **P13 liveness watchdog** (heartbeat toggle + timeout) — and fleshed out P4
  (threshold crossing) and P5 (value mapping) with real verbatim code, including two real
  violations of "read config from flow, never a literal" (a hardcoded `1.5` bar / `2000` rpm
  threshold). Completed `references/standard-functions.js`, which had only 5 of the 7
  functions `SKILL.md`'s own table promised — added `set datapointConfigFilter`, `calculate
  timerange between cycle_start and cycle_end event`, `create json payload`, and `set device
  endpoint`. Mined every node's `type` field across the corpus to resolve
  `deployable-flow.md`'s open question about which contrib palette modules the estate's
  instances actually carry (OPC-UA, two different dashboard-node generations, InfluxDB,
  PostgreSQL, Sparkplug, SOAP) — closed as mined fact, no interview needed.
- **Closed six of the tacit-knowledge placeholders** left open in `od-node-red-flow-builder`
  and `od-equipment-integration` by direct elicitation with human:jakob.gabriel: the
  consultation counterpart for signal/data-model standard changes (Plant ME / Plant IT,
  applies in both skills), the legacy `CT` topic root (no migration planned, permanent),
  edge-device approval status and variant ② brownfield/greenfield scope (both confirmed
  current), and the "Low Cost" `integration_approach` classification (both rows are Concept
  ②; a Helmholz gateway is hardware but does not count as an "edge device" in the
  department's sense). Left open on request: the shift/timezone convention, the Node-RED
  site-code → plant mapping (13 of 18 codes are inferable from the plant list already in
  `od-equipment-integration`, offered and declined pending a confirmed source), the two OESL
  guideline PDFs, and whether any plant still runs NetLink.
- **Closed five of eight open placeholders in `od-information-integration-service`** (the
  Information Integration lane's entry-point skill, previously a bare stub): the shared
  tooling/licensing/signal-standards wait-state owner (Plant ME / Plant IT), two of its three
  task templates now point at `od-equipment-integration`'s already-built
  `assets/assessment-protocol.md` and `assets/guidance-protocol.md` instead of inventing new
  ones, and the acceptance/rework-rate metric is recorded as not captured in any system today
  rather than left as an open blank. Left open: lane lead time, the investment-planning
  template, and the MSB configuration scope.
- Updated `registry.yaml`'s `open_gaps`: removed three items resolved above (contrib palette
  modules, edge-device approval, the Low-Cost/Concept-② question), split the decision-
  counterparts item to show signal/data-model standardization resolved while tool/system
  rollout stays open. Regenerated `docs/skill-state-map.md` (stale since the 2026-09-17
  equipment-integration merge).
- **Fed the new P4/P12 pattern back into `od-node-red-flow-troubleshooting`**: added a
  `hardcoded-threshold` check to `analyze_flow.py` (a limit compared or assigned as a bare
  literal in a function body instead of `flow.get(...)`) and cross-referenced it from both
  sides — the builder's P4/P12 now name the check, the troubleshooting `SKILL.md` and
  `references/symptoms.md` now name the pattern. Run fresh over all the flow corpus: 68 carry it,
  more than `spine-severed` (67). That same full-corpus run also caught two pre-existing,
  unrelated staleness bugs in `SKILL.md`'s findings table — `hardcoded-secret` was recorded
  as more flows than it affects (the finding count differs from the flow count when a flow carries two) and
  `spine-severed` with a wrong count — both corrected along with the blocker-flow total
  (98, not 59). Not an effect of anything changed this session; the table had simply drifted
  from the script.

- **Added a new skill, `od-use-case-solution-evaluation`** (24th in the registry), generalized
  from two external academic papers (Schott et al. 2017, 2020 — a 16-focus-area IT/OT
  capability maturity model, 27 complexity drivers and a realization-dependency table) rather
  than from this registry's own sources; the papers' own three-plant case study and its
  company attribution are deliberately not carried into the skill, only the method. Composes
  into `od-benefit-calculation`, `od-decision-routing`, `od-data-availability-check`,
  `od-equipment-integration` and `od-signal-standardization`; `od-use-case-definition`'s
  Phase 4 now calls it before the business case. Built deep on arrival: 5 references, 1
  script (`evaluate_fit.py` — pre-evaluation case ranking against a 70-case literature
  library, driver-to-area mapping, gap sequencing against the dependency table, a 0-100 total
  evaluation score, ASCII visualization). Raw source material (both papers, the 16
  focus-area files, `model.json`) filed in the Department knowledge base at
  `External Research/IT-IoT-Maturity-Model/`; the research session's
  own chat transcript, which carries unrelated personal/career context, stays in
  `Privat-Projekte/REHAU-IoT-Research/` instead.

- **Deepened all seven remaining Group-A stubs in one pass** (`od-acceptance-test`,
  `od-use-case-standardization`, `od-handover-and-adoption`, `od-scorecard-reporting`,
  `od-portfolio-and-savings-analysis`, `od-analytics-asset-build`, `od-sharepoint-list-export`),
  run as seven parallel forked agents, each grounded in a real, citable method rather than
  invented: FAT/SAT + ISO/IEC/IEEE 29119 (acceptance-test), ADKAR (handover/adoption), ISO
  22400-2 + Balanced Scorecard (scorecard), PMI's portfolio-management standard (portfolio
  analysis), the Kimball Lifecycle + Few's dashboard-design principles (analytics-asset
  build, scoped explicitly against the sibling `build-grafana-ops-dashboard`), and real
  Microsoft Graph/SharePoint REST export patterns (list export, which also picked up a
  schema-drift-checking script). `od-use-case-standardization` instead found its 12 cluster
  definitions/KPIs/checklists already written in the Department knowledge base
  (`_knowledge/30-Nodes/C01`-`C12` and
  `90-Sources/org-analysis/usecase-standardization-knowledgebase.md`) and used that as
  internal evidence rather than researching from scratch — 5 of 12 clusters' citations
  there are carried over, not independently re-verified this round, and the skill says so.
  Every new `assets/*.md` protocol was written to be the next skill's own input (e.g.
  `od-acceptance-test`'s protocol populates `od-handover-and-adoption`'s definition-of-done
  fields directly), and the one naming gap a fork flagged across the parallel run
  (`od-portfolio-and-savings-analysis`'s protocol not naming
  `od-sharepoint-list-export`'s `assets/export-run-log.md` by file) was fixed centrally
  afterward, along with one YAML-breaking unescaped backtick in
  `od-analytics-asset-build`'s frontmatter. Registry-state after: `od-sharepoint-list-export`
  is now deep (3 refs, 1 script); the other six are documented (refs only, no script forced
  where nothing was genuinely mechanizable). Honest gaps carried forward, not invented:
  `od-scorecard-reporting`'s four pre-existing tacit placeholders (utilization-rate target,
  asset-mix target, value-delivery-cycle system/target, escalation window) and
  `od-handover-and-adoption`'s adoption-evidence tier ranking, proposed but not yet confirmed.
  `docs/knowledge-base-alignment.md`'s Phase 3 and crosswalk entries updated to match.

- **Resolved Phase-1 tacit item #4 (ODEC vs. COP in practice) from the department's own
  record, not an interview.** The user pointed at the real source: ODEC and CoP call decks
  already exist as individually split slides in
  `Split Slides/`. Extracted all ~30 ODEC/CoP decks (2023-2026,
  ~550 slides) via raw OOXML parsing (no `python-pptx` available; stdlib `zipfile` + regex
  on `ppt/slides/slideN.xml` instead) and mined three real worked examples into
  `od-decision-routing/references/escalation-worked-examples.md`: the Groot2B cybersecurity
  item split cleanly into a strategic ODEC half and a technical COP half (both forums'
  slide templates name "Cyber Security" explicitly, one strategic one technical); a
  platform-access blocker (San Prairie, MSB Aggregation Server) that stayed at COP across
  months and never reached ODEC; and the eCR Calculator, raised at ODEC as a cross-plant
  pattern while individual eCR execution stays per-plant at COP. Also recovered the
  forums' own definition slides verbatim (Key Question / Key Objective, identical wording
  in every monthly deck) and noted a real data-quality artifact: one archived deck
  (`2023-#1-COP-not-in-use`) mixes in slides from an unrelated "MEIC" (Manufacturing
  Engineering) call and uses the forum's original name "ODIC" before the ODEC rename —
  neither used as ODEC/COP evidence. Updated `PHASE1-ELICITATION.md` topic 4 and
  `docs/knowledge-base-alignment.md`'s tacit-item table to `resolved 2026-10-22`.

- **Resolved Phase-1 tacit items #1 and #3 the same way as #4** (mining the real record
  instead of interview), after the user pointed at a second source:
  `Split Slides/10-Workshops--*.pptx` (78 workshop decks). The
  single richest source for both was one deck — Thomas Zipf's "Agility in System &
  Process" retrospective from the January 2025 MPEE strategy workshop — which documents,
  in the department's own words, several "turns out" lessons: a cosmetic dashboard-change
  request pattern with no value add, a difficult-machines-first approach that burned
  reputation and killed a local project, entry barriers deliberately decoupled from
  Cyber Security and System Deployment approvals the department does not control, and
  three successive failed fixes for plants avoiding savings self-evaluation (passive
  library → workshop slot → the current proactive calculator). Wrote
  `od-use-case-intake-triage/references/refusal-playbook.md` and
  `od-benefit-calculation/references/review-checklist.md` from this record, each stating
  honestly which narrower sub-question (the exact plant pushback phrasing; the specific
  reason a particular row fails SPRINT) the mined record does not answer and remains open.
  Updated `PHASE1-ELICITATION.md` topics 1 and 3 and `docs/knowledge-base-alignment.md`'s
  tacit-item table accordingly — five of the plan's original six tacit items are now
  resolved (fully or partially), only P-02 (non-bet system-fit judgement) has no skill at
  all yet.

- **Built `od-system-fit-check` (25th skill)** — the last of the department's original six
  Wave-1 tacit-knowledge items and the last of four Wave-1 skills the plan called
  load-bearing with no equivalent in the registry (P-02). Resolved from real department
  material rather than invented: `00-core/02-strategy.md`'s non-bets/bets/kill-criteria
  (verbatim), `OD_Skill_Map.md`'s own P-02 scope line, and — the key find — a January 2025
  tool-catalogue deck in `Split Slides/10-Workshops--...` giving
  explicit "is / is not" boundary cards for every lightweight Smart Factory tool (QFPR,
  MDA/PDA — recorded in the department's own table as "(Lightweight MES)" — Manufacturing
  Image Library, Recipe Management/Camline, the Energy Management System/WiriTec), plus
  real per-plant Smart Factory Tool Availability snapshots (San Luis Potosí, Subotica,
  Timisoara) showing the same tool "not necessary" at one plant and "needed for multiple
  use cases" at another in the same quarter. Surfaced one live discrepancy the source
  material itself contains, deliberately not resolved either way: the written non-bets say
  EMS rollout is stopped, while the 2025 tool catalogue shows WiriTec mostly rolled out and
  in active use — flagged in the skill for the user to confirm, not silently picked.
  Wired into `od-use-case-intake-triage` and `od-requirements-breakdown` (both now compose
  into it, with a body pointer at the exact step each one calls it from). Left open
  honestly: a named *real* request that looked normal and secretly needed MES/MIL/EMS —
  the skill's worked example is illustrative, not a real case. Updated
  `PHASE1-ELICITATION.md` topic 5 and `docs/knowledge-base-alignment.md` throughout — all six of
  the plan's original tacit-knowledge items now have a skill; three Wave-1 "load-bearing,
  no equivalent" skills remain genuinely unbuilt (`od-ii-cybersec-gate`,
  `od-ps-rollout-training`, `od-o-context-freshness`).

- **Finished all four remaining lane entry-points** (`od-use-case-support-service`,
  `od-information-integration-service`, `od-project-support-consultancy`,
  `od-analytical-support-service`), run as four parallel forks, plus `od-context`
  directly. These are deliberately thin "front door" pages by design, not previously
  deepened; today's pass was mostly cross-linking rather than new research: every
  `⟨to confirm⟩` that duplicated something resolved earlier this session (utilization-rate
  and asset-mix targets, the value-delivery-cycle gap, the Plant ME/Plant IT decision
  counterpart, the one-round escalation window, the adoption-evidence ranking) was
  propagated rather than re-derived, and each lane's remaining "⟨template — to confirm⟩"
  cells were checked against the sibling skills that were stubs when these pages were
  written and are now built — most resolved to a named real file
  (`od-requirements-breakdown`'s requirement template, `od-acceptance-test`'s protocol,
  `od-handover-and-adoption`'s evidence-of-adoption ranking, `od-decision-routing`'s
  decision-request template) instead of staying open questions. `od-context` itself: MIL
  and EMS abbreviations resolved from today's `od-system-fit-check` research (EMS is
  Energy, not Equipment, Management System), OESL confirmed from the decks' own title
  slides. Two real cross-lane findings surfaced and left open rather than duplicated:
  the Process First-Aid Kit has no template anywhere in the registry (two lanes
  independently hit the same gap), and `od-project-support-consultancy`'s tool/licensing
  decision owner is the same still-open counterpart as `od-decision-routing`'s
  "Tool/system rollout" row, not a separate gap.

## 2026-09-17

- Resolved the connectability-judgement tacit-knowledge item (II-01 in `knowledge-base-alignment.md`)
  by direct elicitation, and wrote it into a new `barrier-classes.md` reference: a
  practitioner difficulty ranking that corrects the raw integration-rate read (Modbus and
  Bachmann rank harder than their integration rate suggests; Siemens splits by protocol, not
  vendor), the resolved Modbus/aggregation-route contradiction, pre-assessment tells not in
  the Machine List, and named-blocker root causes (cyber-security patching usually covers one
  of five different underlying causes, not one). Includes a brownfield-hurdles section sourced
  from general industry research, marked as such rather than estate data.
- Applied a style pass across the 7 `od-machine-integration-guidance` (now
  `od-equipment-integration`) reference files: cut bold overuse, narrator asides ("this is the
  part most often missed") and dramatic section framing, without changing any fact, number,
  quote or table.
- Merged `od-equipment-integration-assessment` and `od-machine-integration-guidance` into one
  skill, `od-equipment-integration`, with two entry routes (assessment: no plant/wave
  inventory exists yet; guidance: a specific machine needs a route and the assessment already
  happened) instead of the former composes-edge handoff. Both routes now write into a
  structured, reusable protocol document. Repointed every cross-reference across the registry
  — see `derivation.md` for the reasoning.

## 2026-08-26

- Added `docs/skill-state-map.md` and `scripts/build_skill_map.py`: a generated Mermaid map of
  all 24 skills in delivery order, coloured by build state, with inbound `composes` counts and
  the three recommended next. Build state is read from the filesystem so the map cannot drift.

- Described the OPC UA direct connector properly and added availability to every connector
  table. `references/connectors.md` covers all 26 with what each reaches, over which protocol,
  which PLCs, its container image, and whether it can be used — seven cannot. The B&R and
  Bachmann connectors are `Idea · NOT AVAILABLE` while machines across those families are
  integrated over OPC UA, so `check_availability.py` now routes them to `DTQ-OPCUA-Connector`
  instead of raising a connector gap, and no longer offers the `DO NOT USE`
  `SFT-SIMATIC S7-Connector` to Siemens machines.
- Built out `od-data-availability-check`: four references, the verdict asset, and
  `check_availability.py`, which walks the six steps against the Machine List, the Connector
  Overview and the Node-RED flow corpus and names which step a request dies at. Step 5 is
  reported unproven on every run because no source in the bundle records fitness for use.
- Recorded five new open gaps found while building it, among them plants with no flow
  evidence, machines integrated by an unrecorded method, and machine rows whose
  `plc_vendor` is not a vendor.

## 2026-08-25

- Adopted the Open Knowledge Format across the registry. Every concept carries OKF
  frontmatter; a `SKILL.md` carries its OKF fields under `metadata.okf`, because the Agent
  Skills spec allows only six top-level keys and anything else fails packaging and upload.
  Contract in [docs/okf-conventions.md](docs/okf-conventions.md), guard in
  `scripts/verify_okf.py`, generated indexes from `scripts/build_okf_index.py`.
- Removed `argument-hint` from `build-grafana-ops-dashboard/SKILL.md`, which would have
  failed upload with a hard error; it now lives under `metadata`.
- Replaced `last_verified` with `sources_read` on all 24 skills. The old name asserted a
  verification nobody performed and carried no actor, so no OKF trust tier could be derived
  from it. Every concept is `unverified`, which is accurate.
- Fixed defects found by review: hand-rolled argument parsing in four scripts silently
  dropped `--lane=` and `--capability=` and reported success; `tokens()` never split
  camelCase, so `HeadTemperature` was reported as German; ambiguous terms across Spanish,
  Portuguese and Serbian resolved to whichever loaded first; three call sites read the label
  column differently; the money check missed a currency-and-year form its own template
  uses; a `"signal" not in row` filter dropped real rows such as `SignalQuality`; unnamed
  Node-RED groups leaked an empty entry into a finding; and `arraySplt` was gated on the
  wrong field.
- Synced `authority_level` between `registry.yaml` and each `SKILL.md` — the registry granted
  `execute-autonomously` in one case where the skill capped at recommend — and made
  `validate_registry.py` fail on any disagreement or on a placeholder inside metadata.
- Added the epic and user stories output to `od-requirements-breakdown`.
- Added multilingual tag handling to `od-signal-standardization`.
