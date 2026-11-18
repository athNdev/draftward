<h1><img src="assets/draftward-lockup.svg" width="520" height="181" alt="Draftward · Formal report skills"></h1>

[![Validate skills](https://github.com/athNdev/draftward/actions/workflows/validate.yml/badge.svg)](https://github.com/athNdev/draftward/actions/workflows/validate.yml)

**Agent Skills for formal reports, from brief to final PDF.**

Draftward helps you draft academic, technical, and professional reports. It connects requirements to sections and claims to evidence, so you can see what the draft covers and where it needs work. The skills follow the [Agent Skills format](https://agentskills.io/specification).

For review and revision, Draftward tracks the author's decisions and points to the exact passages in the current PDF that still need attention.

## Choose a skill

| Skill | Use it when you want to |
| --- | --- |
| [`$report-drafting`](skills/report-drafting/SKILL.md) | Turn a brief and source material into an outline or draft and identify which reporting rules apply. |
| [`$report-review`](skills/report-review/SKILL.md) | Review a whole report, reconcile feedback with the rubric, or plan the next revision. |
| [`$report-clarity`](skills/report-clarity/SKILL.md) | Improve terminology, flow, and reader context while preserving the report's meaning. |
| [`$report-evidence`](skills/report-evidence/SKILL.md) | Trace claims to their evidence and verify results, citations, and limitations. |
| [`$report-release`](skills/report-release/SKILL.md) | Rebuild and check a final PDF, including layout, links, and passage locations. |

For a new report, start with drafting. For a substantial revision, start with review. Use clarity and evidence checks where needed, then run release on the final export.

## Reporting standards

The [standards guide](skills/report-drafting/references/report-standards.md) points to official sources for academic and industry reporting, citation styles, and accessibility. Draftward checks which requirements apply to the specific report and records any that need confirmation.

The [companion skills guide](skills/report-drafting/references/companion-tools.md) shows how to use separately installed citation and document skills alongside Draftward.

## Install

Run this from your report project to install all five skills in a supported harness:

```sh
npx skills add athNdev/draftward --skill '*'
```

Select your harness when prompted. Versioned downloads are available from [GitHub Releases](https://github.com/athNdev/draftward/releases/latest).

### Manual install

1. Clone this repository or download and extract its ZIP from GitHub.
2. Copy the five folders **inside** [`skills/`](skills/) into your harness's project skill directory. Keep them together so their shared references resolve.
3. Open the report project in the harness and select the skill by name. PDF rebuilds and visual checks depend on the build and document tools available to that harness.

| Harness | Project skill directory |
| --- | --- |
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `.agents/skills/` |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/` |
| [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills) | `.github/skills/` |

The same Markdown instructions can be used in other Agent Skills-compatible harnesses. Use that harness's documented location and test discovery and linked resources before relying on it.

## Example prompts

- `Use $report-drafting to outline a technical evaluation from this brief and test summary. Flag missing evidence before drafting the conclusions.`
- `Use $report-review to review this draft against the supplied rubric and propose a revision plan.`
- `Use $report-clarity to improve the discussion while preserving the technical meaning and authorial voice.`
- `Use $report-evidence to check the results section against the supplied evaluation summaries.`
- `Use $report-release to rebuild the report and check the final PDF's figures, links, and page references.`

Provide the current draft and the materials relevant to the task, such as the rubric, evidence summaries, or build instructions. The skills are Markdown instructions. PDF rebuilding uses the report project's existing toolchain.

## Repository layout

Each skill starts at `skills/<skill-name>/SKILL.md`, with supporting guidance in `references/` and Codex interface metadata in `agents/openai.yaml`. Edit these source folders directly. Git ignores generated `.skill` archives.

The [brand guide](assets/README.md) includes the identity sheet, logo exports, and editable ArtCraft source.

See [Contributing](CONTRIBUTING.md) for changes to skills and the standards guide.
See [Distribution](DISTRIBUTION.md) for release packages and marketplace submission paths.
Use [GitHub Discussions](https://github.com/athNdev/draftward/discussions) for workflow questions and examples.

Draftward is licensed under [MIT-0](LICENSE).
