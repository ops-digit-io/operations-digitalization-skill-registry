---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Outputs and hand-off: the text before outputs.yaml

`dept-risk` delivers a dated monthly risk reading against the six-row risk register: the indicator value, the trigger and a status per risk, and the triggers hit with the forum they go to. It never scores risks.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Risk reading | `assets/risk-reading.md`, filled | OD lead (owns five of the six risks); DBVE (owns the value risk) | All six risks have indicator value, source, read date, trigger and a status (triggered, on watch, clear or unreadable) with one-sentence evidence; register `last-verified` date noted, with a warning if older than the month |
| Triggers hit and routing | Triggers section of the risk reading | OD lead or the deciding role per the current approval policy; COP for technical items; `dept-decision-rights` for decisions outside OD | Each triggered risk has its owner, forum and the countermeasure already in the register; any new countermeasure marked as a proposal |
| Unreadable indicators | Statuses in the reading | OD lead | Each unreadable indicator is reported as a finding with the missing source or the undefined parameter named; a risk unreadable three months running has a proposed register change |
| Retro input | The reading itself | `dept-retro` | Reading available for the month's retro; a trigger hit two months running flagged as a candidate for the one adjustment |

## Handoff

- **Receives from:** `metrics-scorecard` and `bc-portfolio` (live figures), the risk register `09-risks.md`; `deploy-cybersec` and `invest-screen` for the Cyber Security and tooling rows.
- **Next in the flow:** `dept-retro` (monthly input), `dept-decision-rights` for triggers outside OD, the OD lead and COP for the rest. Other skills (`deploy-migration`, `dept-plant-diagnosis`, `deploy-project-order`) hand open risks to it.
- **Stops here when:** an indicator has no source or its trigger parameter is `⟨n⟩`. Report it as unreadable, never as clear. Knowledge base aggregates are not readings, and no risk is added to the register by this skill.

## Provenance

Plan item O-07 of the department's skill map. The risk register (`09-risks.md`, review cadence monthly) is built so that an agent can watch it: "an early indicator is a monitorable value - a register an agent can watch, not a table opened once a year". It deliberately has no probability x damage matrix ("false precision; the early indicator does more").

## What is still open

- **Parameters:** `open role > ⟨n⟩ months` has no n unless the OD lead has set one; "impact < target" needs a defined target for use-case impact.
- **Sources with no system named:** support tickets, open-role list, "dependence on few individuals".
- **Owner of the external-tooling risk** is `⟨to confirm⟩` in the register.
- **Escalation window** of COP and the deciding role is `⟨to confirm⟩`.
- **Who may declare a trigger "triggered"**: the register names risk owners, not a declarer.

## Sources used in the improvement run

- None beyond the existing skill material; no vault or archive claim was added.
