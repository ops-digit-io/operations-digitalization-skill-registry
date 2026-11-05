---
type: Design Record
title: New-state flow
description: "The target process flow the registry's skills are gauged against - three branched service lanes, the skill that serves each step, and the five net-new skills it still lacks."
status: draft
owner: human:jakob.gabriel
tags: [process-flow, lanes, gap-analysis]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# New-state flow

The registry's skills are measured against this flow: each step of it names the skill that
serves the step and whether that skill is built, partial or missing. Four files in
[`new-state/`](new-state/) show it, copied unchanged from the files the owner supplied on
2026-11-05.

| File | What it shows |
|---|---|
| [`OD_NewState_Flow.mermaid`](new-state/OD_NewState_Flow.mermaid) | The flow as one Mermaid flowchart: intake, three lanes, gateways, the five gap steps dashed |
| [`OD_NewState_ProcessFlow.html`](new-state/OD_NewState_ProcessFlow.html) | Lane-by-lane process flow with skill chips coloured Built / Partial / Gap and the external waits |
| [`OD_NewState_BPMN.html`](new-state/OD_NewState_BPMN.html) | The same flow in BPMN notation (events, tasks, gateways), laid out like [`process-overview.html`](process-overview.html) |
| [`OD_NewState_VSM_SkillMap.html`](new-state/OD_NewState_VSM_SkillMap.html) | Step-by-step table per lane with touch time, queue time and the registry skill and state per step; the gap register |

## The flow in short

One lane per demand, decided at intake by `od-use-case-intake-triage` and `od-system-fit-check`:

- **Lane 1, run a known use case** (self-service). 1a: machine already connected. 1b: not connected, standardized-system onboarding.
- **Lane 2, develop a new use case** (OD-led). Definition, features and data check, prototype, business case, capital request, implement and graduate into the catalog.
- **Lane 3, new system or connector** (OD front-end, external, IT and Cyber Security). Shared front-end, then 3a a new system or 3b a new connector.

A proven, repeatable Lane 2 result graduates into the catalog and becomes a Lane 1 case.

## What the flow says is missing

Five net-new skills: `catalog-usecase`, `catalog-systems`, `catalog-guardrails` (the Lane 1
self-service layer), `deploy-appstore` and `it-demand-package` (Lane 3a). They were not in the
registry when the flow was drawn and now exist as draft scaffolds. Two spots are thin: prototype / proof of concept, and capital-request packaging.
The business-case assessment rubric `bc-assessment` is named as living outside the registry.

The skill-map file also records one open decision: `od-analytical-support-service`
orchestrates the Analytics lane that the new state dissolves, so it needs to be re-homed
into Lane 1 or Lane 2, or retired.

## Cross-check against the registry (2026-11-05)

Skill names in the four files compared with the 56 skills in `skills/` (25 existing, 31 drafts written from this flow, the department's plan and the slide-deck practice review):

- 28 of the 56 skills are named in at least one file; 17 are named in all four. The other 28 are placed on the flow by this registry alone: the 18 skills built from the department's plan and the flow's two thin spots, and the two lane orchestrators the files do not mention. Where each skill sits: [`new-state-skill-map.md`](new-state-skill-map.md); the interactive version is the site built by `scripts/build_site.py`.
- Every name the flow marks as Built exists in the registry. The one name that is not a registry skill is `bc-assessment`, which the
  flow itself places outside the registry.
- The existing [`process-overview.html`](process-overview.html) draws **four** service lanes; the new
  state has **three** branched lanes. The two disagree until that overview is regenerated.

## Skills the flow files do not place

13 registry skills are not on the three diagrams (`OD_NewState_Flow.mermaid`, `OD_NewState_ProcessFlow.html`,
`OD_NewState_BPMN.html`). Two are in none of the four files; eleven appear only in the skill-map table
(`OD_NewState_VSM_SkillMap.html`) or in one more file. They are listed here because the diagrams are the picture of the flow
and the registry should account for every skill in it.

### In none of the four files (2)

| Skill | Old lane and owner role | Trigger and definition of done (from `registry.yaml`) | Where its work is served in the flow (inferred) |
|---|---|---|---|
| `od-information-integration-service` | Information Integration Service, IIoT Interface & Automation Engineer | Equipment integration or data-model harmonization need per roadmap; machine integrated, signals standardized, data on the data platform | Lane 3b: `od-equipment-integration`, `od-signal-standardization`, `od-node-red-flow-builder` |
| `od-project-support-consultancy` | Project Support & Application Consultancy, IIoT Interface & Automation Engineer | Digital investment project kick-off; integration project managed to acceptance test, application consulted and accepted | Lane 3: `od-acceptance-test`, `od-handover-and-adoption`; application consultancy has no skill of its own |

Open: whether each lane orchestrator is re-homed into the new lanes or retired. The flow says nothing about it.

### Only in the skill-map table, not on the diagrams (11)

| Skill | Where the skill-map table puts it | Missing from |
|---|---|---|
| `od-context` | Foundation, applies to every step | Flow, ProcessFlow, BPMN |
| `od-use-case-support-service` | Lane 2, step 1 (definition) | Flow, ProcessFlow, BPMN |
| `od-use-case-solution-evaluation` | Lane 2, step 2 (features and data check) | Flow, ProcessFlow, BPMN |
| `od-portfolio-and-savings-analysis` | Lane 2, step 4, and the supporting spine | Flow, ProcessFlow, BPMN |
| `od-use-case-standardization` | Lane 2, step 6 (graduate to the catalog) | Flow, ProcessFlow, BPMN |
| `build-grafana-ops-dashboard` | Lane 1, branch 1a, step 2 (self-service mode) | Flow, ProcessFlow, BPMN |
| `od-node-red-flow-troubleshooting` | Lane 3b, step 5b (partial) | Flow, ProcessFlow, BPMN |
| `od-scorecard-reporting` | Supporting spine, not drawn as a step | Flow, ProcessFlow, BPMN |
| `od-sharepoint-list-export` | Supporting spine, not drawn as a step | Flow, ProcessFlow, BPMN |
| `od-analytical-support-service` | Supporting spine: the open decision, the lane the new state dissolves | Flow, ProcessFlow, BPMN |
| `od-use-case-intake-triage` | Intake classifier | Flow (the Mermaid file only) |

The four files are kept exactly as supplied. To make the diagrams agree with the table, these skills have to be drawn into them.

The touch and queue times in the skill-map file are placeholders (`⟨…⟩`) to be confirmed with
OD data; they are not measurements.
