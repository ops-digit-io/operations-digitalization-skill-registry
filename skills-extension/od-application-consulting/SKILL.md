---
name: od-application-consulting
description: >-
  Give a solution design recommendation for an application question inside the lean footprint - which
  existing tool or app covers the need, whether to reuse, build, buy externally or integrate a foreign
  app, how the data reaches it, which gates apply, and who runs it afterwards. Fills the gap that the
  Project Support lane's application consultancy step was never built as its own skill. Use when a plant
  or project asks "which app or tool should we use for this", asks to extend or configure a
  Manufacturing Software Suite tool, proposes a new app or a third-party application, or an existing
  plant-local application is to be replaced, integrated or kept.
license: MIT
allowed-tools: Read Grep Glob
metadata:
  id: od-application-consulting
  tier: practice
  lane: project-support-consultancy
  new_state_lane: Lane 3a (front-end and 3a.4 integrate)
  new_state_step: "Tool decision: application consulting"
  owner_role: human:jakob.gabriel
  authority_level: recommend
  status: draft
  sources_read: 2026-11-05
  requires: [od-context]
  composes: [od-system-fit-check, od-decision-routing, od-requirements-breakdown, od-project-support-consultancy, od-signal-standardization, od-cross-plant-compatibility, od-handover-and-adoption, od-node-red-flow-builder, od-analytics-asset-build, deploy-appstore, it-demand-package, od-cybersec-gate]
  derived_from:
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/OD_Skill_Map.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/02-strategy.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/00-core/14-glossary.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/project-support-consultancy/playbook.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/project-support-consultancy/skills.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/20-lanes/project-support-consultancy/tasks.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case/systems-of-record.md
    - ops-knowledge-graph/_knowledge/OperationsDigitalization-Department/10-modules/smart-factory-use-case/landscape.md
    - Skills od-system-fit-check (its tool boundaries and non-bets) and od-project-support-consultancy (composed protocols, recurring tasks), read 2026-11-05
    - New-state flow (docs/new-state-flow.md and the VSM skill map), Lane 3 shared front-end and branch 3a with options 3a.1 to 3a.4, read 2026-11-05
    - Work vault (Work-OpsDigit-Knowledge), Graph/Tools notes (rollout and use records, Concept 3 operations concept, MES 1.0), Graph/Keynote Initiatives note Manufacturing App Store (CMO) and its business case, read 2026-11-05
    - Work vault bundle file kg_nodes.csv, the Legacy Application records read as an aggregate, 2026-11-05
  okf:
    type: Agent Skill
    title: Application consulting
    tags: [project-support-consultancy, practice, new-state, draft]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Application consulting

Read `od-context` first.

**Plan row PS-04** (`OD_Skill_Map.md`): trigger "Manufacturing Software Suite / app design question";
output "solution design recommendation within lean footprint"; runs regionally; authority `recommend`;
wave 3; sources "playbook step 4; `02-strategy.md` (non-bets)". The registry's own record: the Project
Support lane lists the application consultancy session template as "⟨to confirm; PS-04 application
consulting was never built as its own skill⟩" (`od-project-support-consultancy`). This skill is that
build.

## Purpose and definition of done

Playbook step 4 of the lane: "Application consultancy (Manufacturing Software Suite, apps); control point:
solution design accepted." This skill produces the **design recommendation** that the plant and the OD
team can accept or reject. It is done when the recommendation states: the need in the requester's own
terms and in plain terms; the covering tool or app and why it fits the lean footprint (or the escalation);
the build path; the data path to the machine; the gates; the owner after go-live; and what is still
open. Acceptance of the design is a human decision; acceptance **testing** of the delivered solution is
`od-acceptance-test`.

## Where it sits

Lane 3 of the new-state flow. The shared front-end runs *requirements* (`od-requirements-breakdown`) then
the *tool-decision / IT-footprint gate* (`od-system-fit-check`, `od-decision-routing` routes 3a or 3b),
then business case. Branch **3a** introduces a system: 3a.1 reuse an available codebase or app, 3a.2 new
codebase by self development, 3a.3 new codebase by external development, 3a.4 integrate a foreign app via
IT demand and Cyber Security. This skill advises on the choice among those and on 3a.4; the doing belongs
to `deploy-appstore` and `it-demand-package` (draft skills).

## References and assets

