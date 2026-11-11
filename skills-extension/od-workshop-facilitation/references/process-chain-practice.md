---
type: Skill Reference
title: Process chain practice
description: How workshops are prepared and run as a stage in the AI-driven chain - choosing by trigger, workshop order, preparation checklists, in-room practices, utilization session, legacy-application pattern, output and handoff contract, pitfalls and agent operating notes.
resource: ../SKILL.md
status: draft
tags: [use-case-support-service, practice, workshop, process-chain]
---
# Process-chain practice - workshops

Adds to `SKILL.md` and `workshop-formats.md`; the standard agenda, audience matrix and summary skeleton are not
repeated. `PROPOSAL` marks synthesis that no deck states.

## Where it sits

Step **21** (Define and diagnose: run the workshop) and step **31** (Requirements, Lane 3 front-end). Receives
the intake record (`od-use-case-intake-triage`) and the plant file; hands demand rows to `od-use-case-definition`
and follow-ups to the owning skills.

## 1 · Method in practice

**A workshop is one stage in a repeatable chain:** collect plant demand, pre-evaluate, assess tools, assess
machine demand, staff the plant team in the room, investigate savings and set priority locally, schedule
development phases centrally. Every summary ends with the same split: **local next steps** and **central next
steps**, each with a target window.

**Choose the intent, then the format, by the trigger and not by habit.** Three intents: (a) definition (find
demand), (b) machine or equipment integration (connect machines, often inside the same visit), (c) utilization
(make existing use cases used). Format variants seen: classic multi-day definition; definition at the start of a
rollout project with the second day creating the project plan; definition with a third-party system added;
remote or virtual tour when the site cannot be visited; savings workshop (calculation methods, then defined
sprint projects, then project-plan alignment); site-visit style for a region (visit, use-case gathering, IT
visit for data-feed access, project planning); multi-plant sessions (one mandatory shared first day, then
plant-specific days, a remote plant may join day one online).

**Order is a decision.** Machine-integration workshop first when connectivity is missing; use-case workshop
first when machines are connected; combined formats alternate presenters (use-case lead, machine-integration
lead). `<to confirm>`: speaker notes say "plant dependent" while some agendas fix an order, and one agenda
teaches tools before any machine is connected; ask the OD lead and write the reason for the order into the pre-read.

**Preparation, the plant file.** Use-case list, tool-availability table, machine list with connectivity status,
and for an integration workshop the equipment configuration list with technical interfaces. Preparation checklist
for the IT side of an equipment-integration workshop: access to jump hosts and servers (internal and external
support), firewall rules in place, platform apps running, physical access to all edge devices including unmounted
ones, a priority list with best starting point and best stopping point. Typical open topics: operating system,
admin rights and support gaps for GPU or vision PCs. Attendees of a hands-on integration day: project manager,
machine-integration lead, IT, vendor or integrator; Production and Quality are not needed.

**In the room.**
- Parallel tracks are allowed (tour and development slot; tool demo with management in parallel to hands-on; an
  IT or tool-shop slot on industrial-PC usage).
- A "Go Gemba" walk with Production, Engineering and OPEX collects better than a room session.
- Plant tour: production, quality, machine-integration lead, project manager; optional maintenance and process
  engineering. Minor topics (custom connectors for SCADA, PLC or proprietary systems) are collected on the side.
- A block for "open points, obstacles and pain points", split into machine integration versus use-case development.
- Interactive session alternative to a lecture: walk one real plant example through the six creation steps
  (machine integration, data availability, data standardization, data integration, dashboard creation, use-case
  utilization) ending with a live demo "overview to in-depth". Step six is explicit: utilization produces the
  benefit; savings go into the savings cycle; requirements for the next iteration are defined.
- Requirements mini-method (about half an hour, plenary): rotating brainstorm across a few teams in short
  rounds with a cap on ideas per round, then dot-rating with a cap per person; share the result afterwards.
- Machine integration can happen **during** the workshop: connect machines, deploy and demo a first use case
  live, list the remaining machines with their blocker (vendor to order, hand-over to be issued, hand-over to be
  approved locally). Open item afterwards: tag selection for all machines.
- Low-cost connection pattern to propose, not commit: reuse existing infrastructure; address translation on a
  switch or edge device so PLC and HMI programs stay unchanged; trial one low-cost device on one machine before
  ordering more.
- An integration workshop can include a formal project-closure item, a lessons-learned slot ("what can we do
  better next time") and a building-management side track (list applications, priority by operational impact and
  energy-saving potential, interface and documentation status; market solution versus own bus decided later).

