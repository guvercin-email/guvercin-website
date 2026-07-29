#!/usr/bin/env python3
"""English content for guvercin.email.

Every page body lives here. tools/build_pages.py wraps these in the shared
header, closing CTA band and footer, and writes the files to the site root.
"""
from common import *  # noqa: F401,F403

LANG = "en"
DIR = ""          # English is the site root
LOCALE = "en"

# Strings that appear in the shared chrome.
S = {
    "skip": "skip to content",
    "home_label": "guvercin home",
    "nav": [("features.html", "Features"), ("download.html", "Download"),
            ("open-source.html", "Open Source"), ("faq.html", "FAQ"),
            ("contact.html", "Contact")],
    "github_label": "guvercin on GitHub",
    "theme_label": "switch theme",
    "menu_label": "menu",
    "download": "Download",
    "try_nav": "Try online",
    "cta_h2": "ready to take your inbox back?",
    "cta_p": "free, open source, and it never phones home.",
    "cta_primary": "Download guvercin",
    "cta_secondary": "view on GitHub",
    "cta_try": "or try it in your browser first \u2192",
    "cta_small": "macOS \u00b7 Windows \u00b7 Linux \u2014 version 0.1.0",
    "f_product": "Product", "f_project": "Project", "f_support": "Support",
    "f_legal": "Legal",
    "f_features": "Features", "f_download": "Download", "f_beta": "Beta channel",
    "f_changelog": "Changelog", "f_try": "Try online",
    "f_github": "GitHub", "f_contribute": "Contribute", "f_roadmap": "Roadmap",
    "f_license": "License", "f_faq": "FAQ", "f_contact": "Contact",
    "f_bug": "Report a bug", "f_privacy": "Privacy Policy",
    "f_tagline": "open source email, on your own machine",
    "f_copyright": "\u00a9 2026 guvercin \u2014 open source, made with care.",
    "lang_label": "Language",
    "lang_site": "this website",
    "lang_app": "the app speaks these too",
    "lang_note": "the website is in English and Turkish; the app itself ships 64 languages.",
}

# ============================================================== index.html ==
JSONLD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "guvercin",
  "applicationCategory": "EmailApplication",
  "operatingSystem": "macOS, Windows, Linux",
  "softwareVersion": "0.1.0",
  "description": "a free and open source desktop email client with a calendar, contacts and tasks, storing everything in a local database on your own computer",
  "url": "https://guvercin.email/",
  "downloadUrl": "https://github.com/guvercin-email/guvercin-desktop/releases",
  "license": "https://github.com/guvercin-email/guvercin-desktop/blob/main/LICENSE",
  "sameAs": "https://github.com/guvercin-email/guvercin-desktop",
  "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" }
}
</script>
"""

INDEX = f"""<main id="main">

<section class="hero">
  <div class="wrap center">
    <p class="overline"><span class="pill pill--yellow pill--dot">v0.1.0 · free &amp; open source</span></p>
    <h1>your inbox, on your desktop</h1>
    <p class="lede">a free, open source email client for macOS, Windows and Linux — with a calendar,
      contacts and tasks built in. your mail lives on your machine, not on ours.</p>
    <div class="btn-row">
      <a class="btn btn--primary btn--lg" href="download.html" data-os-button="long">Download free</a>
      <a class="btn btn--secondary btn--lg" href="{TRY}" target="_blank" rel="noopener">try it in your browser</a>
    </div>
    <p class="small">free forever · no account required · no tracking ·
      <a href="{REPO}" target="_blank" rel="noopener">view on GitHub</a></p>
  </div>
  <div class="wrap hero__figure">
    {shot('shot-mail.svg', 'the guvercin mail view: a folder tree on the left, a message list in the middle and the open message on the right', eager=True, cls='frame frame--hero')}
  </div>
</section>

<section class="trust">
  <div class="wrap">
    <ul>
      <li>100% open source</li>
      <li>no ads, no tracking</li>
      <li>works with any IMAP account</li>
      <li>64 languages</li>
      <li>macOS, Windows &amp; Linux</li>
    </ul>
  </div>
</section>

