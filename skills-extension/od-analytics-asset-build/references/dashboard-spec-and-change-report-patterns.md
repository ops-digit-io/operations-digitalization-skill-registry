---
type: Skill Reference
title: Dashboard spec and change report patterns
description: The structure of a dashboard specification set (hub, baseline, data contract, authoring standard, families) and of a dashboard-level requirements and summary pair, plus how to read and use the dashboard change reports. Structure and reading rules only; no estate counts.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice, dashboard, specification]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Dashboard spec and change report patterns

Derived from the vault's dashboard-spec hub and its four specifications, the dashboard-level requirements and summary pair written
from one plant's exports, and the dashboard change and creation reports. Everything in those notes is a count of the estate at an
export date; **none of it is carried here**. What is carried is how such documents are built and read, so an agent or key user can
write the next one or judge one. The specs are drafts, AI-drafted from the exports and not reviewed by a human. Own synthesis is
marked `PROPOSAL`; unknowns are `<...>`.

## 1. The spec set: five documents, one job each

| Document | Decides | Typical contents |
|---|---|---|
| Hub (overview) | Where to start and what must be decided first | "What to know first" list, table of specs (what each decides, main output), decisions needed before next steps, how the numbers are produced, sources |
| Estate baseline | What exists and how it is counted | Evidence and counting rule, measures table, per-plant table, findings, requirements for inventory and lifecycle |
| Telemetry data contract | How dashboards read data | The contract as the dashboards use it, problems, requirements for signal records and binding, acceptance checks |
| Authoring standard | How dashboards are built | Numbered, lintable rules grouped by identity and lifecycle, structure and panels, units limits colours, time refresh variables, documentation |
| Families and central provisioning | What is shared, what is harmonised, in what order | Sharing classes (central, template, same name different content, plant-specific), migration cost, requirements, suggested order |

Reading order: hub, baseline, then the spec that matches your question. The content of the estate and family findings is already
turned into method in `dashboard-estate-baseline.md` and `dashboard-families-catalogue.md`; this file adds the **document
structure** so a new spec follows it.

## 2. Anatomy of a specification

Every spec in the set uses the same numbered sections. Copy them.

| Section | Rule |
|---|---|
| Header | Spec id, title, description, status "draft for review", review status "AI-drafted ... not reviewed by a human", tags, link to hub and neighbours |
| 1 Purpose and scope | One paragraph: what the document gives, what it does not cover (live state, permissions, usage, other data sources) |
| 2 Evidence and method | The exports read, the **counting rule** (newest complete run per location and uid), the file that holds each number, what is not reproduced (host names, user ids, addresses). Anything labelled **Inferred** is reasoning from counts, not a statement of the export |
| 3 The state in numbers / the contract / what the estate looks like | Facts, each traceable to a data file |
| 4 Findings (`F1...`) | Each states the measurement, then what it implies. Observations and inferences are separated |
| 5 Requirements | Table: id, requirement, priority (Must, Should, Could), trace to the finding or problem it solves. Stated as **proposals**, not current practice |
| 6 Suggested order | A sequence that starts with zero-regret fixes and ends with classification and reconciliation |
| 7 Acceptance | Checks a reviewer can run on the exports alone, with those that need live access named as such |
| 8 Open questions (`Q1...`) | Decisions for the owner, with the section that raised them |
| Sources | Internal evidence, read date, generating script |

### Requirement id families

| Family | Meaning | Example scope |
|---|---|---|
| `E-nn` | Estate | One canonical merged inventory, run retention, a status for every dashboard, usage collected before retiring anything |
| `D-nn` | Data contract | One signal record per signal, binding through a variable, no empty binding, one documented way to read a value, standard data source names per role, one downtime schema |
| `S-nn` | Authoring standard rule | Title pattern, status as a tag, template tag, owner role in the description, top-down layout, titles on panels, units from the unit list, thresholds with documented colour meaning, defaults for time and refresh, standard variable names, descriptions |
| `F-nn` | Families | Central deployment of identical families, template for near-identical, reference designs for same-name-different-content, classification of plant-specific ones |

Rules in the authoring standard carry a "now" and a "target" column. **Now** is a violation count from the last export; **target** is
a proposal for the owner to confirm. When you reuse a rule, re-measure "now"; never quote an old one.

### Lintable versus judgement

A rule is *lintable* if the exported JSON alone decides it. Mark each rule: lintable, judgement (a reviewer decides), or needs live
access. The first deliverable that makes a standard enforceable is a lint that reads the same inventory as the analysis script and
prints a count per rule id and plant. A standard without a lint is advice.

### The hub's "numbers" discipline

The hub says how the numbers are produced: a script reads every run, keeps the newest copy per key and rewrites the inventory, the
aggregates and the plant table. **The prose is hand-written and does not update itself.** After a new export, compare the aggregates
with the numbers in the text before quoting either.

## 3. The dashboard-level requirements and summary pair

For one plant's set of dashboards, two documents are written from the exports: a **requirements specification** (for builders and
reviewers) and a **summary** (for the requester and the plant).

### Requirements document

| Part | Content |
|---|---|
| Header table | Location (instance), dashboards (title and uid), created dates, sources (which screenshot run, which JSON run, time range of the screenshot, "first screen only"), status |
| Status line | "Derived from the existing implementation (reverse-engineered)". Three markers are used inline: **[observed]** visible in the screenshots, **[issue]** a deviation to be fixed, **[open]** needs a decision by the process owner |
| 1 Purpose and scope | What each dashboard shows and for whom, one line per level; **out of scope** listed (write-back to the machine, alarm notification when no alert rules exist) |
| 2 Common requirements (`G-nn`) | Rules shared by all dashboards of the set |
| 3..n One section per dashboard | What the screenshot shows [observed]; requirements with ids; signals; issues |

