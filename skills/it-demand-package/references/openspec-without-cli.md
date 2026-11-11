---
type: Skill Reference
title: Openspec without cli
description: How to run OpenSpec's own skills with no OpenSpec CLI (Claude Cowork and other skills-only setups) - every CLI command the skills call, and what to do instead.
resource: ../SKILL.md
status: draft
tags: [openspec, cowork, handover]
---
# OpenSpec without the CLI

OpenSpec's skills ([`openspec/skills/`](openspec/skills/README.md)) are written for agents that can run the `openspec`
command. In Claude Cowork, or anywhere the CLI is not installed, follow the same skills step by step and replace each
command with the line below. Nothing else changes: the skill's steps, its order of artifacts, its planning boundary and
its guardrails still apply. The helper answers from the OpenSpec copy inside this skill (schema and templates of the
pinned release) and from the store's `openspec/config.yaml`; the repository's CI compares its answers with the real CLI.

`<store>` is the OD store folder (it holds `openspec/`); `<change>` is `<store>/openspec/changes/<change-id>`.

| The OpenSpec skill says | Without the CLI |
|---|---|
| `openspec context --json` | The root is `<store>`. Read `<store>/openspec/config.yaml`: its `context` and `rules` are constraints for you, not text for the files |
| `openspec new change "<id>"` (with or without `--store`) | `python3 scripts/openspec_offline.py new <store> <id>` |
| `openspec status --change "<id>" --json` | `python3 scripts/openspec_offline.py status <change>` |
| `openspec instructions <artifact> --change "<id>" --json` | `python3 scripts/openspec_offline.py instructions <change> <artifact>` (same fields: `instruction`, `template`, `context`, `rules`, `dependencies`, `unlocks`, `outputPath`) |
| `openspec list --specs`, `openspec show "<spec>" --type spec` | Read the folders and files under `<store>/openspec/specs/` directly |
| `openspec list` (changes), `openspec show "<change>"` | Read `<store>/openspec/changes/` directly |
| `openspec validate "<id>" --strict` | `python3 scripts/check_handover.py <change>` (OpenSpec's rules offline, plus the OD annex) |
| `openspec store list`, `store register`, `--store "<id>"` | Not needed: work inside the store folder |
| `openspec init` | Not needed: the store already has `openspec/`; `openspec_offline.py new` creates it in an empty folder |
| `openspec apply`, `archive`, `sync`, `verify` (apply, archive, verify, sync skills) | IT's steps, run where the CLI is installed; OD does not run them |

If Python cannot run at all, read the same answers by hand: the artifact order and each `instruction` are in
[`schema.yaml`](openspec/schemas/spec-driven/schema.yaml), each `template` in
[`templates/`](openspec/schemas/spec-driven/templates/proposal.md); an artifact is done when its file exists. Then
check the package against [`openspec-format.md`](openspec-format.md) and say that it was checked by hand.

Where the CLI is installed after all (IT, Claude Code), use OpenSpec's commands as written; `check_handover.py` then
also runs `openspec validate --strict`.
