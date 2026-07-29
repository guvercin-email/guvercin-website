#!/usr/bin/env python3
"""Generate clean, labelled UI mockups (SVG) for the guvercin marketing site.

No external assets, no network. Palette is restricted to the brand system:
  charcoal #4A4B4B  yellow #FECD01  blue #2596BE  cream #FEF5C8
  grey-50 #F7F7F6   border #E9EAEA  muted #7A7B7B  white #FFFFFF
"""
import os

W, H = 1600, 1000
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")

CHAR = "#4A4B4B"
YEL = "#FECD01"
BLUE = "#2596BE"
CREAM = "#FEF5C8"
G50 = "#F7F7F6"
BORD = "#E9EAEA"
MUT = "#7A7B7B"
WHITE = "#FFFFFF"

TR = {}          # English -> current language; empty means English


def tr(s):
    return TR.get(s, s)


FONT = "system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif"


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def r(x, y, w, h, fill, rx=0, stroke=None, sw=1, op=None):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"'
    if stroke:
        s += f' stroke="{stroke}" stroke-width="{sw}"'
    if op is not None:
        s += f' opacity="{op}"'
    return s + "/>"


def t(x, y, s, size=15, fill=CHAR, weight=400, anchor="start", op=None):
    a = f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"'
    if op is not None:
        a += f' opacity="{op}"'
    return a + f">{esc(tr(s))}</text>"


def c(cx, cy, rad, fill, op=None):
    s = f'<circle cx="{cx}" cy="{cy}" r="{rad}" fill="{fill}"'
    if op is not None:
        s += f' opacity="{op}"'
    return s + "/>"


def bar(x, y, w, h=9, fill=CHAR, op=0.18, rx=4):
    return r(x, y, w, h, fill, rx=rx, op=op)


def line(x1, y1, x2, y2, stroke=BORD, sw=1):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"/>'


def window(inner, label):
    """Wrap content in an app window chrome with a title bar and a caption."""
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{esc(tr(label))}">',
        r(0, 0, W, H, WHITE),
        # title bar
        r(0, 0, W, 48, G50),
        line(0, 48, W, 48),
        c(28, 24, 6, BORD), c(50, 24, 6, BORD), c(72, 24, 6, BORD),
        t(W / 2, 29, "guvercin", 15, MUT, 600, "middle"),
        f'<g transform="translate(0,48)">',
        inner,
        "</g>",
        # caption strip
        r(0, H - 34, W, 34, CHAR),
        t(20, H - 12, label, 15, "#E9EAEA", 500),
        "</svg>",
    ]
    return "\n".join(out)


IH = H - 48 - 34  # inner height available under the title bar, above the caption

# ---------------------------------------------------------------- sidebar ----

def sidebar(active="Inbox", items=None, width=280, title="you@example.com"):
    items = items or [
        ("Inbox", "12"), ("Drafts", "2"), ("Sent", ""), ("Archive", ""),
        ("Spam", ""), ("Trash", ""),
    ]
    g = [r(0, 0, width, IH, G50), line(width, 0, width, IH)]
    g.append(r(16, 20, width - 32, 46, WHITE, rx=12, stroke=BORD))
    g.append(c(40, 43, 13, YEL))
    g.append(t(62, 48, title, 14, CHAR, 600))
    g.append(t(20, 100, "MAILBOXES", 11, MUT, 600))
    y = 118
    for name, count in items:
        if name == active:
            g.append(r(10, y, width - 20, 38, WHITE, rx=10, stroke=BORD))
            g.append(r(10, y + 9, 3, 20, YEL, rx=2))
        g.append(t(28, y + 24, name, 15, CHAR, 600 if name == active else 400))
        if count:
            g.append(r(width - 56, y + 10, 34, 19, YEL, rx=999))
            g.append(t(width - 39, y + 24, count, 12, CHAR, 700, "middle"))
        y += 42
    g.append(t(20, y + 28, "LABELS", 11, MUT, 600))
    y += 44
    for col, name in ((BLUE, "work"), (YEL, "family"), (MUT, "receipts")):
        g.append(c(30, y + 12, 5, col))
        g.append(t(46, y + 17, name, 14, CHAR))
        y += 34
    return "\n".join(g)


def msg_list(x, width, rows, active=0, header="Inbox"):
    g = [r(x, 0, width, IH, WHITE), line(x + width, 0, x + width, IH)]
    g.append(t(x + 24, 42, header, 19, CHAR, 700))
    # search field
    g.append(r(x + 24, 60, width - 48, 36, G50, rx=12, stroke=BORD))
    g.append(c(x + 46, 78, 6, MUT, op=0.55))
    g.append(line(x + 51, 83, x + 57, 89, MUT, 2))
    g.append(t(x + 68, 83, "search your mail", 13, MUT))
    y = 112
    for i, (who, subj, snip, when, unread) in enumerate(rows):
        if i == active:
            g.append(r(x + 8, y, width - 16, 84, CREAM, rx=12, op=0.75))
        g.append(c(x + 40, y + 30, 16, BLUE, op=0.14))
        g.append(t(x + 40, y + 35, who[0].upper(), 14, BLUE, 700, "middle"))
        g.append(t(x + 68, y + 26, who, 14, CHAR, 700 if unread else 500))
        g.append(t(x + width - 24, y + 26, when, 12, MUT, 400, "end"))
        g.append(t(x + 68, y + 48, subj, 14, CHAR, 600 if unread else 400))
        g.append(bar(x + 68, y + 60, width - 130, 8, CHAR, 0.14))
        if unread:
            g.append(c(x + 18, y + 30, 4, BLUE))
        g.append(line(x + 24, y + 84, x + width - 24, y + 84))
        y += 88
        if y > IH - 60:
            break
    return "\n".join(g)


