#!/usr/bin/env python3
"""One call of a skill = one run record: a markdown file with the checklist of its outputs.

    python scripts/run_record.py new <skill-id> [--dir runs] [--supersedes <run-id>]   # create the record with its checklist
    python scripts/run_record.py check <record.md> [--run-checks]                      # may this run be closed?
    python scripts/run_record.py open [--dir runs]                                     # list records that are not closed

The checklist comes from the skill's outputs.yaml (scripts/skill_outputs.py): one row per gate item, one row per
`done_when` criterion of every output, one row per automatic check, one row per sign-off. A run may be closed (status `done`)
only when every gate row is met, every criterion row is done with evidence, every check row recorded exit 0 (or, with
--run-checks, exits 0 now) and every sign-off row names the role that signed. A run whose gate is not met is `refused`.
A run waiting for a human is `awaiting-signoff`. The record is the answer: the skill writes its output into the files named
under File, and the record says what was checked.

The record is never overwritten: a new attempt is a new record that names the one it supersedes.
"""
from __future__ import annotations

import datetime as dt
import re
import subprocess
import sys
import uuid
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_output_structure as cos  # noqa: E402
import skill_outputs as so  # noqa: E402
import skillpaths as skp  # noqa: E402

STATUSES = {"open", "done", "refused", "blocked", "awaiting-signoff"}
CLOSED = {"done", "refused", "blocked"}
PLACEHOLDER = re.compile(r"^\s*$|⟨|^(todo|tbd|-|n/a)\s*$", re.I)


def cell(s) -> str:
    return str(s).replace("|", "/").replace("\n", " ").strip()


def new_record(skill: str, supersedes: str = "none") -> tuple[str, str]:
    d = skp.skill_dir(skill)
    data = so.load(d)
    if not data:
        raise SystemExit(f"{skill}: no outputs.yaml, so no checklist")
    now = dt.datetime.now().astimezone().replace(microsecond=0)
    run_id = f"{now:%Y%m%dT%H%M}-{skill}-{uuid.uuid4().hex[:4]}"
    head = {"skill": skill, "skill_version": skp.folder_hash(skill), "run_id": run_id, "started": now.isoformat(),
            "status": "open", "supersedes": supersedes}
    out = ["---", yaml.safe_dump(head, sort_keys=False).strip(), "---", f"# Run record: {skill}", "",
           "## Gate", "", "| Item | Needs | Evidence | Status |", "|---|---|---|---|"]
    for g in data["gate"]:
        out.append(f"| {g['id']} | {cell(g['needs'])} | | open |")
    out += ["", "## Outputs", "", "| Output | File | Criterion | Evidence | Status |", "|---|---|---|---|---|"]
    for o in data["outputs"]:
        for c in o["done_when"]:
            out.append(f"| {o['id']} | | {cell(c)} | | open |")
    out += ["", "## Checks", "", "| Output | Command | Exit | Run at |", "|---|---|---|---|"]
    for o in data["outputs"]:
        if o.get("check"):
            how = o["check"].get("cmd") or f"structure of {o['template']}"
            out.append(f"| {o['id']} | `{cell(how)}` | | |")
    out += ["", "## Sign-offs", "", "| Output | Role | Signed by (role) | Date |", "|---|---|---|---|"]
    for o in data["outputs"]:
        if o.get("signoff"):
            out.append(f"| {o['id']} | {cell(o['signoff'])} | | |")
    out += ["", "## Open items", "", "| Item | Owner (a role) | Needed by |", "|---|---|---|", "| | | |", ""]
    return run_id, "\n".join(out)


def parse(text: str):
    text = text.replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise ValueError("no frontmatter")
    head = yaml.safe_load(m.group(1)) or {}
    sections: dict[str, list[list[str]]] = {}
    cur = None
    for line in text[m.end():].split("\n"):
        if line.startswith("## "):
            cur = line[3:].strip()
            sections[cur] = []
        elif cur and line.strip().startswith("|") and not re.match(r"^\s*\|[-| :]+\|\s*$", line):
            sections[cur].append([c.strip() for c in line.strip().strip("|").split("|")])
    return head, {k: v[1:] for k, v in sections.items()}      # drop each table's header row


