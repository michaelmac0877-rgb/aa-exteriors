# A&A Exteriors — Website

A clean, fast, mobile-friendly marketing site for **A&A Exteriors**, a hardscaping
and outdoor-living company in Rowlett, TX serving the greater DFW area.

Built as a static site (plain HTML/CSS/JS) — no build step, no dependencies — so
it's easy to host, cheap (free on GitHub Pages), and simple to maintain.

## Pages
| File            | Purpose                                                        |
|-----------------|----------------------------------------------------------------|
| `index.html`    | Home — hero, services overview, why-us, gallery, call-to-action|
| `services.html` | Detailed breakdown of all 7 services                           |
| `about.html`    | Company story + core values (placeholder text to be replaced)  |
| `estimate.html` | Free-estimate request form (Formspree)                         |

## Services featured
Outdoor Lighting · Fire Pits · Retaining Walls · Pergolas · Fences ·
Concrete Work (walkways, patios & additions) · Outdoor Kitchens

---

## ✅ Setup checklist (do these to go live)

### 1. Connect the estimate form to Formspree
1. Sign up (free) at <https://formspree.io> using **michael@aa-exteriors.com**.
2. Create a new form and copy its endpoint — it looks like
   `https://formspree.io/f/abcdwxyz`.
3. Open `estimate.html`, find `YOUR_FORM_ID`, and replace the whole action URL
   with your real endpoint.
4. Submit the form once yourself and confirm the first email (Formspree asks you
   to verify the address on the first submission).

Until this is done, the form politely tells visitors it isn't connected yet.

### 2. Add your photos
Drop images into the `images/` folder using the file names listed in
[`images/README.md`](images/README.md). Placeholders show until you do.

### 3. Fill in the About page
Send me your **company history** and **core values** and I'll replace the
placeholder text in `about.html`. (Placeholders are clearly marked with notes.)

### 4. Publish with GitHub Pages
1. Push this repo to GitHub (already at `michaelmac0877-rgb/aa-exteriors`).
2. On GitHub: **Settings → Pages**.
3. Under "Build and deployment", set **Source: Deploy from a branch**,
   **Branch: `main`**, folder **`/ (root)`**, then **Save**.
4. Your site goes live at `https://michaelmac0877-rgb.github.io/aa-exteriors/`
   within a minute or two.
5. (Optional) To use a custom domain like `aa-exteriors.com`, add it under
   Settings → Pages → Custom domain and point your DNS to GitHub. I can walk you
   through this.

---

## Editing the contact info
Phone, email, and address appear in the header/footer of every page and on the
estimate page. Current values:

- **Phone:** 469-496-7500
- **Email:** michael@aa-exteriors.com
- **Address:** 3526 Lakeview Pkwy #B159, Rowlett, TX 75088

## Preview locally
Just open `index.html` in a browser — or, for the form/fetch to behave exactly
like production, run a tiny local server:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Tech notes
- No frameworks. Fonts via Google Fonts (Fraunces + Inter).
- Icons are inline SVG. Colors/spacing are CSS variables in `css/styles.css`.
- `.nojekyll` is included so GitHub Pages serves all files as-is.
