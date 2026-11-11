---
type: Skill Reference
title: Process chain practice
description: How an analytics asset is built inside the new process chain - the dashboard-without-action-owner smell, the generative-AI dashboard process (tag list, requirements, reference JSON), reconciling dashboards with paper records, sprint practice, the handoff contract, pitfalls, and AI agent operating notes. Process guidance only; no figures.
resource: ../SKILL.md
status: draft
tags: [analytics-asset, process-chain, ai-agent, dashboard]
---
# Process-chain practice

Derived from the Operations Digitalization slide decks, abstracted into process guidance. Examples are illustrative and use
`<placeholders>`. Own synthesis is marked `PROPOSAL`; unknowns are `<...>`. Build mechanics for Grafana stay in
`ops-dashboard-engine`; nothing here replaces them.

## Where it sits

Steps **23** (prototype and validate), **26** (implement and graduate), **1a2** (apply the standardized template) and **1b4**
(apply the template and go live). In Lane 1 the asset is a copy of a catalogued one; in Lane 2 it is the first real build.

## Handoff contract

| Receives | From | Must be there |
|---|---|---|
| Data verdict and missing-signal table | `mi-data-availability` | Nothing is built on a failed step |
| Signal analysis report, binding sheet | `mi-signals` | Canonical names, units, scaling |
| Requirements (atomic, testable), the named ritual and the decision | `funnel-requirements`, `funnel-use-case` | Who opens it, when, what follows |
| Validation record (if a mock-up or PoC ran) | `funnel-prototype` | Pass criterion and result |
| Reference solution | `catalog-standardization`, `catalog-usecase` | Adopt before building |

| Hands on | To | What it carries |
|---|---|---|
| Iterated tag list, documented process-domain knowledge, refined requirements, the ready dashboard, tag-to-panel table | `deploy-acceptance`, `deploy-handover` | The ritual of use, the utilization expectation, the named plant owner |
| Dashboard tier, ritual, data model | `ops-dashboard-engine` | Build mechanics start there |
| Proven blueprint | `catalog-standardization` / `catalog-standardization` | Candidate for the library |

## The smell: a dashboard without an action owner

Process-value dashboards, machine-alert dashboards, parameter monitoring (threshold against actual) and andon boards were
deployed widely without recorded savings. Visibility alone did not create savings; savings appeared where the dashboard
**drove a defined action** (an output improvement on a station, a material or shot-weight optimization, a loading-time
reduction). A large number of dashboards is the result of good integration, not proof of value.

Treat it as a build smell. Do not start (or do not call it done) when **any** of these is missing:

1. a **named action** that follows from the number (what someone does when it moves);
2. a **named action owner** (a role at the plant, not "production");
3. the **recurring moment** in which it is read (daily shop-floor meeting, shift check, escalation) and the standard method it
   feeds (SMED, waste types, value-stream mapping, switch-off campaign);
4. a **before condition** and a way to see the after (without one it cannot be counted as a saving);
5. a plant savings project registered, or the explicit statement that none is planned.

If they cannot be named, the output is not a dashboard: deliver the answer as an ad-hoc analysis, or return the case to
`funnel-use-case`. Adoption means integrated into a standard operating procedure with dashboards and escalation flows,
not "dashboard live". The pairing to aim for: standard OPEX method + digital standard use case + standard process.

## Generative-AI dashboard process

**Without AI:** a physically connected machine, a tag list, time-series, requirements from a local or central process expert and a
past dashboard of a similar process. Steps: offline signal analysis (language and domain knowledge are the typical problems),
requirements and signal iteration with the domain expert, dashboard creation with iteration, handover. Duration is days to weeks.

**With AI:** the same chain, with fixed-structure inputs and an importable output.

| Input | Form | Note |
|---|---|---|
| Tag list | labels only (id and label) | Archived points dropped |
| Requirements | text or markdown, atomic and testable | Solution bias removed; assumptions listed as open issues |
| Reference dashboard | JSON, optional | A past dashboard of a similar process |
| Equipment reference | optional | Known signal paths, scaling, thresholds; an HMI screenshot helps |
| Output | a dashboard configuration file | Import and test takes minutes; iteration at most hours |

Time-series data is **not** needed to generate the first version (it is needed to accept it). Key point: standardized inputs plus an
available creator skill-set. The process also yields a machine-specific process description and documented domain knowledge, not
only the dashboard.

Run it as follows:

1. Confirm the verdict from `mi-data-availability`; produce the **missing-signal table** (`signal id | label | why needed`)
   **before** generating, and hand it on rather than approximating.
2. Assemble the three inputs; refine the requirements first (collect once, strip solution bias, resolve plant conflicts, one
   vocabulary).
3. Generate the configuration with the build skill; import to a **test** instance.
4. Produce the **tag-to-panel table**: which tag fed which panel, which query pattern (trend, latest, event-anchored, scaled).
   Write units and scaling into each panel description.
5. The domain expert judges the result **on the running dashboard at the point of use**, not on a spreadsheet; iterate.
6. Record the iterated tag list, the process description and the refined requirements as outputs; hand on.

