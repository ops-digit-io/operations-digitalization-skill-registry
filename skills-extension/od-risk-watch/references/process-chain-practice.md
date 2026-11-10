---
type: Skill Reference
title: Process chain practice
description: Additional early indicators the chain produces for risk watch - operations concept, ticket age, stale lists, savings-forecast gaps, preconditions and go-live gates, the blocker brief - plus the cadence formats and what an agent may draft. Pattern only, no figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice, process-chain, draft]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Process-chain practice

Distilled from the Operations Digitalization slide decks, abstracted into process guidance. No company figures. `PROPOSAL`
marks a synthesis; `<...>` is unknown. It adds to [`risk-indicators.md`](risk-indicators.md). The register stays the authority
on the six risks, their triggers and their absence of scoring.

## 1. Method in practice

**Read the chain's by-products as indicators.** These are monitorable values the chain already produces. Each is proposed as
a *supporting reading* under an existing risk, not as a new risk (new risks go to the OD lead as proposals).

| Supporting reading | Under register risk | How to read it |
|---|---|---|
| Tool or system without a named operations owner, service level and support level | Missing operations concept | Tool-status table: scale of deployment, barrier, recommended action; "operations concept missing" was the most repeated barrier |
| Age of IT tickets, unclear counterpart, unknown security process for application approval, missing lifecycle management | Limited internal IT knowledge / Cyber Security exposure | Ticket age as a risk indicator; source system `<unknown>` |
| Machine list or tag list not updated at a plant | Cyber Security / OT exposure | Speed of response to a vulnerability notice is bounded by machine-list completeness |
| Controller patch or approval status on installed controllers | Cyber Security / OT exposure | Held up a second integration wave and the savings behind it; Cyber Security sign-off runs in parallel and blocks only go-live, so start the package early |
| Use cases implemented with no savings forecast or no registered project | Value not materialising | Count and list per plant at sprint close (`od-handover-and-adoption`) |
| Utilisation `never` on delivered use cases | Value not materialising | From the use-case list, with read date |
| Only one technical key user, or an open key-user role | Key-person / staffing gaps | Dedicated, staffed key user is a first-mover criterion (central capacity goes first to staffed first-mover plants) |
| Separation or migration plan not available where central data is needed | External tooling dependence | A precondition field on the initiative |
| Low participation in community calls | Value not materialising | Leading indicator at plant level |
| Silent threads with no reply for weeks, unowned access or artefacts | any | Signal of missing ownership, not a technical puzzle |

**Monthly metric families** worth a source each: use cases integrated, savings, systems rolled out with months of delay,
equipment-integration count, share of standard deployments over total, number of systems or processes with a major risk,
deployment schedule deviation, software footprint reduction. Planning tables use PLAN / FC (forecast) / ACT per month with an
"overshoot plan" line above target. Record the KPI basis with its date: definitions shift when the architecture changes.

**Blocker brief for a blocked programme** (when a trigger is hit and the cause is not technical): sections for technical,
commercial (supplier) and customer situation; a blockers slide per section; a timeline; what was shown to the customer; an
options slide with a decision date; the infrastructure-change deadline and the customer deadline listed **separately**; a named
list of who can support local IT. Options analysed with their consequences, including "continue as-is". `PROPOSAL` to make
"continue as-is" a mandatory baseline option in every blocker or legacy decision package.

## 2. Decision rules

- **Unreadable is a finding.** Applies equally to a supporting reading without a source.
- **Scoring conflict.** The register excludes probability x damage scoring by design. Project plans and top-risk registers in
  the decks use probability bands and an impact grid with managed / unmanaged marking. Safer reading: that is a project-level
  instrument; keep the register unscored and do not import it. `<to confirm>` with the OD lead.
- **Cost of non-decision.** A triggered risk that waits on a decision carries a "cost of non-decision" line when the
  portfolio gives one (read date stated); route to the rapid decision board where one exists (`od-decision-routing`).
- **Risk-based legacy handling** over big-bang migration: risk-based prioritisation, evergreening, redeployment through the
  standard channel.
- **Cyber Security gate:** state which work is blocked (connecting and productive rollout), not definition or prototyping.
- **Customer deadlines** outrank internal plans and appear as a separate date on any brief.
- **Two to three months unreadable** means the register row needs a source or a rewrite (`SKILL.md`).

## 3. Handoff contract

| Receives (from) | Hands on (to) |
|---|---|
| Metrics with read dates (`od-scorecard-reporting`), forecast-gap list (`od-handover-and-adoption`), barrier log (`od-equipment-integration`) | Dated risk reading with status per risk |
| Operations-concept gaps (`od-decision-routing`, `od-handover-and-adoption`) | Triggered items to the deciding role (current approval policy, look up) or COP with the register's owner role |
| Triggered two months running | Candidate for the retro's one adjustment (`od-retro`) |

## 4. Pitfalls and lessons

- Reporting deprioritised in a turbulent period, so impact could not be shown; the reading then shows "unreadable" for value
  and that must be said plainly.
- Risks named only by their top-line wording: separate technical, commercial and customer causes.
- Escalating by name or by e-mail rather than through the round and the role.

## 5. Questions to ask / definition of done

- Which source gave this reading, on which date? Which trigger text applies exactly? Who is the owning role?
- Done when: every register risk has a status with evidence, supporting readings are labelled as such, hits are routed to a
  forum, and the register's own age is stated.

## 6. AI agent operating notes

- **Can do:** read the supporting indicators on the schedule, label each with source and date, flag silent threads, unowned
  items and stale lists, assemble the blocker brief from tickets and mail, check preconditions against a checklist.
- **Required inputs:** register with its verification date, live metric reads, ticket and list extracts.
- **Human gate:** who declares a trigger "triggered" is the OD lead role; options and escalation are human decisions.
- **Evidence to cite:** source, field, filter, read date, trigger text.
- **Hands over:** the reading to the OD lead role and `od-retro`; triggered items to the forum.
