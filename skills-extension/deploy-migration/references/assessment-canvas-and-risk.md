---
type: Skill Reference
title: Assessment, canvas and risk
description: How a legacy application or platform is assessed before migration - workshop pattern, as-is/to-be canvas, component inventory, per-component risk and recovery-impact tables, OT application inventory with qualitative rubrics.
resource: ../SKILL.md
status: draft
tags: [migration, practice, template]
---
# Assessment, canvas and risk

## Workshop pattern (non-standard case)

Two-day format; a shorter one-day repeat exists.

1. Use cases of the old system (function inventory per component). The functions become the list of what must be preserved.
2. Architecture components, focus on interfaces.
3. Impact analysis per use case.
4. As-is and to-be status of cyber security, service bus, recipe management and MES.
5. Wrap-up and follow-up meeting.

One-day variant: use cases and production visit, components, impact and risk, bus status, next steps.

Audience: plant ME, process planning or production, the original software owner of the old system, central OD, the integration engineer; supplier experts external. Requirement statements are captured verbatim from the plant.

Replacement scope: "low barrier, high impact" first; aim at parallel functionality, not a one-to-one copy; start with a situational briefing; mitigate operational risk with the existing toolbox; keep a proof-of-concept scope (for example write access on one pilot machine).

## As-is / to-be canvas

Columns as-is and to-be, rows per use case. For each row: what the function does, who uses it, which machines and interfaces, what must be preserved, what changes, what is dropped. Add the status rows for security, service bus, recipe management and MES.

## Component inventory

List every component, as in this illustrative pattern: client PCs per machine type, backend kernel, ERP connector, document connector, read API, database server, reporting transformation, office client with licence manager. Per component: owner, interfaces (protocol), version, support status, licence, where it runs. Unknown fields stay `<unknown>`.

## Target component mapping

One line per as-is component: the to-be component, whether it is replaced, kept, merged or dropped, and the dependency on another component. `PROPOSAL`: mark each line "confirmed by <role>".

## Risk table (per component)

| Component | Risk (trigger) | Likelihood | Recovery-impact class | Mitigation | Owner |
|---|---|---|---|---|---|
| `<component>` | `<what could happen, what triggers it>` | low / medium / high | see below | `<action>` | `<role>` |

Recurring risk themes: client software failure, operating system updates, interface-management complexity, loss of know-how, missing documentation, limited external PLC expertise, missing security approval, licence management.

Recovery-impact classes by component: **production stop** (state the lead time to recover, `<lead time>`), **traceability loss**, **data loss with workaround**, **convenience loss**. A production-stop component with a long recovery lead time (for example a replacement machine interface) is a high-impact item and goes last, with a rehearsed back-out.

Write a one-page risk summary for each high-impact application.

## OT application inventory

Local owner fills: name, description and used functions, location, responsible, interfaces (protocol, encoding), interfaced equipment, status, software supplier and its software status (product link), version, security status, network status, production criticality, customer impact, support concept (availability, type), licence required, number of deployments.

OD fills: application category, functional mapping to a standard application, scaling potential.

Bundle migration by largest overlapping functionality. The inventory is also the entry point for Cyber Security (central visibility, risk reduction, structured collaboration): see `deploy-cybersec`.

## Rubric: production criticality (qualitative)

| Level | Meaning |
|---|---|
| Critical | Core production; failure stops production immediately; safety or legal consequence; no workaround; needed around the clock |
| Moderate | Efficiency or maintenance; a workaround exists; regular use |
| Minimal | Convenience or reporting; occasional use; easily replaced |

Guiding questions: Does it control or stop machines? Could failure cause injury, an environmental or a legal issue? Is it needed 24/7? Would failure stop production? Is it used for troubleshooting? Is it part of quality control? Does it only report?

## Rubric: customer impact (qualitative)

Questions: Does failure affect order processing, labelling or delivery? Traceability for audits or recalls? Data shared with customers or regulators? A contract effect? Rate high / medium / low with the reason in the plant's words.

## Know-how risk

Key machine programs often live with individuals, suppliers or local files. Record it as a risk row; a single version-controlled knowledge base with controlled external access is the remedy, first limited to governance, version control and code understanding. `<owner of engineering-software governance>`.

## AI notes

The agent pre-fills description, category and functional mapping from supplier pages and drafts risk rows; the local owner confirms the ratings. Ratings are a human gate. Cite the source of every pre-filled field.
