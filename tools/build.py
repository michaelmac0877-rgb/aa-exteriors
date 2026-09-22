#!/usr/bin/env python3
"""
A&A Exteriors — static page generator.

Builds the service, city, and projects pages from content modules so the
header, footer, schema, and CTA stay identical everywhere. Output is plain
static HTML committed to the repo; Cloudflare Pages just serves it. There is
no build step at deploy time.

    python3 tools/build.py

Add or edit a page by editing tools/content_core.py or tools/content_cities.py
and re-running. Nothing else needs to change.
"""
import os, re, sys, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

BASE   = "https://aa-exteriors.com"
PHONE  = "469-496-7500"
TEL    = "+14694967500"
EMAIL  = "michael@aa-exteriors.com"
STREET = "3526 Lakeview Pkwy #B159"
CITY   = "Rowlett"
REGION = "TX"
ZIP    = "75088"

NAV = [("/", "Home"), ("/services", "Services"), ("/projects", "Projects"),
       ("/about", "About"), ("/estimate", "Free Estimate")]

FOOTER_SERVICES = [
    ("/concrete-patios-stamped-concrete", "Stamped Concrete Patios"),
    ("/concrete-driveways",               "Concrete Driveways"),
    ("/pool-deck-resurfacing",            "Pool Deck Resurfacing"),
    ("/retaining-walls",                  "Retaining Walls"),
    ("/services",                         "All Services"),
]

PHONE_SVG = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
  'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 '
  '19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 '
  '1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 '
  '2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>')
PIN_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
  'stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>')
MAIL_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
  'stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>')


def head(p):
    canon = BASE + p["url"]
    og_img = BASE + p.get("hero_image", "/images/work-stamped.jpg")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p['title']}</title>
  <meta name="description" content="{p['description']}" />
  <link rel="canonical" href="{canon}" />
  <meta name="theme-color" content="#1f2a24" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{p['title']}" />
  <meta property="og:description" content="{p['description']}" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:image" content="{og_img}" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="icon" type="image/png" href="/favicon.png" />
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <link rel="stylesheet" href="/css/styles.css" />
{schema_block(p)}</head>
<body>
"""


def schema_block(p):
    """LocalBusiness + Service + Breadcrumb + optional FAQ, as JSON-LD."""
    import json
    biz = {
        "@type": "GeneralContractor",
        "@id": BASE + "/#business",
        "name": "A&A Exteriors",
        "url": BASE + "/",
        "telephone": PHONE,
        "email": EMAIL,
        "image": BASE + "/images/logo.png",
        "address": {"@type": "PostalAddress", "streetAddress": STREET,
                    "addressLocality": CITY, "addressRegion": REGION,
                    "postalCode": ZIP, "addressCountry": "US"},
        "areaServed": [{"@type": "City", "name": c} for c in
                       ["Rowlett", "Rockwall", "Heath", "Garland", "Wylie",
                        "Sachse", "Royse City", "Fate", "Forney"]],
    }
    graph = [biz]
    crumbs = [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"}]
    for i, (u, n) in enumerate(p.get("breadcrumbs", []), start=2):
        crumbs.append({"@type": "ListItem", "position": i, "name": n, "item": BASE + u})
    graph.append({"@type": "BreadcrumbList", "itemListElement": crumbs})
    if p.get("service_type"):
        graph.append({
            "@type": "Service", "name": p["service_type"],
            "serviceType": p["service_type"],
            "provider": {"@id": BASE + "/#business"},
            "areaServed": p.get("area_served", "Dallas-Fort Worth, TX"),
            "url": BASE + p["url"],
        })
    if p.get("faqs"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
            for q, a in p["faqs"]]})
    data = {"@context": "https://schema.org", "@graph": graph}
    return ('  <script type="application/ld+json">\n  '
            + json.dumps(data, indent=2).replace("\n", "\n  ") + "\n  </script>\n")


def header(active):
    def li(u, n):
        cls = ' class="is-active"' if u == active else ""
        return '        <li><a href="%s"%s>%s</a></li>\n' % (u, cls, n)
    links = "".join(li(u, n) for u, n in NAV)
    return f"""
  <!-- ===================== HEADER ===================== -->
  <header class="site-header">
    <div class="container nav">
      <a class="brand" href="/" aria-label="A&amp;A Exteriors home">
        <img src="/images/logo.png" alt="A&amp;A Exteriors — concrete and hardscape contractor in Rowlett, TX" class="brand__logo" />
      </a>
      <button class="nav__toggle" aria-label="Toggle menu" aria-controls="navLinks" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
      <ul class="nav__links" id="navLinks">
{links}      </ul>
      <div class="nav__cta">
        <a class="nav__phone" href="tel:{TEL}">{PHONE_SVG}
          {PHONE}
        </a>
        <a class="btn btn--primary" href="/estimate">Free Estimate</a>
      </div>
    </div>
  </header>
"""


def breadcrumbs(items):
    if not items:
        return ""
    parts = ['<a href="/">Home</a>']
    for i, (u, n) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f"<span aria-current=\"page\">{n}</span>")
        else:
            parts.append(f'<a href="{u}">{n}</a>')
    return ('\n  <nav class="breadcrumb" aria-label="Breadcrumb"><div class="container">'
            + ' <span class="sep">/</span> '.join(parts) + "</div></nav>\n")


def cta_band(heading, sub):
    return f"""
  <!-- ===================== CTA ===================== -->
  <section class="section cta-band">
    <div class="container">
      <h2 class="reveal">{heading}</h2>
      <p class="reveal">{sub}</p>
      <a class="btn btn--light reveal" href="/estimate">Request Your Free Estimate</a>
      <p style="margin-top:1.1rem;color:rgba(255,255,255,.9);">or call <a href="tel:{TEL}" style="color:#fff;text-decoration:underline;">{PHONE}</a></p>
    </div>
  </section>
