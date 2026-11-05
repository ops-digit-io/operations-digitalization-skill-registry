---
name: od-workshop-facilitation
description: >-
  Prepare, run and close an OD Use Case Definition Workshop or Use Case Integration Workshop at a plant - choose the format, set purpose and audience, send a pre-read, run the days from OD's standard agenda, capture demand, savings pre-evaluation, tool and machine needs in one template, and turn the output into a follow-up list with owners. Drafts all materials; the DBVE facilitates and the Plant ME owns the plant side. Use when a definition or integration workshop is requested or scheduled, when a plant is onboarded or a new demand wave starts, when a use case is ready for integration, or when workshop output exists but no follow-up list.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
allowed-tools: Read Grep Glob
metadata:
  id: od-workshop-facilitation
  tier: practice
  lane: use-case-support-service
  new_state_lane: Lane 2 (definition), Lane 3 front-end
  new_state_step: "Define and diagnose: run the workshop"
  owner_role: human:jakob.gabriel
  authority_level: draft
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-use-case-definition, od-use-case-intake-triage, od-use-case-prioritization, od-benefit-calculation, od-requirements-breakdown, od-data-availability-check, od-system-fit-check, od-use-case-standardization, od-equipment-integration, od-cybersec-gate, od-first-aid-kit]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/use-case-support-service/tasks.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/use-case-support-service/playbook.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/use-case-support-service/agent-brief.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/05-intake.md
    - Work vault (Work-OpsDigit-Knowledge), Slide Index and Split Slides of 03-AMT_MI_Standard_Agenda_Use_Case_Workshop (AMT_MI_UC-Standard_Agenda slides 2 to 5, 55 to 96; Workshop_Summary; OESL Standard Agenda with Interactive Session; Use Case Canvas and Use Case Utilization templates; Creation Process intro), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Slide Index of 10-Workshops (Carei 2024 agenda, canvas and summary; Carei 2025 and Dolne Vestenice 2025 integration workshops; Korbach 2025 equipment integration workshop agenda and summary; Mako and Vac 2023 seven-day agenda), read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Slide Index of 01-Smart_Factory_Use_Case_Support_Service_Workflow, read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Case Groups overview (white space and delivered-without-saving case groups), read 2026-11-05
    - Skill od-use-case-definition, SKILL.md and assets (questionnaire and protocol that run inside a definition workshop)
    - Skill od-use-case-intake-triage, refusal playbook (tool-availability check before accepting a use case)
  okf:
    type: Agent Skill
    title: Workshop facilitation
    tags: [use-case-support-service, practice, workshop]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Workshop facilitation

