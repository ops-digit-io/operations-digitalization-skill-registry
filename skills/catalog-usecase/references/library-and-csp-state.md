---
type: Skill Reference
title: Library and CSP state
description: What the vault records today about the reference library and the CSP decision - the counts, the five entries with a recorded Yes by name, and what that does and does not make self-servable. Open it before you tell a plant that something is catalogued.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Library and CSP state

Computed on 2026-11-05 from the frontmatter of the 846 notes in the vault folder `Graph/Use Cases`
(field `use_case_level`, field `csp_decision`). The bundle statement "applied to 51 of the 100 entries,
5 `Yes`, 46 `No`" (`_knowledge/10-Department/Decision rights.md`, bundle as of 2026-08-24) is confirmed by the notes.

## The counts

| Level (`use_case_level`) | Notes | What it is |
|---|---:|---|
| plant use case | 650 | what a plant wants or has |
| reference solution | 122 | 100 library entries (`Reference solution (UseCase-Library)`) plus 22 notes that exist only because of the archive (7 `Reference solution (archive-derived)`, 15 `Use case idea (archive-derived)`) |
| dashboard family | 74 | one note per family of Grafana dashboards that show the same thing |

CSP decision on the 122 reference-solution notes:

| CSP decision recorded | Library entries | Archive-derived notes |
|---|---:|---:|
| `Yes` | 5 | 0 |
| `No` | 46 | 0 |
| no decision recorded in the note | 49 | 22 |

- The CSP field exists **only on library entries**. None of the 650 plant use cases and none of the 74 dashboard families carries it.
  So "catalogued" can only be read at the reference-solution level, and a dashboard family is never catalogued by itself.
- "No decision recorded" is not the same as "decided No". Do not read the 49 as refusals.
- The vault says "the 100-entry library"; the folder holds 122 reference-solution notes. The difference is the 22 archive-derived notes. Use 100 when you speak of the library.

## The five entries with a recorded CSP Yes

All five also record `csp_initiated: Yes`. Source for each row: the library note in `Graph/Use Cases` (SharePoint list `UseCase-Library`, export of 2026-08-21).

| Entry | Plant | Template (as recorded) | OPEX method | Defined standard procedure in the entry | Dashboard family it points to |
|---|---|---|---|---|---|
| Automatic Bending - Cycle Time Analysis | Subotica | Cycle Time | Gemba Management | "Local Gemba Management work instruction" | Bending Cell Dashboards |
| Bending Cell Area - Availability and Shift Output Overview | Subotica | Downtime Reporting | Gemba Management | same | Bending Cell Dashboards |
| Bending Cell - Availability and Hourly Output Dashboard | Subotica | Downtime Reporting | Gemba Management | same | Bending Cell Dashboards |
| Plant Assembly Report | Monterrey | Analytics | Gemba Management | not recorded | Hourly Production per Line |
| Production Panel for Assembly Lines | Monterrey | Andon Board | Gemba Management | not recorded | Hourly Production per Line; Test Bench Hourly Output and Database |

What the five say about the catalog today:

- They come from **two plants** (three Subotica entries from one bending-cell family, two Monterrey entries from the assembly lines) and cover **four of the eleven templates**:
  Cycle Time (1), Downtime Reporting (2), Analytics (1), Andon Board (1). Seven templates have no entry with a recorded Yes: OEE Calculation, Machine Alerts, Process Values, Process Quality Data, Manual Quality Data, Recipe Values, Other Use Cases.
- Per template the library holds: Andon Board 1 Yes / 9 No, Cycle Time 1 / 4, Downtime Reporting 2 / 5, Analytics 1 / 7, Machine Alerts 0 / 3, OEE Calculation 0 / 4, Process Quality Data 0 / 3, Process Values 0 / 6, Manual Quality Data 0 / 1, Other Use Cases 0 / 4 (computed; archive-derived notes carry no decision and are left out). Recipe Values has no reference solution at all.
- The entries describe the screen and the purpose (for example, hour-by-hour output against the daily target with colour flags where throughput fell short of takt). Two entries say how it was implemented only as the next step ("add 9 more lines", "add current machines"), not as a procedure.
- Documentation gaps recorded on the entries themselves: estimated impact not recorded (the three Subotica entries); standard procedure not recorded (Plant Assembly Report); standard procedure and capability link not recorded (Production Panel for Assembly Lines).
- Each of the five has a savings-estimate field filled in with no currency stated. Treat it as an unaudited entry, never as a saving (`od-benefit-calculation`).

## Do the five meet the four conditions of "catalogued"?

The SKILL.md lists four conditions. Against the vault:

| Condition | Status for the five |
|---|---|
| 1 CSP Yes recorded | met, per the table above |
| 2 maps to one of the eleven templates | met, a template is recorded for each (recorded in the graph, not curated) |
| 3 signals standardized (`od-signal-standardization`) | not recorded in any entry - ⟨whether the signals behind the five are standardized⟩ (IIAE) |
| 4 plant owner and a handover that passed the three-question test | not recorded in the library entries - ⟨plant owner and handover record per entry⟩ (plant, DBVE) |

So the vault names the entries that clear the first threshold. It does **not** show that a second plant can take any of them as they are. Until a plant owner and the signals are confirmed, a match to one of the five is a **strong candidate** for branch 1a/1b, not a finished catalog hit.

## What a plant can actually take

- The reusable thing is the **pattern plus the dashboard family** it points to, not a package. The vault records no deployable artefact per entry.
- For a match, open the library note, then the dashboard family note it links (screenshots, panels), then the template page in `Graph/Use Case Views` (see [template-coverage.md](template-coverage.md)).
- For the dashboard build itself the registry has `build-grafana-ops-dashboard` and `od-analytics-asset-build`.

## Pre-screen signals that are not a CSP decision

The plant use cases carry a `scalable` flag: 162 of 650 are `True` (117 of them in status `IMPLEMENTED` or `PRODUCTIVE`). The flag is set by the plant or OD when the use case is recorded; it is **not** a CSP decision and must not be shown as one. It is useful to find the next candidates to put to the CSP decision. Per template see [template-coverage.md](template-coverage.md).

## Open

- ⟨Whether the 49 library entries without a recorded decision are undecided, not applied, or lost in the export⟩ - OD lead.
- ⟨Why only library entries carry the CSP field⟩ and whether a dashboard family can be put through the gate - OD lead.
- ⟨The date and forum of each of the 51 decisions⟩ - not in the notes read; the CSP call (see `od-decision-routing`) would hold them.
