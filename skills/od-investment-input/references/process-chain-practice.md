---
type: Skill Reference
title: Process chain practice
description: How the investment input (steps 1b2, 25, 33) is run in the AI-driven chain - cost build-up and allocation, cost calculator before the project, machine-integration planning workflow, staged scope, wave decision checks, and what an agent may draft. Pattern only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, practice, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice

Distilled from the Operations Digitalization slide decks, abstracted into process guidance. No company figures. `PROPOSAL`
marks a synthesis; `<...>` is unknown. This file adds practice to [`SKILL.md`](../SKILL.md) and
[`cost-lines.md`](cost-lines.md); it does not repeat them.

## 1. Method in practice

**Planning workflow per rollout plant** (the order in which cost becomes knowable): machine list (template) -> machine
"CV" per machine (PLC program, version history, vendor) -> run the machine-integration guide per core process ->
integration plan (hardware and software change per machine) -> rough time and cost planning that feeds the request ->
kick-off with the plant -> initial tag list -> hardware integration -> software integration -> flow design to the standard
model. Roles: the plant provides inputs; the machine-building tool shop is involved for own machines and supports third-party
machines; the central integration team leads flow design; who executes (plant or external) is decided in planning. First-year
work runs on fixed-price positions; a frame contract is considered only after experience with the first rollouts.

**Cost build-up for a system rollout** (categories; figures come from quotes, not from here): licence or subscription,
central one-time setup, per-site onboarding, hardware and network, key-user and data-analyst time, rollout project team,
training, contingency, yearly operation. **Allocate shared infrastructure by the share the use case actually uses**: some
lines are not relevant at all, some fully.

**Cost calculator before the project.** One calculator per machine-connectivity scenario (hardware plus software), used
before any request is written, to check preconditions and avoid incomplete requests, deviation from the standard rollout
template or frame contract, and long budget discussions. For monitoring-type systems a cost-planning guide with a "budget
building page" plus standard lists (already-connected device types that are known to work, requirements, master-data
guideline) plays the same role.

**Demand-request one-pager** (central change request): what it is, business value, who benefits (roles), one-time cost,
running cost over the planning horizon, business representative, IT representative, budget source, budget owner, timeline of
benefit realisation, footnote that figures are estimates.

**Quick-charter question set** for an intake that needs central money: business problem; existing solution to modify or
a new one; functions needed; obstacles; deadline and why; requesting organisation and proposed sponsor; risk if not solved;
benefit; how much could be invested.

## 2. Decision rules

- **Stage the scope when step one stands alone.** Price a first step without the heavy integration (for example reuse of
  existing manual order entry), then the integration as step two. Expect approval at a fraction; shape the first stage so it
  is still useful (make existing devices monitorable, no new pilot machines).
- **Check compatibility before the cost line.** Old devices with incompatible signals made the hardware cost of connecting
  existing devices easy to underestimate. Bus-based metering: compatibility with the bus, one converter per pulse output,
  unique addresses, limits per segment; wireless links between logger and plant network proved unreliable.
- **Wave decision checks** (add to the wave pack): the plant has the resources and skill to execute (a plant column
  "good / average / insufficient" was used); the layout is stable (repeatedly relocated machines delay integration); the
  controller patch and Cyber Security status is a precondition on the plan, not a later gate; at most one unknown machine
  type per new deployment, known machine types scale first; connect whole processes or areas at once and reuse existing
  infrastructure.
- **Budget class by the systems needed** (small / medium / large by whether bus, edge platform, aggregation server and
  connectivity are required). Allocation was first come first served within a quarter and class; the strategy of serving
  first-mover plants first points the other way. Which one wins: `<to confirm>` with the OD lead. Until then, record the
  rule used.
- **Low-cost connection pattern:** reuse existing devices; address translation on a switch or edge device so PLC and HMI
  programs stay unchanged; fits low data frequency. Trial one low-cost device on one machine before ordering more.
- **Never net value against cost; fund the baseline first.** If no baseline exists, the first line is the measurement layer
  and the return is deferred (`od-benefit-calculation`).
- **A pilot request** is small, time-boxed, software-only, with an explicit exclusion list and a buffer for lost early-offer
  discounts.
- **Cost figures that conflict** (per-seat versus per-site, PoC economics differing by a large factor) are flagged and
  reconciled before totals are printed.

## 3. Handoff contract

| Receives (from) | Hands on (to) |
|---|---|
| Machine list, CVs, integration plan (`od-equipment-integration`) | Cost lines with source or open marker -> `od-decision-routing` decision request (lane 1b) |
| Match record of the standard system (`catalog-systems`) | Cost lines by category and pool, benefit rows with firmness tag, alternatives table, open items with deciding role, checklist status -> `od-capital-request` |
| Fit verdict (`od-system-fit-check`) | Dependency `ECR CREATION` / `ECR APPROVAL` / `MACHINE INTEGRATION` on the rows |
| Barrier record (`od-barrier-triage`) | Gate list including Cyber Security (`od-cybersec-gate`) |

Checklist status to carry: feasibility, make or buy, cost build-up, baseline plan, IT/OT security decision, data-protection
review, benefit ownership, vendor and contract term.

## 4. Pitfalls and lessons

- Requests that arrive incomplete and then run through long rounds; use the calculator and the checklist first.
- Cost of connecting existing meters or devices underestimated; naming of measure points and master-data entry are
  laborious and need up-front thought.
- Connectivity budget approved, but the plant lacks people to execute.
- A tool that is "recommended if" without a cost class invites scope creep: record the cost class (free, per-camera
  connector, per-plant development and deployment), not a number.

## 5. Questions to ask / definition of done

- Which machines or systems does an accepted or planned use case wait for? Is the plant staffed to execute? Is the layout
  stable? Which gates does the line touch?
- Done when: each cost line has a source or an open marker with a supplier role; allocation shares are stated; staging is
  considered; the checklist is filled; open items have a deciding role.

## 6. AI agent operating notes

- **Can do:** draft the machine list and CV from PLC exports; propose the cost build-up from the cost-line template; check
  that value and cost are not netted, that each assumption carries a tag (input / assumption / unknown) and that sensitivity is
  present when thresholds are crossed; list open items; `PROPOSAL`: run the cost calculator for a scenario and compare it
  with the standard rollout template and frame contract.
- **Required inputs:** machine list, scenario, quotes with dates, gate status.
- **Human gate:** every commitment of money, ordering, allocation of resources; the pack recommends only.
- **Evidence to cite:** quote id and date, template version, machine-list read date.
- **Hands over:** the pack to `od-decision-routing`; the cost side to `od-capital-request`.
