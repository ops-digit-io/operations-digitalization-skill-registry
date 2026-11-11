---
type: Skill Reference
title: Lane handoffs
description: Each happy-path step matched to the real, current asset the composed skill now produces, confirmed against each skill's actual state rather than assumed from its name.
resource: ../procedure.md
status: stable
tags: [information-integration-service, lane]
---
# Lane handoffs

This lane page was written when every skill it composes into was a bare stub. All five are
now documented or deep. The step-to-skill mapping was still correct; what each step actually
hands off was not written down until now.

| Step | Composed skill | What actually changes hands |
|---|---|---|
| 1 — Equipment assessment and roadmap | `funnel-requirements`, then `mi-equipment` (assessment route) | A requirement spec, then `assets/assessment-protocol.md` — a machine-by-machine inventory, concept and connector per machine, sequenced and sized |
| 3 — Machine/equipment integration | `mi-equipment` (guidance route) | `assets/guidance-protocol.md` — one document per machine, the four gates answered in order |
| 4 — Signal standardization | `mi-signals` | The signal catalogue entry and clustering result for the newly connected data points |
| 5 — Acceptance testing | `deploy-acceptance` | `assets/acceptance-test-protocol.md` — pass/fail per artefact type, signed off, the input `deploy-handover` reads next |
| 7 — Report and readiness update | `metrics-scorecard` | The lane's own metrics row, read from `OD-Report-Equipment_Integration` and the Scorecard readiness matrix, with the escalation window (one COP round) already defined there |

**One correction to the happy path's own step numbering:** step 1 names "requirement via
`funnel-requirements`" in prose but that skill was missing from this lane's own
`composes` list — added 2026-10-23, since the handoff was already real, just unrecorded.

## What this settles, and what it does not

Confirming the handoff target exists and is current is not the same as the three items
still open at the top of `SKILL.md` (lane lead time, the investment-planning template, MSB
configure scope) — none of the five composed skills answers those; they remain exactly as
open as before.
