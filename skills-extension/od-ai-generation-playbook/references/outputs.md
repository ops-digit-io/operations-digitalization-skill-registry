---
type: Skill Reference
title: Outputs
description: The outputs od-ai-generation-playbook must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-ai-generation-playbook` delivers, for every step where an AI agent drafts, classifies, generates or checks something, an admitted step card with the evidence trail, the open items and the human gate. It adds no service of its own. The skill is not done until the agent output is cited and a named person owns the gate.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| AI step card | `assets/ai-step-card.md`, filled | Process owner named on the card; the skill of the step | A human has named the process owner, the data source and the review point (no name, no start); the evidence and the human gate are recorded |
| Generated output with evidence | The artefact of the step, with the source rows, entries or documents it rests on and the read date | Reviewer on the card, before anyone outside the team sees it | Every element traces to a source field; an output without citations is labelled a draft |
| Open-item list | List handed over with the output | Reviewer on the card | Open items ("to confirm") sit on the list, not in the artefact |
| Missing-signal and binding table | `assets/missing-signal-and-binding-table.md`, filled (steps 22, 23, 1a2, 3b4) | `od-data-availability-check`, information-integration lane | Missing signals are reported before the dashboard as signal id, label and why needed; the binding table shows which tag fed which panel and which query pattern it uses |

## Handoff

- **Receives from:** `od-context` and `od-context-freshness` (a current, owned context section), `od-template-resolution` (the template, never a copy), the fixed-structure input set of the step.
- **Next in the flow:** the skill of the step that asked for the agent (for example `od-analytics-asset-build`, `od-signal-standardization`, `od-data-availability-check`, `od-system-fit-check`, `od-cybersec-gate`, `deploy-appstore`); a person reviews before the output leaves the team. The skill sits on the spine, not on one step of `docs/new-state/process.yaml`.
- **Stops here when:** the needed context section is stale or has no owner, the process owner, data source or review point is not named, or a signal is missing (never approximated). The agent never invents a value, writes to a machine, approves or submits anything; ranking, go / no-go, Cyber Security sign-off and deployment stay human decisions.
