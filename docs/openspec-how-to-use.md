---
type: Design Record
title: OpenSpec how to use
description: "Short usage info for step 3a4 of the process map: the IT demand follows OpenSpec, which is external. The registry holds no copy of OpenSpec or its skills; this page only says how to use them."
status: draft
owner: human:jakob.gabriel
tags: [openspec, lane-3, process-map, external]
generated: { by: claude-code/1, at: 2026-11-16T00:00:00Z }
---
# How to use OpenSpec for the IT demand

Step 3a4 *Package / build* of the process map (routes 3a.3 external build and 3a.4 integrate a foreign app) runs the IT
demand through **OpenSpec**, an open-source, spec-driven workflow: one change folder per demand with a proposal, delta
specs, a design and a task list, kept in Git. OpenSpec is **external**: this registry holds no copy of OpenSpec and no
skill for it. The process map links straight to OpenSpec's own skills and documentation (upstream, tag `v1.17.0`).

## Where to find it

| What | Link |
|---|---|
| OpenSpec project | <https://github.com/Fission-AI/OpenSpec> |
| Its agent skills (`openspec-*`) | <https://github.com/Fission-AI/OpenSpec/tree/v1.17.0/skills> and how to install them: [`skills/README.md`](https://github.com/Fission-AI/OpenSpec/blob/v1.17.0/skills/README.md) |
| Getting started | <https://github.com/Fission-AI/OpenSpec/blob/v1.17.0/docs/getting-started.md> |
| Concepts (changes, specs, artifacts) | <https://github.com/Fission-AI/OpenSpec/blob/v1.17.0/docs/concepts.md> |
| Command line | <https://github.com/Fission-AI/OpenSpec/blob/v1.17.0/docs/cli.md> |

## The six sub-steps and the OpenSpec skill for each

| Sub-step | Who | OpenSpec skill (external link on the map) |
|---|---|---|
| 3a4.1 Explore + collect inputs | OD | `openspec-explore` |
| 3a4.2 Propose the change | OD | `openspec-propose`, or `openspec-new-change` with `openspec-continue-change` and `openspec-ff-change` |
| 3a4.3 Validate + hand over | OD | `openspec-update-change` |
| 3a4.4 Apply | IT / external developer | `openspec-apply-change` |
| 3a4.5 Verify | IT / external developer | `openspec-verify-change` |
| 3a4.6 Archive + sync specs | IT | `openspec-archive-change`, `openspec-bulk-archive-change`, `openspec-sync-specs` |

## How to use it

1. **Set up once.** Install OpenSpec's skills into your agent and initialise a store (a Git folder with an `openspec/`
   directory) as described in OpenSpec's getting-started page and skills README linked above. The skills drive the
   `openspec` command line, so install that too.
2. **Bring the front-end results as the input.** The demand is clear only when the requirement (`funnel-requirements`),
   the gate verdict and route (`invest-screen`), the business case (`bc-build`) and the approval route
   (`bc-capital-request`, `dept-decision-rights`) exist. Give them to `openspec-explore` and `openspec-propose` as context.
   An under-specified demand stays in the front-end; it is not handed to IT or an external developer.
3. **Run the sub-steps in order** with the skill named for each. OD acts on 3a4.1 to 3a4.3; IT or the external developer on
   3a4.4 to 3a4.6.
4. **A human hands over and accepts.** A person commits the change in the store and sends it; ownership moves to IT only on
   formal acceptance (`deploy-handover`). Until then OD owns the demand. Do not pass a delivery date to the plant before a
   team has committed the work.

Anything about OpenSpec itself (commands, file formats, validation rules) is defined by OpenSpec's documentation, not here.
