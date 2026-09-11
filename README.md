# Approaching Interviews and Solving Case Studies

Rethink Systems, Mastering Product Management, Session 03, with Shravan
Tickoo. A scroll-down page: 27 full-screen frames that snap into place on
a laptop and read as a long page on a phone.

Live: https://attyrockstar.github.io/rethink-interviews-deck/

## Presenting

- Scroll, or use the arrow keys, space and page up/down to step frame by frame
- The numbers on the left jump to each of the six parts
- The door on the first screen opens as you scroll
- Every India figure is stamped September 2026; sources are in the
  expandable list on the last content frame

## Editing

The page is assembled from `src2/*.html` by `src2/build.py`:

```bash
python3 src2/build.py
```

That rewrites `index.html`. The receipt's torn edge, the 100-dot waffle,
the seven-to-five mapping diagram and the 90-second timeline are generated
in `build.py` from data. Everything else is hand-authored in the part files.

## Brand

Palette from rethinksystems.in, in the `:root` block at the top of
`src2/00-head.html`. Tanker (Fontshare) carries headlines and numbers,
Figtree (the site's face) carries everything else.

## Deploying

GitHub Pages serves `main` from the repo root. Push and it updates in
about a minute.

## Artwork

All artifacts (scorecard, resumes, profile card, chats, receipt, diagrams)
are HTML and inline SVG. No image files, no third-party artwork.
