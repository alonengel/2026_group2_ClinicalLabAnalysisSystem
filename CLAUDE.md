# seminar-website

The course website for the University of Haifa seminar "Software Engineering in the AI Era" — presents the **Clinical Lab Analysis System** project (team: Hala Hillou, Dana Nmarny, Anas Khoury, Alon Engel).

Workspace context, official requirements, and past-site research live in `../IrisCourse/` (see its `CLAUDE.md`, `docs/SE_SiteFinalAssignment_2026.pdf`, and `research/`).

## Hard constraints (graded requirements — never violate)

- Standalone static site, submitted as `<ProjectName>_2026.zip`: exactly one root folder named like the zip, entry file **`index.htm`**, ALL links relative. Must render correctly opened via `file://` from the unzipped folder.
- Fully self-contained: no CDNs, no external fonts/scripts/images. Bundle every asset.
- Proper English everywhere; Hebrew downloads labeled "(in Hebrew)".
- Team names + topic visible; **student ID numbers appear nowhere** (pages or linked documents).
- All work materials + presentations downloadable from the site.
- Clear topics/sub-topics, uniform and aesthetic; no special software assumed (plain HTML/CSS; vanilla JS only where the page works without it).

## Conventions

- Never commit or push without being asked.
- Keep filenames URL-safe (no spaces/Hebrew in asset filenames); links are case-sensitive when served.