def reading_pane(x, width, subject, sender, lines=7, attach=True, chips=None):
    g = [r(x, 0, width, IH, WHITE)]
    # toolbar
    g.append(r(x, 0, width, 56, WHITE))
    g.append(line(x, 56, x + width, 56))
    bx = x + 24
    for lab in ("reply", "reply all", "forward", "archive"):
        w = 22 + len(tr(lab)) * 7
        g.append(r(bx, 14, w, 30, G50, rx=999, stroke=BORD))
        g.append(t(bx + w / 2, 33, lab, 12, CHAR, 500, "middle"))
        bx += w + 10
    g.append(t(x + 32, 100, subject, 24, CHAR, 700))
    g.append(c(x + 44, 142, 18, YEL, op=0.85))
    g.append(t(x + 44, 148, sender[0].upper(), 15, CHAR, 700, "middle"))
    g.append(t(x + 74, 138, sender, 15, CHAR, 600))
    g.append(t(x + 74, 158, "to me · 10:24", 13, MUT))
    y = 200
    widths = [0.94, 0.99, 0.86, 0.97, 0.72, 0.93, 0.62]
    for i in range(lines):
        g.append(bar(x + 32, y, int((width - 96) * widths[i % len(widths)]), 10, CHAR, 0.13))
        y += 26
    if chips:
        y += 14
        cx = x + 32
        for ch in chips:
            w = 26 + len(tr(ch)) * 7
            g.append(r(cx, y, w, 32, G50, rx=10, stroke=BORD))
            g.append(t(cx + w / 2, y + 21, ch, 12, CHAR, 500, "middle"))
            cx += w + 12
    elif attach:
        y += 14
        g.append(r(x + 32, y, 220, 54, G50, rx=12, stroke=BORD))
        g.append(r(x + 46, y + 14, 22, 26, BLUE, rx=4, op=0.2))
        g.append(t(x + 80, y + 26, "quarterly.pdf", 13, CHAR, 600))
        g.append(t(x + 80, y + 44, "248 KB", 12, MUT))
    return "\n".join(g)


ROWS = [
    ("Ayşe Demir", "the venue is confirmed for the 14th", "", "10:24", True),
    ("build@ci", "nightly build passed on all platforms", "", "09:02", True),
    ("Fastmail", "your monthly summary is ready", "", "Tue", False),
    ("Jonas Petit", "re: translation strings for Catalan", "", "Tue", False),
    ("mum", "photos from the weekend", "", "Mon", False),
    ("Deniz K.", "invoice for June", "", "Mon", False),
    ("no-reply", "your package has shipped", "", "Sun", False),
]


def make_mail():
    inner = "\n".join([
        sidebar(),
        msg_list(280, 460, ROWS, active=0),
        reading_pane(740, W - 740, "the venue is confirmed for the 14th", "Ayşe Demir"),
    ])
    return window(inner, "screenshot: mail view — folder tree, message list and reading pane")


def make_offline():
    inner = [sidebar()]
    # offline banner across the two right columns
    inner.append(r(280, 0, W - 280, 46, CREAM))
    inner.append(line(280, 46, W, 46))
    inner.append(c(310, 23, 6, CHAR, op=0.5))
    inner.append(t(328, 28, "offline — showing your local copy. 3 actions queued, they will send when you reconnect.", 14, CHAR, 600))
    inner.append('<g transform="translate(0,46)">')
    inner.append(msg_list(280, 460, ROWS, active=1))
    inner.append(reading_pane(740, W - 740, "nightly build passed on all platforms", "build@ci", lines=6))
    inner.append("</g>")
    return window("\n".join(inner), "screenshot: reading mail with no connection")


