---
type: Skill Reference
title: Export procedure
description: The runnable browser-console REST procedure for a full list export — items, version history, attachment metadata and binaries — verbatim from the proven playbook.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [all, sharepoint, export]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Export procedure

Verbatim from the proven playbook (`ops-knowledge-graph/_knowledge/90-Sources/sharepoint-export-playbook.md`),
run from the browser's own DevTools console while authenticated on the list's site — no
PowerShell, no PnP module, no tenant admin rights. Change only `LIST` and `SITE`; everything
else is identical across every list this applies to.

## 1 · Verify REST access

```javascript
fetch(
  "/teams/team_10055741/_api/web/lists/getbytitle('SmartFactory UseCase Savings')?$select=Title",
  { headers: { "Accept": "application/json;odata=nometadata" } }
)
.then(r => r.json())
.then(console.log)
.catch(console.error);
```

Expect `{"Title":"SmartFactory UseCase Savings"}`. If that comes back, REST access works
with nothing more than the session already open in the browser.

## 2 · Export items + versions + attachments in one pass

```javascript
(async () => {
  const LIST = "SmartFactory UseCase Savings";
  const SITE = "/teams/team_10055741";

  async function getAll(url) {
    let result = [], next = url;
    while (next) {
      const r = await fetch(next, { headers: { "Accept": "application/json;odata=nometadata" } });
      const j = await r.json();
      result.push(...j.value);
      next = j["@odata.nextLink"];
      console.log("Loaded:", result.length);
    }
    return result;
  }

  const items = await getAll(`${SITE}/_api/web/lists/getbytitle('${LIST}')/items?$top=5000`);
  const exportData = [];

  for (const item of items) {
    let versions = [], attachments = [];
    try {
      versions = await getAll(`${SITE}/_api/web/lists/getbytitle('${LIST}')/items(${item.Id})/versions?$top=5000`);
    } catch (ex) { console.error("Version error", item.Id); }
    try {
      attachments = await getAll(`${SITE}/_api/web/lists/getbytitle('${LIST}')/items(${item.Id})/AttachmentFiles`);
    } catch (ex) { console.error("Attachment error", item.Id); }
    exportData.push({ Item: item, Versions: versions, Attachments: attachments });
  }

  const blob = new Blob([JSON.stringify(
    { ExportDate: new Date().toISOString(), ItemCount: items.length, Data: exportData },
    null, 2
  )], { type: "application/json" });

  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "SharePoint-FullExport.json";
  a.click();
})();
```

`@odata.nextLink` drives every `getAll` call — this is what makes the 5000-row page size
safe on a list with far more than 5000 items (the proven scenario has 1,143; several of the
other seven lists are smaller, none are known to exceed the threshold yet). The export file
carries its own `ExportDate` and `ItemCount` — never rename or re-date the file by hand;
those two fields are the record, not the filename.

## 3 · Download every attachment, once items are exported

Reload the export file into the console (`window.exportData = JSON.parse(...)` via a file
picker), build the flat file list, then fetch and download each one:

```javascript
(async () => {
  for (let i = 0; i < window.__files.length; i++) {
    const f = window.__files[i];
    try {
      const response = await fetch(f.url);
      if (!response.ok) { console.error("Failed", f.fileName); continue; }
      const blob = await response.blob();
      const a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = f.fileName;
      a.click();
      await new Promise(r => setTimeout(r, 500));
    } catch (ex) { console.error(f.fileName, ex); }
  }
  console.log("DONE");
})();
```

The 500 ms pause between downloads is load-bearing, not decoration — without it the browser
drops most of the `click()`-triggered downloads silently on a list with more than a handful
of attachments.

## REST endpoints used

| Endpoint | Returns |
|---|---|
| `/_api/web/lists/getbytitle('LIST')` | List metadata |
| `/_api/web/lists/getbytitle('LIST')/items` | Current items |
| `/_api/web/lists/getbytitle('LIST')/items(ID)` | One item |
| `/_api/web/lists/getbytitle('LIST')/items(ID)/versions` | That item's version history |
| `/_api/web/lists/getbytitle('LIST')/items(ID)/AttachmentFiles` | That item's attachments |

## What this route cannot reach

Deleted attachment binaries · recycle-bin contents · audit-log history · historical
versions of attachment files · permissions history. These are stated here, not discovered
later — if an analysis depends on any of them, it needs a different route (tenant-admin
tooling), not a harder attempt at this one.
