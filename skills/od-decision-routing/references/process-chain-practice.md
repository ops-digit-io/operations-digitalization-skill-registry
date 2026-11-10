---
type: Skill Reference
title: Process chain practice
description: How decision routing (steps 1b2, 25, 32) is run in the AI-driven chain - small change versus project, what may enter routing, decisions with risk of not doing, forum and board patterns, the operations-concept gate, and what an agent may draft. Pattern only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, decision-rights, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice

Distilled from the Operations Digitalization slide decks, abstracted into process guidance. No company figures. `PROPOSAL`
marks a synthesis; `<...>` is unknown. It adds to the decision-rights table in [`SKILL.md`](../SKILL.md) and does not change it.

## 1. Method in practice

**Admission to routing.** An item enters routing only with a named owner role, a sponsor or requester, and a place where its
documents live. An initiative sheet with lead, team and sponsor all empty should not enter the step; send it back to intake.
Write unknown owners as `<...>` rather than inventing them.

**Write each decision as a triple:** *Decision* - *Proposal* (with limiting conditions such as a time limit or reduced scope)
- *Risk of not doing*. Number the decisions. State whether alternatives were compared; a missing comparison is disclosed, and
the commitment is limited instead.

**Barrier decisions.** When a barrier holds work back, show the holding-back barrier and the cost of non-decision to the
decision makers, propose a rapid decision board for holdbacks, and keep an error log reviewed regularly. `PROPOSAL`: compute the
"cost of non-decision" line from the portfolio, with its read date.

**Project order roles.** Requesting side: the steering committee with a sponsor authorises the order, nominates the project
manager, approves the plan, provides resources and is the escalation authority. Contracting side: the project team with a
project manager owns the status light and the approved budget within sign-off rules and escalates. Approval is documented
(signature, e-sign or e-mail).

**Traffic-light semantics.** Red: out of plan, result endangered, steering decision required. Yellow: minor deviation handled
by the team, corrective action in place. Green: according to the approved plan. Grey: not applicable or no data. The project
manager sets the colour within the agreed indicators; the steering committee decides on changes.

## 2. Decision rules / triage

| Situation | Route |
|---|---|
| Small change: a few days of effort at most, budget available, standard interface | Local key user raises it in the ticket tool; approved in the change process |
| Larger, needs central budget or a non-standard interface | A project: governance board with the product owner |
| Tool or system without an operations concept (owner, service concept, SLA, support level) | Not a use case and not a rollout: a **service gap**. Resolve the operations concept first, then decide the rollout |
| Plant software solution proposed locally | Approved by OD and IT together, so data, interface and knowledge domains fit |
| Plant already runs a local solution that fits the method | Input to standardisation, not a new demand |
| Cyber Security patch or approval open | Parallel track; it blocks only go-live (the live connection); start the package early; see the note below |

- **Every application or system needs, before productive use:** a business owner, an IT owner, a service concept, roles and
  responsibilities, demands and requirements, a change-management process and a built-in risk-management process.
- **First mover versus fast follower** is a capacity criterion, not an eligibility criterion. First mover: high estimated
  value, all regions, segments and technologies covered, capacity and knowledge in the plant, synergies, a dedicated and
  staffed key user. Fast follower: central support only when capacity allows, locally driven, limited funding.
- **A rollout-stop decision** for tools without an operations concept is legitimate: no rollout without an operations
  concept and a named run owner; stop until both exist.
- **Out-of-scope guard:** keep an explicit "not ours" list so triage does not drift (smart-automation measures were excluded
  from one strategy).
- **Fund an unfamiliar field in a time-boxed first step** and decide continuation at the evaluation point.
- **Corporate programme impacts** (for example a separation from a former parent's IT) are a precondition: make
  "separation or migration plan available" a field on any initiative that needs central data.

Settled rules:

- *Cyber Security as a gate.* Cyber Security sign-off always runs decoupled and in parallel with planning and build. It
  blocks only go-live (the live connection / live operation), not planning, build, use-case definition, prototyping or an
  integration wave's preparation. Start the package early; `od-cybersec-gate` stays the gate for go-live.
- *Wave allocation.* Eligibility follows request order; central capacity goes first to first-mover plants that are staffed.

## 3. Handoff contract

| Receives (from) | Hands on (to) |
|---|---|
| Decision request with owner role, amount or scope, risk of not doing (`od-capital-request`, `od-investment-input`, `od-system-fit-check`) | Decision record with row, mode, outcome, dependency set on the use case or saving row |
| Barrier record (`od-equipment-integration`) | Strategy exit -> OD lead, deciding role or forum per the current approval policy (look up); technical exit -> COP |
| Small-change request from a key user | Ticket id and change decision; larger ones as a project to the board |

Demand-management checklist (for `od-it-handover`): who can raise requests; who manages the backlog; who evaluates; who
decides yes or no; who estimates effort; who decides to start development; who develops; who does final testing; who decides
and triggers implementation; which configuration items are affected; who is responsible for implementation; and for each
step, which tool documents it. Unanswered items stay `<...>`.

## 4. Pitfalls and lessons

- Work stalls on a gate that was not named at intake, not on engineering.
- Tools rolled out without an operations concept: the most repeated barrier in tool reviews.
- Reorganisation can orphan Cyber Security ownership and the central funding path; list them as open items.
- Initiatives with empty owner fields; decisions without a risk of not doing; decisions that read "tbd" in the checklist.
- Platform criteria for AI tooling as a fit check: governed model operations with audit trails, no company data used for
  training, single-sourcing alignment, security baseline.

## 5. Questions to ask / definition of done

- Which row or gate? Which mode? What happens if nobody decides, and by when? Who is the named owner role?
- Done when: the decision is a triple, the gate is recorded as a dependency with an owner, the forum and the window are
  named, and a human holds the decision.

## 6. AI agent operating notes

- **Can do:** classify a request as small change or project; walk the demand-management checklist and mark unanswered items;
  draft the decision triple; check that owner, sponsor and document location are present; assemble scenario tables from the
  machine list.
- **Required inputs:** the request, the decision-rights table, the current approval policy (look up), gate status.
- **Human gate:** every decision in the table; the agent never commits investment, allocates resources or approves.
- **Evidence to cite:** table row, policy version and date, ticket id.
- **Hands over:** a filled decision request to the deciding role, and the dependency to the use-case record.
