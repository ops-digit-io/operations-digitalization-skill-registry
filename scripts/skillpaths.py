"""Where the skills live: two libraries side by side (stdlib, no side effects).

  skills/            core library: the skills drawn on the process flow (docs/new-state/process.yaml `skills` fields and OD_NewState_Flow.mermaid)
  skills-extension/  extension library: every other skill; optional add-ons that deepen a step or cover a neighbouring process

registry.yaml carries `library: core|extension` per skill; validate_registry.py checks that it matches the folder.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIBRARIES = {"core": ROOT / "skills", "extension": ROOT / "skills-extension"}


def all_ids():
    return sorted(p.name for d in LIBRARIES.values() if d.is_dir() for p in d.iterdir() if p.is_dir())


def library_of(name):
    for lib, d in LIBRARIES.items():
        if (d / name).is_dir():
            return lib
    raise KeyError(name)


def skill_dir(name):
    return LIBRARIES[library_of(name)] / name


def folder_of(name):
    """Repository-relative folder of the library holding the skill: 'skills' or 'skills-extension'."""
    return LIBRARIES[library_of(name)].name
