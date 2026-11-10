---
type: Skill Reference
title: Evaluation design
description: How to test an OD skill beyond its documentation - two or three test cases run with and without the skill, assertions with evidence, a trigger query set with near-misses, and the iteration loop - as the Agent Skills guides prescribe, adapted to OD, with a statement of what has not been run. Open it at step 8.
resource: ../SKILL.md
status: draft
owner: human:jakob.gabriel
tags: [skills, practice, evaluation]
generated: { by: claude-code/1, at: 2026-11-10T00:00:00Z }
---
# Evaluation design

The quality rating (gate 6) measures how a skill is written. It does not show that the skill helps an agent do the task. The Agent Skills project describes two tests for that; this reference adapts them. **No OD skill has been evaluated this way yet**: say so in a skill that has not, and keep it `draft`.

Sources (opened 2026-11-10): Agent Skills, "Evaluating skill output quality" (agentskills.io/skill-creation/evaluating-skills) and "Optimizing skill descriptions" (agentskills.io/skill-creation/optimizing-descriptions). Numbers below are theirs unless marked proposal.

## A. Output quality: with the skill and without it

1. **Write 2 or 3 test cases** to start, stored as `evals/evals.json` with `id`, `prompt`, `expected_output` and optional `files`. Vary the phrasing and the detail; cover at least one edge case; use realistic OD context (a real, masked request, not an invented one).
2. **Run each case twice**, with the skill and without it (or with the previous version), each from a clean context. Record time and tokens.
3. **Add assertions after the first run**, once you see what the output looks like. Good: "the record names an owner role", "the verdict is one of the four allowed words". Weak: "the output is good" (too vague); an exact phrase (too brittle). Style and fit go to human review.
4. **Grade every assertion PASS or FAIL with evidence**; no benefit of the doubt. Use a script for mechanical checks.
5. **Compare**: the pass rate with and without the skill. Assertions that pass in both add nothing and can go; assertions that fail in both need fixing; the ones that pass only with the skill show what the skill adds.
6. **Iterate**: change the skill from what the traces show, rerun in a new iteration, review with a human. Stop when feedback is consistently empty or the improvement stops. Keep the skill lean and explain the why.

Test-case template: [`assets/evals-template.json`](../assets/evals-template.json).

## B. Trigger quality: does the right skill load

1. **About 20 queries**: 8 to 10 that should trigger the skill, 8 to 10 that should not. The should-not queries are near-misses: they share words with the skill but need something else (for an OD skill, a request that belongs to the neighbouring skill).
2. **Run each query about 3 times** with the skill installed and count how often the skill is loaded; a should-trigger query passes above a trigger rate of 0.5, a should-not query passes below it.
3. **Split about 60 percent train and 40 percent validation**, fixed across iterations; change the description from the train failures only; pick the best iteration by the validation rate. About five iterations are usually enough; finish with 5 to 10 fresh queries.

## C. For OD skills (proposal)

- Take should-not queries from the neighbours listed in the skill's `composes` and from its "Not for" boundary.
- Keep eval prompts free of real names and figures (vault rules); mask them as the department record is masked.
- Record the result in the skill's pull request: cases, pass rates with and without, trigger rates, what changed.
