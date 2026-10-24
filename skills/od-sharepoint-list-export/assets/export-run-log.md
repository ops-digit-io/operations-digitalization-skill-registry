---
type: Skill Asset
title: Export run log
description: The defined output of a run - which list, when, how many rows, what the schema check found - so od-portfolio-and-savings-analysis reads a dated, checked export rather than a bare file.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [all, template, protocol]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---

# Export run log — ⟨list name⟩

One entry per run, appended, never overwritten — the history of captures is itself
evidence (it is what lets `od-portfolio-and-savings-analysis` or `od-benefit-calculation`
answer "as of when" for any figure they quote).

| Run date | List | Items | Attachments | Mode | Schema check | Notes |
|---|---|--:|--:|---|---|---|
| ⟨2026-10-22⟩ | ⟨SmartFactory UseCase Savings⟩ | ⟨1143⟩ | ⟨251⟩ | ⟨full / incremental since YYYY-MM-DD⟩ | ⟨OK / columns added: … / columns removed: …⟩ | ⟨anything that needed a second attempt⟩ |

**Mode** is `full` for the first run against a list and every run after a schema-removal
finding (an incremental run cannot be trusted to have seen everything once a column it
might have filtered or branched on has changed shape). Otherwise `incremental since
<checkpoint>`, reading the checkpoint from `<list>.checkpoint.json` per
`references/reliability-discipline.md`.

**Schema check** is `scripts/check_export_schema.py`'s verdict, pasted in, not
re-summarized — a "columns removed" entry here is the signal `od-portfolio-and-savings-analysis`
and `od-benefit-calculation` need to re-check whether a field they depend on still exists
before quoting a figure from this run.

## Hand-off

The file this run produced (`SharePoint-FullExport.json`, landed under
`90-Sources/sharepoint/<list>/` per the export procedure) plus this log's latest row **is**
the input `od-portfolio-and-savings-analysis` reads as "the list" — it should never need to
re-derive the capture date or the row counts from the export file itself; both are already
here.