def make_composer():
    g = [r(0, 0, W, IH, WHITE)]
    # ribbon
    g.append(r(0, 0, W, 54, G50))
    g.append(line(0, 54, W, 54))
    x = 24
    for lab in ("B", "I", "U", "S"):
        g.append(r(x, 12, 32, 30, WHITE, rx=8, stroke=BORD))
        g.append(t(x + 16, 33, lab, 14, CHAR, 700, "middle"))
        x += 38
    x += 14
    for lab in ("list", "quote", "link", "image", "code"):
        w = 20 + len(tr(lab)) * 7
        g.append(r(x, 12, w, 30, WHITE, rx=8, stroke=BORD))
        g.append(t(x + w / 2, 32, lab, 12, CHAR, 500, "middle"))
        x += w + 10
    # fields
    y = 92
    for lab, val in (("to", "ayse@example.com"), ("cc", ""), ("subject", "re: the venue on the 14th")):
        g.append(t(40, y + 6, lab, 13, MUT, 600))
        g.append(t(120, y + 6, val if val else "", 15, CHAR, 500))
        g.append(line(40, y + 22, W - 40, y + 22))
        y += 56
    # body
    y += 10
    for wpct in (0.82, 0.9, 0.74, 0.88, 0.55, 0.86, 0.7, 0.42):
        g.append(bar(40, y, int((W - 120) * wpct), 11, CHAR, 0.13))
        y += 30
    # attachments dropped in
    y += 12
    cx = 40
    for name in ("floorplan.pdf", "budget.xlsx"):
        w = 40 + len(tr(name)) * 7
        g.append(r(cx, y, w, 40, G50, rx=10, stroke=BORD))
        g.append(r(cx + 14, y + 11, 16, 18, BLUE, rx=3, op=0.22))
        g.append(t(cx + 40, y + 25, name, 13, CHAR, 500))
        cx += w + 14
    g.append(r(cx, y, 168, 40, WHITE, rx=10, stroke=BLUE, sw=1.5))
    g.append(t(cx + 84, y + 25, "drop files here", 13, BLUE, 500, "middle"))
    # footer actions
    g.append(line(0, IH - 72, W, IH - 72))
    g.append(r(40, IH - 56, 120, 40, YEL, rx=12))
    g.append(t(100, IH - 31, "send", 15, CHAR, 700, "middle"))
    g.append(r(176, IH - 56, 140, 40, WHITE, rx=12, stroke=BLUE, sw=1.5))
    g.append(t(246, IH - 31, "save draft", 14, BLUE, 600, "middle"))
    g.append(t(W - 40, IH - 31, "Ctrl+Enter to send", 13, MUT, 400, "end"))
    return window("\n".join(g), "screenshot: the compose window, popped out")


def make_signin():
    g = [r(0, 0, W, IH, G50)]
    # dialog
    dx, dy, dw, dh = 400, 60, 800, IH - 130
    g.append(r(dx, dy, dw, dh, WHITE, rx=20, stroke=BORD))
    g.append(t(dx + 48, dy + 62, "add an account", 26, CHAR, 700))
    g.append(t(dx + 48, dy + 94, "guvercin will try to find your server settings for you.", 15, MUT))
    # google button
    by = dy + 130
    g.append(r(dx + 48, by, dw - 96, 56, WHITE, rx=12, stroke=BORD))
    g.append(c(dx + 84, by + 28, 13, BLUE, op=0.18))
    g.append(t(dx + 84, by + 34, "G", 15, BLUE, 700, "middle"))
    g.append(t(dx + 112, by + 34, "continue with Google", 16, CHAR, 600))
    # divider
    dyy = by + 88
    g.append(line(dx + 48, dyy, dx + dw / 2 - 30, dyy))
    g.append(t(dx + dw / 2, dyy + 5, "or", 13, MUT, 400, "middle"))
    g.append(line(dx + dw / 2 + 30, dyy, dx + dw - 48, dyy))
    # fields
    fy = dyy + 34
    for lab, val in (("email address", "you@example.com"), ("password", "••••••••••••")):
        g.append(t(dx + 48, fy + 14, lab, 13, MUT, 600))
        g.append(r(dx + 48, fy + 24, dw - 96, 48, WHITE, rx=12, stroke=BORD))
        g.append(t(dx + 66, fy + 54, val, 15, CHAR))
        fy += 92
    # detected servers
    g.append(r(dx + 48, fy + 10, dw - 96, 96, CREAM, rx=12, op=0.7))
    g.append(t(dx + 70, fy + 42, "detected: imap.example.com : 993 (SSL)", 14, CHAR, 600))
    g.append(t(dx + 70, fy + 68, "smtp.example.com : 465 (SSL) — change manually", 14, CHAR, 500, op=0.8))
    # primary
    g.append(r(dx + 48, dy + dh - 84, 200, 48, YEL, rx=12))
    g.append(t(dx + 148, dy + dh - 54, "add account", 15, CHAR, 700, "middle"))
    return window("\n".join(g), "screenshot: adding an account")


