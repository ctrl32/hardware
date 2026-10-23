#!/usr/bin/env python3
"""check.py - the completeness check of the board guides (run by CI on every
push and pull request).

A push fails when, for a board folder (boards/<family>/<board>/ with a
README.md that names `hardware:`):

  1. a page is missing - README.md, hardware.md, install.md, configure.md,
     troubleshooting.md, examples/README.md, examples/all-in-one/ with its
     README.md and project; or an example folder has no README.md or no .prj32,
  2. the front matter misses a required key, or `slug` differs from the folder,
  3. an image has no alt text, a link points at a file that does not exist or
     outside the repository, a screenshot is over 400 kB (a board photo over
     800 kB), the board has no pinout/ or fewer than the minimum of photos,
  4. the capability table is not current (tools/capabilities.py --check),
  5. a text speaks of two CAN controllers on an ESP32.

Usage:
    python tools/check.py               # the checks above
    python tools/check.py --no-network  # skip 4 (offline)
    python tools/check.py --catalog     # list tested boards without a guide,
                                        # and guides whose board is no longer tested
    python tools/check.py --min-photos N  # the photo minimum (default 1; the target is 3)
"""
import argparse, glob, json, os, re, subprocess, sys, urllib.request

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = ["README.md", "hardware.md", "install.md", "configure.md", "troubleshooting.md", "examples/README.md"]
FM_BOARD = ["title", "slug", "sidebar_position", "hardware", "image", "image_alt", "tags"]
FM_PAGE = ["title", "slug", "sidebar_position", "image", "image_alt", "tags"]
TWO_CAN = re.compile(r"(2\s*[x×]\s*CAN|two\s+TWAI|dual\s+CAN|two\s+CAN\s+controllers)", re.I)


def fm(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return (yaml.safe_load(m.group(1)) or {}) if m else None


def boards():
    for readme in glob.glob(os.path.join(ROOT, "boards", "*", "*", "README.md")):
        f = fm(open(readme, encoding="utf-8").read())
        if f and f.get("hardware"):
            yield os.path.dirname(readme), f


def check_md(path, base, errs, board_dir):
    text = open(path, encoding="utf-8").read()
    rel = os.path.relpath(path, ROOT)
    f = fm(text)
    if f is None:
        errs.append(f"{rel}: no front matter")
        return
    need = FM_BOARD if os.path.dirname(path) == board_dir and path.endswith("README.md") else FM_PAGE
    for k in need:
        if k not in f:
            errs.append(f"{rel}: front matter has no '{k}'")
    for alt, link in re.findall(r"!\[([^\]]*)\]\(([^)\s]+)\)", text):
        if not alt.strip():
            errs.append(f"{rel}: an image without alt text ({link})")
    for _, link in re.findall(r"(!?\[[^\]]*\])\(([^)\s]+)\)", text):
        if re.match(r"^(https?:|mailto:|#)", link):
            continue
        target = os.path.normpath(os.path.join(os.path.dirname(path), link.split("#")[0]))
        if not target.startswith(ROOT):
            errs.append(f"{rel}: link outside the repository ({link})")
        elif not os.path.exists(target):
            errs.append(f"{rel}: link to a missing file ({link})")
    if TWO_CAN.search(text):
        errs.append(f"{rel}: speaks of two CAN controllers - an ESP32 has exactly one")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-network", action="store_true")
    ap.add_argument("--catalog", action="store_true")
    ap.add_argument("--min-photos", type=int, default=1)
    a = ap.parse_args()
    if a.catalog:
        return catalog_check()
    errs = []
    for d, f in boards():
        rel = os.path.relpath(d, ROOT)
        if f.get("slug") != os.path.basename(d):
            errs.append(f"{rel}: slug '{f.get('slug')}' is not the folder name")
        for p in PAGES:
            if not os.path.exists(os.path.join(d, p)):
                errs.append(f"{rel}: missing {p}")
        ex = os.path.join(d, "examples")
        if not os.path.isdir(os.path.join(ex, "all-in-one")):
            errs.append(f"{rel}: missing examples/all-in-one/")
        for x in glob.glob(os.path.join(ex, "*", "")):
            if not os.path.exists(os.path.join(x, "README.md")):
                errs.append(f"{os.path.relpath(x, ROOT)}: no README.md")
            if not glob.glob(os.path.join(x, "*.prj32")):
                errs.append(f"{os.path.relpath(x, ROOT)}: no project (.prj32)")
        if not os.path.exists(os.path.join(d, "pinout", "pinout.svg")):
            errs.append(f"{rel}: no pinout/pinout.svg")
        photos = glob.glob(os.path.join(d, "img", "board-*.jpg"))
        if len(photos) < a.min_photos:
            errs.append(f"{rel}: {len(photos)} board photo(s), the minimum is {a.min_photos}")
        for md in glob.glob(os.path.join(d, "**", "*.md"), recursive=True):
            check_md(md, d, errs, d)
        for im in glob.glob(os.path.join(d, "**", "*.*"), recursive=True):
            ext = os.path.splitext(im)[1].lower()
            size = os.path.getsize(im)
            if ext == ".png" and "pinout" not in im and size > 400 * 1024:
                errs.append(f"{os.path.relpath(im, ROOT)}: {size // 1024} kB, a screenshot is at most 400 kB")
            if ext == ".jpg" and size > 800 * 1024:
                errs.append(f"{os.path.relpath(im, ROOT)}: {size // 1024} kB, a photo is at most 800 kB")
    if not a.no_network:
        r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "capabilities.py"), "--check"])
        if r.returncode != 0:
            errs.append("a capability table is not current - run tools/capabilities.py and commit")
    for e in errs:
        print(e)
    print(f"check: {'FAILED, ' + str(len(errs)) + ' problem(s)' if errs else 'OK'}")
    sys.exit(1 if errs else 0)


def catalog_check():
    def get(u):
        req = urllib.request.Request(u, headers={"User-Agent": "ctrl32-hardware-check"})
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    tested, page = set(), 1
    while True:
        j = get(f"https://ctrl32.com/api/v1/records?bundle=board&page_size=50&page={page}")
        for r in j["results"]:
            for x in r.get("teaser_rows", []):
                if x["name"] == "hw_test_status_ref" and "Tested" in (x.get("items") or []):
                    tested.add(r["canonical_url"])
        if page >= j["pages"]:
            break
        page += 1
    have = {f["hardware"]: d for d, f in boards() if not f.get("draft")}
    for t in sorted(tested - set(have)):
        print(f"tested without a guide: {t}")
    for h in sorted(set(have) - tested):
        print(f"guide without a tested board (set draft: true): {os.path.relpath(have[h], ROOT)}")
    print(f"catalog: {len(tested)} tested, {len(set(have) & tested)} with a guide")


if __name__ == "__main__":
    main()
