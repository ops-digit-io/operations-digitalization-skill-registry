#!/usr/bin/env python3
"""Stop hook for Claude Code: a session may not end while a run record of a skill call is open (stdlib only).

Claude Code runs a Stop hook when the assistant is about to finish. This script reads the hook input from stdin (JSON with
`cwd` and `stop_hook_active`), looks for run records in <cwd>/runs (or $OD_RUN_DIR) and, if one is still `open`, exits 2 with
a message on stderr: Claude Code then keeps the assistant working and shows it the message. Records that are done, refused,
blocked or awaiting-signoff do not hold the session. `stop_hook_active` is true when the hook already blocked once in this
turn; then the script lets the session end so it cannot loop (the open record stays open and `run_record.py open` lists it).

Enable it by adding to a Claude Code settings file (not done by the registry):

    {"hooks": {"Stop": [{"hooks": [{"type": "command", "command": "python <registry>/scripts/stop_hook.py"}]}]}}

What it enforces: a record exists and has been taken to a closed status. What it does not: that the content is true.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_record as rr  # noqa: E402


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        data = {}
    base = Path(data.get("cwd") or os.getcwd())
    directory = Path(os.environ.get("OD_RUN_DIR") or base / "runs")
    if not directory.is_dir():
        return 0
    open_ = rr.open_records(directory)
    if not open_:
        return 0
    if data.get("stop_hook_active"):
        return 0
    print("Run record not closed. Finish the skill call before you stop:\n  " + "\n  ".join(open_) +
          "\nFill every row with evidence, run the checks, then `python scripts/run_record.py check <record>` must print CLOSABLE "
          "and the status must be done, refused, blocked or awaiting-signoff.", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