def make_calendar():
    items = [("Calendar", ""), ("work", ""), ("family", ""), ("birthdays", ""), ("holidays TR", "")]
    g = [sidebar(active="Calendar", items=items, title="calendars")]
    x0 = 280
    g.append(r(x0, 0, W - x0, IH, WHITE))
    g.append(t(x0 + 32, 44, "July 2026", 22, CHAR, 700))
    for i, lab in enumerate(("day", "week", "month")):
        bx = W - 300 + i * 92
        active = lab == "month"
        g.append(r(bx, 22, 84, 32, YEL if active else G50, rx=999, stroke=None if active else BORD))
        g.append(t(bx + 42, 43, lab, 13, CHAR, 700 if active else 500, "middle"))
    top = 74
    cols = 7
    cw = (W - x0 - 64) / cols
    days = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
    for i, d in enumerate(days):
        g.append(t(x0 + 32 + i * cw + 12, top + 16, d, 12, MUT, 600))
    grid_top = top + 30
    rows = 5
    rh = (IH - grid_top - 40) / rows
    g.append(r(x0 + 32, grid_top, cw * cols, rh * rows, WHITE, rx=12, stroke=BORD))
    for i in range(1, cols):
        g.append(line(x0 + 32 + i * cw, grid_top, x0 + 32 + i * cw, grid_top + rh * rows))
    for j in range(1, rows):
        g.append(line(x0 + 32, grid_top + j * rh, x0 + 32 + cw * cols, grid_top + j * rh))
    n = 29
    events = {
        3: [("team sync", BLUE)], 5: [("dentist", YEL)], 9: [("release 0.1.0", YEL), ("review", BLUE)],
        12: [("flight", BLUE)], 14: [("venue visit", YEL)], 18: [("standup", BLUE)],
        21: [("mum's birthday", YEL)], 25: [("translation call", BLUE)], 27: [("retro", BLUE)],
    }
    for j in range(rows):
        for i in range(cols):
            idx = j * cols + i
            day = idx - 2
            cx = x0 + 32 + i * cw
            cy = grid_top + j * rh
            if day < 1 or day > n:
                continue
            today = day == 14
            if today:
                g.append(c(cx + 22, cy + 22, 14, YEL))
            g.append(t(cx + 22, cy + 27, str(day), 12, CHAR, 700 if today else 400, "middle"))
            for k, (name, col) in enumerate(events.get(day, [])):
                ey = cy + 40 + k * 26
                g.append(r(cx + 8, ey, cw - 16, 21, col, rx=6, op=0.16))
                g.append(r(cx + 8, ey, 3, 21, col, rx=2))
                g.append(t(cx + 18, ey + 15, name, 11, CHAR, 600))
    return window("\n".join(g), "screenshot: the built-in calendar")


def make_contacts():
    items = [("All contacts", "412"), ("work", "88"), ("family", "24"), ("newsletters", "31")]
    g = [sidebar(active="All contacts", items=items, title="address book")]
    names = ["Ayşe Demir", "Bruno Sala", "Deniz Kaya", "Elif Aydın", "Jonas Petit",
             "Lucia Ferrari", "Marta Nowak", "Omar Haddad"]
    x = 280
    wl = 420
    g.append(r(x, 0, wl, IH, WHITE))
    g.append(line(x + wl, 0, x + wl, IH))
    g.append(t(x + 24, 42, "contacts", 19, CHAR, 700))
    g.append(r(x + 24, 60, wl - 48, 36, G50, rx=12, stroke=BORD))
    g.append(t(x + 44, 83, "search contacts", 13, MUT))
    y = 116
    for i, nm in enumerate(names):
        if i == 0:
            g.append(r(x + 8, y - 8, wl - 16, 60, CREAM, rx=12, op=0.75))
        g.append(c(x + 44, y + 22, 18, BLUE, op=0.14))
        g.append(t(x + 44, y + 28, "".join(p[0] for p in nm.split()[:2]), 13, BLUE, 700, "middle"))
        g.append(t(x + 76, y + 18, nm, 15, CHAR, 600))
        g.append(t(x + 76, y + 38, nm.split()[0].lower() + "@example.com", 13, MUT))
        g.append(line(x + 24, y + 52, x + wl - 24, y + 52))
        y += 60
    # detail
    dx = x + wl
    g.append(r(dx, 0, W - dx, IH, WHITE))
    g.append(c(dx + 90, 110, 46, YEL, op=0.85))
    g.append(t(dx + 90, 120, "AD", 26, CHAR, 700, "middle"))
    g.append(t(dx + 156, 100, "Ayşe Demir", 26, CHAR, 700))
    g.append(t(dx + 156, 128, "ayse@example.com", 15, BLUE))
    yy = 200
    for lab, val in (("phone", "+90 5xx xxx xx xx"), ("company", "Kadıköy Design"),
                     ("lists", "work · family"), ("note", "prefers email over calls")):
        g.append(t(dx + 48, yy, lab, 12, MUT, 600))
        g.append(t(dx + 200, yy, val, 15, CHAR, 500))
        g.append(line(dx + 48, yy + 20, W - 48, yy + 20))
        yy += 56
    bx = dx + 48
    for lab in ("export vCard", "import vCard"):
        w = 30 + len(tr(lab)) * 8
        g.append(r(bx, yy + 16, w, 40, WHITE, rx=12, stroke=BLUE, sw=1.5))
        g.append(t(bx + w / 2, yy + 41, lab, 13, BLUE, 600, "middle"))
        bx += w + 16
    return window("\n".join(g), "screenshot: contacts and lists")


