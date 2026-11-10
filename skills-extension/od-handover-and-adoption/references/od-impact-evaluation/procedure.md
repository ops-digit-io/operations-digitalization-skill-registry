---
type: Skill Reference
title: Procedure
description: Formerly the skill od-impact-evaluation, absorbed into od-handover-and-adoption on 2026-11-10 to remove duplication against the department context. Evaluate the impact of a use case that is live in a plant and prepare the adoption confirmation record - what the use case is used for, how often, what changed in the process, what saving can be shown and at what firmness (calculated, estimated, linked to a SPRINT project, proven), and what the plant owner still has to confirm. Drafts the evaluation; the plant confirms adoption. Use when a use case has been live for a while and the lane's last step is due, when the Scorecard shows low or NEVER utilization, when a saving needs a methodology before it goes to SPRINT, or when a delivered use case
resource: ../../SKILL.md
status: draft
owner: human:jakob.gabriel
tags:
- use-case-support-service
- practice
- impact
- adoption
- absorbed
derived_from:
- ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
- ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/use-case-support-service/playbook.md
- ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/use-case-support-service/tasks.md
- ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/use-case-support-service/metrics.md
- ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/use-case-support-service/agent-brief.md
- ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/04-service-catalog.md
- Work vault (Work-OpsDigit-Knowledge), Slide Index and Split Slides of 03-AMT_MI_Standard_Agenda_Use_Case_Workshop (Use Case Creation Process slides 7, 18, 19, 20; Workshop Summary slide 20; template Use Case Utilization), read 2026-11-05
- Work vault (Work-OpsDigit-Knowledge), Slide Index of 10-Workshops (Dolne Vestenice 2025 integration workshop purpose and utilization slides; Carei 2025 integration workshop), read 2026-11-05
- Work vault (Work-OpsDigit-Knowledge), Case Groups overview and CG-03 Andon Board - Assembly (section 4 recorded savings, evidence gap, section 7 derivation sheet), read 2026-11-05
- Work vault (Work-OpsDigit-Knowledge), Graph/Business Cases Catalog Maturity Sprint (validation plan pattern), read 2026-11-05
- Skill bc-build SKILL.md and references/review-checklist.md (saving rows, tracked versus proven, calculator)
- Skill od-handover-and-adoption SKILL.md, references/evidence-of-adoption.md and assets/handover-protocol.md
generated:
  by: claude-code/1
  at: 2026-11-05 00:00:00+00:00
---
# Impact evaluation

> **Absorbed.** This was the skill `od-impact-evaluation`. It now runs as a mode of [`od-handover-and-adoption`](../../SKILL.md) (merged 2026-11-10, see `log.md`). Its authority stays as it was: draft the evaluation; the plant confirms adoption.

Read `dept-os` first. Playbook step 7: "Evaluate use-case impact; ensure adoption into daily
process" — control point "Impact evaluated; recipient confirms adoption". After go-live the plant
evaluates its use cases; OD provides the calculator and the method and reviews the result. This skill **drafts the
evaluation** on that basis. It never declares adoption: only the plant can (`od-handover-and-adoption`: "adoption
is the plant's decision"), and only SPRINT can make a saving proven (`bc-build`).

Trigger in the plan (UC-06): "use case live for ⟨n⟩ weeks". ⟨n⟩ is not set in any source read. Until
the OD lead sets it, use the practical triggers in the description above and write the date you used.

## What this skill adds, and what it leaves to neighbours

| Question | Answered by |
|---|---|
| Was the handover complete, which ADKAR element blocks adoption, which evidence tier exists? | `od-handover-and-adoption` (do not repeat; reuse its protocol section 4 and 5) |
| How is a saving row built, what is tracked versus proven? | `bc-build` |
| How are several use cases or a portfolio read? | `od-portfolio-and-savings-analysis` |
| **How did the use case perform against what was promised, how firm is each saving, what step takes it up one level of firmness, and what does the plant owner sign?** | **this skill** |

## References and asset

| File | Use it for |
|---|---|
| [`references/savings-proof-path.md`](references/savings-proof-path.md) | The path a saving takes from pre-evaluation to proven, the gates on it, and the common ways it stalls |
| [`references/evaluation-questions.md`](references/evaluation-questions.md) | What to ask the plant owner and what to read in the systems, mapped to OD's utilization template and the Use Case Canvas success criteria |
| [`assets/impact-evaluation-record.md`](assets/impact-evaluation-record.md) | The output: evaluation and adoption confirmation record |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Deployed is not used, the savings-forecast gate at sprint close, the utilisation table, dashboard-to-paper reconciliation, who attests value, and what an agent may draft |

## Procedure

1. **Open the promise.** Take the definition protocol (`od-use-case-definition`) and the business
   case rows (`bc-build`): stated objective, benefit class, expected saving per row,
   methodology, dependency, named plant owner. If a promise was never written, say so in the record;
   do not reconstruct one from the finished dashboard.
2. **Check the handover first.** Pull sections 1 to 4 of `od-handover-and-adoption`'s protocol. If
   the three-question test fails or the data path is not written to the machine, the impact cannot be
   evaluated yet: work that gap, do not score around it.
3. **Collect usage evidence, strongest tier first** (`od-handover-and-adoption`,
   `references/evidence-of-adoption.md`): system usage record; named owner's dated statement; third
   party observation. Record the tier actually obtained.
4. **Fill OD's utilization description** with the plant owner: who uses it, related process (the
   moment in the day), how it is used in one to three sentences including the initial state without
   digital support, utilization rate (Daily, Weekly, Monthly, On-Demand, Never), impact or potential
   (Low, Medium, High), plant management relevant (yes or no, with the reason). This is the template
   OD already shows at workshops ([`references/evaluation-questions.md`](references/evaluation-questions.md)).
