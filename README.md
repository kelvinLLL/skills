# Kelvin Skills

Personal Codex-first skill library.

This repository keeps my own installable skills at the repository root and tracks important upstream skill projects under `vendor/` as submodules.

## Installable Skills

- `ai-daily-report` - Chinese AI industry daily report workflow with source validation.
- `methodologier` - durable project methodology and seed-insights workflow.
- `domain-model` - domain language, `CONTEXT.md`, and ADR decision capture.
- `ubiquitous-language` - fast glossary extraction and ambiguity cleanup.
- `architecture-review` - deep-module architecture review and refactor candidate discovery.
- `interface-design` - software API/module interface design alternatives.
- `skill-supervisor` - global skill usage logging and evaluation.

Install a root skill with the Skills CLI style used by common SKILL.md repositories:

```bash
npx skills@latest add kelvinLLL/skills/architecture-review
```

Replace `architecture-review` with any root skill folder name.

## Supervised Skills

The root skill folders are the clean public versions. `supervised/` contains generated personal-use copies of my own working skills with a short Skill Supervisor footer appended.

The footer asks the agent to append sanitized metadata to:

```text
~/.codex/skill-supervisor/usage.jsonl
```

Install a supervised copy when I want usage telemetry:

```bash
npx skills@latest add kelvinLLL/skills/supervised/architecture-review
```

Regenerate supervised copies after editing clean skills:

```bash
python3 scripts/build_supervised_skills.py
```

Evaluate logs:

```bash
python3 skill-supervisor/scripts/evaluate_usage.py
```

## Vendor Submodules

These are tracked as upstream references, not copied into root installable folders:

- `vendor/superpowers` -> `obra/superpowers`
- `vendor/andrej-karpathy-skills` -> `forrestchang/andrej-karpathy-skills`
- `vendor/ui-ux-pro-max-skill` -> `nextlevelbuilder/ui-ux-pro-max-skill`
- `vendor/agent-browser` -> `vercel-labs/agent-browser`

After cloning this repository:

```bash
git submodule update --init --recursive
```

## Archive

`_archive/incubator-artifacts/` contains earlier drafting artifacts from the local incubator. They are kept for reference only and are not meant to be installed as skills.

## Validate

```bash
python3 scripts/validate-skills.py
```

The validator checks root and supervised skill folders for `SKILL.md`, required frontmatter, matching names, and description lengths suitable for agent discovery.
