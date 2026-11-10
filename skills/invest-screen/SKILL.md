---
name: invest-screen
description: >-
  Two gates in one skill. Intake fit: catch the request that sounds like a normal dashboard or
  integration ask but quietly needs a system outside the lean footprint (MES, EMS, a heavier MIL,
  Recipe Management or Data Science Factory) and resolve it to fits, redesign or escalate, checked
  against this plant's real tool availability. Lane 3 tool-decision gate (the department's mandatory
  investment-screening): run the software and IT-footprint hard gate, then route the demand to 3a.1
  reuse, 3a.2 self-develop, 3a.3 external build (guided buy), 3a.4 integrate a foreign app, or 3b new
  connector, with a Go / PoC-first / Reduce-complexity / Hold / Blocked verdict; includes the solution
  design recommendation for application questions (formerly od-application-consulting). Use at intake,
  during requirements breakdown, at Lane 3 step 32, whenever someone asks make, buy, integrate or connect,
  or when a purchase ships a PC, software, licence or endpoint.
license: MIT
metadata:
  id: invest-screen
  tier: practice
  lane: all
  new_state_lane: "Intake (i1), Lane 3 front-end (32)"
  new_state_step: "Classify the demand into exactly one lane; Tool-decision / IT-footprint gate (make, buy, integrate or connect)"
  department_names: ["invest-screen", "investment-screening", "investment-checking"]
  owner_role: Digital-Business-Value-Engineer (DBVE) / IIoT Interface & Automation Engineer (IIAE), whichever lane the request entered through
  authority_level: recommend — flags the fit risk and proposes a redesign or an escalation; never approves a system change or a rollout exception itself
  status: stable
  origin: derived
  sources_read: 2026-11-10
  requires: [dept-os]
  composes: [od-decision-routing, od-use-case-solution-evaluation, it-demand-package, deploy-appstore, mi-connector, funnel-prototype]
  derived_from:
    - personal vault, Work-OpsDigit-Knowledge/_knowledge/OperationsDigitalization-Department/00-core/02-strategy.md (the non-bets, bets and kill criteria, verbatim), read 2026-10-23.
    - personal vault, Work-OpsDigit-Knowledge/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md (P-02's own scope statement and deployment-reality framing), read 2026-10-23.
    - personal vault, Work-OpsDigit-Knowledge/Split Slides/10-Workshops--2025-01-12-1.1-OnePager-System_Overview*.pptx (the per-tool is/is-not boundary cards, integration-recommended-if criteria, real cost estimates), read 2026-10-22.
    - personal vault, Work-OpsDigit-Knowledge/Split Slides/10-Workshops--2023_06_29_Summary_SanLuisPotosi_SmartFactory_UseCase_Definition_Workshop*.pptx, --2024_04_04_Summary_Subotica_SmartFactory_UseCase_Definition_Workshop*.pptx, --2024_07_04_Summary_Timisoara_SmartFactory_UseCase_Definition_Workshop*.pptx (three real per-plant Smart Factory Tools Availability snapshots), read 2026-10-22. Resolves PHASE1-ELICITATION.md topic 5 (non-bet system-fit judgement) and builds the skill the department's own Wave-1 plan named but never built (P-02, `od-p-system-fit-check`).
    - Work vault (Work-OpsDigit-Knowledge), Graph/Tools (rollout history and tables, use of the tool, archive-evidence blocks), Graph/Plants rollout blocks and Graph/Legacy Applications, read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Slide Index (deck OD Initiative - CS Legacy Application As_Is_Analysis) and ODEC Facts staging notes (Department KPIs and Roadmap Status), AI-extracted and unverified, read 2026-11-05
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT (README, lane 1-3), read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/20-lanes-newstate-DRAFT/Transcripts/2026-09-11_OD-IT-alignment_meeting-notes.txt, read 2026-11-10"
    - "Work vault, OD Department Knowledge/OD-instance/2026-09-02_OD_Investment_Screen.md, read 2026-11-10"
  okf:
    type: Agent Skill
    title: System fit check
    tags: [practice, all]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-10-23T00:00:00Z }
