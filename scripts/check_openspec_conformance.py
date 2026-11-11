#!/usr/bin/env python3
"""Prove that the IT handover (skills/it-demand-package) follows OpenSpec, using OpenSpec's own CLI.

    python3 scripts/check_openspec_conformance.py [--require]

Builds throw-away OpenSpec projects and runs the real `openspec validate --strict` (the release pinned in
skills/it-demand-package/scripts/check_handover.py, OPENSPEC_PINNED; github.com/Fission-AI/OpenSpec) on:
  1. the worked example, through check_handover.py (OpenSpec plus the OD annex): must be READY;
  2. a package scaffolded by new_handover.py from the templates: OpenSpec must accept its structure;
  3. the worked example with a duplicated task id: OpenSpec must reject it (proves the CLI is really what decides).
Without the CLI (set OPENSPEC_BIN or put `openspec` on PATH) the check is skipped with a note, unless --require is
given (CI does). Standard library only; the CLI needs Node 22.12 or newer: npm install -g @fission-ai/openspec@<pin>.
"""
from __future__ import annotations

import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "it-demand-package"
CHECK = SKILL / "scripts" / "check_handover.py"
NEW = SKILL / "scripts" / "new_handover.py"
EXAMPLE = SKILL / "assets" / "example" / "openspec" / "changes"
CONFIG = SKILL / "assets" / "openspec" / "config.yaml.tmpl"
ENV = {**os.environ, "OPENSPEC_TELEMETRY": "0", "NO_COLOR": "1", "PYTHONIOENCODING": "utf-8"}


def pinned() -> str:
    return re.search(r'OPENSPEC_PINNED = "([^"]+)"', CHECK.read_text(encoding="utf-8")).group(1)


def example_project(dest: pathlib.Path) -> pathlib.Path:
    shutil.copytree(EXAMPLE, dest / "openspec" / "changes")
    for f in (dest / "openspec").rglob("*.example"):
        f.rename(f.with_suffix(""))
    shutil.copy(CONFIG, dest / "openspec" / "config.yaml")
    (dest / "openspec" / "specs").mkdir(exist_ok=True)
    return next((dest / "openspec" / "changes").iterdir())


def run(cmd: list[str], cwd: pathlib.Path) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, env=ENV, timeout=180)


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
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = pathlib.Path(tmp)
        # 1. the worked example, end to end
        change = example_project(tmp_path / "example")
        r = run([sys.executable, str(CHECK), str(change)], tmp_path)
        if r.returncode != 0 or "READY to hand over" not in r.stdout:
            problems.append("worked example is not READY:\n" + (r.stdout + r.stderr)[-800:])
        # 2. the templates, as scaffolded
        proj = tmp_path / "scaffold"
        proj.mkdir()
        r = run([sys.executable, str(NEW), str(proj), "check-openspec-conformance", "--with-config"], tmp_path)
        if r.returncode != 0:
            problems.append("new_handover.py failed:\n" + (r.stdout + r.stderr)[-400:])
        else:
            r = run([cli, "validate", "check-openspec-conformance", "--type", "change", "--strict", "--no-interactive"], proj)
            if r.returncode != 0:
                problems.append("scaffolded templates rejected by openspec validate --strict:\n" + (r.stdout + r.stderr)[-800:])
        # 3. the CLI must be the one that decides: a duplicated task id is rejected by OpenSpec only
        bad = example_project(tmp_path / "bad")
        tasks = bad / "tasks.md"
        tasks.write_text(tasks.read_text(encoding="utf-8").rstrip("\n") + "\n- [ ] 1.1 duplicate id\n", encoding="utf-8")
        r = run([sys.executable, str(CHECK), str(bad)], tmp_path)
        if r.returncode == 0 or "openspec validate --strict rejected" not in r.stdout:
            problems.append("a duplicated task id was not rejected through the OpenSpec CLI")
    if problems:
        print(f"FAIL — {len(problems)} problem(s):\n", file=sys.stderr)
        for p in problems:
            print("  - " + p, file=sys.stderr)
        return 1
    print(f"OK — the IT handover follows OpenSpec {ver} (worked example READY, templates accepted, CLI decides)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
