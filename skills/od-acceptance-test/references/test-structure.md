---
type: Skill Reference
title: Test structure
description: The test-case structure per artefact type that reaches this gate — a connected machine, a Node-RED flow, a dashboard, an evaluated use case — grounded in FAT/SAT/SIT and UAT practice.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [project-support-consultancy, information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Test structure, per artefact type

This gate receives two different shapes of work, and each has its own established testing
discipline. Use the one that matches what is actually being accepted; do not force a
dashboard through a FAT checklist or a machine connection through a UAT script.

## Hardware and connectivity: FAT / SAT / SIT

Industrial automation's own three-stage acceptance sequence (IEC 62381, *Automation
systems in the process industry — factory acceptance test (FAT), site acceptance test
(SAT), and site integration test (SIT)*; summary verified via automationforum.co, not the
standard itself — treat the standard as the citable source if it is ever read directly):

1. **FAT** — at the vendor, before shipment: hardware, logic, interfaces and communication
   verified against simulated signals.
2. **SAT** — at the plant, after installation: the same system verified against real field
   devices, real networks, real power.
3. **SIT** — the integrated system: every subsystem verified working together, not each in
   isolation.

**This registry's gate sits at SAT/SIT, never FAT.** `od-equipment-integration` and
`od-node-red-flow-builder` build and test on a `test` instance first (their own FAT-
equivalent); this skill's protocol is the SAT/SIT step — real field devices, the real
network, the full path end to end, because that is the only version of "it works" the
plant can act on. A test that only proves the logic correct against simulated signals has
not reached this gate yet.

**Structure, adapted from FAT/SAT checklists and this registry's own data path**
(`od-equipment-integration`'s machine → connector → ingress variant → edge → offload →
data platform → asset):

| Field | What goes in it |
|---|---|
| Item | The signal, function or connection under test, named individually |
| Expected value / behaviour | With its tolerance — a number alone is not a test |
| Verified at | Which hop of the data path this check actually exercises |
| Real or simulated | SAT/SIT means real field devices — say so if anything is still simulated, and treat that as not yet acceptance-tested |
| Result | Pass / fail, recorded either way |
| Evidence | What was actually observed (a screenshot, a logged value, a debug trace) — not "confirmed" alone |

## Dashboard, analytics and evaluated use cases: UAT

User acceptance testing's own structure (verified via BrowserStack's UAT template guide)
translates directly:

| Field | What goes in it |
|---|---|
| Test Case ID | A distinct identifier, so a failure can be reopened and re-run |
| Scenario | Tied to the use case's stated business benefit (`od-use-case-definition` Phase 2), not to the dashboard's existence |
| Preconditions | Data flowing, signals standardized, the plant owner briefed |
| Steps | What the plant owner actually does, in the order they do it |
| Expected result | What they should see or be able to decide |
| Actual result | What was observed |
| Pass / fail | A decision rule stated before the run — ISO/IEC/IEEE 29119 Part 1's own definition of pass/fail criteria: "a decision rule used to determine whether a test item... has passed or failed," decided in advance, not negotiated after seeing the result |

**The witness is the plant owner, not whoever built it** — the same rule UAT practice
states explicitly ("preferable to have UAT carried out by the personnel who will be using
the program the most") and this registry's own `od-handover-and-adoption` requires
independently: a demonstration by the builder is not an acceptance test.

## What every artefact type shares

Regardless of which table applies, the same five things from `SKILL.md`'s procedure are
non-negotiable: the item is named individually, the expected result and tolerance are
written before the test runs, the full data path is in scope (not just the layer that is
easy to check), the witness is named, and every result is recorded — passing items
included, not only failures. A protocol with only failures recorded cannot be re-run,
because nobody downstream can tell what was actually checked.