"""


def footer():
    svc = "".join(f'            <li><a href="{u}">{n}</a></li>\n' for u, n in FOOTER_SERVICES)
    return f"""
  <!-- ===================== FOOTER ===================== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid footer-grid--4">
        <div class="footer-brand">
          <div class="footer-logo"><img src="/images/logo.png" alt="A&amp;A Exteriors" /></div>
          <p>Family-owned concrete and hardscape construction, serving Rowlett, Rockwall, Heath, Garland, Wylie, Sachse and the greater Dallas&ndash;Fort Worth Metroplex.</p>
          <p style="font-size:.9rem;color:rgba(255,255,255,.55);">Fully insured. Free on-site estimates.</p>
        </div>
        <div>
          <h4>Services</h4>
          <ul class="footer-links">
{svc}          </ul>
        </div>
        <div>
          <h4>Explore</h4>
          <ul class="footer-links">
            <li><a href="/">Home</a></li>
            <li><a href="/projects">Our Projects</a></li>
            <li><a href="/about">About Us</a></li>
            <li><a href="/estimate">Free Estimate</a></li>
          </ul>
        </div>
        <div>
          <h4>Get In Touch</h4>
          <ul class="footer-contact">
            <li>{PIN_SVG}<span>{STREET}<br/>{CITY}, {REGION} {ZIP}</span></li>
            <li>{PHONE_SVG.replace('width="18" height="18" ', '')}<a href="tel:{TEL}">{PHONE}</a></li>
            <li>{MAIL_SVG}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; <span data-year>2026</span> A&amp;A Exteriors. All rights reserved.</span>
        <span>Rowlett, TX &middot; Serving Rockwall, Heath &amp; the DFW Metroplex</span>
      </div>
    </div>
  </footer>

  <script src="/js/main.js"></script>
</body>
</html>
"""


def hero(p):
    img = p.get("hero_image", "/images/work-stamped.jpg")
    return f"""
  <section class="page-hero" style="background-image:linear-gradient(180deg,rgba(20,28,23,.62),rgba(20,28,23,.80)),url('{img}');">
    <div class="container">
      <span class="eyebrow">{p['eyebrow']}</span>
      <h1>{p['h1']}</h1>
      <p class="lead">{p['intro']}</p>
      <div class="hero__actions">
        <a class="btn btn--primary" href="/estimate">Get a Free Estimate</a>
        <a class="btn btn--onDark" href="tel:{TEL}">Call {PHONE}</a>
      </div>
    </div>
  </section>
"""


def faq_block(faqs):
    if not faqs:
        return ""
    items = "".join(
        f"""        <details class="faq-item">
          <summary>{q}</summary>
          <div class="faq-a">{a}</div>
        </details>\n""" for q, a in faqs)
    return f"""
  <section class="section" style="background:var(--cream-2);">
    <div class="container" style="max-width:820px;">
      <div class="section-head reveal" style="margin-bottom:1.6rem;">
        <span class="eyebrow">Common Questions</span>
        <h2>Questions we get asked</h2>
      </div>
      <div class="reveal">
{items}      </div>
    </div>
  </section>
"""


def related_block(links, heading="Explore more"):
    if not links:
        return ""
    cards = "".join(
        f"""        <a class="related-card reveal" href="{u}">
          <h3>{n}</h3>
          <p>{d}</p>
          <span class="related-go">View page &rarr;</span>
        </a>\n""" for u, n, d in links)
    return f"""
  <section class="section">
    <div class="container">
      <div class="section-head center reveal"><h2>{heading}</h2></div>
      <div class="related-grid">
{cards}      </div>
    </div>
  </section>
"""


def render(p):
    out = [head(p), header(p.get("nav_active", "")), breadcrumbs(p.get("breadcrumbs")), hero(p)]
    out.append(p["body"])
    out.append(faq_block(p.get("faqs")))
    out.append(related_block(p.get("related", []), p.get("related_heading", "Explore more")))
    out.append(cta_band(p.get("cta_h", "Ready to get started?"),
                        p.get("cta_p", "Free, no-obligation estimates across Rowlett, Rockwall, Heath and the DFW area.")))
    out.append(footer())
    return "".join(out)


def main():
    from content_core import PAGES as CORE
    from content_cities import PAGES as CITIES
    pages = CORE + CITIES
    for p in pages:
        path = os.path.join(ROOT, p["url"].strip("/") + ".html")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(render(p))
        words = len(re.sub(r"<[^>]+>", " ", p["body"]).split())
        print(f"  {p['url']:<46} {words:>5} words")
    write_sitemap(pages)
    write_robots()


def write_sitemap(pages):
    statics = ["/", "/services", "/about", "/estimate"]
    urls = statics + [p["url"] for p in pages]
    body = "".join(
        f"  <url>\n    <loc>{BASE}{u}</loc>\n"
        f"    <priority>{'1.0' if u == '/' else '0.8'}</priority>\n  </url>\n"
        for u in dict.fromkeys(urls))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + body + "</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(xml)
    print(f"  sitemap.xml                                    {len(list(dict.fromkeys(urls)))} URLs")


def write_robots():
    txt = ("User-agent: *\n"
           "Allow: /\n\n"
           f"Sitemap: {BASE}/sitemap.xml\n")
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write(txt)
    print("  robots.txt                                     written")


if __name__ == "__main__":
    main()
