---
name: catalog-standardization
description: >-
  Check one use case against the cross-plant capability templates and the reference
  library before anything is specified, assign its cluster tag (C01-C12) with the
  baseline KPIs and checklist, and prepare it for the CSP (Common Solution Portfolio)
  gate. Use when someone says a use case is "standard", when a second plant wants
  something a first plant already has, when a library entry is proposed for rollout,
  when a cluster tag must be assigned or checked, when a dashboard or report built for
  one request keeps coming back and might become a standard use case, or when asked why
  the catalog has not scaled. Recommends only; the CSP decision sits outside OD. Not for
  matching a plant request to the catalog (catalog-usecase) or for the value case
  (bc-build).
license: MIT
metadata:
  id: catalog-standardization
  aliases: [od-use-case-standardization]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: lane-2
  new_state_lane: "Lane 2 (26)"
  new_state_step: "Implement, evaluate impact, ensure adoption, catalogue"
  department_names: ["catalog-synergy"]
  owner_role: Digital-Business-Value-Engineer (DBVE); CSP decision outside OD
  authority_level: recommend
  status: stable
  requires: [dept-context]
  composes: [dept-decision-rights, bc-portfolio, bc-build]
  okf:
    type: Agent Skill
    title: Use-case standardization
    tags: [practice, use-case-support-service]
---

# Use-case standardization

## Purpose

- Make one plant's solution every plant's: check the library, place the use case on the cross-plant templates, assign a cluster tag, prepare the CSP gate.
- Measure standardization by adoption (a second plant takes it, then uses it), not by how many templates exist.
- A second job lives here: decide whether a recurring ad-hoc asset becomes a standard use case (promotion mode, formerly od-use-case-promotion).
- Read `dept-context` first.

## Terms used here

- **Capability**: one of the cross-plant templates (Andon Board, OEE Calculation, Downtime Reporting, Process Quality Data, Machine Alerts, Cycle Time, Recipe Values, Process Values, Manual Quality Data, Analytics, Other Use Cases). Check the live list before quoting it.
- **Process group**: sits inside a material family (rubber, plastic, metal, assembly).
- **Library entry**: a proven, standardized solution with methods and actions written down, kept apart from plant use cases.
- **Cluster**: tag C01-C12 carrying a definition, KPI set and requirements checklist.
- **Catalog**: the set of standard use cases a plant can take; a **standard use case** is an entry that passed the CSP gate.

## Inputs and output

| | |
|---|---|
| Input | The scoped use case (`funnel-use-case` or `funnel-evaluation` record): plant, capability, notes, blockers |
| Input | Live use case list and library (from `bc-portfolio`), with the read date |
| Output | [`assets/standardization-review.md`](assets/standardization-review.md), one per use case, filled as the work happens |
| Receivers | `dept-decision-rights` (rollout gate) and `bc-build` (business case) |

- Output contract: [`outputs.yaml`](outputs.yaml) lists required outputs, criteria, checks and sign-offs.

## Procedure

- Copy the review template first. Each step fills one section, so the receivers never have to re-ask.

1. **Library check (review section 2).** Search the library for a proven entry against the same capability before specifying anything. Take it if it exists, because specifying again is the cost standardization avoids.
2. **Placement (section 1).** Place the use case on its capability and process group. Open `references/process-family-patterns.md` to judge how far it can travel.
3. **Cluster tag (section 3).** Take the tag from the rule-based classifier, then open the cluster's entry in `references/clusters.md` for the baseline definition, KPI set and checklist.
4. **Deltas (section 3).** Record only the plant's own deltas against the baseline: machines, line, local constraint.
5. **CSP readiness (section 4, rollout candidates only).** Work through the checklist below, then state the verdict.
6. **Handoff (section 5).** Name the verdict and the next skill; record the CSP gate as a dependency on the use case or saving row.
7. **Measure by adoption, not templates.** Compute delivered instances over capability instances from the live list and quote the read date.

### CSP readiness checklist

- [ ] Methods and actions are written down.
- [ ] Evidence exists that it works at its first plant (cite it).
- [ ] Utilization is recorded at the first plant, not only a deployment.
- [ ] No new capability or process group was created for it.
- [ ] CSP decision stated as `Yes`, `No` or not submitted (blank).

- Any unticked box means the verdict is "not ready, missing: ...", never "rejected".

### Classifier rules

