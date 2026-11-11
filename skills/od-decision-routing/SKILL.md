---
name: od-decision-routing
description: >-
  Answer "am I allowed to do this, and who decides?" for OD work: map a decision to its owner, approval and authority level. Not for assigning a request to a lane (od-use-case-intake-triage).
license: MIT
metadata:
  id: od-decision-routing
  tier: practice
  lane: all
  new_state_lane: "Lane 1b (1b2), Lane 2 (25), Lane 3 front-end (32)"
  new_state_step: "Cost template, approved by the plant budget owner; Capital request if investment is needed; Tool-decision / IT-footprint gate (make, buy, integrate or connect)"
  owner_role: OD lead
  tags: [all, practice]
  authority_level: read-only — this skill routes decisions, it never takes them
  status: stable
  requires: [od-context]
  composes: [od-investment-input, it-demand-package]
  okf:
    type: Agent Skill
    title: Decision routing and escalation
    tags: [all, practice]
---

# Decision routing and escalation

## Purpose

Answer "am I allowed to do this, and if not who decides?" for OD work: map a decision to its owner role, mode, approval, threshold and authority level, and escalate to the right forum. Use it before committing spend, approving an integration or connection, or changing a standard or a rollout.
- **Outputs:** [`references/outputs.md`](references/outputs.md) lists what this skill must deliver, to whom, and when each output is complete.

## Inputs and output

Inputs: the decision or action in question, the use case or saving row it touches, and the decision-rights tables below. Output: a filled [`assets/decision-request.md`](assets/decision-request.md) naming the row or gate, what the table says, how it was routed and the outcome.

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
| Digitalization investment planning | OD lead | BA Operations | Consultation | **yes** | no | the eCR amount tiers ([approval matrix](../od-capital-request/references/ecr-approval-matrix.md)) | `recommend` |
| Tool/system rollout (MES, MSB, IIoT Edge, the data platform…) | OD lead | IT-responsible role of the business side | Tandem | **yes** | no | strategic-plant scope | `execute-with-approval` |
| Data-model / signal standardization | IIAE | Plant ME / Plant IT | Consultation | no | yes | must stay consumable by every plant's instance of the capability | `recommend` |
| Machine standards for digital connection | OD lead | Manufacturing Engineering | Consultation | **yes** | partially | aligned with M+E standards | `recommend` |
| Lane 1b standardized-system cost (cost template) | Plant budget owner | DBVE (OD supplies the template) | — | **yes** | partially | pre-priced standardized spend only; anything non-standard goes to Lane 3; pre-approval bands recorded 2026 (below 25 kEUR and 25 to 100 kEUR through an automated workflow, central approval at 25 kEUR per a review note, local approval first): see `od-capital-request`, spend route, owner to confirm | `recommend` (OD prepares; the plant budget owner approves) |
| Lane 3 tool decision / IT-footprint gate | OD lead | IT (solution design) | Tandem | **yes** | no | mandatory for every Lane 3 demand; routes 3a.1-3a.4 or 3b | `recommend` |
| Application ownership transfer to IT or another team | Receiving team | Current owner (builder) | Tandem | **yes** | partially | only on formal acceptance; until then the builder runs it | `recommend` |
| Ad-hoc analytics delivery | DBVE | — | — | no | yes | read-only on source systems | `execute-autonomously` |
| Lane 4 outbound use-case story (proposed; not in the department decision rights) | DBVE | Plant owner; Internal Communications | Tandem | **yes** | no (a published item can only be corrected or withdrawn by IC) | only a live, adopted use case; plant owner consents; every figure with an evidence class; no individuals, hosts or supplier detail | `recommend` (OD drafts; IC publishes) ⟨to confirm with the OD lead⟩ |

The three rows above the last are from the department's new-state lane files (Lane 1 step 3b, Lane 3
step 2) and the OD x IT alignment of 2026-09-11; `08-decision-rights.md` does not carry them yet.
That file's `valid-until` was 2026-11-10. **Until the OD lead re-verifies it, every row is used at most at
`recommend`**: route the decision to its owner, never act on a row's `execute-with-approval` or
`execute-autonomously` alone, and note "decision rights pending re-verification" on the decision request.

**Modes.** *Tandem* — both must agree. *Consultation* — hear, then decide alone.
*Information* — tell, do not ask.

**Authority levels**, lowest to highest: `read-only` → `draft` → `recommend` →
`execute-with-approval` → `execute-autonomously`. "Reversible" alone is not enough to
decide; the level and the threshold together are what make "is this allowed?" answerable.

## The five gates outside OD

| Gate | Route | Threshold / state |
|---|---|---|
| **Spend** | eCR (electronic capital request) | The recorded approval matrix: three amount tiers, approvers by role and by case type (IT invest adds IT Controller and, from the middle tier, CIO) - [`ecr-approval-matrix.md`](../od-capital-request/references/ecr-approval-matrix.md); a ladder, not alternatives. Confirm it still applies under neuwerk (Finance) |
| **Demand on IT platforms** | IT demand management + demand evaluation board | anything touching a platform OD does not own |
| **Standard enough to roll out** | CSP decision, per reference-library entry | decision recorded per library entry (`Yes` / `No` / not yet decided) |
| **Into daily use** | The plant | OD can deliver and hand over; only the plant makes it `PRODUCTIVE` |
| **Value is proven** | SPRINT portfolio review | saving rows marked proven after review (count live) |

`ECR APPROVAL` and `ECR CREATION` appear on saving rows as recorded
dependencies (filter the `Dependency` field live to see how many). The spend gate is not
theoretical — it is a common recorded reason a booked saving is not yet real.

## Deputisation

In the OD lead's absence, the next-higher management role decides prioritization and rollout matters
**within the agreed roadmap**. Investment commitments stay with the competent approval body. No level of
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

## Human gate and AI-agent notes

An agent may look up the row, draft the decision request, state the recommendation and record the gate as a dependency. The decision itself stays with the named role in the table: the DBVE, IIAE, OD lead, plant budget owner, plant owner, receiving team or Cyber Security role, as the row says. Until the OD lead role re-verifies the decision rights, every row is used at most at `recommend`.

## Example

Fictional example (all values invented for illustration):

```text
Input : "Can we order a connection kit for Plant X?"
Lookup: row "Equipment integration go-ahead": role IIAE with Plant ME / Plant IT, Tandem,
        approval yes, Cyber Security sign-off for an external connection
Output: decision request: routed to IIAE (Tandem); agent level recommend; gate recorded as
        dependency; outcome: waiting for sign-off
```

If it fails: when no row or gate fits, or the rights look out of date, validate with the OD lead role and write "decision rights pending re-verification"; do not act on the row.

## Definition of done

The decision request names the row or gate, the deciding role, the mode, the authority level and the outcome; the gate is recorded as a dependency on the use case or saving row; escalation has been sent to the named role or forum when a trigger was met.

## Do not

- Do not act on a row above `recommend` while the decision rights are pending re-verification.
- Do not narrow an action until it fits your authority level; produce the recommendation and route it.
- Do not treat urgency as a substitute for the deciding role or the approval body.
