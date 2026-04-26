# Skill Usage Log Schema

Each line of `~/.codex/skill-supervisor/usage.jsonl` is one JSON object.

## Required Fields

| Field | Meaning |
| --- | --- |
| `timestamp` | ISO-8601 UTC timestamp. |
| `skill` | Skill folder/name used. |
| `workspace` | Basename of the current workspace or `unknown`. |
| `trigger` | Short sanitized reason the skill was used. |
| `task_type` | `planning`, `implementation`, `review`, `research`, `debugging`, `evaluation`, or `other`. |
| `outcome` | `started`, `completed`, `blocked`, or `skipped`. |
| `verification` | `passed`, `failed`, `not_run`, or `not_applicable`. |

## Privacy Rules

Do not record:

- Secrets, tokens, credentials, API keys.
- Full user prompts.
- File contents.
- Private customer or personal data.
- Long transcripts.

Prefer short summaries such as "architecture review request" or "daily report generation".
