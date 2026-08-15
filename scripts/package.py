"""Package the site as the course-required standalone zip.

Produces dist/2026_ClinicalLabAnalysisSystem.zip (year first, per the
course convention) containing exactly one root directory,
2026_ClinicalLabAnalysisSystem/, with index.htm inside it. Only site
files are included (pages, assets, files) — repo metadata, scripts, and
docs are excluded.
"""
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME = "2026_ClinicalLabAnalysisSystem"
DIST = ROOT / "dist"

INCLUDE_DIRS = ["assets", "files"]
EXCLUDE_TOP = {".git", ".gitignore", "dist", "scripts", "CLAUDE.md", "README.md"}


def main() -> int:
    stage = DIST / NAME
    if DIST.exists():
        shutil.rmtree(DIST)
    stage.mkdir(parents=True)

    for page in ROOT.glob("*.htm"):
        shutil.copy2(page, stage / page.name)
    for d in INCLUDE_DIRS:
        shutil.copytree(ROOT / d, stage / d)

    if not (stage / "index.htm").exists():
        print("FATAL: staged folder has no index.htm")
        return 1

    zip_path = DIST / f"{NAME}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(stage.rglob("*")):
            if f.is_file():
                zf.write(f, f.relative_to(DIST))

    names = zipfile.ZipFile(zip_path).namelist()
    roots = {n.split("/")[0] for n in names}
    assert roots == {NAME}, f"zip must contain exactly one root dir, got: {roots}"
    assert f"{NAME}/index.htm" in names, "index.htm missing from zip root dir"

    size_mb = zip_path.stat().st_size / 1e6
    print(f"OK: {zip_path.name} ({size_mb:.1f} MB), {len(names)} files, single root '{NAME}/', index.htm present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
