---
type: Skill Reference
title: Barrier log and cost of non-decision
description: The wave's barrier log - fields, how it relates to barrier triage, how to state the cost of non-decision, the rapid decision board and the error-log review - process guidance, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Barrier log and cost of non-decision

## 1. Purpose

A wave plan stays honest only if what holds machines back is written down with an owner. The log has two
jobs: show decision makers **which barrier holds back the most**, and show them **what waiting costs**.
`od-barrier-triage` classifies one stuck machine and routes it (roadmap, strategy, substitution); this log
is the wave-level list those results land in.

## 2. Fields (one row per barrier, not per machine)

| Field | Content |
|---|---|
| Barrier | What holds back, in one sentence; one root-cause class (`od-barrier-triage`) |
| Machines affected | By type and plant; count live at read time |
| Use cases waiting | Which use cases cannot start (they decide whether a connector is built) |
| Decision needed | The question, the forum (`od-decision-routing`), the decider role |
| Owner and due date | Role, calendar week |
| Wait state | Patch window, approval, procurement, none |
| Cost of non-decision | See section 3 |
| Status | open, decided, cleared, accepted as parked |
| Read date | Date the log was last checked |

## 3. Cost of non-decision

`PROPOSAL`: for each barrier waiting on a decision, state per week or per month of delay what is lost, and
what the decision costs or risks if taken. Compute it from the portfolio live, never from memory:

1. List the use cases that depend on the machines behind the barrier (`od-portfolio-and-savings-analysis`).
2. Take their expected value from the business case, with its firmness tag (potential, estimated, measured). Do not net value against cost.
3. State the delay in the unit of the decision calendar and the read date.
4. If no baseline exists, say "value unquantified" instead of a figure.
5. Add the second-order effects: next wave blocked, reputation, double work (running old and new in parallel).

The same logic appears in decision papers as "risk of not doing". An unfamiliar field may be funded as a
time-boxed first step to limit the cost of failure.

## 4. Rapid decision board

Barriers that wait for a decision go to a **rapid decision board**: a short meeting for holdbacks only,
with the barrier, the cost of non-decision and the options on one page. If no such board exists, the
deciding role or forum is the one named in the current approval policy (look up). Barrier types that recur: patch window,
operations concept missing (the most repeated tool barrier), tool or platform not rolled out, connector
to be developed for several machines, budget approved but no resource.

## 5. Error log and review

Keep a regular review of the log: weekly in the wave status call; what went wrong, what changed, who
decides. Feed lessons to `od-retro` and live risks to `od-risk-watch`. Typical classes of issue: knowledge
and understanding, service lines and processes, IT, project-management overhead.

## 6. AI agent notes

An agent can: collect rows from the status table and the triage records, group by class, compute the cost
line from the portfolio with the read date, flag rows without owner or due date, and draft the one-page
decision paper. The decision and the owner stay human; the agent cites the portfolio source and the read
date for every cost statement.
