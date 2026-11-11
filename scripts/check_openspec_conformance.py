#!/usr/bin/env python3
"""Prove that the IT handover (skills/deploy-it-demand) follows OpenSpec, without users needing OpenSpec's CLI.

    python3 scripts/check_openspec_conformance.py [--require]

Users draft handovers with skills only (Claude Cowork): scripts/openspec_offline.py answers `openspec new change`,
`openspec instructions` and `openspec status` from the OpenSpec copy in the skill, and scripts/check_handover.py
validates offline. This check runs the real CLI of the pinned release (OPENSPEC_PINNED in check_handover.py) next to
them and fails when they disagree:
  1. new: the change the offline helper creates equals the CLI's (.openspec.yaml);
  2. instructions and status: the same instruction, template, context, rules, dependencies, unlocks and artifact
     states as the CLI, on an empty change and on the worked example;
  3. validation: the worked example passes both; every broken variant that `openspec validate --strict` rejects is
     also rejected by the offline check (it may be stricter, never looser);
  4. the OD part: new_handover.py adds the annex and attachments/ to a change.
Without the CLI the check is skipped with a note, unless --require is given (CI does).
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "deploy-it-demand"
CHECK = SKILL / "scripts" / "check_handover.py"
NEW = SKILL / "scripts" / "new_handover.py"
OFFLINE = SKILL / "scripts" / "openspec_offline.py"
EXAMPLE = SKILL / "assets" / "example" / "openspec" / "changes"
CONFIG = SKILL / "assets" / "openspec" / "config.yaml.tmpl"
ENV = {**os.environ, "OPENSPEC_TELEMETRY": "0", "NO_COLOR": "1", "PYTHONIOENCODING": "utf-8"}
# the offline check must decide on its own: no CLI reachable
ENV_OFFLINE = {k: v for k, v in ENV.items() if k != "OPENSPEC_BIN"}
ENV_OFFLINE["PATH"] = os.pathsep.join(p for p in os.environ.get("PATH", "").split(os.pathsep)
                                      if not (pathlib.Path(p) / "openspec").exists()
                                      and not (pathlib.Path(p) / "openspec.cmd").exists())
ARTIFACTS = ["proposal", "specs", "design", "tasks"]
FIELDS = ["instruction", "template", "context", "rules", "outputPath", "unlocks", "description"]


def pinned() -> str:
    return re.search(r'OPENSPEC_PINNED = "([^"]+)"', CHECK.read_text(encoding="utf-8")).group(1)


def run(cmd: list[str], cwd: pathlib.Path, env: dict | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=env or ENV, timeout=180)


def example_project(dest: pathlib.Path) -> pathlib.Path:
    shutil.copytree(EXAMPLE, dest / "openspec" / "changes")
    for f in (dest / "openspec").rglob("*.example"):
        f.rename(f.with_suffix(""))
    shutil.copy(CONFIG, dest / "openspec" / "config.yaml")
    (dest / "openspec" / "specs").mkdir(exist_ok=True)
    return next((dest / "openspec" / "changes").iterdir())


def edit(path: pathlib.Path, old: str, new: str) -> None:
    t = path.read_text(encoding="utf-8")
    assert old in t, (path.name, old[:40])
    path.write_text(t.replace(old, new, 1), encoding="utf-8")


def broken_variants() -> dict:
    """Name -> function that breaks a copy of the worked example in one way."""
    spec = "specs/downtime-reason-capture/spec.md"

    def first_req_text(ch):
        t = (ch / spec).read_text(encoding="utf-8")
        return re.search(r"^### Requirement:.*\n(.+)$", t, re.M).group(1)

    return {
        "why too short": lambda ch: edit(ch / "proposal.md", "## Why\n", "## Why\n\nShort.\n\n## Was\n"),
        "no delta specs": lambda ch: shutil.rmtree(ch / "specs"),
        "scenario with three hashes": lambda ch: edit(ch / spec, "#### Scenario:", "### Scenario:"),
        "no SHALL or MUST": lambda ch: edit(ch / spec, first_req_text(ch), "The system records it."),
        "requirement over 500 chars": lambda ch: edit(ch / spec, first_req_text(ch), "The system SHALL " + "record it " * 60 + "."),
        "scenario without THEN": lambda ch: edit(ch / spec, "**THEN**", "**AND**"),
        "duplicate task id": lambda ch: edit(ch / "tasks.md", "- [ ] 1.2", "- [ ] 1.1"),
        "task in wrong group": lambda ch: edit(ch / "tasks.md", "- [ ] 2.1", "- [ ] 1.9"),
        "spec at specs root": lambda ch: shutil.copy(ch / spec, ch / "specs" / "spec.md"),
        "requirement outside delta section": lambda ch: edit(ch / spec, "## ADDED Requirements", "## Requirements"),
    }


def main() -> int:
    cli = os.environ.get("OPENSPEC_BIN") or shutil.which("openspec")
    if not cli:
        if "--require" in sys.argv:
            print("FAIL: OpenSpec CLI not found (npm install -g @fission-ai/openspec@%s)" % pinned(), file=sys.stderr)
            return 1
        print("note: OpenSpec CLI not found; handover conformance not checked here (CI checks it)")
        return 0
    problems: list[str] = []
    ver = run([cli, "--version"], ROOT).stdout.strip()
    if ver != pinned():
        problems.append(f"OpenSpec CLI is {ver}, the skill follows {pinned()}")
    py = sys.executable
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = pathlib.Path(tmp)

        # 1. new change: offline helper and CLI create the same .openspec.yaml
        a, b = tmp_path / "cli-store", tmp_path / "offline-store"
        (a / "openspec").mkdir(parents=True)
        b.mkdir()
        run([cli, "new", "change", "add-x"], a)
        r = run([py, str(OFFLINE), "new", str(b), "add-x"], tmp_path)
        ca, cb = a / "openspec/changes/add-x/.openspec.yaml", b / "openspec/changes/add-x/.openspec.yaml"
        if r.returncode != 0 or not cb.is_file() or ca.read_text(encoding="utf-8") != cb.read_text(encoding="utf-8"):
            problems.append("openspec_offline.py new differs from `openspec new change`:\n" + (r.stdout + r.stderr)[-300:])

        # 2. instructions and status, on an empty change and on the worked example
        empty = b / "openspec/changes/add-x"
        shutil.copy(CONFIG, b / "openspec" / "config.yaml")
        ex = example_project(tmp_path / "example")
        for change in (empty, ex):
            home = change.parent.parent.parent
            for art in ARTIFACTS:
                c = json.loads(run([cli, "instructions", art, "--change", change.name, "--json"], home).stdout or "{}")
                o = json.loads(run([py, str(OFFLINE), "instructions", str(change), art], tmp_path).stdout or "{}")
                for k in FIELDS:
                    if c.get(k) != o.get(k):
                        problems.append(f"instructions {art} ({change.name}): '{k}' differs from the CLI")
                if [(d["id"], d["done"]) for d in c.get("dependencies", [])] != [(d["id"], d["done"]) for d in o.get("dependencies", [])]:
                    problems.append(f"instructions {art} ({change.name}): dependencies differ from the CLI")
            c = json.loads(run([cli, "status", "--change", change.name, "--json"], home).stdout or "{}")
            o = json.loads(run([py, str(OFFLINE), "status", str(change)], tmp_path).stdout or "{}")
            if [(x["id"], x["status"]) for x in c.get("artifacts", [])] != [(x["id"], x["status"]) for x in o.get("artifacts", [])] \
                    or c.get("applyRequires") != o.get("applyRequires"):
                problems.append(f"status ({change.name}): artifact states differ from the CLI")

        # 3. validation: the example passes both; offline never passes what OpenSpec --strict rejects
        r = run([py, str(CHECK), str(ex)], tmp_path, ENV_OFFLINE)
        if r.returncode != 0:
            problems.append("worked example fails the offline check:\n" + r.stdout[-600:])
        r = run([py, str(CHECK), str(ex), "--require-cli"], tmp_path)
        if r.returncode != 0:
            problems.append("worked example fails with the CLI:\n" + r.stdout[-600:])
        rejected_by_cli = 0
        for name, breaker in broken_variants().items():
            ch = example_project(tmp_path / ("v-" + re.sub(r"\W+", "-", name)))
            breaker(ch)
            cli_ok = run([cli, "validate", ch.name, "--type", "change", "--strict", "--no-interactive"],
                         ch.parent.parent.parent).returncode == 0
            off_ok = run([py, str(CHECK), str(ch)], tmp_path, ENV_OFFLINE).returncode == 0
            rejected_by_cli += not cli_ok
            if off_ok and not cli_ok:
                problems.append(f"variant '{name}': OpenSpec --strict rejects it, the offline check lets it pass")
        if rejected_by_cli < len(broken_variants()) - 1:
            problems.append(f"only {rejected_by_cli} of {len(broken_variants())} broken variants are rejected by the CLI: the corpus no longer tests anything")

        # 4. the OD part on a change
        r = run([py, str(NEW), str(empty), "--with-config"], tmp_path)
        if r.returncode != 0 or not (empty / "handover.md").is_file() or not (empty / "attachments").is_dir():
            problems.append("new_handover.py did not add the annex and attachments/:\n" + (r.stdout + r.stderr)[-300:])

    if problems:
        print(f"FAIL — {len(problems)} problem(s):\n", file=sys.stderr)
        for p in problems:
            print("  - " + p, file=sys.stderr)
        return 1
    print(f"OK — skills-only drafting matches OpenSpec {ver}: new, instructions and status equal the CLI; the offline "
          f"check passes the example and rejects every broken variant the CLI rejects ({rejected_by_cli}); OD part added")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
