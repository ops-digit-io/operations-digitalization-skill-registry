---
type: Skill Reference
title: Outputs
description: The outputs od-template-resolution must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-template-resolution` delivers a resolution record for one deliverable: which approved master to start from, where it lives, who owns it and what state the register gives it. It points; it authorises nothing.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Template resolution record | `assets/template-resolution-record.md`, filled and attached to the deliverable | The person producing the deliverable; the skill that asked which template to fill | States the master chosen, its location, its owner, the register's verification date, and one of four outcomes: use the master, use the master and flag its age, master not collected yet (stop and route), or no master exists (route to creation) |
| Register row citation | Source line in the deliverable | Reader of the deliverable | The register row is cited and no placeholder text or sample figure from the master remains (leak check) |
| Route for a missing master | One sentence in the record | Owner role named in the register (DBVE, IIAE, Engineering Standards, OESL IT Digital Platforms); OD lead | When the outcome is "stop" or "route", the sentence names who can supply the master; any draft is labelled draft, not as the template |

## Handoff

- **Receives from:** `od-use-case-intake-triage` or `od-decision-routing` (an unscoped deliverable is handed back to them); any OD skill that names an artefact to fill, for example `od-requirements-breakdown`, `od-benefit-calculation`, `od-scorecard-reporting`, `od-handover-and-adoption`.
- **Next in the flow:** Lane 1 step 1a2 (apply template, with `od-analytics-asset-build`) and the supporting spine. The record travels with the deliverable to the skill that fills the master. Two conflicting masters go to `od-decision-routing`.
- **Stops here when:** the register row says `to collect` or `to confirm or create`, the master cannot be opened at its stated location, or two files claim to be the master. Do not substitute a plausible structure and do not decide that a master is approved.
