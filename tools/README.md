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
| `capture_shots.mjs` | drives `try.guvercin.email` and photographs each screen, in both themes |
| `shots_to_webp.py` | turns those PNGs into the WebP files `assets/img/` serves |

Building the pages is plain Python 3 with no dependencies:

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

These are photographs of the running app, not drawings. `capture_shots.mjs`
opens `try.guvercin.email` — the real interface over an in-memory backend — and
shoots each screen at 1600×1000 @2x. The data in them is invented; the pixels
are not.

```bash
npm i -D playwright
node tools/capture_shots.mjs light
node tools/capture_shots.mjs dark
python3 tools/shots_to_webp.py     # needs pillow
```

Every shot exists in both themes, and CSS shows whichever matches the page —
see `shot()` in `common.py`. A `display:none` image is never fetched, so the
theme you are not looking at costs nothing, except on the hero, which is in the
viewport and loads either way.

Two things the script has to work around, both worth knowing if a screen ever
comes out wrong: seeding the demo account rewrites the stored theme, so the
theme is applied *after* load rather than before; and the workspace tabs live
inside `/dashboard` rather than on routes of their own, so they need a click.

If you would rather hand-edit the HTML from now on, delete this folder — the
site does not depend on it.
