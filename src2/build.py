#!/usr/bin/env python3
"""Assemble index.html from src2/*.html. Generates the receipt's torn edge,
the 100-dot waffle, the seven-to-five mapping diagram and the 90-second
timeline from data.   Run: python3 src2/build.py
"""
import glob, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src2")

def receipt_clip(teeth=22, depth=14):
    pts = ["0 0", "100% 0"]
    step = 100 / teeth
    for k in range(teeth + 1):
        x = 100 - k * step
        y = "100%" if k % 2 == 0 else f"calc(100% - {depth}px)"
        pts.append(f"{x:.2f}% {y}")
    return "polygon(" + ", ".join(pts) + ")"

def waffle(filled=71):
    return "".join('<i></i>' if k < filled else '<i class="off"></i>' for k in range(100))

def mapping():
    left = ["Product sense", "Practice of PM", "Process", "Past projects", "Brain teasers", "Domain expertise", "Understanding of technology"]
    right = ["Has product sense", "Is smart", "Gets things done", "Is a culture fit", "Has technical skills"]
    edges = [(0,0),(1,0),(1,1),(2,2),(3,2),(3,3),(4,1),(5,4),(6,4)]
    W, H = 1100, 400
    ly = [22 + k * (H - 44) / 6 for k in range(7)]
    ry = [22 + k * (H - 44) / 4 for k in range(5)]
    lx, rx = 300, 800
    parts = []
    for a, b in edges:
        parts.append(f'<path d="M{lx+14} {ly[a]:.0f} C {lx+220} {ly[a]:.0f}, {rx-220} {ry[b]:.0f}, {rx-14} {ry[b]:.0f}" fill="none" stroke="#84ADFF" stroke-width="2.5" stroke-linecap="round" opacity=".75"/>')
    for k, t in enumerate(left):
        parts.append(f'<circle cx="{lx}" cy="{ly[k]:.0f}" r="7" fill="#84ADFF"/>')
        parts.append(f'<text x="{lx-22}" y="{ly[k]:.0f}" text-anchor="end" dominant-baseline="central" font-family="Figtree,sans-serif" font-size="21" font-weight="500" fill="#F3F6FF">{html.escape(t)}</text>')
    for k, t in enumerate(right):
        parts.append(f'<circle cx="{rx}" cy="{ry[k]:.0f}" r="7" fill="#3D5BF1" stroke="#84ADFF" stroke-width="2"/>')
        parts.append(f'<text x="{rx+22}" y="{ry[k]:.0f}" dominant-baseline="central" font-family="Tanker,Figtree,sans-serif" font-size="26" letter-spacing=".03em" fill="#F3F6FF">{html.escape(t.upper())}</text>')
    return (f'<svg viewBox="0 0 {W} {H}" style="width:100%;height:auto;display:block;overflow:visible" role="img" '
            f'aria-label="Seven interview question categories connected to the five attributes they score">' + "".join(parts) + '</svg>')

def timeline():
    W, H = 1100, 190
    px = W / 90
    beats = [(0,20,"Problem","the problem you care about, at the scale you think at"),
             (20,50,"Place","why the companies you chose made sense for it"),
             (50,75,"Path","the through-line in your moves, owned"),
             (75,90,"Why now","why this role is next. Then stop.")]
    parts = []
    for k,(a,b,name,desc) in enumerate(beats):
        x, w = a*px, (b-a)*px
        fill = "#3D5BF1" if k % 2 == 0 else "#84ADFF"
        parts.append(f'<rect x="{x:.0f}" y="62" width="{w-5:.0f}" height="34" rx="6" fill="{fill}"/>')
        parts.append(f'<text x="{x:.0f}" y="44" font-family="Tanker,Figtree,sans-serif" font-size="30" letter-spacing=".03em" fill="#0B1030">{name.upper()}</text>')
        parts.append(f'<text x="{x:.0f}" y="124" font-family="Figtree,sans-serif" font-size="15" fill="#4A5478">{a} to {b} s</text>')
        parts.append(f'<foreignObject x="{x:.0f}" y="134" width="{w-14:.0f}" height="60"><div xmlns="http://www.w3.org/1999/xhtml" style="font:400 16px/1.35 Figtree,sans-serif;color:#0B1030">{html.escape(desc)}</div></foreignObject>')
    return (f'<svg viewBox="0 0 {W} {H}" style="width:100%;height:auto;display:block;overflow:visible" role="img" '
            f'aria-label="A ninety second bar in four beats: problem, place, path, why now">' + "".join(parts) + '</svg>')

def main():
    files = sorted(glob.glob(os.path.join(SRC, "*.html")))
    out = "".join(open(f, encoding="utf-8").read() for f in files)
    out = out.replace("{{RECEIPT_CLIP}}", receipt_clip())
    out = out.replace("{{WAFFLE}}", waffle())
    out = out.replace("{{MAPPING}}", mapping())
    out = out.replace("{{TIMELINE}}", timeline())
    assert "{{" not in out, "unreplaced token"
    dest = os.path.join(ROOT, "index.html")
    open(dest, "w", encoding="utf-8").write(out)
    print("wrote", dest, len(out), "bytes;", out.count("<section"), "sections")

if __name__ == "__main__":
    main()
