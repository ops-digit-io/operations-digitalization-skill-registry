---
type: Skill Reference
title: Procedure
description: Formerly the skill od-use-case-promotion, absorbed into od-use-case-standardization on 2026-11-10 to remove duplication against the department context. Decide whether a recurring ad-hoc asset (a dashboard, report, analytics workflow or app first built for one request) should become a standard use case, and if so assemble the promotion package - the recurrence and value evidence, the reproducibility check, the placement on capability template, process group and cluster, the handover record, and which of the catalog conditions are met - that feeds use case definition and the standardization gate. Refusing to promote is a valid result. Use when the same analytical request or asset comes back from more than one plant or more than once, when utili
resource: ../../SKILL.md
status: draft
owner: human:jakob.gabriel
tags:
- analytical-support-service
- practice
- new-state
- draft
- absorbed
derived_from:
- ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
- ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/analytical-support-service/playbook.md
- ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/analytical-support-service/tasks.md
- ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/analytical-support-service/agent-brief.md
- ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/08-decision-rights.md
- ops-knowledge-graph/_knowledge/10-Department/Use case lifecycle.md
- ops-knowledge-graph/_knowledge/10-Department/Use case standardization.md
- Skills catalog-usecase (the four conditions for "catalogued"), od-use-case-standardization, od-analytical-support-service, od-handover-and-adoption, od-analytics-asset-build and od-use-case-definition, read 2026-11-05
- New-state flow (docs/new-state-flow.md and the VSM skill map), Lane 2 step 6 implement, adopt and graduate, read 2026-11-05
- Department knowledge base, Case Groups - Overview and the group notes CG-03 and others, read 2026-11-05
- Department knowledge base bundle file kg_nodes.csv, the use case records and library use case records read as aggregates (category, handover, output asset, CSP decision), 2026-11-05
generated:
  by: claude-code/1
  at: 2026-11-05 00:00:00+00:00
---
# Use-case promotion

> **Absorbed.** This was the skill `od-use-case-promotion`. It now runs as a mode of [`od-use-case-standardization`](../../SKILL.md) (merged 2026-11-10, see `log.md`). Its authority stays as it was: recommend.

Read `od-context` first.

**Plan row AS-04** (`OD_Skill_Map.md`, named `od-as-industrialize` there): trigger "recurring value in an
ad-hoc asset"; output "promotion package into a standard use case (feeds UC-02)"; runs regionally;
authority `recommend`; wave 3; source "playbook step 6". The analytical lane's step 6 reads: "Track
utilization; promote recurring value into a standard use case; control point: utilization recorded."

## Purpose and definition of done

