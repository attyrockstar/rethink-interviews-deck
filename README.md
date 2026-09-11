# Approaching Interviews and Solving Case Studies

A 41-slide presentation deck for the Rethink Systems MPM cohort.
Self-contained single HTML file. No build step, no dependencies.

## Deploying to GitHub Pages

### Option A: entirely through the browser, no terminal needed

1. Go to https://github.com/new and create a repository.
   Name it something like `rethink-interviews-deck`. Set it to **Public**
   (GitHub Pages needs Public on free accounts). Tick
   "Add a README file" so the repo is not empty.
2. In the new repo, click **Add file** then **Upload files**.
3. Drag in `index.html` and `.nojekyll`, then click **Commit changes**.
4. Go to **Settings**, then **Pages** in the left sidebar.
5. Under "Build and deployment", set Source to **Deploy from a branch**,
   Branch to **main**, folder to **/ (root)**. Click **Save**.
6. Wait about a minute, then reload the Pages settings screen. Your URL
   will be shown at the top:
   `https://<your-username>.github.io/rethink-interviews-deck/`

### Option B: from the terminal

```bash
git init
git add index.html .nojekyll README.md
git commit -m "Add PM interviews deck"
git branch -M main
git remote add origin https://github.com/<your-username>/rethink-interviews-deck.git
git push -u origin main
```

Then follow steps 4 to 6 above to switch Pages on.

## Presenting

- `F` toggles full screen
- Right arrow, space, or click advances
- Left arrow goes back
- `Home` and `End` jump to the first and last slide
- The slide number is in the URL, so you can link straight to a slide:
  `.../rethink-interviews-deck/#24`
- The on-screen controls fade out after a couple of seconds so nothing
  sits over your slides

## Changing the brand colours

The palette is lifted from rethinksystems.in. Open `index.html` and edit
the values in the `:root` block at the top of the `<style>` tag. Nothing
else references colour directly.

```css
:root{
  --ink:       #01061B;   /* Rethink navy: dark slides, body text on light */
  --paper:     #F3F6FF;   /* light slide background                        */
  --accent:    #3D5BF1;   /* Rethink blue on light slides                  */
  --accent-dk: #84ADFF;   /* Rethink blue on navy slides                   */
  --glow:      #3D5BF1;   /* cover and divider glow                        */
  --strong:    #0E7A55;   /* the "do this" colour                          */
  --weak:      #B93A22;   /* the "not this" colour                         */
}
```

## Fonts

Figtree, the typeface used on rethinksystems.in, loads from Google Fonts.
If the room has no internet the deck falls back to system sans and still
holds its layout. The PDF export is the safer backup either way.

## Illustrations

All diagrams are original inline SVG. There are no image files and no
third-party artwork, so the repo is safe to make public.
