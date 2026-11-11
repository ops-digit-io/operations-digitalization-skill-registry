---
type: Skill Reference
title: Outputs
description: The outputs od-context-freshness must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-context-freshness` delivers a dated hygiene report on how current the context behind the other skills is. It repairs nothing. The skill is not done until every finding has an owner and an action.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Hygiene report | `assets/hygiene-report.md`, with the script's tables pasted in | OD lead (bundle files), registry owner (skills and registry marks) | Dated; the exact command line and thresholds recorded; bundle, skills, cross and registry-mark tables included |
| Findings with owner and action | Decision per finding in the report | OD lead, registry owner | Every finding has an owner and an action per the decision table; nothing was edited to make a date look newer |
| Manual-check results | Section of the report | Registry owner | Figure-finder hits, the comparison of the bundle README open-gap list with `open_gaps` in `registry.yaml`, and the dates of knowledge notes relied on are recorded |

## Handoff

- **Receives from:** `od-context` (the sources and dates it points to) and the registry files read by the script. `od-ai-generation-playbook` calls this skill when a stale source must stop an agent.
- **Next in the flow:** bundle-file findings go to the OD lead; skill and registry-mark findings go to the registry owner. They decide and repair; no downstream skill takes the report. The skill sits on the spine, not on one step of `docs/new-state/process.yaml`.
- **Stops here when:** a finding would have to be cleared by editing `last-verified`, `valid-until`, `sources_read` or an `*_as_of` value, or by marking something verified on the script's say-so alone. Report; do not fix in the same pass.
