---
name: dept-plant-onboarding
description: >-
  Answers "where does this plant start, and what comes next?". Places one plant by what is recorded
  (no machines recorded, machines but none integrated, partly or fully integrated), then walks eight
  stages in order from recording the plant and assessing its equipment, through demand intake, first
  catalog wins, connecting machines and new use cases, to handover, training and joining the
  reporting routines, naming skill, artefact and responsible role per stage. Use when a plant enters
  scope, has records but no roadmap, a local key user asks where to start, or onboarding stalled.
  Not for diagnosing unequal savings or tiering (dept-plant-diagnosis) or classifying one request
  (dept-intake).
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: dept-plant-onboarding
  aliases: [od-plant-onboarding]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Spine"
  new_state_step: "Supporting spine"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  requires: [dept-context]
  composes: [dept-intake, invest-screen, know-sharepoint-export, mi-equipment, mi-data-availability, catalog-template, catalog-compatibility, catalog-usecase, dept-decision-rights, deploy-handover, know-training, metrics-scorecard, dept-risk, dept-retro]
  okf:
    type: Agent Skill
    title: Plant onboarding
    tags: [all, practice, new-state, draft]
---

# Plant onboarding

- Read `dept-context` first.
- Basis: the playbooks, the new-state lanes and the plant records. No department document describes plant onboarding, so this is a route through existing skills, not a new method; where the sources are silent it says so.
- Aim: use-case work, machine integration and requirement derivation happen **decentrally in the plants**. A local key user needs one place that says where the plant is, what comes next, which skill, which artefact, who decides.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Trigger and definition of done

- Trigger: a new plant enters scope.
  - The sources do not define "enters scope" (the strategic-plant list is incomplete): `⟨scope rule, to confirm with the OD lead role⟩`.
  - The same path serves a plant that has records but no roadmap, or a plant whose onboarding stalled.
- Done (proposal, not a source rule): each stage in the path table has its artefact filed, or an explicit `⟨reason it does not apply⟩`.
  - The plant appears in the Equipment Integration report and the readiness matrix.
  - The plant has a plant-side owner for each lane it uses and is in the department's reporting routines.

## The references

| File | Open when |
|---|---|
| [`references/plant-landscape.md`](references/plant-landscape.md) | You place a plant: how to read the plant record (region, machines, integrated share, use cases, main controller, integration method), get it live, and the four starting profiles |
| [`assets/onboarding-path.md`](assets/onboarding-path.md) | You start the tracker: one row per stage with skill, artefact, role, evidence and status |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | You plan a plant visit, tier first mover vs fast follower, judge readiness signals, or plan waves and migration |
| [`references/background.md`](references/background.md) | You need context, the required-output table or the handoff text; never an instruction |

## Place the plant (before stage 1)

1. Find the plant in the live plant record, read as described in `references/plant-landscape.md`. Note region, machines recorded, integrated share. Always read the current Machine List, because this skill holds no figures.
2. Assign the starting profile: **A** no machines recorded, **B** machines recorded but none integrated, **C** partly integrated, **D** fully integrated.
3. The profile sets the entry stage (last column of the profile table). Do not skip earlier stages for a profile-C plant without checking their artefacts exist: a partly integrated plant may still have no roadmap.

## The path

| Stage | What happens | Skill (in order) | Artefact | Lane in new-state flow | Decided by |
|---|---|---|---|---|---|
| 1. Record the plant | Plant, machines, tools, use cases and legacy applications are in the lists the department reads; refresh the knowledge base view | `know-sharepoint-export`; ground rule `dept-context` | Plant record complete; run log | Spine | Plant ME / Plant IT for content; OD for the lists' structure |
| 2. Assess the equipment | Equipment inventory with connectability and a barrier log; sequence a roadmap (playbook step 1, triggered by "new plant / integration wave") | `mi-equipment` (assessment route); `mi-data-availability` for what the platform already receives; `mi-equipment` (planned) for machines that will not connect | `assets/assessment-protocol.md` of `mi-equipment`; barrier log | Lane 3b entry, Lane 1b | IIAE with Plant ME / Plant IT |
| 3. Take in demands | Each plant demand is classified: known use case, new use case, new system or connector | `dept-intake`, `invest-screen`, `catalog-template` (start from the approved master) | Intake decision with written reason; fit check | Intake, then Lane 1, 2 or 3 | DBVE with Plant ME (prioritization: recommend) |
| 4. First wins from the catalog | Machines already connected: pick a catalogued use case and apply its template | `catalog-usecase`, `catalog-compatibility` (is the standard consumable here?), `ops-analytics-asset`, `ops-dashboard-engine`, `catalog-usecase` | Asset live on the plant's local Grafana; compatibility check | Lane 1 (1a) | The plant decides what it runs |
| 5. Connect what is not connected | Requirements, cost and approval, Cyber Security sign-off in parallel (blocks only go-live), build the connection, standardize signals, accept | `funnel-requirements`, `bc-cost` and `dept-decision-rights` (spend via eCR), `deploy-cybersec` (planned), `mi-equipment` (guidance route), `mi-flow`, `mi-signals`, `deploy-acceptance` | Requirement spec; decision request; guidance protocol per machine; signal analysis report; acceptance protocol | Lane 1 (1b), Lane 3b | IIAE: equipment go-ahead is execute-with-approval; investment by the OD lead with BA Operations (recommend); Cyber Security sign-off for external connection |
| 6. Develop a new use case where no catalog entry fits | Define, check data, prove, business case, capital request, implement | `funnel-use-case`, `funnel-evaluation`, `funnel-prototype`, `bc-build`, `bc-capital-request` (planned), `catalog-standardization` for graduation | Definition one-pager; evaluation; prototype record; benefit calculation | Lane 2 | DBVE with Plant ME; spend and rollout route via `dept-decision-rights` |
| 7. Hand over and train | Solution accepted, then adopted by the plant | `deploy-handover`, `know-training` (planned) | Handover protocol; adoption evidence | Lane 2 and 3 end steps | The plant owns "into daily use" |
| 8. Join the routines | Plant numbers in the Scorecard; plant issues in the COP or with the OD lead (ODEC is historical); plant risks and learnings | `metrics-scorecard`, `bc-portfolio`, `dept-risk`, `dept-retro`, `dept-context-freshness` (planned) | Scorecard entries; round inputs; risk reading; retro record | Spine | OD lead |

