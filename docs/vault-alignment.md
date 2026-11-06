---
type: Design Record
title: Vault alignment
description: Cross-check of this registry's 24 skills against the department's own 33-skill build plan and gap analysis, with the resulting build order.
resource: ../registry.yaml
status: stable
owner: human:jakob.gabriel
tags: [derivation, roadmap]
generated: { by: claude-code/1, at: 2026-09-17T00:00:00Z }
---

# Vault alignment

This registry was derived from the `ops-knowledge-graph` bundle (see
[`derivation.md`](derivation.md)). Separately, and earlier, the same knowledge base carried
its own build plan for an OD skill repository —
`OperationsDigitalization-Department/OD_Skill_Map.md` — under different skill IDs (`UC-01`,
`II-04`, `P-02`, `O-08`...) and a working checklist, `Vault Gap Analysis — Working Items.md`
(2026-09-16), that names the tacit knowledge blocking it. Neither document names or is aware
of this registry by its actual skill names. This note reconciles the three: what the plan
called for, what got built, and what is still missing — so the divergence is recorded rather
than silently absorbed.

## Crosswalk

| Plan ID (Wave) | Plan's proposed name | Built as | State |
|---|---|---|---|
| UC-01 (**W1**) | `od-uc-intake-triage` | `od-use-case-intake-triage` | stub — refusal-in-practice not written |
| UC-02 (**W1**) | `od-uc-define` | `od-use-case-definition` | stub |
| UC-03 (**W1**) | `od-uc-requirements-breakdown` | `od-requirements-breakdown` | deep — 5 refs, 2 scripts |
| UC-04 (**W1**) | `od-uc-benefit-case` | `od-benefit-calculation` | stub — review method not written |
| UC-05–08 (W2/W3) | prioritize / impact / workshop / first-aid | `od-use-case-solution-evaluation` partially covers "impact" | prioritize/workshop/first-aid not built |
| II-01 (**W1**) | `od-ii-equipment-assessment` | `od-equipment-integration` (assessment route) | documented — barrier-class judgement resolved 2026-09-17, `references/barrier-classes.md` |
| II-02 (**W1**) | `od-ii-integration-roadmap` | folded into `od-equipment-integration` (assessment route) | not separated |
| II-03 (**W1**) | `od-ii-machine-integration` | `od-equipment-integration` (guidance route) | documented, 7 refs. Merged with II-01/II-02 into one skill, 2026-09-17 — see [`derivation.md`](derivation.md) |
| II-04 (**W1**) | `od-ii-signal-standardization` | `od-signal-standardization` | deep |
| II-05 (W2) | `od-ii-acceptance-test` | `od-acceptance-test` | documented, 2026-10-22 — FAT/SAT + ISO/IEC/IEEE 29119 |
| II-06 (**W1**) | `od-ii-cybersec-gate` | — | **not built** |
| II-07–08 (W2) | investment input / barrier triage | — | not built |
| PS-01 (W2) | `od-ps-project-kickoff` | `od-project-support-consultancy` (lane stub) | not separated |
| PS-02 (**W1**, "the decentralization skill") | `od-ps-rollout-training` | — | **not built** |
| PS-03 (W2) | `od-ps-adoption-handover` | `od-handover-and-adoption` | documented, 2026-10-22 — ADKAR |
| PS-04 (W3) | application consulting | — | not built |
| AS-01–02 (W2) | request scoping / diagnostics | `od-analytical-support-service` (lane stub), `od-data-availability-check` | partial |
| AS-03 (W3) | `od-as-asset-build` | `od-analytics-asset-build` | documented, 2026-10-22 — Kimball Lifecycle + Few's dashboard design |
| AS-04 (W3) | industrialize | — | not built |
| P-01 (**W1**) | `od-p-data-availability` | `od-data-availability-check` | deep |
| P-02 (**W1**) | `od-p-system-fit-check` | `od-system-fit-check` | documented, 2026-10-22 — tool boundaries + non-bets + per-plant deployment reality |
| P-03 (**W1**) | no-invented-figures | folded into `od-context`'s honesty rules | covered, not standalone |
| P-04 (**W1**) | handover-packet | folded into `od-acceptance-test` / `od-handover-and-adoption` | covered, not standalone |
| P-05 (**W1**) | `od-p-escalation-routing` | `od-decision-routing` | stub — ODEC-vs-COP boundary cases not written |
| P-06 (W2) | template-resolution | — | not built |
| P-07 (**W1**) | decision-authority | folded into `od-decision-routing` | covered |
| P-08 (W2) | cross-plant compatibility | — | not built |
| O-01 (**W1**) | metrics-pull | `od-scorecard-reporting` | documented, 2026-10-22 — ISO 22400-2 + Balanced Scorecard; 4 tacit placeholders still open |
| O-02–07, 09 (W2/W3) | scorecard update / portfolio sweep / odec-cop prep / retro / risk-watch / onboarding | `od-portfolio-and-savings-analysis` (documented, 2026-10-22 — PMI portfolio standard), `od-scorecard-reporting` (partial) | mostly not separated |
| O-08 (**W1**, "keeps every other skill honest") | `od-o-context-freshness` | — | **not built** |

