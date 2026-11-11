---
type: Skill Reference
title: Outputs
description: The outputs od-risk-watch must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-risk-watch` delivers a dated monthly risk reading against the six-row risk register: the indicator value, the trigger and a status per risk, and the triggers hit with the forum they go to. It never scores risks.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Risk reading | `assets/risk-reading.md`, filled | OD lead (owns five of the six risks); DBVE (owns the value risk) | All six risks have indicator value, source, read date, trigger and a status (triggered, on watch, clear or unreadable) with one-sentence evidence; register `last-verified` date noted, with a warning if older than the month |
| Triggers hit and routing | Triggers section of the risk reading | OD lead or the deciding role per the current approval policy; COP for technical items; `od-decision-routing` for decisions outside OD | Each triggered risk has its owner, forum and the countermeasure already in the register; any new countermeasure marked as a proposal |
| Unreadable indicators | Statuses in the reading | OD lead | Each unreadable indicator is reported as a finding with the missing source or the undefined parameter named; a risk unreadable three months running has a proposed register change |
| Retro input | The reading itself | `od-retro` | Reading available for the month's retro; a trigger hit two months running flagged as a candidate for the one adjustment |

## Handoff

- **Receives from:** `od-scorecard-reporting` and `od-portfolio-and-savings-analysis` (live figures), the risk register `09-risks.md`; `od-cybersec-gate` and `od-system-fit-check` for the Cyber Security and tooling rows.
- **Next in the flow:** `od-retro` (monthly input), `od-decision-routing` for triggers outside OD, the OD lead and COP for the rest. Other skills (`od-migration-cutover`, `od-plant-diagnosis`, `od-project-order`) hand open risks to it.
- **Stops here when:** an indicator has no source or its trigger parameter is `⟨n⟩`. Report it as unreadable, never as clear. Knowledge base aggregates are not readings, and no risk is added to the register by this skill.
