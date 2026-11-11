---
type: Skill Reference
title: Provenance and source catalogue
description: How to find content that lives in non-Markdown files via the source catalogues, how to use the verified reference library and published industry benchmarks without overclaiming, and how to record the provenance of any statement an agent produces.
resource: ../SKILL.md
status: draft
tags: [all, practice, context, provenance]
---
# Provenance and source catalogue

Derived from the knowledge base's source-catalogue notes, the sources README, the research notes behind the graph descriptions and the
reference-library index. Method only: file counts, source counts and benchmark figures are not reproduced. Own synthesis is marked
`PROPOSAL`; unknowns are `<...>`.

## 1. Where content hides, and how to find it

Much of the department's knowledge sits in decks, spreadsheets, PDFs, diagrams and attachments, not in notes. The **source
catalogues** index those files so that content can be found by searching text.

| Catalogue | Indexes | Use it when |
|---|---|---|
| Use-case attachments | Files attached to use-case records | You need the original brief, sketch or sheet behind a use case |
| Decks and strategy documents | Strategy, overview and keynote decks, workbooks | You need to know which deck states a position, and its structure |
| Work-notes attachments (multi-year) | Attachments to personal work notes | You are tracing an older decision or format |
| Generated and analysis sources | Pipeline outputs and analysis files | You need to know which generated file holds a list or export |

**Entry shape.** File name, type, size, slide or page count, location path, an **outline** (slide titles) and an **extract** (first
text). Files in languages other than English are listed by name and structure only. The catalogue is produced by a script that reads
the files and changes nothing.

**How to use it.**

1. Search the outline and extract for the topic words, not the file name.
2. Take the location path and open the original file; the catalogue is a signpost, not the content.
3. Cite the file and slide or page, never the catalogue entry.
4. Treat the extract as automatic and possibly truncated or mangled; **table structure often does not survive text extraction**
   (see the matrix trap in `od-context-freshness/references/fact-triage-and-generated-registers.md`).
5. If the catalogue and the file disagree, the file wins; report the drift to the catalogue's owner.

`od-information-integration-service/references/finding-decks.md` covers searching the slide index for the integration lane; this
file covers the catalogues for everything else.

## 2. Raw versus produced material

The sources folder separates **raw** material (list exports, decks, dumps) from **machine-produced** material (graph exports,
registers). Rules that follow:

- Nothing in the raw folders is hand-edited. A correction goes into the layer above (see `references/swot-and-dependency-seams.md`,
  section 5), never into the raw file.
- Machine-produced files are rebuilt, not repaired. Change the generator, not the output.
- A committed copy of a build artefact that claims to be current is a failure mode: it cannot be told from a stale one. Prefer a
  fingerprint or a rebuild date.
- Long-form generated reports can be older than the pipeline: an earlier knowledge-base document may carry counts that no longer
  match the current build. Treat its **definitions and checklists** as reusable and its **counts** as stale.

## 3. The reference library: tiers and "safe to claim"

External statements that notes rely on are kept as keyed entries. Each entry records the citation, the **tier** (for example
peer-reviewed paper, standard, practitioner glossary), the date retrieved, how it was verified, what it **safely supports** and what
was **not verified**.

| Tier idea | Meaning | Use |
|---|---|---|
| Peer-reviewed or standard | Strongest | May underpin a normative statement; still quote what the source says, not more |
| Practitioner glossary or institute page | Definition-level | Good for vocabulary; not for effect sizes |
| Vendor or practitioner blog | Weakest | Directional only |

**Rules.** Cite by key. Do not stretch a claim beyond the "safe to claim" line. External statements describe the outside world,
**not results from our plants**; never write them as ours.

## 4. Using published benchmarks

Published industry benchmarks back the "so that" benefit clauses of generated user stories and the cluster descriptions. They are
the best available stand-in for how comparable organisations do this, no more.

- **Mostly vendor sourced.** Treat as the range of what is achievable, not as an audited result and not as a forecast for a plant.
  The research notes say so for each cluster and name where no independent source was found; carry that gap into anything you write.
- **Prefer figures corroborated across independent sources**, and the strongest source over the biggest number.
- **Never put a benchmark in a plant's business case as its saving.** Savings come from the saving basis
  (`od-benefit-calculation`); a benchmark can set an expectation of direction.
- **Mind the baseline.** Manually captured performance figures (for example availability-type metrics) are typically more
  favourable than automatically measured ones, so the displayed value can **drop** after automation without any real regression.
  When comparing a post-digitization figure with a manual baseline, say which way each was measured.
- **Rollout pattern the sources agree on:** start with the highest-frequency alert or signal on one line, prove value in a short
  window, then scale in phases; do not do a plant-wide big bang. This matches the first-mover and fast-follower logic in
  `references/process-chain-practice.md`.
- **Escalation design pattern (vendor-sourced, illustrative):** safety signals bypass any delay rule; process-deviation signals
  route immediately to process engineering; an unacknowledged signal escalates to the next tier after a defined time-box.
  Take the *structure*; tune the time-boxes with the plant.

## 5. Stating provenance in what you produce

Every statement an agent writes should carry one of these tags, in words or as a footnote, so a reader can tell what to trust:

| Tag | Meaning |
|---|---|
| list or report, with read date | Read from a system of record or read surface |
| plant statement | Reported by a named role at a plant, with date |
| derived | Computed from the above; show the rule |
| domain knowledge | Standard terminology, not a plant statement |
| published benchmark | External, with tier and key |
| PROPOSAL | Own synthesis awaiting a human decision |
| `<unknown>` | Honest gap; to be collected |

`PROPOSAL`: when two tags disagree on a fact (a plant statement against a list), keep both with their tags and route the conflict to
the list owner; do not merge silently.

## AI agent operating notes

- **May do:** search the catalogues to locate the original file; extract and summarise with the file and page cited; compose a
  provenance footnote; flag claims that use a benchmark as if it were a plant result.
- **Inputs:** the topic words, the catalogue, the reference library keys.
- **Evidence to cite:** original file path with slide or page; reference key with tier.
- **Human gate:** a benchmark enters an external-facing document only with the OD lead's approval; conflicting provenance goes to
  the list owner.
- **Hands over to:** `od-benefit-calculation` (savings basis), `od-use-case-standardization` (cluster rationale),
  `od-context-freshness` (stale catalogue entries).
