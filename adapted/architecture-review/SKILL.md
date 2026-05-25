---
name: architecture-review
description: Use when reviewing architecture, refactoring module boundaries, improving testability, finding shallow modules, or making a codebase easier for humans and agents to navigate.
---

# Architecture Review

Use this skill to find high-leverage architecture improvements before editing code. The goal is not generic cleanliness. The goal is better locality, smaller interfaces, clearer seams, and tests that verify behavior through public contracts.

## Vocabulary

Use these terms consistently:

- **Module**: anything with an interface and implementation.
- **Interface**: everything callers must know to use a module correctly, including invariants and error modes.
- **Implementation**: code hidden behind the interface.
- **Seam**: the place where behavior can vary without editing callers.
- **Adapter**: a concrete implementation behind a seam.
- **Depth**: leverage behind a small interface.
- **Locality**: change, bugs, and verification concentrated in one place.

Read `references/language.md` when you need the full vocabulary.

## Workflow

1. Read project memory first.
   - `docs/seed-insights.md`, `.claude/seed-insights.md`, or other methodologier output.
   - `CONTEXT.md` or `CONTEXT-MAP.md`.
   - `docs/adr/`.
   - README, feature docs, and tests that explain intended behavior.

2. Explore the codebase.
   - Identify entry points, public interfaces, core workflows, and tests.
   - Follow existing patterns before judging them.
   - Note where understanding one concept requires bouncing across many files.
   - Note where tests must reach through a module instead of crossing its interface.

3. Apply the deepening checks.
   - Deletion test: if deleting a module removes complexity, it may be a pass-through.
   - Caller knowledge test: if every caller repeats the same rules, the module is too shallow.
   - Variation test: one adapter means a hypothetical seam; two adapters means a real seam.
   - Test surface test: if tests need internals, the interface may be wrong.
   - Read `references/deepening-checklist.md` for detail.

4. Present candidates only.
   - Do not implement refactors in this skill.
   - Do not invent new interfaces yet unless the user asks.
   - For each candidate, show involved files, problem, proposed direction, expected leverage, and verification approach.

5. Recommend a next move.
   - Use `interface-design` when a candidate needs alternative interface shapes.
   - Use `domain-model` when architecture friction comes from fuzzy domain language.
   - Use `methodologier` when a reusable architecture lesson should be preserved.

## Output Shape

For each candidate:

- **Area**: module or workflow.
- **Friction**: what makes change or understanding harder.
- **Deepening direction**: what should move behind which interface.
- **Why it helps**: leverage, locality, testability.
- **Risk**: migration or compatibility concern.
- **Verification**: behavior-level checks or tests.

End with a ranked recommendation and the smallest useful next step.

## Common Mistakes

- Do not propose unrelated rewrites.
- Do not equate more abstraction with better architecture.
- Do not split modules only by technical layer if behavior changes together.
- Do not create seams for a single adapter without real variation.
- Do not ignore existing ADRs; challenge them only when current friction justifies reopening them.
