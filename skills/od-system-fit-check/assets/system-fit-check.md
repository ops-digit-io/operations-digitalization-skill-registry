---
type: Skill Asset
title: System fit check
description: The defined output of the check - the request's actual need stated plainly, which tool boundary it crosses if any, and the redesign-or-escalate verdict - so the result is a reusable record rather than a private judgement call.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [practice, template, protocol]
generated: { by: claude-code/1, at: 2026-10-23T00:00:00Z }
---
# System fit check — ⟨request / use case name⟩

Run once per request, at intake (`od-use-case-intake-triage`) or at requirements breakdown
(`od-requirements-breakdown`) — whichever catches it first. Five minutes, not a workshop.

| | |
|---|---|
| **Request** | ⟨one line: what was asked for⟩ |
| **Plant** | ⟨name⟩ |
| **Checked by / date** | ⟨name⟩ · ⟨date⟩ |
| **Verdict** | ⟨fits the lean footprint · redesign onto ⟨tool⟩ · escalate as exception⟩ |

## 1 · State the actual need, not the request's own words

A request rarely names a system. State what it is actually asking the data/process layer
to do — cross-process scheduling, full order genealogy, live deviation alerting, image-
based inspection, recipe versioning, energy optimization, etc.

## 2 · Check against each tool's own boundary

Walk `references/tool-boundaries.md`'s "is not" lines in order. Stop at the first one the
need crosses.

| Tool | Covers it? | Where it stops (the "is not" line, if it applies) |
|---|---|---|
| QFPR | ⟨yes/no⟩ | |
| MDA/PDA | ⟨yes/no⟩ | |
| Manufacturing Image Library | ⟨yes/no⟩ | |
| Recipe Management (Camline) | ⟨yes/no⟩ | |
| Energy Management System (WiriTec) | ⟨yes/no⟩ | |
| *(none of the above — MES-shaped)* | | |

## 3 · Check this plant's actual availability

Not the estate average — `references/deployment-reality.md` and this plant's own current
Smart Factory Tools Availability table. A tool being the right answer in principle and a
tool being deployed here are two different checks.

| | |
|---|---|
| **Tool availability at this plant** | ⟨status, dated⟩ |

## 4 · Verdict

- **Fits the lean footprint** — a covering tool exists and is available at this plant. Hand
  back to the calling skill; no further action here.
- **Redesign onto ⟨tool⟩** — the need is covered by a lighter tool than the request assumed;
  re-scope the request to that tool before it is defined any further.
- **Escalate as exception** — the need genuinely crosses into non-bet territory (MES/EMS-
  shaped, or a tool not yet deployed at this plant with no substitute). Route via
  `od-decision-routing`'s "Tool/system rollout" decision row — the OD lead decides in tandem
  with the IT-responsible role of the business side.

## Worked example

```text
Request: "Live dashboard showing which work order is running on which line, with
          automatic re-sequencing when a line goes down."
Plant: Example plant, MDA/PDA deployed, QFPR deployed, no MES.

1. Actual need: cross-process order scheduling with automatic re-sequencing logic.
2. Tool check:
   QFPR            no  - quality-record shaped, not order/schedule shaped
   MDA/PDA         no  - asset/machine-state data, not order orchestration
   MIL             no  - vision/image, unrelated
   Camline         no  - recipe master data, not scheduling
   WiriTec         no  - energy data, unrelated
   -> none cover it. This is MES-shaped: "cross-process scheduling... work-order
      management" is exactly tool-boundaries.md's MES tell.
3. Availability: MES not available at this plant per its own Tool Overview row (look
   up the plant's current row and date it); no standardized MES rollout per strategy.
4. Verdict: ESCALATE AS EXCEPTION. Redesign option considered and rejected - no
   combination of QFPR + MDA/PDA produces automatic re-sequencing without building
   scheduling logic the department does not own building. Routed to od-decision-routing.
```
