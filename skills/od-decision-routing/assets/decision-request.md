---
type: Skill Asset
title: Decision request
description: The defined output of routing one decision - owner, mode, threshold and gate read off the table, recorded as a dependency, so the thing the decision is about can cite that its gate was cleared.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [all, template, protocol]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Decision request — ⟨decision, one line⟩

Copy once per decision that needs routing. Fill as the routing happens, not afterward.

| | |
|---|---|
| **What is being decided** | ⟨one line — not the background, the actual ask⟩ |
| **Attached to** | ⟨use case / saving row / equipment / rollout this decision is about⟩ |
| **Requester / date** | ⟨name⟩ · ⟨date⟩ |

## 1 · Which row or gate this is

⟨Name the exact row from `SKILL.md`'s decision-rights table, or the exact outside gate
(spend / IT-platform demand / CSP / plant adoption / SPRINT). If neither fits, stop —
this is not yet a decision this skill can route; escalate the gap itself instead of
forcing a row.⟩

## 2 · Read off the table

| Field | Value |
|---|---|
| Owner | ⟨role⟩ |
| Together with | ⟨counterpart, or — ⟩ |
| Mode | ⟨Tandem / Consultation / Information⟩ |
| Approval required | ⟨yes / no⟩ |
| Reversible | ⟨yes / no / partially⟩ |
| Threshold | ⟨exact wording from the table⟩ |
| `authority_level` | ⟨read-only / draft / recommend / execute-with-approval / execute-autonomously⟩ |

## 3 · Route and record

- **If the required level is above the requester's own:** produce the recommendation as-is
  and route it — do not narrow the ask to fit a lower level.
- **Record the gate as a dependency** on the use case or saving row this decision attaches
  to (field name: `Dependency`, per `od-benefit-calculation`), naming this decision and its
  owner — not left as a silent blocker.

## 4 · Outcome

| | |
|---|---|
| **Decided by** | ⟨name, role⟩ · ⟨date⟩ |
| **Outcome** | ⟨approved / declined / deferred, and to what⟩ |
| **If escalated** | ⟨ODEC / COP⟩ · raised ⟨date⟩ · window: one round (unresolved at one cycle escalates to the next) |

A decision request with no row 4 is still open — do not let it read as closed because
someone stopped updating it.
