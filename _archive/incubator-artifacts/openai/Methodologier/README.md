# Methodologier

A Claude-style skill for building and maintaining a high-leverage seed insight document for AI-assisted software projects.

## Contents

- `SKILL.md`: entrypoint
- `references/`: supporting reference docs the skill can read on demand
- `assets/seed-insights-template.md`: default output template
- `evals/evals.json`: starter evaluation prompts

## Install in Claude Code

Project-local:

```bash
mkdir -p .claude/skills
cp -R Methodologier .claude/skills/methodologier
```

Global:

```bash
mkdir -p ~/.claude/skills
cp -R Methodologier ~/.claude/skills/methodologier
```

## Recommended companion files

Methodologier works best alongside one or more of:

- `CLAUDE.md`
- `AGENTS.md`
- `.github/copilot-instructions.md`
- `memory-bank/`
- feature-level specs such as `requirements.md`, `design.md`, `tasks.md`

## Suggested first run

- “Before we start, create our seed methodology document.”
- “Review the repo and update our seed insight doc with reusable architecture lessons.”
