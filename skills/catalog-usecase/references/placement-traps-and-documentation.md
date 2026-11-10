---
type: Skill Reference
title: Placement traps and documentation
description: Where catalog matching goes wrong on template placement (same title in different templates, mis-templated records, the catch-all), what "Other Use Cases" resolves into, and the documentation standard that decides whether a peer is a usable match. Pattern only, no counts.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [all, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Placement traps and documentation

Source: vault `Graph/Use Case Views/Use Case Views - Standardization` (placement rules R1 to R13, review lists), the eleven template
pages, and the vault's microservice-landscape draft (`Microservice Apps (WIP)`, "Extension Services"). AI-drafted, not reviewed by a
human; the vault changes only through its generator, so state the export date. No counts here: read them live.

## Why placement is the first catalog risk

A match is only as good as the template the request was placed on. The vault itself says the recorded placements are not fully
consistent and that its own review lists are "review candidates, the graph is not changed". Three recurring shapes:

| Shape | What it looks like | What to do |
|---|---|---|
| Title points to another template | A recorded "Other Use Cases" whose title is a first-part inspection sheet (Manual Quality Data), or a recorded "Process Values" case titled as a leak tester (Process Quality Data) | Apply R12 precedence: purpose stated in the target text beats the title, the title's head noun beats the tool. Then decide |
| Same title, different templates | Generic titles ("Andon Board", "Process Values", "Traceability", "Machine Errors", "Availability for Machines") placed in more than one template | Never match on title alone. Read the purpose and the data source; the less common recorded placement is the one to question first |
| Dashboard family names a solution of another template | A board shows status, stops and OEE together; the family spans templates by design | A family may show several templates: a mismatch is a question, not an error. Match each function to its own template |

The vault warns that its own keyword check against the recorded placement disagrees with the record often enough that a sizeable
share of its flags are the rule's mistake. So a flag is a prompt to look, not a verdict. Hand-fixing a placement is not allowed:
curated placements live in the generator input, not in the generated block. Raise the correction to the vault owner.

## The boundary pairs that are mixed up most

| Pair | The test |
|---|---|
| Machine Alerts / Andon Board | Is a message sent to a person (alert) or is a status shown to people who are there (board)? |
| Downtime Reporting / OEE Calculation | Is it the stop event with duration and reason, or the availability percentage? An "OEE" request often asks only for availability |
| Cycle Time / Downtime Reporting | Is the gap a slow cycle or a stop? Classifying the gap is the downtime function |
| Process Values / Process Quality Data | Does it show what a parameter is, or judge a measurement (SPC, pass/fail)? |
| Process Quality Data / Manual Quality Data | Same physical test; the source of the record decides: automatic versus typed |
| Process Values / Recipe Values | Actual value versus what the value should be; set-value transfer is Recipe Values |
| Process Values / Analytics | Live display of one machine or line versus analysis across machines, lines or plants; energy monitoring versus energy analysis (R5) |
| Analytics / Other Use Cases | Production-data model or report versus AI helper on documents (R3, R11) |

## What "Other Use Cases" resolves into

The vault's microservice draft read the whole residual item by item and found that most of it is not formless. For matching, treat
"Other Use Cases" as five recurring sub-patterns plus a small number of true one-offs, and some records that belong elsewhere:

| Sub-pattern | Typical content | Catalog reading |
|---|---|---|
| AI knowledge and document assistant | LLM helpers for work instructions, IT problem solving, lessons learned | Not production data. Route through `od-ai-generation-playbook` governance, not as a template match |
| Workplace and operator administration | Work instruction visualisation, shopfloor change management (4M), HR and safety administration | Office or workplace app; a peer may exist, the data is not machine data |
| Production-to-ERP integration | Booking scrap or output to the ERP, label printing automation | Integration work; follows the systems-of-record rule of one source per data object |
| Mold and tool lifecycle | Tool cycle counts and service due | Tool management; often a small shared app |
| Device and camera status | Health of cameras and controllers | Infrastructure monitoring |
| Mis-templated records | Waiting and cycle time calculation, dryer monitoring, energy versus output, multi-machine optimization | Belong to a named template (Cycle Time, Machine Alerts, Analytics): re-place before matching |
| True one-offs | Plant-specific tools with no second user | Not a catalog entry; individually catalogued container in the store (`deploy-appstore`) |

The landscape draft is **design only**. It says nothing about which of these exist as running services. Use it to classify a
request, not to promise a service.

## Documentation standard: when is a peer a usable match?

The vault defines, per plant and template, how well a delivered use case is described:

| Level | Meaning | Consequence for a match |
|---|---|---|
| Fully described | The plant has a reference solution (library entry or archive-derived note) and a dashboard family in the same template, and archive evidence on at least one note | The peer can hand over a working description; prefer it |
| Partly described | Only one of reference solution and dashboard family exists | Call the plant; expect a walkthrough, not a copy |
| Bare | Only the use case note | A delivered case, not a documented pattern. The fastest next step is to write up the existing solution, not to build a new one |

Template pages show where documentation is thin. A template with delivered cases but mostly bare plants is a weak match source;
Recipe Values has been the thinnest. Check the live figures before you quote a level.

## Choosing the reference solution to point at

1. Prefer the entry of the same template and the same process group as the request.
2. Among those, prefer a fully described plant; then a library entry with a recorded CSP `Yes`
   (`references/library-and-csp-state.md`).
3. The template page's "reference implementations to start from" are **inferred** (best word match plus best documented): say so.
4. A dashboard that composes several templates is a composition, not one entry; name the parts.

## Pitfalls

- Matching a title. Titles are generic and repeated; read purpose, data source, and who sees it.
- Counting a template as covered because a use case exists: delivered, documented and used are three separate states.
- Calling a catch-all hit a match. An "Other" record is a pointer to a conversation, not a standard.
- Taking a family or a placement set by curation as recorded: the vault marks curated placements and their confidence; low-confidence
  ones are the first to check.

## AI agent notes

The agent may propose the template with rule ids (R1 to R13) and the boundary pair that decided it, list the two nearest peers with
their documentation level, and flag same-title conflicts. It cites the template page and the export date. It does not change any
placement, does not state that a service exists, and hands the verdict "match / partial / no match" to the DBVE.
