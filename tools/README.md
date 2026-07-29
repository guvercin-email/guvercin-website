# tools — optional, not part of the deployed site

The site in the parent directory is plain static HTML and needs no build step.
Deploy it exactly as it is; do not upload this folder.

These scripts are what generated it, kept so the shared chrome and the two
languages stay in step if you regenerate.

| file | what it does |
| --- | --- |
| `common.py` | constants (repo URLs, `try.guvercin.email`, the 64-language table) and small HTML helpers |
| `content_en.py` | every English page body + the English chrome strings |
| `content_tr.py` | every Turkish page body + the Turkish chrome strings |
| `build_pages.py` | wraps the bodies in the shared header, CTA band and footer; writes English to the root and Turkish to `/tr/`, plus `sitemap.xml`, `robots.txt`, `site.webmanifest` |
| `build_screenshots.py` | draws the labelled UI mockups in `assets/img/shot-*.svg` |

Plain Python 3, no dependencies:

```bash
python3 tools/build_pages.py
```

## Adding a language

1. Copy `content_tr.py`, translate the strings and page bodies, set `LANG`,
   `DIR` (e.g. `"de/"`) and `LOCALE` at the top.
2. Add it to `CONTENT` in `build_pages.py` and to `WEB_LANGS` in `common.py`.

The footer picker, the `hreflang` tags, the sitemap and the auto-detect
redirect all read from `WEB_LANGS`, so nothing else needs touching.

## Screenshots

`assets/img/shot-*.svg` are placeholder mockups. Replace them with real
screenshots using the same filenames and the same 1600×1000 aspect ratio and
nothing else needs to change — both languages point at the same files.

`build_screenshots.py` also carries a `TURKISH` string table, unused today. If
localised mockups are ever wanted, add `render(OUT + "/tr", TURKISH)` back to
its `__main__` block and point the Turkish pages at `assets/img/tr/`.

If you would rather hand-edit the HTML from now on, delete this folder — the
site does not depend on it.
