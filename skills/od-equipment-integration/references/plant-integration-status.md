---
type: Skill Reference
title: Plant integration status
description: Guidance for building a plant-by-plant integration status view from the Machine List, the Tool Overview and the Legacy Application List - which fields to read, how to count live, which flags to compute, which record mismatches to expect. Guidance only, no company figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [information-integration-service, technical]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Plant integration status

**This file holds no counts.** The plant-by-plant numbers that used to sit here were a snapshot
of one export and went stale. What stays is how to build the view on the live lists, what each
column means, and which patterns and record mismatches to expect. Re-count on the live lists
before quoting any figure in a decision, and give the export date next to it.

## Where the data lives

| Source | What it gives per plant |
|---|---|
| Machine List (SharePoint list; vault notes in `Graph/Machines`) | One row per machine or PLC: plant, vendor, PLC model, network protocol, `integration_status`, `integration_method`, `integration_approach`, `integration_blockers`, project reference, planned integration date |
| Tool Overview (`ToolOverview-List`; vault notes in `Graph/Tools`) | Which integration concepts are rolled out at the plant, with status and comment |
| Legacy Application List | Which legacy applications are located at the plant |
| Plant notes (`Graph/Plants`) | The plant profile; a plant note can exist with no machine row |

## How to count live

1. Export the Machine List and group by plant.
2. Per plant count rows by `integration_status`: `INTEGRATED`, `NOT INTEGRATED`,
   `INTEGRATION ONGOING`, blank.
3. Per plant count rows by `integration_method`: `Edge` = IIoT Edge Computing Platform,
   `Aggr.` = Central OPCUA Aggregation Server, `Eval.` = `EVALUATION ONGOING` (route still
   undecided for that machine), none = field blank.
4. Per plant take the controller vendors by row count.
5. Per plant read the concept rows in the Tool Overview: C1 = Concept 1 central OPC-UA server,
   C2 = Concept 2 container-based machine integration, C3 = Concept 3 IIoT edge computing
   platform, each with its rollout status (`AVAILABLE` or other).
6. Per plant count rows with free text in `integration_blockers` and classify the text with
   `blockers-and-waves.md`.
7. Per plant count Legacy Application List entries located there
   (`od-system-fit-check` (`../../od-system-fit-check/references/legacy-applications-landscape.md`)).
   An application can be located at several plants, so the plant column does not add up to the
   application count.

## How to read a column

- **Status columns.** Blank is not "not integrated" (see
  `od-data-availability-check` (`../../../skills/od-data-availability-check/SKILL.md`)). A plant with a
  blank status on most rows is a plant where the record has not been kept, not a plant with a
  zero result.
- **Route recorded.** Blank means the field was not filled, not that there is no route. A plant
  with a SCADA that gathers the data itself may legitimately carry no method; read the Tool
  Overview comment.
- **Concepts in Tool Overview.** A plant can show machines routed to a concept that the Tool
  Overview does not list for it, and the reverse. That is a record mismatch to clear with the
  IIAE, not proof either way.
- **Blocker rows.** Rows with free text; the text is a kind, not a count. Blockers often sit on
  machines already `INTEGRATED`, which means the blocker text is stale or describes follow-up
  work.

## Flags to compute (each is a question for the Plant ME / Plant IT, not a finding)

| Flag | Condition | Typical reading |
|---|---|---|
| Method blank | Most rows of the plant have no `integration_method` | Documentation gap, or a SCADA-based plant |
| Status blank | Most rows have no `integration_status` | Plant at the start of the conversation, or record not maintained |
| Route under evaluation | Many rows carry `EVALUATION ONGOING` | Route decision genuinely open; usually a Rockwell or mixed-vendor plant |
| Mostly not integrated | Large share of `NOT INTEGRATED` | Check whether any use case wants the data before calling it a gap |
| No concept in Tool Overview | Plant has no concept row | Rollout conversation first, integration second |
| Integrated but undocumented | Most rows `INTEGRATED` but PLC model and protocol blank | Not repeatable by a second engineer |

## Record mismatches to look for

Compute these on the live lists; they show where two records of the same plant disagree. They
do not say which one is right.

| Mismatch | How to find it |
|---|---|
| Machines routed to the IIoT Edge platform, but Concept 3 is not in the plant's Tool Overview rows | Plants with Edge-routed rows minus plants with a C3 row |
| Machines routed to the Central OPCUA Aggregation Server, but Concept 1 is not in the Tool Overview rows | Same, for `Aggr.` and C1 |
| Concept 1 listed `AVAILABLE`, but no machine carries the aggregation route | Plants with a C1 row and no `Aggr.` rows; read the Tool Overview comment (a migration note explains some) |

