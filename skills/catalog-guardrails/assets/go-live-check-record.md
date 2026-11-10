---
type: Skill Asset
title: Go-live check record
description: The record a plant fills before it declares a catalogued use case live - the seven seeded guardrails plus the candidate build guardrails, with result, evidence, date and who answered. Copy one per use case.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Go-live check record

```text
Use case:                      Template:                    Catalog match record: (from catalog-usecase, pick)
Plant:                         Plant owner (role):          System match record (1b only):
Date of check:                 Answered by (role):          Reviewed by DBVE?  yes / no
```

Rules for filling: a result is `passed`, `failed` or `not checked`. "Yes" without evidence is `not checked`. A number needs a source and a capture date. Any `failed` or `not checked` in a **block** row means no go-live.

## A - Seeded guardrails (SKILL.md)

| # | Guardrail | Result | Evidence (verdict, source, name of role) | Date |
|---|---|---|---|---|
| G1 | Signals exist and are fresh; verdict names the step reached (1 to 6 of `od-data-availability-check`) | | | |
| G2 | Platform boundary: local Grafana only; global layer not wired in; no cross-plant view on a local instance | | | |
| G3 | Inside the lean footprint (`od-system-fit-check`) | | | |
| G4 | No figure without source and capture date | | | |
| G5 | Named plant owner; the plant decides daily use | | | |
| G6 | Three-question handover test answerable from the record alone | | | |
| G7 | External connection: Cyber Security sign-off (human-only) granted - by whom, when | | | |

## B - Candidate build guardrails (references/technical-guardrails.md; proposals, not yet confirmed)

| # | Check | Setting proposed | Result | Evidence | Date |
|---|---|---|---|---|---|
| G8 | Signals via variable or lookup, no literal UUID in new SQL | warn | | | |
| G9 | No `uuid = ''` binding | block | | | |
| G10 | Queries follow the time picker | block (new dashboards) | | | |
| G11 | Data sources bound by role name; dashboard imports in this plant without editing the JSON | block (new dashboards) | | | |
| G12 | Every panel has title, query, unit | block | | | |
| G13 | Title, folder, tags (status, template, plant), owner role, purpose in description | block for title, folder, tags; warn for the rest | | | |
| G14 | Thresholds and colours readable; a good state is never red | warn | | | |
| G15 | Missing value shown as missing, never 0; age of newest value visible | warn | | | |
| G16 | Refresh and range fit the use | warn | | | |
| G17 | Free-text fields: no names, no automated forwarding | block where a field exists | | | |
| G18 | No write-back to a machine | block | | | |
| G19 | No credentials, sessions or tokens stored beside the script or export | block | | | |

## C - Content check against the template (warn)

Does the screen show what the template's standard says it is for? Take the "belongs here" and the most frequent figures from `catalog-usecase`, `references/template-coverage.md`.

```text
Template: ____    The purpose in one sentence (the "issue solved"): ____
Figures it must show (from the template page; keyword counts, not a KPI definition): ____
Figures this screen shows: ____        Missing: ____        Extra (belongs to another template?): ____
```

## D - After go-live

```text
Utilization expectation written in the record (DAILY / WEEKLY / MONTHLY / ON DEMAND / ONE-TIME):   ____
Moment of use (shift check, Gemba walk, Andon escalation, report):                                   ____
First scorecard review date:                                                                          ____
Adoption evidence tier at that review (od-handover-and-adoption, references/evidence-of-adoption.md): ____
```

## E - Result

```text
Guardrails failed: ____     not checked: ____     Routed to (failed-guardrail table in references/failure-cases-and-routing.md): ____
Final line (always): go-live decision: the plant's.
```
