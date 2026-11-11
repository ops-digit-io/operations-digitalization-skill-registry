---
type: Skill Reference
title: Fact triage and generated registers
description: A pattern for triaging a staging pile of extracted facts (verdict per bucket, why, order of work), the limits of text extraction, and how to keep generated registers honest, including the masking review that needs a human check.
resource: ../SKILL.md
status: draft
tags: [all, practice, freshness, registers]
---
# Fact triage and generated registers

Derived from the knowledge base's ODEC-facts triage note, the register hub and the full-text masking review. The per-plant fact notes
themselves are company facts and are **not** used here; only the structure of the triage and the register hygiene are.
No counts, savings values or per-plant status are carried. Own synthesis is marked `PROPOSAL`; unknowns are `<...>`.

## 1. What a triage is

A triage is an assessment of a **staging folder** of extracted facts: what has already been acted on, what is worth pursuing per
bucket, what is not, with reasons, and a suggested order. It is *not* an enrichment. Its value is that a later pass (by hand or by
a generator) does not re-derive the same judgement calls.

### Structure to copy

1. **Purpose** in two sentences, stating it is an assessment.
2. **Already acted on**: facts folded into their destination notes, with the route (script or manual) so duplicates can be
   recognised. Remaining copies in the staging file are usually earlier drafts or exact duplicates.
3. **Per bucket verdict table**: item, verdict, why.
4. **Plant (or entity) buckets**: how much genuine single-entity content there is, ranked by density of non-duplicate content.
5. **Recommendation**: order of work and what is explicitly not worth pursuing.
6. **Sources and status line**: internal evidence, nothing verified by a human.

### Verdict vocabulary

| Verdict | Use when |
|---|---|
| Done | Folded into its destination; the staging copy is redundant |
| Minor remainder | A little genuine content, thin and low priority; append as short examples if wanted |
| Not usable as extracted | The extraction lost structure (see section 2); needs the original image or file |
| Reinforces an existing gap | More detail on something that still has no home note; name the missing note |
| Low value | Mostly headings or repeated text; not worth a note |
| No new detail | Restates what the destination already holds |
| Scope decision | A new kind of artefact would be needed; flag for the owner, do not act unprompted |

### Reading a plant bucket

A large share of what a keyword tag attaches to a plant is a **multi-plant summary table** (a ranking, an approval list, a savings
forecast) and not plant narrative. Judge a bucket by the **single-plant** content only. Before adding anything to a plant note, read
that plant's existing notes first: the fact may be new, a duplicate, or a status update, and only the existing note tells you which.
That makes the work plant by plant, not a bulk operation. Order: highest density of new single-plant content first.

## 2. Limits of text extraction

- **Matrices do not survive.** A readiness table (systems in rows, status phrases in columns) can come out as one flattened list
  where which phrase belongs to which system cannot be told. Do not apply it anywhere; verify against the original slide image.
- **Section-header slides with no body** usually held the status in an image or table that did not extract.
- **Near-verbatim repetition across calls** is the same content re-presented: keep one.
- **Teaching examples** (generic improvement methods) are not facts about a plant or tool.
- **Amounts and targets in a slide** are internal claims of that deck's date; they belong to a saving basis review, not to a note.

When an agent meets a flattened table, it reports "structure lost, original needed" and names the slide; it does not guess the cell
assignment.

## 3. Time series of department indicators

A call-to-call series of department figures (pool size, target versus actual, regional plan versus today) is a **new kind of
artefact** that fits none of the plant, tool, use-case or initiative note types. Triage flags it as a scope decision for the owner.
`PROPOSAL`: if the owner decides to keep such a series, store it as a dated table with source slide per row and never overwrite a
row; the read surface for current values remains the Scorecard.

## 4. Generated registers: keep them honest

The register hub states the rules; carry them into any register an agent builds or reads.

| Rule | Why |
|---|---|
| Header carries who or what generated it and "not reviewed by a human" | A reader must know the trust level |
| Themes inferred by keyword are labelled as inferred; the texts under them are verbatim | Themes are leads, texts are evidence |
| Amounts are labelled internal claims, not verified | A register is not a savings approval |
| Change the generator, not the output | Hand edits vanish on the next build |
| Aggregates are produced by script; prose written by hand does not update itself | After a new export, compare the aggregates with the numbers in the prose |
| A committed build artefact claiming to be current is a risk | Use a fingerprint or rebuild date |
| Several runs of the same export are not several datasets | Merge per key and keep the newest complete run, as the analysis script does |

## 5. The masking review

The full-text layer copies list items verbatim after scrubbing links, hosts, addresses, e-mail and credentials, and **masking the
names of individuals**. A review register lists, per note, how many maskings were made (full names, single first or last names,
honorific plus name, greeting plus name) so a human can check them. The masked text itself is never shown.

**How to read it.**

- The counts show where the mask was applied, not whether it was right. A high count in a note with many comments is expected.
- Limits are stated on the register: a person who never edited an item and whose first name is not on the name list is **not**
  caught; a surname that is an ordinary word may be left visible; a product or place word that is also a name may be masked.
- Fix the rule in the masking script, not in the notes, then rebuild.
- Greeting detection ("Hi X", "@X") is a separate counter because it catches names the author lists miss.

**For an agent:** never quote a masked or withheld passage's surroundings in a way that re-identifies a person; write roles. If a
visible name appears in a generated note, report it to the owner of the masking rule instead of copying it.

## 6. Hygiene checklist (before relying on a generated or staged source)

1. Who or what generated it, when, from which source version?
2. Is it labelled reviewed or not?
3. Which parts are inferred and which verbatim?
4. Has the source been re-exported since? If yes, re-run, do not patch.
5. For a staging pile: is there a triage? If not, write one before using any fact.
6. Which facts have been acted on, and where do they live now?

## AI agent operating notes

- **May do:** triage a staging file into the verdict table with reasons; flag flattened tables; compare a register's aggregates
  with the prose that cites them; list the masking counts of notes touched by a task; propose the order of plant-by-plant work.
- **Inputs:** the staging file, the destination notes, the register header and sources section.
- **Evidence to cite:** staging file and slide or row, destination note, generation date.
- **Human gate:** the owner decides scope questions, any fact that changes a plant note, and any change to the masking rule.
- **Hands over to:** `triage-and-actions.md` for owners, `od-context` (corrections go to the source list), `od-equipment-integration`
  for tool and readiness records.
