# Approaching Interviews and Solving Case Studies

A 65-slide deck for the Rethink Systems MPM cohort, Session 03, with
Shravan Tickoo. Self-contained single HTML file, no build step needed to
present. Live at https://attyrockstar.github.io/rethink-interviews-deck/

## What is in it

Six parts: what hiring managers score, getting PM experience before the
title, the pre-interview assignment, the resume, research and the
interview, and the choice between offers. The 2026 India figures (PM
openings, salaries, MBA fees, referral rates, Groww and edtech numbers)
are sourced on the last slide and stamped "as of September 2026".

## Presenting

- `F` toggles full screen
- Right arrow, space, click or swipe advances; left arrow goes back
- `Home` and `End` jump to the first and last slide
- The slide number is in the URL: `.../rethink-interviews-deck/#24`
- On-screen controls fade after a couple of seconds

## Editing

The deck is assembled from `src/*.html` by `src/build.py`. Edit the part
files, then:

```bash
python3 src/build.py
```

That rewrites `index.html`. The three dialogue comics, the 100-dot grid
and the 90-second timeline are generated in `build.py` from data, so
change the lines there rather than in the SVG.

To refresh a figure, change it on its slide and on the sources slide
(`src/40-choice.html`, last table).

## Brand

Palette and type are lifted from rethinksystems.in. Edit the `:root`
block at the top of `src/00-head.html`:

```css
:root{
  --ink:       #01061B;   /* Rethink navy: dark slides, body text on light */
  --paper:     #F3F6FF;   /* light slide background                        */
  --accent:    #3D5BF1;   /* Rethink blue on light slides                  */
  --accent-dk: #84ADFF;   /* Rethink blue on navy slides                   */
  --strong:    #0E7A55;   /* the "do this" colour                          */
  --weak:      #B93A22;   /* the "not this" colour                         */
}
```

Figtree loads from Google Fonts. With no internet the deck falls back to
system sans and still holds its layout.

## Deploying

GitHub Pages serves `main` from the repo root. Push and it updates in
about a minute.

```bash
git add -A && git commit -m "..." && git push
```

## Illustrations

All comics and diagrams are original inline SVG. No image files, no
third-party artwork, so the repo is safe to keep public.
