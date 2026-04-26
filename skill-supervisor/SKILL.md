---
name: skill-supervisor
description: Use when analyzing skill usage logs, evaluating whether skills are useful, adding supervised logging footers, or reviewing skill trigger quality.
---

# Skill Supervisor

Skill Supervisor evaluates skills indirectly by reading global usage records from supervised skill copies.

## Core Idea

Keep public skills clean. Generate personal supervised copies with a short footer that asks the agent to append sanitized metadata to a global JSONL log whenever the skill is used.

Default log path:

```text
~/.codex/skill-supervisor/usage.jsonl
```

## What To Log

Use one JSON object per line:

```json
{"timestamp":"2026-04-26T12:00:00Z","skill":"architecture-review","workspace":"personal-web","trigger":"architecture review request","task_type":"review","outcome":"completed","verification":"not_applicable"}
```

Required fields are documented in `references/schema.md`.

## Rules

- Log globally, not inside the user's current repo.
- Record only metadata, never secrets or full prompts.
- If logging fails, continue the user's task normally.
- Treat the log as a signal source, not a perfect truth source.
- Evaluate patterns over time instead of judging a skill from one call.

## Workflows

### Generate Supervised Copies

From this repository:

```bash
python3 scripts/build_supervised_skills.py
```

This rebuilds `supervised/` from clean root skills and appends a standardized footer.

### Evaluate Usage

```bash
python3 skill-supervisor/scripts/evaluate_usage.py
```

Use `--log <path>` to evaluate a different JSONL file.

## Evaluation Heuristics

Look for:

- High-use skills: preserve and refine.
- Never-used skills: improve description, merge, or retire.
- Skills that start often but block often: clarify prerequisites or scope.
- Skills with no verification signal: improve their workflow or footer expectations.
- Frequent chains: document intended sequences or create a workflow skill.

## Output

When asked to evaluate skills, report:

- Calls by skill.
- Outcomes by skill.
- Verification patterns.
- Suspected underused or mis-triggered skills.
- Concrete improvements to descriptions, workflow bodies, or supervised footer design.
