---
type: Skill Asset
title: Standardization review
description: The defined output of the procedure - template placement, library check, cluster baseline and delta, and the CSP-readiness verdict od-decision-routing's rollout gate consumes directly.
resource: ../SKILL.md
status: stable
tags: [use-case-support-service, template, protocol]
---

# Standardization review — ⟨use case name⟩

Copy once per use case. Fill as the work happens, in order — each section is one step of
the procedure, so a plant engineer who was not in the room can see what was checked, what
was taken from elsewhere, and what is genuinely new.

| | |
|---|---|
| **Use case** | ⟨name, plant⟩ |
| **From definition / solution evaluation** | ⟨`od-use-case-definition` / `od-use-case-solution-evaluation` protocol reference⟩ |
| **Reviewer / date** | ⟨name⟩ · ⟨date⟩ |

## 1 · Template placement

| | |
|---|---|
| **Capability** | ⟨one of the cross-plant capability templates⟩ |
| **Process group** | ⟨one of the process groups, inside Rubber/Plastic/Metal/Assembly⟩ |

Never create a new capability or process group to accommodate one plant — if neither fits,
that is a finding to raise, not a reason to invent a new template.

## 2 · Library check

| | |
|---|---|
| **Proven entry found for this capability?** | ⟨yes — cite it · no⟩ |
| **If yes, taken as-is or adapted?** | ⟨as-is · adapted, name the delta · rejected, name why⟩ |
| **If no**, this use case is itself a library candidate once delivered — note it for `od-use-case-standardization`'s own catalogue. | |

## 3 · Cluster tag and baseline

| | |
|---|---|
| **Cluster (from the classifier, never hand-assigned)** | ⟨C01-C12⟩ |
| **Baseline checklist applied** | ⟨`references/clusters.md` §Cn⟩ |
| **Plant-specific deltas** (machines, line, local constraint — only what differs from the baseline) | ⟨list⟩ |

A `C12` placement is itself a finding: re-check the process-group link and the sibling-
plant search in `references/clusters.md` §C12 before accepting it as genuinely unique.

## 4 · CSP readiness (only if this use case is a rollout candidate)

| | |
|---|---|
| **Methods and actions written down?** | ⟨yes/no⟩ |
| **Evidence it works at its first plant?** | ⟨cite it⟩ |
| **CSP decision** | ⟨Yes · No, not yet — name what is missing · not submitted⟩ |

A `No` is information about rollout readiness, not a rejection of the use case — do not
record it as a failure.

## 5 · Handoff

| | |
|---|---|
| **Standardization verdict** | ⟨take the library entry as-is · adapted with named deltas · genuinely new, candidate for the library once delivered⟩ |
| **CSP gate recorded as a dependency** | ⟨on the use case / the saving row — per `od-decision-routing`'s "standard enough to roll out" gate⟩ |
| **Next skill** | `od-benefit-calculation` (value), `od-portfolio-and-savings-analysis` (adoption tracking), or `od-decision-routing` if the CSP outcome needs escalation |
