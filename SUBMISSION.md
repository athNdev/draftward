# Marketplace submission checklist

Use the [public Draftward repository](https://github.com/athNdev/draftward) as the source for each submission. The [distribution guide](DISTRIBUTION.md#verify-accepted-listings) covers the checks to repeat after approval.

## Batch 1 · OpenAI and Claude

| Portal | Account step | Submission |
| --- | --- | --- |
| [ChatGPT and Codex](https://platform.openai.com/plugins) | Sign in as the intended publisher. Select the organisation and project that should own Draftward. Complete developer identity verification if prompted. | Upload the [OpenAI submission ZIP](https://github.com/athNdev/draftward/releases/download/v0.1.0/draftward-openai-0.1.0.zip) as a skills-only plugin. Review the imported listing and automated checks in **Metadata & Skills**, try the sample below, then submit for review and complete the required attestations. |
| [Claude directory](https://claude.ai/directory/manage/new) | Sign in with the paid Claude account that should own the listing. Approve access to the Draftward repository if the portal requests it. | Choose a plugin bundle and submit `https://github.com/athNdev/draftward`. Select `main` and the repository root if prompted. Review the detected plugin and complete the submission. |

OpenAI's MCP demo video, test-account, and test-case requirements apply to MCP apps. Draftward is a skills-only package. The repository's Claude Code marketplace already provides a direct install while the official listing is under review.

## Batch 2 · Cursor, Skills Directory and LobeHub

| Portal | Account step | Submission |
| --- | --- | --- |
| [Cursor Marketplace](https://cursor.com/marketplace/publish) | Sign in and complete the publisher application if prompted. | Submit `https://github.com/athNdev/draftward`. The Cursor manifest and square logo are committed. |
| [Skills Directory](https://app.skillsdirectory.com/submit) | Sign in with GitHub or email. | Submit the repository URL if the form accepts a repository. If it asks for a single skill, use the five [skill source folders](skills/) individually and mention that the full suite preserves the shared references. |
| [LobeHub](https://lobehub.com/skills) | Sign in, open **Community**, and open your creator page from your avatar. Approve GitHub access if requested. | Under **Skills**, choose **Submit Repository** and select `athNdev/draftward`. |

## Listing materials

| Field | Value |
| --- | --- |
| Name | Draftward |
| Subtitle | Formal report skills |
| Short description | Agent skills for drafting, reviewing, and verifying formal reports. |
| Category | Productivity, or Documentation if that is the closest option |
| Source and website | `https://github.com/athNdev/draftward` |
| Support | `https://github.com/athNdev/draftward/issues` |
| Licence | MIT-0 |
| Search terms | report writing, technical writing, academic writing, report review, reporting standards |
| Square logo | [Draftward avatar](assets/draftward-avatar.png) |
| Wide preview | [Draftward social card](assets/draftward-social.png) |

**Sample reviewer prompt**

> Use Draftward to outline an engineering test report and write its executive summary. Twenty trials produced a median of 150 ms. The acceptance criterion requires every trial to finish below 200 ms. I only have the median. Use sections for scope, setup, results and recommendation.

The outline should follow the named sections. The summary should report the median and trial count, leave the acceptance decision open, and identify the per-trial readings needed to evaluate it.

After approval, publish the draft if the portal leaves that decision to you. Keep the submission receipt or public listing URL for each channel.
