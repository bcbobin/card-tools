# D&D 2024 Spell Card Generator

A free web tool for generating printable spell cards for the 2024 D&D rules revision.

**[Use it now](https://spell-cards.pages.dev/)**

## Features

- **339 D&D SRD 5.2 spells** included out of the box, covering all levels and most classes
- **Filter** by class, spell level, school of magic, or source book
- **Color-coding modes**: By School, By Spell Level, By Class (highlight mode), or Monochrome — with customizable class color palette
- **Multi-card splitting** for long spell descriptions instead of truncating
- **8 card sizes**: Poker, Bridge, Tarot, A7, Small Index, Large Index, plus Tall and Wide maximized layouts
- **Adjustable font sizes** for readability vs. content density
- **Card backs** for duplex printing — with ornament picker, 20 Google Fonts, custom text, and live preview
- **Print-optimized** layout with cut guides, tight margins, and correct cards-per-page for every size
- **Share spell lists** via URL, clipboard text, or JSON export/import
- **Save & load** spell lists in your browser
- **Create custom spells** directly in the browser with Markdown formatting support
- **Load all official spell sources** — core books and supplements, without playtest material

## Running locally

Serve the project directory over HTTP, then open the local URL in your browser:

```bash
python3 -m http.server 8000
```

Open <http://localhost:8000/>. Opening `index.html` directly may display the interface, but the browser will block loading the bundled spell data.

## Custom Spell Data

The site ships with spells from the [D&D SRD 5.2.1](https://www.dndbeyond.com/srd), licensed under CC-BY-4.0. Its 5etools importer loads every official core and supplemental source in the upstream spell index—including future releases—excludes playtest material, and prefers current-rule versions when spell names overlap. You can also generate this list with the included [scraper tools](scraper/).

## Planned Features

- Import from more sources (homebrew wiki, Homebrewery pages, D&D Beyond)

## Contributing

Issues and pull requests are welcome!

## License

- **Spell data**: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) (Wizards of the Coast, via the D&D SRD 5.2)
- **Code**: [MIT](https://opensource.org/licenses/MIT)

## Support

If you find this useful, consider [buying me a coffee](https://ko-fi.com/mugasofer).
