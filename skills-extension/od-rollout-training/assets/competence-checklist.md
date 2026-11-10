---
type: Skill Asset
title: Competence checklist
description: The plant competence checklist for one solution - observable competences by role, the module and source behind each, the evidence tier, and an empty confirmation field the plant owner fills; the assistant never confirms.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [project-support-consultancy, practice, template]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Competence checklist - ⟨plant⟩ · ⟨solution⟩

Drafted by the assistant. **Confirmation fields are filled by the plant owner (by role), never by the assistant.**
Strike rows that do not apply to this solution; do not add a row without naming where its content lives. "Critical"
rows must be confirmed for at least two people (see
[`../references/competence-and-sustainment.md`](../references/competence-and-sustainment.md), section 3).

Evidence tiers: **1** system record, **2** the plant owner's dated statement, **3** third-party observation.

| # | Competence (what the person does) | Role | Module | Critical | Content held in |
|---|---|---|---|---|---|
| C1 | States which lane a request belongs to and who decides it | PO, KU | M0 | no | `od-decision-routing` |
| C2 | Says what decision the delivered use case supports and in which ritual it is used | SL, PO | M1 | yes | `od-handover-and-adoption` (Q1) |
| C3 | Acts correctly on a deviation shown on the screen (the agreed Andon or shift-check step) | SL | M1 | yes | the plant's use-case record |
| C4 | Traces the data path from screen to machine and names the link that broke | KU, ME | M2 | yes | `od-handover-and-adoption` (Q2); `iiot-edge-platform.md` |
| C5 | Says which layer is plant-local (Grafana) and which is global (data platform) | KU, ME, IT | M2 | no | registry open gaps; `dept-os` |
| C6 | Fills the machine integration guidance protocol for one machine without OD help | ME | M3 | yes | `mi-connector` |
| C7 | Names what is installed at the plant and which route is therefore available | ME, IT | M3 | no | guidance protocol Gate 0 |
| C8 | Classifies a blocked machine into a barrier class and says where it is routed | ME | M3 | no | `barrier-classes.md` |
| C9 | Changes or fixes one element of the plant's own dashboard or flow and has it reviewed | ME, KU | M4 | no | `ops-dashboard-engine`; Node-RED skills |
| C10 | Names the gate an action hits and fills a decision request instead of proceeding | ME, IT, KU, PO | M5 | yes | `od-decision-routing` |
| C11 | States that a machine is not connected, and an external connection not made, before Cyber Security answers | ME, IT, PO | M5 | yes | `od-cybersec-gate` |
| C12 | Acts as the witness at an acceptance item and writes the evidence line | PO, KU | M6 | yes | `od-acceptance-test` |
| C13 | Records adoption evidence at the strongest tier available, without upgrading it | PO | M6 | no | `evidence-of-adoption.md` |
| C14 | Brings a technical item to COP with the facts it needs | KU, PO | M7 | no | `od-decision-routing` (escalation) |
| C15 | Reads the utilization rate and says when it triggers an escalation | PO | M7 | no | `od-scorecard-reporting` |

## Confirmation

One block per person, copied as needed.

| Field | Entry |
|---|---|
| Person (role, not name) | ⟨⟩ |
| Competences confirmed (C numbers) | ⟨⟩ |
| Evidence tier and where kept, per competence | ⟨⟩ |
| Confirmed by (plant owner role) | ⟨⟩ |
| Date | ⟨⟩ |
| Re-confirm by / trigger | ⟨⟩ |

## Coverage check (fill after all blocks)

| Critical competence | People confirmed (count) | Two or more? |
|---|---|---|
| C2 | ⟨⟩ | ⟨yes / no - single point of failure⟩ |
| C3 | ⟨⟩ | ⟨⟩ |
| C4 | ⟨⟩ | ⟨⟩ |
| C6 | ⟨⟩ | ⟨⟩ |
| C10 | ⟨⟩ | ⟨⟩ |
| C11 | ⟨⟩ | ⟨⟩ |
| C12 | ⟨⟩ | ⟨⟩ |

A "no" is reported to the OD lead through COP. It does not block the use case from running; it blocks writing
"adopted" next to it.