---

# System fit check

Read `dept-os` first. This is the cross-cutting check `od-use-case-intake-triage` and
`funnel-requirements` both call before a request is scoped any further: **does this
quietly need a system outside the lean footprint?**

A request rarely names a system. It says "we need live cross-process scheduling with full
order genealogy," which is MES in different words — and by the time a use case is already
scoped around it, redesigning is a much bigger conversation than catching it at intake.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/tool-decision-gate.md`](references/tool-decision-gate.md) | The Lane 3 gate: IT-footprint hard gate, route to 3a.1-3a.4 or 3b, OD x IT sourcing principles, verdict words |
| [`references/od-application-consulting/procedure.md`](references/od-application-consulting/procedure.md) | Absorbed: the solution design recommendation for an application question (formerly `od-application-consulting`) |
| [`references/non-bets.md`](references/non-bets.md) | The department's own choice architecture — what is deliberately not pursued, the trade-offs behind it, and the kill criteria attached to what *is* pursued |
| [`references/tool-boundaries.md`](references/tool-boundaries.md) | What each lightweight tool (QFPR, MDA/PDA, MIL, Camline, WiriTec) is and is not for, in the department's own words — the actual tell, per tool |
| [`references/deployment-reality.md`](references/deployment-reality.md) | Why the same tool catalogue is in different states at different plants, and how to read a plant's own tool-availability table — check this plant, not the estate average |
| [`references/plant-tool-availability.md`](references/plant-tool-availability.md) | How to read the live Tool Overview for a plant (status codes, what an empty cell means), how to count use cases naming a tool, and how to handle disagreement with workshop tables. Guidance only, no figures |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | How the check runs as chain step i1 / 32: boundary and "recommended if" lines as intake classifiers, demand shapes, the operations-concept precondition, handoff contract, agent notes |
| [`references/maturity-profile-signals.md`](references/maturity-profile-signals.md) | Which maturity-model levels on a requested or existing system act as fit-check signals (MES shape, edge need, reporting before AI, integration cost); profile from `od-use-case-solution-evaluation`, evidence next to the boundary line, never a verdict |
| [`references/legacy-applications-landscape.md`](references/legacy-applications-landscape.md) | How to read the Legacy Application List (fields, blank-cell traps) and how to spot the plant that already runs a parallel MES, SCADA or dashboard system. Guidance only, no figures |

## The check — three steps

### 1 · State the need, not the request

Restate what the request is actually asking the data or process layer to do, independent of
whatever system or dashboard name the requester used. This is the step most often skipped,
and skipping it is why a request "sounds like a normal ask" in the first place — the
requester's own framing is doing the disguising, not lying.

### 2 · Walk the tool boundaries in order

Check the need against each lightweight tool's own **"is not"** line
(`references/tool-boundaries.md`): QFPR (quality feedback, not KPI calculation or master
data), MDA/PDA (machine/asset data, the "lightweight MES" for automation data), the
Manufacturing Image Library (images and DL inspection, not process-parameter storage or
model training itself), Recipe Management / Camline (recipe master data, not live value
storage or alerting), the Energy Management System (energy data only).

Test each tool's "integration recommended if" trigger as well: it says when the tool earns a
rollout, and the tool's cost class (never a number) goes on the record.

**If none of them cover it, the need is MES- or EMS-shaped.** That is the actual tell this
skill resolves to — not a vibe, a specific boundary line the need crosses.

### 3 · Check this plant's actual availability, not the estate average

The same tool can be "not necessary" at one plant and "needed for multiple use cases" at
another at the same time — see `references/deployment-reality.md`. A tool being the
right answer in principle and a tool being deployed *here* are two different facts; check
both before concluding anything.

## Verdict and next step

| Verdict | When | Next |
|---|---|---|
| **Fits the lean footprint** | A covering tool exists and is available at this plant | Hand back to the calling skill — no further action |
| **Redesign onto a lighter tool** | The need is covered by a lighter tool than the request assumed | Re-scope the request onto that tool before defining it any further |
| **Escalate as exception** | The need is genuinely MES/EMS-shaped, or needs a tool not yet deployed here with no substitute | `od-decision-routing`'s "Tool/system rollout" decision row — the OD lead decides in tandem with the IT-responsible role of the business side |

Fill [`assets/system-fit-check.md`](assets/system-fit-check.md) as the check happens — five
minutes, not a workshop. When the plant may already run a legacy application or a tool that covers
the need, add [`assets/existing-system-worksheet.md`](assets/existing-system-worksheet.md). A request that resolves to "escalate" and also has a large,
multi-area capability gap in `od-use-case-solution-evaluation`'s own gap analysis is the
same finding seen from two angles; check whether that evaluation has already been run
before escalating twice for one request.

## Lane 3 tool-decision gate (step 32)

In Lane 3 this skill is the department's mandatory **tool-decision / IT-footprint gate**
(`investment-screening`). No demand leaves the front-end without it. Run the intake check above first,
then [`references/tool-decision-gate.md`](references/tool-decision-gate.md):

1. **Software and IT-footprint hard gate.** Shipped PC or controller, framework, exposed endpoints,
   licence owner, hosting, data ownership, standard interface, Cyber Security status. Any open point
   blocks.
2. **Route** to 3a.1 reuse, 3a.2 self-develop, 3a.3 external build (guided buy), 3a.4 integrate a
   foreign app, or 3b new connector, using the OD x IT sourcing principles (solution-design stage
   first; build in-house only where the know-how is manufacturing's own; prefer cloud services, open
   source and the CMO deployment path; judge external builds on multi-year TCO).
3. **Verdict** in the department's words: Go, PoC-first, Reduce-complexity, Hold, Blocked, Engage.

For an application question that needs a full solution design recommendation (which existing tool or
app covers it, how the data reaches it, who runs it afterwards), run the absorbed procedure in
[`references/od-application-consulting/procedure.md`](references/od-application-consulting/procedure.md).
The route goes to `it-demand-package` (3a.3, 3a.4), `deploy-appstore` (3a.1, 3a.2) or
`mi-connector` (3b).

## A live discrepancy this skill surfaces rather than hides

`references/non-bets.md` records the strategy position on EMS rollout. `references/tool-boundaries.md`'s
own tool catalogue can describe WiriTec (the EMS) as rolled out and in active use. When the written
position and the catalogue disagree, **confirm current status before citing
either version** — this is exactly the kind of policy-vs-practice drift the check exists to
catch, including in its own source material. Do not silently pick one.

## Guardrails

- **Never conclude "MES-shaped" from a feeling.** Name the specific tool boundary the need
  crosses; if you cannot name one, the check is not finished.
- **Never treat an available tool as not available, or vice versa, from the estate average.**
  Check the specific plant.
- **Never return "fits" for a tool nobody runs.** A tool with no named operations owner and
  support level is a service gap, not a fit: escalate (`references/process-chain-practice.md`).
- **Never let this check itself approve a rollout exception.** It recommends; the "Tool /
  system rollout" gate in `od-decision-routing` decides.
- **Never silently resolve the EMS discrepancy above by picking the version that is more
  convenient for the request in front of you.** Ask.

## Definition of done

The actual need is stated independent of the request's own framing; each lightweight tool's
boundary has been checked against it with a stated reason, not a guess; this plant's actual
availability has been checked, dated; and the verdict is one of the three above, with a
named next step. In Lane 3, additionally: the IT-footprint gate has no open point (or the verdict is
Blocked), and the demand carries one route (3a.1-3a.4 or 3b) with its next skill.