def make_tasks():
    items = [("Inbox", "12"), ("Tasks", "6"), ("Calendar", ""), ("Contacts", "")]
    g = [sidebar(active="Tasks", items=items, title="you@example.com")]
    x = 280
    g.append(r(x, 0, W - x, IH, WHITE))
    g.append(t(x + 32, 44, "tasks", 22, CHAR, 700))
    g.append(r(W - 220, 22, 180, 34, WHITE, rx=999, stroke=BLUE, sw=1.5))
    g.append(t(W - 130, 44, "clear completed", 12, BLUE, 600, "middle"))
    lists = [
        ("today", [("reply to Ayşe about the venue", False), ("push translation fix", False),
                   ("book the flight", True), ("call the bank", True)]),
        ("this week", [("write release notes for 0.1.0", False), ("test the .rpm build", False),
                       ("update the FAQ page", False), ("archive June invoices", True)]),
        ("someday", [("look at PGP libraries", False), ("sketch the mobile companion", False),
                     ("try Fedora 41 build", False), ("tidy the locales folder", True)]),
    ]
    cw = (W - x - 96) / 3
    for i, (title, rows) in enumerate(lists):
        cx = x + 32 + i * (cw + 16)
        g.append(r(cx, 74, cw, IH - 120, G50, rx=16, stroke=BORD))
        g.append(t(cx + 20, 108, title, 15, CHAR, 700))
        g.append(t(cx + cw - 20, 108, str(len([q for q in rows if not q[1]])), 13, MUT, 600, "end"))
        y = 132
        for name, done in rows:
            g.append(r(cx + 12, y, cw - 24, 62, WHITE, rx=12, stroke=BORD))
            if done:
                g.append(c(cx + 34, y + 31, 10, YEL))
                g.append(f'<path d="M{cx + 29} {y + 31} l4 5 l8 -9" fill="none" stroke="{CHAR}" stroke-width="2" stroke-linecap="round"/>')
            else:
                g.append(c(cx + 34, y + 31, 10, WHITE))
                g.append(f'<circle cx="{cx + 34}" cy="{y + 31}" r="10" fill="none" stroke="{BORD}" stroke-width="1.5"/>')
            g.append(t(cx + 54, y + 30, name[:26], 13, MUT if done else CHAR, 500, op=0.6 if done else None))
            g.append(t(cx + 54, y + 48, "due today" if not done else "done", 11, MUT))
            y += 72
    return window("\n".join(g), "screenshot: the task panel")


def make_appearance():
    g = [sidebar(active="Appearance", items=[("General", ""), ("Accounts", ""), ("Appearance", ""),
                                             ("Shortcuts", ""), ("Privacy", "")], title="settings")]
    x = 280
    g.append(r(x, 0, W - x, IH, WHITE))
    g.append(t(x + 48, 56, "appearance", 26, CHAR, 700))
    g.append(t(x + 48, 90, "themes apply per account, and follow the system if you want them to.", 15, MUT))
    # theme cards
    cards = [("light", CREAM, YEL, BLUE, True), ("dark", "#14181D", "#D6B14A", "#2F88A6", False),
             ("follow system", G50, YEL, BLUE, False)]
    cw = 300
    for i, (name, bg, a1, a2, active) in enumerate(cards):
        cx = x + 48 + i * (cw + 24)
        g.append(r(cx, 120, cw, 168, WHITE, rx=16, stroke=YEL if active else BORD, sw=2 if active else 1))
        g.append(r(cx + 16, 138, cw - 32, 96, bg, rx=10))
        g.append(r(cx + 30, 154, 70, 64, a2, rx=6, op=0.35))
        g.append(r(cx + 112, 154, cw - 158, 12, a1, rx=4))
        g.append(bar(cx + 112, 176, cw - 180, 8, CHAR if name == "light" else WHITE, 0.28))
        g.append(bar(cx + 112, 192, cw - 200, 8, CHAR if name == "light" else WHITE, 0.28))
        g.append(t(cx + 20, 268, name, 15, CHAR, 700))
        if active:
            g.append(r(cx + cw - 92, 252, 72, 22, YEL, rx=999))
            g.append(t(cx + cw - 56, 268, "in use", 11, CHAR, 700, "middle"))
    g.append(r(x + 48, 312, W - x - 96, 56, G50, rx=12, stroke=BORD))
    g.append(t(x + 70, 346, "import a custom theme from a file", 14, CHAR, 600))
    g.append(t(W - 70, 346, "choose file", 13, BLUE, 600, "end"))
    # language
    g.append(t(x + 48, 420, "interface language", 19, CHAR, 700))
    g.append(t(x + 48, 448, "64 languages ship with the app", 14, MUT))
    langs = ["English", "Türkçe", "Deutsch", "Français", "Español", "Português", "Nederlands",
             "Polski", "Čeština", "Русский", "Українська", "العربية", "فارسی", "हिन्दी",
             "বাংলা", "ไทย", "日本語", "한국어", "中文", "Bahasa Indonesia", "Kiswahili", "Norsk"]
    px, py = x + 48, 476
    for lg in langs:
        w = 24 + len(tr(lg)) * 8
        if px + w > W - 48:
            px = x + 48
            py += 44
        if py > IH - 40:
            break
        active = lg == "English"
        g.append(r(px, py, w, 34, CREAM if active else G50, rx=999, stroke=YEL if active else BORD))
        g.append(t(px + w / 2, py + 22, lg, 13, CHAR, 700 if active else 400, "middle"))
        px += w + 12
    return window("\n".join(g), "screenshot: themes and languages in settings")


