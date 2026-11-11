---
type: Skill Reference
title: Outputs
description: The outputs od-sharepoint-list-export must deliver, who receives each one, and what makes each complete.
resource: ../SKILL.md
status: draft
tags: [outputs, handoff]
---
# Outputs

`od-sharepoint-list-export` delivers a full export of one SharePoint list (items, version history, attachment metadata and binaries) and a run log that records how it was made. Downstream analysis reads the export and the log as "the list".

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| List export | Files landed under `90-Sources/sharepoint/<list>/` | `od-portfolio-and-savings-analysis` | Items, complete item version history, attachment metadata and attachment binaries are exported (never current items only); counts verified against the list's own item count; not hand-edited |
| Export run log | `assets/export-run-log.md`, filled | `od-portfolio-and-savings-analysis` | Date, counts, mode (full or incremental) and the schema check result are recorded, so capture date and row counts need no re-deriving |
| Schema check result | Line in the run log from `scripts/check_export_schema.py` | `od-portfolio-and-savings-analysis`; OD lead | Result is `OK`, or every finding is carried forward in the log |

## Handoff

- **Receives from:** `od-context` (list name, site path and the department context); an authenticated browser session of the person with access to the list.
- **Next in the flow:** supporting spine, no process step. `od-portfolio-and-savings-analysis` reads the export plus the run log.
- **Stops here when:** counts do not match the list's item count, or the schema check reports a finding before an incremental run. Carry the finding forward; do not re-run and hope, and do not present a figure without its capture date. If an analysis needs deleted binaries, recycle-bin contents, audit-log history, attachment versions or permissions history, this route cannot supply them.