<section class="section section--after-hero">
  <div class="wrap">
    <h2 class="visually-hidden">what you get</h2>
    <div class="grid grid--4">
      <div class="card card--link reveal" data-delay="0">
        {IC_STACK}
        <h3>all your accounts in one place</h3>
        <p>add as many IMAP and SMTP accounts as you like, or sign in to Google with one click.</p>
      </div>
      <div class="card card--link reveal" data-delay="1">
        {IC_CAL}
        <h3>more than mail</h3>
        <p>a calendar, an address book and a task list, in the same window.</p>
      </div>
      <div class="card card--link reveal" data-delay="2">
        {IC_LOCK}
        <h3>private by design</h3>
        <p>messages sit in an encrypted local database on your computer, and nothing is uploaded to us.</p>
      </div>
      <div class="card card--link reveal" data-delay="3">
        {IC_HEART}
        <h3>yours to keep</h3>
        <p>open source, free forever, no subscription and nothing to upgrade.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="wrap center">
    <p class="overline">no install, no account</p>
    <h2>try guvercin before you download it</h2>
    <p class="lede">a live version runs in your browser, so you can click through the mail view,
      the calendar and the settings without putting anything on your disk.</p>
    <div class="btn-row">
      <a class="btn btn--primary btn--lg" href="{TRY}" target="_blank" rel="noopener">open try.guvercin.email</a>
      <a class="btn btn--secondary btn--lg" href="download.html" data-os-button="long">Download guvercin</a>
    </div>
    <p class="small">the desktop app is the real thing — this is just a look around first.</p>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <div class="split">
      <div class="split__media reveal">
        {shot('shot-offline.svg', 'the mail view with an offline notice at the top, still showing messages from the local copy')}
      </div>
      <div class="reveal">
        <h2>email that feels like a desktop app</h2>
        <p>a full folder tree you can reorder, conversation view you can switch off, and a reading
          pane you can move to wherever you actually read. per-account theme and font size are
          remembered, so a work account can look nothing like a personal one.</p>
        <p>search runs against the local database, which means it also runs on a train with no
          signal. so do your attachments and inline images.</p>
        <p><a href="features.html">see all features →</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section section--cream">
  <div class="wrap prose">
    <h2>we cannot read your mail, and neither can anyone else</h2>
    <p>there is no guvercin cloud. the app connects from your computer straight to your own
      provider, and everything it keeps — messages, drafts, attachments, calendar events,
      contacts, tasks — is stored in a local database on your disk. there is no telemetry, no
      crash reporting and no advertising, and no account to create in the first place.</p>
    <p>we have nothing to sell, because we never receive anything.</p>
    <p><a href="privacy.html">read the privacy policy →</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>questions people ask first</h2>
    <div class="accordion">
      <details>
        <summary>is guvercin really free?</summary>
        <div class="answer">
          <p>yes. it is free and open source, with no subscription, no paid tier and nothing to
            upgrade to. the one thing you may not do is sell it.</p>
        </div>
      </details>
      <details>
        <summary>which email providers work?</summary>
        <div class="answer">
          <p>any provider that speaks IMAP and SMTP — Gmail, Outlook and Hotmail, Yandex, iCloud,
            Fastmail, your university, your own server. Google accounts can sign in with a single
            click.</p>
        </div>
      </details>
      <details>
        <summary>where is my mail stored?</summary>
        <div class="answer">
          <p>in a local database on your own computer. nothing reaches our servers, because there
            are no servers.</p>
        </div>
      </details>
    </div>
    <p style="margin-top:24px"><a href="faq.html">see all questions →</a></p>
  </div>
</section>

</main>
"""

# =========================================================== download.html ==
DOWNLOAD = f"""<main id="main">

<section class="section section--cream">
  <div class="wrap center">
    <h1>download guvercin</h1>
    <p class="lede">free and open source. no account, no tracking, no strings.</p>
    <div class="btn-row">
      <a class="btn btn--primary btn--lg" href="{RELEASES}" data-release-link data-os-button="long" target="_blank" rel="noopener">Download guvercin</a>
    </div>
    <p class="small">version {VERSION} · released {RELEASE_DATE[LANG]} · about {DMG_MB} MB · macOS 11 or later</p>
    <p class="small"><a href="#all-downloads">not your system? see all downloads ↓</a></p>
    <p class="small">not ready to install? <a href="{TRY}" target="_blank" rel="noopener">try guvercin online →</a></p>
  </div>
</section>

<section class="section" id="all-downloads">
  <div class="wrap">
    <h2>all downloads</h2>
    <p class="note">every build comes from the same public repository, and every link below points at
      the GitHub releases page.</p>
    <div class="grid grid--3" style="margin-top:32px">

      <div class="card" data-os-card="macos">
        <p class="overline">macOS</p>
        <span data-os-pill></span>
        <h3>macOS 11 or later</h3>
        <p>a disk image you drag into Applications. universal features, two builds — pick the one
          that matches your chip.</p>
        <div class="btn-row" style="flex-direction:column;align-items:stretch;gap:12px">
          <a class="btn btn--primary" href="{RELEASES}" data-release-link target="_blank" rel="noopener">Apple Silicon (.dmg)</a>
          <a class="btn btn--secondary" href="{RELEASES}" data-release-link target="_blank" rel="noopener">Intel (.dmg)</a>
        </div>
        <p class="small" style="margin-top:16px">format: .dmg</p>
      </div>

      <div class="card" data-os-card="windows">
        <p class="overline">Windows</p>
        <span data-os-pill></span>
        <h3>Windows 10 or 11</h3>
        <p>an NSIS installer that puts guvercin in your Start menu and registers it for mailto:
          links if you want it to.</p>
        <div class="btn-row" style="flex-direction:column;align-items:stretch;gap:12px">
          <a class="btn btn--primary" href="{RELEASES}" data-release-link target="_blank" rel="noopener">Installer (.exe)</a>
        </div>
        <p class="small" style="margin-top:16px">format: .exe · Windows may show a SmartScreen
          warning because the installer is not code-signed yet — choose More info → Run anyway.</p>
      </div>

      <div class="card" data-os-card="linux">
        <p class="overline">Linux</p>
        <span data-os-pill></span>
        <h3>64-bit Linux</h3>
        <p>native packages for the two common families. you will need WebKitGTK 4.1 and libsecret,
          which most desktops already ship.</p>
        <div class="btn-row" style="flex-direction:column;align-items:stretch;gap:12px">
          <a class="btn btn--primary" href="{RELEASES}" data-release-link target="_blank" rel="noopener">Debian / Ubuntu (.deb)</a>
          <a class="btn btn--secondary" href="{RELEASES}" data-release-link target="_blank" rel="noopener">Fedora / RHEL (.rpm)</a>
        </div>
        <p class="small" style="margin-top:16px">formats: .deb and .rpm</p>
      </div>

    </div>
  </div>
