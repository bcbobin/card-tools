# D&D 2024 Spell Scrapers

Tools for downloading official spell data for the [Spell Card Generator](https://github.com/MugaSofer/spell-cards).

The website ships with 339 D&D SRD 5.2 spells, licensed under CC-BY-4.0. Use these tools to generate additional 2024-compatible spell data for personal use.

## Setup

```bash
cd scraper
pip install -r requirements.txt
```

## Sources

### Wikidot (`scrape_spells.py`)

Scrapes the 2024 Wikidot spell database.

```bash
python scrape_spells.py
python scrape_spells.py --reparse  # Reparse cached HTML without network access
```

Output: `spells_2024.json`; cached pages: `raw_html_2024/`.

### 5etools (`convert_5etools.py`)

Imports every official core and supplemental spell source from the [5etools](https://5e.tools) GitHub repository, including `PHB`, `XPHB`, `XGE`, and `TCE`. New official sources enter automatically when 5etools adds them to its spell index. `AU` and `UA*` playtest data are excluded by default. Duplicate names use their current-rule version.

```bash
python convert_5etools.py
python convert_5etools.py --sources XPHB XGE
python convert_5etools.py --list-sources
```

Output: `spells_5etools.json`, or `spells_5etools_<source>.json` for a single source.

## Using with the Spell Card Generator

Use the “Load custom spells.json” button in the web interface to load a generated file.

## Regenerating bundled SRD spells

```bash
python convert_5etools.py --sources XPHB
python generate_srd_json.py  # outputs srd_spells_2024.json to the project root
```
