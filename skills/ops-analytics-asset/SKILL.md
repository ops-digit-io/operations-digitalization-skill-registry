---
name: ops-analytics-asset
description: >-
  Choose, design and build the asset a plant actually opens (dashboard, report, analytics workflow, app or agent) tied to a named daily routine such as the Gemba walk, shift check or Andon escalation, an action owner and a validation against the paper record. Use when someone asks for a dashboard, report or app, when choosing between them, when a delivered dashboard is not opened, or when a plant applies a catalogued dashboard template itself (Lane 1a). Not for the Grafana panel and JSON build (ops-dashboard-engine), data availability checks (mi-data-availability) or handover and adoption (deploy-handover).
license: MIT
metadata:
  id: ops-analytics-asset
  aliases: [od-analytics-asset-build]   # former name (naming convention, 2026-11-11)
  tier: practice
  lane: [lane-1, lane-2]
  new_state_lane: "Lane 1a (1a2), Lane 1b (1b4), Lane 2 (23, 26)"
  new_state_step: "Apply the standard template (self-service); Standardized deployment, go live, confirm adoption; Prototype / click-dummy, validated with the recipient; Implement, evaluate impact, ensure adoption, catalogue"
  department_names: ["ops-dashboard-datatron (self-service mode, external engine)"]
  owner_role: Digital-Business-Value-Engineer (DBVE)
  tags: [analytical-support-service, practice, use-case-support-service]
  authority_level: draft/author the asset; publishing externally is human-approved
  status: stable
  requires: [dept-context]
  composes: [ops-dashboard-engine, mi-data-availability, deploy-handover, catalog-standardization, catalog-usecase]
  okf:
    type: Agent Skill
    title: Analytics asset build
    tags: [analytical-support-service, practice, use-case-support-service]
---

# Analytics asset build

## Purpose

- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.
- Build the asset the plant actually opens (dashboard, report, analytics workflow, app or agent) so that it is used inside a real ritual, can be diagnosed by the plant and is counted in the portfolio.
- Use it when a delivery asset is designed, reworked, or when choosing between a dashboard, a report and an app.
- Scope: this skill chooses the asset type, names the ritual, validates and hands off; the Grafana build itself belongs to `ops-dashboard-engine` (a core skill; `ops-dashboard-datatron` is its extension).

## Inputs and output

- Inputs: a data-availability verdict, the use case with its ritual, decision and action owner, and the catalog entry or template if one exists.
- Output: the built and validated asset, handed off with a filled [`assets/asset-build-protocol.md`](assets/asset-build-protocol.md) (output asset, utilization expectation, named plant owner, data path).
- Read `dept-context` first.
- Run `mi-data-availability` before building anything, because an asset on a proxy signal is later retired.

## Procedure

1. Confirm data availability and fitness → `mi-data-availability`.
2. Check the reference library first and take a proven entry rather than building → `catalog-standardization`.
3. Name the **ritual**, the **decision** and the **action owner** the asset supports. If one is missing it is a "dashboard without an action owner": do not build it (five smell checks in `references/process-chain-practice.md`).
4. Choose the asset type from the table below; justify it if it is a dashboard by default → `references/asset-type-and-tier.md`.
5. Build to the standard layout; every figure traces to a nameable source. For a dashboard, hand the ritual, the tier and the data model to `ops-dashboard-engine` rather than hand-building panels here.
6. **Validate before calling it built** with the checklist in `references/lifecycle-and-validation.md`; rendering is not the same claim as correct.
   - Reconcile with the paper record for the same period and explain differences.
   - Name who stops the paper process.
7. **Deliver it and explain it to the requester**, because delivery without explanation is the most common route to a `NEVER` utilization row.
8. Record on the use case: output asset, business process, utilization expectation, named plant owner, data path → `deploy-handover`. Fill `assets/asset-build-protocol.md` as the work happens; `deploy-acceptance` and `deploy-handover` read it next.
9. Review utilization monthly; low utilization means rework or retire.

- Validation loop: run the checklist, fix every failed line, re-run until clean, and only then deliver.

## What this function actually produces

