---
type: Skill Reference
title: Technical guardrails
description: Candidate guardrails G8 to G17 for a self-served dashboard, each with its recorded source, the measured failure count in the Grafana estate and a proposed block-or-warn setting. Open it when the seven seeded guardrails are not enough for the screen a plant has built.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Technical guardrails

The seven guardrails in `SKILL.md` (G1 to G7) cover data, platform boundary, footprint, figures, ownership, handover and Cyber Security. A plant that builds or copies a dashboard needs more: how the screen reads data, how it is built, what it shows. The vault holds these as **proposed specifications**, not as adopted rules. Treat every row below as a **candidate** that the OD lead has not yet confirmed.

## Where they come from and how far to trust them

Vault folder `Dashboard Exports/specs`, read 2026-11-05, all AI-drafted from the Grafana JSON exports of 19 plant locations (94 export runs, 8,280 files, 1,010 unique dashboards, 17,961 panels; exports read 2026-11-03) and marked "Draft for review":

- SPEC-02 Telemetry Data Contract: requirements D-01 to D-10 (proposals "inferred from the problems P1 to P7; none is a statement of current practice").
- SPEC-03 Dashboard Authoring Standard: rules S-01 to S-19 with the count of dashboards that break each today. Thresholds are proposals; the counts are facts counted from the exports.
- SPEC-04 Dashboard Families and Central Provisioning: classes A to D and requirements F-01 to F-08.
- Hannover Stoecken KKA / Pulp Mixer requirements: the one worked example of a dashboard-level requirement set, reverse-engineered from an existing implementation.

None of these says "a plant must not go live unless...". The block-or-warn setting below is mine from SPEC-03 section 6, which names the rules that every **new** dashboard must pass after adoption (S-01 to S-03, S-06, S-07, S-10, S-15, S-17). Everything else is "warn" in this table. ⟨Which guardrails block and which only warn⟩ remains the OD lead's decision.

## The candidates

| # | Guardrail (plain words) | Source rule | Failure today in the estate (counted) | Proposed |
|---|---|---|---|---|
| G8 | **Signals are not bound by a literal UUID typed into the SQL.** A new screen takes signals through a variable or a lookup on the signal record | SPEC-02 D-02, S-11 | 16,452 literal UUID predicates in 498 dashboards; half sit in 73 dashboards. A re-created device or datapoint breaks every dashboard holding the old UUID | warn (D-02 is "must" for new dashboards; no signal record exists yet - D-01) |
| G9 | **No empty signal binding.** No query with `uuid = ''` | SPEC-02 D-03 | 450 empty predicates in 49 dashboards; the panel returns no data without saying so | block (zero-regret fix named first in SPEC-04 section 6) |
| G10 | **Queries follow the time picker** (time macros, not `now()` or interval literals); a fixed bucket needs a note in the panel description | SPEC-02 D-06, SPEC-03 S-15 | 670 queries in 67 dashboards ignore the picker | block for new dashboards (S-15) |
| G11 | **Data sources are bound by role name,** identical in every plant, so an exported dashboard imports without re-binding | SPEC-02 D-07, SPEC-03 S-17 | 129 dashboards name no input; the telemetry source carries three names across plants | block for new dashboards (S-17) |
| G12 | **Every panel has a title, a query or content, and a unit from the Grafana unit list** | SPEC-03 S-06, S-07, S-10 | 4,494 untitled panels (3,450 stat); 2,231 empty query targets in 181 dashboards; 10,920 panels without a unit | block (S-06, S-07, S-10) |
| G13 | **The dashboard says what it is:** title `<Area or line> - <What it shows>`, folder `<Plant>/<Area>`, tags for status, template and plant, owner role in the description | SPEC-03 S-01 to S-04, S-18 | 32 draft-like titles; 162 dashboards in lifecycle-named folders; 128 of 1,010 have a description | block for S-01 to S-03; warn for S-04, S-18 |
| G14 | **Limits and states are readable:** thresholds with colour meaning (green normal, yellow warning, red limit, "no fault" is green); coded states use value mappings with text | SPEC-03 S-12, S-13; Hannover requirement G-07 | 2,989 of 9,573 stat panels carry thresholds; the Hannover review found a good state shown red | warn |
| G15 | **A missing value is shown as missing,** never as 0; the age of the newest value is visible and stale data (over 15 minutes in the Hannover example) is marked | Hannover requirements G-10, G-11 | Hannover trend lines end 10 to 40 minutes before "now" | warn; ties to G1 (a silent number is the quiet failure) |
| G16 | **Refresh and range follow the use:** live status 5-minute range and 5 to 30 s refresh; trends 6 to 24 h and at most 1 minute; shift reports shift-aligned. A 5 s refresh needs a note on query cost | SPEC-03 S-14 | 101 dashboards at 5 s refresh; 695 with refresh off | warn |
| G17 | **Free text stays free of names and is not forwarded.** A reason or comment field is never summarised, enriched or sent on by an automated pipeline without filtering | WIP microservice spec "Cross-Cutting Platform Concerns", citing the vault's own rule on names and an existing note that carries an individual's name from an unfiltered export | one recorded case in the vault | block where a self-served screen has a free-text field |
| G18 | **No write-back to a machine from a self-served use case.** Anything that sets values in a control system is not Lane 1 | WIP spec "Platform Extensibility": `writes_to_machines: true` routes through the ISA/IEC 62443 and NIST SP 800-82 segmentation review; `od-decision-routing`: an agent never writes to a production system | n/a | block; hand to Lane 3 and `od-cybersec-gate` |

Two further rules from the specs concern central operators rather than a plant, and are left out: class A tool dashboards are maintained once and deployed to all plants (SPEC-04 F-01), and the signal record is the system of record for unit and scale (D-01). A plant that wants to change a class A dashboard asks OD instead of editing its copy.

## Reading the same-name trap

SPEC-04 splits the 17 dashboard names present in three or more plants into class A (query-identical everywhere: DTQ tool dashboards), class B (12 to 14 of 17 identical: process value overviews, `Home`) and class C (**same name, different content**: Operations Dashboard in 9 plants with 8 distinct query sets, Alert Dashboard 6 plants / 5 sets, Andon Board 6 plants / 6 sets). So "the Andon board that plant X runs" is not one design; a plant that copies it gets that plant's logic. Check the template page and the library entry, not the title, before declaring a match (`catalog-usecase`).

## What a plant can run itself today

The scripts named in the specs (lint per rule id and plant; weekly re-run of the counts) are **not built yet** (SPEC-03 section 5, SPEC-02 D-10). Until they exist a plant answers G8 to G16 by reading the dashboard JSON or the panel list by hand. The key user can check G9, G10, G12 and G13 with the Grafana search and panel inspection; G8 and G11 need the data platform contact (IIAE). The exports carry no view counts, so usage is unknown; do not use "not opened" as evidence in a go-live check.

## Open

- ⟨Whether Grafana 11 (one plant) is the target platform or an exception⟩ - SPEC-01 / SPEC-04 open question; affects G12 for plugin panels.
- ⟨Whether the community chart plugin (1,241 panels, 273 dashboards) is on the approved list⟩ - SPEC-03 Q2; until then a plugin panel in a self-served screen is a warn.
- ⟨Who owns the central dashboard repository and the signal record⟩ - SPEC-04 Q3, SPEC-02 D-01.
- ⟨The dashboard language rule⟩ (63 titles with Chinese characters) - SPEC-03 Q1.
