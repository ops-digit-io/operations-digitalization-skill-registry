---
type: Skill Reference
title: Precedents
description: Patterns from the department's own record of Cyber Security approvals - the Groot2B programme, an app that waited on approval, a network-separation case, how application cyber status is recorded, how security shows up in blocker records - so a plant sees how the gate behaved before. Guidance only, no current figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Precedents

Read from the work vault (`Work-OpsDigit-Knowledge`). The ODEC Facts notes are extracts of call
slides and some lines are cut off in the export. This file keeps the patterns and drops dates,
deadlines, counts and current statuses; look those up at the source. Nothing below is a rule: the
rules are in [`gate-rules.md`](gate-rules.md).

## 1. Groot2B - the cybersecurity programme (ODEC Facts - Tools and Systems)

- The call slides carry a standing **call for action**: check the project overview and process flow;
  check the current status and missing factors in the "GROOT2B Direct" Power BI report; contact the
  Operational Digitalization team for the remaining steps or support.
- A later slide records an escalation from the Head of Operations of the business area, a follow-on
  programme with a programme manager who supports IT-Cybersecurity and the network team, and
  monthly reporting through COP calls. Pattern: programme deadlines moved between slides, so never
  quote a programme date from a skill; read the current report.
- Use for the gate: Groot2B carries cybersecurity implementation to the plants and is tracked in COP.
  ⟨How a plant's Groot2B status relates to the sign-off for a new connection⟩ is not in the sources.
- The vault triage note rates these slides low value because most are bare headers; the status
  probably lived in images that did not extract.

## 2. An app that waited on approval (pattern from the QFPR case)

Sources: Graph/Tools QFPR; ODEC Facts - Tools and Systems; ODEC Facts - Plant notes.

- The **cyber-security approval stayed pending for a long time** and was treated as **mandatory before
  any productive rollout**, not only before test instances. The work moved through a
  vulnerability-scan and penetration-test stage with Group IT.
- Slides list the approval as a pending item beside the deployment documentation.
- Use for the gate: an app can run test instances while the approval is open; go-live cannot. Start
  the package when the app is first described, not when it is finished. Read the current approval
  state from the app's own record.

## 3. A plant case - network separation and a tool assessment (pattern)

A use-case workshop result for one plant listed IT/OT network separation as done and a Cyber
Security assessment for a specific tool as still to be followed up. Use for the gate: a plant-level
network fact (separation done) belongs in the package's network-position row; a tool that has not
been assessed is its own open item.

## 4. Legacy applications - how cyber status is recorded (Graph/Legacy Applications)

The legacy-application notes carry these fields; read them on the live notes, do not quote
distributions:

| Field | How to read it |
|---|---|
| Cyber Security Status | Values such as "Not started", "NA - Standalone", or no value. A blank is not a finding; "Not started" is the common value. Count live before quoting a share |
| Network Status | Standalone, IT, OT/IT, OT; tells which network a sign-off would have to cover |
| Production Criticality | Critical, Moderate, Minimal, NA; orders the work |

Use for the gate: the department already has a place for "cybersecurity status" on applications; the
ODEC slide on the Shopfloor Application List names it among the key inputs, with production
criticality, customer impact and service concept. Machines have the same field; check on the live
Machine List whether it is filled. The legacy-application notes also cite two standards by name,
ISA/IEC 62443 and NIST SP 800-82, as OT security references. They are reference material in the
vault, not a recorded department requirement.

## 5. Security in blocker records

In the use-case Blocker Register, keyword themes such as "IT security and approvals" and "Network and
IT infrastructure" can be counted live (filter the register's blocker text). The themes are
keyword-inferred and unreviewed. Use for the gate: plants rarely write security down as the blocker.
That is not evidence that security is rarely the real wait.

## 6. The two-path model from the historical ODEC record (cited in `od-decision-routing`)

Cybersecurity appeared as a strategy item in past ODEC material (a historical forum and source of information) with a two-path decision model: substitute the
solution, or approve it and manage it externally. Use for a refusal: name which path the case takes,
and take it to the deciding role or forum named in the current approval policy (look up) when it changes a standard.

## 7. What the platform's operations concept adds (Graph/Tools Concept 3)

The operations-concept deck summarised in the vault defines roles (Local Key User, BA/BU Key User,
Governance Board, Central Key User, Divisional Engineering Support, Divisional IT, Local IT, platform
service provider) and has security-incident-management process flows. It states that interfaces
between a divisional-standard application and a local application need governance-board approval.
The vault note does not tie this to the Cyber Security sign-off: ⟨whether the governance board
approval and the sign-off are one step or two⟩.
