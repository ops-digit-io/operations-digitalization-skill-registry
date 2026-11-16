---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Outputs and hand-off: the text before outputs.yaml

`catalog-template` delivers a resolution record for one deliverable: which approved master to start from, where it lives, who owns it and what state the register gives it. It points; it authorises nothing.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Template resolution record | `assets/template-resolution-record.md`, filled and attached to the deliverable | The person producing the deliverable; the skill that asked which template to fill | States the master chosen, its location, its owner, the register's verification date, and one of four outcomes: use the master, use the master and flag its age, master not collected yet (stop and route), or no master exists (route to creation) |
| Register row citation | Source line in the deliverable | Reader of the deliverable | The register row is cited and no placeholder text or sample figure from the master remains (leak check) |
| Route for a missing master | One sentence in the record | Owner role named in the register (DBVE, IIAE, Engineering Standards, OESL IT Digital Platforms); OD lead | When the outcome is "stop" or "route", the sentence names who can supply the master; any draft is labelled draft, not as the template |

## Handoff

- **Receives from:** `dept-intake` or `dept-decision-rights` (an unscoped deliverable is handed back to them); any OD skill that names an artefact to fill, for example `funnel-requirements`, `bc-build`, `metrics-scorecard`, `deploy-handover`.
- **Next in the flow:** Lane 1 step 1a2 (apply template, with `ops-analytics-asset`) and the supporting spine. The record travels with the deliverable to the skill that fills the master. Two conflicting masters go to `dept-decision-rights`.
- **Stops here when:** the register row says `to collect` or `to confirm or create`, the master cannot be opened at its stated location, or two files claim to be the master. Do not substitute a plausible structure and do not decide that a master is approved.

## Kinds of gap to expect (moved from SKILL.md)

- These are patterns, not a status report. Whether a gap is open today is read from the register on the day.
- The use-case one-pager and business-case template has been a gap row (`to confirm or create`, owner role DBVE). While it is a gap, `bc-build` and `funnel-use-case` carry their own protocols and those are the best available, not the approved master.
- Locations of Power BI reports, the data platform portal and the IIoT Edge / MSB portal are often `to confirm` or `to collect`. Owner: IIAE for the platforms, DBVE / OD lead for the reports.
- The Cyber Security sign-off standard belongs to another team; while it is `to collect`, `deploy-cybersec` has no approved master to start from.
- The knowledge base can hold a master-slide file that the register does not list (section C of `references/master-register.md`): whether it is approved, and for which deliverable, is to confirm with the OD lead role.
- Register freshness: check the register's own verification date against the quarterly review cadence; see `dept-context-freshness`.
- Plan item P-06 of the department's skill map is the origin of the rule; the register says: when an agent produces a deliverable "it must start from the approved template and cite the canonical source, not invent one".

## Sources used in the improvement run

- None added; no vault or archive claim was introduced in this run.
