---
name: know-sharepoint-export
description: >-
  Export an OD SharePoint Online list in full — current items, complete item version
  history, attachment metadata and attachment binaries — from the browser console using
  only the REST API and an authenticated session. No PowerShell, no PnP module, no tenant
  admin rights. Use whenever OD source data has to leave SharePoint for analysis, a
  refresh of the knowledge graph or portfolio reporting, when the narrative behind a
  record (rationale, blockers, comments) has to be recovered from version history, or when
  someone asks how the exports underneath the analyses were produced.
license: MIT
allowed-tools: Read Grep Glob Bash(python3 scripts/check_export_schema.py:*)
metadata:
  id: know-sharepoint-export
  aliases: [od-sharepoint-list-export]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: all
  new_state_lane: "Extension, deepens Spine"
  new_state_step: "Supporting spine"
  owner_role: human:jakob.gabriel
  authority_level: read-only on SharePoint
  status: stable
  delivered: 2026-08
  requires: [dept-context]
  composes: [bc-portfolio]
  okf:
    type: Agent Skill
    title: SharePoint list export
    tags: [all, practice]
---

# SharePoint list export

Read `dept-context` first.

A repeatable way to export a SharePoint Online list in full — current items, complete item
version history, attachment metadata and attachment binaries — from the browser console,
using nothing but the REST API and an authenticated session.

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## What it needs, and what it does not

**Does not need:** PowerShell, the PnP module, or tenant admin rights. That is the point —
the export has to be runnable by the person who already has access to the list, not by
whoever can get a service account provisioned.

**Needs:** an authenticated browser session on the site, and the list name and site path.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/export-procedure.md`](references/export-procedure.md) | The runnable browser-console steps — verify access, export items/versions/attachments, download attachments — change only `LIST` and `SITE` |
| [`references/reliability-discipline.md`](references/reliability-discipline.md) | For a recurring export, not a one-off capture: the incremental `Modified`-filter pattern, the list-view-threshold trap it can walk into, checkpointing so a failed run resumes instead of silently skipping, and schema-drift detection |

Do not re-derive the scripts; run the procedure as given.

## The lists this applies to

SmartFactory UseCase Savings · UseCase SavingCalculation · UseCase Library · Machine List ·
Connector Overview · Tool Overview · Legacy Application List · Business Cases (AI at Operations).

Proven against the SmartFactory UseCase Savings list, which has both item history and attachments.
Sizes change; read the list's own item count when you export, do not quote a remembered figure.

## Why version history is the point

A large amount of the narrative in the portfolio — rationale, blockers, comments — was
written during active work and later tidied back to `-`. **Exporting versions rather than
only the current snapshot is what recovered it.** An export of current items alone will
silently lose most of the reasoning behind the portfolio.

Always export versions. The full exports under `90-Sources/sharepoint/` are what
every analysis in the bundle is built from, including the knowledge graph itself and the
portfolio analysis.

## What it cannot do — state these limits up front

Out of reach through this route: deleted attachment binaries · recycle-bin contents ·
audit-log history · historical versions of attachment files · permissions history.

These limits are stated in the playbook rather than discovered later. If an analysis
depends on any of them, it needs a different route, not a harder attempt at this one.

## Procedure

1. Open the list in an authenticated browser session.
2. Run `references/export-procedure.md`'s steps; set the list name and site path.
3. First run against a list: full export. Every run after: either full again, or
   incremental since the last checkpoint — `references/reliability-discipline.md` says
   which.
4. Verify counts against the list's own item count before using the output.
5. Run `scripts/check_export_schema.py` against the previous export. A clean result is
   `OK`; anything else is a finding to carry forward, not a reason to re-run and hope.
6. Land the export under `90-Sources/sharepoint/<list>/`, and record the run in
   [`assets/export-run-log.md`](assets/export-run-log.md) — date, counts, mode, the schema
   check's result. This log plus the export file is what `bc-portfolio`
   reads as "the list"; neither the capture date nor the row counts should need deriving
   again downstream.

## Do not

- Do not export current items only.
- Do not hand-edit an export. Files under `90-Sources/` are conformant but never
  hand-edited; correct the SharePoint list and re-export.
- Do not present a figure from an export without its capture date.
- Do not run an incremental export without checking the schema first — a column removed
  since the checkpoint reads as merely absent, not as an error, in every row the incremental
  filter returns.
- Do not reach for `GetListItemChangesSinceToken` by default. It is the only route that
  reports deletions, but it returns XML against a POST body, not JSON against a GET — a real
  parsing change from the rest of this procedure. Use it only where a deletion itself is the
  thing worth knowing (the Machine List, where a machine disappearing is information).
