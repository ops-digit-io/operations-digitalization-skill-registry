---
type: Skill Reference
title: Sprint runbook
description: How a plant use-case sprint is planned, run and reviewed - preconditions, rhythm, standard deliverables, review questions, additional-phase rule and pitfalls.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---
# Sprint runbook

Lane flow lives in `funnel-use-case`; build in `ops-analytics-asset`; prototype in `funnel-prototype`.

## Preconditions (all before day one)

- Machines connected and signals selected for the sprint scope.
- A named expert for the process and the plant key user in the team from the start.
- Savings baseline and owner defined, and the use case linked to a registered plant savings project.
- Architecture and user access agreed (OT/IT separation, firewall, access for local users).
- Notification channels and historization requested as changes.
- Out-of-scope written down explicitly ("avoid grey zones").
- Flows kept in version control; impact of any runtime redeployment checked.

## Rhythm

Time-box 3 to 6 weeks (earlier 3 to 4, later re-planned per 4 to 6 as a continuous activity). One weekly status
review of about 30 minutes, one to two technical meetings a week of about 60 minutes, a mid-sprint status
update, a sprint-end review with a Q&A link. Keep an IT-issue log from day one.

## Standard deliverable set

Generic process-value dashboard for all machines; andon board (status plus history); operations dashboard
(output, cycle time, alerts per time group or shift); machine availability by mode; one process-specific
dashboard as blueprint; alert dashboard; SPC for inline measurement; data-transformation flows (one or more
per PLC) with documentation. Check the dashboard tool in `dept-context`.

Quality dashboards that do not depend on machine connectivity (lab tests) run on a different path, owned by
the local quality team; do not put them into the integration sequence.

## Review questions

What was carried over from another plant; what is blocked; what is a rollout option to other machines or
plants; are flows and dashboards documented; is the scalability statement made; open topics; impact of IT issues.

## Rules

- Use cases only for connected machines; a requirement beyond the time-box is an additional phase.
- Rollout of a dashboard is gated by integration and tag selection, not by the dashboard.
- Done means integrated into a standard operating procedure with a utilisation review, not "dashboard live".
  Pair the use case with the plant's lean method and standard process.

## Pitfalls

Missing process understanding with one machine connected; flows that do not scale or are unstructured;
architecture changes during the sprint cost weeks; no baseline, so savings are never reported; deployments
without a defined action produce visibility but no saving.
