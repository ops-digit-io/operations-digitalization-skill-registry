---
type: Design Record
title: Agent skills spec
description: "The open Agent Skills specification this registry follows: the rules, how each skill is checked, the one known deviation and how the download packages resolve it, and how a user gets the skills of a process step."
status: draft
owner: human:jakob.gabriel
tags: [specification, packaging, publishing]
generated: { by: claude-code/1, at: 2026-11-05T00:00:00Z }
---
# Agent skills spec

Every skill in `skills/` is a folder in the format of the open **Agent Skills** specification, so that any client that supports it can load the skill.
The rules below were read on 2026-11-05 from the specification and its reference validator.

| Source | URL |
|---|---|
| Specification | <https://agentskills.io/specification> |
| Overview, loading model | <https://agentskills.io> |
| Reference validator `skills-ref` (documented as a demonstration, not for production) | <https://github.com/agentskills/agentskills/tree/main/skills-ref> |

## The rules

| Part | Rule |
|---|---|
| Folder | `skills/<name>/SKILL.md` is required; `scripts/`, `references/`, `assets/` are optional |
| `name` | 1-64 characters, lowercase letters, digits and hyphens, no leading, trailing or double hyphen, equal to the folder name |
| `description` | 1-1024 characters: what the skill does and when to use it |
| `license` | optional string |
| `compatibility` | optional, 1-500 characters |
| `metadata` | optional, **a map from string keys to string values** |
| `allowed-tools` | optional, experimental: a space-separated string of pre-approved tools, for example `Read Grep Bash(python3 scripts/x.py:*)` |
| Other top-level keys | not allowed |
| Size | keep `SKILL.md` under 500 lines (instructions under about 5,000 tokens); keep reference files focused |
| File references | relative to the skill root, one level deep from `SKILL.md` |
| Loading | a client reads only `name` and `description` at start-up and the full `SKILL.md` when a task matches; scripts and references load on demand |

The specification does not say where a client looks for skills; that depends on the client.

## How the registry meets it

- **Checked by script.** `python scripts/agent_skills_spec.py` reports every skill against the rules above. `--export DIR` writes spec-strict copies and validates them; its exit code is 1 if an export is invalid.
- **Known deviation: structured `metadata`.** The registry's own checks read lists (`requires`, `composes`, `derived_from`) and a nested `okf` block from `metadata`. The specification asks for string values. The source skills therefore fail that one rule by design.
- **The packages are exported, not copied.** `--export` turns lists into comma-separated text, nested blocks into dotted keys (`okf.type`), and links from one skill into another into a text reference (`skill od-x, references/y.md`), because a packaged skill has to work alone. Every download package of the documentation site is such an export.
- **Not met everywhere: one level deep.** Reference files link on to other reference files in many skills. The script lists these as warnings. The reference validator does not check it.
- **Frontmatter size.** `description` stays under 1,024 characters in every skill (also enforced by `scripts/validate_registry.py`).

## Getting the skills of a process step

1. Open the documentation site's **process map** (built by `python scripts/build_site.py`, output in `site/`, static, works from the file system; also `docs/new-state-skill-map.md` for the same mapping as a table).
2. Pick a lane and a step. Each skill chip opens its description, its authority level, where else it sits in the process, and links to the skill page and its download.
3. **Download the lane** (all skills of that lane) or a single skill as a `.zip` and place the folders where your client reads skills.

The mapping of skills to steps is data: `docs/new-state/process.yaml`. A skill the New-State files do not name on a step is shown with a dashed outline (*proposed*).

## Libraries

The repository holds two libraries side by side: `skills/` (core, the skills the four New-State process files name) and `skills-extension/` (optional add-ons). Both follow the same specification rules and the same export; the site and the downloads (`core-library.zip`, `extension-library.zip`) keep them apart.

## Publishing

`scripts/build_site.py` produces a static site. CI (`.github/workflows/validate.yml`) builds it on every push and keeps it as a downloadable artifact. The site is published on GitHub Pages at <https://ops-digit-io.github.io/operations-digitalization-skill-registry/> by the manual workflow `.github/workflows/pages.yml` (Actions, "pages", run workflow on `main`). Pages must stay on **Settings, Pages, Source: GitHub Actions**; the legacy branch build serves the Markdown through Jekyll instead and hides the process map.

The repository and the site are public. Skills are guidance and process and carry no current company figures (`scripts/check_no_figures.py` lists lines that still look like figures); the licence line "Internal - not for external distribution" in the skill frontmatter predates this and should be reviewed by the owner.
