---
type: Skill Reference
title: Machine list completeness
description: How to measure, live, how complete the Machine List is for a plant - which fields to count, which patterns to expect, and which plants cannot answer step 2 (is the machine integrated) from the list - so a blank is never read as a no. Guidance only; no fill rates or per-plant figures.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [analytical-support-service, practice]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---

# Machine list completeness

Step 2 of the six steps asks "is the machine integrated?" and answers from the Machine List.
That answer is only as good as the field behind it. Before you run the check, measure **live**
whether the list can speak for the plant at all. This file says what to count and how to read
it. It holds no fill rates: they change with every edit of the list, so re-count on the
current export and name the export date.

## How to measure

1. Take the current `Machine-List` SharePoint export (or the `Graph/Machines` notes that quote
   it) and note the export date.
2. Filter to the plant. For each field below, count rows with a non-empty value, and divide by
   the plant's rows. Do this per plant, not only for the whole list: the estate-wide average
   hides plants that cannot answer at all.
3. Keep the count next to its date in the verdict. A count without a date is not a status.

## Fields to count, and what each one decides

| Field | What a blank means for the check |
|---|---|
| Controller vendor, PLC model, PLC part number | Steps 3 and 4: the connector cannot be matched specifically |
| Network protocol | Step 3: connector match from the other side |
| Integration status | Step 2: **blank is "not recorded", never "not integrated"** |
| Integration route (method) | Which ingress variant; without it, what is published is unknown |
| Priority | When it will be integrated, if it is not |
| Integration date | Whether history exists as far back as an analysis needs (step 5, depth) |
| Process area, project reference | Which wave or project the machine belongs to |
| Free-text approach and free-text blockers | The only place a blocker is written; rarely filled |
| Typed fields for production criticality, cyber-security status, input protocol, machine blockers | Check whether they are used at all; if empty everywhere, "is this machine critical" and "is its cyber-security status approved" cannot be answered from the list |

## Patterns to expect (kinds, not numbers)

- **Plants with no machine rows at all.** Step 1 (does a machine produce the signal) has no
  inventory; the answer comes from the plant, not from the list. Find them by comparing the
  plant list (`Graph/Plants`) with the plants that have machine rows.
- **Plants with status blank on every row.** Step 2 cannot be answered from the list. Say "not
  recorded", and ask the Plant ME.
- **Plants with status blank on most rows.** Report the recorded share and call the rest "not
  recorded"; never report them as "not integrated".
- **Plants with status complete but little else.** Step 2 is answered, steps 3 and 4 (which
  connector, which route) are not: model, protocol or route are empty. Ask the IIAE for the
  connector chain before promising a signal.
- **Plants with status complete but priority missing** cannot say when a machine would be
  integrated.
- **`INTEGRATED` rows with no date** and **dated rows that are not `INTEGRATED`**: a date is the
  best evidence that a machine has delivered data since then, but the list does not say it
  still does (step 5 stays unproven).
- **Vendor spelling variants** (a company name, its short form, an abbreviation, upper and lower
  case). A single-string match undercounts: build the variant list from the data.
- **Rows tidied to `-`.** The narrative may be in the version history: text was often written
  during active work and then tidied back; the knowledge base's `SharePoint record (full text)` block of
  the machine note shows earlier values when they exist.

## Procedure for a key user

1. Count the fields above for the plant. If the status share is below the whole plant, say in
   the verdict that step 2 is "not recorded" for the missing share of rows.
2. For the machines the request needs, ask the Plant ME for the actual status and record it
   in the Machine List (the SharePoint list is the write surface; a correction made in the
   knowledge graph does not travel, per the department's *Systems of record* note).
3. Where the list shows `INTEGRATED` but vendor, model or route is blank, treat steps 3 and
   4 as unproven and ask the IIAE for the connector chain before promising a signal.
4. Match a vendor by all its spellings.

## What the script does with these gaps

[`scripts/check_availability.py`](../scripts/check_availability.py) reports *unproven* for a
step it cannot answer and never *absent*. For plants in the blank-status groups above, expect
step 2 to come back unproven for most machines. That is the correct result and not a defect
of the check: the remedy is a Machine List update by the plant, which is a data request, not
an integration request.

⟨Whether the Machine List is audited for completeness anywhere (a periodic check or an
owner per plant). Who could supply it: OD lead.⟩

## Sources

- Knowledge base `Graph/Machines` notes quoting the `Machine-List` export; take the export date from
  the note.
- Department note *Systems of record* (`_knowledge/10-Department/Systems of record.md`):
  write surface, version history, absence is not a zero.