Ad-hoc work is the lane's fast path: "an answer, not an industrialized solution" (`od-first-aid-kit`).
Most of it should stay ad-hoc. This skill decides, with evidence, which asset should not, and prepares what
the next owner needs so nobody re-derives it. Done when the package states the **decision** (promote, keep
as ad-hoc, or retire), the evidence behind it with sources, which of the catalog conditions are met today
and which are not, the named human who takes it on, and the next step. The decision to commit to
industrialization is the responsible human's, never the agent's (`agent-brief`: "may not commit a use case to
industrialization without the responsible human").

## Where it sits

- **Analytical lane, step 6** (old lane) and **Lane 2 step 6** of the new-state flow: "Implement, adopt and
  graduate to catalog - if repeatable, graduate to a future Lane 1" (VSM skill map). The registry's skills for
  the step are `od-analytics-asset-build`, `od-handover-and-adoption`, `od-use-case-standardization`; the
  graduation into a plant self-serve catalog is `catalog-usecase`, a draft.
- **Feeds UC-02**: use case definition (`od-use-case-definition`), whose Phase 1 is *Collect*: "demand
  logged against plant roadmap". The package is that logged demand, with its evidence attached.
- Handover to the Use Case Support lane: "Recurring, high-value analytics go to the Use Case Support lane
  to become standard use cases" (playbook handover rule).

## References and assets

| File | Use it for |
|---|---|
| [`references/promotion-criteria.md`](references/promotion-criteria.md) | The six tests (recurrence, value, reproducibility, placement, handover, catalog conditions), what evidence answers each, and the promote / keep / retire rule |
| [`references/pattern-evidence.md`](references/pattern-evidence.md) | How to read the portfolio aggregates that frame a promotion (declared standard, library and CSP status, case groups, handover and utilization) with live-count recipes, and what the numbers do not show - no figures |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Graduation conditions, the exchange with the operational-excellence function, promotion template fields, retire versus re-evaluate, handoff contract, agent notes |
| [`assets/promotion-package.md`](assets/promotion-package.md) | The package |

## Procedure

1. **Confirm it is an asset, not an insight.** A one-off insight with no recurring value is closed as ad-hoc,
   and refusing to promote is a valid outcome (`error paths`, analytical lane). Stop here if the request
   was a single question.
2. **Collect recurrence evidence.** Who asked, how many times, for which plants, what changed between
   requests. The sources give no threshold for "recurring": write the evidence, mark the threshold
   `⟨to confirm with the DBVE lead⟩`, and do not invent one.
3. **Collect value evidence.** Utilization of the asset (Scorecard, Use Case Utilization; `NEVER` is a
   recorded value), saving rows with reliability and proven status (`od-benefit-calculation`: tracked and
   proven never added), and the decision the asset supports. No evidence yet: write "to be collected".
4. **Check it can be reproduced.** The data path is written down to the machine and signal; data fitness was
   confirmed (`od-data-availability-check`); signals are standardized so a second plant can consume them
   (`od-signal-standardization`); the asset passed the validation checklist of `od-analytics-asset-build`;
   plant-specific parts are separable as deltas.
5. **Place it.** Search the reference library first (`od-use-case-standardization`): if an entry covers the
   need, the answer is **reuse that entry**, not a new one. Otherwise place it on its capability template
   (one of the capability templates), process group and let the classifier assign the cluster tag; do not
   hand-assign one. Pull the cluster's baseline definition, KPIs and requirement checklist and record only
   the deltas.
6. **Check the handover record.** Plant owner named; the three-question test passed
   (`od-handover-and-adoption`); the plant has used it in a real shift.
7. **State which catalog conditions are met** (`catalog-usecase`): CSP `Yes` recorded; capability template;
   standardized signals; plant owner and handover record. Conditions 2 and 3 there are proposals awaiting
   the OD lead. Say plainly: *prepared for the CSP gate*, never *catalogued*, unless all four hold. A validated
   prototype alone is not enough: it must also be packaged as a configurable application
   (`references/process-chain-practice.md`).
8. **Decide and recommend.** Promote, keep as ad-hoc (with a review date), or retire (low utilization is
   reviewed with the requester or retired). A promote recommendation needs a named responsible human
   (DBVE) who accepts it.
9. **Hand over.** Promote: to `od-use-case-definition` (the Collect phase, with the package as the logged
   demand), prioritization through `od-portfolio-and-savings-analysis` if competing candidates exist, and the CSP
   preparation in `od-use-case-standardization`. Record the outcome so the promotion rate can be counted
   (the lane lists it as a metric with source `⟨tracker — to collect⟩`).

## Output

[`assets/promotion-package.md`](assets/promotion-package.md), one per candidate asset.

## Still open

- `⟨Recurrence threshold⟩` (how many requests, plants or months make an asset "recurring"): not in the
  sources. Supplier: DBVE lead / OD lead.
- `⟨Sequence⟩`: whether an ad-hoc asset must pass full UC-02 definition before it can be proposed for the
  catalog, or whether a proven asset can be assessed against the catalog conditions directly.
- `⟨Who may propose and who may add a catalog entry⟩`, and `⟨where the catalog lives⟩` (open in
  `catalog-usecase`).
- `⟨Promotion rate target and tracker⟩`: the lane metric has no source and no target.
- `⟨Whether a recorded CSP Yes is the right threshold for self-service⟩`, given how few
  library entries have a recorded Yes (`catalog-usecase`; count live).
- `⟨Who takes the CSP decision step⟩` for a new candidate and how often the gate sits (owner outside OD).

## Do not

- Do not industrialize a one-off insight, or commit a use case to industrialization without the
  responsible human.
- Do not call an entry catalogued, standard or "CSP-approved" without a recorded CSP `Yes`; the CSP
  decision is not this skill's.
- Do not create a new capability template or process group to fit one asset
  (`od-use-case-standardization`).
- Do not hand-edit a cluster tag; fix the input fields and re-run the classifier.
- Do not report a saving without its source, or add tracked and proven euros; a missing figure is
  "to be collected", not zero.
- Do not count templates, library entries or case groups as evidence that a promotion is warranted:
  adoption by a second plant is the measure.
