---
type: Design Record
title: Skill output contract
description: How every skill's outputs are made checkable and enforced - outputs.yaml per skill, SKILL.md without prose, one run record per call with a checklist, the structure check, the Stop hook, what is automatic and what stays manual.
status: draft
owner: human:jakob.gabriel
tags: [skills, outputs, enforcement]
generated: { by: claude-code/1, at: 2026-11-16T00:00:00Z }
---
# Skill output contract

## Rules

| Rule | Enforced by |
|---|---|
| `SKILL.md` holds structure only: headings, tables, list items of at most 40 words, code blocks | `scripts/skill_form.py` (in `validate_registry.py` and CI) |
| Context, rationale and examples live in `references/background.md`, never as an instruction | `scripts/migrate_skill_form.py` moved them once, nothing lost (`--verify`) |
| Every skill has `outputs.yaml`: gate, outputs, criteria, checks or sign-off, hand-offs, stop conditions | `scripts/skill_outputs.py` (in `validate_registry.py` and CI) |
| An output without a check and without a sign-off is refused | `scripts/skill_outputs.py` |
| `references/outputs.md` is generated from `outputs.yaml` | `scripts/skill_outputs.py --write`, stale file fails CI |
| Every call writes a run record with one row per criterion | `scripts/run_record.py` |
| A session does not end with an open run record | `scripts/stop_hook.py` (Claude Code Stop hook, not active until you add it) |

## `outputs.yaml`

| Key | Meaning |
|---|---|
| `gate` | Inputs that must exist before step 1; one missing means the run is refused |
| `outputs[].id`, `form`, `template` | The output, its form, the template it follows (optional) |
| `outputs[].to_skills`, `to_roles` | Who receives it |
| `outputs[].done_when` | Criteria; each needs evidence in the run record |
| `outputs[].check` | `cmd` (a command with `{file}`) and/or `structure: true` |
| `outputs[].signoff` | The role that signs (a human) |
| `receives_from`, `next`, `stops_when` | Hand-offs and stop conditions |

## Run record

| Step | Command |
|---|---|
| Create, with checklist | `python scripts/run_record.py new <skill-id> [--dir runs] [--supersedes <run-id>]` |
| May it be closed | `python scripts/run_record.py check <record> [--run-checks]` |
| Which are open | `python scripts/run_record.py open [--dir runs]` |

Header: `skill`, `skill_version` (folder hash), `run_id`, `started`, `status`, `supersedes`. Status: `open`, `done`, `refused`, `blocked`, `awaiting-signoff`.

| Status | Allowed when |
|---|---|
| `done` | Every gate row met, every criterion done with evidence and an output file, every check exited 0, every sign-off entered |
| `awaiting-signoff` | As `done`, but a human has not signed yet |
| `refused` | At least one gate row not met |
| `blocked` | Work cannot continue; the reason is in the open items |

Versioning: a record is never overwritten; a new attempt names the one it supersedes; the records are committed with the work; `skill_version` shows which version of the skill produced the answer.

## Checks

| Kind | What it proves | Coverage today |
|---|---|---|
| Structure (`structure: true`) | The output keeps every section of its template and has no open placeholder | Every output with a Markdown template |
| Command (`cmd`) | The skill's own check script exits 0 | `funnel-features`, `comms-brief`, `funnel-requirements`, `process-derivation` |
| Evidence per criterion | A person or agent named a file, a place or a result for each criterion | Every output, by `run_record.py check` |
| Sign-off | A role accepted the output | Every output without a full automatic check |

## What it does not do

- It does not prove that an output is true; truth stays a human sign-off.
- Outputs without a template and without a script have only evidence and sign-off.
- A hook enforces that a record is closed; it does not read the content.
- The hook is a script in this repository; Claude Code runs it only if it is added to a settings file.

## Stop hook

```json
{"hooks": {"Stop": [{"hooks": [{"type": "command", "command": "python <registry>/scripts/stop_hook.py"}]}]}}
```

Exit 2 keeps the session working and shows the open records. `$OD_RUN_DIR` sets the folder (default `runs/` of the working directory). After one block in a turn it lets go, so it cannot loop.
