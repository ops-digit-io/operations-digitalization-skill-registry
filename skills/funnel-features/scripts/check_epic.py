#!/usr/bin/env python3
"""Check an epic-and-stories document before it enters a backlog.

    python3 check_epic.py EPIC.md
    python3 check_epic.py EPIC.md --json

Reads the markdown produced from `assets/epic-and-stories.md` and reports what is missing,
what is still a placeholder, and what has been filled with a sentence that would fit any
epic in the portfolio.

The checks encode this portfolio's measured failure pattern, not a generic agile rulebook.
In the estate's leaf user stories, very few carry an "I want" tag, almost none mention
acceptance criteria, and none carry a "so that" that differs from the generated one. The
structure was never the problem.

Exit code: 2 if any BLOCKER, 1 if any WARN, 0 otherwise.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter

PLACEHOLDER = re.compile(r"⟨[^⟩]*⟩")
SEV = {"BLOCKER": 0, "WARN": 1, "INFO": 2}
ICON = {"BLOCKER": "✗", "WARN": "!", "INFO": "·"}

# The generated benefit clause and its close relatives. A "so that" built only from these
# words says nothing that is not true of every use case ever written.
GENERIC_BENEFIT = re.compile(
    r"\b(transparency|transparent|faster reaction|reaction time|less manual effort|"
    r"manual effort|more efficient|efficiency|better overview|overview|"
    r"improve[ds]?|optimi[sz]ation|optimi[sz]ed?|digitali[sz]ation|visibility|"
    r"insights?|quality|productivity|the process gains|process gains|gains?|"
    r"monitoring|control|save[sd]? time|time saving)\b", re.I)

# Words that carry no meaning on their own; what is left after removing both these and the
# generic benefit words is the part of the reason that is actually about this story.
FILLER = re.compile(
    r"\b(the|a|an|and|or|of|for|to|in|on|at|by|with|we|our|it|is|are|be|get|gets|"
    r"have|has|more|less|better|faster|so|that|this|their|there|can|will|would|"
    r"process|processes|machine|machines|data|plant|team|line|lines)\b", re.I)

# Placeholder roles carried by every generated story.
VAGUE_ROLE = re.compile(
    r"^\s*(the\s+)?(shop[- ]?floor|process team|shop[- ]?floor\s*/\s*process team|"
    r"operations|the team|user|users|management|everyone|we)\s*$", re.I)

BACKGROUND_PROMPTS = {
    "today":   (re.compile(r"\*\*today\b|^\s*today[.:]", re.I | re.M), "what happens today"),
    "moment":  (re.compile(r"moment of use", re.I), "the moment of use"),
    "decision":(re.compile(r"decision it changes|decision this changes", re.I), "the decision it changes"),
    "why":     (re.compile(r"why now", re.I), "why now — the trigger"),
    "notfor":  (re.compile(r"not for|out of scope|scope fence", re.I), "what this is not for"),
}

STORY_HEAD = re.compile(r"^###\s+(US-\S+.*)$", re.M)

# Field labels inside a story. Splitting on this fixed set rather than on "any bold at line
# start" matters: a wrapped Given/When/Then criterion begins its continuation line with
# **Then**, and a looser split truncates the acceptance block right before the part that
# proves it is testable.
FIELD_LABELS = ("background", "signal", "signals", "acceptance criteria", "blocker",
                "blockers", "value", "depends on", "sequencing", "definition of done")
FIELD_HEAD = re.compile(
    r"^\s*\*\*(" + "|".join(re.escape(x) for x in FIELD_LABELS) + r")\.?\*?\*?\.?\*\*",
    re.I | re.M)
GIVEN_WHEN_THEN = re.compile(r"\bgiven\b.*\bwhen\b.*\bthen\b", re.I | re.S)
SHIFT_USE = re.compile(
    r"\b(consecutive shifts?|in a real shift|real shift|without the (old|manual|previous)|"
    r"for \d+ shifts?|during (a|the) shift)\b", re.I)
EXISTS_VERDICT = re.compile(r"\b(yes|no)\b", re.I)
RELIABILITY = re.compile(r"\b(CALCULATION|ESTIMATION|not yet assessed|carried at epic level)\b", re.I)


def add(f, sev, check, message, fix=""):
    f.append({"severity": sev, "check": check, "message": message, "fix": fix})


def section(text: str, pattern: str) -> str:
    """Body of the first heading matching pattern, up to the next heading of same-or-higher level."""
    m = re.search(rf"^(#+)\s*{pattern}.*$", text, re.I | re.M)
    if not m:
        return ""
    level = len(m.group(1))
    rest = text[m.end():]
    nxt = re.search(rf"^#{{1,{level}}}\s", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


def story_fields(body: str) -> dict[str, str]:
    """Map lowercase field label -> its body, splitting only on the known labels."""
    heads = list(FIELD_HEAD.finditer(body))
    out: dict[str, str] = {}
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(body)
        out[h.group(1).lower()] = body[h.end(): end]
    return out


def split_stories(text: str) -> list[tuple[str, str]]:
    heads = list(STORY_HEAD.finditer(text))
    out = []
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        out.append((h.group(1).strip(), text[h.end(): end]))
    return out


def check_statement(body: str, label: str, findings: list, prefix: str) -> None:
    """A statement is 'As X, I/we want Y, so that Z' — check each third carries weight."""
    m = re.search(r"\*\*as\*\*(.+?)\*\*(?:i|we)\s+want\*\*(.+?)\*\*so that\*\*(.+?)(?:\n\n|\Z)",
                  body, re.I | re.S)
    if not m:
        add(findings, "BLOCKER", f"{prefix}-statement",
            f"{label} has no 'As … I/we want … so that …' statement.",
            fix="All three parts are load-bearing; a missing one is what the estate already has.")
        return
    role, want, why = (re.sub(r"\s+", " ", x).strip().strip(",. ") for x in m.groups())
    if PLACEHOLDER.search(role) or not role:
        add(findings, "BLOCKER", f"{prefix}-role", f"{label}: the role is still a placeholder.")
    elif VAGUE_ROLE.match(re.sub(r"[*_]", "", role)):
        add(findings, "BLOCKER", f"{prefix}-role",
            f"{label}: role is '{role}' — the placeholder carried by every generated story.",
            fix="Name the plant role: shift leader, process engineer, maintenance planner.")
    if PLACEHOLDER.search(want) or len(want) < 8:
        add(findings, "BLOCKER", f"{prefix}-want",
            f"{label}: the capability is not stated. most generated stories read '(not tagged)'.")
    if PLACEHOLDER.search(why):
        add(findings, "BLOCKER", f"{prefix}-reason", f"{label}: the reason is still a placeholder.")
    else:
        stripped = FILLER.sub("", GENERIC_BENEFIT.sub("", why))
        if len(re.sub(r"[^\w]", "", stripped)) < 12:
            add(findings, "BLOCKER", f"{prefix}-reason",
                f"{label}: the 'so that' is the generated clause — '{why[:70]}'.",
                fix="It must name a decision or action this story changes. If it would read "
                    "the same on another plant's epic, it says nothing.")


def analyze(path: str) -> list[dict]:
    text = open(path, encoding="utf-8").read()
    findings: list[dict] = []

    left = PLACEHOLDER.findall(text)
    if left:
        add(findings, "BLOCKER", "placeholders",
            f"{len(left)} unfilled placeholder(s) remain, first: ⟨{left[0][:48]}⟩.")

    # --- background -------------------------------------------------------------
    bg = section(text, r"background")
    if not bg.strip():
        add(findings, "BLOCKER", "background-missing",
            "No background section. This is the part that survives the person who asked leaving.",
            fix="The skill map names this step as the one 'currently held by a departing individual'.")
    else:
        missing = [lbl for _, (pat, lbl) in BACKGROUND_PROMPTS.items() if not pat.search(bg)]
        if missing:
            add(findings, "WARN", "background-incomplete",
                "Background does not cover: " + ", ".join(missing) + ".")
        words = len(re.findall(r"\w+", bg))
        if words < 60:
            add(findings, "WARN", "background-thin",
                f"Background is {words} words. It has to let somebody not in the room judge a story.")
        if not re.search(r"\b(\d{1,2}[:.]\d{2}|shift|daily|weekly|per (shift|day|week)|each \w+)\b",
                         bg, re.I):
            add(findings, "INFO", "background-no-rhythm",
                "Background names no frequency or moment (a time, a shift, 'per day').",
                fix="'The shift leader walks the line at 06:00' beats 'data collection is manual'.")

    # --- epic statement ---------------------------------------------------------
    stmt = section(text, r"epic statement")
    if not stmt.strip():
        add(findings, "BLOCKER", "epic-statement-missing", "No epic statement.")
    else:
        check_statement(stmt, "Epic statement", findings, "epic")

    # --- frame ------------------------------------------------------------------
    frame = section(text, r"epic frame")
    if not frame.strip():
        add(findings, "WARN", "frame-missing", "No epic frame table.")
    else:
        if not re.search(r"capability epic", frame, re.I) or not re.search(r"process epic", frame, re.I):
            add(findings, "WARN", "frame-one-axis",
                "Only one of the two epic axes is recorded.",
                fix="334 leaves carry only a capability parent and 291 only a process parent — "
                    "a query on either axis misses half the portfolio. Fill both.")
        if not RELIABILITY.search(frame):
            add(findings, "WARN", "value-unlabelled",
                "The epic value carries no reliability label.",
                fix="CALCULATION, ESTIMATION or 'not yet assessed'. An unlabelled figure reads as fact.")
        if not re.search(r"requirement", frame, re.I):
            add(findings, "WARN", "no-requirement-link",
                "The epic does not link back to its §1–§11 requirement.")

    # --- stories ----------------------------------------------------------------
    stories = split_stories(text)
    if len(stories) == 0:
        add(findings, "BLOCKER", "no-stories", "The epic has no user stories.")
    elif len(stories) == 1:
        add(findings, "BLOCKER", "single-story",
            "The epic has one story. One story is a story, not an epic.",
            fix="Cut by moment and role, or by which signals exist today — see epic-and-user-stories.md.")
    elif len(stories) > 8:
        add(findings, "WARN", "too-many-stories",
            f"{len(stories)} stories. Above about eight this is two epics, or the background "
            "is describing a programme.")

    layer_words = re.compile(r"\b(connect the plc|build the flow|build the dashboard|"
                             r"set up the broker|create the tags?|deploy the)\b", re.I)
    layered = 0
    for title, body in stories:
        short = title.split("·")[0].strip()
        check_statement(body, short, findings, "story")

        fields = story_fields(body)

        if "background" not in fields:
            add(findings, "WARN", "story-no-background",
                f"{short}: no story-level background. The epic's does not substitute for it.")

        acc_body = fields.get("acceptance criteria", "")
        if not acc_body.strip():
            add(findings, "BLOCKER", "story-no-acceptance",
                f"{short}: no acceptance criteria. Almost no use case in the estate has any.")
        else:
            if not GIVEN_WHEN_THEN.search(acc_body):
                add(findings, "WARN", "story-acceptance-prose",
                    f"{short}: acceptance criteria are not in Given/When/Then form.",
                    fix="Prose criteria cannot be failed, which is what makes them useless.")
            if not SHIFT_USE.search(acc_body):
                add(findings, "BLOCKER", "story-no-shift-criterion",
                    f"{short}: no criterion requiring use in a real shift by a named role.",
                    fix="That is the department's own handover rule and the line between "
                        "delivered and accepted.")
            if not re.search(r"\d", acc_body):
                add(findings, "WARN", "story-acceptance-unquantified",
                    f"{short}: no acceptance criterion carries a number.")

        sig_body = fields.get("signals") or fields.get("signal") or ""
        if "|" not in sig_body:
            add(findings, "WARN", "story-no-signals",
                f"{short}: no signal table.",
                fix="If the story genuinely needs no signals, say so explicitly.")
        else:
            rows = [r for r in sig_body.splitlines()
                    if r.strip().startswith("|") and "---" not in r and "Direction" not in r]
            for r in rows:
                cells = [c.strip() for c in r.strip().strip("|").split("|")]
                if len(cells) >= 3 and not EXISTS_VERDICT.search(cells[2]):
                    add(findings, "BLOCKER", "signal-unverified",
                        f"{short}: signal '{cells[0]}' has no existence verdict.",
                        fix="Verify via od-data-availability-check. Assumed signals are the "
                            "most common late failure — machine connectivity is a "
                            "recurring blocker class in the estate.")
                    break

        if "depends on" not in fields and "sequencing" not in fields:
            add(findings, "INFO", "story-no-dependency",
                f"{short}: no 'depends on'. Write 'nothing' if it stands alone.")
        if layer_words.search(body) and not re.search(r"\bso that\b.*\b(shift|engineer|planner|"
                                                      r"technician|leader)\b", body, re.I):
            layered += 1

    if layered >= 2:
        add(findings, "WARN", "layered-stories",
            f"{layered} stories read as technical layers (connect / build / deploy).",
            fix="If they must land in a fixed order and only the last is worth anything, "
                "they are tasks under one story.")

    if not section(text, r"epic acceptance").strip():
        add(findings, "WARN", "no-epic-acceptance",
            "No epic acceptance. Write 'all stories accepted' if that is genuinely true.")

    return findings


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    as_json = "--json" in argv
    if not args:
        print(__doc__)
        return 0
    worst, out = 0, []
    for path in args:
        try:
            findings = analyze(path)
        except Exception as exc:  # noqa: BLE001
            print(f"{path}: could not check — {exc}", file=sys.stderr)
            worst = max(worst, 1)
            continue
        c = Counter(f["severity"] for f in findings)
        worst = max(worst, 2 if c["BLOCKER"] else 1 if c["WARN"] else 0)
        if as_json:
            out.append({"file": path, "findings": findings})
            continue
        print(f"\n=== {path}")
        if not findings:
            print("    ready for the backlog")
        for f in sorted(findings, key=lambda x: SEV[x["severity"]]):
            print(f"  {ICON[f['severity']]} {f['severity']:7s} {f['check']}")
            print(f"      {f['message']}")
            if f["fix"]:
                print(f"      → {f['fix']}")
        print(f"    {c['BLOCKER']} blocker · {c['WARN']} warn · {c['INFO']} info")
    if as_json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    return worst



def _run(argv: list[str]) -> int:
    """Wrap main so piping into `head` or `less` exits quietly instead of tracebacking."""
    try:
        return main(argv)
    except BrokenPipeError:
        try:
            sys.stdout.close()
        except BrokenPipeError:
            pass
        return 0
    except KeyboardInterrupt:
        return 130


if __name__ == "__main__":
    sys.exit(_run(sys.argv))
