---
type: Skill Reference
title: Microservice app pattern
description: The service-per-capability pattern from the knowledge base's work-in-progress microservice design - what each capability service does, its event contract, what a plant configures, how it degrades, which have a write path, and the shared kernel and composition services around them. A design proposal, not a running landscape. Open it when you package an app that implements a standard capability or decide whether a request is a new service.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Microservice app pattern

**Status of the source.** Everything here comes from the AI-drafted work-in-progress folder `Microservice Apps (WIP)` in the knowledge base
("draft", "not reviewed by a human"): the landscape overview, one note per capability service, *Platform Services (Shared Kernel)*,
*Cross-Service Composition Services*, *Extension Services*, *User Interfaces and Interaction Layer*, *Cross-Cutting Platform
Concerns*, *Platform Extensibility and Onboarding*. It is a **design proposal**. It says which services would exist, not which
run. Check `references/platform-and-pilot-status.md` before you name a target, and say "proposal" in the package. Counts of use
cases per service in the notes are not repeated here.

## The pattern in one paragraph

One bounded context per standardized capability template. The "belongs / does not belong" text of the placement rules (R1 to R13)
**is** the non-overlap contract between services. Services talk through one event bus with one envelope; no service reads another's
database; no service calls another's write API to do its own job. Plant-local by default; only analytics is cross-plant. A use
case that needs several capabilities is a screen or report **composing** published events, not a merged service. A plant's
difference from another is **configuration**, never a code fork.

## The event envelope (proposed)

Every topic payload travels in one envelope: an event id, an occurred-at timestamp (UTC), plant id, machine id (or none), an
optional line id, a source (connector, rule engine, manual entry or service name), a schema name with a version (`<topic>.v1`) and
the payload. Topics are named `<domain>.<event>`: `signal.*` raw values, `condition.*` evaluated rules, then one family per
capability (`andon`, `oee`, `cycletime`, `downtime`, `alert`, `quality`, `recipe`, `analytics`). Automated and manual quality share
the `quality.*` family so consumers need not know which produced a result. Changes are additive inside a version; an incompatible
change ships as the next version beside the old one (see `references/app-manifest-and-release-gate.md`).

## What each capability service does

Illustrative contract in words; the notes give payload shapes. "Config" is what a plant sets without touching code.

| Service (capability) | Job | Consumes | Publishes | Owns | Config per plant | If an upstream is down |
|---|---|---|---|---|---|---|
| Process Values | store and serve live parameters; the primary consumer of raw signals | `signal.process_value` | nothing derived | plant-local time series | which signals per machine; retention | shows nothing new; others unaffected |
| Andon Board | compose current status of line, cell, area, plant and detect when a human should look; it composes, it does not measure | output counters, `condition.stop_detected`; optional OEE and downtime for tiles | `andon.status_changed`, `andon.escalation_raised` | latest status plus a short shift history | which lines and cells feed a board; staleness window | board keeps showing status with a stale flag; tile or reason drops out |
| OEE Calculation | availability, performance, quality and OEE as a composition of other services' figures | run state and counters, `downtime.event`, `quality.*` | `oee.snapshot` | OEE time series by shift, day, week | window sizes; definition per ISO 22400-2 | keeps last known component, marked stale |
| Cycle Time | cycle against a standard per machine and part | start/end signals or counters | `cycletime.snapshot`, `cycletime.deviation` | cycle series plus the standard time | the standard times | OEE performance falls back to stale |
| Downtime Reporting | stop events with duration and reason | `condition.stop_detected` | `downtime.event` | append-only event log and the reason-code taxonomy | the plant's reason codes | operator can still log a stop by hand into the same log |
| Machine Alerts | alarms and tolerance alerts as a journal with acknowledge | `condition.*`, compliance deviations | `alert.raised`, `alert.acknowledged` | append-only alert journal | which conditions, severity, who is notified | journal intact; delivery waits and nothing is lost |
| Process Quality Data | automated in-process quality: SPC, vision, leak test, per-part record | measurement channels, stop conditions | `quality.result` | per-part quality record with genealogy keys, SPC history | characteristics and limits | independent of Manual Quality Data |
| Manual Quality Data | paper-to-digital forms and checklists | none from the machine bus | `quality.manual_result` | form schemas and records | the form fields per plant and line | works without any machine data |
| Recipe Values | recipes, parameter sets, change history, set-value transfer | optional read-only context | `recipe.changed`, write requested, write confirmed | recipe store and append-only change log | approval roles | machine keeps its last recipe |
| Analytics | cross-machine and cross-plant reports, forecasts, models | the published events of all others and the existing data lake | `analytics.report_published`, `analytics.model_scored` | a report and model registry, no new production store | scope of a report | none of the others depend on it |