</section>

<section class="section section--alt" id="beta">
  <div class="wrap">
    <div class="callout">
      <p><span class="pill pill--blue">beta</span></p>
      <h2 style="font-size:28px">beta channel</h2>
      <p>beta builds get new features first and may be unstable. they can also change how data is
        stored, so keep a backup of anything you care about. if something breaks, please tell us on
        GitHub — that is what beta is for.</p>
      <div class="btn-row">
        <a class="btn btn--secondary btn--sm" href="{PRERELEASES}" data-release-link target="_blank" rel="noopener">beta for macOS</a>
        <a class="btn btn--secondary btn--sm" href="{PRERELEASES}" data-release-link target="_blank" rel="noopener">beta for Windows</a>
        <a class="btn btn--secondary btn--sm" href="{PRERELEASES}" data-release-link target="_blank" rel="noopener">beta for Linux</a>
      </div>
      <p style="margin-top:16px"><a href="{PRERELEASES}" target="_blank" rel="noopener">see every pre-release on GitHub →</a></p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2>system requirements</h2>
    <div class="table-wrap">
      <table class="table-stack">
        <thead>
          <tr><th scope="col">platform</th><th scope="col">what you need</th></tr>
        </thead>
        <tbody>
          <tr><td>macOS</td><td>macOS 11 Big Sur or later; Apple Silicon or Intel.</td></tr>
          <tr><td>Windows</td><td>Windows 10 or 11, 64-bit.</td></tr>
          <tr><td>Linux</td><td>a modern 64-bit distribution with WebKitGTK 4.1 and libsecret available.</td></tr>
          <tr><td>all platforms</td><td>roughly 200 MB free disk space plus room for your synced mail; 4 GB RAM; an internet connection for the first sync.</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <h2>installing</h2>
    <div class="grid grid--3" style="margin-top:32px">
      <div class="card">
        <h3>macOS</h3>
        <ol class="steps">
          <li>open the .dmg</li>
          <li>drag guvercin into Applications</li>
          <li>the first time, right-click the app and choose Open, then confirm — the build is not
            notarized yet, so a normal double-click will be blocked.</li>
        </ol>
      </div>
      <div class="card">
        <h3>Windows</h3>
        <ol class="steps">
          <li>run the .exe installer</li>
          <li>if SmartScreen appears, choose More info → Run anyway</li>
          <li>launch guvercin from the Start menu.</li>
        </ol>
      </div>
      <div class="card">
        <h3>Linux</h3>
        <ol class="steps">
          <li>install with <code>sudo dpkg -i guvercin_0.1.0_amd64.deb</code> or
            <code>sudo rpm -i guvercin-0.1.0.x86_64.rpm</code></li>
          <li>if dependencies are missing, run <code>sudo apt -f install</code></li>
          <li>launch guvercin from your application menu.</li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split">
      <div class="split__media reveal">
        {shot('shot-signin.svg', 'the add-an-account dialog with a continue with Google button and detected IMAP and SMTP server settings')}
      </div>
      <div class="reveal">
        <h2>add your account in three steps</h2>
        <ol class="steps">
          <li>choose “continue with Google” or enter your email address</li>
          <li>confirm in your browser, or fill in your IMAP and SMTP details — guvercin will try to
            detect them for you</li>
          <li>wait for the first sync, then your mail is available offline too.</li>
        </ol>
        <p>you can add as many accounts as you like, and each one keeps its own local database.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap prose">
    <h2>build it yourself</h2>
    <p>the source is public, and the app you download is the app you can compile.</p>
    <div class="code">
      <button class="copy-btn" type="button" hidden>copy</button>
      <pre><code>git clone {REPO}.git
cd guvercin-desktop
npm install
npm run app:build</code></pre>
    </div>
    <p class="note">you will need Rust and the Tauri prerequisites for your platform —
      the <a href="{README}" target="_blank" rel="noopener">repository README</a> lists them.</p>
    <p><a href="{RELEASES}" target="_blank" rel="noopener">full changelog →</a></p>
    <p>having trouble? write to <a href="mailto:support@guvercin.email">support@guvercin.email</a> — we read everything.</p>
  </div>
</section>

</main>
"""

# =========================================================== features.html ==
FEATURE_ANCHORS = [
    ("mail", "mail"), ("sign-in", "sign-in"), ("composer", "composer"),
    ("calendar", "calendar"), ("contacts", "contacts"), ("tasks", "tasks"),
    ("offline", "offline"), ("appearance", "appearance"), ("keyboard", "keyboard"),
    ("privacy", "privacy"),
]


def feature(anchor, title, media, paragraphs, bullets=None, flip=False):
    ps = "\n        ".join(f"<p>{p}</p>" for p in paragraphs)
    bl = ""
    if bullets:
        lis = "\n          ".join(f"<li>{b}</li>" for b in bullets)
        bl = f"\n        <ul>\n          {lis}\n        </ul>"
    cls = "split split--flip" if flip else "split"
    return f"""    <div class="{cls} feature-section" id="{anchor}">
      <div class="split__media reveal">
        {media}
      </div>
      <div class="reveal">
        <h2>{title}</h2>
        {ps}{bl}
      </div>
    </div>
