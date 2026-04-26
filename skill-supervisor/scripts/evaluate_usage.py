#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import argparse
import json


DEFAULT_LOG = Path.home() / ".codex" / "skill-supervisor" / "usage.jsonl"


def read_records(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records: list[dict] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            records.append({"skill": "<invalid>", "outcome": "blocked", "verification": "failed", "line": line_number})
            continue
        records.append(record)
    return records


def summarize(records: list[dict]) -> str:
    if not records:
        return "No skill usage records found."

    by_skill = Counter(record.get("skill", "unknown") for record in records)
    outcomes: dict[str, Counter] = defaultdict(Counter)
    verification: dict[str, Counter] = defaultdict(Counter)
    workspaces: dict[str, Counter] = defaultdict(Counter)

    for record in records:
        skill = record.get("skill", "unknown")
        outcomes[skill][record.get("outcome", "unknown")] += 1
        verification[skill][record.get("verification", "unknown")] += 1
        workspaces[skill][record.get("workspace", "unknown")] += 1

    lines = [
        "# Skill Usage Evaluation",
        "",
        f"Total records: {len(records)}",
        "",
        "## Calls By Skill",
    ]
    for skill, count in by_skill.most_common():
        lines.append(f"- `{skill}`: {count}")

    lines.extend(["", "## Outcome Patterns"])
    for skill, _count in by_skill.most_common():
        outcome_summary = ", ".join(
            f"{name}={count}" for name, count in outcomes[skill].most_common()
        )
        verification_summary = ", ".join(
            f"{name}={count}" for name, count in verification[skill].most_common()
        )
        workspace_summary = ", ".join(
            f"{name}={count}" for name, count in workspaces[skill].most_common(3)
        )
        lines.append(
            f"- `{skill}`: outcomes({outcome_summary}); verification({verification_summary}); workspaces({workspace_summary})"
        )

    lines.extend(["", "## Signals To Investigate"])
    for skill, count in by_skill.most_common():
        blocked = outcomes[skill].get("blocked", 0)
        no_verification = verification[skill].get("not_run", 0)
        if blocked:
            lines.append(f"- `{skill}` has {blocked}/{count} blocked calls; check prerequisites and scope.")
        if no_verification:
            lines.append(f"- `{skill}` has {no_verification}/{count} calls without verification; improve close-out guidance.")

    if lines[-1] == "## Signals To Investigate":
        lines.append("- No obvious negative signal in the current log.")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate Skill Supervisor JSONL logs.")
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG)
    args = parser.parse_args()
    print(summarize(read_records(args.log)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
