---
type: Skill Reference
title: Instances
description: Guidance, no figures - how Node-RED instances are named and discovered, what a site code is, what the instance shape tells you, and how to count flows per instance live.
resource: ../SKILL.md
status: stable
tags: [node-red, estate]
---
# The Node-RED estate

Instances and flows are auto-documented by `node-red-auto-docs`. This page holds **no counts**: how many
instances exist and how many flows each carries changes with every export. Count live (see below) and
quote the figure with its source and date.

## Naming

```text
ct-oesl-<plant-code>-nodered-<prod|test>[N]
```

The doc generator discovers repositories with the regex
`^ct-oesl-.*-nodered-(prod|test).*` in the `ct-oesl` GitHub organization, clones each, and
reads its `flows.json` (or `flow.json`). An instance not matching that pattern is invisible
to the documentation — which is a reason to follow it, not a naming preference.

The trailing `2` / `-2` variants (`…-prod2`, `…-test-2`) are second instances at the same
site, not versions.

## Flows per instance: how to count

List the folders under `ops-knowledge-graph/_knowledge/node-red-auto-docs/docs/` (one per instance)
and count the flow JSON files in each. The result is a per-instance and per-site-code table to build on
the day; it is not kept in this skill because it would drift. A generated dashboard page may report
totals that differ from the file count; see `corpus-census.md` for
how to treat sources that do not reconcile.

## Plant codes

Some codes are confirmed by the `CT/…` topics inside the flows themselves:

| Code | Plant | Confirmed by |
|---|---|---|
| `qda` | Qingdao | `CT/OESL/AS/CHN/QDA/…` |
| `spr` | Sun Prairie | `CT/OESL/NA/USA/SPR/…` |
| `cshz` | Changshu | `CT/MFS/AS/CHN/CSHZ/…` |

The remaining codes are OESL site codes and are **not** resolved to plant names here, because nothing in
the bundle states the mapping. ⟨Site-code table — to confirm with the IIAE.⟩ Do not infer one from a name
that merely looks similar; the Machine List's plant names are the authority and joining on a guess would
produce a wrong per-plant figure.

`mpee` is not a plant: its instance is a department test instance.

Several numbered codes (for example `wth1` to `wth4`) can be separate instances at one site, which is why
the site appears more than once.

## What the shape says

**Test often carries as much as prod, sometimes more.** Test instances here are working environments,
not scratch — which is why "build on test" is a workable rule rather than a formality, and also why a test
instance can hold a literal secret that matters. Compare prod and test per site before assuming one is the
superset of the other.

**Flow count is not maturity.** A site with few flows may have a single well-built integration; a site
with many may have accumulated variants. Read the flows, not the count.

**Some flows are marked disabled.** Count them live from the `disabled` value of each flow's first
element in the exported JSON. See `corpus-census.md` for how to read
the split, including the protobuf-config bootstrap tab that is meant to be disabled after its first run.

## The documentation pipeline

`generate_docs.py` produces, per flow: a Markdown page (title, repository, flow id,
disabled state, description, an embedded interactive flow renderer, a node-details table
and a groups table) plus the flow's own JSON beside it, and rebuilds `mkdocs.yml` nav and
an index dashboard. It needs `GH_ORG`, `GH_REPO_PATTERN`, `GITHUB_PAT`, and optionally
`GH_API` for GitHub Enterprise.

Everything on the generated page comes from the flow itself: the tab `label` and `info`,
each node's `name` and `info`, and each group's `name`. There is no separate documentation
source and no place to add prose afterwards — **the flow is the documentation**.