"""


FEATURES_BODY = "".join([
    feature("mail", "an inbox that behaves",
            shot("shot-mail.svg", "the mail view with the folder tree, message list and reading pane side by side"),
            ["several IMAP and SMTP accounts side by side, each with its own local database. a full "
             "folder tree you can reorder, custom label ordering, and a choice of how unread counts "
             "appear.",
             "conversation view on or off, an adjustable reading pane, and per-account theme and font "
             "size. search — including a structured advanced search — keeps working when you are "
             "offline."],
            ["open .eml files directly — guvercin registers as a handler for message/rfc822 files",
             "export a message as .eml or raw RFC822",
             "block a sender, with the rule stored locally",
             "print a message"]),
    feature("sign-in", "one click for Google, plain IMAP for everyone else",
            shot("shot-signin.svg", "the add-an-account dialog offering Google sign-in above a manual email and password form"),
            ["“continue with Google” runs an OAuth2 (XOAUTH2) PKCE flow in your system browser, so your "
             "password is never typed into guvercin and no token ever passes through the interface. the "
             "app ships with a working OAuth client, so it works out of the box.",
             "for everything else, guvercin probes your provider’s servers from your address and lets "
             "you override host, port and encryption by hand. it works with Gmail, Outlook and Hotmail, "
             "Yandex, iCloud, Fastmail and self-hosted servers."],
            flip=True),
    feature("composer", "write properly",
            shot("shot-composer.svg", "a popped-out compose window with a formatting ribbon, address fields and two attached files"),
            ["a rich-text WYSIWYG editor with a formatting ribbon, drag &amp; drop attachments, and a "
             "compose window you can pop out into its own native window. drafts save locally and can "
             "be sent later.",
             "right-click any file in your file manager and choose “send with guvercin” to start a "
             "message with it already attached — registered automatically on Windows and Linux. on "
             "macOS, drag the file onto the window or use Open With."]),
    feature("calendar", "your week, in the same window",
            shot("shot-calendar.svg", "a month view of the built-in calendar with several coloured events"),
            ["multiple calendars per account, CalDAV sync against your own server, Google Calendar "
             "sync, and .ics import and export.",
             "it sits beside your mail rather than in another tab, which is the entire point."],
            flip=True),
    feature("contacts", "an address book that is actually yours",
            shot("shot-contacts.svg", "the contacts view with a searchable list and a contact detail panel"),
            ["contact lists and groups, vCard import and export, and Google Contacts sync.",
             "sender avatars are resolved when a message is displayed, and addresses autocomplete "
             "while you write."]),
    feature("tasks", "todos next to your mail",
            shot("shot-tasks.svg", "three task lists shown side by side with checkboxes, some items completed"),
            ["multiple task lists, one-tap clearing of completed items, and Google Tasks sync — so the "
             "thing you were supposed to do about that email lives beside the email."],
            flip=True),
    feature("offline", "a plane-friendly mail client",
            shot("shot-offline.svg", "the mail view showing an offline notice while messages remain readable"),
            ["mailboxes sync into a local database, so mail, attachments, inline images and search all "
             "keep working with no connection.",
             "anything you do offline is queued and replayed when you are back, and you can trigger a "
             "full or per-mailbox sync whenever you want."]),
    feature("appearance", "make it yours",
            shot("shot-appearance.svg", "the appearance settings with light, dark and follow-system theme cards and a list of languages"),
            ["light and dark themes plus follow-the-system, and custom themes you can import from a "
             "file. 64 interface languages ship with the app, all contributed through the repository.",
             "guvercin ships with Hanken Grotesk and lets you change the reading font per account."],
            bullets=["English · Türkçe · Deutsch · Français · Español · Português",
                     "Русский · Українська · Polski · Nederlands · Svenska · Norsk",
                     "العربية · فارسی · हिन्दी · বাংলা · ไทย · 日本語 · 한국어 · 中文",
                     "…and 40 more"],
            flip=True),
    feature("keyboard", "every shortcut is yours to change",
            shot("shot-keyboard.svg", "the shortcuts settings listing mail and navigation shortcuts with keycaps and toggles"),
            ["shortcuts are grouped into mail actions, navigation and tabs, view and layout, compose "
             "and application, and every single one can be rebound or switched off."]),
    feature("privacy", "designed so we never see anything",
            shot("shot-privacy.svg", "the privacy settings showing local encryption always on and telemetry listed as not present"),
            ["every database is SQLCipher-encrypted and cached files are sealed with "
             "XChaCha20-Poly1305. that cannot be switched off. the key that unlocks them is a file "
             "in your user profile, readable by anything running as you, so keep full-disk "
             "encryption on — the details are in SECURITY.md.",
             "remote images are not loaded until you ask for them, so opening a message tells the "
             "sender nothing. there is no telemetry, no crash reporting and no advertising anywhere "
             "in the app. when you uninstall, guvercin offers to erase its local data — or to keep "
             "it for a reinstall."],
            flip=True),
])

KEYCAPS = [
    ("new message", ["Ctrl", "N"]), ("reply", ["Ctrl", "R"]),
    ("reply all", ["Ctrl", "Shift", "R"]), ("forward", ["Ctrl", "Shift", "F"]),
    ("archive", ["E"]), ("toggle read", ["Ctrl", "U"]), ("search", ["Ctrl", "F"]),
    ("sync", ["F5"]), ("send", ["Ctrl", "Enter"]), ("save draft", ["Ctrl", "S"]),
    ("settings", ["Ctrl", ","]), ("close tab", ["Ctrl", "W"]),
]
KEYCAP_HTML = "\n      ".join(
    "<li><span>" + name + "</span> " + " ".join(f"<kbd>{k}</kbd>" for k in keys) + "</li>"
    for name, keys in KEYCAPS
)

FEATURES = f"""<main id="main">

