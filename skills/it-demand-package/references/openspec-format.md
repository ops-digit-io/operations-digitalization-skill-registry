---
type: Skill Reference
title: Openspec format
description: "The OpenSpec rules an OD handover package must meet (structure, proposal sections, delta spec format, validation thresholds) and which OD skill fills which artefact."
resource: ../SKILL.md
status: draft
tags: [openspec, handover, format]
---
# OpenSpec format

OpenSpec is a public, plain-markdown way to plan a change before code: a change folder holds *why*
(proposal), *what* (delta specs), *how* (design) and the *work* (tasks). It never touches Git; the folder is
committed and reviewed like code, and archived into the main specs once shipped.

## Structure

```
openspec/
├── config.yaml                 project context and rules (schema: spec-driven)
├── specs/                      the main specs, built up by archiving changes
└── changes/<change-id>/
    ├── .openspec.yaml          schema: spec-driven · created: <date>
    ├── proposal.md             Why · What Changes · Capabilities · Impact
    ├── specs/<capability>/spec.md   delta spec per capability
    ├── design.md               Context · Goals / Non-Goals · Decisions · Risks / Trade-offs
    ├── tasks.md                numbered checkbox groups
    └── handover.md             OD annex (not an OpenSpec artefact; travels with the change)
```

## Authority: OpenSpec itself

This skill follows OpenSpec release **1.17.0** (github.com/Fission-AI/OpenSpec, npm `@fission-ai/openspec`). The
OpenSpec CLI decides: `check_handover.py` runs `openspec validate <change-id> --strict` and fails if the CLI is
missing, rejects the package, or is another release (re-check the package against the new release). The templates
under `assets/openspec/` keep OpenSpec's own headings (`# Proposal`, `# Spec Delta`, `# Design`, `# Tasks`;
`**Goals:**` and `**Non-Goals:**`). The table below is a summary, not the full rule set: OpenSpec also rejects, for
example, a task numbered into the wrong group and a duplicated task id. To move to a newer OpenSpec release, change
`OPENSPEC_PINNED` in `scripts/check_handover.py` and run `python3 scripts/check_openspec_conformance.py --require`.

## Rules the check enforces (from OpenSpec's validator)

| Rule | Level |
|---|---|
| `proposal.md` has `## Why` of 50 to 1000 characters and a non-empty `## What Changes` | error |
| At least one delta spec (or `skip_specs: true` in `.openspec.yaml`, never for an OD handover) | error |
| More than ten deltas → split the change | warning |
| A delta spec uses `## ADDED / MODIFIED / REMOVED / RENAMED Requirements` | error |
| Every `### Requirement:` body contains SHALL or MUST | error |
| Every requirement has at least one `#### Scenario:` (exactly four hashes) | error |
| Every scenario has a WHEN (or GIVEN) and a THEN step | warning (strict: error) |
| Requirement description at most 500 characters | warning (strict: error) |
| New capability: `## Purpose` of 50+ characters | warning (strict: error) |
| Capability path segments kebab-case | error |
| Tasks are `- [ ] n.m description` under `## n. Group` | error |

The OD check runs these in strict mode: a handover package passes only with no warnings left.

## Which OD skill fills which artefact

| Artefact | Section | Filled from |
|---|---|---|
| proposal.md | Why | Problem and bankable value: `od-benefit-calculation`; objective: `od-requirements-breakdown` |
| | What Changes | Requirement scope and growth boundaries: `od-requirements-breakdown` |
| | Capabilities | The epic's durable behaviours: `od-requirements-breakdown` |
| | Impact | Plants, systems, interfaces, data: `od-data-availability-check`, `od-system-fit-check` |
| specs/ | Requirements and scenarios | User stories and acceptance criteria: `od-requirements-breakdown`, `od-acceptance-test`; data contract: `od-signal-standardization` |
| design.md | Decisions | Route and sourcing: `od-system-fit-check` (tool-decision gate); platform and manifests: `deploy-appstore`; Cyber Security: `od-cybersec-gate`; legacy: `od-requirements-breakdown` (legacy assessment) |
| | Non-Goals | Growth boundaries |
| tasks.md | — | Build tasks, plus logging, observability, manifests, acceptance test, Cyber Security sign-off, handover checklist |
| handover.md | all | `references/it-expected-inputs.md` |

## Writing style IT will expect

- Specs describe observable behaviour; "The system SHALL …". Framework, library and class names go in
  `design.md`.
- One behaviour per requirement; examples and edge cases become scenarios.
- English only in every file (department rule for deliverables).