Not on the plan at all, and additions from the technical corpus instead: `od-node-red-flows`, `od-use-case-standardization`, `od-sharepoint-list-export`,
`build-grafana-ops-dashboard` (vendored). These came from mining the Node-RED flow corpus and the
`20-Done/` record directly, a source the skill map did not have in front of it.

`od-use-case-solution-evaluation` (added 2026-10-22) is a further addition from outside the
plan, generalized from two external academic papers (Schott et al. 2017, 2020) rather than
from this registry's own sources — see the skill's `derived_from`. It partially covers the
plan's never-built UC-04 "impact" step: a use case's envisioned solution checked against a
16-area IT/OT capability model, not the prioritize/workshop/first-aid parts of that wave.

## What this settles

**Three Wave-1 skills the plan calls load-bearing still have no equivalent anywhere in the
registry:** `od-ii-cybersec-gate`, `od-ps-rollout-training`, `od-o-context-freshness`.
`od-p-system-fit-check` was the fourth — built 2026-10-22 as `od-system-fit-check`, from the
department's own tool-boundary cards and Smart Factory Tool Availability snapshots rather
than from a fresh interview.

**The build order diverged from the plan's own recommendation.** The plan said: build the
`P-*` procedures first (they are dependencies), then `UC-01→04`, then `II-01→04`, then
`PS-02`, then `O-01`/`O-08`. What actually went deep was picked by inbound-composition count
instead (`od-requirements-breakdown`, `od-data-availability-check`, `od-signal-standardization`,
`od-node-red-flows`) — a defensible metric, and it left `P-02` and `O-08`
untouched for most of the registry's life; `P-02` is no longer one of them.

**All six tacit-knowledge items the plan names ("★ What only you can supply") now have a
skill, five of them resolved (three fully, two partially with an honestly-named residual
question).** What makes a requirements spec integration-ready got resolved as a side effect
of `od-requirements-breakdown` going deep; the connectability judgement (II-01) was resolved
by direct elicitation on 2026-09-17,
recorded in `od-equipment-integration/references/barrier-classes.md`; and three more —
ODEC-vs-COP routing (P-05), refusal in practice (UC-01, partially), and
benefit-calculation review (UC-04, partially) — were resolved on 2026-10-22 not by
interview but by mining the department's own call decks and workshop retrospectives
directly in `Work-OpsDigit-Knowledge/Split Slides/`. Each of those three still carries one
narrower residual question the mined record does not answer (see each reference file's own
"what is still open" section) — real evidence closed most of the gap, not all of it.

