#!/usr/bin/env python3
"""Assemble index.html from src/*.html and generate the data-driven SVGs.

Run:  python3 src/build.py
The comics, the dot grid and the 90-second timeline are computed here so their
geometry is measured, not eyeballed. Everything else is hand-authored HTML.
"""
import glob, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")

# ---------- 10x10 dot grid: 71 filled, 29 outlined ----------
def dots(filled=71, total=100, cols=10, cell=32, r=11):
    out = []
    for k in range(total):
        cx = 16 + (k % cols) * cell
        cy = 16 + (k // cols) * cell
        cls = "dot" if k < filled else "dot off"
        out.append(f'<circle class="{cls}" cx="{cx}" cy="{cy}" r="{r}"/>')
    return "\n      ".join(out)

# ---------- dialogue comic: two figures, alternating speech bubbles ----------
# Speech text is 22px Figtree 500. Measured average advance ~11.1px per character.
CHAR_W = 11.1
PAD = 22
LINE_H = 30        # text line height inside a bubble
GAP = 16           # vertical gap between bubbles
FIG_W, FIG_H = 100, 217          # figure box (symbol is 60x130, scaled)
LEFT_X, RIGHT_X = 150, 954       # bubble column bounds (figures stand outside)
MAX_CH = int((RIGHT_X - LEFT_X - 2 * PAD) / CHAR_W)   # chars per line before wrapping

def wrap(text, n=MAX_CH):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) > n:
            lines.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur: lines.append(cur)
    return lines

def comic(lines, left_label, right_label, left_fig="fig", right_fig="fig-sad", aria=""):
    """lines: list of (side, text) where side is 'L' or 'R'."""
    y = 10
    parts = []
    for side, text in lines:
        ls = wrap(text)
        w = int(max(len(l) for l in ls) * CHAR_W + 2 * PAD)
        h = LINE_H * len(ls) + 24
        if side == "L":
            x = LEFT_X
            tail = f'<path class="bub" d="M{x} {y+16} l-16 9 l16 9"/>'
            cls = "bub"
        else:
            x = RIGHT_X - w
            tail = f'<path class="bub hi" d="M{x+w} {y+16} l16 9 l-16 9"/>'
            cls = "bub hi"
        parts.append(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="9"/>')
        parts.append(tail)
        for k, l in enumerate(ls):
            parts.append(f'<text class="say" x="{x+PAD}" y="{y+33+k*LINE_H}">{html.escape(l)}</text>')
        y += h + GAP
    fig_y = y - 6
    total_h = fig_y + FIG_H + 30
    parts.append(f'<use href="#{left_fig}" class="ln solid" x="18" y="{fig_y}" width="{FIG_W}" height="{FIG_H}"/>')
    parts.append(f'<text class="lbl dim" x="0" y="{fig_y+FIG_H+24}">{html.escape(left_label)}</text>')
    parts.append(f'<use href="#{right_fig}" class="ln solid" x="{1104-18-FIG_W}" y="{fig_y}" width="{FIG_W}" height="{FIG_H}"/>')
    parts.append(f'<text class="lbl dim" x="1104" y="{fig_y+FIG_H+24}" text-anchor="end">{html.escape(right_label)}</text>')
    body = "\n      ".join(parts)
    return (f'<svg class="illo" viewBox="0 0 1104 {total_h}" role="img" aria-label="{html.escape(aria)}" style="max-height:540px;width:auto;margin:0 auto">\n'
            f'      {body}\n    </svg>')

COMICS = {
    "noeng": comic([
        ("L", "Your first project is to figure out our Tier-2 city strategy."),
        ("R", "Great! How many engineers do I get to build it?"),
        ("L", "Exactly zero. You need to convince the platform PM to put your features on his roadmap."),
        ("R", "Hmm. How do I do that?"),
        ("L", "Didn't we tell you about the wrestling match?"),
    ], "Director of PMs", "You, week one", "fig-up", "fig",
       "A director of product managers assigns a strategy with zero engineers; the new PM is told to negotiate with a peer for roadmap space."),
    "p3bug": comic([
        ("L", "We're ready to ship on the date we committed. As per our inflated schedule."),
        ("R", "Wait. There's a misspelling on the main page. We need to fix it before shipping."),
        ("L", "I know. But that means rebuilding the binaries. Misspellings are P3 bugs, not launch-gating."),
        ("R", "But in this case THE NAME OF THE PRODUCT is misspelled. Can't we do something?"),
        ("L", "You have two options. One, blame QA, they missed it. Two, change the product name."),
    ], "Engineering manager", "You", "fig", "fig-sad",
       "An engineering manager refuses to fix a misspelled product name before launch, offering to blame QA or rename the product instead."),
    "mrd": comic([
        ("L", "Welcome to the team, Rohan. Your job is to deliver this MRD to engineering."),
        ("R", "Okay. Just curious, why won't the marketing managers do it?"),
        ("L", "The engineers won't get into the same room with them. That's why we hired you."),
        ("R", "Okay. Can I review the requirements and make changes to the document?"),
        ("L", "Now that you mention it, yes. We really need a table of contents in the doc."),
    ], "VP Marketing", "You, the new PM", "fig-up", "fig-sad",
       "A VP of marketing hires a PM to carry a requirements document to engineers who will not meet marketing, and lets the PM add a table of contents."),
}

# ---------- 90-second "tell me about yourself" timeline ----------
def timeline():
    W = 1104; px = W / 90.0
    beats = [
        (0, 20,  "Problem",  "the problem you care about, at the scale you think at"),
        (20, 50, "Place",    "why the companies you chose made sense for that problem"),
        (50, 75, "Path",     "the through-line in your moves, owned, not apologised for"),
        (75, 90, "Why now",  "why this role is the next step. Then stop."),
    ]
    parts = []
    y0 = 78
    for k, (a, b, name, desc) in enumerate(beats):
        x = a * px; w = (b - a) * px
        cls = "hif" if k % 2 == 0 else "sf"
        op = "" if k % 2 == 0 else ' style="opacity:.18"'
        parts.append(f'<rect class="{cls}" x="{x:.0f}" y="{y0}" width="{w-4:.0f}" height="30" rx="4"{op}/>')
        parts.append(f'<text class="lbl b" x="{x:.0f}" y="{y0-16}">{html.escape(name)}</text>')
        parts.append(f'<text class="lbl sm" x="{x:.0f}" y="{y0+58}">{a} to {b} s</text>')
        parts.append(f'<foreignObject x="{x:.0f}" y="{y0+70}" width="{w-16:.0f}" height="70">'
                     f'<div xmlns="http://www.w3.org/1999/xhtml" style="font:400 16px/1.35 Figtree,sans-serif;opacity:.75">{html.escape(desc)}</div></foreignObject>')
    body = "\n      ".join(parts)
    return (f'<svg class="illo" viewBox="0 0 {W} 220" role="img" aria-label="A ninety second bar split into four beats: problem, place, path, why now.">\n'
            f'      {body}\n    </svg>')

def main():
    files = sorted(glob.glob(os.path.join(SRC, "*.html")))
    out = "".join(open(f, encoding="utf-8").read() for f in files)
    out = out.replace("{{DOTS}}", dots())
    out = out.replace("{{TIMELINE}}", timeline())
    for k, v in COMICS.items():
        out = out.replace("{{COMIC:%s}}" % k, v)
    assert "{{" not in out, "unreplaced token"
    dest = os.path.join(ROOT, "index.html")
    open(dest, "w", encoding="utf-8").write(out)
    print("wrote", dest, len(out), "bytes;", out.count('class="slide'), "slides")

if __name__ == "__main__":
    main()
