---
type: Skill Reference
title: Process chain practice
description: How the capital request (steps 25 and 33) is run in the AI-driven chain - management-summary shape, decisions with risk of not doing, pilot and scope-limiting patterns, mandatory sensitivity, the offer-eCR-contract consistency check, and what an agent may draft. Pattern only, no figures.
resource: ../SKILL.md
status: draft
tags: [use-case-support-service, practice, process-chain, draft]
---
# Process-chain practice

Distilled from the Operations Digitalization slide decks, abstracted into process guidance. No company figures. `PROPOSAL`
marks a synthesis; `<...>` is unknown. The eCR form itself is still not in any source (see [`SKILL.md`](../SKILL.md)); this
file covers what an approver reads and what goes wrong around it.

## 1. Method in practice

**Shape of the management summary** (seen repeatedly; keep the order, drop sections that do not apply and move them to the
back rather than deleting):

1. Executive summary: what, why, how, plus the invest summary. Write it so a reader outside the field can follow ("your
   bank manager"); pictures must explain themselves.
2. Project description: current versus future state (capacity, availability, improvement where relevant), root cause,
   what we do, three or four reasons why, and the **decisions needed**.
3. Status of foundations, and scope actually used versus deferred.
4. Use-case card: impact as a SMART estimate, maturity (proof of concept, prototype, pilot, rollout), scaling factors
   (organisational, technical, process maturity).
5. Investment details by category and spend pool (central versus local), assumptions with grounding tags, cost development
   by year, key financial figures.
6. Risks and opportunities with action, **sensitivity**, alternatives, timeline with gated milestones and an evaluation
   point, environment/safety/health statement, open items with the role that decides.

**Wave rhythm for machine-connectivity requests.** The eCR is milestone one of each integration wave. The repeatable weekly
micro-process per plant: call with the local OT expert -> prepare the request with the local expert -> upload with the local
team -> close-loop communication until approval. Status per plant by traffic light with a "call for action" cell:
uploaded / OT requirements still being identified / no approving manager. The recurring action is to push local management
approval.

**Bought applications.** The requirement specification is the contract anchor and doubles as the product backlog; the
supplier offer is the input to the purchase order. Track phases: requirement spec final, NDAs, supplier Q&A and selection,
quotation rounds, sourcing complete, build, deploy.

## 2. Decision rules

- **Write each decision as a triple:** *Decision* - *Proposal* (including limiting conditions such as a time limit or a
  reduced audit) - *Risk of not doing* (the realistic alternative, for example that the thing happens anyway through
  uncontrolled channels). A decision without a stated risk of not doing is not ready.
- **Disclose the comparison.** If no competitive comparison was run, say so, limit the commitment (time cap, restricted
  scope), plan the comparison during the work and get a quote before the cost risk is accepted.
- **Mandatory sensitivity** when both the amount threshold and the realisation-duration threshold are crossed
  (thresholds: look up in the current approval policy, `<to confirm>`). Choose swing factors that are governance decisions
  (a runtime path in or out of scope, a baseline funded or not), not only price.
- **Software-only initiatives** state it plainly: no equipment, no machine integration, no change to production processes,
  hence no physical or ESH effect.
- **Scope-limiting as a gate strategy.** A proof of concept that states "no machine connectivity, no production gateway,
  deployment unchanged" stays out of the heavier OT security path. Keep two lists side by side: *used in the PoC* and
  *deferred, needs further Cyber Security approval*.
- **Pilot framing:** time-boxed, named user group, explicit capacity, explicit evaluation date that feeds a scale/funding
  decision, small software-only budget with a buffer for lost early-offer discounts so the pilot is not re-submitted.
- **Fund an unfamiliar field in a time-boxed first step** (the governing framework only, for about a year), assess, then
  decide how to continue at minimum cost. Expect **staging by approval**: a request may be approved at a fraction, with the
  first stage cut to what is monitorable today.
- **Alternatives table** includes the selected option, the status quo, point solutions and a governance-only option.
- **Value and cost are never netted**; with no measured baseline do not print NPV or IRR, and fund the measurement layer
  first (`od-benefit-calculation`).
- **Prove foundations before the request:** cyber assessment status, data protection, AI protection (no customer data used
  for model training), single-sourcing alignment with purchasing, back-out plan owner `<content unknown>`.
- **Name both a business representative and an IT representative;** budget source (IT or business) and budget owner are
  explicit. A funding deadline (grant window) goes into the timeline as a constraint.

### Commercial-consistency check (run before the request is called ready)

| Check | Pass condition |
|---|---|
| Offer version = eCR version = contract version | One version, one date, stated in the package |
| Order of events | The offer was obtained first (a second quotation where the policy asks), then the eCR was raised; the eCR was not launched before a pending contract separation or carry-over was settled; before ordering, offer = eCR = contract (checked) |
| Frame contract | Used, or the deviation is explained |
| Purchasing | A named role drives the purchasing process |
| Cost conflicts | Per-seat versus per-site or PoC figures that differ by a large factor are flagged and reconciled before totals are printed |
| Compatibility | Existing devices were checked for signal compatibility before the hardware line was costed |
| Ownership after reorganisation | Cyber Security ownership and the central funding path are named, or listed as open items |

`PROPOSAL`: treat any "no" in this table as a blocker for "ready", not as a footnote.

Where decks disagree: two copies of an eCR summary split the pilot budget between budget classes differently. Confirm with
controlling before submission. `<to confirm>`

## 3. Handoff contract

| Receives (from) | Hands on (to) |
|---|---|
| Value rows with tier, grounding tag, basis label (`od-benefit-calculation`) | The package to the human submitter; outcome recorded in the package |
| Cost lines by category and pool, cost-calculator output (`od-investment-input`) | Dependency `ECR CREATION` -> `ECR APPROVAL` on the use case and rows (`od-decision-routing`) |
| Validation record, verdict (`od-prototype-poc`, `od-system-fit-check`) | After the decision: scope and milestones to `od-handover-and-adoption` and the build |
| Requirements and tool decision (`od-requirements-breakdown`) | Open items with a deciding role, to the steering forum |

## 4. Pitfalls and lessons

- Connectivity requests arrive incomplete, deviate from the standard rollout template or frame contract, and trigger long
  budget discussions. Cure: a cost calculator per connectivity scenario (hardware plus software) used before the project.
- An eCR launched before the contract picture was stable: offers, eCR and contract disagreed and the first order stalled.
- Work that "does not materialise" because the plants did not support the request; set-up and purchasing processes named as
  weaknesses.
- Benefit stated as a top-down envelope with no verified plant saving, presented as realised: label it potential.

## 5. Questions to ask / definition of done

- What exactly is funded, what is excluded, and what is the evaluation date? Which decision does the steering group take,
  and what happens if it does not?
- Which gates does the spend touch (Cyber Security, IT demand, data protection, works council)?
- Done when: executive summary readable alone, decisions as triples, sensitivity present or its absence justified,
  consistency table all green or listed as open items, owners named, a human holds the package. Nothing submitted by an agent.

## 6. AI agent operating notes

- **Can do:** draft the summary from the use-case card and benefit rows; run a completeness check against the field list
  above; run the consistency table (offer, eCR, contract, frame-contract id); list open items with the deciding role;
  `PROPOSAL`: a connectivity cost calculator as an asset, and a lint for "NPV printed without baseline" and "value netted
  against cost".
- **Required inputs:** benefit rows, cost lines, quote and contract references, gate status.
- **Human gate:** submission, approval, signature, any budget commitment (`od-decision-routing`).
- **Evidence to cite:** benefit row ids, quote, frame-contract id, gate status with its date.
- **Hands over:** a package with open items listed, to the human submitter; after the decision, the outcome to the
  dependency field.