Counting plants by machine route and counting them by Tool Overview concept rows give different
lists. Ask the IIAE which list is the reference. ⟨Which of the two records the department treats
as the reference for "plant has concept X". Who could supply it: IIAE.⟩

## Plants without machine rows

A plant note can exist with no machine at all. Such a plant has **no integration record**, not an
integration of zero: the first conversation is an inventory (Route A in
[`SKILL.md`](../SKILL.md)). Some of these plants still carry an unrelated tool row (for example
an Energy Management rollout).

## Patterns seen plant by plant (qualitative, no counts)

- **Large plant with a low-cost wave.** The `integration_approach` field records low-cost shapes
  ("Low Cost - Direct Connection", "Low Cost - Helmholz", plain "Edge", "Edge (together with
  camera)", Beckhoff clamps). A Helmholz gateway addresses a PLC without Ethernet; see
  `decision-paths.md`. The blocker "TIA V16 Upgrade necessary for TIA V17"
  clusters on S7-1500 and S7-1200 rows that are `NOT INTEGRATED`.
- **Mixed-vendor plant with routes under evaluation.** Vendors such as Bachmann and Philips
  appear next to Siemens; Philips rows tend to be `NOT INTEGRATED` (see
  `vendor-protocol-routes.md`). "Preferred integration with Softing
  OPC-UA DataFeed Suite" text can appear in the approach field.
- **Rockwell-dominated plant.** Edge-routed with many `NOT INTEGRATED` rows, or all rows with
  blank status and routes under evaluation. A blank-status plant is at the start of the
  conversation, not at a zero result.
- **Plant with a "Cybersecurity Vulnerability - Needs to be patched before integration" blocker.**
  Appears on S7-1500 rows; clear the firmware patch before the integration date.
- **Plant integrated but undocumented.** Rows are `INTEGRATED` but PLC model, network protocol and
  route are blank, and the vendor mix is mixed (Engel, Bachmann OPC, Siemens). It is integrated
  and undocumented at the level a second engineer would need
  (`od-data-availability-check` (`../../../skills/od-data-availability-check/references/machine-list-completeness.md`)).
- **Plant with blank status and method on most rows.** Concept approval can be dated in the
  Tool Overview comment (an eSign) while the Machine List is still empty.
- **Edge devices shared across cells.** Rows such as "Edge Device [Same as BMnn device] via
  Siemens TCP/IP Ethernet Driver" record a shared device; sharing changes the failure domain.
- **Wave blocker rows that are all one class.** For example "1x Edge Device ... dedicated to
  Module n needed", camera hardware, or "PLC Program missing, was wrong"; or the data-model
  standardization class ("Data model Standardization (CT Base)") recorded on rows whose
  controllers differ and that are often already `INTEGRATED`. See
  `blockers-and-waves.md`.
- **Plant with all tools `AVAILABLE` in the Tool Overview but machines not connected.** The tools
  are there; the machines are not. Do not read the tool rollout as machine integration.
- **Plant with a roadmap project reference and planned integration dates.** Planned dates that are
  earlier than the export date and already show `INTEGRATED` mean the field was not cleaned up.
- **Plant running a SCADA that gathers the data itself.** No method or route recorded; read the
  Tool Overview comment and the follow-up for the tool's cyber security assessment.
- **Plant with all rows `INTEGRATED` on one platform.** Either aggregation-routed (OPC-UA via
  RSLinx for Rockwell) or edge-routed with shared devices.

## Use

1. For a plant conversation, open the plant's row first, then the machine rows behind it.
2. Treat every flag as a question for the Plant ME / Plant IT, not as a finding.
3. When the plant is in a wave, the project reference in `integration_status`'s neighbour field
   names it; see `blockers-and-waves.md`.
4. Quote counts only after re-counting, with the export date of the list you used.

## Not in the records

⟨Per-plant lead times, budget, and the date by which a plant's remaining machines are planned.
Planned integration dates exist on a minority of rows; compare them with the export date and the
status. Who could supply it: OD lead and the regional IIAE.⟩

⟨Production criticality, cyber-security status and input protocol per machine: unpopulated fields
in the export; check the live list (see [`SKILL.md`](../SKILL.md)).⟩