<section class="section section--tight">
  <div class="wrap">
    <h1>everything guvercin does</h1>
    <p class="lede">a mail client, a calendar, an address book and a task list — in one native
      window, on your own machine.</p>
    <nav aria-label="features on this page" style="margin-top:32px">
      <ul class="anchor-list">
        {''.join(f'<li><a href="#{a}">{l}</a></li>' for a, l in FEATURE_ANCHORS)}
      </ul>
    </nav>
  </div>
</section>

<section class="section">
  <div class="wrap">
{FEATURES_BODY}  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <h2>the defaults, if you never change a thing</h2>
    <ul class="keycaps" style="margin-top:24px">
      {KEYCAP_HTML}
    </ul>
  </div>
</section>

</main>
"""

# ======================================================== open-source.html ==
ROADMAP = [
    ("unified cross-account search", "planned"),
    ("PGP support", "planned"),
    ("more sync providers", "planned"),
    ("signed and notarized builds", "in progress"),
    ("a mobile companion", "planned"),
]
ROADMAP_HTML = "\n      ".join(
    f'<li><span class="pill">{state}</span><span>{name}</span></li>' for name, state in ROADMAP
)

OPEN_SOURCE = f"""<main id="main">

<section class="section section--tight">
  <div class="wrap prose">
    <h1>open source, because it is your mail</h1>
    <p>email is the most personal archive most people own. password resets, contracts, the thread
      where you agreed the price, letters from people who are gone. software that reads an archive
      like that should be readable itself.</p>
    <p>every line of guvercin is public. anyone can check that it does what this website says it
      does — and that it does not do anything else.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <div class="card">
      <p class="overline">repository</p>
      <h2 style="font-size:28px">guvercin-email/guvercin-desktop</h2>
      <p>a desktop email client built with Tauri, Rust and React. mail, calendar, contacts and tasks,
        stored locally in SQLite.</p>
      <p>
        <span class="pill">stars: see GitHub</span>
        <span class="pill">forks: see GitHub</span>
        <span class="pill">issues: see GitHub</span>
        <span class="pill">v0.1.0</span>
      </p>
      <div class="btn-row" style="margin-top:8px">
        <a class="btn btn--primary" href="{REPO}" target="_blank" rel="noopener">open the repository</a>
        <a class="btn btn--secondary" href="{ISSUES}" target="_blank" rel="noopener">browse the issues</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <h2>the stack</h2>
    <div class="grid grid--4" style="margin-top:32px">
      <div class="card reveal" data-delay="0"><h3>Tauri</h3><p>the native shell. one small window
        instead of a browser bundled per app.</p></div>
      <div class="card reveal" data-delay="1"><h3>Rust</h3><p>the mail engine — IMAP, SMTP and sync.
        memory safety matters when you are parsing other people’s messages.</p></div>
      <div class="card reveal" data-delay="2"><h3>React</h3><p>the interface. a familiar layer, so
        contributing a fix does not require learning a new UI toolkit first.</p></div>
      <div class="card reveal" data-delay="3"><h3>SQLite</h3><p>local storage. your mail ends up in a
        file you own, on a disk you own.</p></div>
    </div>
  </div>
</section>

<section class="section" id="contribute">
  <div class="wrap">
    <h2>how to contribute</h2>
    <p class="note">we are a small open source project, so every one of these genuinely helps.</p>
    <div class="grid grid--3" style="margin-top:32px">
      <div class="card">
        {IC_CODE}
        <h3>write code</h3>
        <p>build from source with the snippet on the download page, pick a good-first issue, and open
          a pull request.</p>
        <p><a href="{CONTRIB}" target="_blank" rel="noopener">contributing notes →</a></p>
      </div>
      <div class="card">
        {IC_MAIL}
        <h3>translate guvercin</h3>
        <p>the app ships 64 languages, all contributed through the repository. adding a language means
          adding one JSON file under the locales folder.</p>
        <p><a href="{LOCALES}" target="_blank" rel="noopener">the locales folder →</a></p>
      </div>
      <div class="card">
        {IC_BUG}
        <h3>report and test</h3>
        <p>file issues with your operating system, the app version and the steps to reproduce. try the
          beta channel and tell us what broke.</p>
        <p><a href="{ISSUES}" target="_blank" rel="noopener">open an issue →</a></p>
      </div>
    </div>
  </div>
</section>

<section class="section section--alt" id="roadmap">
  <div class="wrap prose">
    <h2>roadmap</h2>
    <p class="note">indicative, not a promise. it is what we would like to do next, in no strict
      order.</p>
    <ul class="checklist">
      {ROADMAP_HTML}
    </ul>
    <p>want something else? <a href="{ISSUES}" target="_blank" rel="noopener">open an issue</a> — the
      roadmap follows what people actually ask for.</p>
  </div>
</section>

