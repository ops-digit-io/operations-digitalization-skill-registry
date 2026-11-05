---
name: od-decision-routing
description: >-
  Answer "am I allowed to do this, and if not who decides?" for OD work — map a decision
  to its owner, mode, approval requirement, reversibility, threshold and authority level;
  route spend through eCR, IT demand through demand management, rollout readiness through
  CSP, daily use through the plant and proven value through SPRINT; and escalate to the
  right forum. Use before committing spend, approving an integration or a connection,
  changing a standard or a rollout, or whenever it is unclear whether an action is
  recommend, execute-with-approval or execute-autonomously.
license: MIT
metadata:
  id: od-decision-routing
  tier: practice
  lane: all
  owner_role: OD lead
  authority_level: read-only — this skill routes decisions, it never takes them
  status: stable
  sources_read: 2026-10-22
  requires: [od-context]
  derived_from:
    - ops-knowledge-graph/.../00-core/08-decision-rights.md
    - ops-knowledge-graph/_knowledge/10-Department/Decision rights.md
    - ops-knowledge-graph/.../00-core/09-risks.md
    - Rogers, P. and Blenko, M. (2006). Who Has the D? How Clear Decision Roles Enhance Organizational Performance. Harvard Business Review, 84(1), 52-61. The RAPID decision-rights framework (Recommend/Agree/Input/Perform/Decide), verified via Bain & Company's own summary, 2026-10-22 — grounds this skill's Tandem/Consultation/Information modes.
    - personal vault, Work-OpsDigit-Knowledge/Split Slides/D-Operations Digitalization--2024#9-ODEC*.pptx and --2024#1-CoP_Call*.pptx (ODEC and CoP call decks, split-slide export), read 2026-10-22 — resolves PHASE1-ELICITATION.md topic 4 (ODEC-vs-COP worked examples) from the department's own record rather than from memory.
  okf:
    type: Agent Skill
    title: Decision routing and escalation
    tags: [all, practice]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---

# Decision routing and escalation

Read `od-context` first.

## The references are the substance

| File | Use it for |
|---|---|
| [`references/decision-rights-framework.md`](references/decision-rights-framework.md) | Why Tandem/Consultation/Information are a cited framework (Bain's RAPID), not a house convention — and how to pick a mode for a decision not yet in the table |
| [`references/escalation-worked-examples.md`](references/escalation-worked-examples.md) | Illustrative patterns, from the historical ODEC and COP records, on the strategic/technical split within one topic (cybersecurity), a blocker that stays at COP, and what happens when COP under-delivers |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | Small change versus project, what may enter routing, decisions as decision / proposal / risk of not doing, the operations-concept gate, board patterns, and what an agent may draft |

**The function proposes; other people decide.** Most portfolio gates sit
outside OD. The work that reliably moves is the work where the gate was identified at
intake and the owner was named. **The work that stalls is almost never stuck on
engineering.**

## Decision rights inside OD

| Decision | Role | Together with | Mode | Approval | Reversible | Threshold | `authority_level` |
|---|---|---|---|---|---|---|---|
| Use-case prioritization & selection | DBVE | Plant ME | Tandem | no | yes | within plant roadmap scope | `recommend` |
| Equipment integration go-ahead | IIAE | Plant ME / Plant IT | Tandem | **yes** | partially | per investment plan; Cyber Security sign-off for external connection | `execute-with-approval` |
| Digitalization investment planning | OD lead | BA Operations | Consultation | **yes** | no | ⟨budget threshold — to confirm⟩ | `recommend` |
| Tool/system rollout (MES, MSB, IIoT Edge, the data platform…) | OD lead | ⟨counterpart to confirm⟩ | Tandem | **yes** | no | strategic-plant scope | `execute-with-approval` |
| Data-model / signal standardization | IIAE | Plant ME / Plant IT | Consultation | no | yes | must stay consumable by every plant's instance of the capability | `recommend` |
| Machine standards for digital connection | OD lead | Manufacturing Engineering | Consultation | **yes** | partially | aligned with M+E standards | `recommend` |
| Ad-hoc analytics delivery | DBVE | — | — | no | yes | read-only on source systems | `execute-autonomously` |

**Modes.** *Tandem* — both must agree. *Consultation* — hear, then decide alone.
*Information* — tell, do not ask.

**Authority levels**, lowest to highest: `read-only` → `draft` → `recommend` →
`execute-with-approval` → `execute-autonomously`. "Reversible" alone is not enough to
decide; the level and the threshold together are what make "is this allowed?" answerable.

## The five gates outside OD

| Gate | Route | Threshold / state |
|---|---|---|
| **Spend** | eCR (electronic capital request) | Approval ladder per the current approval policy (look up: Controlling / eCR process owner) — a ladder, not alternatives |
| **Demand on IT platforms** | IT demand management + demand evaluation board | anything touching a platform OD does not own |
| **Standard enough to roll out** | CSP decision, per reference-library entry | decision recorded per library entry (`Yes` / `No` / not yet decided) |
| **Into daily use** | The plant | OD can deliver and hand over; only the plant makes it `PRODUCTIVE` |
| **Value is proven** | SPRINT portfolio review | saving rows marked proven after review (count live) |

`ECR APPROVAL` and `ECR CREATION` appear on saving rows as recorded
dependencies (filter the `Dependency` field live to see how many). The spend gate is not
theoretical — it is a common recorded reason a booked saving is not yet real.

## Deputisation

In the OD lead's absence, ⟨deputy — to confirm⟩ decides prioritization and rollout matters
**within the agreed roadmap**. Investment commitments wait for the OD lead. No level of
urgency substitutes.

## What an agent may never do, at any authority level

Sign off acceptance · connect a machine or write to a production system · approve an
external connection without Cyber Security / OT sign-off · commit investment or allocate
resources · change a signal or data-model standard · make licensing commitments
· publish externally · commit a use case to industrialization without the responsible
human · present unvalidated insight as fact.

## Escalation

**→ OD lead** for strategy, priority, rollout and blocked projects, in the
deciding role or forum named in the current approval policy (look up); via **COP**
for technical matters — connection barriers, failed acceptance, missing operations
concepts. ODEC is a historical forum and a source of information (past decisions, decks,
facts), not a current route; no recurring governance meeting is prescribed.

Escalate on these triggers from the risk register:

| Risk | Escalation trigger |
|---|---|
| Missing operations concept for the data platform / MSB / MDA-PDA | Rollout blocked at a strategic plant |
| Key-person / staffing gaps (open roles in a region) | Open role beyond the agreed tolerance ⟨to confirm⟩ |
| Limited internal IT knowledge (the data platform, MDA/PDA) | A single point of failure identified |
| External tooling dependence (MES/ERP, licensing) ⟨owner to confirm⟩ | Decision delayed past plan |
| Cyber Security / OT exposure on machine connection | A security gap on a connected asset |
| Value not materializing from investment | Impact below target for the quarter |

## Procedure

1. Name the decision in the table, or the gate it hits.
2. Read off the owner, the mode, the threshold and the authority level.
3. If the required level is above yours, produce the recommendation and route it — do not
   narrow the action until it fits your level.
4. Record the gate as a **dependency** on the use case or saving row so it stays visible. Write the decision as decision, proposal, risk of not doing.
5. Escalate on the trigger, to the deciding role or forum named in the current approval policy (look up), inside the agreed window.

## Output — the protocol

Fill [`assets/decision-request.md`](assets/decision-request.md) per decision, not as a
mental note: which row or gate, what the table says, how it was routed, and the outcome —
so a decision that stalled has a record of where, not just a memory of it.