- Across the use cases that record an output asset, the **dashboard** is by far the most common output; reports, apps, analytics workflows and agents are rare (re-count on the use-case list before quoting a split).
- The dashboard is the default output; question the default instead of inheriting it.

| Asset | Fits when |
|---|---|
| **Dashboard** | A number has to be current at the line, inside a recurring moment |
| **Report** | A question is asked on a cadence and the answer is read away from the line |
| **Analytics workflow** | The insight is derived, repeatable, and consumed by another system or analysis |
| **App** | The user has to *enter* or *decide* something, not only read |
| **Agent** | The work is judgement over data on a cadence, with a named responsible human |

## Design for the ritual, not the data

- **A dashboard that is not read inside a ritual is a dashboard nobody reads.** Before building, name the moment:
- **Daily Gemba**: the shop-floor walk, the largest consumer of what OD builds; it needs current numbers at the line, not a report assembled afterwards.
- **Shift checks**: recorded in the plant's own standard procedures (for example supervisors checking OEE several times per shift); find out whether the asset supports or replaces that procedure.
- **Escalation (Andon)**: two-step by design, the first signal requests help without stopping the line, the second stops it if unresolved, with tiers and a time-boxed response per tier.
   - Log every event, not only display it; the log makes improvement analysis possible.
   - An Andon asset that only displays is half an asset.

## Where it will live

- **Grafana** is where most of what the function builds is seen; a line-side dashboard belongs on the plant's local instance, a cross-plant question does not.
- Once the ritual and decision are named and "Dashboard" is chosen, the JSON build is `ops-dashboard-engine`'s job (schema interview, archetype, tier).
- Grafana has no export worth relying on; if dashboard state must appear in a report or review, use the screenshot automation in `_apps/`.
- **Power BI / OESL Dashboards** carry the Scorecard and the two OD reports: the steering layer. Do not build a line-side asset there.
- **Layer:** Databricks and the Azure Storage Account are the global platform (`dept-context`).

## What the plants already have

- Read the baseline and the catalogue before designing: `references/dashboard-estate-baseline.md`, `references/dashboard-families-catalogue.md`.
- Most dashboards exist in one plant only; recurring titles (Andon, Alert, Operations) are shared in name, not in content. Measure patterns on the current export; the specs they come from are drafts.
- Bind new panels through a variable, not a literal UUID, and put shift windows and targets in configuration, so a port does not need a code edit.

## Lane 1a self-service mode

- In the new state a plant runs a **catalogued** use case itself (Lane 1a): the key user applies the standard template; OD supplies the catalog entry, template and guardrails.
1. Start from the catalog entry's template (`catalog-usecase`, `catalog-template`), never from a blank dashboard or an ad-hoc copy.
2. Apply it to this plant's signals; anything the template does not cover is a deviation, not a local extension: stop and route it (a recurring need is Lane 2).
3. Pass the technical guardrails and the go-live check (`catalog-guardrails`, its `references/technical-guardrails.md`); passing the checklist is the approval gate.
4. The plant confirms adoption (`deploy-handover`).

- The DATATRON dashboard package (families, L1 to L3 drill-down, schema, queries, panel recipes, datapoint enablement) is `references/ops-grafana-dashboards.md`; use it for any DATATRON dashboard in Lane 1a, 1b4 and Lane 2.
- A value the machine does not deliver directly is derived first as a calculated datapoint (`mi-flow`, rule engine).

## When not to build

- The insight is a one-off with no recurring value → deliver the answer, close it as ad-hoc, **do not industrialize**.
- An asset for this capability already exists at another plant → adopt it.
- The data gap is real → route it, do not build on a proxy.
- The smell checks in step 3 fail → a dashboard without an action owner.

## Pitfalls

- **Delivery without explanation**: the requester never opens it and the use case ends as `NEVER` utilization.
- **Skipping the paper reconciliation**: a rendering dashboard can still be wrong; production and engineering deep dives must explain every difference.
- **Literal UUID binding in panels**: it breaks on every port and hides which signal is meant; bind through a variable.
- **Same title, different content**: do not assume an Andon or Alert dashboard at plant B matches plant A.
- **Building a dashboard by default** when a report or an app fits the decision.
- **Adding a tool to build it**: the strategy is a deliberately small operational footprint.