<section class="section">
  <div class="wrap prose">
    <div class="callout">
      <h2 style="font-size:28px">security disclosure</h2>
      <p>found a vulnerability? write to <a href="mailto:support@guvercin.email">support@guvercin.email</a>
        with the details and how to reproduce it. please give us a chance to ship a fix before opening
        a public issue.</p>
      <p>there is no bounty programme — we are a small project — but you will be credited in the
        release notes if you want to be.</p>
    </div>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap prose">
    <div class="summary-box">
      <h2 style="font-size:24px">the license, in three lines</h2>
      <p>use it for free, at home or at work, for as long as you like.</p>
      <p>read it, modify it, fork it, and share your changes under the same terms.</p>
      <p>do not sell it, or build a paid product or service whose value comes substantially from it.</p>
      <p><a href="license.html">read the full license →</a></p>
    </div>
  </div>
</section>

</main>
"""

# ================================================================ faq.html ==
FAQ_GROUPS = [
    ("the basics", [
        ("is guvercin really free?",
         ["yes. it is free and open source, with no subscription, no paid tier and nothing to upgrade "
          "to. you cannot resell it, but you can use it as much as you like."]),
        ("which email providers work?",
         ["any provider that speaks IMAP and SMTP — Gmail, Outlook and Hotmail, Yandex, iCloud, "
          "Fastmail, your university, your own server. Google accounts can sign in with a single "
          "click."]),
        ("does guvercin give me an email address?",
         ["no. it is a client for the mailboxes you already have, not a mail provider."]),
        ("what does “guvercin” mean?",
         ["it is Turkish for pigeon — the bird that used to carry your mail."]),
        ("how finished is it?",
         ["version 0.1.0 is an early release. it is used daily by the people who make it, but expect "
          "rough edges and please report them."]),
    ]),
    ("privacy &amp; security", [
        ("where is my mail stored?",
         ["in a local database on your own computer. nothing reaches our servers, because there are "
          "no servers."]),
        ("do you collect analytics?",
         ["no telemetry, no usage statistics, no crash reporting, no ads, no tracking code of any "
          "kind — in the app or on this website."]),
        ("is my password safe?",
         ["credentials and OAuth tokens live in the SQLCipher-encrypted local database, never in "
          "plain text. with Google sign-in, the app never sees your password at all. note that the "
          "key to that database is a file in your user profile rather than the OS keychain, so it "
          "protects you against a lost disk, not against something already running as you."]),
        ("can senders tell that I opened their email?",
         ["no — remote images are withheld until you click load images, so opening a message sends "
          "the sender nothing at all. that is what defeats a tracking pixel."]),
        ("what happens to my data if I uninstall?",
         ["Settings offers a proper uninstall that asks whether you want your local data erased or "
          "kept for a future reinstall."]),
    ]),
    ("installing &amp; using", [
        ("does it work offline?",
         ["yes. synced mail, attachments and search work with no connection, and anything you do is "
          "replayed when you reconnect."]),
        ("macOS says the app cannot be opened because the developer cannot be verified.",
         ["right-click the app, choose Open, and confirm once. the builds are not notarized yet; "
          "signing is on the roadmap."]),
        ("Windows shows a SmartScreen warning.",
         ["choose More info, then Run anyway. same reason: the installer is not code-signed yet."]),
        ("can I use it on Linux?",
         ["yes, with the .deb or .rpm package. you will need WebKitGTK and libsecret, which most "
          "desktops already have."]),
        ("what is the difference between stable and beta?",
         ["beta gets features first and may break or change how data is stored; stable is what we "
          "recommend for the mail you actually rely on."]),
        ("can I use guvercin at work or in my company?",
         ["yes, for internal use. the only thing you may not do is sell it or build a paid service out "
          "of it."]),
        ("how do I make guvercin my default mail app?",
         ["it offers this on first launch, and you can change it later in Settings — after that, "
          "mailto: links open a compose window."]),
        ("can I change the keyboard shortcuts?",
         ["all of them, individually, in Settings."]),
        ("is there a mobile app?",
         ["not today. a companion app is on the roadmap, nothing more."]),
        ("how do I report a bug or request a feature?",
         [f'open an issue on <a href="{ISSUES}" target="_blank" rel="noopener">GitHub</a>, or write to '
          '<a href="mailto:support@guvercin.email">support@guvercin.email</a> with your operating '
          'system, the app version and what you did before it broke.']),
    ]),
]


def faq_group(title, items):
    rows = []
    for q, answers in items:
        ps = "".join(f"<p>{a}</p>" for a in answers)
        rows.append(
            f"      <details>\n        <summary>{q}</summary>\n"
            f"        <div class=\"answer\">{ps}</div>\n      </details>\n"
        )
    return (f'    <h2>{title}</h2>\n    <div class="accordion" style="margin-bottom:48px">\n'
            + "".join(rows) + "    </div>\n")


FAQ = f"""<main id="main">

<section class="section section--tight">
  <div class="wrap">
    <h1>questions &amp; support</h1>
    <p class="lede">the things people ask before and after they install it. if your question is not
      here, write to us — a person reads that address.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
{''.join(faq_group(t, items) for t, items in FAQ_GROUPS)}  </div>
</section>

<section class="section section--alt">
  <div class="wrap">
    <h2>still need a hand?</h2>
    <div class="grid grid--2" style="margin-top:32px">
      <div class="card">
        {IC_MAIL}
        <h3>still stuck?</h3>
        <p>write to <a href="mailto:support@guvercin.email">support@guvercin.email</a> with your
          operating system and app version. we read everything.</p>
      </div>
      <div class="card">
        {IC_BUG}
        <h3>found a bug?</h3>
        <p>open an issue on <a href="{ISSUES}" target="_blank" rel="noopener">GitHub</a> with the steps
          to reproduce it, and it goes straight to the people who can fix it.</p>
      </div>
    </div>
  </div>
