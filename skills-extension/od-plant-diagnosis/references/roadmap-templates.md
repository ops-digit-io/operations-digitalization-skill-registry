---
type: Skill Reference
title: Roadmap templates
description: Fields of the plant roadmap and the regional roadmap, the status colours and the call-for-action format, and how the calls consume them; open it to draft or refresh a roadmap.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Plant and regional roadmap templates

Fields, not content. Fill live; do not copy numbers from an old deck. Tables to copy: [`../assets/plant-roadmap-template.md`](../assets/plant-roadmap-template.md).

## Plant roadmap: workstreams (one row each)

Machine-integration wave; use cases deployed; system and platform rollout; cyber-security application screening, impact
analysis and migration planning; admin use cases (ETL, BI); energy-data integration; standard data model for the plant's
process families (with other regions); training roll-out; app roll-out; analytics and AI roll-out; know-how management.
Add a **chances** box and a **workload** line (one responsible person per location for digitalization use cases).
Inputs that feed the plant roadmap: carry-over projects, new plant requests with high value-add (need for
standardization), system, equipment and use-case rollouts, and central strategic initiatives. Plants should raise
requests proactively.

Per row: owner role, end-of-quarter target, status colour, evidence, call-for-action text.

## Status colours

| Colour | Rule |
|---|---|
| Red | Phase delayed |
| Yellow | Close-loop update required (the plant has not confirmed the next step) |
| Green | On track, evidence attached |

One traffic-light scale (red / yellow / green) per round. A row without evidence is not green; "not started" goes in the comment.

## Call for action

A short numbered list per call, each step with a calendar week and a named link set (project overview, status report,
regional contacts), and an escalation line where operations management set a deadline.
Shape borrowed from the cyber-security call for action, four steps: (1) check the project overview and process flow,
(2) check own status and missing factors in the shared dashboard, (3) contact OD for the remaining steps, (4) implement
and finish before the deadline. A rollout wave repeats a weekly micro-process per plant, shifted one calendar week per
plant: call with the local OT expert, prepare the capital request with the local expert, upload with the local team,
close-loop communication until approval.

Write each action as: verb, object, role, calendar week, link. Example (illustrative): "Confirm the <system> status in the
shared dashboard - <plant key user> - <CW> - <link>."

## Regional roadmap

Frame conditions with an owner area and end-of-quarter dates for: equipment integration, use-case deployment, system
deployment, data ecosystem (for example data lifecycle), cyber security, admin use cases, energy data, standard data
models (with other regions), know-how management, analytics and AI. Two KPIs: use-case savings target and integration
count target (values live from the scorecard). Chances; workload (one responsible person per location); responsibility
(timeline for system rollouts, cost-saving calculation and reporting for use cases, compliance of new requests). A
brainstorm page lists per plant the machines, systems and open questions, marked "?" when unknown. A short, mid and long
term horizon page spans all regions. Drafts are approved in the plant engineering roadmap workshops.

Report per region against plan with a short relative judgement (proactive, slow and complex), not a blended number;
regional gaps are structural (complex infrastructure) as much as effort.

## Who consumes it

- **Community-of-practice call** (technical, plant-facing; look up the current schedule): roadmap and rollout status, then cyber-security call
  for action, then use-case forecast with one worked example, then trainings, then feedback on the last open question. The
  plant status table: plant, system status, machines done of planned, traffic light, call for action.
- **Strategy rounds** (ODEC, now historical, no fixed replacement forum; past decks are a source): regional roadmaps, cyber-security status.
- Plant management one-pager: current progress, regional engineering roadmap, plant scorecard, initiate investment,
  allocate resources, integrate with OPEX processes.
Hand over to `od-scorecard-reporting`; investment items to `bc-cost`.