Tablet-friendly access for area leaders is a recurring first-delivery requirement; ask for it in the requirements.

## Reconcile dashboards with paper records

Accept a dashboard only after reconciling it with the paper process that exists today:

1. Take the production record (shift report, downtime log, cycle-time record) and the dashboard for the **same period**.
2. Run **one deep dive with production** (downtime against the paper record) and **one with engineering** (cycle-time records).
3. Explain every difference: breaks, shift changes, a tolerance not yet applied, events the PLC cannot see (hybrid capture).
4. Only then settle signal selection and categories (for example standardized pareto categories for downtime reasons).
5. Decide the switch-off: name who stops the paper process and when. Running both because nobody trusts the new one, with no one
   assigned to stop the old, is the recurring MES-rollout failure.

Also check for **organizational loss** before proposing technology: human-dependent automation (a feeder worked one by one, no
fast-forward during breaks) caps what a dashboard can show, and a top-error list often shows an organizational fix beats a
technical one. Heavy daily manual correction of a KPI is itself the first use case (automatic detection of breaks, cleaning,
shift ends; automatic MTTR and MTBF). An unclean KPI is flagged, not reported.

## Sprint practice

- A use-case sprint runs a few weeks (3 to 6 depending on the plant) with a weekly short review and technical meetings; the plant
  key user is part of the team. The sprint review compares: what was carried over from another plant, what is blocked, what is
  a rollout option.
- Standard deliverable set to plan at the start: a generic process-value dashboard for all machines, an andon board (status plus
  history), an operations dashboard (output, cycle time, alerts per shift), machine availability by mode, one process-specific
  dashboard as blueprint, an alert dashboard, SPC for inline measurement, plus transformation flows with documentation.
  Dashboard family order: overview or andon for supervisors, operations dashboard for technicians, process-value dashboard
  for deep diagnostics.
- **Agree architecture and user access before the sprint starts** (firewall separation and unclear local access cost weeks).
  Request notification channels and data historization as IT changes early. Keep flows in version control: a redeploy of the
  flow runtime has lost production configuration.
- Requirements will change: schedule an explicit iteration loop after the first delivery (dashboards are not right at first
  delivery). A requirement beyond the time frame is an additional phase. Route requests for fonts, colours and headlines by
  cost-saving impact and time-box them.
- Rollout of a dashboard to another process is gated by integration (machines, tag selection), not by the dashboard.
- Quality dashboards that do not depend on machine connectivity (laboratory tests) run on their own path, owned by the local
  quality team.
- Close the sprint with: dashboards live, flows and dashboards documented, a scalability statement, an open-topics list, the
  impact of IT issues, and a **savings-forecast completeness check**: a forecast and a registered project exist, or the
  absence is stated. A sprint that starts without a savings baseline never reports the saving.

## Decision rules

- Value and risk first: build what is high value and low risk (visual management, dashboards from existing data); for a
  high-risk idea build the cheapest test that teaches the most important thing (`funnel-prototype`).
- Rule-based per-machine solutions do not generalize; a learned approach is justified when generalization and influencers are the
  value. A prototype that works for one plant needs a containerized, more flexible algorithm to scale.
- Dashboard tool: Grafana for operations and near-real-time views, Power BI for management reporting; the choice follows the audience.

## Pitfalls and lessons

- Per-plant, unharmonized dashboards are a standardization debt.
- Delivery without explanation, no utilization measurement, no named owner: not done.
- Strategy material counts dashboard use cases as full transparency while the gap analysis shows dashboard-type use cases
  without savings. The safer reading: transparency is an enabler, savings need the action owner.
- "Just do it" use cases on integrated equipment move fastest; copy from the library rather than design anew.

## Questions to ask

- What decision follows from the number, who is the named plant owner, and in which recurring moment is it read?
- What is the condition before, and how will the after be seen?
- Which paper record does this replace, and who stops it?
- Is a proven reference available; is the machine connected and are the signals collecting?

## Definition of done

The five smell checks pass; the paper reconciliation is documented; the tag-to-panel table and the missing-signal table are
filed; the expert has validated on the running asset; the utilization expectation and owner are recorded
(`assets/asset-build-protocol.md`); the savings-forecast completeness check is answered.

## AI agent operating notes

- **Can do:** refine requirements into stories, assemble the three inputs, generate the dashboard configuration for a test
  instance, build the tag-to-panel table, draft the panel descriptions with units, draft the reconciliation worksheet (paper
  record against dashboard for the same period), run the smell checks and list what is missing.
- **Required inputs:** tag list (labels), requirements text, optional reference JSON, equipment reference, the named ritual.
- **Evidence it must cite:** which tag fed which panel and which query pattern; the verdict it relied on; the reference
  dashboard used.
- **Human gate:** the domain expert approves the requirements and judges the result at the point of use; the plant owner confirms
  the action owner and the ritual; publishing outside the department and any production import stay human-approved. An agent
  must not mark a dashboard "accepted" before the reconciliation is signed.
- **Hands over:** the outputs listed in the handoff table to `deploy-acceptance` and `deploy-handover`.
