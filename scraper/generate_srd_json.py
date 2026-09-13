#!/usr/bin/env python3
"""Generate the bundled D&D SRD 5.2 spell list for the website.

Usage:
    python convert_5etools.py --sources XPHB
    python generate_srd_json.py
"""

import json
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "spells_5etools_xphb.json"
OUTPUT_FILE = SCRIPT_DIR.parent / "srd_spells_2024.json"


def generate_srd() -> list[dict]:
    """Generate SRD 5.2 spells from converted 2024 Player's Handbook data."""
    if not INPUT_FILE.exists():
        print(f"ERROR: {INPUT_FILE} not found.")
        print("Run first: python convert_5etools.py --sources XPHB")
        return []

    with INPUT_FILE.open(encoding="utf-8") as file:
        all_spells = json.load(file)

    srd_spells = []
    for spell in all_spells:
        if not spell.get("srd52"):
            continue
        srd_spell = dict(spell)
        srd_spell["source"] = "SRD"
        srd_spell.pop("srd", None)
        srd_spell.pop("srd52", None)
        srd_spells.append(srd_spell)

    srd_spells.sort(key=lambda spell: (spell.get("level", 0), spell.get("name", "")))

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(srd_spells, file, indent=2, ensure_ascii=False)

    print(f"Generated {OUTPUT_FILE.name}: {len(srd_spells)} D&D SRD 5.2 spells")
    return srd_spells


def print_summary(spells: list[dict]) -> None:
    by_level: dict[int, int] = {}
    for spell in spells:
        level = spell.get("level", 0)
        by_level[level] = by_level.get(level, 0) + 1

    print("\nSpells by level:")
    for level in sorted(by_level):
        label = "Cantrips" if level == 0 else f"Level {level}"
        print(f"  {label}: {by_level[level]}")


def main() -> None:
    spells = generate_srd()
    if spells:
        print_summary(spells)


if __name__ == "__main__":
    main()