Rules that hold across the table:

- **Reads versus writes.** Only a few write paths exist, each deliberate: an escalation, an alert acknowledgement, a downtime
  reason, a form submission, and one machine write (recipe set-point). Everything else only reads.
- **The machine write is guarded.** The recipe deploy needs an explicit approval step and goes out only through the gateway's
  write-capable connector, never directly to a controller. Any app that writes to a machine is routed through the segmentation
  review (ISA/IEC 62443, NIST SP 800-82) and Cyber Security sign-off, however small.
- **Append-only logs** (downtime, alerts, recipe changes) are the audit shape: never rewrite, add a classification or state.
- **The distinction between services is the source or the question, not the content**: automated versus typed quality, actual
  versus intended value, stop event versus availability figure.

## The shared kernel (four small capabilities)

Used by several services, described once so no service re-implements them: an **ingestion gateway** (protocol adapters publishing
`signal.process_value`; no business logic), an **asset and integration registry** (read-mostly API over the machine, connector,
tool and legacy-application lists; owns no data), a **rule and threshold engine** (the one place bands, thresholds,
maintenance-due and stop detection are evaluated; a new condition is configuration, not a redeploy) and **notification and
delivery** (fan-out from an alert to the channel a person sees). These formalize existing tools; the draft says nothing new is
required beyond a small shared gateway for language-model helpers. A service's coverage is bounded by which machines are
integrated: that is the most frequent top blocker, so sequence the kernel before the services that depend on it.

## Composition and the two gap services

Default answer to "this use case needs several capabilities": a dashboard folder or an optional backend-for-frontend that pulls
from each service's read API. Only when the **function itself** falls between two services' "does not belong" lines does a small
closed service earn its place. The draft names two: **parameter compliance** (actual value against its active set-point within a
tolerance band, reading process values and recipe changes) and **traceability and genealogy** (a part's full history indexed by
part, serial, batch or lot, reading the other services' records without producing any). Neither adds to the use-case count; each
realizes cases already counted elsewhere.

## User interface rule

Effort follows write need: a read-only capability is a panel on the plant dashboard tool already in use; a capability that takes a
write needs a small app (a reason picker, a digital checklist, a recipe console), and one status board needs a small shared
escalation widget. Do not build an app where a panel will do.

## Deciding where a request belongs

1. Apply R1 to R13. If it names a core capability, it is a **new plant instance** of an existing service: a deployment plus a row in
   the registry, no new service.
2. If it fits an extension domain (AI knowledge assistant, workplace administration, production-to-ERP integration, tool
   lifecycle, device status), treat it as that domain's instance.
3. If it fits nothing, it is a candidate for a new service **only when a second, unrelated use case needs the same function**. A
   single one-off goes to the store as an individually catalogued container.
4. Onboard through one of the three scenarios in `references/platform-and-pilot-status.md`; the draft holds that a fourth path
   defeats the catalog.

## Pitfalls

- Treating the draft as the pilot's procedure. It is not; no image, registry, resource or deploy-rights rule is in it.
- Letting an app read another app's database "just this once": the contract is the event and the read API.
- Forking an app per plant for a field or a tile: that is a configuration or a registry entry.
- Merging two capabilities into one app because a plant asked for one screen.
- Building a machine-write path without the approval step and the security review.
- Counting a use case twice: a composed service realizes cases already counted under its inputs.

## AI agent notes

An agent can draft the manifest, the consumed and published topic list from the table, the config sheet for the plant, and a
placement of the request on a capability with rule ids. It must mark the landscape as proposal, never set the Cyber Security
review to passed, and never state that a service runs. The human gate stays at the release gate (R7, R8 in the checklist).
