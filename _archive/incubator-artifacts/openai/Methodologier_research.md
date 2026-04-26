# Methodologier Research Notes

## 1. Why this skill should exist

The strongest current AI-coding patterns are converging around three layers rather than a single prompt:

1. **Spec-driven artifacts** for turning ideas into requirements, design, and tasks.
2. **Steering / agent instruction files** for always-on constraints and workflow rules.
3. **Project memory / durable notes** for preserving architecture lessons and context across sessions.

Your Methodologier concept sits exactly at the intersection of these three.

## 2. Community and ecosystem signals

### Strongest evidence of community demand
- **GitHub Spec Kit** has extremely strong adoption and explicitly centers specification-driven development.
- **cc-sdd** and **claude-code-spec-workflow** show that spec-first workflows have become a major grassroots pattern around coding agents.
- **AGENTS.md / CLAUDE.md / steering** are now first-class concepts across multiple agent hosts.
- **Memory Bank** approaches are widely used to make coding agents preserve project understanding across sessions.

## 3. What existing tools do well

### Spec Kit / Kiro-style SDD
Best at:
- structured requirements → design → tasks flow
- turning complex feature work into explicit executable planning artifacts

Weak spot for your use case:
- they do not fully solve the “durable cross-feature methodology” layer by themselves

### CLAUDE.md / AGENTS.md / steering
Best at:
- always-on project guidance
- boundaries, commands, examples, constraints

Weak spot:
- these files become overloaded if you dump every architectural lesson into them

### Memory Bank
Best at:
- preserving evolving project context and architecture knowledge across sessions

Weak spot:
- memory-bank style systems often become too broad; they need a stricter filter for what counts as a reusable methodology insight

## 4. Key design conclusion

Methodologier should not compete with specs, AGENTS.md, or Memory Bank.
It should act as a **curation and distillation layer**:

- before implementation: produce a high-quality seed methodology document
- during implementation: periodically review the repo and harvest only the reusable lessons worth preserving
- across the whole lifecycle: keep one canonical insight document aligned with host files

## 5. Skill behavior decisions

### Decision A — two modes
Use two explicit modes:
- **Bootstrap mode**
- **Reflection mode**

Reason:
The user’s two desired capabilities are different enough that a single vague workflow would underperform.

### Decision B — keep one canonical artifact
Prefer one seed insight document, not many small parallel files.

Reason:
Otherwise the repo ends up with overlapping `CLAUDE.md`, `AGENTS.md`, specs, memory notes, and methodology notes.

### Decision C — insight quality filter
Only preserve insights that are:
- reusable
- decision-shaping
- observable in future work
- scoped enough to apply correctly

Reason:
This prevents the document from decaying into generic prose.

### Decision D — align with host ecosystem
The skill should detect existing host conventions and fit into them:
- Claude Code / CLAUDE.md / skills
- Codex / AGENTS.md
- Copilot instructions
- Kiro steering / specs / skills
- Memory Bank structures

## 6. Recommended usage pattern

### Before implementation
Run Methodologier to create:
- purpose and usage
- project context snapshot
- hard constraints
- strong defaults
- architecture heuristics
- delivery heuristics
- documentation rules
- future-agent instructions
- open questions

### During implementation
Call Methodologier when:
- a major refactor was completed
- a good architecture pattern emerged
- the team discovered a rule that future AI sessions should follow
- the repo is starting to drift or over-couple
- specs or agent files are getting noisy and need a cleaner durable core

## 7. Why this is better than a plain “best practices” skill

A generic best-practices skill teaches static rules.
Methodologier instead:
- interviews the user
- inspects the live repo
- writes into a persistent artifact
- merges new lessons over time
- treats methodology as project memory plus steering, not just advice

## 8. Future extensions worth adding

- optional rubric-based scoring of an existing seed insight doc
- optional `--bootstrap` / `--reflect` argument handling
- optional support for generating a short companion snippet for `CLAUDE.md` or `AGENTS.md`
- optional eval assertions once you start testing the skill inside a real host