</section>

</main>
"""

# ============================================================ contact.html ==
CONTACT = f"""<main id="main">

<section class="section section--tight">
  <div class="wrap">
    <h1>get in touch</h1>
    <p class="lede">a small open source project, reachable by actual email.</p>
  </div>
</section>

<section class="section section--tight">
  <div class="wrap">
    <h2 class="visually-hidden">ways to reach us</h2>
    <div class="grid grid--3">
      <div class="card reveal" data-delay="0">
        {IC_MAIL}
        <h3>general &amp; partnerships</h3>
        <p>questions about the project, press, collaborations.</p>
        <p><a class="btn btn--secondary btn--sm" href="mailto:hello@guvercin.email">hello@guvercin.email</a></p>
      </div>
      <div class="card reveal" data-delay="1">
        {IC_BUG}
        <h3>support &amp; bug reports</h3>
        <p>trouble installing, an account that will not connect, something that crashed. including
          your operating system and app version gets you a faster answer.</p>
        <p><a class="btn btn--secondary btn--sm" href="mailto:support@guvercin.email">support@guvercin.email</a></p>
      </div>
      <div class="card reveal" data-delay="2">
        {IC_CODE}
        <h3>developers</h3>
        <p>feature requests, patches, and anything best discussed in public.</p>
        <p>
          <a class="btn btn--secondary btn--sm" href="{ISSUES}" target="_blank" rel="noopener">GitHub Issues</a>
        </p>
        <p><a href="{DISCUSSIONS}" target="_blank" rel="noopener">GitHub Discussions →</a></p>
      </div>
    </div>
    <p class="note" style="margin-top:32px">we are a small open source project, so expect a reply
      within a few days rather than a few minutes.</p>
  </div>
</section>

<section class="section section--alt">
  <div class="wrap prose">
    <h2>before you write</h2>
    <ul>
      <li>check the <a href="faq.html">FAQ</a> — most installation questions are answered there.</li>
      <li>check the <a href="{ISSUES}" target="_blank" rel="noopener">open issues</a> in case someone
        has already reported it.</li>
      <li>include your operating system and your guvercin version, from Settings → About.</li>
    </ul>
    <p>for security issues, write to <a href="mailto:support@guvercin.email">support@guvercin.email</a>
      and please hold off on a public issue until there is a fix.</p>
    <p class="note">there is no contact form on this page, because there is no backend to receive one.
      nothing you send goes anywhere except an inbox.</p>
  </div>
</section>

</main>
"""

# ============================================================ privacy.html ==
PRIVACY = """<main id="main">

<section class="section">
  <div class="wrap prose">
    <h1>Privacy Policy</h1>
    <p class="note">plain-language summary: guvercin has no servers, so there is nothing for us to
      collect. this page explains that in more detail.</p>
    <p class="small">last updated 26 July 2026</p>

    <div class="toc" style="margin:32px 0">
      <h2 style="font-size:16px;margin-bottom:12px">on this page</h2>
      <ul>
        <li><a href="#app">the app</a></li>
        <li><a href="#third-parties">third parties</a></li>
        <li><a href="#analytics">analytics and telemetry</a></li>
        <li><a href="#website">the website</a></li>
        <li><a href="#email">email</a></li>
        <li><a href="#children">children</a></li>
        <li><a href="#rights">your rights</a></li>
        <li><a href="#changes">changes</a></li>
      </ul>
    </div>

    <p>guvercin is an open source desktop email application. This policy covers both the
      guvercin.email website and the desktop app.</p>

    <h2 id="app" style="font-size:24px">The app</h2>
    <p>guvercin runs entirely on your own computer. Your messages, drafts, attachments, calendar
      events, contacts and tasks are stored in a local database on your device. Your account
      credentials and OAuth tokens are stored inside that encrypted database, never in plain text.
      The key that unlocks it is a file in your user profile. We operate no servers, no accounts and
      no cloud storage — your data is never uploaded to us, because there is nowhere for it to go.</p>

    <h2 id="third-parties" style="font-size:24px">Third parties</h2>
    <p>When you add an account, the app connects directly from your computer to your own email,
      calendar or contacts provider (for example Gmail, Outlook, Yandex, or your own IMAP/SMTP or
      CalDAV server). Those connections are governed by that provider's privacy policy. Remote images
      inside messages are not loaded at all until you choose to load them, and sender avatars may be
      requested from third-party services; both can be turned off in Settings. Opening a link in an email opens it in your own browser.</p>

    <h2 id="analytics" style="font-size:24px">Analytics and telemetry</h2>
    <p>The app collects no analytics, no usage statistics and no crash telemetry, and it contains no
      advertising or tracking code.</p>

    <h2 id="website" style="font-size:24px">The website</h2>
    <p>guvercin.email is a static site. It sets no advertising or tracking cookies, uses no analytics,
      and does not build profiles of visitors. The only thing stored in your browser is your light or
      dark theme preference. Our hosting provider may keep standard server logs (IP address, browser
      type, requested page) for security and reliability. Downloads are served from GitHub; GitHub's
      own privacy policy applies when you download a release.</p>

    <h2 id="email" style="font-size:24px">Email</h2>
    <p>If you write to <a href="mailto:hello@guvercin.email">hello@guvercin.email</a> or
      <a href="mailto:support@guvercin.email">support@guvercin.email</a>, we keep your message and your
      address only for as long as it takes to answer you and to keep a record of the issue, and we
      never use them for marketing.</p>

    <h2 id="children" style="font-size:24px">Children</h2>
    <p>guvercin is not directed at children under 13.</p>

    <h2 id="rights" style="font-size:24px">Your rights</h2>
    <p>Because we hold no personal data about you, there is nothing for us to export or delete — your
      data is already in your own hands, on your own disk. If you have written to us by email and want
      that correspondence deleted, ask and we will delete it.</p>

    <h2 id="changes" style="font-size:24px">Changes</h2>
    <p>If this policy changes, the date above will be updated and the change will be visible in the
      website's public repository history.</p>

    <p>Questions: <a href="mailto:hello@guvercin.email">hello@guvercin.email</a></p>
  </div>
