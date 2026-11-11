---
type: Skill Reference
title: Outputs
description: The outputs metrics-scorecard must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`metrics-scorecard` delivers one filled scorecard update per cycle: refreshed metrics with read dates, the regional breakout and the honest headline, ready to hand to the round or the requester. It is not a summary reconstructed afterwards.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Scorecard update protocol | `assets/scorecard-update-protocol.md`, filled once per cycle | The round (COP or a round held on request) or the requester; OD lead | Every metric refreshed from its authoritative source with a read date; compared against target-to-date; the round-ready regional breakout and headline are present |
| Intervention flags | Section of the protocol | Lane owner named per metric (DBVE for use-case metrics, IIAE for equipment metrics); OD lead | Every metric past its intervene-from threshold is flagged with the lane owner named |
| Round output and the one retro change | Section of the protocol, recorded after the round | OD lead | The round's output is recorded; the retro produced exactly one decided adjustment, not a list |
| Open gaps carried forward | Section of the protocol | OD lead; next cycle's protocol | Every metric without a source is marked ⟨to collect⟩; unresolved items are labelled as carried into the next round |

## Handoff

- **Also receives from:** `dept-plant-diagnosis`: Plant roadmap; Regional roadmap.
- **Receives from:** `deploy-handover` (adoption and utilization findings), `bc-portfolio` (savings roll-up), `dept-context` (department context).
- **Next in the flow:** supporting spine, no fixed downstream step. The protocol goes to the round or the requester; an item unresolved at one round escalates into the next, and where no round is scheduled it goes to the OD lead directly.
- **Stops here when:** a figure has no read date or source, the two reports disagree and only the favourable one would be used, or a target is still ⟨to confirm⟩. Do not publish; refetch, state the Scorecard figure and the filter of the other source, or mark the gap.