def check(path: Path, run_checks: bool = False) -> list[str]:
    errs: list[str] = []
    try:
        head, sec = parse(path.read_text(encoding="utf-8-sig"))
    except ValueError as e:
        return [f"{path.name}: {e}"]
    for k in ("skill", "skill_version", "run_id", "started", "status", "supersedes"):
        if not head.get(k):
            errs.append(f"header: '{k}' is missing")
    skill = head.get("skill")
    if skill not in skp.all_ids():
        return errs + [f"header: '{skill}' is not a skill"]
    status = head.get("status")
    if status not in STATUSES:
        errs.append(f"header: status '{status}' is not one of {sorted(STATUSES)}")
    data = so.load(skp.skill_dir(skill))
    if not data:
        return errs + [f"{skill}: no outputs.yaml"]
    if head.get("skill_version") != skp.folder_hash(skill):
        errs.append("note: the skill changed since this record was created (skill_version differs)")
    errs = [e for e in errs if not e.startswith("note:")] + [e for e in errs if e.startswith("note:")]
    gate_rows = {r[0]: r for r in sec.get("Gate", []) if len(r) >= 4}
    for g in data["gate"]:
        if g["id"] not in gate_rows:
            errs.append(f"gate: row '{g['id']}' is missing")
    unmet = [r[0] for r in gate_rows.values() if r[3] != "met"]
    if status == "refused":
        if not unmet:
            errs.append("status refused, but every gate row is met")
        return [e for e in errs if not e.startswith("note:")] + [e for e in errs if e.startswith("note:")]
    if status in ("done", "awaiting-signoff") and unmet:
        errs.append(f"gate: not met ({', '.join(unmet)}); the run is refused, not done")
    if status == "open":
        errs.append("status is open: the run is not finished (done, refused, blocked or awaiting-signoff)")
    if status not in ("done", "awaiting-signoff"):
        return errs
    for r in gate_rows.values():
        if r[3] == "met" and PLACEHOLDER.search(r[2]):
            errs.append(f"gate: '{r[0]}' is met without evidence")
    rows = [r for r in sec.get("Outputs", []) if len(r) >= 5]
    expected = [(o["id"], c) for o in data["outputs"] for c in o["done_when"]]
    for oid, crit in expected:
        match = [r for r in rows if r[0] == oid and r[2] == cell(crit)]
        if not match:
            errs.append(f"outputs: criterion row for '{oid}' is missing: {crit[:60]}")
            continue
        r = match[0]
        if r[4] != "done":
            errs.append(f"outputs: '{oid}': '{crit[:50]}' is {r[4] or 'open'}")
        elif PLACEHOLDER.search(r[3]):
            errs.append(f"outputs: '{oid}': '{crit[:50]}' is done without evidence")
    for o in data["outputs"]:
        files = {r[1] for r in rows if r[0] == o["id"]}
        if not any(files) or any(PLACEHOLDER.search(f) for f in files):
            errs.append(f"outputs: '{o['id']}' names no output file")
    check_rows = {r[0]: r for r in sec.get("Checks", []) if len(r) >= 4}
    for o in data["outputs"]:
        if not o.get("check"):
            continue
        r = check_rows.get(o["id"])
        if not r or r[2] != "0" or PLACEHOLDER.search(r[3]):
            errs.append(f"checks: '{o['id']}' has no recorded exit 0")
        if run_checks:
            file = next((x[1] for x in rows if x[0] == o["id"] and x[1]), "")
            if o["check"].get("structure"):
                try:
                    fs = cos.findings(Path(file).read_text(encoding="utf-8-sig"), (skp.skill_dir(skill) / o["template"]).read_text(encoding="utf-8-sig"))
                except OSError as e:
                    fs = [f"cannot read {file}: {e}"]
                if fs:
                    errs.append(f"checks: '{o['id']}' structure: {fs[0]}")
            if o["check"].get("cmd"):
                cmd = o["check"]["cmd"].replace("{file}", file)
                res = subprocess.run(cmd, shell=True, cwd=str(skp.skill_dir(skill)), capture_output=True, text=True)
                if res.returncode != 0:
                    errs.append(f"checks: '{o['id']}' exits {res.returncode} now: {(res.stdout + res.stderr).strip()[:120]}")
    sign_rows = {r[0]: r for r in sec.get("Sign-offs", []) if len(r) >= 4}
    pending = []
    for o in data["outputs"]:
        if o.get("signoff"):
            r = sign_rows.get(o["id"])
            if not r or PLACEHOLDER.search(r[2]) or PLACEHOLDER.search(r[3]):
                pending.append(o["id"])
    if pending and status == "done":
        errs.append(f"sign-offs: waiting for a human ({', '.join(pending)}); the status is awaiting-signoff, not done")
    if not pending and status == "awaiting-signoff":
        errs.append("status awaiting-signoff, but every sign-off is done: close the run")
    return errs


def open_records(directory: Path) -> list[str]:
    out = []
    for p in sorted(directory.glob("*.md")):
        try:
            head, _ = parse(p.read_text(encoding="utf-8-sig"))
        except ValueError:
            continue
        if head.get("skill") and head.get("status") not in CLOSED:
            out.append(f"{p.name}: {head.get('status')}")
    return out


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    cmd, rest = argv[0], argv[1:]
    opt = lambda k, d=None: rest[rest.index(k) + 1] if k in rest else d      # noqa: E731
    if cmd == "new":
        skill = rest[0]
        run_id, text = new_record(skill, opt("--supersedes", "none"))
        directory = Path(opt("--dir", "runs"))
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / f"{run_id}.md"
        path.write_text(text, encoding="utf-8", newline="\n")
        print(path)
        return 0
    if cmd == "check":
        errs = check(Path(rest[0]), "--run-checks" in rest)
        hard = [e for e in errs if not e.startswith("note:")]
        for e in errs:
            print(f"- {e}")
        print("CLOSABLE" if not hard else "NOT CLOSABLE")
        return 1 if hard else 0
    if cmd == "open":
        rows = open_records(Path(opt("--dir", "runs")))
        for r in rows:
            print(r)
        return 1 if rows else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
