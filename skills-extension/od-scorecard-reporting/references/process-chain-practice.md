---
type: Skill Reference
title: Process chain practice
description: Method, decision rules, handoff contract, pitfalls and agent notes for running the community-of-practice call, other reporting rounds and the scorecard cycle, abstracted from the Operations Digitalization slide decks - agenda blocks, call for action, status colours, plant status and readiness tables, KPI-basis discipline, utilization next to count. Guidance only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice - rounds, status and reporting

Deck-derived practice for the spine. `PROPOSAL` = registry synthesis; `<to confirm>` = decks disagree or are dated.

## 1. Method in practice

**Forums and their jobs.** The strategy / information call (ODEC) is historical: it met monthly only until 2025-12 and no longer does, with no fixed replacement forum; its decks are a source of information. The table shows the jobs the formats had.

| Forum | Key question | Content | Output |
|---|---|---|---|
| Strategy / information call | why do we prioritize | strategy update, priorities and deadlines, accomplished sprints, scaling potentials, security strategic view | triggers for action, feeds the technical call |
| Community-of-practice call | how are we doing operations digitalization | technical issues, data-model updates, rule-engine flows, dashboards, training schedule, connector updates, security technical view | guidance on issues, triggers for action |
| Benefits call with the plant operations lead | what did it save | timing, savings, feedback | savings status |

Every format lists *input* (plant side and central side), *content* and *trigger for action*. **No fixed cadence is claimed**: reporting is on request or on the department's own schedule. A later deck may reuse an old agenda unchanged: check the current agenda before copying one.

**Standard agenda of the technical call:** roadmap and rollout status -> security call for action -> use-case forecast with one worked best-practice example -> trainings -> feedback on the last call's open process question. A fixed question pack drives it: technical issues, data-model updates, rule-engine flows, dashboards, training schedule, new connectors, ideas for new use cases.

**Preparing a round:** pull the plant status table, the readiness table and the integration status; write the call-for-action text; list which plants lack a registered savings project; attach links (project overview, status report, regional contacts). **After the round:** record the output, the open homework and the one retro change.

**Call for action format:** numbered steps with calendar weeks, a named link set, and an escalation line when a deadline was set by the operations head. A recurring weekly micro-process per rollout wave: call with the local technical expert, prepare the capital request with the local expert, upload with the local team, close-loop communication until approval; the same three steps shift one calendar week per plant.

**First round survey (to open a community):** are the tools working and which features are missing; which use cases were done, planned, should be standard; what process understanding was gained. Collect demand type per system (information, implementation, training) and a vote on which core process deserves a standard data model next.

## 2. Decision rules

- **Status colours.** Traffic light red / yellow / green, one scale per round. Plant or rollout status: red = phase delayed; yellow = close-loop update required; green = on track; add a call-for-action cell per row. "Input collected", "delayed" or "at risk" may appear only as reason text in the comment. Project status: red = out of plan, result endangered, steering decision required; yellow = minor deviation handled by the team with an action; green = per plan; grey = not applicable or no data. The project manager owns the colour, the steering committee decides on changes.
- **Report per region against plan** with a short relative judgement (proactive and good / slow and complex); regional gaps are structural as often as they are effort. Do not blend into one number.
- **Utilization is its own result next to delivery count.** "System and use-case utilization must be accelerated" recurs as a conclusion; a delivery count on target can sit beside a missed savings target because savings are unreported, not because nothing was gained.
- **Savings are counted only with a baseline, an owner and a registered plant savings project.** A use case without a registered project is invisible to the ledger; an implemented use case with no forecast is flagged "implemented, no forecast / no project registered".
- **Record the KPI basis with its date.** A use-case count against a threshold assumes the system landscape of its year; platform centralization shifts the count. Say which basis a figure used.
- **Escalation.** An unresolved item carries forward one round with the label "escalated"; a hard deadline set by management is quoted verbatim in the call for action.
- **Wave allocation:** eligibility follows request order; central capacity goes first to first-mover plants that are staffed (staffed key user, estimated value).

## 3. Handoff contract

| Receives | From |
|---|---|
| adoption / utilization findings per use case | `od-handover-and-adoption` |
| savings roll-up with tracked / proven split | `od-portfolio-and-savings-analysis` |
| integration status per plant and wave | `mi-connector`, project tracker |
| risks, blocked items, ticket age | `od-risk-watch` (planned), `mi-connector` |
| open homework from the last round | the previous output record |

| Hands on | To |
|---|---|
| round pack and the recorded outputs | participants; `od-retro` (planned) for the one change |
| plants without registered savings project, stale tag lists | `od-plant-onboarding` (planned), plant key users |
| leading indicators (participation, ticket age, utilization) | `od-risk-watch` |

## 4. Pitfalls and lessons

- **Reporting deprioritized in a busy year** meant impact could not be shown; the response was an impact analysis, a barrier overview and automated reporting.
- **Participation in the technical call is a leading indicator**: low participation went with low understanding and low savings.
- **Ticket age is a risk indicator** for systematic IT issues (reverse proxy, access, unknown approval process, no lifecycle management).
- **A sprint review that starts without a savings baseline never reports the saving.**
- **Template residue.** Initiative one-pagers still carried a leftover plan / forecast / actual table with identical placeholder numbers; do not treat them as initiative data.
- **Realized versus estimated wording.** A headline labelled "realized" that is in fact a top-down estimate: label it potential.
- **Metric families worth a source each (method only):** use cases integrated, savings, systems rolled out and months of delay, equipment integration count, share of standard deployments, systems and processes with major risk, schedule deviation, software footprint reduction. Planning tables use plan / forecast / actual per month with an overshoot line above target.
- **Scorecard filters** are region, location, manufacturing process; a security indication was added later. A plant management one-pager shows progress, regional engineering roadmap, plant scorecard, investment initiation, resource allocation and integration with the operational-excellence routine.

## 5. Questions to ask and definition of done

Which source is authoritative for this figure and what is its read date? Which basis does the count use? What does the plant do with the number? What is the call for action, who owns it, by which week? Which items carry from the last round?

**Done:** every figure has source and read date; leading and lagging metrics shown together; call for action numbered with weeks and owners; outputs recorded; one retro change decided.

## 6. AI agent operating notes

- **Can do:** draft the round pack from the portfolio and integration status lists (status colour, call-for-action text, plants lacking a registered project) citing list and read date; classify incoming questions into the question-pack categories and route them to the owning service line; keep homework items up to date and chase open ones; flag "implemented, no forecast".
- **Needs:** Scorecard and report extracts with read dates, plant status list, previous output record.
- **Human gate:** the OD lead decides escalation wording and which item is escalated; plant owners confirm status; targets are never filled in by the agent.
- **Must cite:** source report, filter, read date.
- **Hands over:** the pack with `<to collect>` for any missing source.
