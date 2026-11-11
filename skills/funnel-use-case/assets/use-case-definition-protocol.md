---
type: Skill Asset
title: Use case definition protocol
description: The defined output of the four phases - Collect, Analyse, Assess, Control - each with its control point, so the result is a reusable record rather than prose.
resource: ../SKILL.md
status: stable
tags: [use-case-support-service, template, protocol]
---

# Use case definition — ⟨plant⟩ · ⟨use case⟩

| | |
|---|---|
| **Plant** | ⟨plant⟩ |
| **Use case** | ⟨name — one need, one plant⟩ |
| **Material family / process group** | ⟨Rubber / Plastic / Metal / Assembly⟩ · ⟨process group⟩ |
| **Capability** | ⟨capability template, or "non-standard"⟩ |
| **DBVE / date** | ⟨name⟩ · ⟨date⟩ |
| **Overall verdict** | ⟨all four control points met · in progress, at phase ⟨n⟩ · blocked⟩ |

## 1 · Collect

**Control point: demand logged against the plant roadmap.**

| | |
|---|---|
| Source | ⟨workshop · direct request⟩, ⟨date, location⟩ |
| Requested by | ⟨name, role⟩ |
| Is this one need? | ⟨yes / decomposes into: …⟩ |
| Moment in the day | ⟨Gemba walk · shift check · escalation · other⟩ |
| Logged against roadmap? | ⟨yes, ⟨where⟩ / not yet⟩ |

## 2 · Analyse

**Control point: use case scoped with a clear objective.**

| | |
|---|---|
| Stated problem | ⟨as the requester put it⟩ |
| Actual problem (diagnostics) | ⟨what process diagnostics found — may differ from stated⟩ |
| Analytical insight | ⟨what justifies the scope⟩ |
| Objective | ⟨one sentence — not a solution, not a dashboard design⟩ |
| Investment objective | ⟨why this matters beyond this one request⟩ |
| Business benefit | ⟨what measurably improves, for whom⟩ |
| Benefit classification | ⟨tangible / intangible⟩ × ⟨cashable / non-cashable⟩ — see `references/benefit-theory.md` |
| Options considered | ⟨do nothing: … / library entry: … / smaller scope: … — why each was rejected⟩ |

## 3 · Assess

**Control point: system assessment complete.**

| | |
|---|---|
| Requirement breakdown | ⟨reference to `funnel-requirements` output, or inline⟩ |
| Legacy MF IT systems touched | ⟨named⟩ |
| Already served by a system being retired? | ⟨yes → ⟨which⟩ / no⟩ |
| Data availability | ⟨verdict from `mi-data-availability`⟩ |
| Library check | ⟨proven entry found in `catalog-standardization`? which one, or none⟩ |

## 4 · Control (decide)

**Control point: business case and priority agreed with Plant ME.**

| | |
|---|---|
| Business / process change | ⟨who does something differently once this exists, and who confirms it's happening — not who receives the output⟩ |
| Output asset | ⟨Dashboard / Analytics / Report / App / Agent⟩ |
| Business process | ⟨⟩ |
| Utilization expectation | ⟨e.g. daily, at a named ritual⟩ |
| Plant owner | ⟨name⟩ |
| Dependencies | ⟨every known one, not just the blocking one⟩ |
| Business case | ⟨savings / lead-time / cost avoidance — reference `bc-build` output⟩ |
| Priority | ⟨PRIO1/2/3 — never `UNKNOWN` recorded as if it were low⟩ |
| **Decision** | ⟨proceed → `PLANNED` / hold / refused, with reason⟩ |

## Category declared

⟨standard, cross-process · standard, per-process · non-standard, unique to one plant · AI
use case⟩ — this commits the use case to `catalog-standardization` if declared standard;
the CSP gate will not agree to a declaration the record doesn't support.

## Portfolio stage reached

⟨Captured · Evaluated · Assessed · Planned/Implementation · Handed over · Effective⟩ — should
match the last control point actually met, per `00-core/12-portfolio.md`.

## Still open

- ⟨what couldn't be settled at this phase, and who can answer it⟩

## Hand-off

→ `funnel-requirements` (integration-ready spec) → Lane 3b (`mi-equipment`) or Lane 3a (`invest-screen`).
