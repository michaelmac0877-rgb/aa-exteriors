#!/usr/bin/env python3
"""
Retrofit the four original hand-written pages (home, services, about, estimate)
so they share the generated header, footer, schema, and clean URLs.

Safe to re-run: every edit is idempotent.

    python3 tools/retrofit.py
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import build  # noqa: E402

TARGETS = {
    "index.html":    {"url": "/",          "nav": "/"},
    "services.html": {"url": "/services",  "nav": "/services"},
    "about.html":    {"url": "/about",     "nav": "/about"},
    "estimate.html": {"url": "/estimate",  "nav": "/estimate"},
}

# internal .html links -> clean URLs
LINK_MAP = [
    ('href="index.html"',    'href="/"'),
    ('href="services.html"', 'href="/services"'),
    ('href="about.html"',    'href="/about"'),
    ('href="estimate.html"', 'href="/estimate"'),
]

# repo-relative asset paths -> root-absolute (site is served at domain root)
ASSET_MAP = [
    ('href="css/styles.css"', 'href="/css/styles.css"'),
    ('src="js/main.js"',      'src="/js/main.js"'),
    ('href="favicon.png"',    'href="/favicon.png"'),
    ('href="favicon.svg"',    'href="/favicon.svg"'),
    ('src="images/',          'src="/images/'),
    ("url('images/",          "url('/images/"),
]

HEADER_RE = re.compile(
    r"\n\s*<!-- =+ HEADER =+ -->.*?</header>\n", re.S)
FOOTER_RE = re.compile(
    r"\n\s*<!-- =+ FOOTER =+ -->.*?</html>\s*", re.S)


def head_extras(url, title, desc):
    canon = build.BASE + url
    img = build.BASE + "/images/work-fireplace.jpg"
    return (
        f'  <link rel="canonical" href="{canon}" />\n'
        f'  <meta property="og:type" content="website" />\n'
        f'  <meta property="og:title" content="{title}" />\n'
        f'  <meta property="og:description" content="{desc}" />\n'
        f'  <meta property="og:url" content="{canon}" />\n'
        f'  <meta property="og:image" content="{img}" />\n'
        f'  <meta name="twitter:card" content="summary_large_image" />\n'
    )


def process(fname, meta):
    path = os.path.join(ROOT, fname)
    s = open(path, encoding="utf-8").read()
    orig = s

    for a, b in LINK_MAP + ASSET_MAP:
        s = s.replace(a, b)

    # swap in the shared header / footer
    s = HEADER_RE.sub("\n" + build.header(meta["nav"]).strip("\n") + "\n", s, count=1)
    s = FOOTER_RE.sub("\n" + build.footer().strip("\n") + "\n", s, count=1)

    # canonical + open graph (idempotent)
    if 'rel="canonical"' not in s:
        title = re.search(r"<title>(.*?)</title>", s, re.S).group(1).strip()
        desc = re.search(r'name="description" content="(.*?)"', s, re.S).group(1).strip()
        s = s.replace('  <link rel="stylesheet" href="/css/styles.css" />',
                      head_extras(meta["url"], title, desc)
                      + '  <link rel="stylesheet" href="/css/styles.css" />', 1)

    # structured data (idempotent)
    if "application/ld+json" not in s:
        p = {"url": meta["url"], "breadcrumbs": [] if meta["url"] == "/" else
             [(meta["url"], re.search(r"<title>(.*?)[|—<]", s).group(1).strip())]}
        s = s.replace('  <link rel="stylesheet" href="/css/styles.css" />\n</head>',
                      '  <link rel="stylesheet" href="/css/styles.css" />\n'
                      + build.schema_block(p) + "</head>", 1)

    open(path, "w", encoding="utf-8").write(s)
    print(f"  {fname:<16} {'updated' if s != orig else 'already current'}")


if __name__ == "__main__":
    for f, m in TARGETS.items():
        process(f, m)
