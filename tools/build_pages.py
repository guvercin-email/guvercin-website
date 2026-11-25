#!/usr/bin/env python3
"""Generate the static guvercin.email site.

The header, the closing CTA band and the footer live here once, which is why
they are identical markup on every page. Page bodies come from content_en.py
and content_tr.py. English is written to the site root, Turkish to /tr/.

    python3 tools/build_pages.py

The output is plain static HTML; the deployed site has no build step.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from common import (  # noqa: E402
    OUT, SITE, REPO, RELEASES, ISSUES, TRY, LANGUAGES, WEB_LANGS,
)
import content_en  # noqa: E402
import content_tr  # noqa: E402

CONTENT = [content_en, content_tr]


# --------------------------------------------------------------------- head --
def head(mod, page, title, desc, extra=""):
    """<head> for one page. `up` walks back out of a language directory."""
    up = "../" if mod.DIR else ""
    slug = "" if page == "index.html" else page
    canonical = SITE + "/" + mod.DIR + slug
    alts = "\n".join(
        '<link rel="alternate" hreflang="%s" href="%s/%s%s">'
        % (code, SITE, WEB_LANGS[code], slug)
        for code in ("en", "tr")
    )
    return f"""<!doctype html>
<html lang="{mod.LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
{alts}
<link rel="alternate" hreflang="x-default" href="{SITE}/{slug}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="guvercin">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{mod.LOCALE}">
<meta property="og:image" content="{SITE}/assets/img/og-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="the guvercin dove mark and the wordmark on a charcoal background">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/img/og-card.png">
<meta name="theme-color" content="#4A4B4B">
<link rel="icon" href="{up}assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{up}assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{up}assets/img/apple-touch-icon.png">
<link rel="manifest" href="{up}site.webmanifest">
<link rel="stylesheet" href="{up}assets/css/style.css">
<!-- Optional Google Analytics 4. Set GA_MEASUREMENT_ID to your G-... ID to enable. -->
<script>
  window.GA_MEASUREMENT_ID = "G-8LWJP0L3E1";
  if (/^G-[A-Z0-9]+$/.test(window.GA_MEASUREMENT_ID)) {{
    var gaScript = document.createElement("script");
    gaScript.async = true;
    gaScript.src = "https://www.googletagmanager.com/gtag/js?id=" + window.GA_MEASUREMENT_ID;
    document.head.appendChild(gaScript);
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag("js", new Date());
    gtag("config", window.GA_MEASUREMENT_ID);
  }}
</script>
<script>
/* Theme and language, settled before first paint so nothing flashes and nobody
   lands in the wrong language. Both are plain preferences, stored locally. */
