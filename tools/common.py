#!/usr/bin/env python3
"""Shared constants and small HTML helpers used by the content modules."""
import os

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://guvercin.email"

REPO = "https://github.com/guvercin-email/guvercin-desktop"
RELEASES = REPO + "/releases"
PRERELEASES = REPO + "/releases"
ISSUES = REPO + "/issues"
DISCUSSIONS = REPO + "/discussions"
LICENSE_FILE = REPO + "/blob/main/LICENSE"
README = REPO + "#readme"
LOCALES = REPO + "/tree/main/frontend/src/locales"
CONTRIB = REPO + "/blob/main/README.md"

# The release the download page describes. Kept here rather than written into
# the page bodies so a new version is one edit, not a hunt through two
# languages. DMG_MB is the universal macOS build — the arch that is fused from
# two slices and therefore the largest of the three downloads.
VERSION = "0.1.0"
RELEASE_DATE = {"en": "29 July 2026", "tr": "29 Temmuz 2026"}
DMG_MB = 24  # guvercin_0.1.0_universal.dmg, 25,588,042 bytes

def shot(name, alt, eager=False, cls="frame"):
    load = "eager" if eager else "lazy"
    fetch = ' fetchpriority="high"' if eager else ""
    return (
        f'<div class="{cls}"><img src="assets/img/{name}" width="1600" height="1000" '
        f'alt="{alt}" loading="{load}" decoding="async"{fetch}></div>'
    )


def icon(paths):
    return (
        '<svg class="card__icon" width="40" height="40" viewBox="0 0 40 40" fill="none" '
        'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" '
        'aria-hidden="true">' + paths + "</svg>"
    )


IC_STACK = icon('<path d="M5 13.5 20 6l15 7.5-15 7.5Z"/><path d="M5 20.5 20 28l15-7.5"/>'
                '<path d="M5 27.5 20 35l15-7.5"/>')
IC_CAL = icon('<rect x="5.5" y="8.5" width="29" height="26" rx="4"/><path d="M5.5 16h29"/>'
              '<path d="M13 5v7M27 5v7"/><path d="M12 23h4M18 23h4M24 23h4M12 29h4M18 29h4"/>')
IC_LOCK = icon('<rect x="8.5" y="17.5" width="23" height="16" rx="4"/>'
               '<path d="M14 17.5v-4a6 6 0 0 1 12 0v4"/><path d="M20 24v3"/>')
IC_HEART = icon('<path d="M20 33S6.5 25.4 6.5 16.4A6.9 6.9 0 0 1 20 13a6.9 6.9 0 0 1 13.5 3.4'
                'C33.5 25.4 20 33 20 33Z"/>')
IC_MAIL = icon('<rect x="4.5" y="9.5" width="31" height="21" rx="4"/><path d="m5.5 12 14.5 10 14.5-10"/>')
IC_BUG = icon('<rect x="12.5" y="12.5" width="15" height="19" rx="7.5"/>'
              '<path d="M12.5 20H5M35 20h-7.5M13 14l-5-4M27 14l5-4M13 29l-5 4M27 29l5 4"/>')
IC_CODE = icon('<path d="m14 13-8 7 8 7M26 13l8 7-8 7"/><path d="m22.5 8-5 24"/>')




TRY = "https://try.guvercin.email"

# The 64 interface languages the desktop app ships with, as endonyms.
# The website itself exists in the two marked WEB_LANGS below; the rest are
# listed so a visitor can see the real count, and are shown as app-only.
LANGUAGES = [
    ("ar", "العربية"), ("ar-BH", "العربية (البحرين)"), ("ar-PS", "العربية (فلسطين)"),
    ("az", "Azərbaycanca"), ("bg", "Български"), ("bn", "বাংলা"), ("bs", "Bosanski"),
    ("ca", "Català"), ("cs", "Čeština"), ("da", "Dansk"), ("de", "Deutsch"),
    ("el", "Ελληνικά"), ("en", "English"), ("es", "Español"), ("et", "Eesti"),
    ("fa", "فارسی"), ("fi", "Suomi"), ("fil", "Filipino"), ("fr", "Français"),
    ("hi", "हिन्दी"), ("hr", "Hrvatski"), ("hu", "Magyar"), ("hy", "Հայերեն"),
    ("id", "Bahasa Indonesia"), ("is", "Íslenska"), ("it", "Italiano"), ("ja", "日本語"),
    ("ka", "ქართული"), ("kk", "Қазақша"), ("ko", "한국어"), ("ky", "Кыргызча"),
    ("lo", "ລາວ"), ("lt", "Lietuvių"), ("lv", "Latviešu"), ("mk", "Македонски"),
    ("mn", "Монгол"), ("ms", "Bahasa Melayu"), ("my", "မြန်မာ"), ("ne", "नेपाली"),
    ("nl", "Nederlands"), ("no", "Norsk"), ("pa", "ਪੰਜਾਬੀ"), ("pl", "Polski"),
    ("ps", "پښتو"), ("pt", "Português"), ("ro", "Română"), ("ru", "Русский"),
    ("si", "සිංහල"), ("sk", "Slovenčina"), ("sl", "Slovenščina"), ("so", "Soomaali"),
    ("sq", "Shqip"), ("sq-XK", "Shqip (Kosovë)"), ("sr", "Српски"), ("sv", "Svenska"),
    ("sw", "Kiswahili"), ("th", "ไทย"), ("tk", "Türkmençe"), ("tr", "Türkçe"),
    ("uk", "Українська"), ("ur", "اردو"), ("uz", "Oʻzbekcha"), ("vi", "Tiếng Việt"),
    ("zh", "中文"),
]

# Languages the website itself is translated into: code -> directory prefix.
WEB_LANGS = {"en": "", "tr": "tr/"}

assert len(LANGUAGES) == 64, len(LANGUAGES)
