---
type: Skill Asset
title: Acceptance test protocol
description: The defined output of this gate - written before the build, filled as the test runs, and the final section is exactly what deploy-handover needs as input.
resource: ../SKILL.md
status: stable
tags: [project-support-consultancy, information-integration-service, template, protocol]
---
# Acceptance test protocol — ⟨artefact name⟩

Copy once per artefact (machine connection, flow, dashboard or evaluated use case). Write
sections 1–2 **before** the build is tested, not after — see `SKILL.md`. Choose the
matching row of `references/test-structure.md` for section 3's columns.

| | |
|---|---|
| **Artefact type** | ⟨machine/connector · Node-RED flow · dashboard/analytics asset · evaluated use case⟩ |
| **Use case / machine** | ⟨name, plant, line⟩ |
| **Witness (receiving side)** | ⟨name — never the builder⟩ |
| **Date run** | ⟨date⟩ |
| **Overall result** | ⟨pass · fail, n of m items⟩ |

## 1 · Scope, written before the test

⟨List every signal, function or scenario in scope, individually — not "the dashboard
works."⟩

## 2 · Expected result and tolerance, written before the test

⟨For each item in §1: the expected value/behaviour and its tolerance, or the business
scenario and its expected outcome.⟩

## 3 · Test record

| Item | Expected | Real or simulated / preconditions | Result | Evidence |
|---|---|---|---|---|
| ⟨…⟩ | ⟨…⟩ | ⟨…⟩ | ⟨pass/fail⟩ | ⟨screenshot, logged value, trace⟩ |

Record every item, passing ones included — see `references/test-structure.md`.

## 4 · Failures and rework

| Item | What failed | Loop (per `references/signoff-and-rework.md`) | Owner |
|---|---|---|---|
| ⟨…⟩ | ⟨…⟩ | ⟨equipment rework · project management · integration hand-off⟩ | ⟨name⟩ |

## 5 · Sign-off

**A human signs here. Never an agent, never the builder.**

⟨Name, role, date, "I witnessed this test and accept the result above."⟩

## 6 · Handover readiness — carried forward into `deploy-handover`

Fill this section only on an overall pass. It is written so the next skill does not need to
ask again.

| Field | Value |
|---|---|
| Output asset | ⟨Dashboard · Report · App · Analytics Workflow · Agent⟩ |
| Business process it supports | ⟨…⟩ |
| Utilization expectation | ⟨moment in the day it belongs to — daily Gemba, shift check, Andon escalation, …⟩ |
| Data path, to the machine | ⟨machine → connector → ingress variant → edge → offload → data platform → asset⟩ |
| Plant owner (named) | ⟨name⟩ |
| Open dependency, if any | ⟨…⟩ |
