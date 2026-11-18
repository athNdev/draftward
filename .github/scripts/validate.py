"""Check Draftward's skill layout and repository-local link targets."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"
LINK = re.compile(r'\]\(([^)\s]+)\)|\bsrc="([^"]+)"')
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def check_skill(skill):
    entry = skill / "SKILL.md"
    if not entry.is_file():
        return [f"{entry.relative_to(ROOT)} is missing"]

    frontmatter = re.match(r"\A---\n(.+?)\n---\n", entry.read_text(encoding="utf-8"), re.S)
    if frontmatter is None:
        return [f"{entry.relative_to(ROOT)} has no frontmatter"]

    name = re.search(r"^name: (.+)$", frontmatter[1], re.M)
    description = re.search(r"^description: (.+)$", frontmatter[1], re.M)
    errors = []
    if name is None or name[1] != skill.name or len(name[1]) > 64 or not NAME.fullmatch(name[1]):
        errors.append(f"{entry.relative_to(ROOT)} needs a valid name matching its directory")
    if description is None or not 1 <= len(description[1].strip()) <= 1024:
        errors.append(f"{entry.relative_to(ROOT)} needs a description of 1–1024 characters")
    if not (skill / "agents" / "openai.yaml").is_file():
        errors.append(f"{skill.relative_to(ROOT)} needs agents/openai.yaml")
    return errors


def check_links(document):
    errors = []
    for markdown_link, image_source in LINK.findall(document.read_text(encoding="utf-8")):
        reference = markdown_link or image_source
        url = urlsplit(reference)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (document.parent / unquote(url.path)).resolve()
        if not target.is_relative_to(ROOT) or not target.exists():
            errors.append(f"{document.relative_to(ROOT)} has an invalid local link to {reference}")
    return errors


def main():
    skills = sorted(path for path in SKILLS.iterdir() if path.is_dir())
    documents = sorted(ROOT.glob("*.md")) + sorted((ROOT / "assets").glob("*.md"))
    documents += sorted(SKILLS.rglob("*.md"))
    errors = [] if skills else ["No skills found"]
    for skill in skills:
        errors.extend(check_skill(skill))
    for document in documents:
        errors.extend(check_links(document))
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {len(skills)} skills and local links in {len(documents)} documents.")


if __name__ == "__main__":
    main()