def make_keyboard():
    g = [sidebar(active="Shortcuts", items=[("General", ""), ("Accounts", ""), ("Appearance", ""),
                                            ("Shortcuts", ""), ("Privacy", "")], title="settings")]
    x = 280
    g.append(r(x, 0, W - x, IH, WHITE))
    g.append(t(x + 48, 56, "keyboard shortcuts", 26, CHAR, 700))
    g.append(t(x + 48, 90, "every shortcut can be rebound or switched off, one by one.", 15, MUT))
    groups = [
        ("MAIL ACTIONS", [("new message", ["Ctrl", "N"]), ("reply", ["Ctrl", "R"]),
                          ("reply all", ["Ctrl", "Shift", "R"]), ("forward", ["Ctrl", "Shift", "F"]),
                          ("archive", ["E"]), ("toggle read", ["Ctrl", "U"])]),
        ("NAVIGATION & APP", [("search", ["Ctrl", "F"]), ("sync now", ["F5"]),
                              ("send", ["Ctrl", "Enter"]), ("save draft", ["Ctrl", "S"]),
                              ("settings", ["Ctrl", ","]), ("close tab", ["Ctrl", "W"])]),
    ]
    colw = (W - x - 128) / 2
    for gi, (gname, rows) in enumerate(groups):
        cx = x + 48 + gi * (colw + 32)
        g.append(t(cx, 140, gname, 11, MUT, 700))
        y = 160
        for name, keys in rows:
            g.append(r(cx, y, colw, 56, WHITE, rx=12, stroke=BORD))
            g.append(t(cx + 20, y + 34, name, 15, CHAR, 500))
            kx = cx + colw - 20
            for k in reversed(keys):
                kw = 22 + len(k) * 9
                kx -= kw
                g.append(r(kx, y + 14, kw, 28, G50, rx=8, stroke=BORD))
                g.append(t(kx + kw / 2, y + 33, k, 12, CHAR, 700, "middle"))
                kx -= 8
            y += 66
        # toggle row
        g.append(r(cx, y + 8, colw, 56, G50, rx=12, stroke=BORD))
        g.append(t(cx + 20, y + 42, "rebind or switch off", 14, CHAR, 600))
        g.append(r(cx + colw - 76, y + 25, 52, 26, YEL, rx=999))
        g.append(c(cx + colw - 38, y + 38, 10, WHITE))
    return window("\n".join(g), "screenshot: rebinding shortcuts")


def make_privacy():
    g = [sidebar(active="Privacy", items=[("General", ""), ("Accounts", ""), ("Appearance", ""),
                                          ("Shortcuts", ""), ("Privacy", "")], title="settings")]
    x = 280
    g.append(r(x, 0, W - x, IH, WHITE))
    g.append(t(x + 48, 56, "privacy & security", 26, CHAR, 700))
    g.append(t(x + 48, 90, "nothing here talks to a guvercin server, because there isn't one.", 15, MUT))
    rows = [
        ("local data encryption", "always on — cannot be switched off", "locked"),
        ("credentials in the encrypted database", "never stored in plain text", "locked"),
        ("load remote images automatically", "off — a message you open tells the sender nothing", "off"),
        ("sender avatars from third parties", "resolved when a message is displayed", "on"),
        ("analytics and telemetry", "not present in this application", "none"),
        ("crash reporting", "not present in this application", "none"),
    ]
    y = 130
    for name, sub, state in rows:
        g.append(r(x + 48, y, W - x - 96, 76, WHITE, rx=14, stroke=BORD))
        g.append(t(x + 72, y + 32, name, 15, CHAR, 600))
        g.append(t(x + 72, y + 55, sub, 13, MUT))
        if state == "on":
            g.append(r(W - 128, y + 24, 52, 28, YEL, rx=999))
            g.append(c(W - 90, y + 38, 11, WHITE))
        elif state == "off":
            g.append(r(W - 128, y + 24, 52, 28, G50, rx=999, stroke=BORD))
            g.append(c(W - 114, y + 38, 11, WHITE))
        elif state == "locked":
            g.append(r(W - 176, y + 25, 100, 26, CREAM, rx=999, stroke=YEL))
            g.append(t(W - 126, y + 43, "always on", 12, CHAR, 700, "middle"))
        else:
            g.append(r(W - 158, y + 25, 82, 26, G50, rx=999, stroke=BORD))
            g.append(t(W - 117, y + 43, "none", 12, MUT, 700, "middle"))
        y += 88
    g.append(r(x + 48, y + 12, W - x - 96, 96, CREAM, rx=16, op=0.7))
    g.append(t(x + 72, y + 50, "uninstall guvercin", 15, CHAR, 700))
    g.append(t(x + 72, y + 76, "choose whether your local data is erased or kept for a reinstall", 13, CHAR, 500))
    return window("\n".join(g), "screenshot: privacy settings")


