---
name: od-sharepoint-list-export
description: >-
  Export an OD SharePoint Online list in full — current items, complete item version
  history, attachment metadata and attachment binaries — from the browser console using
  only the REST API and an authenticated session. No PowerShell, no PnP module, no tenant
  admin rights. Use whenever OD source data has to leave SharePoint for analysis, a
  refresh of the knowledge graph or portfolio reporting, when the narrative behind a
  record (rationale, blockers, comments) has to be recovered from version history, or when
  someone asks how the exports underneath the analyses were produced.
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-sharepoint-list-export
  tier: practice
  lane: all
  owner_role: human:jakob.gabriel
  authority_level: read-only on SharePoint
  status: stable
  delivered: 2026-08
  last_verified: 2026-08-24
  requires: [od-context]
  composes: [od-portfolio-and-savings-analysis]
  derived_from:
    - ops-knowledge-graph/_knowledge/20-Done/SharePoint list export procedure.md
    - ops-knowledge-graph/_knowledge/90-Sources/sharepoint-export-playbook.md
    - ops-knowledge-graph/_knowledge/10-Department/Systems of record.md
---

# SharePoint list export

Read `od-context` first.

A repeatable way to export a SharePoint Online list in full — current items, complete item
version history, attachment metadata and attachment binaries — from the browser console,
using nothing but the REST API and an authenticated session.

## What it needs, and what it does not

**Does not need:** PowerShell, the PnP module, or tenant admin rights. That is the point —
the export has to be runnable by the person who already has access to the list, not by
whoever can get a service account provisioned.

**Needs:** an authenticated browser session on the site, and the list name and site path.

## Where the procedure lives

`90-Sources/sharepoint-export-playbook.md` in the `ops-knowledge-graph` bundle, with the
scripts inline and a **generic template at the end** — change the list name and the site
path, everything else stays identical. Do not re-derive the scripts; run the playbook.

## The lists this applies to

SmartFactory UseCase Savings (650 use cases) · UseCase SavingCalculation (553 rows) ·
UseCase Library (100 entries) · Machine List (1,715 machines) · Connector Overview (26) ·
Tool Overview · Legacy Application List (268) · Business Cases (AI at Operations).

Proven against the SmartFactory UseCase Savings list: **1,143 items and 251 attachments**.

## Why version history is the point

A large amount of the narrative in the portfolio — rationale, blockers, comments — was
written during active work and later tidied back to `-`. **Exporting versions rather than
only the current snapshot is what recovered it.** An export of current items alone will
silently lose most of the reasoning behind the portfolio.

Always export versions. The eight full exports under `90-Sources/sharepoint/` are what
every analysis in the bundle is built from, including the knowledge graph itself and the
portfolio analysis.

## What it cannot do — state these limits up front

Out of reach through this route: deleted attachment binaries · recycle-bin contents ·
audit-log history · historical versions of attachment files · permissions history.

These limits are stated in the playbook rather than discovered later. If an analysis
depends on any of them, it needs a different route, not a harder attempt at this one.

## Procedure

1. Open the list in an authenticated browser session.
2. Take the generic template from the end of the playbook; set the list name and site path.
3. Run the items export, then the version-history export, then the attachments export.
4. Verify counts against the list's own item count before using the output.
5. Land the export under `90-Sources/sharepoint/<list>/` and note the capture date — every
   figure derived from it inherits that date.

## Do not

- Do not export current items only.
- Do not hand-edit an export. Files under `90-Sources/` are conformant but never
  hand-edited; correct the SharePoint list and re-export.
- Do not present a figure from an export without its capture date.
