---
type: Skill Reference
title: Business case archetypes
description: The archetypes of the strategic AI and operations business cases (foundation, enabling layer, value layer, attribution, bundle, compliance, big bet, defer), what a complete business-case record contains, how the cases depend on each other, and how that changes ranking. Pattern only, no value ranges, scores or counts.
resource: ../procedure.md
status: draft
tags: [all, practice, ai]
---
# Business case archetypes

Source: knowledge base `Graph/Business Cases` (the strategic business-case list "AI at Operations", one note per case, AI-curated from the
SharePoint list) and `Graph/Keynote Initiatives` and `Graph/Keynote Clusters` (the same cases as strategic initiatives with value
domains). The knowledge base states that this set is **different from** the plant use-case portfolio and the case groups: do not merge
them and do not rank one against the other. Value ranges, costs, scores and tiers in these notes are the authors' own inputs and
are not verified; this file carries none of them. Read them live when you need them, with the read date.

## Archetypes

| Archetype | What it is | Typical examples (kinds) | How to treat it in ranking |
|---|---|---|---|
| Foundation / platform | Infrastructure other cases need: edge model serving, a message bus namespace for derived events, a catalog made decision-grade | edge MLOps backbone, catalog maturity sprint | Rank by what it unblocks. Do not score it on its own saving |
| Enabling data layer | Produces a data product other cases consume | state labelling layer, event mining that yields a label corpus, state-machine mining for locked legacy machines | Fund early; its direct value is real but small, its enabling value is booked in the dependent cases |
| Value layer on a foundation | Predicts or optimizes using the enabling layer | predictive maintenance, predictive quality, cycle-time optimization from process mining, AI overlay on SPC, vision quality control | Rank after the enabler it needs. Check the adoption risk (false positives, labelling effort) before the value |
| Attribution / outcome | Explains or sums value; has no standalone euro | OEE and yield attribution, ramp-up acceleration | Not scored on value-to-effort; rank by whether it makes other cases measurable. An outcome is not a use case |
| Bundle | Has no standalone case without its parent | generative shopfloor design, AI factory planning (both with the digital twin) | Rank with the parent, never alone |
| Enabler without own value | A decision aid for downstream cases | sensor-upgrade decision frame | Its value is a ranked list; the case closes only if the downstream cases pay |
| Compliance-mandatory | Needed regardless of return | cybersecurity backlog closure, legacy PLC evergreening driven by regulation | Sequence by the deadline and the dependency, not by return; keep the compliance driver explicit |
| Big bet / capability build | Large value claim that needs a new capability or organisation | manufacturing app store, virtual simulation / digital twin | Split "value real" from "capability build pace"; the confidence is usually different for each. Needs a partner or a pilot before it is ranked high |
| Process enabler | Changes how work is done | agentic admin workflows, AI requirements engineering pipeline, legacy app assimilation | Adoption is the risk, not capability; plan with a lower adoption than the deck states |
| Defer / R&D bet | Prerequisite data or methods are not ready | production risk scoring (heterogeneous source documents), reverse-engineering PLC (inferred states need manual confirmation), procurement insights | Park behind a named prerequisite; do not fund as a delivery |
| Cross-functional | Needs a partner function to want it | traceability by serialization, energy optimization with facility teams, procurement insights | The partner's co-design is a prerequisite, not a risk line |

A case can wear two labels (for example a value layer that is also a quick win once its enabler exists). The enabling and dependent
roles are what matter for order.

## What a complete business-case record contains

The list's fields are a good template for a record a ranker can use:

1. **Code, label, category** (for example operate, engineer, plan, process-enabled, foundation).
2. **Portfolio tier** (quick win, bundle, enabler, platform, big bet, defer) and a **value-to-effort** reading where it applies.
3. **Description** with what is produced and for whom.
4. **Evidence** and whether it is internal, a pilot, or an external reference; say which.
5. **Value justification** as named anchors with the arithmetic shown, and a statement of what is counted here and what is booked in
   a dependent case (to avoid double counting).
6. **Key risk** written as one falsifiable assumption plus what happens if it is false.
7. **MVP scope** and a **validation plan** with a time box and a **pass criterion** stated up front (recognition by domain leads,
   a lead-time and false-positive threshold, a load-test latency target).
8. **Prerequisites** (other cases, platform, a pilot site, a partner function).
9. **Sensitivity notes**: the conservative version of the value, and the condition under which the case shrinks.
10. **Cost and resources** with what is reused.

Missing fields are findings: a case without a falsifiable key risk or a pass criterion is not ready to rank above a PoC.

## Dependencies drive the order

Cases in this set depend on each other in a chain, and the knowledge base says so repeatedly:

- Enabling layers first: state labels and mined event patterns feed the predictive and optimization cases. If the label corpus is
  not consumed by its dependents, the enabler shrinks to engineering-hour savings.
- Bundles follow the parent: planning and layout cases have no path without the simulation stack.
- Process enablers feed the store: requirements pipeline and legacy assimilation feed the app store; the cybersecurity backlog is
  the political vehicle that forces re-platforming.
- Edge model serving is a shared prerequisite for any model that must run at the machine.

Rule: **rank by dependency before return**, consistent with `process-chain-practice.md` (foundation-first). A dependent case ranked
above its enabler cannot start; its value is a promise, not a plan.

## The strategic clusters and their maturity labels

The keynote groups the initiatives in three clusters, each with a maturity label:

| Cluster | Reading | Use |
|---|---|---|
| Data-enabled foundation | The most actionable: enabling layers form the backbone, value layers sit on top; plus a flagship production feedback app | Start here; the shared data platform is the first IT dependency |
| Process-enabled engineering | Engineering tooling (generative PLC and robot work, simulation, planning) and first agentic proofs of concept; needs only calibration | Pilot-sized; adoption and certification are the risks |
| Technology-enabled engineering | Technology is market-ready, the organisation is not: app store, AI-assisted coding, requirements pipeline, cybersecurity, agentic admin | Fund the organisational change with the technology |

Each initiative also states its IT dependency (a prioritized data platform; joint concept work still open; enablement of the
agent tooling). Copy that dependency into your ranking record.

## Traps

- Ranking on the quoted value range. The ranges are authors' inputs; some cases carry none. Rank on the dependency, risk and
  validation plan first.
- Adding the cases up. Value domains overlap (first-pass yield appears in more than one case); never sum the ranges (see
  `bc-portfolio`, `references/strategic-initiatives-and-savings.md`).
- Treating an attribution or outcome case as a use case to fund or to cost.
- Using a quick-win label on a value layer whose enabler is not delivered.
- Ignoring the partner function: a case that needs facility, procurement or maintenance co-design has the partner as a gate.
- Mixing this set with plant case groups. They answer different questions.

## AI agent notes

An agent may classify a case into an archetype from the record fields, list its prerequisites and dependents as a graph, flag
missing fields (no falsifiable risk, no pass criterion, no sensitivity note) and draft the validation plan. It does not assign a
tier, does not edit value figures, and hands the ranking and the funding recommendation to the OD lead.
