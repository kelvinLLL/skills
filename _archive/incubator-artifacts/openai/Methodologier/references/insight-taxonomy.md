# Insight taxonomy for Methodologier

Use this file when you need concrete examples of what is worth preserving in a seed insight document.

## 1. Product and scope discipline

High-value insights:
- Prefer a thin end-to-end vertical slice before broad feature coverage.
- Separate “exploration-only” decisions from committed product guarantees.
- Write acceptance criteria around user-visible outcomes, not implementation steps.

Weak insights:
- “Keep scope small.”
- “Make sure the product is useful.”

## 2. Boundary and decomposition rules

High-value insights:
- Keep orchestration logic out of domain objects; let domain components expose explicit interfaces.
- Put unstable vendor / API integrations behind thin adapters.
- Prefer composition over cross-module inheritance when behavior will diverge by domain.

Signals to preserve:
- clean adapter layers
- anti-corruption layers
- explicit module APIs
- narrow internal contracts

## 3. Data model and state management

High-value insights:
- Stabilize the canonical data model early; derive presentation shapes at the edges.
- Avoid passing untyped / catch-all dictionaries across major boundaries when the domain is still evolving.
- Separate persisted state, derived state, and transient execution state.

## 4. Reliability and change safety

High-value insights:
- Every non-trivial refactor should preserve an executable behavioral check.
- Hide risky migrations behind compatibility shims or staged rollout flags.
- Prefer observable failure modes over silent fallback when debugging cost is high.

## 5. Testing heuristics

High-value insights:
- Put most tests at the contract / behavior layer where they survive refactors.
- Use end-to-end tests only for critical workflows and integration seams.
- For generated code or AI-written code, require one validation step that checks the most failure-prone assumption.

## 6. Documentation and memory hygiene

High-value insights:
- Keep one canonical methodology document and reference it from agent-facing files.
- Record open questions explicitly so future sessions do not treat them as settled design.
- Update the insight document only when a lesson is reusable, not after every tiny implementation change.

## 7. AI-agent operating rules

High-value insights:
- Require the agent to distinguish hard constraints from defaults before proposing a plan.
- Require design review before cross-cutting changes.
- Prefer localized edits that preserve existing abstractions unless the task explicitly authorizes restructuring.

## 8. Project execution methodology

High-value insights:
- Do architecture decisions before task fan-out when multiple modules will be touched.
- Surface irreversible choices early: schemas, public APIs, extension points, deployment constraints.
- Break work into steps that each reduce uncertainty, not just move files around.

## Compression rule

When the draft gets too long, keep only items that are:
1. likely to matter again,
2. capable of changing future decisions, and
3. not already obvious from the codebase conventions.
