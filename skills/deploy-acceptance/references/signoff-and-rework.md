---
type: Skill Reference
title: Signoff and rework
description: Who signs off on each artefact type, what a failure actually means, and the rework loop it triggers rather than a quiet retry.
resource: ../SKILL.md
status: stable
tags: [project-support-consultancy, information-integration-service, practice]
---
# Sign-off and rework

## Sign-off authority follows the artefact, never the builder

Industrial FAT/SAT/SIT practice splits sign-off by stage — vendor and client at FAT,
project team and commissioning engineer at SAT, operations and safety jointly at SIT. UAT
practice is explicit that the signer is "the personnel who will be using the program the
most," never the team that built it. Both traditions converge on the same rule this
registry already states: **acceptance sign-off is human-only, and it is the receiving
side, by name — never the agent or person who built the thing.**

| Artefact | Who signs |
|---|---|
| Machine / connector (Information Integration) | Plant ME / Plant IT, the named contact who will own the connection |
| Node-RED flow | Plant ME/IT, after it has run on the real data path, not just on `test` |
| Dashboard / analytics asset | The plant owner who will actually open it — not the DBVE who built it |
| Evaluated use case (`funnel-evaluation`'s output) | Whoever owns the business case being carried into `bc-build` |

## What a failure means, and where it routes

A failure is a **finding**, recorded against the artefact that failed — not a reason to
quietly retry until something passes. This registry already names three rework loops; the
test-structure distinction above decides which one applies:

| Failure | Loop | Record it against |
|---|---|---|
| Hardware/connectivity fails SAT/SIT (Information Integration lane) | Equipment returns for rework; the readiness dimension does not turn "Available" | The machine, in `mi-equipment`'s guidance-protocol |
| A dashboard/analytics asset fails UAT (Project Support lane) | Back to step 3, integration project management | The use case record |
| A use case fails acceptance after handover to integration (Use Case Support lane) | Rework loop back to the integration hand-off | The use case record, with the integration dependency re-opened |

**A partial pass is not a pass.** UAT practice's own entry/exit criteria are explicit: "all
critical scenarios pass, no showstopper defects remain" — a protocol with nine of ten items
passing is nine findings short of done, not 90% accepted. Record which items passed and
which did not; do not average them into a verdict.

## The acceptance / rework rate

This registry already names this as a lane metric with no source system in place yet
(`mi-equipment`'s metrics table) — the fix is procedural, not
technical: every protocol filled from `assets/acceptance-test-protocol.md` (`../assets/acceptance-test-protocol.md`)
already records pass/fail per item and the loop a failure routed into. Counting protocols
by outcome, once enough exist, **is** the source system — nothing further needs building
before the metric can start being collected by hand.
