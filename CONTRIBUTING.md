# Contributing to Draftward

Use a GitHub issue to report a workflow problem or suggest a reporting authority. Include a short example using public or synthetic material and describe what the skill should do in that case.

For a skills change, edit the relevant `SKILL.md` and put guidance that only some tasks need in `references/`. Keep the folder name and skill name aligned. For a standards entry, link to the issuing body and explain the report types, jurisdiction, editions, or adoption conditions that determine applicability. Describe the reporting implications in your own words.

Run `python .github/scripts/validate.py` from the repository root before opening a pull request. The check covers skill structure and local links. For behavioural changes, also try the affected skill on a representative report task and describe the outcome in the pull request.
