---
type: Skill Reference
title: Quality gates
description: The gates a new or changed skill passes, in order, with the command for each, what a failure means and how to repair it - registry validator, specification export, OKF, figures check, the SkillEvaluator quality rating - plus the known conflicts between the tool and the specification. Open it at step 7 of the method.
resource: ../SKILL.md
status: draft
tags: [skills, practice, quality]
---
# Quality gates

Run from the repository root. Gates 1 to 4 also run in CI (`.github/workflows/validate.yml`); gate 6 needs the SkillEvaluator and is run by hand.

| # | Gate | Command | A failure means |
|---|---|---|---|
| 1 | Registry and frontmatter | `python scripts/validate_registry.py` | A name, description length, required metadata field, listing, flow placement or authority mismatch; the message names the file |
| 2 | Agent Skills specification | `python scripts/agent_skills_spec.py --export dist` | The strict export is invalid: an unknown top-level key, a name that is not the folder, a link into another skill the export cannot rewrite. Warnings (references that link on to other references) do not fail |
| 3 | OKF conformance | `python scripts/build_okf_index.py` then `python scripts/verify_okf.py` | A file without frontmatter, a `title` that does not slug to the file name, a source path that does not exist. The check takes minutes |
| 4 | Generated pages current | `python scripts/build_okf_index.py --check`, `build_skill_map.py --check`, `build_new_state_skill_map.py --check`, `build_skill_quality.py --check` | A generated page is stale: run the generator, do not edit the page |
| 5 | No invented figures | `python scripts/check_no_figures.py <name>` | Lines that look like a company figure. It is a heuristic with many false positives (colours, ids, years): read each line, remove or mask what is a real claim |
| 6 | Quality rating | see below | A grade below the target, or findings worth fixing |

## Gate 6: the SkillEvaluator quality rating

The registry rates every skill with NVIDIA SkillEvaluator (Apache-2.0, `github.com/NVIDIA/SkillEvaluator`), tier 1 `quality-check`, deterministic and offline, using `config/skill-quality.yaml` (documentation: `docs.nvidia.com/skills/skillevaluator`, read 2026-11-10). The tool needs Python 3.12 or newer. Running it downloads and executes third-party code: do it only where that is allowed, and ask the owner if a sandbox blocks it.

```bash
skillevaluator quality-check skills-extension --quality-config config/skill-quality.yaml -r json -o <output>
python scripts/build_skill_quality.py <output>/skillevaluator-quality.json --tool-commit <sha> --run-date <date>
```

The score is the weighted sum of four categories, each starting at 100 and losing points per finding: Correctness 35%, Discoverability 25%, Reliability 25%, Efficiency 15%; grades A from 90, B from 80, C from 70, D from 60. **Proposed target: B or higher before the pull request**; below C is repaired first. The rating measures documentation, not task success (that is the tool's tier 3, not run).

### What the common findings mean and what to do

| Finding (deduction) | Repair |
|---|---|
| No `## Purpose` section (5) | Add one paragraph on what the skill is for |
| No examples provided (5) | Add one worked example with a code fence |
| Broad description without negative triggers (5) | End the description with "Not for ...": the boundary against neighbouring skills |
| No human gate, procedure, inputs or definition-of-done heading (5 each) | These are this registry's expected sections (`config/skill-quality.yaml`); a skill that truly lacks one should say why or gain the section |
| Deeply nested references (10) | A reference links on to another reference: link from `SKILL.md` instead, or merge the files. The generated `index.md` files are also flagged: a tool artefact |
| Large skill (over about 5,000 tokens) | Move detail into `references/` |
| Instructions do not mention `run_script`; no scripts in table format (10 each) | Only for skills that ship scripts: add a `## Scripts` table (script, purpose, arguments) |
| No mention of error handling or validation (10) | State what fails, how it shows and what to do |

### Known conflicts between the tool and the registry

- **`version`.** The tool expects a top-level `version` (5 points). The specification allows only six top-level keys and a seventh breaks packaging (`docs/okf-conventions.md`), so the registry does not add it: every skill loses these 5 points.
- **`metadata.author` and `metadata.tags`** (5 each). They can be added under `metadata`; the registry has not decided whether to (it uses `owner_role` and `okf.tags`). Until it does, every skill loses these 10 points. The score differences between skills come from the other findings.
- **Frontmatter text with angle brackets** is read as an XML tag and flagged as a possible prompt injection (the one HIGH finding of the first run was a `<domain>` hint). Write `[domain]`.

### After the run

Commit `docs/new-state/skill-quality.json` and the regenerated `docs/skill-quality.md`. The validator notes a skill that changed after its rating run; rerun the tool for it.