**Common requirements that recur** (use as a checklist): data from the telemetry table with the signal addressed by identifier;
identifiers kept in hidden variables or one central place, not scattered as literals; stat tiles show the latest value in the
range, trends aggregate with a bucket variable; PLC scaling applied in the query and written in the panel description; every
physical value has a unit; default time range relative and refresh set; status tiles use value mappings with text and colour (green
normal, yellow attention, red fault, **a good state is never red**); navigation links between levels; one label language per
dashboard; a clear text for "no data" instead of 0 or an empty chart; data freshness visible and stale data marked.

### The three-level pattern

The set splits one system into levels of increasing depth, each for a different reader.

| Level | Reader | Question it answers |
|---|---|---|
| 1 Overview | Shift and operators | Is it running, are the key values fine, are there faults? |
| 2 Subsystem process detail | Process engineering | Which subsystem causes the deviation? |
| 3 Maintenance and diagnostics | Maintenance | Condition, vibration, operating hours, wear |

A production overview for a single machine follows the same logic with machine state, safety state, batches, output, actual versus
setpoint and faults. This is the same overview-to-in-depth family `dashboard-families-catalogue.md` describes.

### Summary document

One block per dashboard with three headings, in this order:

1. **Issue solved:** the situation without it, in operational terms (who has to walk to the PLC or HMI, what is noticed too late).
2. **Requirements:** one paragraph of what the screen must give, with limits and links.
3. **Signals:** the list of signals with their address and scaling, grouped by subsystem.

The summary is what you can hand to the requester; the requirements document is what the builder and reviewer use.

### Writing one from an existing dashboard (reverse-engineering)

1. Take the **JSON** (all panels, queries, thresholds) and a **screenshot** (what a reader sees). Note that a screenshot covers a
   time range and the first screen only; say so in the header.
2. List what the screen shows [observed]: rows, tiles with unit and colour, charts and what they plot.
3. List deviations [issue] against the common requirements: tiles without a unit, a fixed absolute time range saved, refresh off,
   a good state shown red, hard-coded identifiers, missing links, mixed label languages, trend lines ending well before "now".
4. List decisions [open]: label language, refresh proposals, pilot choices.
5. Write the signal list with scaling; mark signals that deliver no data.
6. Write the summary from the "issue solved" question.

Use `assets/dashboard-requirements-template.md`.

## 4. Reading the change and creation reports

Two kinds of report are generated from the newest run per location: a **changes** report (dashboards created or changed in a
period) and a **created** report (new dashboards in a period). A `.csv` twin carries the same rows.

| Part | Meaning |
|---|---|
| Title and period | The window of the report |
| "Generated ... from the newest run per location" | How current it is; a later export makes it stale |
| Counting rule | A dashboard created in the period is listed as *created* only, even if edited after; *changed* shows the **last save** only. The platform keeps only the latest change date, so **earlier edits within the period are invisible** |
| Summary matrix | Location by month, "created / changed" |
| Sections by month, then location | Tables with date, change type, folder, dashboard, saved by (a user id), version |

**How to read it.**

- **Version** is a churn signal: a high version on a "changed" row means the dashboard is edited live; a low version on a "created"
  row means it is new. Neither says it is used (the exports carry no views).
- **Bulk creation on one date in one location** is an import, a migration or a wave, not independent work. Count it once.
- **Folder** names carry lifecycle (`dev`, `archive`, `Trashbin`) because there is no status field; read them as lifecycle marks.
- **A conflict copy** (a sync tool's duplicate of the same report) is not a second report. Use the one without the conflict marker and
  compare only if the two differ in generation time.
- The **saved by** column holds user ids. Do not copy them into notes or messages; write the role ("plant key user") or "a plant
  user".
- **Use it as a worklist:** every newly created dashboard without a requirements document is a candidate for the reverse-engineering
  routine above; every changed dashboard with a high version in a lifecycle folder is a candidate for review before retirement.

## 5. Pitfalls

- Quoting a baseline number from a spec without re-running the analysis on the current export.
- Treating "Inferred" as "observed".
- Retiring on staleness alone: usage data has to come first.
- Taking a family with the same name across plants as identical; check the query sets.
- Writing a requirements document from a screenshot alone: the signals, scaling and queries are in the JSON.
- Counting the repeated exports of one dashboard as several dashboards.

## AI agent operating notes

- **May do:** draft a requirements and summary pair from a JSON export and screenshot using the marker convention; run the lint
  rules that are lintable and report per rule id; merge runs per key; summarise a change report by location and type; list
  candidates (new dashboards without requirements, lifecycle-folder dashboards with high versions).
- **Inputs:** export JSON (newest complete run per location), screenshots with their time range, the authoring standard, the
  report file with generation time.
- **Evidence to cite:** run id and read date, dashboard uid, rule id, the counting rule used.
- **Human gate:** targets, priorities and any retirement are decided by the owner; a requirement that is `[open]` is never closed by
  the agent.
- **Hands over to:** `ops-dashboard-engine` (build), `od-acceptance-test` (verify against the requirements),
  `od-handover-and-adoption` (explain to the requester), `od-context-freshness` (stale report).
