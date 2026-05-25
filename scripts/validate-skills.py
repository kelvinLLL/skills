#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_GROUPS = ("original", "adapted")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter")
    try:
        _, block, _ = text.split("---", 2)
    except ValueError as exc:
        raise ValueError("missing closing frontmatter") from exc

    data: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def collect_skill_dirs(group_dir: Path) -> list[Path]:
    skill_dirs: list[Path] = []
    if not group_dir.exists():
        return skill_dirs

    for child in sorted(group_dir.iterdir()):
        if not child.is_dir():
            continue
        skill_file = child / "SKILL.md"
        if skill_file.exists():
            skill_dirs.append(child)
    return skill_dirs


def validate_skill_dirs(skill_dirs: list[Path]) -> list[str]:
    errors: list[str] = []
    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        try:
            meta = parse_frontmatter(skill_file)
        except ValueError as exc:
            errors.append(f"{skill_file}: {exc}")
            continue

        name = meta.get("name")
        description = meta.get("description")
        if not name:
            errors.append(f"{skill_file}: missing name")
        elif not re.fullmatch(r"[a-z0-9-]+", name):
            errors.append(f"{skill_file}: invalid name {name!r}")
        elif name != skill_dir.name:
            errors.append(f"{skill_file}: name does not match folder")

        if not description:
            errors.append(f"{skill_file}: missing description")
        elif len(description) > 1024:
            errors.append(f"{skill_file}: description exceeds 1024 chars")
    return errors


def main() -> int:
    errors: list[str] = []
    grouped_skill_dirs: dict[str, list[Path]] = {}
    for group in SKILL_GROUPS:
        skill_dirs = collect_skill_dirs(ROOT / group)
        grouped_skill_dirs[group] = skill_dirs
        if not skill_dirs:
            errors.append(f"no skill directories found in {group}/")
        errors.extend(validate_skill_dirs(skill_dirs))

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    total = sum(len(skill_dirs) for skill_dirs in grouped_skill_dirs.values())
    print(f"Validated {total} skills.")
    for group, skill_dirs in grouped_skill_dirs.items():
        print(f"{group}/")
        for skill_dir in skill_dirs:
            print(f"- {skill_dir.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