</section>

</main>
"""

# ============================================================ license.html ==
LICENSE = f"""<main id="main">

<section class="section">
  <div class="wrap prose">
    <h1>license</h1>
    <p class="lede">free to use, free to read, free to modify — not for resale.</p>

    <div class="summary-box" style="margin:32px 0">
      <p><strong>guvercin is licensed under the Apache License 2.0 with the Commons Clause
        condition.</strong></p>
      <p><strong>You may:</strong> use it for free at home or at work; read, study and modify the
        source; fork it and share your changes; redistribute it under these same terms.</p>
      <p><strong>You may not:</strong> sell the software, resell it, charge a subscription for it, or
        offer a paid product or service whose value comes substantially from it.</p>
    </div>

    <h2 style="font-size:24px">an honest note about the words</h2>
    <p>the Commons Clause is an extra condition layered on top of Apache 2.0. Because of it, guvercin
      is source-available rather than OSI-approved open source. We use the phrase “open source” on this
      site in its everyday sense — the source is public and you can build it yourself — and we would
      rather say this plainly here than bury it.</p>

    <h2 style="font-size:24px">copyright</h2>
    <p>Copyright (c) 2026 Hidayet Erdem / Guvercin / Herdem.</p>

    <h2 style="font-size:24px">third-party notices</h2>
    <p>the app ships the Hanken Grotesk typeface under the SIL Open Font License. the rest of the
      dependency licenses are listed in the repository.</p>

    <p style="margin-top:32px">
      <a class="btn btn--secondary" href="{LICENSE_FILE}" target="_blank" rel="noopener">read the full license text →</a>
    </p>
  </div>
</section>

</main>
"""

# ================================================================ 404.html ==
NOTFOUND = f"""<main id="main">
<section class="section center">
  <div class="wrap">
    <img class="brand__mark--light" src="assets/img/logo-mark-light.svg" width="120" height="112" alt="">
    <img class="brand__mark--dark" src="assets/img/logo-mark-dark.svg" width="120" height="112" alt="">
    <h1 style="margin-top:24px">this page flew off</h1>
    <p class="lede">the bird could not find that address. it happens.</p>
    <div class="btn-row">
      <a class="btn btn--primary btn--lg" href="index.html">go home</a>
      <a class="btn btn--secondary btn--lg" href="download.html">download guvercin</a>
    </div>
  </div>
</section>
</main>
"""


PAGES = [
    ("index.html",
     "guvercin — free &amp; open source desktop email client for macOS, Windows and Linux",
     "guvercin is a free, open source desktop email client for macOS, Windows and Linux, with "
     "calendar, contacts and tasks. your mail stays on your own machine.",
     "index.html", INDEX, JSONLD, True),
    ("download.html",
     "download guvercin — macOS, Windows and Linux",
     "download guvercin free for macOS, Windows or Linux. .dmg, .exe, .deb and .rpm builds, install "
     "steps, system requirements and the source to build it yourself.",
     "download.html", DOWNLOAD, "", True),
    ("features.html",
     "features — guvercin",
     "mail, calendar, contacts, tasks, offline sync, 64 languages and rebindable shortcuts, in one "
     "native window. see what guvercin does, then download it free.",
     "features.html", FEATURES, "", True),
    ("open-source.html",
     "open source — guvercin",
     "guvercin is public source you can read, build and contribute to: Tauri, Rust, React and "
     "SQLite. see the repository, the roadmap and how to help.",
     "open-source.html", OPEN_SOURCE, "", True),
    ("faq.html",
     "faq &amp; support — guvercin",
     "answers about guvercin: what it costs, which providers work, where your mail is stored, "
     "installing on macOS, Windows and Linux, and how to get help.",
     "faq.html", FAQ, "", True),
    ("contact.html",
     "contact — guvercin",
     "get in touch with the guvercin project by email: general questions, support and bug reports, "
     "or GitHub for anything best discussed in public.",
     "contact.html", CONTACT, "", True),
    ("privacy.html",
     "privacy policy — guvercin",
     "guvercin has no servers, no accounts and no telemetry, so there is nothing for us to collect. "
     "read how the desktop app and this website handle your data.",
     "privacy.html", PRIVACY, "", False),
    ("license.html",
     "license — guvercin",
     "guvercin is licensed under the Apache License 2.0 with the Commons Clause: free to use, read "
     "and modify at home or at work, but not to sell or resell.",
     "license.html", LICENSE, "", False),
    ("404.html",
     "page not found — guvercin",
     "that page does not exist on guvercin.email. head back to the home page, or download the free "
     "and open source guvercin email client for macOS, Windows and Linux.",
     "404.html", NOTFOUND, '<meta name="robots" content="noindex">\n', False),
]