- Signals in priority order: the use case's own **category** (an AI category routes straight to the AI cluster), then its **capability template**, then **keyword matching** across title, notes, blockers and target text.
- Deterministic: re-running after a data refresh reproduces the tags.
- A wrong or C12 tag means thin input: fix the input fields and re-run. Do not hand-assign a tag.
- Treat a C12 placement as a finding: re-check the process-group link and search sibling plants (`references/clusters.md`, C12).

### Promotion mode (a recurring ad-hoc asset)

- Use when a dashboard, report or app built for one request keeps being asked for.
- Run `references/od-use-case-promotion/procedure.md`; it keeps its own references, assets and authority (recommend).
- Refusing to promote is a valid result.

## Example

```text
Use case (fictional): "Line 4 stop reasons on a tablet", plant Alpha, injection molding.
1 Library: entry "Downtime Reporting - injection" found, CSP Yes, proven at plant Beta -> take it, adapted.
2 Placement: capability Downtime Reporting, process group Injection molding (plastic).
3 Cluster: classifier says C05 (category and template agree); baseline pulled from clusters.md C05.
4 Deltas: two machines without a stop signal; reason list in local language.
5 CSP: methods written, evidence from Beta cited -> verdict "ready; entry already CSP Yes".
6 Handoff: dept-decision-rights (rollout gate), bc-build (value), bc-portfolio (track adoption at Alpha).
```

## Human gate and AI-agent notes

- The agent recommends. The CSP decision sits outside OD; the OD lead signs off the review.
- Do not call an entry catalogued, standard or CSP-approved without a recorded CSP `Yes`.
- A blank CSP means the gate was not applied, not that the entry failed. Count the three outcomes on the live library before quoting a status.
- Promoting an asset needs a named responsible human (DBVE); the agent never commits a use case to industrialization.
- Compare regions on the live list: a low conversion rate is a different problem from a high one, not a smaller one.

## Pitfalls

- A blank CSP read as `No`: the gate has not been applied, so the entry is neither approved nor rejected.
- C12 growth read as "the portfolio is idiosyncratic": it mostly means intake text is thin, so improve the notes, not the tag.
- A deployment count read as adoption: a scaled use case needs utilization (and a saving where one is reported).
- Template existence read as standardization: all templates exist; only second-plant take-up counts.
- A new capability or process group created for one plant: it breaks the shared denominator. Raise it as a finding.
- A region treated as a scaled-down copy of another: conversion patterns differ by region.

## Do not

- Do not create a new capability or process group to accommodate one plant.
- Do not hand-edit cluster tags.
- Do not treat a `No` at the CSP gate as a rejection of the use case; it states rollout readiness.
- Do not count templates as evidence of standardization.
- Do not quote counts or statuses without the live read date.

## Definition of done

- All five sections of the review are filled, so neither receiver has to re-ask.
- The use case hangs off an existing capability and process group, with one classifier-assigned tag.
- Baseline pulled and only the plant's deltas recorded.
- For a rollout candidate, the CSP-readiness verdict names what is missing.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/clusters.md`](references/clusters.md) | Step 3: you need a cluster's definition, KPI set, checklist and sources (marked verified or carried-over) |
| [`references/process-family-patterns.md`](references/process-family-patterns.md) | Step 2: placing a use case, judging standardization potential, or briefing a plant on what peers ask for |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Step 7 or a scaling question: archetypes, graduation from prototype to configurable app, utilization over rollout count |
| [`references/background.md`](references/background.md) | You need the rationale, portfolio findings, open questions or sources; never an instruction |
| [`references/od-use-case-promotion/procedure.md`](references/od-use-case-promotion/procedure.md) | Promotion mode: a recurring ad-hoc asset |
| [`references/od-use-case-promotion/assets/promotion-package.md`](references/od-use-case-promotion/assets/promotion-package.md) | Promotion mode: the package and the promote / reuse / keep / retire recommendation |
| [`references/od-use-case-promotion/references/promotion-criteria.md`](references/od-use-case-promotion/references/promotion-criteria.md) | Promotion mode: the six tests and the evidence for each |
| [`references/od-use-case-promotion/references/pattern-evidence.md`](references/od-use-case-promotion/references/pattern-evidence.md) | Promotion mode: reading portfolio aggregates (declared standard, library and CSP status, utilization) |
| [`references/od-use-case-promotion/references/process-chain-practice.md`](references/od-use-case-promotion/references/process-chain-practice.md) | Promotion mode: graduation conditions, exchange with the operational-excellence function, retire versus keep |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
| [`references/outputs.md`](references/outputs.md) | The output contract in full (generated from outputs.yaml) |
