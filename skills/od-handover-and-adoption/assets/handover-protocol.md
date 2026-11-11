---
type: Skill Asset
title: Handover protocol
description: The defined output of this gate - consumes od-acceptance-test's handover-readiness section as input, records the three-question test and the ADKAR barrier point, and its utilization-tracking section is what od-scorecard-reporting reads.
resource: ../SKILL.md
status: stable
tags: [all, template, protocol, adoption]
---
# Handover and adoption protocol — ⟨use case name⟩

Copy once per use case. Section 1 is filled from `od-acceptance-test`'s protocol, section 6
of that document — do not re-ask those questions. Sections 2-4 are this skill's own work.
Revisit section 5 on the Scorecard cadence; it is the one section meant to be reopened.

| | |
|---|---|
| **Use case** | ⟨name, plant, line⟩ |
| **From acceptance test** | ⟨reference to the passed `acceptance-test-protocol.md`, date⟩ |
| **Handover date** | ⟨date⟩ |
| **Overall status** | ⟨handover DONE / ONGOING · adoption tier 1/2/3 / none yet⟩ |

## 1 · Carried forward from the acceptance test

| Field | Value |
|---|---|
| Output asset | ⟨from acceptance-test protocol §6⟩ |
| Business process it supports | ⟨…⟩ |
| Utilization expectation | ⟨the moment in the day it belongs to⟩ |
| Data path, to the machine | ⟨…⟩ |
| Plant owner (named) | ⟨…⟩ |
| Affected people told before go-live (who, when, how) | ⟨…⟩ |
| Open dependency, if any | ⟨…⟩ |

## 2 · The three-question test

Answered by the receiving side, without asking the person who built it.

| Question | Answer |
|---|---|
| What is this, and what decision does it support? | ⟨…⟩ |
| Where does its data come from, and what breaks it? | ⟨…⟩ |
| Who owns it now, and who do they call? | ⟨…⟩ |

## 3 · ADKAR barrier point

Rate 1-5 in order; stop and record the first element that is not yet sufficient (≤3) — see
`references/adkar-diagnostic.md`.

| Element | Score (1-5) | Barrier point? | Note |
|---|---|---|---|
| Awareness | ⟨…⟩ | | |
| Desire | ⟨…⟩ | | |
| Knowledge | ⟨…⟩ | | |
| Ability | ⟨…⟩ | | |
| Reinforcement | ⟨…⟩ | | ⟨reassessed on the Scorecard cadence, not only at handover⟩ |

**Action taken, if a barrier point was found:** ⟨…⟩ — see the per-element rollout action in
`references/adkar-diagnostic.md`; never apply a Knowledge fix to a Desire barrier.

## 4 · Evidence of adoption

Per `references/evidence-of-adoption.md`, strongest tier actually available — never upgraded.

| Tier | Evidence | Source | Date |
|---|---|---|---|
| ⟨1 system usage log · 2 named owner's dated statement · 3 third-party observation · none⟩ | ⟨…⟩ | ⟨…⟩ | ⟨…⟩ |

## 5 · Handed to `od-scorecard-reporting`

Reopen this section on the Scorecard cadence, not only once:

| Field | Value |
|---|---|
| Utilization rate (latest) | ⟨…⟩ |
| Trend since last check | ⟨rising · stable · falling · NEVER⟩ |
| Retirement considered? | ⟨yes/no, and why⟩ |

## Do not

- Do not fill section 1 by re-asking the acceptance test's questions — pull them forward.
- Do not record an adoption tier higher than the evidence actually supports.
- Do not treat a Knowledge-element action as the fix for a Desire-element barrier point.
- Do not close this protocol after one good week; Reinforcement is read over time.
