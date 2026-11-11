---
type: Skill Reference
title: Outputs
description: The outputs od-skill-authoring must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-skill-authoring` delivers a new or reworked skill that has passed the registry gates, with the one-page brief that preceded it and a pull request for the department owner. It never marks a skill reviewed or verified.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Skill brief | `assets/skill-brief.md`, filled | Department owner | Need, users, lane and step, tier, authority level, inputs and outputs, sources and three test cases are written, and the owner agreed the brief before the skill was written |
| Skill folder | Folder written to the registry's anatomy | Department owner (DBVE; the OD lead approves publication) | Passes the registry validator, the specification export, the OKF check and the figures check; status stays `draft` |
| Registry, flow and README entries | `registry.yaml` entry (authority level equal to the `SKILL.md`), placement on `docs/new-state/process.yaml`, README row | Department owner | All three entries exist and the generated pages are regenerated |
| Quality rating and test record | Rating from the SkillEvaluator; test cases and trigger queries | Department owner | Rating is recorded (proposed target B or higher); cases and trigger queries are written and run, or stated as not run |
| Pull request | Pull request using `assets/release-checklist.md` | Department owner | Carries the rating and the open points; owner has reviewed it |

## Handoff

- **Receives from:** `od-context` (department context); a recurring OD procedure with a named owner; `od-context-freshness`, `od-ai-generation-playbook` and `od-decision-routing` are composed where their topics apply.
- **Next in the flow:** supporting spine, no process step. The department owner reviews and decides; only a human sets a status beyond `draft`.
- **Stops here when:** an existing skill already covers the topic (extend it instead), no owner is named, the owner has not agreed the brief, or a gate fails. Never invent a figure, name or source to make a skill look finished; mark the gap `to confirm` and name who can fill it.
