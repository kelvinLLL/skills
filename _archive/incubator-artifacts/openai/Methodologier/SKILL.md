---
name: methodologier
description: Build or continuously improve a project's seed insight document before or during AI-assisted development. Use this skill whenever the user asks to create a seed methodology doc, insight doc, architecture principles doc, engineering playbook, design heuristics file, planning rules, implementation guardrails, project memory, or wants the agent to extract reusable architectural / process insights from an existing codebase and write them back into a persistent document. Also use it when spec-driven development, steering, AGENTS.md / CLAUDE.md quality, decoupling, maintainability, extensibility, refactor safety, implementation planning, or long-horizon AI coding quality is a central concern, even if the user does not explicitly ask for an "insight" document.
---

# Methodologier

Turn scattered methodology, architecture taste, and project lessons into a durable seed insight document that improves future AI work.

## What this skill does

Operate in two modes:

1. **Bootstrap mode**: before implementation starts, interview the user, inspect the repo if available, and create a high-quality seed insight document that will guide later spec-driven work.
2. **Reflection mode**: during development, inspect the current project state and extract fresh, evidence-backed insights worth preserving, then merge them into the same document without bloating it.

Treat the insight document as **steering + memory + architecture review notes**, not as vague motivational prose.

## Default output location

Prefer one of these, in order:

1. User-specified path
2. `docs/methodologier/seed-insights.md`
3. `.claude/context/seed-insights.md`
4. `docs/seed-insights.md`

If the repo already has `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/`, `memory-bank/`, or `specs/`, align with them instead of creating parallel conflicting docs.

## Mode selection

Infer the mode from context.

Use **Bootstrap mode** when the user is starting a project, feature, refactor, migration, framework build, platform design, or asks for principles / methods / planning.

Use **Reflection mode** when the repo already exists and the user asks to review architecture, summarize current good practices, harvest reusable lessons, improve project guidance, or update the seed document after implementation work.

If the request is ambiguous, do not block on it. State the assumed mode and proceed.

## Core rules

- Ground every insight in one of three sources: explicit user intent, codebase evidence, or strong cross-project engineering principles.
- Prefer **decision-enabling guidance** over generic advice.
- Distinguish **hard constraints**, **strong defaults**, and **situational heuristics**.
- Prefer compact, high-signal bullets over long essays.
- Avoid duplicating content that already exists elsewhere; reference or consolidate instead.
- When reviewing an existing project, do not praise blindly. Preserve only insights that are likely to improve future work.
- Never turn temporary implementation details into enduring methodology unless they are clearly reusable.

## Bootstrap workflow

### Step 1: gather context fast

Ask only the highest-value questions. Prioritize:

- project goal and users
- repo type (greenfield / brownfield / framework / app / platform / library)
- expected change velocity
- quality bar (prototype / internal / production / multi-team)
- architectural pain the user most wants to avoid
- preferred tech / testing / release constraints

If the repo is available, inspect it before asking too many questions.

### Step 2: identify methodology axes

Populate the seed document around the axes that matter most:

- product and scope discipline
- decomposition and boundaries
- coupling / cohesion / interface design
- data model design
- failure handling and observability
- testing and verification strategy
- migration / rollout / compatibility rules
- planning and execution rhythm
- documentation and memory hygiene
- AI-agent operating rules

Skip axes that are irrelevant.

### Step 3: write the seed insight document

Use the template in `assets/seed-insights-template.md` as the default structure.

When writing principles:

- explain *why* the principle exists
- define what good looks like in this project
- mention anti-patterns to avoid
- include concrete decision rules when possible

### Step 4: make it actionable

Conclude with a short “How future agents should use this doc” section that tells the agent how to apply the document during planning, implementation, review, and refactor work.

## Reflection workflow

### Step 1: inspect current state

Inspect relevant files, architecture boundaries, docs, tests, and recent patterns.

Look for:

- clean abstractions worth preserving
- accidental complexity to explicitly avoid repeating
- stable conventions already emerging in the repo
- places where a principle is missing and future AI work would drift
- implementation patterns that make iteration safer

### Step 2: classify findings

Sort candidate insights into:

- **keep as principle**: reusable beyond the current task
- **keep as pattern**: specific but recurring design choice
- **keep as project note**: context that future work must know
- **discard**: too local, too temporary, or too obvious

### Step 3: merge without bloat

Update the seed insight document by:

- preserving section structure
- merging duplicates
- rewriting vague statements into concrete guidance
- adding a dated `Delta` or `New lessons` subsection only when it aids traceability

Do not append endless changelog-style notes.

## Insight quality rubric

A high-quality insight usually has all or most of these properties:

1. **Specific**: says what to do in this project, not generic wisdom
2. **Reusable**: likely to matter again
3. **Decision-shaping**: changes future implementation choices
4. **Observable**: can be checked in code review or tests
5. **Scoped**: names when the rule applies and when it does not

Reject insights like:

- “write clean code”
- “use good architecture”
- “think before coding”

Upgrade them into project-specific rules.

## Mandatory structure for the generated document

Unless the repo already has a stronger house style, generate a document with these sections:

1. Purpose and usage
2. Project context snapshot
3. Hard constraints
4. Strong defaults
5. Architecture and design heuristics
6. Delivery and verification heuristics
7. Documentation / memory rules
8. Future-agent operating instructions
9. Open questions / watchpoints

## Architecture review checklist

When architecture is central, explicitly evaluate:

- Are responsibilities separated cleanly?
- Are domain concepts explicit in the data model?
- Are public interfaces smaller and more stable than internal implementation details?
- Does the design allow partial replacement, testing, or parallel work?
- Are workflows coupled through hidden state, shared utilities, or leaky abstractions?
- Are there boundaries where contracts should be documented more clearly?
- Is complexity located in the right layer?

## Planning review checklist

When project execution is central, explicitly evaluate:

- Is work broken into decision-reducing increments?
- Are risky unknowns surfaced early?
- Are acceptance checks defined before implementation expands?
- Is there a clear distinction between exploration, committed design, and execution?
- Will future AI sessions understand what is stable vs still in flux?

## Output requirements

Always produce:

1. The updated or newly created insight document
2. A short summary covering:
   - what changed
   - top 3 durable insights
   - any unresolved questions

If you are writing into the repo, show the path.

## When to read bundled resources

- Read `references/insight-taxonomy.md` when you need examples of high-value insight categories.
- Read `references/host-ecosystem-notes.md` when the repo already uses spec / steering / memory patterns and you need to align instead of duplicating.
- Read `assets/seed-insights-template.md` when creating a fresh document or heavily restructuring an existing one.

## Example invocation patterns

- “Before we start coding, help me build a seed methodology doc for this framework project.”
- “Review the current repo and update our insight document with the architecture lessons worth preserving.”
- “Create a project playbook so future coding agents don’t over-couple modules.”
- “Summarize the best design patterns already present in this codebase and write them into our seed doc.”

## Final reminder

This skill is not a generic planning assistant. Its job is to create or maintain a **high-leverage, reusable methodology artifact** that makes future specification, implementation, and review work better.
