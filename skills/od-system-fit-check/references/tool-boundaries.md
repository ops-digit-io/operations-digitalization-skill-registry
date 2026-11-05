---
type: Skill Reference
title: Tool boundaries
description: What each lightweight Smart Factory tool is and is not for, in the department's own words, with the real cost estimates and recommended-if criteria the tell is built from.
resource: ../SKILL.md
status: stable
owner: human:jakob.gabriel
tags: [practice, system-fit]
generated: { by: claude-code/1, at: 2026-10-22T00:00:00Z }
---
# Tool boundaries

Each tool below carries its own **is / is not** line in the department's own tool catalogue
— stated once per tool, not per plant, so this is the stable part. Plant-by-plant
availability (what is actually deployed where) changes constantly; check
`references/deployment-reality.md` and the live Smart Factory Tool Overview before quoting a
status.

## Quality Feedback App (QFPR) — lightweight MES, quality side

**Is:** collects quality feedback at the shopfloor — failure labels, measurements, checks —
on part, box and batch level, via standardized communication streams.

**Is not:** a tool to calculate quality or production KPIs, or to standardize quality data
input. Not a master-data tool beyond the quality specifications the shopfloor checks need.

**Integration recommended if:** the plant is starting its digitalization journey, some
machines are already connected, and parts carry a serial code read automatically.

**Cost reference:** per the current tool one-pager (look up: tool owner / System Overview one-pager); do not quote a remembered amount.

**The tell this resolves:** a request that wants QFPR itself to compute OEE/quality KPIs,
or to become the master-data system for specs beyond the checklist, has outgrown QFPR —
that is a sign pointing toward MES, not a QFPR configuration question.

## MDA/PDA (Iconics Genesis64) — lightweight MES, automation/asset-data side

**Is:** machine- and asset-data acquisition and visualization, recorded in the tool catalogue
itself as *"(Lightweight MES) — Focus: Automation Asset Data."*

**The tell this resolves:** a request for automation/asset-level data history, states or
events that QFPR does not cover (QFPR is quality-record-shaped, MDA/PDA is machine-state-
and asset-data-shaped) is still inside the lean footprint if MDA/PDA is deployed at that
plant — it does not by itself imply MES.

## Manufacturing Image Library (MIL)

**Is:** connects shopfloor camera systems to standardized image storage, enables Deep-
Learning-based inspection rules, records all inspection results across the inspection
systems.

**Is not:** a tool to store process parameters or other two-dimensional product measurement
values. Not a tool to directly execute Deep Learning training itself.

**Integration recommended if:** a customer request to store pictures exists, or a new
process is being built that includes vision systems; it fits any industrial camera system.
Integration effort is rated low once edge integration already exists.

**Cost reference:** one-time connector cost per camera system, per the current tool one-pager (look up: tool owner).

**The tell this resolves:** a vision/inspection request that wants to store process values
alongside images, or wants the model trained inside the app itself, has outgrown MIL's own
stated boundary.

## Recipe Management (Camline)

**Is:** manages and versions machine/equipment recipe master data, sends it to equipment via
standard interfaces (OPC-UA).

**Is not:** a tool to store actual values from the machine, or to alert on machine-parameter
deviations.

**Integration recommended if:** multiple or few complex standardized machines exist that can
retrieve recipe information via OPC-UA — ideally with MDA/PDA already in place.

**The tell this resolves:** a "recipe" request that is really asking for live deviation
alerting or historical value storage is a QFPR/MDA-PDA request wearing Camline's name, not
a Camline request.

## Manufacturing Execution System (MES) — the department's clearest non-bet

**Is not pursued as a standardized rollout, short/mid-term.** Typically recorded in a plant's own Smart Factory Tool Overview as `NOT AVAILABLE` with the
reason `NOT NECESSARY` or `NOT RECOMMENDED AS OF NOW`. The strategy
record states why: ERP/S4HANA-dependent, and the kill criterion for the pilot bet (the existing MES plants) is "MES value-add not demonstrated" — see `references/non-bets.md`.

**The tell:** if neither QFPR nor MDA/PDA — alone or together — cover what the request
actually needs (cross-process scheduling, work-order management, genealogy across the
whole order lifecycle rather than a single quality or asset-data slice), the request is
MES-shaped. That is the moment to redesign scope or escalate, not the moment to improvise
a bespoke equivalent.

## Energy Management System (WiriTec)

**Is:** measurement devices collecting energy-consumption data for energy optimization; can
pass data to analytics (e.g. the Data Science Factory).

**Is not:** a system to collect any data other than energy data from the processes.

**Status — a possible discrepancy, not a resolved fact:** the department's own non-bets record
(`references/non-bets.md`) can say EMS rollout is *stopped until operational criteria are
resolved*, while the tool catalogue describes WiriTec as rolled out and used for energy use
cases, with its own cost example. **Confirm which is current (look up: OD lead; the live Tool Overview) before treating either as settled** — this is
exactly the kind of drift this skill exists to catch, including in its own source material.

## Data Science Factory (DSF)

**Status:** a central capability whose status differs by plant and by the date of the source (planned, ongoing, stopped), not yet a thing a single use case can assume
exists at an arbitrary plant. Treat a request that assumes central DSF access the same way
as a request that assumes MES: check the specific plant's current status before promising
it, and if it is not yet there, that is a platform-readiness escalation, not a use case.