| Tacit item (plan's own wording) | Blocks | Status |
|---|---|---|
| UC-03 — what makes a spec integration-ready | `od-requirements-breakdown` | resolved |
| II-01 — connectability judgement (cheap / expensive / no route) | `od-equipment-integration` | resolved 2026-09-17 |
| P-05 — ODEC vs. COP in practice, which blocker to which | `od-decision-routing` | resolved 2026-10-22, from the department's own call decks |
| UC-01 — refusal in practice, what plants push back on | `od-use-case-intake-triage` | resolved 2026-10-22 (partially) — pushback phrasing still open |
| UC-04 — benefit-calculation method, which claims survive review | `od-benefit-calculation` | resolved 2026-10-22 (partially) — specific SPRINT rejection reasons still open |
| P-02 — when a demand quietly requires a non-bet system | `od-system-fit-check` | resolved 2026-10-22 (partially) — the tell and the redesign/escalate response are real; a named real "looked normal, secretly needed MES" case is still open |

## Build order

**Phase 1 — elicit the open tacit-knowledge items** and write each into a rich reference set
on its target skill (`od-equipment-integration` — done, 2026-09-17; `od-benefit-calculation`,
`od-use-case-intake-triage`, `od-decision-routing` — open), plus draft the missing
`od-system-fit-check` skill from the fifth item. In progress — see each skill's
`sources_read` date and `references/` for status.

**Phase 2 — the other three missing Wave-1 skills**, which do not need an elicitation
session, only drafting from material already written elsewhere in the registry:
`od-cybersec-gate` (source: the guardrails already in `od-information-integration-service`
and the escalation triggers in `od-decision-routing`), `od-context-freshness` (source: the
`sources_read` / unverified convention every skill already carries), and
`od-rollout-training` — folded into Phase 1 instead, because the plan calls it
under-specified in the same way as the tacit items ("needs the most new content").

**Phase 3 — deepen the registry's own top picks** (`docs/skill-state-map.md`'s "what is next"):
`od-acceptance-test`, `od-use-case-standardization`, `od-handover-and-adoption` — **done,
2026-10-22**, along with `od-scorecard-reporting`, `od-portfolio-and-savings-analysis`,
`od-analytics-asset-build` and `od-sharepoint-list-export` in the same pass (all research-
grounded: FAT/SAT + ISO/IEC/IEEE 29119, ADKAR, ISO 22400-2 + Balanced Scorecard, PMI's
portfolio standard, the Kimball Lifecycle, and real Graph-API export patterns respectively —
see each skill's own `derived_from`). These reinforced Phase 1 rather than competing with it:
handover and acceptance are exactly where the adoption-confirmation gap (`registry.yaml`
`open_gaps`) lived. Each skill's `assets/*.md` protocol was written to be the next skill's
own input, so the Use Case Support and Project Support lanes now chain end to end without a
gap in the hand-off format. Still open from this batch: `od-scorecard-reporting`'s own
tacit-knowledge placeholders (utilization-rate target, asset-mix target, value-delivery-cycle
system/target, escalation window) and `od-handover-and-adoption`'s evidence-tier ranking,
which is a proposal pending confirmation, not a closed fact.

**Phase 4 — opportunistic.** The remaining Wave-2/3 plan items with no equivalent
(`od-uc-prioritize`, `od-ii-integration-roadmap`, `od-ii-barrier-triage`, plant onboarding,
retro, risk-watch) and the `registry.yaml` open-gap items that unblock a specific skill going
deep, rather than the majority of open gaps, which are data-quality findings about the
machine estate with no skill attached.

## Constraint carried into every phase

Every skill in this registry must read as a standalone procedure — nothing in a `SKILL.md`
or its `references/` names the knowledge base it was derived from, an Obsidian vault, or any
file path outside this repository. Provenance belongs in `metadata.derived_from` (machine-
readable, in the frontmatter a person does not read as prose) and in this doc, never in the
skill body. Content elicited directly rather than mined from a written source is marked
`origin: elicited` with a `derived_from` entry naming the interview and its date, exactly as
honestly as a mined figure is marked with the corpus it came from.
