---
name: interface-design
description: Use when designing software module interfaces, public APIs, seams, adapters, contracts, or comparing alternative shapes for code-facing interfaces.
---

# Interface Design

Use this skill when the important question is "what should callers know?" It is for software interfaces, APIs, module seams, and contracts. For visual interface work, use `ui-ux-pro-max` instead.

## Core Principle

Design it more than once. The first interface is usually anchored to the current implementation. Better designs appear when you compare genuinely different caller experiences.

## Workflow

1. Frame the problem.
   - What behavior should the module provide?
   - Who are the callers?
   - What invariants, ordering rules, errors, and performance expectations matter?
   - What should be hidden in the implementation?
   - What existing code and tests already constrain the shape?

2. Generate alternatives.
   - Default: produce 3 local designs in this session.
   - Only use subagents when the user explicitly asks for parallel agent work.
   - Make alternatives meaningfully different, not small syntax variants.

3. For each design, show:
   - Interface signature or contract.
   - Usage example from the caller perspective.
   - What the implementation hides.
   - How dependencies or adapters fit.
   - Test strategy through the public interface.
   - Trade-offs and likely misuse modes.

4. Compare in prose.
   - Simplicity for common callers.
   - Flexibility for uncommon callers.
   - Depth: behavior per unit of interface.
   - Locality: where future changes concentrate.
   - Migration cost from current code.

5. Recommend one option.
   - Prefer a strong recommendation over a neutral menu.
   - If a hybrid is best, name which pieces come from which alternatives.
   - List the smallest tracer-bullet implementation path.

## Design Lenses

Use these constraints to force different shapes:

- Minimal surface: one to three entry points.
- Common-case optimized: default use is trivial.
- Flexible: extension points are explicit.
- Ports and adapters: external systems sit behind seams.
- Batch/workflow: module owns ordering and lifecycle.

## Common Mistakes

- Do not expose implementation steps as interface methods.
- Do not add config for hypothetical callers.
- Do not let tests become the only caller that needs a seam.
- Do not design around mocks instead of real behavior.
- Do not call something an interface if callers still need to know the implementation rules.
