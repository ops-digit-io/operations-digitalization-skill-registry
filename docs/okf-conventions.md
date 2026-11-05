---
type: Map of Content
title: OKF conventions
description: The Open Knowledge Format contract this registry follows, the three places it deviates from the knowledge-graph bundle and why, and what the guard refuses.
resource: ../registry.yaml
status: stable
owner: human:jakob.gabriel
tags: [conventions, okf]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---

# OKF conventions

This registry is an **[Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing)
bundle** as well as a library of [Agent Skills](https://agentskills.io): a directory of
Markdown files with YAML frontmatter, one required field, and ordinary relative Markdown
links between files forming the graph. It follows the same v0.2 contract as the
`ops-knowledge-graph` bundle it was derived from, so a consumer that reads one reads both.

The two formats are not in tension anywhere except one place, and that place decided the
whole design.

## The one real conflict, and how it is resolved

OKF wants `type`, `title`, `description`, `tags` and `timestamp` at the top of the file. The
Agent Skills spec allows **exactly six** top-level frontmatter keys in a `SKILL.md`:

```
name, description, license, compatibility, metadata, allowed-tools
```

Anything else is not ignored. Packaging with `package_skill.py`, uploading to claude.ai, and
the Skills API all fail with a hard error:

```
Unexpected key(s) in SKILL.md frontmatter: argument-hint.
Allowed properties are: allowed-tools, compatibility, description, license, metadata, name
```

So putting OKF fields at the top of a `SKILL.md` would make **every skill in this registry
undistributable**. It would be conformance bought by breaking the artefact.

**The resolution: a skill carries its OKF fields under `metadata`, which the spec defines as
a "free-form YAML map for your own key-value data, such as entitlement or catalog fields,
read by your own tooling."** That is precisely what this is. Every other Markdown file in the
bundle — references, assets, guides, docs — has no loader constraint and carries ordinary
top-level OKF frontmatter.

```yaml
# SKILL.md — the six spec keys only
---
name: od-signal-standardization          # equals the directory; this is the identity
description: >-
  ...                                    # serves both the loader and OKF
license: MIT
metadata:
  id: od-signal-standardization
  tier: technical
  ...
  okf:
    type: Agent Skill
    title: Signal analysis and standardization
    tags: [information-integration-service, od, technical]
    owner: human:jakob.gabriel
    generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
```

```yaml
# every other concept — ordinary OKF frontmatter
---
type: Skill Reference
title: Multilingual tags                 # slugs to the filename
description: One sentence saying what this is.
resource: ../SKILL.md                    # the skill this belongs to
status: stable
owner: human:jakob.gabriel
tags: [signals, translation]
generated: { by: claude-code/1, at: 2026-08-25T00:00:00Z }
---
```

A skill's `description` is not repeated under `okf:` — it is already at the top level, where
both readers find it.

## The types this bundle declares

OKF does not prescribe a vocabulary; a producer declares its own.

| `type` | What it is |
|---|---|
| `Agent Skill` | A `SKILL.md` — a procedure an agent runs |
| `Skill Reference` | Material a skill loads when it needs it, under `references/` |
| `Skill Asset` | A template or worked example a user copies, under `assets/` |
| `Skill Guide` | How to drive a skill, for a human or an assistant |
| `Map of Content` | Navigation and conventions |
| `Design Record` | How something came to be the way it is |

## Identity: what must match what

The knowledge-graph bundle requires `title` to equal the filename, so a graph label can be
found on disk. That rule cannot apply unchanged here for two reasons, and each gets its own
adaptation:

| Concept | The rule here | Why |
|---|---|---|
| Every file except `SKILL.md` | `title` must **slug to the filename** — `PLC packet` → `plc-packet.md` | Filenames here are kebab/snake slugs fixed by the skill layout, and renaming one breaks the paths inside `SKILL.md`. Slugging preserves the rule's purpose while letting a title carry its acronyms |
| `SKILL.md` | `name` must equal the **directory**; `title` is a free display name | `SKILL.md` is the same filename 24 times over, so it carries no identity. The directory does — it is where the loader gets the command name — and `name` is checked against it, which is a stronger guarantee than the filename rule it replaces |

**A title is a name, not a summary.** What the concept is belongs in `description`.

## Links, indexes and history

- **Links** are relative Markdown links with spaces percent-encoded. Bundle-relative links
  (`/docs/x.md`) are refused: a leading `/` means the repository root on GitHub, so one of
  the ways of reading these files would break. Wikilinks are not OKF cross-references and
  are refused.
- **`index.md` and `log.md`** are reserved (OKF §8 and §9). They are navigation and history,
  not concepts: they carry no `type` and never become graph nodes. Only the bundle root's
  index carries frontmatter, and only `okf_version`.
- **The indexes are generated.** Run `python3 scripts/build_okf_index.py` after adding a
  concept; `--check` fails if any index is stale.

## Trust

OKF derives a trust tier from `verified`, and nothing else may influence it:

- no `verified` → **unverified**
- machine or process actors only → **machine-confirmed**
- contains a `human:<id>` → **human-reviewed**

**Every concept here is currently unverified.** That is accurate, not modest: these skills
were derived from the knowledge graph and the source systems, and nobody has read them line
by line. An earlier version of this registry carried `last_verified: 2026-08-25` on all 24
skills, which asserted a verification nobody performed and carried no actor, so no trust tier
could be derived from it either way. It is now `sources_read` — the date the source data was
read, which is what it always meant. Add `verified: { by: human:<id>, at: <timestamp> }` once
somebody has read one.

## What the guard enforces

```bash
python3 scripts/verify_okf.py
```

| Rule | The failure it prevents |
|---|---|
| Frontmatter parses; `type` is non-empty and declared | OKF §11.2 — a file no consumer can read |
| A `SKILL.md` carries only the six spec keys at the top level | A skill that cannot be packaged or uploaded |
| A `SKILL.md` carries `metadata.okf` and its `name` equals the directory | A skill invisible to an OKF consumer, or one whose command name does not match its identity |
| Every other concept's `title` slugs to its filename | A graph label you cannot find on disk |
| `description` is present | A node in the graph with nothing under its name |
| `status` is one of `draft \| stable \| deprecated` | A vocabulary nothing can act on |
| `generated` names an OKF actor and an ISO 8601 timestamp | Provenance that says nothing |
| `resource` and every path-shaped `derived_from` entry resolves | A claim the bundle cannot back |
| Every in-bundle link resolves | A reference that navigates nowhere |
| No wikilinks, no bundle-relative links | Drifting out of conformance one convenient link at a time |
| The root has an `index.md`; no other index carries frontmatter | OKF §8 |

`derived_from` entries pointing into `ops-knowledge-graph/` are resolved against that bundle
when it sits beside this repository — including the abbreviated `.../`, `{a,b}` and `*` forms
the skills use. When it is not there, the guard says so in its output rather than passing
those paths silently.

## The one thing no guard can check

Whether a skill still describes what the department does. That stays a reading job.