5. **Establish what changed in the process**: which decision or action now differs, who takes it,
   how often. A dashboard being open is not an impact; the action it triggers is.
6. **Evaluate each saving row against the proof path**
   ([`references/savings-proof-path.md`](references/savings-proof-path.md)): is there a baseline, a
   methodology line a stranger can check, a dependency, a SPRINT link? Mark each row with its
   current firmness and the next step. Where no saving was ever recorded, say "not recorded"; the
   vault shows delivered cases in this state, which is common, not a failure of yours.
7. **Decide the outcome** and let the plant owner confirm the adoption part:

| Finding | Outcome | Next |
|---|---|---|
| Tier 1 or 2 evidence, change named, rows firm | Adoption confirmed by the plant owner; hand rows to `bc-build` for SPRINT | `od-scorecard-reporting` cadence |
| Used, but no baseline or methodology for the saving | Adoption confirmed; saving stays `ESTIMATION` or unrecorded with a named gap | Collect the baseline; re-evaluate |
| Not used or `NEVER` | No adoption claim | ADKAR diagnostic in `od-handover-and-adoption`; review with requester; retire if justified |
| Used at one plant only, wanted elsewhere | Impact recorded; adoption gap elsewhere | `od-use-case-standardization` |
| Integration or acceptance fails after handover | Rework loop to step 5 of the playbook | Information Integration lane |

8. **Draft the record and send it to the plant owner.** The adoption confirmation is the plant
   owner's dated statement. If the owner does not respond, record "confirmation pending, requested
   ⟨date⟩"; do not write adopted.
9. **Close the loop upstream.** Feed the finding to `od-retro` (what the definition promised versus
   what happened) and, if training was the barrier, `od-rollout-training`.

## Definition of done

The record is filled; every saving row is shown at its true firmness with the next step and owner;
the adoption section is signed by the plant owner or explicitly pending; nothing reports tracked and
proven euros as one total.

## What is still open

- ⟨n weeks live before evaluation⟩ — plan UC-06 leaves it open. Supplier: OD lead.
- ⟨Impact evaluation template⟩ — `tasks.md` of the lane says "template — to confirm"; the record in
  `assets/` is the working version, built from OD's own utilization template and the Canvas success
  criteria. Supplier of the official one: DBVE.
- ⟨SPRINT acceptance criteria⟩ — no source read says what SPRINT routinely rejects (also open in
  `bc-build`). Supplier: whoever attends the SPRINT review.
- ⟨Utilization target⟩ — "to confirm" in the lane metrics. Supplier: OD lead.
- ⟨Plant-side owner for confirmation⟩ — the department has no plant-side lane owner yet (OD skill
  map, open gaps). Supplier: OD lead.

## Do not

- Do not close a sprint or an evaluation while savings baseline, forecast and registered project are missing (forecast gate in `references/process-chain-practice.md`).
- Do not accept a dashboard as valid before it is reconciled with the paper process, and do not count a dashboard without an action owner as impact.
- Do not mark adoption confirmed without the plant owner's dated statement.
- Do not turn a missing figure into zero or an estimate into a calculation.
- Do not add tracked and proven euros together, or report a plant's saving as a department total.
- Do not use a handover marked `DONE` or status `IMPLEMENTED` as evidence of use.
- Do not claim a saving before a baseline exists; name the baseline as the gap.
- Do not repeat the ADKAR diagnostic here; run it in `od-handover-and-adoption`.
