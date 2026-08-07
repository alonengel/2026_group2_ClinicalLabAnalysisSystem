"""Static checks for the standalone course site.

Verifies, for every .htm page in the site root:
  - every internal href/src resolves to an existing file (case-sensitively)
  - no absolute local links (leading '/', 'file://', drive letters)
  - no spaces in referenced internal paths
  - external links use https
  - every <img> has a non-empty alt attribute
  - no student-ID-like numbers (8-9 digit runs) in page text

Exit code 0 = clean, 1 = problems found.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS: list[str] = []


def note(page: str, msg: str) -> None:
    PROBLEMS.append(f"{page}: {msg}")


def exists_case_sensitive(path: Path) -> bool:
    if not path.exists():
        return False
    # Windows resolves case-insensitively; compare the real name per component.
    current = ROOT
    for part in path.relative_to(ROOT).parts:
        matches = {p.name for p in current.iterdir()}
        if part not in matches:
            return False
        current = current / part
    return True


def main() -> int:
    pages = sorted(ROOT.glob("*.htm"))
    if not pages:
        print("No .htm pages found — wrong directory?")
        return 1

    for page in pages:
        html = page.read_text(encoding="utf-8")
        rel = page.name

        for m in re.finditer(r'(?:href|src)="([^"]+)"', html):
            url = m.group(1)
            if url.startswith("data:") or url.startswith("#") or url.startswith("mailto:"):
                continue
            if url.startswith("http://"):
                note(rel, f"insecure external link: {url}")
                continue
            if url.startswith("https://"):
                continue
            if url.startswith("/") or url.startswith("file:") or re.match(r"^[A-Za-z]:", url):
                note(rel, f"absolute local link (must be relative): {url}")
                continue
            if " " in url:
                note(rel, f"space in internal path: {url}")
            target = (ROOT / url.split("#")[0]).resolve()
            if not exists_case_sensitive(target):
                note(rel, f"broken internal link: {url}")

        for m in re.finditer(r"<img\b[^>]*>", html):
            tag = m.group(0)
            alt = re.search(r'alt="([^"]*)"', tag)
            if not alt or not alt.group(1).strip():
                note(rel, f"img without alt text: {tag[:80]}...")

        text = re.sub(r"<[^>]+>", " ", html)
        for m in re.finditer(r"(?<![\d,.])\d{8,9}(?![\d,.])", text):
            note(rel, f"ID-like number in visible text: {m.group(0)}")

    entry = ROOT / "index.htm"
    if not entry.exists():
        PROBLEMS.append("MISSING entry file index.htm")

    if PROBLEMS:
        print(f"{len(PROBLEMS)} problem(s):")
        for p in PROBLEMS:
            print("  -", p)
        return 1
    print(f"OK: {len(pages)} pages checked, all internal links resolve, no hygiene issues.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
