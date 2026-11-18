"""Build a portable plugin and a standalone registry skill from the same source."""

import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from validate import LINK, ROOT, SKILLS


VERSION = re.compile(r"v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)")
SIBLING_LINK = re.compile(r"(\]\((?:\.\./)+[^)\s]+/)SKILL\.md(?=[)#])")


def skill_files():
    return sorted(
        path for path in SKILLS.rglob("*")
        if path.is_file() and (path.suffix == ".md" or path.name == "openai.yaml")
    )


def plugin_files(paths, version):
    files = {path.relative_to(ROOT).as_posix(): path.read_bytes() for path in paths}
    for name in ("plugin.json", ".claude-plugin/plugin.json"):
        manifest = json.loads((ROOT / name).read_text(encoding="utf-8"))
        manifest["version"] = version
        files[name] = json.dumps(manifest, indent=2).encode()
    files["assets/draftward-avatar.png"] = (ROOT / "assets/draftward-avatar.png").read_bytes()
    if (ROOT / "LICENSE").is_file():
        files["LICENSE"] = (ROOT / "LICENSE").read_bytes()
    return files


def standalone_files(paths):
    entry = ROOT / ".github/distribution/draftward.md"
    files = {"draftward/SKILL.md": entry.read_bytes()}
    if (ROOT / "LICENSE").is_file():
        files["draftward/LICENSE"] = (ROOT / "LICENSE").read_bytes()
    for path in paths:
        if path.suffix != ".md":
            continue
        relative = path.relative_to(SKILLS)
        if relative.name == "SKILL.md":
            relative = relative.with_name("workflow.md")
        target = f"draftward/references/{relative.as_posix()}"
        content = SIBLING_LINK.sub(r"\1workflow.md", path.read_text(encoding="utf-8"))
        files[target] = content.encode("utf-8")
    return files


def verify_links(files):
    from posixpath import dirname, join, normpath

    for name, data in files.items():
        if not name.endswith(".md"):
            continue
        for markdown_link, image_source in LINK.findall(data.decode("utf-8")):
            link = markdown_link or image_source
            url = urlsplit(link)
            if url.scheme or url.netloc or not url.path:
                continue
            target = normpath(join(dirname(name), unquote(url.path)))
            if target not in files:
                raise SystemExit(f"{name}: missing packaged link target {link}")


def write_zip(path, files):
    verify_links(files)
    with ZipFile(path, "w", compression=ZIP_DEFLATED) as archive:
        for name, data in sorted(files.items()):
            archive.writestr(ZipInfo(name), data, compress_type=ZIP_DEFLATED)
    return f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tag")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if not VERSION.fullmatch(args.tag):
        parser.error("use a stable release tag in the form vMAJOR.MINOR.PATCH")

    version = args.tag[1:]
    paths = skill_files()
    args.output.mkdir(parents=True, exist_ok=True)
    checksums = [
        write_zip(args.output / f"draftward-{version}.zip", plugin_files(paths, version)),
        write_zip(args.output / f"draftward-skill-{version}.zip", standalone_files(paths)),
    ]
    (args.output / "SHA256SUMS").write_text("\n".join(checksums) + "\n", encoding="utf-8", newline="\n")
    print(f"Built and checked both Draftward {version} archives.")


if __name__ == "__main__":
    main()
