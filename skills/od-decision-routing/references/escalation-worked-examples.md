---
type: Skill Reference
title: Escalation worked examples
description: Illustrative patterns, from the historical ODEC and COP records, where the forum was not obvious, how it was decided, and what happens when something lands at the wrong forum - guidance only, no plant names or figures.
resource: ../SKILL.md
status: stable
tags: [all, practice, decision-rights]
---
# Escalation worked examples

`SKILL.md` states the rule — strategy, priority, rollout and blocked projects go to the OD lead and the deciding role
named in the current approval policy (look up), technical matters go to COP — but a rule stated in the abstract is not the
same as knowing where a real, ambiguous blocker actually went. ODEC is a historical forum and a source of information: it met
monthly only until 2025-12 and no longer does, so nothing below is a current rhythm or a place a decision must go now. The
patterns were distilled from the ODEC and COP call decks (see `metadata.derived_from`) and are given as illustrations,
without plant names, dates or counts.

## The forums' own stated boundary

Both call types carried an identical pair of slides defining themselves in the same words
— this is the department's own record of the boundary, not an inference from behaviour:

| | ODEC | COP |
|---|---|---|
| **Key question** | "Why are we prioritizing Operations Digitalization?" | "How are we doing Operations Digitalization?" |
| **Key objective** | Strategy and Smart Factory tools | Technical implementation of machine integration, data models, use cases |
| **Typical content** | Strategy updates, roadmaps/rollouts/workshops, use-case sprints with savings focus, **strategic view of Cyber Security & OT** | Data-model updates, rule-engine/transformation-flow and dashboard use cases, connector updates, **technical view of Cyber Security** |
| **What it triggers** | COP and CSP calls | Action — direct, within the call |

The split for a topic is almost never "ODEC or COP" — it was "the strategic level (then ODEC) for the strategic
half, COP for the technical half," and cybersecurity is the clearest case of both halves
being named explicitly in the template itself.

## Illustrative pattern 1 - Cybersecurity: strategic framing at strategy level, execution at COP

*Illustrative; names and dates are placeholders.*

A cybersecurity *standard or compliance posture* appeared as an ODEC strategy item: situational
awareness across shop-floor systems, a two-path decision model (substitute the solution vs.
approve and manage it externally), and the objective of steering standard creation and
deployment. Nothing plant-specific, no project name, no deadline - pure standard-setting.

Once a programme exists to implement that standard, it appears at COP as a named project with a
presenter, a status per region and a **call for action** with concrete steps and a due date. If
the deadline needs pushing, the push may come from outside both forums (a line-management
escalation) and lands at COP as an action item, because by then it is a delivery question, not a
strategy question.

**What this settles:** a standard or compliance-posture question is a strategy-level question (historically ODEC's). Once a project exists
to implement it, the project itself (status, regional rollout, who does what by when) is COP's,
even though the underlying topic never changes.

## Illustrative pattern 2 - A platform-access blocker that stays at COP

*Illustrative.*

A machine-integration status table shows one plant "ongoing" with a next step such as "regular
call with project team / central IT until the platform access issue is completed". This is a real
technical blocker stopping a plant's wave, yet it is worked entirely as a COP / local-IT
follow-up. **The tell:** the blocker has an owner who can act on it directly (central IT, the
local project team) and a mechanism already in motion (a recurring call). A technical blocker
escalates to strategy level (the OD lead) when no one inside the technical chain can clear it alone - not simply because
it is blocking.

## Illustrative pattern 3 - A process/tooling gap raised at strategy level, executed per plant at COP

*Illustrative.*

Cost-transparency problems for machine-connectivity and rollout eCRs recur in several locations,
causing long budget discussions and deviations from standard rollout templates. The proposed fix
is a tool (a cost calculator) - a cross-plant, standard-setting response to a pattern seen in
*multiple* locations. That is what makes it a strategy-level item (historically ODEC's): one plant's slow eCR is not a strategy item, a
recurring pattern across plants is.

The eCR work itself is COP's standing per-plant process: exchange call with the local OT expert,
prepare the eCR to the planned budget, upload it with the local team, close the loop until
approved - one eCR per machine wave, per plant, with no strategy-level involvement at any step.

## What happens when something lands at the wrong forum

Items are rarely *rejected* from a forum and bounced back - the two forums have different
standing agendas (ODEC, historically: strategy update, use-case rollouts, tooling; COP: machine-integration
status, cybersecurity project status, training, tag selection) and a presenter places the topic
on the agenda section that matches it. The real failure mode is different and more informative:
**when COP itself does not run well, the technical half simply does not get done.** Poor call
attendance affects standard reporting, next-wave machine-integration budget may not be claimed in
time, and security programmes sit on risk. Nothing escalated upward to ODEC when COP
under-delivered - the technical items slip, and the same status tables recur unresolved across
consecutive months.

**The practical rule this supports:** if a technical item has been sitting unresolved across more
than one COP cycle with no forward motion, that is itself the signal to escalate to the OD lead - not
because the forum was wrong, but because COP-level follow-up has stalled and only the strategy level can
re-prioritize the resource or capacity behind it.

## Sources

Distilled from the department's ODEC and CoP call decks (full citations in `SKILL.md`'s
`metadata.derived_from`). Only the stable Key-Question / Key-Objective split of the two forums is used here.
