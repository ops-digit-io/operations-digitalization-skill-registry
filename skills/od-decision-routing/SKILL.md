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
license: Internal — OESL MPEE Operations Digitalization. Not for external distribution.
metadata:
  id: od-decision-routing
  tier: practice
  lane: all
  owner_role: OD lead (Thomas Zipf)
  authority_level: read-only — this skill routes decisions, it never takes them
  status: stable
  last_verified: 2026-08-10
  requires: [od-context]
  derived_from:
    - ops-knowledge-graph/.../00-core/08-decision-rights.md
    - ops-knowledge-graph/_knowledge/10-Department/Decision rights.md
    - ops-knowledge-graph/.../00-core/09-risks.md
---

# Decision routing and escalation

Read `od-context` first.

**The function proposes; other people decide.** Four of the five portfolio gates sit
outside OD. The work that reliably moves is the work where the gate was identified at
intake and the owner was named. **The work that stalls is almost never stuck on
engineering.**

## Decision rights inside OD

| Decision | Role | Together with | Mode | Approval | Reversible | Threshold | `authority_level` |
|---|---|---|---|---|---|---|---|
| Use-case prioritization & selection | DBVE | Plant ME | Tandem | no | yes | within plant roadmap scope | `recommend` |
| Equipment integration go-ahead | IIAE | Plant ME / Plant IT | Tandem | **yes** | partially | per investment plan; Cyber Security sign-off for external connection | `execute-with-approval` |
| Digitalization investment planning | OD lead | BA Operations | Consultation | **yes** | no | ⟨budget threshold — to confirm⟩ | `recommend` |
| Tool/system rollout (MES, MDL, MSB, IIoT Edge…) | OD lead | ContiTech central | Tandem | **yes** | no | strategic-plant scope; ContiTech interface compatibility | `execute-with-approval` |
| Data-model / signal standardization | IIAE | ContiTech central | Consultation | no | yes | must maintain ContiTech interface compatibility | `recommend` |
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
| **Spend** | eCR (engineering change request) | **CTO up to €150k · Board above €75k** — a ladder, not alternatives |
| **Demand on IT platforms** | IT demand management + demand evaluation board | anything touching a platform OD does not own |
| **Standard enough to roll out** | CSP decision, per reference-library entry | applied to 51 of 100: 5 `Yes`, 46 `No` |
| **Into daily use** | The plant | OD can deliver and hand over; only the plant makes it `PRODUCTIVE` |
| **Value is proven** | SPRINT portfolio review | 19 of 553 saving rows, €653,820 |

`ECR APPROVAL` and `ECR CREATION` together appear on 20 saving rows as recorded
dependencies. The spend gate is not theoretical — it is the most common recorded reason a
booked saving is not yet real.

## Deputisation

In the OD lead's absence, ⟨deputy — to confirm⟩ decides prioritization and rollout matters
**within the agreed roadmap**. Investment commitments wait for the OD lead. No level of
urgency substitutes.

## What an agent may never do, at any authority level

Sign off acceptance · connect a machine or write to a production system · approve an
external connection without Cyber Security / OT sign-off · commit investment or allocate
resources · change a signal or data-model standard · make ContiTech licensing commitments
· publish externally · commit a use case to industrialization without the responsible
human · present unvalidated insight as fact.

## Escalation

**→ OD lead (Thomas Zipf)**, via **ODEC** for strategy, priority, rollout and blocked
projects; via **COP** for technical matters — connection barriers, failed acceptance,
missing operations concepts.

Escalate on these triggers from the risk register:

| Risk | Escalation trigger |
|---|---|
| Missing operations concept for MDL / MSB / MDA-PDA | Rollout blocked at a strategic plant |
| Key-person / staffing gaps (open roles Asia, Americas) | Open role beyond ⟨n⟩ months |
| Limited internal IT knowledge (MDL, MDA/PDA) | A single point of failure identified |
| ContiTech tooling dependence (MES/ERP, DeepSpect, licensing) | CT decision delayed past plan |
| Cyber Security / OT exposure on machine connection | A security gap on a connected asset |
| Value not materializing from investment | Impact below target for the quarter |

## Procedure

1. Name the decision in the table, or the gate it hits.
2. Read off the owner, the mode, the threshold and the authority level.
3. If the required level is above yours, produce the recommendation and route it — do not
   narrow the action until it fits your level.
4. Record the gate as a **dependency** on the use case or saving row so it stays visible.
5. Escalate on the trigger, to the right forum, inside the round's window.
