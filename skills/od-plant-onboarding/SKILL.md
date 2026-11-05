---
name: od-plant-onboarding
description: >-
  Lay out the onboarding path of one plant through the OD skill set, in order - place the plant
  by its starting profile (no machines recorded, machines but none integrated, partly or fully
  integrated), then walk the stages from recording the plant and assessing its equipment, through
  intake and the three new-state lanes, to handover, training and joining the monthly rhythm,
  naming the skill, the artefact and the role for each stage. Use when a plant enters OD scope,
  when a plant has records but no roadmap, when a local key user asks where to start, or when a
  plant's onboarding has stalled and the missing stage must be found.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
allowed-tools: Read Grep Glob
metadata:
  id: od-plant-onboarding
  tier: practice
  lane: all
  new_state_lane: Spine
  new_state_step: Plant onboarding
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-use-case-intake-triage, od-system-fit-check, od-sharepoint-list-export, od-equipment-integration, od-data-availability-check, od-template-resolution, od-cross-plant-compatibility, catalog-usecase, od-decision-routing, od-handover-and-adoption, od-rollout-training, od-scorecard-reporting, od-risk-watch, od-retro]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/information-integration-service/playbook.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/information-integration-service/tasks.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case/landscape.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/06-operating-rhythm.md
    - ops-knowledge-graph/_knowledge/20-Done/Machine connectivity rollout.md
    - Registry docs/new-state-flow.md and docs/new-state/OD_NewState_Flow.mermaid (the three lanes and their steps), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Graph/Plants (plant notes, plant-profile blocks), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Graph/Tools and Graph/Connectors note names, read 2026-11-05
    - Skill od-data-availability-check, references/plant-instance-map.md, read 2026-11-05
  okf:
    type: Agent Skill
    title: Plant onboarding
    tags: [all, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Plant onboarding

Read `od-context` first.

Plan item O-09 of the department's skill map. Its source column reads "- (new)": **no Department OS document describes
plant onboarding**, so this skill is assembled from the playbooks, the new-state lanes and the plant records. It is a
route through existing skills, not a new method. Where the sources are silent it says so.

The department's aim is that use-case work, machine integration and requirement derivation happen **decentrally in the
plants** rather than centrally (skill map, purpose). A local key user at a plant needs one place that says: *where are we,
what comes next, which skill, what artefact, who decides.*

## Trigger and definition of done

- Trigger (plan): a new plant enters scope. The sources do not define "enters scope" (the strategic-plant list is
  incomplete in the landscape module): `⟨scope rule, to confirm with the OD lead role⟩`. The same path serves a plant that
  has records but no roadmap, or a plant whose onboarding stalled.
- Done (proposal, not a source rule): each stage in the table below has its artefact filed, or an explicit `⟨reason it does
  not apply⟩`; the plant appears in the Equipment Integration report and the readiness matrix; the plant has a plant-side
  owner for each lane it uses; the plant is in the monthly rhythm.

## The references

| File | Use it for |
|---|---|
| [`references/plant-landscape.md`](references/plant-landscape.md) | How to read the plant records (region, machines, integrated share, use cases, main controller and integration method) and how to obtain them live; the four starting profiles and where each begins |
| [`assets/onboarding-path.md`](assets/onboarding-path.md) | The tracker: one row per stage with skill, artefact, role, evidence and status |

## Step 0: place the plant

1. Find the plant in the live plant record, read as described in [`plant-landscape.md`](references/plant-landscape.md). Note
   region, machines recorded, integrated share. Always read the current Machine List; this skill holds no figures.
2. Assign the starting profile: **A** no machines recorded · **B** machines recorded, none integrated ·
   **C** partly integrated · **D** fully integrated.
3. The profile sets the entry stage (last column of the profile table). Do not skip earlier stages for a profile-C plant
   without checking their artefacts exist: a partly integrated plant may still have no roadmap.

## The path

| Stage | What happens | Skill (in order) | Artefact | Lane in new-state flow | Decided by |
|---|---|---|---|---|---|
| 1. Record the plant | Plant, machines, tools, use cases and legacy applications are in the lists the department reads; refresh the vault view | `od-sharepoint-list-export`; ground rule `od-context` | Plant record complete; run log | Spine | Plant ME / Plant IT for content; OD for the lists' structure |
| 2. Assess the equipment | Equipment inventory with connectability and a barrier log; sequence a roadmap (this is playbook step 1, triggered by "new plant / integration wave") | `od-equipment-integration` (assessment route); `od-data-availability-check` for what the platform already receives; `od-barrier-triage` (planned) for machines that will not connect | `assets/assessment-protocol.md` of `od-equipment-integration`; barrier log | Lane 3b entry, Lane 1b | IIAE with Plant ME / Plant IT |
| 3. Take in demands | Each plant demand is classified: known use case, new use case, new system or connector | `od-use-case-intake-triage`, `od-system-fit-check`, `od-template-resolution` (start from the approved master) | Intake decision with written reason; fit check | Intake, then Lane 1, 2 or 3 | DBVE with Plant ME (prioritization: recommend) |
| 4. First wins from the catalog | Machines already connected: pick a catalogued use case and apply its template | `catalog-usecase`, `od-cross-plant-compatibility` (is the standard consumable here?), `od-analytics-asset-build`, `build-grafana-ops-dashboard`, `catalog-guardrails` | Asset live on the plant's local Grafana; compatibility check | Lane 1 (1a) | The plant decides what it runs |
| 5. Connect what is not connected | Requirements, cost and approval, cyber gate, build the connection, standardize signals, accept | `od-requirements-breakdown`, `od-investment-input` and `od-decision-routing` (spend via eCR), `od-cybersec-gate` (planned), `od-equipment-integration` (guidance route), `od-node-red-flow-builder`, `od-signal-standardization`, `od-acceptance-test` | Requirement spec; decision request; guidance protocol per machine; signal analysis report; acceptance protocol | Lane 1 (1b), Lane 3b | IIAE: equipment go-ahead is execute-with-approval; investment by the OD lead with BA Operations (recommend); Cyber Security sign-off for external connection |
| 6. Develop a new use case where no catalog entry fits | Define, check data, prove, business case, capital request, implement | `od-use-case-definition`, `od-use-case-solution-evaluation`, `od-prototype-poc`, `od-benefit-calculation`, `od-capital-request` (planned), `od-use-case-standardization` for graduation | Definition one-pager; evaluation; prototype record; benefit calculation | Lane 2 | DBVE with Plant ME; spend and rollout route via `od-decision-routing` |
| 7. Hand over and train | Solution accepted, then adopted by the plant | `od-handover-and-adoption`, `od-rollout-training` (planned) | Handover protocol; adoption evidence | Lane 2 and 3 end steps | The plant owns "into daily use" |
| 8. Join the rhythm | Plant numbers in the Scorecard; plant issues in ODEC and COP; plant risks and learnings | `od-scorecard-reporting`, `od-portfolio-and-savings-analysis`, `od-risk-watch`, `od-retro`, `od-context-freshness` (planned) | Scorecard entries; round inputs; risk reading; retro record | Spine | OD lead |

A 3a path (new system, via IT demand) is not part of a normal plant onboarding; it is taken only when stage 3 or 5 finds
a need no connector can meet: `it-demand-package`, `deploy-appstore`.

## What each profile skips or adds

| Profile | Start | Special attention |
|---|---|---|
| A | Stage 1 | Cannot be graded or compared; do not infer. The plant instance map in `od-data-availability-check` shows which plants lack flow evidence: check the edge platform directly |
| B | Stage 2 | The route to the platform may not be chosen: in some profile-B plants most machines are recorded as "evaluation ongoing". Choosing the ingress variant is part of stage 2, not stage 5 |
| C | Stage 3 (and 2 for the remainder) | A low share with a large estate means stage 2 and 5 dominate; a high share means stages 4 and 6 |
| D | Stage 3, 4, 6 | No integration roadmap for recorded machines; catalog reuse and Lane 2 candidates |

## What is still open

- **Plant-side owner per lane** does not exist yet (skill map: open gap). Until it does, the table names OD roles and
  "Plant ME / Plant IT"; assign `⟨plant-side owner per lane⟩` at the start of stage 1.
- **Lead times per lane** are `⟨to confirm⟩` in all four lane packs; no stage can be judged late.
- **Definition of "enters scope"** and the full strategic-plant list.
- **Whether onboarding has a defined end** in the department: the done-criteria above are a proposal.
- **Training package** (`od-rollout-training`) is planned, not built; stage 7 has no training artefact yet.
- Three of the stage-5 skills are planned (`od-cybersec-gate`) or only drafted (`od-investment-input`, `od-prototype-poc`
  exist as drafts in the registry); the Cyber Security sign-off standard is `to collect` in the resource register.

## Do not

- Do not start with a use case before the plant is recorded: stage 1 is the precondition for every comparison.
- Do not assume the plant looks like the first plant: run `od-cross-plant-compatibility` before taking a standard.
- Do not connect a machine to an external system without Cyber Security / OT sign-off.
- Do not name individuals in the tracker; roles only.
- Do not reorder the stages to hit a date; if a stage cannot start, record the wait state (investment approval, Cyber
  Security sign-off, a decision on shared tooling, per the playbook) rather than skipping.