| File | Use it for |
|---|---|
| [`references/footprint-and-data-path.md`](references/footprint-and-data-path.md) | The reference architecture and systems of record, how to read the tools' rollout and use records, how the footprint is bounded, and the discrepancies to confirm before citing a status |
| [`references/build-path-options.md`](references/build-path-options.md) | The four build paths, the question that selects each, the skill that executes it, the gates, and the support-tier split |
| [`references/legacy-application-landscape.md`](references/legacy-application-landscape.md) | How to read the recorded plant-local applications: categories, support, licences, network placement, and what that means for "replace, integrate or keep" |
| [`references/process-chain-practice.md`](references/process-chain-practice.md) | How the recommendation is produced at chain steps 32 / 3a4: rule chain from use case to make-or-buy, supplier-built app and selection round, legacy component assessment, operations-concept precondition, handoffs, agent notes |
| [`references/application-maturity-profile.md`](references/application-maturity-profile.md) | Which IT/OT focus areas describe an application and what their levels say about integrate, keep or replace, the data path and the run owner (profile from `od-maturity-assessment`) |
| [`assets/design-recommendation.md`](assets/design-recommendation.md) | The recommendation form |

The per-tool "is / is not" lines and the per-plant availability guidance are in `od-system-fit-check`; they are used
here, not copied.

## Procedure

1. **State the need, not the request.** Restate what the app must do for the process, in words that name
   no system (step 1 of `od-system-fit-check`). Get the requirement through `od-requirements-breakdown` if
   it is not yet a spec. A question about "configuring the Manufacturing Software Suite" must name the
   tool; see "Still open" for the term.
2. **Check the footprint.** Walk the need through the tool boundaries and this plant's actual tool
   availability (`od-system-fit-check`, steps 2 and 3): fits, redesign onto a lighter tool, or escalate.
   Strategy non-bets apply: no standardized MES rollout short or mid-term (check lightweight substitutes,
   for example QFPR), EMS rollout paused as written (possible discrepancy: confirm), OD builds no automation
   solutions, no broad tool proliferation.
3. **Check for an existing app.** Search the library of reference solutions (`od-use-case-standardization`)
   and the plant's legacy applications
   ([`legacy-application-landscape`](references/legacy-application-landscape.md)): a plant-local app that
   already does this is an integrate-or-keep question, not a build.
4. **Place the data path.** Name the source of each data object (one source per object; the systems-of-record
   rule) and the path: machine to IIoT Edge, MQTT and Node-RED, offload to the data platform, then apps or
   the plant's Grafana. If a signal is not yet on the path, route the gap to `od-data-availability-check`
   and the integration lane; do not design around data that is not there.
5. **Select the build path** with [`build-path-options`](references/build-path-options.md): reuse,
   self-develop, external development, or integrate a foreign app. Record the gate each path triggers
   (IT demand, Cyber Security / OT, tool rollout decision).
6. **Cross-plant check.** The signals and interfaces must stay consumable by every plant's instance of
   the capability (plan row P-08, `od-cross-plant-compatibility`; `od-signal-standardization`). An app
   that fixes a plant-specific layout into its tags fails this.
7. **Name the run owner.** Who supports the app after go-live, local or central, and who is the plant
   owner (`od-handover-and-adoption`: the three-question test). A tool with no business owner, IT
   owner, service concept and support level is not recommended for rollout: escalate it as a
   service gap (`references/process-chain-practice.md`).
8. **Write the recommendation** in the form and hand it over: the tool/system rollout row of
   `od-decision-routing` if a tool is added, the IT demand route if a platform OD does not own is touched,
   `od-benefit-calculation` for the value side, `od-investment-input` for the cost side.

## Output

[`assets/design-recommendation.md`](assets/design-recommendation.md), one per question.

## Still open

- `⟨What the "Manufacturing Software Suite" comprises⟩`. The glossary does not define it; the lane's
  skills table says "configure ⟨scope to confirm⟩"; the IIoT Edge operations concept in the work vault
  speaks of a "CT Manufacturing Suite" without listing its parts. Until the OD lead confirms, treat a
  question about the suite as a question about the named tool. Supplier: OD lead.
- `⟨Application consultancy session template⟩` and a lead time for the lane (both `⟨to confirm⟩` in the
  lane documents).
- `⟨Counterpart of the OD lead for tool and system rollout decisions⟩`.
- `⟨Where 3a.1 to 3a.4 are decided⟩` between OD, IT and the external parties: the flow names the steps and
  skills, not the deciders.
- `⟨Owner of external tooling and licensing decisions⟩` (open in the risk register and the lane wait
  states).
- `⟨Current status of EMS and MES (the tool overview and the systems-of-record note can differ)⟩`:
  see the discrepancy list in `footprint-and-data-path`.

## Do not

- Do not recommend a system outside the lean footprint as if it were available; escalate it as an
  exception (`od-system-fit-check`).
- Do not design a bespoke per-plant solution where a standard exists: "highly standardized, modular
  deployments" is a recorded trade-off of the strategy.
- Do not build, deploy to production, make licensing commitments or commit investment; the lane's "may
  not" list applies.
- Do not approve acceptance or declare the design accepted; the plant and the OD lead do.
- Do not present a cost, saving or adoption figure that has no source; mark it to-be-collected.
- Do not take a business-case proposal of the AI-at-operations list (for example the app store or the
  legacy-app assimilation case) as an approved direction; they are proposals with their own confidence
  notes.
