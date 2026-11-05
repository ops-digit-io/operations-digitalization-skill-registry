---
type: Skill Reference
title: Technical guardrails
description: Candidate guardrails G8 to G18 for a self-served dashboard, each with its recorded source rule, the failure pattern it prevents (no counts) and a proposed block-or-warn setting. Open it when the seven seeded guardrails are not enough for the screen a plant has built.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Technical guardrails

The seven guardrails in `SKILL.md` (G1 to G7) cover data, platform boundary, footprint, figures, ownership, handover and Cyber Security. A plant that builds or copies a dashboard needs more: how the screen reads data, how it is built, what it shows. The vault holds these as **proposed specifications**, not as adopted rules. Treat every row below as a **candidate** that the OD lead has not yet confirmed. This file holds no counts of the Grafana estate; the specs carry them and they move.

## Where they come from and how far to trust them

Vault folder `Dashboard Exports/specs`, all AI-drafted from the Grafana JSON exports of the plant locations and marked "Draft for review":

- SPEC-02 Telemetry Data Contract: requirements D-01 to D-10 (proposals "inferred from the problems P1 to P7; none is a statement of current practice").
- SPEC-03 Dashboard Authoring Standard: rules S-01 to S-19, each with the number of dashboards that break it at the time of the export. Thresholds are proposals; the counts are facts from that export. Re-run the check on a fresh export before quoting one.
- SPEC-04 Dashboard Families and Central Provisioning: classes A to D and requirements F-01 to F-08.
- A plant-level requirements note (a KKA / Pulp Mixer dashboard): the one worked example of a dashboard-level requirement set, reverse-engineered from an existing implementation.

None of these says "a plant must not go live unless...". The block-or-warn setting below is derived from SPEC-03 section 6, which names the rules that every **new** dashboard must pass after adoption (S-01 to S-03, S-06, S-07, S-10, S-15, S-17). Everything else is "warn" in this table. ⟨Which guardrails block and which only warn⟩ remains the OD lead's decision.

## The candidates

| # | Guardrail (plain words) | Source rule | Failure pattern it prevents | Proposed |
|---|---|---|---|---|
| G8 | **Signals are not bound by a literal UUID typed into the SQL.** A new screen takes signals through a variable or a lookup on the signal record | SPEC-02 D-02, S-11 | Literal UUID predicates are widespread; a re-created device or datapoint breaks every dashboard holding the old UUID, and a copy to another plant carries the wrong ones | warn (D-02 is "must" for new dashboards; no signal record exists yet - D-01) |
| G9 | **No empty signal binding.** No query with `uuid = ''` | SPEC-02 D-03 | The panel returns no data without saying so | block (zero-regret fix named first in SPEC-04 section 6) |
| G10 | **Queries follow the time picker** (time macros, not `now()` or interval literals); a fixed bucket needs a note in the panel description | SPEC-02 D-06, SPEC-03 S-15 | The panel ignores the range the user picked | block for new dashboards (S-15) |
| G11 | **Data sources are bound by role name,** identical in every plant, so an exported dashboard imports without re-binding | SPEC-02 D-07, SPEC-03 S-17 | Dashboards name no input; the telemetry source carries different names across plants | block for new dashboards (S-17) |
| G12 | **Every panel has a title, a query or content, and a unit from the Grafana unit list** | SPEC-03 S-06, S-07, S-10 | Untitled panels, empty query targets, missing units | block (S-06, S-07, S-10) |
| G13 | **The dashboard says what it is:** title `<Area or line> - <What it shows>`, folder `<Plant>/<Area>`, tags for status, template and plant, owner role in the description | SPEC-03 S-01 to S-04, S-18 | Draft-like titles, lifecycle-named folders, missing descriptions | block for S-01 to S-03; warn for S-04, S-18 |
| G14 | **Limits and states are readable:** thresholds with colour meaning (green normal, yellow warning, red limit, "no fault" is green); coded states use value mappings with text | SPEC-03 S-12, S-13; plant requirements G-07 | Thresholds missing on most stat panels; a good state shown red | warn |
| G15 | **A missing value is shown as missing,** never as 0; the age of the newest value is visible and stale data (beyond a threshold the screen's owner sets) is marked | plant requirements G-10, G-11 | Trend lines end well before "now" with no sign of it | warn; ties to G1 (a silent number is the quiet failure) |
| G16 | **Refresh and range follow the use:** live status short range and short refresh; trends hours and minute-level; shift reports shift-aligned. A very short refresh needs a note on query cost | SPEC-03 S-14 | Very short refresh on heavy queries; refresh switched off on live screens | warn |
| G17 | **Free text stays free of names and is not forwarded.** A reason or comment field is never summarised, enriched or sent on by an automated pipeline without filtering | WIP microservice spec "Cross-Cutting Platform Concerns", citing the vault's own rule on names and an existing note that carries an individual's name from an unfiltered export | A recorded case of a name leaking through an unfiltered free-text export | block where a self-served screen has a free-text field |
| G18 | **No write-back to a machine from a self-served use case.** Anything that sets values in a control system is not Lane 1 | WIP spec "Platform Extensibility": `writes_to_machines: true` routes through the ISA/IEC 62443 and NIST SP 800-82 segmentation review; `od-decision-routing`: an agent never writes to a production system | n/a | block; hand to Lane 3 and `od-cybersec-gate` |

Two further rules from the specs concern central operators rather than a plant, and are left out: class A tool dashboards are maintained once and deployed to all plants (SPEC-04 F-01), and the signal record is the system of record for unit and scale (D-01). A plant that wants to change a class A dashboard asks OD instead of editing its copy.

## Reading the same-name trap

SPEC-04 sorts the dashboard names present in several plants into classes: class A (query-identical everywhere: DTQ tool dashboards), class B (mostly identical: process value overviews, `Home`) and class C (**same name, different content**: for example Operations Dashboard, Alert Dashboard, Andon Board, each with a different query set per plant). So "the Andon board that plant X runs" is not one design; a plant that copies it gets that plant's logic. Check the template page and the library entry, not the title, before declaring a match (`catalog-usecase`).

## What a plant can run itself today

The scripts named in the specs (lint per rule id and plant; periodic re-run of the counts) are **not built yet** (SPEC-03 section 5, SPEC-02 D-10). Until they exist a plant answers G8 to G16 by reading the dashboard JSON or the panel list by hand. The key user can check G9, G10, G12 and G13 with the Grafana search and panel inspection; G8 and G11 need the data platform contact (IIAE). The exports carry no view counts, so usage is unknown; do not use "not opened" as evidence in a go-live check.

## Open

- ⟨Whether the newer Grafana major version used at one plant is the target platform or an exception⟩ - SPEC-01 / SPEC-04 open question; affects G12 for plugin panels.
- ⟨Whether the community chart plugin in use is on the approved list⟩ - SPEC-03 Q2; until then a plugin panel in a self-served screen is a warn.
- ⟨Who owns the central dashboard repository and the signal record⟩ - SPEC-04 Q3, SPEC-02 D-01.
- ⟨The dashboard language rule⟩ (titles with non-Latin characters exist) - SPEC-03 Q1.
