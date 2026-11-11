---
type: Skill Reference
title: Input intake
description: How to collect every input for an IT handover, including the user's own files (PDF, Excel, images, slides, mails, exports), read each one, register it, and never lose or invent anything.
resource: ../SKILL.md
status: draft
tags: [handover, inputs, attachments]
---
# Input intake

Do this before any package file is written. The handover is only as good as the inputs behind it, and the people who
hold them often have material that no template asks for: a spreadsheet of downtimes, a PDF from the supplier, a
screenshot of the current screen, a slide, a mail thread. Ask for all of it. Nothing the user provides may be dropped
silently, and nothing may be filled in that no input supports.

## 1. Ask, item by item

1. Show the user the twelve expected inputs from [`it-expected-inputs.md`](it-expected-inputs.md) as a checklist, in
   plain words, with what is already known from the front-end results (requirement, gate verdict, business case,
   approval route). Mark each as **known**, **partly known** or **missing**.
2. For every item that is partly known or missing, ask for it. Say what form helps and that any form is welcome:
   typed text, a file, a link, a screenshot, a photo, a forwarded mail.
3. Ask the open question, and repeat it until the answer is no: *"Is there anything else that describes this demand
   or the system around it: files, exports, drawings, supplier documents, earlier mails or slides, even if you are not
   sure it matters?"*
4. Ask who may see each file. A file that is not cleared for the external developer is marked `IT only` or `OD only` and
   its content is not copied into a file the external developer receives.

## 2. Read every file, by type

Read the whole file before relying on it. Say what was read and what was not.

| Type | How to read it | Watch for |
|---|---|---|
| PDF | Read every page; take text, tables and figures; note page numbers | Scans without text (read the image; if unreadable, say so), password protection, supplier marketing text that is not a requirement |
| Excel, CSV | List every sheet, the header row, the units and the row count; read formulas and named ranges where they define a figure; look at hidden sheets and filters | Hidden sheets, merged headers, mixed units, totals that do not add up, personal data in a column |
| Word, PowerPoint | Read the text, tables, notes and comments; for slides, every slide | Tracked changes, speaker notes, slides that were copied from another project |
| Images, screenshots, photos, drawings | Describe what is shown; transcribe visible text; name the screen, machine or system | Unreadable or cropped text, personal data, a screenshot of an old version |
| Mail, chat export | Read the thread in order; take the decision, not the quote | A later mail that reverses an earlier one |
| JSON, XML, flow exports, logs | Parse the structure; name the fields and what each means | Secrets or tokens in the file: stop, do not copy them, tell the user |
| Anything else | Ask the user what it is and what it is for; ask for an export to text, CSV or PDF | A format that cannot be read: record it as `not readable` and add an open item |

A figure taken from a file is stated with its source and its tag (see `dept-context`). A figure no file supports is not
written.

## 3. Register every input

Keep the files with the change: copy each into `attachments/` next to `proposal.md`, or give a link where the file
lives. Then record each in section 14 of `handover.md` (*Inputs and attachments*). One row per input:

| Column | Content |
|---|---|
| ID | `I-01`, `I-02`, ... in the order received |
| File or link | `attachments/<file name>` or an https link |
| Type | PDF, Excel, image, ... |
| What it is | One line, in the user's words where possible |
| Covers | The expected-input numbers (1 to 12) it supports, as `1, 6`; `extra` for material no expected input names |
| Used in | Where it feeds the package: `proposal Why`, `spec downtime-reason-capture`, `design Context`, `annex 8`, ... |
| Read | `in full`, `in part` or `not readable` |
| Share with | `IT and external developer`, `IT only` or `OD only` |

If the user has no further files, write the line `No attachments supplied (confirmed by <role>)` instead of the
table. The check accepts one or the other, never an empty section.

A row with `in part` or `not readable` also gets an open item (section 15) that names its ID and who supplies a
readable version.

## 4. Use the inputs, and trace them

- Every package statement that rests on a file names the input ID in the annex (section 14, `Used in`), so IT can
  find the source of a requirement, a figure or a constraint.
- A conflict between two inputs (two files give different volumes) is not resolved by choosing one. Write both,
  name the IDs, and add an open item for the owner to decide.
- A requirement or figure that no input supports stays `⟨…⟩` with who supplies it, or becomes an open item.
- A file that turns out irrelevant stays registered with `Used in: not used` and a reason in `What it is`, so the
  user can see it was read.

## 5. Before the check

Ask the user once more: *"Is every file you gave me listed in section 14, and is anything missing from the
checklist?"* Then run the check. It fails when a file under `attachments/` is not registered, a registered file is
missing, a cell is empty, or a row that was not read in full has no open item.
