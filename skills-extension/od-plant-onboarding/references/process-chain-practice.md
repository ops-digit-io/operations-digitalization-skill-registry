---
type: Skill Reference
title: Process chain practice
description: How a plant joins the chain in practice - first mover versus fast follower tiering, the plant visit, readiness signals from good and poor plants, wave and migration mechanics, and what an agent may draft. Pattern only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice

Distilled from the Operations Digitalization slide decks, abstracted into process guidance. No company figures, no plant
statuses. `PROPOSAL` marks a synthesis; `<...>` is unknown. It adds to [`plant-landscape.md`](plant-landscape.md).

## 1. Method in practice

**Plant visit for a new plant.** A short visit (about one day): the cluster manager's reporting expectation, the as-is list of
what is already connected, the plant's priority process cluster, then plan the machine integration. A longer definition visit
adds tool trainings, hands-on use-case creation with key users, a machine-integration day and a wrap-up to the whole team,
management and neighbouring departments. Pick the workshop order by the trigger: machine-integration first when connectivity
is missing, use-case first when machines are connected (see `od-workshop-facilitation`). A remote or virtual tour is an
accepted variant when the site cannot be visited.

**Fix these in the room when a rollout follows:** a rollout team staffed, the kick-off date, IT and OT assessments as
*separate* meetings, a standing rhythm (a short bi-weekly team meeting, a planner board, a steering board), the machine list
finalised for the capital request, and calculation and presentation templates for the request.

**Four onboarding tracks** (generic roadmap by year): infrastructure (bus and edge platform, data acquisition stages),
people (key users assigned or hired), organisation (workshops, use-case staffing, one responsible person per location),
applications. Count accomplished milestones, not intentions.

**Roadmap.** A regional roadmap is drafted centrally and approved in the plant-engineering roadmap workshop. Inputs: carry-over
projects, new plant requests with standardisation value, central initiatives, system and use-case rollouts. Plants state
requests proactively. Template fields: machine-integration wave, use-case deployment, system deployment, frame conditions
(security screening, admin use cases, energy data), data lifecycle, standard data models, know-how management, analytics and AI;
the workload (one responsible person per location) and responsibility columns.

**Wave mechanics.** Per wave and plant: kick-off, then a traffic-light status (red / yellow / green, one scale per round; "input collected", "delayed" or "at risk" only as reason text)
before the equipment request is uploaded; the weekly micro-process (call the local OT expert, prepare the request, upload, close-loop until
approval). First mover waves ahead of fast follower waves when capacity is short (see section 2).

## 2. Decision rules

| Tier | Criteria | Support |
|---|---|---|
| **First mover** | High estimated value; regions, segments and technologies covered; capacity and knowledge in the plant; integration synergies; a dedicated, staffed key user | Central support and review first |
| **Fast follower** | Anything else | Central support only when capacity allows; locally driven; limited, resource-adjusted funding; roadmap from local assessment |

- Tier decides *capacity*, not *eligibility*. Use the department definition of first mover; a sector-level definition is
  background. Eligibility follows request order; central capacity goes first to first-mover plants that are staffed.
- **Scale known machine types.** At most one unknown machine type per new deployment; document the process per controller
  type; create an integration standard. Starting with the hardest machines first burned reputation and killed the local project.
- **Do not skip the plant-readiness signals** (below) because the plant "looks like the last one".
- **Layout stability** is checked before committing a wave; repeatedly relocated machines delay integration.
- **Connect more machines only on capable infrastructure.** More connected machines does not mean more savings; production
  pull and a cross-functional team do.
- **First action on the plant's use-case list:** evaluate the remaining use cases that relate to the machines being
  integrated, and re-evaluate stale or low-value entries.
- **Customer audits** are a hard external deadline that outranks internal plans; do not take a customer-facing line down
  before an audit.

### Readiness signals (good versus poor plant)
- Good: production proactively drives ideas and asks for blueprints; requirements are formalised with OD in dedicated
  meetings; savings are calculated together with controlling; savings are pushed before the next wave; participation in
  community calls.
- Poor: a single engineer "only responsible for the technical part"; production demand unknown; standards ignored; "we do not
  know how to calculate savings"; low participation. Equal integration with unequal savings points here, not to technology.

### Migration or cutover per location (when a platform or server moves)
1. Scope per location: network, certificates, interfaces, directory integration, licences, assessed with the application owner.
2. Time plan across locations; announce ahead; execute per timeline.
3. Per-location checklist file with a RAG; a location-specific meeting with the key users after cutover to verify every item.
4. An outage window per location for reconfiguring edge devices; announce that process data and dashboards are unavailable.
5. Check runtime licence models before moving a virtual machine (bound to one machine; keep the key to reset the state);
   confirm DNS, certificates for new names and user access carry-over.
6. Refresh the per-application service concept (change and incident process, connection matrix, roles, risk and gap).
A "new installation" location without a legacy baseline is the hardest case. Separation from a former parent: track carry-over
of service documentation, contracts and processes as items with owners.

## 3. Handoff contract

| Receives (from) | Hands on (to) |
|---|---|
| Plant record, machine list, tier (`od-sharepoint-list-export`) | Entry stage and profile; first-mover or fast-follower flag in the tracker |
| Intake decisions (`od-use-case-intake-triage`) | Lane assignment per demand |
| Roadmap workshop output | Regional roadmap entry; plant numbers in `od-scorecard-reporting`; risks to `od-risk-watch` |

## 4. Pitfalls and lessons

- At the start only a few engineers believed in the system: build trust step by step; do not promise breadth first.
- Connectivity budget approved but the plant lacks people; a central priority without a staffed key user.
- Wireless connectivity for small or moved assembly equipment: prove with a few machines first and keep the discussion simple.
- Preconditions missing before a migration (registry, source-code host, firewall changes, approvals): the signal is often
  missing ownership, not a technical puzzle. Ask who is responsible for the connection and what the other sites do.

## 5. Questions to ask / definition of done

- Is there a staffed key user? Is the machine list current (response speed is bounded by it)? Which machine types are known?
  Is the layout stable? Which customer deadline applies?
- Done when: tier recorded with the criteria that set it; every stage has its artefact or a reason; the plant is in the department's reporting routines
  rhythm; a plant-side owner per lane is named as a role.

## 6. AI agent operating notes

- **Can do:** draft the tier assessment from the criteria with the fact used per criterion; pre-fill the roadmap slide;
  build the per-location migration checklist and RAG table; flag silent threads and unowned items.
- **Required inputs:** plant record, machine list read date, roadmap workshop notes, staffing of the key user.
- **Human gate:** the tier decision, the wave order, any commitment of central capacity.
- **Evidence to cite:** record and read date, the criterion and the fact behind it.
- **Hands over:** the tracker to the plant-side owner; the roadmap draft to the workshop.
