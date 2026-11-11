---
type: Skill Reference
title: Vendored
description: OpenSpec 1.17.0 as shipped by its authors - the agent skills, the spec-driven schema, the documentation, README and license - kept inside this skill unchanged.
resource: ../../SKILL.md
status: stable
tags: [openspec, vendored]
---
# Vendored: OpenSpec 1.17.0

Copied unchanged from github.com/Fission-AI/OpenSpec, tag `v1.17.0`, commit `579fcac57ae00c2dff38f971b6d88b6f1f098b8a`, under the MIT license in
[`LICENSE`](LICENSE). Do not edit these files: refresh them with `python3 scripts/sync_openspec_vendor.py --from
<checkout>` after moving `OPENSPEC_PINNED`; CI fails when they drift from the tag. Links inside the copied files that
point outside this set (for example to OpenSpec's own `openspec/` folder) refer to the upstream repository at the same
tag.

The skills under `skills/` are the ones `openspec init` installs for an agent; this skill follows them for every
OpenSpec step and adds only what OD needs (inputs, annex, attachments, check). They need the OpenSpec CLI.

| File |
|---|
| [`LICENSE`](LICENSE) |
| [`README.md`](README.md) |
| [`docs/README.md`](docs/README.md) |
| [`docs/agent-contract.md`](docs/agent-contract.md) |
| [`docs/cli.md`](docs/cli.md) |
| [`docs/commands.md`](docs/commands.md) |
| [`docs/community.md`](docs/community.md) |
| [`docs/concepts.md`](docs/concepts.md) |
| [`docs/customization.md`](docs/customization.md) |
| [`docs/editing-changes.md`](docs/editing-changes.md) |
| [`docs/examples.md`](docs/examples.md) |
| [`docs/existing-projects.md`](docs/existing-projects.md) |
| [`docs/explore.md`](docs/explore.md) |
| [`docs/faq.md`](docs/faq.md) |
| [`docs/getting-started.md`](docs/getting-started.md) |
| [`docs/glossary.md`](docs/glossary.md) |
| [`docs/how-commands-work.md`](docs/how-commands-work.md) |
| [`docs/installation.md`](docs/installation.md) |
| [`docs/migration-guide.md`](docs/migration-guide.md) |
| [`docs/multi-language.md`](docs/multi-language.md) |
| [`docs/opsx.md`](docs/opsx.md) |
| [`docs/overview.md`](docs/overview.md) |
| [`docs/reviewing-changes.md`](docs/reviewing-changes.md) |
| [`docs/stores-beta/user-guide.md`](docs/stores-beta/user-guide.md) |
| [`docs/supported-tools.md`](docs/supported-tools.md) |
| [`docs/team-workflow.md`](docs/team-workflow.md) |
| [`docs/troubleshooting.md`](docs/troubleshooting.md) |
| [`docs/workflows.md`](docs/workflows.md) |
| [`docs/writing-specs.md`](docs/writing-specs.md) |
| [`schemas/spec-driven/schema.yaml`](schemas/spec-driven/schema.yaml) |
| [`schemas/spec-driven/templates/design.md`](schemas/spec-driven/templates/design.md) |
| [`schemas/spec-driven/templates/proposal.md`](schemas/spec-driven/templates/proposal.md) |
| [`schemas/spec-driven/templates/spec.md`](schemas/spec-driven/templates/spec.md) |
| [`schemas/spec-driven/templates/tasks.md`](schemas/spec-driven/templates/tasks.md) |
| [`skills/README.md`](skills/README.md) |
| [`skills/openspec-apply-change/SKILL.md`](skills/openspec-apply-change/SKILL.md) |
| [`skills/openspec-archive-change/SKILL.md`](skills/openspec-archive-change/SKILL.md) |
| [`skills/openspec-bulk-archive-change/SKILL.md`](skills/openspec-bulk-archive-change/SKILL.md) |
| [`skills/openspec-continue-change/SKILL.md`](skills/openspec-continue-change/SKILL.md) |
| [`skills/openspec-explore/SKILL.md`](skills/openspec-explore/SKILL.md) |
| [`skills/openspec-ff-change/SKILL.md`](skills/openspec-ff-change/SKILL.md) |
| [`skills/openspec-new-change/SKILL.md`](skills/openspec-new-change/SKILL.md) |
| [`skills/openspec-onboard/SKILL.md`](skills/openspec-onboard/SKILL.md) |
| [`skills/openspec-propose/SKILL.md`](skills/openspec-propose/SKILL.md) |
| [`skills/openspec-sync-specs/SKILL.md`](skills/openspec-sync-specs/SKILL.md) |
| [`skills/openspec-update-change/SKILL.md`](skills/openspec-update-change/SKILL.md) |
| [`skills/openspec-verify-change/SKILL.md`](skills/openspec-verify-change/SKILL.md) |
