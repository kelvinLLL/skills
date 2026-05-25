# Kelvin Skills

Personal Codex-first skill library.

This repository keeps installable skills grouped by source:

- `original/` - skills I built from scratch.
- `adapted/` - skills adapted from external ideas or upstream skill libraries.
- `vendor/` - upstream projects tracked directly as submodules.

## Original Skills

- `original/ai-daily-report` - Chinese AI industry daily report workflow with source validation.
- `original/methodologier` - durable project methodology and seed-insights workflow.
- `original/research-insight` - structured Chinese insight reports for papers, reports, surveys, and technical repositories.

## Adapted Skills

- `adapted/architecture-review` - deep-module architecture review and refactor candidate discovery.
- `adapted/domain-model` - domain language, `CONTEXT.md`, and ADR decision capture.
- `adapted/interface-design` - software API/module interface design alternatives.
- `adapted/ubiquitous-language` - fast glossary extraction and ambiguity cleanup.

These are kept as local working versions. Their exact upstream ancestry may be mixed or historical, so the folder marks them as adapted rather than direct vendor copies.

Install a skill with the Skills CLI style used by common `SKILL.md` repositories:

```bash
npx skills@latest add kelvinLLL/skills/original/ai-daily-report
npx skills@latest add kelvinLLL/skills/adapted/domain-model
```

Replace the path with any concrete skill folder under `original/` or `adapted/`.

## Vendor Submodules

These are tracked as upstream references and should stay close to upstream:

- `vendor/superpowers` -> `obra/superpowers`
- `vendor/andrej-karpathy-skills` -> `forrestchang/andrej-karpathy-skills`
- `vendor/ui-ux-pro-max-skill` -> `nextlevelbuilder/ui-ux-pro-max-skill`
- `vendor/agent-browser` -> `vercel-labs/agent-browser`

After cloning this repository:

```bash
git submodule update --init --recursive
```

## Validate

```bash
python3 scripts/validate-skills.py
```

The validator checks installable skills under `original/` and `adapted/` for `SKILL.md`, required frontmatter, matching names, and description lengths suitable for agent discovery.
