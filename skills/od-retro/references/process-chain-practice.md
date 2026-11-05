---
type: Skill Reference
title: Process chain practice
description: Where the retro gets its learning items in the AI-driven chain - issue-log loop, feedback forms, project-closure lessons, sprint and workshop recaps, a cause classification, clean-up and kill/hold hygiene, and what an agent may draft. Pattern only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice

Distilled from the Operations Digitalization slide decks, abstracted into process guidance. No company figures. `PROPOSAL`
marks a synthesis; `<...>` is unknown. The one-adjustment rule of [`SKILL.md`](../SKILL.md) is unchanged; this file adds where
good learning items come from and how to classify them. It adds to [`retro-inputs.md`](retro-inputs.md).

## 1. Method in practice

**Feeders of the monthly retro** (all are inputs, none is a substitute for the evidence rule):
- **Issue-log loop:** a weekly review per region of all meetings and events with the question "what went wrong", feedback
  forms after each major event, and a yearly strategy check of goals, KPIs and the system. Top issue classes seen: knowledge
  and understanding, service lines and processes, IT, project-management overhead.
- **Sprint review:** what was carried over from another plant, what is blocked, what is a rollout option; open topics and
  IT-related issues with their impact.
- **Workshop recap:** "what can we do better next time" is an agenda item of an integration workshop; a formal project closure
  can sit inside it.
- **Project closure report** (lessons-learned part): topic, experience to keep or change, proven solution, originator; plus
  the five major risks with countermeasure, owner and due date, organisation changes, and a closure checklist including
  "handover completed?".
- **Community-call feedback and survey answers,** classified into the question-pack categories (technical issues, data-model
  updates, flows, dashboards, training schedule, connectors, ideas for use cases).

**Check the loop on the system, not on the case.** The aim is a repeatable, owned system that generates use cases, not an
activity per use case. A system is diagnosed by its KPIs, a project by project management. Ask of every learning: what has to
happen to be able to reuse this (concept and quality)?

## 2. Decision rules

**Classify each learning by cause** (a condensed cause map used in a gap analysis; it helps spot recurrence across months):
- *Method:* no standard for savings calculation, weak requirements management, no systematic follow-up and escalation,
  approaches explained too complexly.
- *Machine and IT:* scattered infrastructure, black-box legacy systems, no interoperability, slow feature updates.
- *People:* "not my responsibility", unclear OD / IT / engineering roles, production or OPEX not involved.
- *Environment:* security approval that does not integrate, purchasing lead times beyond project timelines, no incident
  management for operational systems.

Then apply the retro's own test (can OD change it alone, reversible, observable next month).

- **Prefer clean-up over addition.** The recurring pattern: "if a system is insufficient people introduce another
  insufficient system; we forget to clean up". When two candidate adjustments are equal, prefer the one that removes or merges
  a tracker, slide or system. `PROPOSAL`
- **Requests for fonts, colours or headlines of dashboards** burn capacity at low value: route by cost-saving impact and
  time-box in sprints. A recurring pattern of this kind is a valid retro item.
- **Keep a kill/hold register** with the recorded reason, so cancelled ideas are not re-raised; reading it is a retro input.
- **Do not reopen routed decisions;** learn from them (rule in `SKILL.md`).

## 3. Handoff contract

| Receives (from) | Hands on (to) |
|---|---|
| Metrics and round outputs (`od-scorecard-reporting`) | The one adjustment with owner role, date and observable |
| Risk reading with triggered items (`od-risk-watch`) | Escalations to `od-decision-routing` (ODEC / COP) |
| Evaluation findings: promise versus outcome (`od-impact-evaluation`) | Adjustments to context files -> `od-context-freshness` |
| Closure and sprint lessons | Parking list with first-seen month |

## 4. Pitfalls and lessons

- Lessons that name no originator or no proven solution cannot be reused.
- Ad-hoc request volume and under-used calls recur as causes; training and calls need participation to work.
- Admin-process improvements are deprioritised against daily business; a dedicated, empathic role that asks stakeholders
  continuously and drafts lean solutions works best.
- Learnings from the field that stay in a deck and never reach a decision.

## 5. Questions to ask / definition of done

- What went wrong this month? What recurred? Which of these can OD change by itself? What would show it worked?
- Done when: last month's check is closed, every learning has evidence and a cause class, exactly one adjustment is
  recorded with its observable, the rest is parked with the first-seen month.

## 6. AI agent operating notes

- **Can do:** gather the month's feeders, group learnings by cause class and by recurrence, draft the check question for last
  month's adjustment with the evidence found, and propose the preference order result; classify incoming feedback into the
  question-pack categories and route it to the owning service line.
- **Required inputs:** last month's record, metrics with read dates, risk reading, issue log, closure and sprint reports.
- **Human gate:** the decider takes the adjustment; an agent never invents a candidate when none is evidence-backed.
- **Evidence to cite:** source and date per learning.
- **Hands over:** the record with one adjustment to the next ODEC / COP input.
