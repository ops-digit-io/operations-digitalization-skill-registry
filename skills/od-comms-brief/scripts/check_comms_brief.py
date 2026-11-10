#!/usr/bin/env python3
"""Check a use-case communications brief before it leaves OD (stdlib, read-only).

    check_comms_brief.py Brief.md

Exit 2 = blockers, 1 = warnings only, 0 = ready. The check looks at the form of the brief
(sources, evidence classes, call to action, approvals, sensitive items); it cannot judge
whether the story is true, which is the plant owner's approval.
"""
import re
import sys

SECTIONS = {
    "message": (r"^#+\s*message", True),
    "audience": (r"^#+\s*audience", True),
    "proof": (r"^#+\s*proof points", True),
    "cta": (r"^#+\s*call to action", True),
    "channels": (r"^#+\s*channels", False),
    "sensitivity": (r"^#+\s*sensitivity", True),
    "approvals": (r"^#+\s*approvals", True),
}
PLACEHOLDER = re.compile(r"⟨[^⟩]*⟩")
CLASSES = re.compile(r"\b(CALCULATION|ESTIMATION|not yet assessed)\b")
FIGURE = re.compile(r"(€\s?\d|\d\s?(?:€|EUR|k€|kEUR)\b|\b\d+(?:[.,]\d+)?\s?%|\b\d+\s?k\b|\b\d{2,}\s+(?:machines?|plants?|lines?|users?|hours?|h)\b)", re.I)
SENSITIVE = re.compile(r"(https?://|\\\\[\w.-]+\\|\b\d{1,3}(?:\.\d{1,3}){3}\b|\bpassword\b|\btoken\b)", re.I)
SUPERLATIVE = re.compile(r"\b(revolution\w*|game[- ]chang\w*|first[- ]ever|best[- ]in[- ]class|world[- ]class|breakthrough)\b", re.I)
PERSON = re.compile(r"\b(?i:built|developed|created|designed|led|driven) by [A-Z][a-z]+ [A-Z][a-z]+\b|\b(?:Mr|Ms|Mrs|Dr)\.? [A-Z][a-z]+")


def split_sections(text):
    lines = text.splitlines()
    heads = []
    for i, line in enumerate(lines):
        if line.lstrip().startswith("#"):
            key = next((k for k, (p, _) in SECTIONS.items() if re.search(p, line.lower())), None)
            heads.append((i, key or f"_other{i}"))
    out = {}
    for n, (i, key) in enumerate(heads):
        end = heads[n + 1][0] if n + 1 < len(heads) else len(lines)
        out[key] = out.get(key, "") + "\n".join(lines[i + 1:end]).strip() + "\n"
    return out


def analyze(text):
    sec = split_sections(text)
    out = []

    def add(sev, check, msg, fix=""):
        out.append((sev, check, msg, fix))

    for key, (_, required) in SECTIONS.items():
        body = sec.get(key, "").strip()
        if key not in sec:
            add("BLOCKER" if required else "WARN", "missing-section", f"Section '{key}' is absent.")
        elif not body:
            add("BLOCKER" if required else "WARN", "empty-section", f"Section '{key}' has no content.")

    # proof points: every row has a source and an evidence class
    rows = [l for l in sec.get("proof", "").splitlines()
            if l.strip().startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", l.strip())]
    body_rows = [r for r in rows[1:]] if rows else []
    if "proof" in sec and not body_rows:
        add("BLOCKER", "no-proof-points", "The proof points table has no rows.",
            "Two to four proof points, each with a class and a source.")
    for r in body_rows:
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        if len(cells) < 3 or not cells[2] or PLACEHOLDER.fullmatch(cells[2]):
            add("BLOCKER", "proof-without-source", f"A proof point has no source: {r.strip()[:80]}")
        if not CLASSES.search(r):
            add("BLOCKER", "proof-without-class", f"A proof point has no evidence class: {r.strip()[:80]}",
                "Use CALCULATION, ESTIMATION or 'not yet assessed'.")
        if len(cells) >= 4 and re.search(r"\bresult\b", cells[3], re.I) and re.search(r"saving|cost|eur|€", r, re.I) \
                and not re.search(r"registered", r, re.I):
            add("BLOCKER", "saving-as-result", f"A saving is worded as a result without a registered project: {r.strip()[:80]}",
                "A saving is a result only with a registered plant savings project and a baseline; otherwise word it as a claim.")

    # a figure anywhere outside the proof table must carry an evidence class on its line
    for n, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("|") or line.lstrip().startswith("#"):
            continue
        if FIGURE.search(line) and not CLASSES.search(line) and not PLACEHOLDER.search(line):
            add("BLOCKER", "figure-without-class", f"Line {n} states a figure with no evidence class: {line.strip()[:80]}")

    for n, line in enumerate(text.splitlines(), 1):
        if SENSITIVE.search(line):
            add("BLOCKER", "sensitive-item", f"Line {n} holds a link, address or credential word: {line.strip()[:80]}",
                "No links to internal systems, host names, addresses or credentials in a story.")
        if PERSON.search(line):
            add("BLOCKER", "named-individual", f"Line {n} names an individual: {line.strip()[:80]}",
                "Use the role and the plant.")
        if SUPERLATIVE.search(line):
            add("WARN", "superlative", f"Line {n} uses a superlative: {line.strip()[:80]}")

    cta = sec.get("cta", "")
    if cta.strip() and (PLACEHOLDER.fullmatch(cta.strip()) or len(cta.split()) < 5):
        add("BLOCKER", "weak-cta", "The call to action is empty or a placeholder.",
            "Say what the reader does next and where.")

    appr = sec.get("approvals", "")
    for role in ("plant owner", "od lead", "internal communications"):
        if appr.strip() and role not in appr.lower():
            add("BLOCKER", "missing-approver", f"The approvals list does not name: {role}.")
    for line in appr.splitlines():
        if re.search(r"\bgiven\b", line, re.I) and not re.search(r"\d{4}-\d{2}-\d{2}", line):
            add("WARN", "approval-without-date", f"An approval is marked given without a date: {line.strip()[:80]}")

    for key in ("message", "audience", "cta"):
        ph = PLACEHOLDER.findall(sec.get(key, ""))
        if ph:
            add("WARN", "placeholder-left", f"Section '{key}' still has {len(ph)} placeholder(s).")
    return out


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    findings = analyze(open(argv[1], encoding="utf-8").read())
    order = {"BLOCKER": 0, "WARN": 1}
    for sev, check, msg, fix in sorted(findings, key=lambda f: order[f[0]]):
        print(f"{'x' if sev == 'BLOCKER' else '!'} {sev:7} {check}\n    {msg}" + (f"\n    -> {fix}" if fix else ""))
    b = sum(1 for f in findings if f[0] == "BLOCKER")
    w = len(findings) - b
    print(f"{b} blocker, {w} warn")
    return 2 if b else (1 if w else 0)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main(sys.argv))
