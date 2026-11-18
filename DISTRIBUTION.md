# Distribution

GitHub is Draftward's source of truth. The release workflow builds a plugin ZIP containing the five skills together and a standalone skill ZIP containing the same workflows and references under one entry point. The standalone form keeps sibling references available in registries that install one skill folder at a time.

## Prepare a release

1. For a preview, run [Distribute Draftward](https://github.com/athNdev/draftward/actions/workflows/distribute.yml) from `main` with a stable tag such as `v0.1.0`. Download the `draftward-release` artifact, or choose **Create a GitHub draft release** to attach the ZIPs and checksums to a draft.
2. To build locally, run `python .github/scripts/validate.py` and `python .github/scripts/package_release.py v0.1.0 dist`.
3. Before publishing, verify the [MIT-0 licence](LICENSE) is included, review the files intended for public release, and update both repository plugin manifests to the release version. Test the plugin on the intended host with the full five-skill set.
4. Add the registry secrets below. On the public repository, use **Check registry** in the dispatch form to verify each credential without publishing.
5. Set the repository Actions variable `ENABLE_PUBLIC_SKILL_RELEASES` to `true` to publish from stable GitHub releases. The workflow checks live GitHub visibility. A job warns and skips its registry when the corresponding secret is missing.

## Channels

| Channel | Delivery |
| --- | --- |
| GitHub Releases | Build and attach both archives to a draft, then publish the draft when approved. |
| [ClawHub](https://docs.openclaw.ai/clawhub/publishing) | The workflow submits the standalone `draftward` skill with `CLAWHUB_TOKEN`. ClawHub applies [MIT-0](https://docs.openclaw.ai/clawhub/skill-format#license), so set `CLAWHUB_MIT0_ACCEPTED=true` only after approving those terms for this distribution. ClawHub scans the submitted version before it becomes installable. |
| [Sundial Hub](https://github.com/sundial-org/skills/blob/main/skills/skill/SKILL.md#publish-a-skill) | The workflow submits the standalone version using `SUNDIAL_TOKEN`. |
| [skills.sh](https://www.skills.sh/docs) | Once GitHub is public, run `npx skills add athNdev/draftward --skill '*'` and select your harness. The leaderboard uses real install telemetry. |
| [SkillsMP](https://skillsmp.com/docs/api) | The public GitHub source is ready for indexing. The documented API searches existing listings. |
| [Claude and Claude Code directory](https://claude.com/resources/articles/build-plugins-for-claude) | Submit the GitHub plugin repository in Anthropic's directory portal. The repo includes the Claude plugin manifest. Directory submission requires an eligible account and review. |
| [ChatGPT and Codex directory](https://developers.openai.com/plugins/deploy/submission) | Upload the versioned plugin ZIP as **Skills only**. Complete listing metadata, test the install, and submit for review in the portal. |
| [Cursor Marketplace](https://cursor.com/docs/plugins) | Submit the public GitHub repo in Cursor's review portal. The root portable plugin manifest is included. |
| [LobeHub Skills Marketplace](https://lobehub.com/docs/usage/community/become-a-creator) | Select the public GitHub repo in the creator submission flow. |
| [Skills Directory](https://www.skillsdirectory.com/) | Submit the public source through the directory's review form. |

Check each listing after acceptance. Directory approval, indexing, and installation are separate from building the release. Keep the repository private until the owner approves public distribution.