**Utilization session** (integration workshops, and as a recurring check). Fill a utilization table per use case:
name, who uses it (team), related process or meeting, utilization method in a few sentences **including the
initial state without digital support**, utilization rate (daily / weekly / monthly / on demand / never),
impact (low / medium / high), plant-management relevant yes/no. Ask: who uses it, how often, which actions
follow, what would make people use it. Also record the improvement list with its source role, and who attests
value (OPEX plus plant ME).

**Legacy-application workshop pattern** (non-standard case; hands on to `od-requirements-breakdown`, section on
legacy assessment, and `od-system-fit-check`): two-day format of use cases of the legacy application (function
inventory per component), architecture components with focus on interfaces, impact analysis per use case,
as-is / to-be status of cyber security, service bus, recipe management and MES, wrap-up with follow-up meeting.
Participants: plant ME, plant process or production, the application's original software owner, OD; supplier
experts external. Capture requirement statements verbatim from the plant. The legacy functions become a use-case
list of what must be preserved; aim at parallel functionality, not a one-to-one replacement.
`PROPOSAL`: make "continue as-is" a mandatory baseline scenario in every legacy decision package.

## 2 · Decision rules

- **Plant tier** decides how much central workshop capacity a plant gets (first mover versus fast follower; see
  `od-use-case-intake-triage`), never whether its demand is legitimate.
- **Ranking of the collected list:** savings first (value, ROI); generalization potential and effort are secondary
  criteria; dependency order is the tie-breaker; custom use cases may need extra budget.
- **Tool recommendation** only against a named defined use case; a recommendation with no use case behind it is
  not made. Savings carry a basis label (calculated / estimated / none); a savings sum with no shown basis does not
  leave the room.
- **Not in the room:** machine connection, investment, external connection (other decisions, other gates).
- **For rollout plants add** to the summary: rollout team staffed, IT and OT assessments scheduled as separate
  meetings, kick-off date fixed, a standing rhythm (short regular team meeting, planner board, steering board),
  machine list finalized for the capital request, calculation and presentation templates for the capital request.
- **Accept a dashboard only after reconciling** it with the paper process; run one deep dive with production
  and one with engineering.

## 3 · Handoff contract

**Receives:** intake record; plant file with read dates; list of priority machines; attendee list by role.

**Hands on, per demand row:** plant, process group, capability, moment of use, owner role, savings-basis label,
tool dependency, machine dependency. Routing: use case to `od-use-case-definition`; machine need to
`od-equipment-integration`; savings to `od-benefit-calculation`; ranking to `od-portfolio-and-savings-analysis`;
standard candidates to `od-use-case-standardization`; IT demand to `it-demand-package`; ad-hoc issue to
`od-first-aid-kit`. Output set: use-case list by production area, process, use case (split per step and purpose,
naming convention plant-material-process-use case); tool availability with recommendation; savings pre-evaluation
(usually still open); local and central next steps.

## 4 · Pitfalls and lessons

- Savings calculated in the workshop stall the agenda; book it as a follow-up with an owner and a date.
- Deployed is not used: many scaled cases show no saving. Pivot the utilization session to "what is necessary
  for the use cases to be utilized?"; delivered count is not an impact measure.
- More integrated machines does not mean more savings: without pull from Production and a cross-functional team
  there is none.
- Human-dependent automation caps what a dashboard can show; check for organisational loss before technology.
- Recorded outcomes are not traced: nobody knows which workshop use cases went live. Close this by filtering the
  live list on workshop source.
- Do not let the testimonial or advert recording become a workshop deliverable; keep it optional.

## 5 · Questions to ask / definition of done

Before: what is the trigger, which intent, which order and why, who is required on which day, is the equipment
list and IT access in place, is a wait state (Cyber Security, investment) in the way.
After (adds to `SKILL.md`): each tool recommendation traces to a named use case; rollout team named and kick-off
date set when a rollout follows; utilization table started for every use case already live; improvement list
captured with its source role.

## 6 · AI agent operating notes

- **Can do:** draft the agenda from the trigger table and the audience matrix; draft the pre-read from the
  plant's tool-availability status with the canvas pre-filled from a library match; check the IT-side
  preparation checklist against what the plant reports; after the workshop turn the capture sheet into the
  follow-up list, the local / central split and the summary skeleton; draft utilization-table rows from call
  notes (`PROPOSAL`: from dashboard usage logs, no deck shows that source).
- **Required inputs:** intake record, plant file with dates, capture sheet.
- **Human gates:** the DBVE chooses format and order and facilitates; the Plant ME confirms priority; OPEX / ME
  attest value; anything that commits budget or a connection stays with its own gate.
- **Evidence to cite:** use-case-list row, library entry, tool-status source and date.
- **Hand over:** the routed items of section 3, each with an owner role and a date or "open".
