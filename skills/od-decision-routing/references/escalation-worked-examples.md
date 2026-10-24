---
type: Skill Reference
title: Escalation worked examples
description: Real blockers where the forum (ODEC vs COP) was not obvious, how it was actually decided, and what happens when something lands at the wrong forum — Phase-1 tacit-knowledge item #4, resolved from the department's own call decks rather than from memory.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [all, practice, decision-rights]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Escalation worked examples

`SKILL.md` states the rule — ODEC for strategy/priority/rollout/blocked projects, COP for
technical matters — but a rule stated in the abstract is not the same as knowing which
forum a real, ambiguous blocker actually went to. Rather than ask the department lead to
recall examples from memory, this file is built from the actual ODEC and COP call decks
themselves (internal evidence — see `metadata.derived_from`), which record real items,
real presenters and real outcomes.

## The forums' own stated boundary

Both call types carry an identical pair of slides defining themselves, every month, in the
same words — this is the department's own rule, not an inference from behaviour:

| | ODEC | COP |
|---|---|---|
| **Key question** | "Why are we prioritizing Operations Digitalization?" | "How are we doing Operations Digitalization?" |
| **Key objective** | Strategy and Smart Factory tools | Technical implementation of machine integration, data models, use cases |
| **Typical content** | Strategy updates, roadmaps/rollouts/workshops, use-case sprints with savings focus, **strategic view of Cyber Security & OT** | Data-model updates, rule-engine/transformation-flow and dashboard use cases, connector updates, **technical view of Cyber Security** |
| **What it triggers** | COP and CSP calls | Action — direct, within the call |

The forum split for a topic is almost never "ODEC or COP" — it is "ODEC for the strategic
half, COP for the technical half," and cybersecurity is the clearest case of both halves
being named explicitly in the template itself.

## Worked example 1 — Cybersecurity (Groot2B): strategic framing at ODEC, execution at COP

At ODEC #9 (September 2024), cybersecurity appeared as a strategy item: *"OT Solutions &
Cybersecurity Compliance Report"* — situational awareness across shop-floor systems, a
two-path decision model (substitute the solution vs. approve and manage it externally), and
the objective *"steer standard creation & deployment."* Nothing plant-specific, no project
name, no deadline — pure standard-setting.

The same programme, Groot2B, showed up at the CoP call (#1, February 2024) as a named
project with a presenter, a status per region (Americas/APAC/EMEA), and a **Call for
Action** with four concrete steps (check the project overview, check status via a Power BI
report, contact the OD team, implement before Q2) — plus the line **"Escalation from Head
of Operations BA OESL to complete the project until Q2."**

**What this settles:** a cybersecurity *standard or compliance posture* question is ODEC's
— no project, no deadline, just "what should the rule be." Once a project exists to
implement it, the project itself (status, regional rollout, who does what by when) is
COP's, even though the underlying topic (cybersecurity) never changes forum. The
escalation that pushed the Q2 deadline came from outside both forums (Head of Operations)
and landed as an action item at COP, not at ODEC — because by that point it was a delivery
question, not a strategy question.

## Worked example 2 — A platform-access blocker that stayed at COP and never reached ODEC

The same CoP call's Machine Integration status table records, per plant, a RAG status and a
named next step. San Prairie: *"Ongoing, 0 of 10 machines… Regular call for close loop with
project team/Central IT team **until the access issues to the platform (MSB Aggregation
Server) is completed**."*

This is a real, named technical blocker (platform access) stopping a whole plant's wave.
It never shows up as an ODEC agenda item in any of the surrounding months' decks — it was
worked entirely as a COP/local-IT follow-up. **The tell:** the blocker has an owner who can
act on it directly (Central IT, the local project team) and a mechanism already in motion
(a recurring call). A technical blocker escalates to ODEC when no one inside the technical
chain can clear it alone — not simply because it is blocking.

## Worked example 3 — A process/tooling gap raised at ODEC, executed per-plant at COP

ODEC #9 raised the **eCR Calculator** as a strategy item: *"Issues regarding cost
transparency for Machine Connectivity and Rollout eCRs in multiple locations… leading to
unnecessary long discussions for budget planning and purchasing… deviations from standard
rollout templates."* The proposed fix is a tool (a cost calculator) — a cross-plant,
standard-setting response to a pattern seen in *multiple* locations. That is what makes it
ODEC's: one plant's slow eCR is not a strategy item, a recurring pattern across plants
is.

The actual eCR work this was meant to speed up is COP's own standing process, spelled out
step by step in the CoP call deck: exchange call with the local OT expert → prepare the eCR
to the planned budget → upload it with the local team → close the loop until approved —
one eCR per machine wave, per plant, with no ODEC involvement at any step.

## What happens when something lands at the wrong forum

Nothing in the record shows an item being *rejected* from a forum and bounced back —
the two forums have different standing agendas (ODEC: strategy update, use-case rollouts,
tooling; COP: machine-integration status, cybersecurity project status, training, tag
selection) and a presenter places their topic on the agenda that matches its *agenda
section*, not the forum as a whole. The real failure mode the record shows is different and
more informative: **when COP itself does not run well, the technical half simply does not
get done.** The CoP call's own "Current Status" slide (#1, February 2024) names the direct
consequences of poor call attendance: standard reporting affected, "Machine Integration
next wave budget might not be claimed or not claimed in time," and "Cyber Security – Groot2B
management on Risk." Nothing escalates upward to ODEC when COP under-delivers — the
technical items simply slip, which is why the same status tables (machine-integration RAG,
Groot2B regional status) recur, unresolved, across consecutive months' decks.

**The practical rule this supports:** if a technical item has been sitting unresolved
across more than one COP cycle with no forward motion, that is itself the signal to
escalate to ODEC — not because the forum was wrong, but because COP-level follow-up has
stalled and only ODEC can re-prioritize the resource or capacity behind it.

## Sources

Internal evidence, read 2026-10-22: the department's own ODEC and CoP call decks, as
individually split slides. Full citations in `SKILL.md`'s `metadata.derived_from`. One
caveat worth stating plainly: the earliest deck in the set names the forum "ODIC"
(Operations Digitalization Information Call), renamed to "ODEC" by the dated decks used
above — the rename itself is not analysed here, only the stable Key-Question/Key-Objective
split that survived it.
