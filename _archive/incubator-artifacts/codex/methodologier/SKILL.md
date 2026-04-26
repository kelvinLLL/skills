---
name: methodologier
description: Use when creating or updating a durable seed insights document for a software project, especially before spec-driven work, after major refactors, or when future AI sessions need clearer architectural guidance, reusable design heuristics, or project-level guardrails that do not belong in CLAUDE.md, AGENTS.md, or feature specs.
---

# Methodologier

## Overview

Create or maintain one durable methodology artifact that future Claude sessions can rely on.

This skill is for curating reusable project guidance, not for writing generic best practices, feature specs, or changelog-style notes. Treat the seed insights document as the repo's deeper methodology layer: architecture taste, design guardrails, delivery heuristics, and the lessons worth preserving across tasks.

## When to Use

- Starting a project, framework, migration, platform, or major refactor and needing a seed insights document before implementation expands
- Reviewing an existing repo to harvest reusable architecture lessons and update the durable methodology
- The user asks for a seed doc, methodology doc, engineering playbook, design heuristics, architecture principles, project memory, or similar long-lived guidance
- Future AI sessions keep making the same architectural mistakes or missing the same context
- CLAUDE.md, AGENTS.md, or specs are getting noisy and need a cleaner methodology layer beneath them

## When Not to Use

- The real need is a feature spec, design doc, requirements file, or task breakdown
- The user only wants a one-time summary of the current codebase
- The guidance is mostly operational and belongs in CLAUDE.md, AGENTS.md, or build and test instructions
- The insight is just a temporary implementation detail, migration note, or release log
- You are tempted to record obvious slogans such as "keep code clean" or "use good architecture"

## Core Model

Every candidate insight must end up in one of four buckets:

- Hard constraint: non-negotiable rule
- Strong default: preferred choice unless there is a clear reason not to use it
- Situational heuristic: useful rule that only applies in named contexts
- Discard: too local, too obvious, too temporary, or too vague

The document should help future Claude instances make better decisions during planning, implementation, review, and refactoring.

## Canonical Artifact Rule

Prefer one canonical seed insights document, not multiple overlapping methodology files.

Use this placement order:

1. User-specified path
2. Existing seed insights or methodology document already in the repo
3. `docs/seed-insights.md`
4. `.claude/seed-insights.md`

If the repo already uses `CLAUDE.md`, `AGENTS.md`, spec files, architecture docs, or memory-style notes, align with them instead of creating a parallel document that says the same thing.

## Conflict Resolution

If guidance conflicts, use this order:

1. Direct user instruction
2. `CLAUDE.md` and other explicit repo-level instruction files
3. Existing seed insights document
4. Codebase evidence and inferred project principles

Do not silently smooth over real conflicts. If an ambiguity matters, record it under watchpoints or open questions so future sessions do not treat it as settled.

## Mode Selection

Infer the mode from context and proceed without ceremony.

- Bootstrap mode: the project or change direction is still being shaped, and the methodology doc needs to be created or heavily reworked
- Reflection mode: the repo already exists, and you need to extract, refine, or merge durable lessons from what is already there

If the request is ambiguous, state the assumed mode and continue.

## Bootstrap Workflow

### 1. Inspect before interviewing

If a repo is available, inspect it before asking many questions. Read enough to avoid asking for information the code or docs already reveal.

Start with:

1. `CLAUDE.md`, `AGENTS.md`, existing seed docs, architecture docs, or memory docs
2. `README.md` and root config files
3. Main entry points and architecture-heavy directories
4. Test structure and validation commands if they are easy to identify

### 2. Ask only high-value questions

Do not force a rigid ten-question interview. Ask only what is needed to make the document decision-shaping.

Prioritize:

- project goal and primary users
- repo type and expected change velocity
- quality bar, risk tolerance, and release expectations
- architecture pain the user most wants to avoid
- preferred testing, rollout, or compatibility posture

If the repo already answers some of these, do not ask again.

### 3. Build the document around the right axes

Use only the axes that matter for this project:

- product and scope discipline
- decomposition and boundaries
- coupling, cohesion, and extension points
- data model and state ownership
- failure handling and observability
- testing and verification
- rollout, migration, and compatibility
- planning rhythm and change safety
- documentation and memory hygiene
- future agent operating rules

### 4. Write for decisions, not decoration

For each important principle:

- explain why it matters here
- state what good looks like in this repo
- name the anti-patterns to avoid
- include a decision rule when possible

After writing, summarize the key choices and refine if the user wants adjustments.

## Reflection Workflow

### 1. Read the current baseline first

If a seed insights document already exists, read it before analyzing the repo. You need the current baseline in order to detect drift, duplication, and stale guidance.

### 2. Recon the repo structurally

Read in roughly this order:

1. Current seed insights or methodology doc
2. `README.md` and root package or build files
3. Main entry points
4. Architecture-heavy directories such as `src/`, `lib/`, `core/`, `domain/`, or `services/`
5. Test directories and representative test files

Use structural scanning and targeted reads. Do not read the whole repo line by line.

### 3. Classify what you find

Look for:

- abstractions worth preserving
- accidental complexity that should not be repeated
- stable conventions already emerging in code
- architecture drift against existing guidance
- implementation patterns that make change safer

Then classify each candidate insight:

- Keep as principle: reusable across future work
- Keep as pattern: specific but recurring design choice
- Keep as project note: context future sessions must know
- Discard: one-off, obvious, or too temporary

### 4. Merge without bloat

Do not turn the document into a diary.

Prefer:

- merging duplicates
- rewriting vague guidance into concrete rules
- refreshing existing sections when lessons have become clearer
- adding a dated delta only when traceability is genuinely useful

Avoid endless timestamped appendices unless the user explicitly wants a running log.

## Insight Quality Filter

Keep an insight only if most of these are true:

1. Specific: it says what to do in this project
2. Reusable: it is likely to matter again
3. Decision-shaping: it changes future implementation choices
4. Observable: it can be checked in code review, tests, or architecture review
5. Scoped: it states when the rule applies and when it does not

Reject weak insights such as:

- write clean code
- use good architecture
- think before coding
- keep things maintainable

Upgrade them into repo-specific rules or discard them.

## Host Alignment Rules

Use the right artifact for the right job:

- `CLAUDE.md`: always-on instructions, commands, workflow constraints, and short repo rules
- `AGENTS.md`: concise agent-facing behavior and project context when the repo uses it
- feature specs or design docs: task-specific intent and implementation design
- seed insights document: enduring cross-feature methodology and architecture heuristics

The seed insights document should influence specs and future sessions. It should not replace task-specific docs.

## Output Structure

Unless the repo already has a stronger house style, aim for this structure:

1. Purpose and usage
2. Project context snapshot
3. Hard constraints
4. Strong defaults
5. Architecture and design heuristics
6. Delivery and verification heuristics
7. Documentation and memory rules
8. Future agent operating instructions
9. Open questions and watchpoints

## Compression Rule

Prefer a compact, high-signal document over an exhaustive one.

Keep only material that is:

1. likely to matter again
2. capable of changing future decisions
3. not already obvious from existing repo conventions

If the draft is getting bloated, cut repetition first, then local details, then generic rationale. Keep the parts that actually steer work.

## Output Contract

Always produce:

1. The updated or newly created seed insights document
2. A short summary covering:
   - what changed
   - the top durable insights
   - unresolved questions or watchpoints
3. The output path if you wrote into the repo

## Common Mistakes

- Asking a long questionnaire before inspecting the repo
- Recording implementation trivia as if it were durable methodology
- Appending every analysis run instead of curating and merging
- Duplicating large sections from `CLAUDE.md`, `AGENTS.md`, or specs
- Writing principles that cannot influence any future decision
- Praising existing architecture without filtering for what is actually worth preserving

## Final Reminder

Methodologier is not a general planning assistant. Its job is to create or maintain a high-leverage methodology document that improves future Claude work across many sessions, not just the current task.
