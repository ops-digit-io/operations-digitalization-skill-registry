---
type: Skill Reference
title: Vocabulary
description: The controlled vocabulary in use for business process, output asset, and legacy/target systems - for Phases 1, 3 and 4.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [use-case-support-service, vocabulary]
derived_from:
  - personal vault, Graph/Use Cases/*.md, read 2026-09-17
generated: { by: claude-code/1, at: 2026-09-17T00:00:00Z }
---

# Vocabulary

## Business process (Collect)

The moment in the day a use case belongs to. A use case can carry more than one.

- Daily Gemba
- Troubleshooting
- Activity Tracking
- Utilization Improvement
- Process Improvement
- Quality Improvement
- Traceability
- Energy Reporting

## Output asset (Control)

What gets built. Dashboard is the default; naming anything else is worth a second look at
whether a Dashboard would serve the same need cheaper.

- Dashboard
- Report
- App
- Analytics Workflow
- Agent

## Legacy / target systems (Assess)

Named systems and tools a use case's data actually passes through or lands on:

- RuleEngine 2.0
- Concept 1 — Central OPC-UA Server
- Concept 2 — container-based Machine Integration
- Concept 3 — IIoT Edge Computing Platform

  (the three integration concepts — see `mi-connector`)
- MSB (versioned family)
- MDA-PDA (versioned family)
- QFPR
- MIL
- Data Science Factory
- Energy Management (versioned family)

The Legacy Application List separately tracks applications being replaced or retired — check
whether the need is already served by one on that list before specifying a new one.
