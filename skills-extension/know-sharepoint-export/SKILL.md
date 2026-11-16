---
name: know-sharepoint-export
description: >-
  Export a full SharePoint Online list (current items, complete version history, attachment
  metadata and binaries) from the browser console with the REST API, no PowerShell, PnP or admin
  rights. Use when OD source data has to leave SharePoint for analysis, portfolio reporting or a
  knowledge-graph refresh, when the rationale, blockers or comments behind a record must be
  recovered from version history, when a recurring export needs incremental runs, a checkpoint or
  a schema-drift check, or when someone asks how the exports behind the analyses were made.
  Read-only on SharePoint. Not for analysing the export (bc-portfolio).
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

## Purpose

- Read `dept-context` first.
- A repeatable way to export a SharePoint Online list in full from the browser console, using nothing but the REST API and an authenticated session.
- **Needs:** an authenticated browser session on the site, and the list name and site path.
- **Does not need:** PowerShell, the PnP module or tenant admin rights. Reason: the export must be runnable by the person who already has access to the list, not by whoever can get a service account.
- Requires Python 3.8+ (standard library only) for `scripts/check_export_schema.py`.

## Inputs and output

- **Input:** list name, site path, an authenticated browser session; for a repeat run, the previous export and its checkpoint.
- **Output:** the export files landed under `90-Sources/sharepoint/<list>/`, a filled [`assets/export-run-log.md`](assets/export-run-log.md) row and the schema-check line.
- [`outputs.yaml`](outputs.yaml) lists required outputs, criteria, checks and sign-offs.
- Lists this applies to: SmartFactory UseCase Savings, UseCase SavingCalculation, UseCase Library, Machine List, Connector Overview, Tool Overview, Legacy Application List, Business Cases (AI at Operations).
- Proven against the SmartFactory UseCase Savings list, which has both item history and attachments.
- Sizes change; read the list's own item count when you export, do not quote a remembered figure.

## Why version history is the point

- Much of the narrative in the portfolio (rationale, blockers, comments) was written during active work and later tidied back to `-`.
- **Exporting versions, not only the current snapshot, is what recovered it.** An export of current items alone silently loses most of the reasoning behind the portfolio.
- The full exports under `90-Sources/sharepoint/` are what every analysis in the bundle is built from, including the knowledge graph and the portfolio analysis.
- Always export versions.

## What it cannot do (state these limits up front)

- Out of reach through this route: deleted attachment binaries, recycle-bin contents, audit-log history, historical versions of attachment files, permissions history.
- If an analysis depends on any of them, it needs a different route, not a harder attempt at this one.

## Procedure

- Copy this checklist and tick it per run:

- [ ] 1. Open the list in an authenticated browser session.
- [ ] 2. Run the steps of `export-procedure` (verify access, export, download attachments); change only `LIST` and `SITE`. Do not re-derive them.
- [ ] 3. First run against a list: full export. Later runs: full again or incremental since the last checkpoint; `reliability-discipline` says which.
- [ ] 4. Verify counts against the list's own item count before using the output.
- [ ] 5. Run the schema check against the previous export (below).
- [ ] 6. Land the export under `90-Sources/sharepoint/<list>/` and add a row to the run log: date, counts, mode, schema-check result.

### Schema check (validation loop)

```text
python3 scripts/check_export_schema.py OLD.json NEW.json
```

- Exit 0 and `OK`: continue. Exit 1: a finding (column removed or checkpoint not advanced); carry it forward in the log, do not re-run and hope.
- Exit 2: bad input (missing or invalid JSON file, wrong argument count); fix the file path or re-export, then run again.
- `--help` prints usage. The script never prompts.
- The run log plus the export file is what `bc-portfolio` reads as "the list"; capture date and row counts must not need deriving again downstream.

## Example

```text
$ python3 scripts/check_export_schema.py old/SharePoint-FullExport.json new/SharePoint-FullExport.json
Items: 120 -> 123 (+3)
ExportDate: 2026-03-01 -> 2026-04-01
Columns added:   ReviewDate

OK

Run log row (fictional values):
| 2026-04-01 | Example Savings List | 123 | 40 | incremental since 2026-03-01 | OK, columns added: ReviewDate | second attempt after a throttled download |
```

## Human gate and AI-agent notes

- **Authority:** read-only on SharePoint. The export is run by the person with list access; the agent prepares, checks and logs.
- **Sign-off:** the OD lead signs the export and run log (`outputs.yaml`).
- Never hand-edit an export; correct the SharePoint list and re-export.
- The agent does not run the browser-console script on a list it has no session for; it gives the person the steps.

## Pitfalls

- **Current items only:** loses the narrative. Always export versions.
- **Hand-edited export:** files under `90-Sources/` are conformant but never hand-edited; correct the list and re-export.
- **Figure without capture date:** do not present a figure from an export without its capture date.
- **Incremental run without schema check:** a column removed since the checkpoint reads as merely absent, not as an error, in every row the incremental filter returns.
- **Stale re-export:** a failed or repeated run can look like success; the check flags an `ExportDate` that did not advance.
- **List view threshold:** the incremental `Modified` filter can hit it; see `reliability-discipline`.
- **`GetListItemChangesSinceToken` by default:** do not. It is the only route that reports deletions, but it returns XML against a POST body, not JSON against a GET.
- Use it only where a deletion is the thing worth knowing (the Machine List, where a machine disappearing is information).

## Definition of done

- Items, version history, attachment metadata and binaries are exported; counts match the list's own item count.
- The schema check ran against the previous export and its result sits in the run log, with any finding carried forward.
- The export is landed under `90-Sources/sharepoint/<list>/`, not hand-edited, and the run log row names date, counts and mode.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/export-procedure.md`](references/export-procedure.md) | You run the export: the browser-console steps to verify access, export items, versions and attachments, and download binaries |
| [`references/reliability-discipline.md`](references/reliability-discipline.md) | The export recurs: incremental `Modified` filter, list-view-threshold trap, checkpointing, schema-drift detection |
| [`references/background.md`](references/background.md) | You need context and rationale; never an instruction |
| [`assets/export-run-log.md`](assets/export-run-log.md) | You record a run: date, counts, mode, schema-check result |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
| [`references/outputs.md`](references/outputs.md) | The output contract in full (generated from outputs.yaml) |