BUILD = {
    "shot-mail.svg": make_mail,
    "shot-offline.svg": make_offline,
    "shot-composer.svg": make_composer,
    "shot-signin.svg": make_signin,
    "shot-calendar.svg": make_calendar,
    "shot-contacts.svg": make_contacts,
    "shot-tasks.svg": make_tasks,
    "shot-appearance.svg": make_appearance,
    "shot-keyboard.svg": make_keyboard,
    "shot-privacy.svg": make_privacy,
}

# The Turkish interface, so a visitor on /tr/ sees a Turkish app. Keys are the
# English strings above; anything missing simply stays as it is (names, file
# names, addresses and the Ctrl keys are the same in both).
TURKISH = {
    # chrome and sidebar
    "MAILBOXES": "POSTA KUTULARI", "LABELS": "ETİKETLER",
    "Inbox": "Gelen kutusu", "Drafts": "Taslaklar", "Sent": "Gönderilen",
    "Archive": "Arşiv", "Spam": "Gereksiz", "Trash": "Çöp",
    "work": "iş", "family": "aile", "newsletters": "bültenler",
    "search your mail": "postanda ara", "search contacts": "kişilerde ara",
    # reading pane
    "reply": "yanıtla", "reply all": "tümünü yanıtla", "forward": "ilet",
    "archive": "arşivle", "to me · 10:24": "bana · 10:24",
    # message rows
    "the venue is confirmed for the 14th": "mekân 14'ü için kesinleşti",
    "nightly build passed on all platforms": "gecelik derleme tüm platformlarda geçti",
    "your monthly summary is ready": "aylık özetin hazır",
    "re: translation strings for Catalan": "ynt: Katalanca çeviri metinleri",
    "photos from the weekend": "hafta sonundan fotoğraflar",
    "invoice for June": "haziran faturası",
    "your package has shipped": "kargon yola çıktı",
    "mum": "annem",
    # composer
    "list": "liste", "quote": "alıntı", "link": "bağlantı", "image": "görsel",
    "code": "kod", "to": "kime", "cc": "bilgi", "subject": "konu",
    "re: the venue on the 14th": "ynt: 14'ündeki mekân",
    "drop files here": "dosyaları buraya bırak", "send": "gönder",
    "save draft": "taslağı kaydet", "Ctrl+Enter to send": "göndermek için Ctrl+Enter",
    # sign-in
    "add an account": "hesap ekle",
    "guvercin will try to find your server settings for you.":
        "guvercin sunucu ayarlarını senin için bulmayı dener.",
    "continue with Google": "Google ile devam et", "or": "ya da",
    "email address": "e-posta adresi", "password": "parola",
    "detected: imap.example.com : 993 (SSL)": "bulundu: imap.example.com : 993 (SSL)",
    "smtp.example.com : 465 (SSL) — change manually":
        "smtp.example.com : 465 (SSL) — elle değiştir",
    "add account": "hesabı ekle",
    # calendar
    "Calendar": "Takvim", "calendars": "takvimler", "July 2026": "Temmuz 2026",
    "day": "gün", "week": "hafta", "month": "ay",
    "mon": "pzt", "tue": "sal", "wed": "çar", "thu": "per", "fri": "cum",
    "sat": "cmt", "sun": "paz",
    "birthdays": "doğum günleri", "holidays TR": "resmî tatiller",
    "team sync": "ekip toplantısı", "dentist": "dişçi", "release 0.1.0": "0.1.0 sürümü",
    "review": "gözden geçirme", "flight": "uçuş", "venue visit": "mekân ziyareti",
    "standup": "günlük toplantı", "mum's birthday": "annemin doğum günü",
    "translation call": "çeviri görüşmesi", "retro": "retro",
    # contacts
    "Contacts": "Kişiler", "All contacts": "Tüm kişiler", "contacts": "kişiler",
    "address book": "adres defteri", "phone": "telefon", "company": "şirket",
    "lists": "listeler", "note": "not",
    "prefers email over calls": "aramak yerine e-posta tercih ediyor",
    "export vCard": "vCard dışa aktar", "import vCard": "vCard içe aktar",
    # tasks
    "Tasks": "Görevler", "tasks": "görevler",
    "clear completed": "tamamlananları temizle",
    "today": "bugün", "this week": "bu hafta", "someday": "bir gün",
    "due today": "bugün", "done": "bitti",
    "reply to Ayşe about the venue": "Ayşe'ye mekân için dön",
    "push translation fix": "çeviri düzeltmesini gönder",
    "book the flight": "uçuşu al", "call the bank": "bankayı ara",
    "write release notes for 0.1.0": "0.1.0 sürüm notlarını yaz",
    "test the .rpm build": ".rpm paketini dene",
    "update the FAQ page": "SSS sayfasını güncelle",
    "archive June invoices": "haziran faturalarını arşivle",
    "look at PGP libraries": "PGP kütüphanelerine bak",
    "sketch the mobile companion": "mobil uygulamayı taslakla",
    "try Fedora 41 build": "Fedora 41 paketini dene",
    "tidy the locales folder": "locales klasörünü topla",
    # settings
    "General": "Genel", "Accounts": "Hesaplar", "Appearance": "Görünüm",
    "Shortcuts": "Kısayollar", "Privacy": "Gizlilik", "settings": "ayarlar",
    "appearance": "görünüm",
    "themes apply per account, and follow the system if you want them to.":
        "temalar hesap başına uygulanır, istersen sistemi de izleyebilir.",
    "light": "açık", "dark": "koyu", "follow system": "sistemi izle",
    "in use": "kullanımda",
    "import a custom theme from a file": "dosyadan özel bir tema içe aktar",
    "choose file": "dosya seç",
    "interface language": "arayüz dili",
    "64 languages ship with the app": "uygulama 64 dille geliyor",
    "keyboard shortcuts": "klavye kısayolları",
    "every shortcut can be rebound or switched off, one by one.":
        "her kısayol tek tek yeniden atanabilir ya da kapatılabilir.",
    "MAIL ACTIONS": "POSTA İŞLEMLERİ", "NAVIGATION & APP": "GEZİNME VE UYGULAMA",
    "new message": "yeni ileti", "toggle read": "okundu işaretle",
    "search": "ara", "sync now": "şimdi eşitle", "settings": "ayarlar",
    "close tab": "sekmeyi kapat", "rebind or switch off": "yeniden ata ya da kapat",
    "privacy & security": "gizlilik ve güvenlik",
    "nothing here talks to a guvercin server, because there isn't one.":
        "buradaki hiçbir şey bir guvercin sunucusuyla konuşmaz, çünkü öyle bir şey yok.",
    "local data encryption": "yerel veri şifrelemesi",
    "always on — cannot be switched off": "her zaman açık — kapatılamaz",
    "always on": "her zaman açık",
    "credentials in the encrypted database": "kimlik bilgileri şifreli veritabanında",
    "never stored in plain text": "hiçbir zaman düz metin olarak saklanmaz",
    "load remote images automatically": "uzak görselleri otomatik yükle",
    "off — a message you open tells the sender nothing":
        "kapalı — açtığın ileti gönderene hiçbir şey söylemez",
    "sender avatars from third parties": "üçüncü taraflardan gönderen avatarları",
    "resolved when a message is displayed": "ileti görüntülenirken çözülür",
    "analytics and telemetry": "analitik ve telemetri",
    "not present in this application": "bu uygulamada mevcut değil",
    "crash reporting": "çökme raporlama", "none": "yok",
    "uninstall guvercin": "guvercin'i kaldır",
    "choose whether your local data is erased or kept for a reinstall":
        "yerel verinin silinmesini mi yoksa yeniden kurulum için saklanmasını mı seç",
    # offline banner
    "offline — showing your local copy. 3 actions queued, they will send when you reconnect.":
        "çevrimdışı — yerel kopyan gösteriliyor. 3 işlem kuyrukta, bağlanınca gönderilecek.",
    # captions
    "screenshot: mail view — folder tree, message list and reading pane":
        "ekran görüntüsü: posta görünümü — klasör ağacı, ileti listesi ve okuma bölmesi",
    "screenshot: reading mail with no connection":
        "ekran görüntüsü: bağlantı olmadan posta okuma",
    "screenshot: the compose window, popped out":
        "ekran görüntüsü: ayrı pencereye çıkarılmış yazma ekranı",
    "screenshot: adding an account": "ekran görüntüsü: hesap ekleme",
    "screenshot: the built-in calendar": "ekran görüntüsü: yerleşik takvim",
    "screenshot: contacts and lists": "ekran görüntüsü: kişiler ve listeler",
    "screenshot: the task panel": "ekran görüntüsü: görev paneli",
    "screenshot: themes and languages in settings":
        "ekran görüntüsü: ayarlarda temalar ve diller",
    "screenshot: rebinding shortcuts": "ekran görüntüsü: kısayolları yeniden atama",
    "screenshot: privacy settings": "ekran görüntüsü: gizlilik ayarları",
}


def render(directory, table):
    os.makedirs(directory, exist_ok=True)
    TR.clear()
    TR.update(table)
    for name, fn in BUILD.items():
        path = os.path.join(directory, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(fn())
    print(f"  {directory}: {len(BUILD)} files")


if __name__ == "__main__":
    # One shared set of mockups, used by both languages, so there is only one
    # place to swap in real screenshots later. The TURKISH table above stays
    # ready if localised mockups are ever wanted: render(OUT + "/tr", TURKISH).
    render(OUT, {})
