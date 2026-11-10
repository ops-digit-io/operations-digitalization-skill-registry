---
type: Skill Reference
title: Procedure
description: Formerly the skill od-project-support-consultancy, absorbed into it-demand-package on 2026-11-10 to remove duplication against the department context. Run the Project Support & Application Consultancy lane — kick off digital investment projects with the MPEE OD team, break down requirements, manage equipment and solution integration projects to acceptance, consult on the Manufacturing Software Suite and manufacturing apps, confirm use cases are integrated into daily processes, and report progress and impact into the department's reporting. Use when a digital investment project starts or stalls, when a project needs a kick-off agenda, requirement spec or status report, when application-consultancy advice is needed, or when progress and impact
resource: ../../SKILL.md
status: stable
owner: human:jakob.gabriel
tags:
- lane
- project-support-consultancy
- absorbed
derived_from:
- ops-knowledge-graph/.../20-lanes/project-support-consultancy/{playbook,skills,tasks,metrics,agent-brief}.md
generated:
  by: claude-code/1
  at: 2026-10-23 00:00:00+00:00
---
# Project Support & Application Consultancy

> **Absorbed.** This was the skill `od-project-support-consultancy`. It now runs as a mode of [`it-demand-package`](../../SKILL.md) (merged 2026-11-10, see `log.md`). Its authority stays as it was: read-only on systems; draft on project artefacts; recommend on sequencing.

Read `dept-os` first.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/task-chain-and-tool-use.md`](references/task-chain-and-tool-use.md) | The lane's recurring tasks as a trigger chain (starts when, needs, tool, leaves behind, feeds), why each tool has its access, metric hooks, the business-case shape (A/B anchors, strategic fit) |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Project order and plan structure, kick-off workshop, status colours, milestone and closure reports, integration-workshop preparation, wave and consultancy gates, handover lessons, handoff contract, agent notes |
| [`references/composed-protocols.md`](references/composed-protocols.md) | Which real protocol in which composed skill answers each happy-path step — this lane routes through them, it does not duplicate them |

**Trigger.** A digital investment project kick-off.
**Definition of done.** Integration project managed to acceptance test; application
consulted and accepted. **Customer.** Plant / project teams. **Scope:** regional.
**Lead time:** ⟨to confirm⟩.

## Happy path

| # | Step | Who | Control point |
|---|---|---|---|
| 1 | Digital investment project initiated per plant roadmap | Plant + OD | Project in plan |
| 2 | Kick-off with the MPEE OD team; scope and requirements | IIAE/DBVE + Plant | Scope agreed — see `funnel-requirements` |
| 3 | Equipment and solution integration project management | IIAE | Milestones tracked |
| 4 | Application consultancy (Manufacturing Software Suite, apps) | Human | Solution design accepted |
| 5 | Acceptance testing | IIAE | Acceptance passed |
| 6 | Ensure use cases are fully integrated into daily processes | both | Adoption confirmed |
| 7 | Report progress and impact (Equipment / Applications / Use Cases) | both | Progress and impact reporting updated |

Step 5 → `od-acceptance-test`. Step 6 → `od-handover-and-adoption` — "adoption confirmed"
means its three-tier evidence ranking is met, never just that handover is marked `DONE`.
Step 7 → `od-scorecard-reporting`. Investment and gate questions → `od-decision-routing`.

## Error paths

- **Investment not approved or resources not allocated** → the project stays "captured"
  and is flagged **blocked**. A blocked project is steering information, not a failure to
  hide: blocking points say why value is not flowing.
- **Solution fails acceptance** → rework loop back to step 3.
- **Tool or licensing dependency unresolved** → wait state ⟨owner to confirm⟩.
- **Application has no operations concept** (no business owner, IT owner, service level or support role) →
  do not roll out; route to the operations-concept discussion first.

## Wait states

Awaiting resource allocation to prioritize the digital initiative · awaiting a tool or
licensing decision ⟨owner to confirm⟩ · awaiting Cyber Security sign-off before go-live (runs in parallel with planning and build).

## Recurring tasks

| Task | Trigger | Template |
|---|---|---|
| Project kick-off with OD team | Digital investment project initiated | ⟨approved kick-off agenda — to confirm⟩; the structure the decks show is in `references/process-chain-practice.md` |
| Requirements breakdown | Kick-off done | `funnel-requirements`'s `assets/requirement-template.md` |
| Integration project status | Weekly / milestone | Project tracker |
| Application consultancy session | Solution design needed | ⟨template — to confirm; PS-04 application consulting was never built as its own skill⟩ |
| Acceptance test | Solution ready | `od-acceptance-test`'s `assets/acceptance-test-protocol.md` |
| Progress & impact reporting | On request or on the department's own schedule | Department report, formerly the ODEC report (Equipment / Applications / Use Cases) |

## Stage gates

Projects move: **Captured → Evaluated → Assessed → Planned/Implementation → *gate:
artefact accepted* → Handed over → Effective**, mapping onto the OD value chain
(01 Digitalization Benefit Analysis · 02 System & Connectivity Assessment · 03 System &
Connectivity Roadmap · 04 SF Use Case Executive Support · 05 Digitalization Demands &
Iterations · 06 Enhanced Process Understanding & Control).

Record, per undertaking: facility, region, stage, gate date, business case, **blocking
point with its owner and class**, opportunity, handover status. ⟨A single flow owner for
the end-to-end chain is not yet named — to confirm.⟩

## Systems and access

Project management method / tracker (read / update) · Manufacturing Software Suite
(configure ⟨scope to confirm⟩) · Manufacturing Apps / app store on IIoT Edge (deploy) ·
acceptance-test protocols (author) · department reporting, formerly ODEC (read / update) · investment planning
templates (author).

Reference: **ProView Support Process** (incident management, Hannover et al.) as the
support/handover reference.

## Autonomy

**May** — read the project tracker and roadmaps; draft kick-off agendas, requirement
specs and status reports; assemble progress/impact reporting (the department report, formerly the ODEC report); flag blocked projects.
**May not** — commit investment or allocate resources; approve acceptance; deploy to
production; make licensing commitments.
**Guardrails** — never sign off acceptance; never invent progress or impact figures;
respect Cyber Security sign-off.

## Metrics for this lane

| Metric | Source | Target | Intervene from |
|---|---|---|---|
| Integration projects to acceptance | ⟨project tracker — to collect⟩ | ⟨to confirm⟩ | acceptance slippage |
| Equipment integration progress | Department report · Equipment Integration | on plan | behind plan |
| Applications progress | Department report · Applications | on plan | behind plan |
| Use-case impact | Department report · Use Cases (Impact) | ⟨to confirm⟩ | impact below plan |
| On-time delivery | ⟨tracker — to collect⟩ | ⟨to confirm⟩ | delays rising |

## Handover / rework rule

The delivered solution goes to plant operations and to the Use Case Support lane for
adoption. It returns for rework if acceptance fails, or if the use case is not integrated
into daily operations.
