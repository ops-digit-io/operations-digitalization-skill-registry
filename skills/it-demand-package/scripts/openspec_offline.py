#!/usr/bin/env python3
"""OpenSpec without its CLI: the three commands OpenSpec's skills call while drafting a change, answered from the
OpenSpec copy in ../references/openspec/ (schema and templates of the pinned release) and the store's config.yaml.

    python3 openspec_offline.py new <root> <change-id>                 # = openspec new change <change-id>
    python3 openspec_offline.py instructions <change> <artifact-id>    # = openspec instructions <artifact> --change <id> --json
    python3 openspec_offline.py status <change>                        # = openspec status --change <id> --json

<root> holds openspec/ (the OD store); <change> is <root>/openspec/changes/<change-id>. Output is JSON with the fields
OpenSpec's skills read (instruction, template, context, rules, dependencies, unlocks, outputPath, ...; for status the
artifacts with done / ready / blocked and applyRequires). CI compares these answers with the real CLI's for the pinned
release (scripts/check_openspec_conformance.py). Needs PyYAML.
"""
from __future__ import annotations

import datetime
import glob
import json
import pathlib
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

SCHEMA_DIR = pathlib.Path(__file__).resolve().parent.parent / "references" / "openspec" / "schemas" / "spec-driven"
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def schema() -> dict:
    return yaml.safe_load((SCHEMA_DIR / "schema.yaml").read_text(encoding="utf-8"))


def config(change: pathlib.Path) -> dict:
    f = change.parent.parent / "config.yaml"
    if not f.is_file():
        f = change.parent.parent / "config.yml"
    data = yaml.safe_load(f.read_text(encoding="utf-8")) if f.is_file() else None
    return data if isinstance(data, dict) else {}


def outputs(change: pathlib.Path, pattern: str) -> list[str]:
    hits = glob.glob(str(change / pattern), recursive=True)
    return sorted(str(pathlib.Path(h)) for h in hits if pathlib.Path(h).is_file())


def artifact_status(change: pathlib.Path) -> dict[str, str]:
    arts = schema()["artifacts"]
    done = {a["id"] for a in arts if outputs(change, a["generates"])}
    return {a["id"]: "done" if a["id"] in done else ("ready" if set(a.get("requires") or []) <= done else "blocked")
            for a in arts}


def cmd_new(root: pathlib.Path, cid: str) -> dict:
    if not KEBAB.match(cid):
        sys.exit("change id must be kebab-case, e.g. add-downtime-reason-capture")
    change = root / "openspec" / "changes" / cid
    if change.exists():
        sys.exit(f"change '{cid}' already exists at {change}")
    change.mkdir(parents=True)
    (root / "openspec" / "specs").mkdir(exist_ok=True)
    cfg = root / "openspec" / "config.yaml"
    if not cfg.exists() and not (root / "openspec" / "config.yml").exists():
        cfg.write_text("schema: spec-driven\n", encoding="utf-8", newline="\n")
    (change / ".openspec.yaml").write_text(
        f"schema: {schema()['name']}\ncreated: {datetime.date.today().isoformat()}\n", encoding="utf-8", newline="\n")
    return {"changeName": cid, "changeDir": str(change), "schemaName": schema()["name"]}


def cmd_instructions(change: pathlib.Path, artifact: str) -> dict:
    sch = schema()
    arts = {a["id"]: a for a in sch["artifacts"]}
    if artifact not in arts:
        sys.exit(f"unknown artifact '{artifact}'; the schema has {', '.join(arts)}")
    a = arts[artifact]
    cfg = config(change)
    status = artifact_status(change)
    rules = (cfg.get("rules") or {}).get(artifact) or []
    out = {
        "changeName": change.name,
        "artifactId": artifact,
        "schemaName": sch["name"],
        "changeDir": str(change),
        "outputPath": a["generates"],
        "resolvedOutputPath": str(change / a["generates"]),
        "existingOutputPaths": outputs(change, a["generates"]),
        "description": a.get("description", ""),
        "instruction": a.get("instruction", ""),
        "template": (SCHEMA_DIR / "templates" / a["template"]).read_text(encoding="utf-8"),
        "dependencies": [{"id": d, "done": status[d] == "done", "path": arts[d]["generates"],
                          "description": arts[d].get("description", "")} for d in a.get("requires") or []],
        "unlocks": [x["id"] for x in sch["artifacts"] if artifact in (x.get("requires") or [])],
    }
    if isinstance(cfg.get("context"), str) and cfg["context"].strip():
        out["context"] = cfg["context"].strip()   # the CLI trims it
    if rules:
        out["rules"] = [str(r) for r in rules]
    return out


def cmd_status(change: pathlib.Path) -> dict:
    sch = schema()
    status = artifact_status(change)
    apply_requires = (sch.get("apply") or {}).get("requires") or []
    return {
        "changeName": change.name,
        "schemaName": sch["name"],
        "changeRoot": str(change),
        "applyRequires": apply_requires,
        "artifacts": [{"id": a["id"], "outputPath": a["generates"], "status": status[a["id"]],
                       "requires": a.get("requires") or []} for a in sch["artifacts"]],
        "isPlanningComplete": all(s == "done" for s in status.values()),
    }


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[0] not in ("new", "instructions", "status"):
        sys.exit(__doc__)
    if argv[0] == "new" and len(argv) == 3:
        result = cmd_new(pathlib.Path(argv[1]), argv[2])
    elif argv[0] == "instructions" and len(argv) == 3:
        result = cmd_instructions(pathlib.Path(argv[1]), argv[2])
    elif argv[0] == "status" and len(argv) == 2:
        result = cmd_status(pathlib.Path(argv[1]))
    else:
        sys.exit(__doc__)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