Read `od-context` first. The lane's recurring tasks (`tasks.md`) include two workshops: the **Use
Case Definition Workshop** (trigger: plant onboarding or a new demand wave; template: "Standard
Agenda — Use Case Workshop" on SharePoint) and the **Use Case Integration Workshop** (trigger: use
case ready for integration; template: "Use Case Integration Workshop agenda"). Both are intake
channels (`05-intake.md`: "plant use-case demand collected via Use Case Definition/Integration
Workshops"). This skill produces the four things the plan asks for: agenda, pre-read, capture
template, follow-up list. Authority: **draft**; the DBVE facilitates, the Plant ME owns the plant
side, nothing is committed in the room (investment, equipment integration, external connection are
other decisions).

## The references and assets

| File | Use it for |
|---|---|
| [`references/workshop-formats.md`](references/workshop-formats.md) | The formats OD has actually run (definition, integration, equipment integration, machine integration, savings), their purpose lines, days, audience and typical outputs, and where to find the workshops on record |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Chain practice: intent and order decision, IT-side preparation checklist, in-room practices, utilization table, legacy-application pattern, handoff contract, agent notes |
| [`assets/workshop-agenda-and-preread.md`](assets/workshop-agenda-and-preread.md) | Agenda skeletons per format and the pre-read checklist to send |
| [`assets/workshop-capture-template.md`](assets/workshop-capture-template.md) | The sheet filled during the workshop: demand list, canvas, savings pre-evaluation, tool and machine assessment, decisions |
| [`assets/workshop-follow-up-list.md`](assets/workshop-follow-up-list.md) | The follow-up list and summary skeleton to close the workshop |

## Procedure

### A · Before (about the weeks ahead; ⟨lead time for scheduling — not in the sources⟩)

1. **Pick the format** from [`references/workshop-formats.md`](references/workshop-formats.md). Rule
   from the decks' speaker notes: which comes first, a Machine Integration workshop or a Use Case
   workshop, depends on the plant ("Dependent on which Workshop format is first"). If the plant has
   an ad-hoc process issue and no use case, it is not a workshop; use `od-first-aid-kit`. Write the
   reason for the chosen order into the pre-read (machine-integration first when connectivity is
   missing, use-case first when machines are connected; `<to confirm>` with the OD lead where an
   agenda fixes an order).
2. **State purpose and timeframe** in the style of OD's own agenda slide: a short purpose list
   (what is defined, what status is followed up, what is prioritized, what project it starts) and a
   preferred window agreed with the plant. See the plant-agenda example in the formats reference.
3. **Fix the audience.** The standard agenda marks each item Required or Recommended for these
   roles: Project Manager MSB, Machine Integration Lead, Quality, Production, CBS, IT (⟨what "CBS"
   stands for — the deck does not spell it out⟩). Open slide 2 of the Standard Agenda deck for the
   per-item matrix. Add the Plant ME, the plant owner of any use case already on the list, OPEX and
   Engineering for utilization sessions.
4. **Prepare the plant file.** Existing use case list for the plant, case groups where the plant is
   white space or has Delivered use cases (`od-use-case-prioritization`, evidence baselines), tool
   availability table for the plant (which of IIoT Edge, MSB/MQTT broker, rule engine, MES, QFPR,
   recipe management, image library, Data Science Factory are deployed), machine list and
   connectivity status. The tool-availability check matters: a tool demoed at a plant is not the
   same as a use case being in scope there (`od-use-case-intake-triage`, refusal playbook).
5. **Send the pre-read** from [`assets/workshop-agenda-and-preread.md`](assets/workshop-agenda-and-preread.md):
   agenda, purpose, the blank Use Case Canvas, the savings pre-evaluation template and its
   examples, the utilization template, the list of priority machines the plant should have ready,
   and who must be present on which day.
6. **Check the wait states** you must not promise around: Cyber Security sign-off for any external
   machine connection (`od-cybersec-gate`), investment approval (`playbook.md`).

### B · During

7. **Day structure for a definition workshop** (OD Standard Agenda; check the deck for the current version):
   Day 1 introduction (OD and its service lines, tools, use case creation process, use case
   library, analytics use case library); Day 2 use case definition (plant tour with focus on
   priority machines; collection of use case demand); Day 3 detail evaluation (pre-evaluation of
   found use cases for savings; assessment of Smart Factory tools needed; assessment of machine
   integration demands). Trim days the plant already knows; the earlier variant with an interactive
   session uses the six creation steps (machine integration, data availability, data
   standardization, data integration, dashboard creation, use case utilization).
8. **Capture live, in one sheet** ([`assets/workshop-capture-template.md`](assets/workshop-capture-template.md)).
   For each demand run the questions of `od-use-case-definition`'s questionnaire; do not define a
   duplicate of something already logged. Check the library before drafting from a blank page.
9. **Savings: pre-evaluate, do not promise.** Use OD's pre-evaluation template with its examples
   (productivity, quality, maintenance) and mark each figure with its basis (calculated /
   estimated / none); make tool recommendations only against a named use case. Workshops have not
   always produced the number: past summaries carried "Savings Estimation for Use Cases:
   open task" for the use cases collected. Past attempts to fit savings calculation into the
   workshop agenda stalled it (`od-benefit-calculation`, review checklist), so book calculation as a
   follow-up with OD's calculator and fix the date in the room.
10. **Rank lightly.** Classification and priority in the standard agenda: highest generalization
    potential, highest saving potential; custom use cases per plant may need extra budget. Leave the
    full ranking to `od-use-case-prioritization`.
11. **Record disagreement.** If participants describe the same need differently, that is several use
    cases (`od-use-case-definition`); log them separately.

### C · After

12. **Summarize within the follow-up window** (⟨target days — not in the sources⟩) in the shape of
    OD's summary decks: tool availability with recommendation, top three or four use cases by current
    priority per process, next steps split into local and central. Skeleton in
    [`assets/workshop-follow-up-list.md`](assets/workshop-follow-up-list.md).
13. **Route every item**: use case to definition or `od-use-case-intake-triage`; machine need to
    `od-equipment-integration` or the Information Integration lane; savings to
    `od-benefit-calculation`; ranking to `od-use-case-prioritization`; standard candidates to
    `od-use-case-standardization`; ad-hoc issues to `od-first-aid-kit`.
14. **Give each follow-up an owner role and a date, or mark it open.** The sources show open items
    without dates; an item with no owner is not a follow-up.
15. **Ask for utilization feedback at the next visit.** Integration workshops end with a utilization
    session (who uses it, how often, which actions); schedule it.

## Definition of done

Purpose, audience and timeframe were agreed with the plant; the pre-read went out; the capture
sheet is filled and legible to someone who was not present; every demand is logged against the plant
roadmap or returned with a reason; the follow-up list has owner roles, dates or explicit
"open"; the summary reached the Plant ME.

## What is still open

- ⟨Official integration workshop agenda template⟩ — the SharePoint template named in `tasks.md` was
  not available; the skeleton in `assets/` is distilled from past agendas. Supplier: DBVE.
- ⟨Lead times⟩ for scheduling, pre-read and summary — not set anywhere read. Supplier: OD lead.
- ⟨Attendance matrix⟩ per agenda item — in the deck's slide 2 table; the text extraction loses empty
  cells, so it is not reproduced here.
- ⟨Recorded outcomes⟩ of past workshops (which use cases went live afterwards) — not traced.
  Supplier: DBVE, by filtering the live use case list on workshop source.

## Do not

- Do not leave the room with savings figures that have no basis; record them as pre-evaluation.
- Do not accept a use case on a tool that is not available at the plant without recording the
  rollout dependency.
- Do not commit machine integration, investment or an external connection in the room.
- Do not define a duplicate of a logged use case.
- Do not name individuals in the record; use roles. Do not paste credentials, hostnames or addresses.
