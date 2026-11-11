#!/usr/bin/env python3
"""Keep the OpenSpec copy inside skills/it-demand-package identical to the pinned OpenSpec release.

    python3 scripts/sync_openspec_vendor.py --from <OpenSpec checkout at the pinned tag>           # copy + rewrite VENDORED.md
    python3 scripts/sync_openspec_vendor.py --check --from <OpenSpec checkout at the pinned tag>   # fail on any drift

The copy is OpenSpec's own agent skills (skills/), the workflow schema they follow (schemas/spec-driven/), the
documentation they and the store guide point to (docs/), README.md and LICENSE (MIT), byte for byte apart from line
endings. The release is OPENSPEC_PINNED in skills/it-demand-package/scripts/check_handover.py; check out the matching
tag first: git clone --depth 1 --branch v<pin> https://github.com/Fission-AI/OpenSpec.
"""
from __future__ import annotations

import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "it-demand-package"
DEST = SKILL / "references" / "openspec"
MANIFEST = DEST / "VENDORED.md"
SETS = ["skills", "schemas/spec-driven", "docs", "README.md", "LICENSE"]


def pinned() -> str:
    text = (SKILL / "scripts" / "check_handover.py").read_text(encoding="utf-8")
    return re.search(r'OPENSPEC_PINNED = "([^"]+)"', text).group(1)


def files_of(base: pathlib.Path) -> list[str]:
    out: list[str] = []
    for s in SETS:
        p = base / s
        if p.is_file():
            out.append(s)
        elif p.is_dir():
            out += [f.relative_to(base).as_posix() for f in sorted(p.rglob("*")) if f.is_file()]
    return sorted(out)


def norm(b: bytes) -> bytes:
    return b.replace(b"\r\n", b"\n")


def commit_of(src: pathlib.Path) -> str:
    r = subprocess.run(["git", "-C", str(src), "rev-parse", "HEAD"], capture_output=True, text=True)
    return r.stdout.strip() or "unknown"


def manifest(files: list[str], commit: str) -> str:
    rows = "\n".join(f"| [`{f}`]({f}) |" for f in files)
    return f"""---
type: Skill Reference
title: Vendored
description: OpenSpec {pinned()} as shipped by its authors - the agent skills, the spec-driven schema, the documentation, README and license - kept inside this skill unchanged.
resource: ../../SKILL.md
status: stable
tags: [openspec, vendored]
---
# Vendored: OpenSpec {pinned()}

Copied unchanged from github.com/Fission-AI/OpenSpec, tag `v{pinned()}`, commit `{commit}`, under the MIT license in
[`LICENSE`](LICENSE). Do not edit these files: refresh them with `python3 scripts/sync_openspec_vendor.py --from
<checkout>` after moving `OPENSPEC_PINNED`; CI fails when they drift from the tag. Links inside the copied files that
point outside this set (for example to OpenSpec's own `openspec/` folder) refer to the upstream repository at the same
tag.

The skills under `skills/` are the ones `openspec init` installs for an agent; this skill follows them for every
OpenSpec step and adds only what OD needs (inputs, annex, attachments, check). They need the OpenSpec CLI.

| File |
|---|
{rows}
"""


def main(argv: list[str]) -> int:
    if "--from" not in argv:
        sys.exit(__doc__)
    src = pathlib.Path(argv[argv.index("--from") + 1]).resolve()
    want = files_of(src)
    if not want:
        sys.exit(f"{src} does not look like an OpenSpec checkout")
    commit = commit_of(src)
    if "--check" in argv:
        have = [f for f in files_of(DEST)]
        problems = [f"missing: {f}" for f in sorted(set(want) - set(have))]
        problems += [f"not in OpenSpec {pinned()}: {f}" for f in sorted(set(have) - set(want))]
        problems += [f"differs from OpenSpec {pinned()}: {f}" for f in sorted(set(want) & set(have))
                     if norm((src / f).read_bytes()) != norm((DEST / f).read_bytes())]
        if not MANIFEST.is_file() or norm(MANIFEST.read_bytes()) != manifest(want, commit).encode("utf-8"):
            problems.append("VENDORED.md is stale (rerun with --from)")
        if problems:
            print(f"FAIL - the OpenSpec copy drifted from v{pinned()}:", *problems, sep="\n  ", file=sys.stderr)
            return 1
        print(f"OK - the OpenSpec copy equals v{pinned()} ({len(want)} files, commit {commit[:7]})")
        return 0
    for s in SETS:
        p = DEST / s
        if p.is_dir():
            shutil.rmtree(p)
        elif p.is_file():
            p.unlink()
    for f in want:
        (DEST / f).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src / f, DEST / f)
    MANIFEST.write_text(manifest(want, commit), encoding="utf-8", newline="\n")
    print(f"copied {len(want)} files from OpenSpec v{pinned()} ({commit[:7]}) and wrote {MANIFEST.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