(function(){{document.documentElement.classList.add("js");try{{var t=localStorage.getItem("guvercin-theme");if(!t){{t=window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light";}}document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}
try{{var here="{mod.LANG}",saved=null;try{{saved=localStorage.getItem("guvercin-lang");}}catch(e2){{}}
var want=saved||((navigator.language||"en").toLowerCase().indexOf("tr")===0?"tr":"en");
if(want!==here&&location.protocol.indexOf("http")===0){{location.replace(want==="tr"?"{SITE}/tr/{slug}":"{SITE}/{slug}");}}}}catch(e3){{}}}})();
</script>
{extra}</head>
<body>
"""


# ------------------------------------------------------------------ header --
GITHUB_ICON = (
    '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 '
    '6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0'
    'C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7'
    'A3.37 3.37 0 0 0 9 18.13V22"/></svg>'
)
SUN_ICON = (
    '<svg class="icon-sun" width="22" height="22" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true">'
    '<circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M4.2 4.2l1.6 1.6'
    'M18.2 18.2l1.6 1.6M2.5 12h2.2M19.3 12h2.2M4.2 19.8l1.6-1.6M18.2 5.8l1.6-1.6"/></svg>'
)
MOON_ICON = (
    '<svg class="icon-moon" width="22" height="22" viewBox="0 0 24 24" fill="none" '
    'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" '
    'aria-hidden="true"><path d="M20.5 14.3A8.5 8.5 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z"/></svg>'
)
MENU_ICON = (
    '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.8" stroke-linecap="round" aria-hidden="true">'
    '<path d="M3.5 7h17M3.5 12h17M3.5 17h17"/></svg>'
)


def mark(up):
    return (
        f'<img class="brand__mark--light" src="{up}assets/img/logo-mark-light.svg" width="34" height="32" alt="">'
        f'<img class="brand__mark--dark" src="{up}assets/img/logo-mark-dark.svg" width="34" height="32" alt="">'
    )


def header(mod, active):
    S = mod.S
    up = "../" if mod.DIR else ""
    items, mobile = [], []
    for href, label in S["nav"]:
        cur = ' aria-current="page"' if href == active else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
        mobile.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    mobile.append(f'<li><a href="{TRY}" target="_blank" rel="noopener">{S["try_nav"]}</a></li>')
    mobile.append(f'<li><a href="{REPO}" target="_blank" rel="noopener">GitHub</a></li>')
    return f"""<a class="skip-link" href="#main">{S["skip"]}</a>
<header class="site-header">
  <div class="wrap site-header__inner">
    <a class="brand" href="index.html" aria-label="{S["home_label"]}">{mark(up)}<span>guvercin</span></a>
    <nav class="nav" aria-label="main">
      <ul>{''.join(items)}</ul>
    </nav>
    <div class="header-actions">
      <a class="btn btn--secondary btn--sm try-link" href="{TRY}" target="_blank" rel="noopener">{S["try_nav"]}</a>
      <a class="icon-btn github-link" href="{REPO}" target="_blank" rel="noopener" aria-label="{S["github_label"]}">{GITHUB_ICON}</a>
      <button class="icon-btn theme-toggle" type="button" aria-label="{S["theme_label"]}">{SUN_ICON}{MOON_ICON}</button>
      <button class="icon-btn nav-toggle" type="button" aria-label="{S["menu_label"]}" aria-expanded="false" aria-controls="mobile-menu">{MENU_ICON}</button>
      <a class="btn btn--primary btn--sm" href="download.html">{S["download"]}</a>
    </div>
  </div>
</header>
<div class="mobile-panel" id="mobile-menu" hidden>
  <ul>{''.join(mobile)}</ul>
</div>
"""


# ---------------------------------------------------------------- cta band --
def cta(mod):
    S = mod.S
    return f"""<section class="cta-band on-dark">
  <div class="wrap">
    <h2>{S["cta_h2"]}</h2>
    <p>{S["cta_p"]}</p>
    <div class="btn-row">
      <a class="btn btn--primary btn--lg" href="download.html" data-os-button="long">{S["cta_primary"]}</a>
      <a class="btn btn--secondary btn--lg" href="{REPO}" target="_blank" rel="noopener">{S["cta_secondary"]}</a>
    </div>
    <p class="small"><a href="{TRY}" target="_blank" rel="noopener">{S["cta_try"]}</a></p>
    <p class="small">{S["cta_small"]}</p>
  </div>
</section>
"""


# ----------------------------------------------------------- language picker --
def lang_picker(mod, page):
    """A quiet switcher in the footer.

    English and Turkish are real pages and navigate. The other 62 are the
    languages the desktop app ships with; they are listed so the count is
    visible and honest, and marked as app-only rather than pretending.
    """
    S = mod.S
    slug = "" if page == "index.html" else page
    site_opts, app_opts = [], []
    for code, name in LANGUAGES:
        if code in WEB_LANGS:
            target = "/" + WEB_LANGS[code] + slug
            sel = " selected" if code == mod.LANG else ""
            site_opts.append(f'<option value="{target}" data-lang="{code}"{sel}>{name}</option>')
        else:
            app_opts.append(f'<option value="" disabled>{name}</option>')
    nl = chr(10)
    return f"""    <div class="lang-picker">
      <label for="lang-select">{S["lang_label"]}</label>
      <select id="lang-select" class="lang-select">
        <optgroup label="{S["lang_site"]}">
{nl.join('          ' + o for o in site_opts)}
        </optgroup>
        <optgroup label="{S["lang_app"]} ({len(LANGUAGES)})">
{nl.join('          ' + o for o in app_opts)}
        </optgroup>
      </select>
      <p class="small">{S["lang_note"]}</p>
    </div>
"""


def footer(mod, page):
    S = mod.S
    up = "../" if mod.DIR else ""
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-cols">
      <div>
        <h2>{S["f_product"]}</h2>
        <ul>
          <li><a href="features.html">{S["f_features"]}</a></li>
          <li><a href="download.html">{S["f_download"]}</a></li>
          <li><a href="{TRY}" target="_blank" rel="noopener">{S["f_try"]}</a></li>
          <li><a href="download.html#beta">{S["f_beta"]}</a></li>
          <li><a href="{RELEASES}" target="_blank" rel="noopener">{S["f_changelog"]}</a></li>
        </ul>
      </div>
      <div>
        <h2>{S["f_project"]}</h2>
        <ul>
          <li><a href="{REPO}" target="_blank" rel="noopener">{S["f_github"]}</a></li>
          <li><a href="open-source.html#contribute">{S["f_contribute"]}</a></li>
          <li><a href="open-source.html#roadmap">{S["f_roadmap"]}</a></li>
          <li><a href="license.html">{S["f_license"]}</a></li>
        </ul>
      </div>
      <div>
        <h2>{S["f_support"]}</h2>
        <ul>
          <li><a href="faq.html">{S["f_faq"]}</a></li>
          <li><a href="contact.html">{S["f_contact"]}</a></li>
          <li><a href="{ISSUES}" target="_blank" rel="noopener">{S["f_bug"]}</a></li>
        </ul>
      </div>
      <div>
        <h2>{S["f_legal"]}</h2>
        <ul>
          <li><a href="privacy.html">{S["f_privacy"]}</a></li>
          <li><a href="license.html">{S["f_license"]}</a></li>
        </ul>
      </div>
    </div>
{lang_picker(mod, page)}    <div class="footer-base">
      <img src="{up}assets/img/logo-mark-dark.svg" width="32" height="30" alt="">
      <p>{S["f_tagline"]}</p>
      <p class="copyright">{S["f_copyright"]}</p>
    </div>
  </div>
</footer>
<script src="{up}assets/js/main.js" defer></script>
</body>
</html>
"""


# ------------------------------------------------------------------- build --
def build(mod, page, title, desc, active, body, extra_head="", with_cta=True):
    up = "../" if mod.DIR else ""
    if up:
        body = body.replace('="assets/', '="' + up + "assets/")
    html = head(mod, page, title, desc, extra_head) + header(mod, active) + body
    if with_cta:
        html += cta(mod)
    html += footer(mod, page)
    directory = os.path.join(OUT, mod.DIR) if mod.DIR else OUT
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, page), "w", encoding="utf-8") as f:
        f.write(html)
    n = len(desc)
    flag = "" if 140 <= n <= 160 else "  <-- CHECK"
    print(f"  {mod.DIR}{page:20} desc={n}{flag}")


if __name__ == "__main__":
    for mod in CONTENT:
        print(f"[{mod.LANG}]")
        for page, title, desc, active, body, extra, with_cta in mod.PAGES:
            build(mod, page, title, desc, active, body, extra, with_cta)

    manifest = """{
  "name": "guvercin",
  "short_name": "guvercin",
  "description": "open source email, on your own machine",
  "start_url": "/",
  "display": "browser",
  "background_color": "#FFFFFF",
  "theme_color": "#4A4B4B",
  "icons": [
    { "src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png" },
    { "src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml" }
  ]
}
"""
    open(os.path.join(OUT, "site.webmanifest"), "w").write(manifest)

    slugs = ["", "download.html", "features.html", "open-source.html", "faq.html",
             "contact.html", "privacy.html", "license.html"]
    prio = {"": "1.0", "download.html": "0.9", "features.html": "0.8"}
    entries = []
    for slug in slugs:
        for code in ("en", "tr"):
            loc = f"{SITE}/{WEB_LANGS[code]}{slug}"
            links = "\n".join(
                '    <xhtml:link rel="alternate" hreflang="%s" href="%s/%s%s"/>'
                % (c, SITE, WEB_LANGS[c], slug) for c in ("en", "tr")
            )
            entries.append(
                f"  <url>\n    <loc>{loc}</loc>\n{links}\n"
                f"    <lastmod>2026-07-26</lastmod>\n"
                f"    <priority>{prio.get(slug, '0.6')}</priority>\n  </url>"
            )
    open(os.path.join(OUT, "sitemap.xml"), "w").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(entries) + "\n</urlset>\n"
    )

    open(os.path.join(OUT, "robots.txt"), "w").write(
        "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE
    )
    print("wrote site.webmanifest, sitemap.xml, robots.txt")
