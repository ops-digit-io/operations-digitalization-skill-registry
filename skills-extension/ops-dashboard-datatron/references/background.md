---
type: Skill Reference
title: Background
description: Context, rationale, examples and notes that stood in SKILL.md, moved here unchanged. Open it for the why; it is never an instruction.
resource: ../SKILL.md
status: draft
tags: [background]
---
# Background

## Outputs and hand-off: the text before outputs.yaml

`ops-dashboard-datatron` delivers a Grafana dashboard on the DATATRON telemetry schema, built from a catalogued template, plus the list of datapoint UUIDs that had to be enabled first. The QA checklist is the go-live gate.

## Required outputs

| Output | Form | Recipient | Complete when |
|---|---|---|---|
| Datapoint UUID list | List produced before the build starts | Plant (switches the signals on, via datapoint-enablement intake) | Every disabled signal the dashboard needs is listed by UUID before the build; no build rests on a disabled signal |
| Dashboard | Grafana dashboard built from the catalog entry's template through `ops-dashboard-engine` | Plant key user (self-service); `catalog-usecase` | Built on selected DATATRON tags with the proven query and variable patterns and scaled-PLC handling; nothing outside the template added locally |
| QA checklist result | Checklist pass recorded against the dashboard | Plant key user; `catalog-guardrails` | The QA checklist is passed; this is the objective go-live gate |
| Published example | Approved dashboard published to the use-case library | `catalog-usecase`; DBVE | Published as a reusable example only after the QA pass; publishing to a shared Grafana is human-approved |

## Handoff

- **Receives from:** `catalog-usecase` (the catalogued dashboard and its template), `catalog-guardrails` (the QA gate), `ops-dashboard-engine` (the generic Grafana JSON engine).
- **Next in the flow:** Lane 1 step 1a2 (apply template) and 1b4 (apply template and go live), and Lane 2 step 26 (implement and graduate); on 1b4 the dashboard is accompanied by `know-training`. A need the template does not cover goes to Lane 2 as a deviation.
- **Stops here when:** a required signal is disabled (list its UUID and stop), the QA checklist has not passed, or the need extends the catalogued template (route it to Lane 2, do not extend locally). Do not publish without the QA pass.

## Open questions

- The department master package `ops-grafana-dashboards.zip` is not in the registry. The QA checklist and the patterns in `SKILL.md` follow its transcription in the `ops-analytics-asset` reference `references/ops-grafana-dashboards.md`, which is itself draft; compare with the master before marking this skill stable.
- `is_delta` has no written definition in the data contract (SPEC-02 question Q2) and appears in eight spellings; the reading in the checklist (`'t'` for change events, `'t','f'` for states) is the package's reading and is not confirmed by the contract.
- Value model coupled to the dashboard's own measured queries is shared with `bc-build` (`bc-value-model`) and is not part of this skill.
- Coverage beyond KKA, press centres and utilities (conveyors) is a department roadmap item.
- Whether this skill and the Lane 1a section of `ops-analytics-asset` should be one unit is undecided; both point at the same package.
- No real plant run is recorded: the worked example in `SKILL.md` is fictional.

## Sources used in the improvement run

- `V:\jakobgabriel\obsidian\personalvault\Work-OpsDigit-Knowledge\Dashboard Exports\specs\SPEC-02 Telemetry Data Contract.md` (scale and unit are decided per panel; `is_delta` appears in eight forms and is unexplained; unit and scale are not stored with the signal).
- `V:\jakobgabriel\obsidian\personalvault\Work-OpsDigit-Knowledge\Dashboard Exports\Dashboard Notes\Waltershausen\Andon Board - BBM [l9gNAKKV].md` (is_delta filter forms in real dashboard queries).
- Registry file `skills/ops-analytics-asset/references/ops-grafana-dashboards.md` (the transcribed department package: QA checklist, datapoint enablement list, two time-filter dialects, scaling note).
