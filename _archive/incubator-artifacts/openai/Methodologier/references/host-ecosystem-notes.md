# Host ecosystem alignment notes

Use this file to avoid creating overlapping guidance files when the repository already follows a context-engineering pattern.

## If the repo uses CLAUDE.md / Claude Code skills

- Treat the seed insight document as durable project guidance.
- Keep procedural multi-step workflows in skills.
- Keep short always-on rules in `CLAUDE.md`.
- Reference the seed insight doc from `CLAUDE.md` instead of duplicating large sections.

## If the repo uses AGENTS.md

- Keep the seed insight document as deeper project methodology.
- Put concise agent behavior rules in `AGENTS.md`.
- Prefer links / references over copying long methodology sections into the root instruction file.

## If the repo uses GitHub Copilot instructions

- Repository-wide build/test/validation instructions belong in `.github/copilot-instructions.md`.
- Path-specific rules belong in `.github/instructions/**/*.instructions.md`.
- Reusable methodology can live in the seed insight document and be referenced from those instruction files.

## If the repo uses Memory Bank style docs

Map Methodologier output roughly as:
- project context snapshot -> `projectbrief.md` / `productContext.md`
- architecture and design heuristics -> `systemPatterns.md`
- open questions / watchpoints -> `activeContext.md`
- progress-specific items -> `progress.md`

Do not duplicate the entire Memory Bank structure unless the project lacks one.

## If the repo uses spec-driven artifacts

Typical split:
- seed insight document -> enduring cross-feature methodology
- `requirements.md` / `bugfix.md` -> feature or bug intent
- `design.md` -> task-specific technical design
- `tasks.md` -> execution plan

The seed insight document should influence specs, not replace them.
