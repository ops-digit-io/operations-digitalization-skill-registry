---
type: Skill Reference
title: Precedents
description: What the department's own record shows about Cyber Security approvals - Groot2B, the QFPR approval, a network-separation case, legacy-application cyber status and blocker counts - so a plant sees how the gate behaved before.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Precedents

Read 2026-11-05 from the work vault (`Work-OpsDigit-Knowledge`). The ODEC Facts notes are extracts of call
slides and some lines are cut off in the export; where a line is cut, this file says so. Nothing below is a rule:
the rules are in [`gate-rules.md`](gate-rules.md).

## 1. Groot2B - the cybersecurity programme (ODEC Facts - Tools and Systems)

- Feb and June 2024 call slides carry the same **call for action**: check the project overview and process flow;
  check the current status and missing factors in the "GROOT2B Direct" Power BI report (meeting invites per
  region); contact the Operational Digitalization team for the remaining steps or support. A step 4 exists and is
  cut off in the export.
- Nov 2024 slide "Cybersecurity - Groot 2 / 3": an escalation from the Head of Operations of the business area;
  the goal is to complete the Groot2B projects in all plants "until Q3"; a Groot3 programme team has a programme
  manager who supports IT-Cybersecurity and the network team; monthly reporting runs through COP calls. A CoP
  slide of Feb 2024 (read for `od-decision-routing`) gave Q2: the deadline moved.
- Use for the gate: Groot2B carries cybersecurity implementation to the plants and is tracked in COP.
  ⟨How a plant's Groot2B status relates to the sign-off for a new connection⟩ is not in the sources.
- The vault triage note rates these slides low value because most are bare headers; the status probably lived
  in images that did not extract.

## 2. QFPR (Quality Feedback and Part Routing) - an app that waited on approval

Sources: Graph/Tools QFPR; ODEC Facts - Tools and Systems; ODEC Facts - Plant - Monterrey.

- Through 2024 the **cyber-security approval was pending** and was treated as **mandatory before any productive
  rollout**, not only before test instances. By December 2024 the work had reached a vulnerability-scan and
  penetration-test stage with Group IT.
- An Aug 2024 slide lists "Cyber Security Application pending" beside the deployment documentation; the later
  project update lists "Cyber Security Approval: Pending, continuous work on features".
- Use for the gate: an app can run test instances while the approval is open; go-live cannot. Start the package
  when the app is first described, not when it is finished.

## 3. A plant case - network separation and a tool assessment (ODEC Facts - Plant - Auburn, 2025-05-21)

The use-case workshop result for one plant lists "Network Separation is done (IT / OT Separation)" and "Cyber
Security Assessment for Ignition to be followed up". Use for the gate: a plant-level network fact (separation done)
belongs in the package's network-position row; a tool that has not been assessed is its own open item.

## 4. Legacy applications - recorded cyber status (Graph/Legacy Applications, 268 notes)

Counted on 2026-11-05 from the field lines of the notes (not audited):

| Field | Values counted |
|---|---|
| Cyber Security Status | Not started 172; NA - Standalone 15; the other 81 carry no value in those lines |
| Network Status | Standalone 94; IT 65; OT/IT 25; OT 21 |
| Production Criticality | Critical 109; NA 61; Moderate 34; Minimal 23 |

Use for the gate: the department already has a place for "cybersecurity status" on applications; the 2025 ODEC
slide on the Shopfloor Application List names it among the key inputs, with production criticality, customer
impact and service concept. Machines have the same field but it is empty on all 1,715 rows. The legacy-application
notes also cite two standards by name, ISA/IEC 62443 and NIST SP 800-82 Rev. 3, as OT security references. They are
reference material in the vault, not a recorded department requirement.

## 5. Blockers in use-case records (Graph/Registers/Blocker Register, SharePoint export of 2026-08-21)

Of 83 blocker texts on 68 use cases, the keyword theme "IT security and approvals" holds **3 texts on 3 use cases
at 3 plants**; "Network and IT infrastructure" holds 6. The themes are keyword-inferred and unreviewed. Use for the
gate: plants rarely write security down as the blocker. That is not evidence that security is rarely the real wait.

## 6. The ODEC two-path model (cited in `od-decision-routing`)

At ODEC #9 (Sept 2024) cybersecurity appeared as a strategy item with a two-path decision model: substitute the
solution, or approve it and manage it externally. Use for a refusal: name which path the case takes, and take it
to ODEC when it changes a standard.

## 7. What the platform's operations concept adds (Graph/Tools Concept 3)

The operations-concept deck summarised in the vault defines roles (Local Key User, BA/BU Key User, Governance
Board, Central Key User, Divisional Engineering Support, Divisional IT, Local IT, platform service provider) and
has security-incident-management process flows. It states that interfaces between a divisional-standard
application and a local application need governance-board approval. The vault note does not tie this to the Cyber
Security sign-off: ⟨whether the governance board approval and the sign-off are one step or two⟩.
