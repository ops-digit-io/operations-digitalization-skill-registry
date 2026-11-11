---
type: Skill Reference
title: Library and CSP state
description: Guidance, no figures - how to read the reference library and the CSP decision in the knowledge base, how to find the entries with a recorded Yes live, and what that does and does not make self-servable. Open it before you tell a plant that something is catalogued.
resource: ../SKILL.md
status: draft
tags: [all, practice]
---
# Library and CSP state

This file holds **no counts and names no entry**. The state of the library and of the CSP decisions changes; read it live
from the frontmatter of the notes in the knowledge base folder `Graph/Use Cases` (fields `use_case_level`, `csp_decision`,
`csp_initiated`) and from the bundle statement in `_knowledge/10-Department/Decision rights.md` (check its date). Say which
list and date a statement comes from.

## How to read the levels

| Level (`use_case_level`) | What it is |
|---|---|
| plant use case | what a plant wants or has |
| reference solution | a library entry (`Reference solution (UseCase-Library)`), plus a few notes that exist only because of the archive (`Reference solution (archive-derived)`, `Use case idea (archive-derived)`) |
| dashboard family | one note per family of Grafana dashboards that show the same thing |

To count the library live: filter `use_case_level` to the library reference solutions and group by `csp_decision`
(`Yes`, `No`, empty). Archive-derived notes carry no decision and are left out.

Traps:

- The CSP field exists **only on library entries**. Plant use cases and dashboard families do not carry it. So "catalogued"
  can only be read at the reference-solution level, and a dashboard family is never catalogued by itself.
- "No decision recorded" is not the same as "decided No". Do not read blanks as refusals.
- The knowledge base speaks of "the library" with a round number of entries; the folder holds more reference-solution notes than that
  because of the archive-derived ones. Speak of the library entries only, and re-count.
- The library entries are derived from the SharePoint list `UseCase-Library`; the export date matters, state it.

## How to find the entries with a recorded CSP Yes

Filter library entries to `csp_decision: Yes`. For each, read: plant, template as recorded, OPEX method, the "defined standard
procedure" field, the dashboard family it points to, and the documentation gaps recorded on the entry itself (estimated impact
not recorded, standard procedure not recorded, capability link not recorded). Then read:

- which plants and templates the `Yes` entries cover (typically few plants and a minority of the templates; check which
  templates have no `Yes` entry, because a request in such a template falls through to Lane 2);
- whether the entry describes the screen and purpose only, or also a procedure (an entry that only says "add more lines" as
  the next step does not hold a procedure);
- the savings-estimate field: it can be filled in with no currency stated. Treat it as an unaudited entry, never as a saving
  (`bc-build`).

## Do the entries meet the four conditions of "catalogued"?

The SKILL.md lists four conditions. Against what the knowledge base records:

| Condition | Where to check |
|---|---|
| 1 CSP Yes recorded | the entry's `csp_decision` |
| 2 maps to one of the eleven templates | the template recorded on the entry (recorded in the graph, not curated) |
| 3 signals standardized (`mi-signals`) | typically not recorded in the entry - ⟨whether the signals behind the entry are standardized⟩ (IIAE) |
| 4 plant owner and a handover that passed the three-question test | typically not recorded in the library entry - ⟨plant owner and handover record per entry⟩ (plant, DBVE) |

So the knowledge base can name the entries that clear the first threshold. It does **not** show that a second plant can take any of
them as they are. Until a plant owner and the signals are confirmed, a match to a `Yes` entry is a **strong candidate** for
branch 1a/1b, not a finished catalog hit.

## What a plant can actually take

- The reusable thing is the **pattern plus the dashboard family** it points to, not a package. The knowledge base records no
  deployable artefact per entry.
- For a match, open the library note, then the dashboard family note it links (screenshots, panels), then the template page
  in `Graph/Use Case Views` (see `template-coverage.md`).
- For the dashboard build itself the registry has `ops-dashboard-engine` and `ops-analytics-asset`.

## Pre-screen signals that are not a CSP decision

Plant use cases carry a `scalable` flag. It is set by the plant or OD when the use case is recorded; it is **not** a CSP
decision and must not be shown as one. It is useful to find the next candidates to put to the CSP decision: filter `scalable`
and status `IMPLEMENTED` or `PRODUCTIVE`, per template (see `template-coverage.md`).

## Open

- ⟨Whether library entries without a recorded decision are undecided, not applied, or lost in the export⟩ - OD lead.
- ⟨Why only library entries carry the CSP field⟩ and whether a dashboard family can be put through the gate - OD lead.
- ⟨The date and forum of each CSP decision⟩ - not in the notes read; the CSP call (see `dept-decision-rights`) would hold them.
