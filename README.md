# seminar-website

> **Note:** This repository is the submission copy of the course website, under its course-convention name (`2026_group2_ClinicalLabAnalysisSystem`). It mirrors the team's working repository, [alonengel/seminar-website](https://github.com/alonengel/seminar-website), where day-to-day development took place. The project source code is in the repository **2026_group2_ClinicalLabAnalysisSystem-code** under the same owner as this repository.


Course website for the **Clinical Lab Analysis System** — final deliverable of the University of Haifa seminar *Software Engineering in the Age of AI* (team: Hala Hillou, Dana Nmarny, Anas Khoury, Alon Engel).

A fully standalone static site: plain HTML/CSS, system fonts, no build step, no CDNs, no JavaScript required. Entry file is `index.htm`; all links are relative, so the site works opened directly from a local folder (`file://`) — which is exactly how the course submission is graded.

## Pages

| Page | Content |
| --- | --- |
| `index.htm` | Overview: research question, headline numbers, pipeline, section map |
| `method.htm` | Approach, module architecture, algorithms, sandbox guardrails, dataset |
| `results.htm` | Manual + automated evaluation, coverage, edge cases, baselines, conclusions |
| `demo.htm` | Screenshot walkthrough: roles, all 12 questions, transparency tabs |
| `manual.htm` | Full user manual (requirements, install, inputs, operation, outputs) |
| `papers.htm` | AgentCoder + Self-Edit: abstracts and contribution to the project |
| `downloads.htm` | All materials (report, decks in PDF+PPTX), papers, source repo |
| `team.htm` | Team & roles, development phases, challenges, lessons, acknowledgment |

## Development

```bash
python scripts/check_site.py   # link/hygiene checks (relative links, alt text, no ID-like numbers)
python scripts/package.py      # builds dist/2026_ClinicalLabAnalysisSystem.zip (course submission format)
```

The zip contains exactly one root folder (`2026_ClinicalLabAnalysisSystem/`, year first per the course convention) with `index.htm` inside — per the assignment's standalone-site requirements. Before submitting: unzip to a fresh location, open `index.htm` in a browser, and click through every page and download.

Requirements, past-site research, and workspace context: see `../IrisCourse/`.
