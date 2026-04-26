#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import argparse
import json
import os


DEFAULT_LOG = Path.home() / ".codex" / "skill-supervisor" / "usage.jsonl"


def log_usage(
    *,
    skill: str,
    trigger: str,
    task_type: str = "other",
    outcome: str = "completed",
    verification: str = "not_applicable",
    workspace: str | None = None,
    log_path: Path = DEFAULT_LOG,
) -> Path:
    workspace_name = workspace or Path(os.getcwd()).name or "unknown"
    record = {
        "timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "skill": skill,
        "workspace": workspace_name,
        "trigger": trigger[:160],
        "task_type": task_type,
        "outcome": outcome,
        "verification": verification,
    }
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    return log_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Append a sanitized skill usage record.")
    parser.add_argument("--skill", required=True)
    parser.add_argument("--trigger", required=True)
    parser.add_argument("--task-type", default="other")
    parser.add_argument("--outcome", default="completed")
    parser.add_argument("--verification", default="not_applicable")
    parser.add_argument("--workspace")
    parser.add_argument("--log", type=Path, default=DEFAULT_LOG)
    args = parser.parse_args()

    path = log_usage(
        skill=args.skill,
        trigger=args.trigger,
        task_type=args.task_type,
        outcome=args.outcome,
        verification=args.verification,
        workspace=args.workspace,
        log_path=args.log,
    )
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
