---
name: od-project-support-consultancy
description: >-
  Run the Project Support & Application Consultancy lane — kick off digital investment
  projects with the MPEE OD team, break down requirements, manage equipment and solution
  integration projects to acceptance, consult on the Manufacturing Software Suite and
  manufacturing apps, confirm use cases are integrated into daily processes, and report
  progress and impact into the ODEC cycle. Use when a digital investment project starts
  or stalls, when a project needs a kick-off agenda, requirement spec or status report,
  when application-consultancy advice is needed, or when ODEC progress and impact
  reporting is due. Owner is the IIoT Interface & Automation Engineer (IIAE).
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-project-support-consultancy
  tier: lane
  lane: project-support-consultancy
  owner_role: IIoT Interface & Automation Engineer (IIAE) — ⟨named person to confirm⟩
  capacity: ⟨to confirm⟩
  authority_level: read-only on systems; draft on project artefacts; recommend on sequencing
  escalation: OD lead (Thomas Zipf) via ODEC
  status: stable
  last_verified: 2026-08-10
  requires: [od-context]
  composes: [od-acceptance-test, od-handover-and-adoption, od-scorecard-reporting, od-decision-routing]
  derived_from:
    - ops-knowledge-graph/.../20-lanes/project-support-consultancy/{playbook,skills,tasks,metrics,agent-brief}.md
---

# Project Support & Application Consultancy

Read `od-context` first.

**Trigger.** A digital investment project kick-off.
**Definition of done.** Integration project managed to acceptance test; application
consulted and accepted. **Customer.** Plant / project teams. **Scope:** regional.
**Lead time:** ⟨to confirm⟩.

Delivered partly as Shared Services with ContiTech; interface compatibility must be
maintained.

## Happy path

| # | Step | Who | Control point |
|---|---|---|---|
| 1 | Digital investment project initiated per plant roadmap | Plant + OD | Project in plan |
| 2 | Kick-off with the MPEE OD team; scope and requirements | IIAE/DBVE + Plant | Scope agreed |
| 3 | Equipment and solution integration project management | IIAE | Milestones tracked |
| 4 | Application consultancy (Manufacturing Software Suite, apps) | Human | Solution design accepted |
| 5 | Acceptance testing | IIAE | Acceptance passed |
| 6 | Ensure use cases are fully integrated into daily processes | both | Adoption confirmed |
| 7 | Report progress and impact (Equipment / Applications / Use Cases) | both | ODEC reporting updated |

Step 5 → `od-acceptance-test`. Step 6 → `od-handover-and-adoption`. Step 7 →
`od-scorecard-reporting`. Investment and gate questions → `od-decision-routing`.

## Error paths

- **Investment not approved or resources not allocated** → the project stays "captured"
  and is flagged **blocked**. A blocked project is steering information, not a failure to
  hide: blocking points say why value is not flowing.
- **Solution fails acceptance** → rework loop back to step 3.
- **ContiTech tool or licensing dependency unresolved** → wait state.

## Wait states

Awaiting resource allocation to prioritize the digital initiative · awaiting a ContiTech
decision (tool, licensing, DeepSpect dependency) · awaiting Cyber Security sign-off.

## Recurring tasks

| Task | Trigger | Template |
|---|---|---|
| Project kick-off with OD team | Digital investment project initiated | ⟨kick-off agenda — to confirm⟩ |
| Requirements breakdown | Kick-off done | ⟨requirement spec — to confirm⟩ |
| Integration project status | Weekly / milestone | Project tracker |
| Application consultancy session | Solution design needed | ⟨template — to confirm⟩ |
| Acceptance test | Solution ready | Acceptance test protocol |
| Progress & impact reporting | ODEC cycle | ODEC report (Equipment / Applications / Use Cases) |

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
acceptance-test protocols (author) · ODEC reporting (read / update) · investment planning
templates (author) · ContiTech shared-services interface (consult).

Reference: **ProView Support Process** (incident management, Hannover et al.) as the
support/handover reference.

## Autonomy

**May** — read the project tracker and roadmaps; draft kick-off agendas, requirement
specs and status reports; assemble ODEC progress/impact reporting; flag blocked projects.
**May not** — commit investment or allocate resources; approve acceptance; deploy to
production; make ContiTech licensing commitments.
**Guardrails** — never sign off acceptance; never invent progress or impact figures;
respect Cyber Security sign-off and ContiTech interface compatibility.

## Metrics for this lane

| Metric | Source | Target | Intervene from |
|---|---|---|---|
| Integration projects to acceptance | ⟨project tracker — to collect⟩ | ⟨to confirm⟩ | acceptance slippage |
| Equipment integration progress | ODEC report · Equipment Integration | on plan | behind plan |
| Applications progress | ODEC report · Applications | on plan | behind plan |
| Use-case impact | ODEC report · Use Cases (Impact) | ⟨to confirm⟩ | impact below plan |
| On-time delivery | ⟨tracker — to collect⟩ | ⟨to confirm⟩ | delays rising |

## Handover / rework rule

The delivered solution goes to plant operations and to the Use Case Support lane for
adoption. It returns for rework if acceptance fails, or if the use case is not integrated
into daily operations.