## Do not

- Do not present unvalidated insight as fact.
- Do not state a figure without a nameable source (`dept-context` rule 4).
- Do not publish an asset externally without the responsible human.
- Do not mark an asset accepted before the paper reconciliation is signed.

## Human gate and AI-agent notes

- An agent may draft the requirements, pick the asset type with a reason, prepare the build and run the validation checklist.
- The plant owner role decides daily use (`PRODUCTIVE`); the requester role confirms the paper reconciliation; the responsible human role approves any external publication; the DBVE role signs off acceptance.
- An agent never marks an asset accepted before the paper reconciliation is signed.
- Chain detail (handoff contract, generative-AI process, paper reconciliation, sprint practice): `references/process-chain-practice.md`.

## Example

```text
Input : request for a "line status dashboard", Plant X (fictional), data verdict fit
Check : ritual = daily Gemba; decision = which line to visit first; action owner = shift supervisor role
Output: asset type Dashboard (justified); handed to ops-dashboard-engine with ritual, tier, data model;
        validated against the checklist; protocol filled; utilization expectation: daily
```

```text
Input : "We want to see scrap by cause every week" (fictional), no line-side moment, read in a Monday meeting
Check : ritual = weekly quality review, away from the line; no entry of data needed
Output: asset type Report, not a dashboard; justified in the protocol; ops-dashboard-engine not engaged
```

## Definition of done

- The asset passed the validation checklist, was reconciled with the paper record, was delivered and explained to the requester, and the protocol records output asset, utilization expectation, plant owner role and data path.

## Outputs

- [`outputs.yaml`](outputs.yaml): required outputs, criteria, checks and sign-offs.
- One run record per call: `python scripts/run_record.py new <skill-id>` (registry root).

## References

| File | Open when |
|---|---|
| [`references/background.md`](references/background.md) | You need context and rationale; never an instruction |
| [`references/asset-type-and-tier.md`](references/asset-type-and-tier.md) | Choosing the asset type, or deciding where this skill ends and `ops-dashboard-engine` begins |
| [`references/lifecycle-and-validation.md`](references/lifecycle-and-validation.md) | Validating before delivery: lifecycle mapped to the registry skills and the "it renders vs it is correct" checklist |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Checking the smell tests, handoff contract, paper reconciliation, sprint practice, agent notes |
| [`references/dashboard-families-catalogue.md`](references/dashboard-families-catalogue.md) | Before building: family groups, sharing classes, 14 family cards with signals and traps |
| [`references/dashboard-estate-baseline.md`](references/dashboard-estate-baseline.md) | Reading or measuring a plant's Grafana estate (data sources, query patterns, churn) |
| [`references/dashboard-worked-examples.md`](references/dashboard-worked-examples.md) | Looking for an illustrative pattern and its lesson |
| [`references/dashboard-json-sample.md`](references/dashboard-json-sample.md) | Sampling dashboard JSON and the nine query patterns |
| [`references/capability-templates-and-placement.md`](references/capability-templates-and-placement.md) | Placing a new asset: the 11 templates and 13 placement rules |
| [`references/dashboard-spec-and-change-report-patterns.md`](references/dashboard-spec-and-change-report-patterns.md) | Writing a dashboard spec set or reading a change or creation report |
| [`references/ops-grafana-dashboards.md`](references/ops-grafana-dashboards.md) | Building a DATATRON dashboard in Lane 1a, 1b4 or Lane 2: schema, queries, variables, panel recipes, datapoint enablement |
| [`assets/dashboard-requirements-template.md`](assets/dashboard-requirements-template.md) | Writing requirements and summary for one system's dashboards |
| [`assets/dashboard-review-checklist.md`](assets/dashboard-review-checklist.md) | Reviewing a dashboard: ritual, family, signal binding, authoring rules, placement |
| [`assets/asset-build-protocol.md`](assets/asset-build-protocol.md) | Recording the build as it happens (handoff record) |
| [`evals/evals.json`](evals/evals.json) | Test cases and trigger queries to run with and without this skill |