- A 3a path (new system, via IT demand) is not part of a normal plant onboarding; take it only when stage 3 or 5 finds a need no connector can meet: OpenSpec IT demand (external), `deploy-appstore`.

## Stage gate (before moving to the next stage)

1. The stage's artefact is filed (file or list reference in the tracker) or its row says why it does not apply.
2. A role is named as responsible; no individual names.
3. Status is one of: not started, in progress, waiting (state the wait), done, not applicable (state why).
4. If the stage cannot start, the wait state is recorded; the stage is not skipped.

## Example (fictional)

```text
Plant:   Plant X (fictional), Machine List read 2026-03-02
Record:  120 machines recorded, 45 integrated (38 percent)  ->  profile C
Entry:   Stage 3 for new demands, stage 2 for the 75 machines not yet integrated
Tracker: 1 Record the plant   | know-sharepoint-export | plant record    | OD data role | done
         2 Assess equipment   | mi-equipment           | barrier log     | IIAE         | in progress
         3 Take in demands    | dept-intake            | intake decision | DBVE         | in progress
         5 Connect machines   | deploy-cybersec        | sign-off package| Plant IT     | waiting: sign-off before go-live
         6 Develop use case   | -                      | -               | -            | not applicable: catalog entry fits
```

## What each profile skips or adds

| Profile | Start | Special attention |
|---|---|---|
| A | Stage 1 | Cannot be graded or compared; do not infer. The plant instance map in `mi-data-availability` shows which plants lack flow evidence: check the edge platform directly |
| B | Stage 2 | The route to the platform may not be chosen: in some profile-B plants most machines are recorded as "evaluation ongoing". Choosing the ingress variant is part of stage 2, not stage 5 |
| C | Stage 3 (and 2 for the remainder) | A low share with a large estate means stage 2 and 5 dominate; a high share means stages 4 and 6 |
| D | Stage 3, 4, 6 | No integration roadmap for recorded machines; catalog reuse and Lane 2 candidates |

## What is still open

- **Plant-side owner per lane** does not exist yet (skill map: open gap). Until it does, the table names OD roles and "Plant ME / Plant IT"; assign `⟨plant-side owner per lane⟩` at the start of stage 1.
- **Lead times per lane** are `⟨to confirm⟩` in all four lane packs; no stage can be judged late.
- **Definition of "enters scope"** and the full strategic-plant list.
- **Whether onboarding has a defined end** in the department: the done-criteria above are a proposal.
- **Training package** (`know-training`) is planned, not built; stage 7 has no training artefact yet.
- Planned or only drafted stage skills: `deploy-cybersec` is planned; `bc-cost` and `funnel-prototype` exist as drafts. The Cyber Security sign-off standard is `to collect` in the resource register.

## Pitfalls

- **Starting with the hardest machine types.** Scale known types and take at most one unknown type per new deployment, because unknown types are where integrations stall.
- **Treating first mover vs fast follower as eligibility.** It decides central capacity (`references/process-chain-practice.md`).
- **Starting with a use case before the plant is recorded.** Stage 1 is the precondition for every comparison; unrecorded machines read as zero.
- **Assuming the plant looks like the first plant.** Run `catalog-compatibility` before taking a standard, because controllers, field networks and ingress differ.
- **Connecting a machine to an external system without Cyber Security / OT sign-off.** The sign-off runs in parallel with planning and build and blocks only go-live: start the package early.
- **Naming individuals in the tracker.** Roles only.
- **Reordering stages to hit a date.** If a stage cannot start, record the wait state (investment approval, Cyber Security sign-off before go-live, a decision on shared tooling) rather than skipping, because a skipped stage resurfaces as rework.
- **Reading "100 percent integrated" as complete.** Check it is not a small recorded subset.

## Human gate and AI-agent notes

- The agent drafts the profile, the tracker and the next-stage list; it never connects a machine, approves spend or signs off.
- Equipment go-ahead, investment and Cyber Security sign-off stay with the roles in the path table.
- Cite the list name and read date for every plant figure.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/background.md`](references/background.md) | You need context, the required-output table or the handoff text; never an instruction |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
