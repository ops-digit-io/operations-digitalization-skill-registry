---
name: od-system-fit-check
description: >-
  Catch the request that sounds like a normal dashboard or integration ask but quietly
  needs a system outside the lean footprint — MES, EMS, or a heavier read on MIL, Recipe
  Management or the Data Science Factory than the lightweight tools (QFPR, MDA/PDA) cover.
  Checks a stated need against each tool's own "is / is not" boundary, checks this specific
  plant's actual tool availability (not the estate average), and resolves to one of three
  verdicts: fits the lean footprint, redesign onto a lighter tool, or escalate as an
  exception. Use during intake (`od-use-case-intake-triage`) or requirements breakdown
  (`od-requirements-breakdown`), whichever catches the request first — never after a use
  case has already been scoped around the heavier system.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-system-fit-check
  tier: practice
  lane: all
  owner_role: Digital-Business-Value-Engineer (DBVE) / IIoT Interface & Automation Engineer (IIAE), whichever lane the request entered through
  authority_level: recommend — flags the fit risk and proposes a redesign or an escalation; never approves a system change or a rollout exception itself
  status: stable
  origin: derived
  sources_read: 2026-10-23
  requires: [od-context]
  composes: [od-decision-routing, od-use-case-solution-evaluation]
  derived_from:
    - personal vault, Work-OpsDigit-Knowledge/_knowledge/OperationsDigitalization-Department/00-core/02-strategy.md (the non-bets, bets and kill criteria, verbatim), read 2026-10-23.
    - personal vault, Work-OpsDigit-Knowledge/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md (P-02's own scope statement and deployment-reality framing), read 2026-10-23.
    - personal vault, Work-OpsDigit-Knowledge/Split Slides/10-Workshops--2025-01-12-1.1-OnePager-System_Overview*.pptx (the per-tool is/is-not boundary cards, integration-recommended-if criteria, real cost estimates), read 2026-10-22.
    - personal vault, Work-OpsDigit-Knowledge/Split Slides/10-Workshops--2023_06_29_Summary_SanLuisPotosi_SmartFactory_UseCase_Definition_Workshop*.pptx, --2024_04_04_Summary_Subotica_SmartFactory_UseCase_Definition_Workshop*.pptx, --2024_07_04_Summary_Timisoara_SmartFactory_UseCase_Definition_Workshop*.pptx (three real per-plant Smart Factory Tools Availability snapshots), read 2026-10-22. Resolves PHASE1-ELICITATION.md topic 5 (non-bet system-fit judgement) and builds the skill the department's own Wave-1 plan named but never built (P-02, `od-p-system-fit-check`).
  okf:
    type: Agent Skill
    title: System fit check
    tags: [practice, all]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-10-23T00:00:00Z }
---

# System fit check

Read `od-context` first. This is the cross-cutting check `od-use-case-intake-triage` and
`od-requirements-breakdown` both call before a request is scoped any further: **does this
quietly need a system outside the lean footprint?**

A request rarely names a system. It says "we need live cross-process scheduling with full
order genealogy," which is MES in different words — and by the time a use case is already
scoped around it, redesigning is a much bigger conversation than catching it at intake.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/non-bets.md`](references/non-bets.md) | The department's own choice architecture — what is deliberately not pursued, the trade-offs behind it, and the kill criteria attached to what *is* pursued |
| [`references/tool-boundaries.md`](references/tool-boundaries.md) | What each lightweight tool (QFPR, MDA/PDA, MIL, Camline, WiriTec) is and is not for, in the department's own words — the actual tell, per tool |
| [`references/deployment-reality.md`](references/deployment-reality.md) | Three real per-plant snapshots showing the same tool catalogue in three different states — check this plant, not the estate average |

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

**If none of them cover it, the need is MES- or EMS-shaped.** That is the actual tell this
skill resolves to — not a vibe, a specific boundary line the need crosses.

### 3 · Check this plant's actual availability, not the estate average

The same tool is "not necessary" at one plant and "needed for multiple use cases" at
another in the same quarter — see `references/deployment-reality.md`. A tool being the
right answer in principle and a tool being deployed *here* are two different facts; check
both before concluding anything.

## Verdict and next step

| Verdict | When | Next |
|---|---|---|
| **Fits the lean footprint** | A covering tool exists and is available at this plant | Hand back to the calling skill — no further action |
| **Redesign onto a lighter tool** | The need is covered by a lighter tool than the request assumed | Re-scope the request onto that tool before defining it any further |
| **Escalate as exception** | The need is genuinely MES/EMS-shaped, or needs a tool not yet deployed here with no substitute | `od-decision-routing`'s "Tool/system rollout" decision row — note its counterpart is itself still `⟨to confirm⟩`; name the OD lead at minimum |

Fill [`assets/system-fit-check.md`](assets/system-fit-check.md) as the check happens — five
minutes, not a workshop. A request that resolves to "escalate" and also has a large,
multi-area capability gap in `od-use-case-solution-evaluation`'s own gap analysis is the
same finding seen from two angles; check whether that evaluation has already been run
before escalating twice for one request.

## A live discrepancy this skill surfaces rather than hides

`references/non-bets.md` states EMS rollout is stopped. `references/tool-boundaries.md`'s
own source, dated January 2025, records WiriTec (the EMS) as already rolled out to most
locations and names it as an active 2025 initiative. **Confirm current status before citing
either version** — this is exactly the kind of policy-vs-practice drift the check exists to
catch, including in its own source material. Do not silently pick one.

## Guardrails

- **Never conclude "MES-shaped" from a feeling.** Name the specific tool boundary the need
  crosses; if you cannot name one, the check is not finished.
- **Never treat an available tool as not available, or vice versa, from the estate average.**
  Check the specific plant.
- **Never let this check itself approve a rollout exception.** It recommends; the "Tool /
  system rollout" gate in `od-decision-routing` decides.
- **Never silently resolve the EMS discrepancy above by picking the version that is more
  convenient for the request in front of you.** Ask.

## Definition of done

The actual need is stated independent of the request's own framing; each lightweight tool's
boundary has been checked against it with a stated reason, not a guess; this plant's actual
availability has been checked, dated; and the verdict is one of the three above, with a
named next step.
