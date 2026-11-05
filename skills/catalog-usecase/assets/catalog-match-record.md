---
type: Skill Asset
title: Catalog match record
description: The blank record a plant fills when it matches a request to a catalogued use case, with one worked example built from a real library entry. Copy it per request.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Catalog match record

Fill one per request. Every field needs a source or the words "not checked". "Yes" without a source counts as "not checked".

```text
Request (one sentence, the plant's words):
Plant / plant owner (role):
Date:

1  TEMPLATE
   Template (one of the eleven):          Rule that placed it (R1-R13, R12 order):
   Boundary check - what the request is NOT (see references/template-coverage.md):

2  CANDIDATE ENTRY
   Library entry (title, plant):          Dashboard family it points to:
   CSP decision:   Yes / No / none recorded     Source: library note, SharePoint list UseCase-Library
   Peer plant that runs the template (delivered):
   Documentation gaps on the entry (as recorded):

3  CONDITIONS FOR "CATALOGUED"
   a CSP Yes recorded:                          met / not met
   b maps to a template:                        met / not met
   c signals standardized (od-signal-standardization):   met / not met / not checked
   d plant owner + handover passed three-question test:   met / not met / not checked

4  PRECONDITIONS AT THIS PLANT (od-data-availability-check)
   Target types needed (template-coverage.md):      
   Machine(s) / controller:                          Integration status (Machine List):  INTEGRATED / NOT INTEGRATED / no status recorded
   Signals present and fresh:                        Verdict step reached: 1-6

5  FOOTPRINT
   Systems needed:                                   Inside lean footprint?  yes / no -> od-system-fit-check

6  BRANCH AND NEXT SKILL
   1a connected  -> od-analytics-asset-build (dashboard) / build-grafana-ops-dashboard
   1b not connected -> catalog-systems
   falls through -> Lane 2 (od-use-case-definition) or Lane 3 (od-system-fit-check)
   Reason for the branch:

7  OPEN POINTS (each with an owner role)
```

A blank in "integration status" is not a "No": 451 of 1,715 machines carry no status (`od-data-availability-check`). Ask the IIAE.

## Worked example (illustrative - the request is invented to show the steps; the entry is real)

*A plant asks for "an hour-by-hour output board for one assembly line, with a colour flag when an hour misses target".*

| Field | Entry |
|---|---|
| Template | Andon Board. Rule R2 (a board that shows output against target, hourly output). Not Machine Alerts (no message to people), not Analytics (live, one line) |
| Candidate entry | "Production Panel for Assembly Lines", Monterrey; family "Hourly Production per Line" |
| CSP decision | Yes (recorded; `references/library-and-csp-state.md`) |
| Peer plants running Andon Board (delivered) | 20 plants, listed in `references/template-coverage.md`; the entry's own plant is Monterrey |
| Documentation gaps on the entry | standard procedure and capability link not recorded |
| Conditions | a met; b met; c ⟨not recorded for this entry⟩; d ⟨plant owner and handover not recorded in the library entry⟩ |
| Target types needed | Andon Board, Machine Availability, Cycle Time Monitoring (template page); a count of OK parts per hour is what the entry's purpose text describes |
| Machine and signals | ⟨to be read from the Machine List and the data check at the requesting plant⟩ |
| Branch | decided by the machine: integrated and signals present - 1a; not integrated - 1b (`catalog-systems`); no matching signal - Lane 2 |
| Open | c and d for the entry (IIAE, plant owner); who at Monterrey can walk the requesting plant through the screen (DBVE) |

The example stops where the vault stops: the entry is a strong candidate, and the two conditions that make it a catalog hit are not on record.
