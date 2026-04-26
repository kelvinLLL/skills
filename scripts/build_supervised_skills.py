#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import shutil
import sys


ROOT = Path(__file__).resolve().parents[1]
SUPERVISED_DIR = "supervised"
EXCLUDED_ROOTS = {
    ".git",
    ".pytest_cache",
    "_archive",
    "__pycache__",
    "scripts",
    "skill-supervisor",
    SUPERVISED_DIR,
    "tests",
    "vendor",
}


def is_skill_dir(path: Path) -> bool:
    return path.is_dir() and (path / "SKILL.md").exists()


def discover_clean_skills(root: Path) -> list[Path]:
    skills: list[Path] = []
    for child in sorted(root.iterdir()):
        if child.name in EXCLUDED_ROOTS:
            continue
        if is_skill_dir(child):
            skills.append(child)
    return skills


def ignore_generated(_dir: str, names: list[str]) -> set[str]:
    ignored = {".DS_Store", "__pycache__", ".pytest_cache"}
    return {name for name in names if name in ignored or name.endswith(".pyc")}


def supervisor_footer(skill_name: str) -> str:
    return f"""

<!-- Skill Supervisor Footer -->
## Skill Supervisor Footer

When this supervised skill is used, append one sanitized JSONL record to `~/.codex/skill-supervisor/usage.jsonl`.

Suggested record:

```json
{{"timestamp":"<ISO-8601 UTC>","skill": "{skill_name}","workspace":"<workspace basename or unknown>","trigger":"<short non-sensitive reason>","task_type":"<planning|implementation|review|research|other>","outcome":"<started|completed|blocked|skipped>","verification":"<passed|failed|not_run|not_applicable>"}}
```

Only record metadata. Do not record secrets, credentials, full prompts, file contents, private user data, or long task transcripts. If logging is unavailable, continue the task normally.

If the `skill-supervisor` skill is installed globally, prefer its helper script:

```bash
python3 ~/.codex/skills/skill-supervisor/scripts/log_usage.py --skill "{skill_name}" --trigger "<short non-sensitive reason>" --task-type "<type>" --outcome "<outcome>" --verification "<status>"
```
"""


def build_supervised_skills(root: Path = ROOT) -> list[str]:
    root = root.resolve()
    supervised_root = root / SUPERVISED_DIR
    if supervised_root.exists():
        shutil.rmtree(supervised_root)
    supervised_root.mkdir()

    readme = supervised_root / "README.md"
    readme.write_text(
        "# Supervised Skills\n\n"
        "Generated copies of the clean root skills with a Skill Supervisor footer. "
        "Do not edit these by hand; run `python3 scripts/build_supervised_skills.py` instead.\n",
        encoding="utf-8",
    )

    built: list[str] = []
    for skill_dir in discover_clean_skills(root):
        target = supervised_root / skill_dir.name
        shutil.copytree(skill_dir, target, ignore=ignore_generated)
        skill_file = target / "SKILL.md"
        skill_file.write_text(
            skill_file.read_text(encoding="utf-8").rstrip()
            + supervisor_footer(skill_dir.name),
            encoding="utf-8",
        )
        built.append(skill_dir.name)
    return built


def main() -> int:
    built = build_supervised_skills(ROOT)
    print(f"Built {len(built)} supervised skills:")
    for name in built:
        print(f"- {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
