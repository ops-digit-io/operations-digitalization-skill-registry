---
type: Skill Reference
title: Reliability discipline
description: What a full re-export does not give you — an incremental pattern for daily use, the list-view-threshold trap it walks into, schema-drift detection, and the checkpoint a resumed run needs.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [all, sharepoint, export, reliability]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Reliability discipline

The playbook (`references/export-procedure.md`) re-reads every item, every time. That is
correct for a one-off capture and wrong for a recurring export — it gets slower as the list
grows and gives no way to tell "nothing changed" from "the run failed silently."

## Incremental export — filter on `Modified`, don't walk the full list

SharePoint's REST service supports OData filtering on the items endpoint, including the
`Modified` field [R1]:

```javascript
const since = "2026-10-01T00:00:00Z";   // the last successful run's checkpoint
const url = `${SITE}/_api/web/lists/getbytitle('${LIST}')/items` +
            `?$filter=Modified gt datetime'${since}'&$top=5000`;
```

Run the same `getAll` pagination as the full export; only items changed since the
checkpoint come back, so versions and attachments are only re-fetched for rows that could
plausibly have changed.

**A more complete alternative exists and is deliberately not recommended by default.**
SharePoint also exposes `GetListItemChangesSinceToken` [R2], a change-tracking endpoint that
returns every insert, update and *delete* since a token, which is the only way to learn that
an item was removed — a `Modified`-filter query cannot see a deletion. Its cost: it is a
`POST` carrying an `SP.ChangeLogItemQuery` body and returns ADO rowset **XML**, not the JSON
this playbook's `fetch`/`getAll` pattern is built around — a real parsing change, not a
one-line swap. Use the simple `Modified` filter for routine incremental runs; reach for
`GetListItemChangesSinceToken` only when a list's deletions matter to what reads the export
(the Machine List, where a retired machine disappearing is itself information).

**The list-view threshold is the trap waiting in this pattern.** A SharePoint list with more
than 5,000 items throttles any query that filters or sorts on a column without an index,
`Modified` included on a list that large [R3]. None of the eight lists this skill targets is
known to be near that size today (the proven scenario is 1,143 items), but the Machine List
at 1,715 is the one to watch if it keeps growing — index the `Modified` column on any list
approaching 5,000 before relying on the incremental filter.

## Checkpointing — resume without re-reading

Write the checkpoint alongside the export, not inside it: a small sidecar,
`<list>.checkpoint.json`, holding the previous run's `ExportDate` and `ItemCount`. The next
run's `since` value is the prior `ExportDate`; a failed run that never wrote a new export
leaves the old checkpoint in place, so a retry naturally re-covers the gap instead of
silently skipping it. `scripts/check_export_schema.py` reads this sidecar alongside the
export to report both the item-count delta and whether the checkpoint actually advanced.

## Schema drift — a renamed or removed column breaks downstream silently

Nothing in the export procedure fails if a column `od-portfolio-and-savings-analysis` or
`od-benefit-calculation` reads is renamed or removed in SharePoint — the JSON simply stops
carrying that key, and every downstream read of it reads as an absent field rather than an
error. That is exactly the failure mode `od-portfolio-and-savings-analysis` already warns
about generally ("absence read as a zero") — a schema change makes it happen at the source,
not just in interpretation.

`scripts/check_export_schema.py` compares the key set of the first item between two export
runs and reports additions, removals and renames-that-look-like-an-add-plus-a-remove. Run it
every time, not only when something looks wrong — the whole point is catching the silent
case.

## Sources

- [R1] ShortPoint (vendor documentation, tier 4), *REST API: Selecting, Filtering, Sorting
  Results in a SharePoint List* — `$filter=Modified gt datetime'...'` syntax and the
  `gt`/`ge` operators.
  https://www.shortpoint.com/support/shortpoint-rest-api-selecting-filtering-sorting-results-in-a-sharepoint-list.
  Retrieved 2026-10-22. Not Microsoft documentation; the syntax matches the official OData
  conventions in R2/R3 but treat this one specifically as vendor-reported.
- [R2] Microsoft Learn, *Synchronize SharePoint items using the REST service* —
  `GetListItemChangesSinceToken`, its `POST` + `SP.ChangeLogItemQuery` shape, the ADO
  rowset XML response, and that it is the only route that reports deletions.
  https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/synchronize-sharepoint-items-using-the-rest-service.
  Retrieved 2026-10-22.
- [R3] Microsoft Learn / community guidance on the SharePoint list-view threshold (5,000
  items) and its effect on filtered or sorted queries over unindexed columns — referenced
  via *REST API Filter by Modified date ThrottledException*,
  https://learn.microsoft.com/en-us/answers/a/1367813. Retrieved 2026-10-22.
