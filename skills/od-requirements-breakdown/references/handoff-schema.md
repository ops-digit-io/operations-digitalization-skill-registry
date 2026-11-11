---
type: Skill Reference
title: Handoff schema
description: "The handoff file the requirements stage writes and the feature stage reads: frame, riskiest assumption, problems, candidates, with the rules the consumer relies on and a minimal valid example."
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [requirements, handoff, department-package]
derived_from:
  - "Department knowledge base, read 2026-11-10"
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
> Transcribed from the department package `product-funnel-skills.zip/skills/requirements-funnel/references/handoff-schema.md` (the master).

# Handoff Schema

The contract between `requirements-funnel` (producer) and `feature-funnel`
(consumer). Both skills must agree on this. If you change a field, change it in
both places.

Written as a YAML block inside `requirements-funnel-output.md`.

## Fields

### `frame` (required)

| Field | Type | Notes |
|-------|------|-------|
| `actor` | string | The primary actor. One only. If the funnel produced several, the first is primary and the rest go in `secondary_actors`. |
| `secondary_actors` | string[] | Optional. Present here means "not optimised for in the MVP". |
| `outcome` | string | Before/after sentence from Stage 1. |
| `trigger` | string | Optional. What happens immediately before use. |
| `out_of_scope` | string[] | Minimum two entries. Used downstream to reject candidates that drift back in. |
| `constraints` | string[] | Hard limits. A candidate violating one is disqualified, not down-scored. |

### `riskiest_assumption` (required)

Single string. The one belief that, if wrong, makes the whole product
pointless. `feature-funnel` uses this to select MVP content: the MVP should
test this assumption as cheaply as possible.

### `problems` (required)

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | `P1`, `P2`… Stable; referenced by candidates. |
| `statement` | string | Full `As … when … I need … so that …` form. |
| `evidence` | enum | `observed` (user has seen it happen), `stated` (user asserts it), `assumed` (neither). Feeds the confidence factor downstream. |
| `frequency` | string | Optional. How often the problem occurs — daily, per changeover, once per project. Strongly affects Reach. |

### `candidates` (required)

| Field | Type | Notes |
|-------|------|-------|
| `id` | string | `F1`, `F2`… |
| `problem` | string | The `P*` id it addresses. Exactly one. A candidate solving two problems was not decomposed properly. |
| `name` | string | Short imperative name. |
| `description` | string | Optional. One or two lines. |
| `variant` | enum | `cheap`, `obvious`, `strong`. Preserves the Stage 3 fan-out so the next skill can see the cheap alternative it is trading against. |
| `depends_on` | string[] | Other `F*` ids that must ship first. Hard constraint on tiering. |
| `assumptions` | object[] | Each `{ text, status }` where status is `validated` or `unvalidated`. |

## Rules the consumer relies on

1. Every `candidate.problem` resolves to an existing problem id.
2. Every problem has at least one candidate.
3. `depends_on` is acyclic. A cycle means the candidates are one feature.
4. No candidate violates a `frame.constraints` entry — those are removed during
   Stage 4, not passed through with a low score.

## Minimal valid example

```yaml
frame:
  actor: "Small-batch production planner"
  outcome: "get a feasible cell layout in an afternoon instead of two weeks"
  out_of_scope: ["ERP integration"]
  constraints: ["offline, single user"]
riskiest_assumption: "planners will trust a generated layout"
problems:
  - id: P1
    statement: "As a planner, when comparing layouts, I need travel distance per option, so that I can defend the choice"
    evidence: observed
    frequency: "per new cell, ~6/year"
candidates:
  - id: F1
    problem: P1
    name: "Travel-distance readout on a manual canvas"
    variant: cheap
    depends_on: []
    assumptions:
      - text: "travel distance is the metric planners optimise"
        status: unvalidated
```
