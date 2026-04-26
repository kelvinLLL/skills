# Deepening Checklist

Use this checklist to identify architecture improvements worth discussing.

## Good Candidates

- Multiple callers repeat the same validation, state transition, or ordering rule.
- Tests duplicate setup because the public interface is not expressive enough.
- A workflow is scattered across small helpers that must be understood together.
- A module exposes flags, callbacks, or config that force callers to know implementation details.
- A file is large because it owns a coherent behavior, but callers see only a small contract. This may already be deep, not bad.
- A file is small because it delegates everything and adds no leverage. This may be shallow.

## Weak Candidates

- Refactor would only rename files.
- Refactor adds an interface with one adapter and no expected variation.
- Refactor improves aesthetic layering but not behavior locality.
- Refactor contradicts an ADR without strong current evidence.
- Refactor makes tests more coupled to implementation.

## Questions To Answer

- What behavior would be easier to test after this change?
- Which callers become simpler?
- Which domain rule moves behind the interface?
- What compatibility risk exists?
- Can the change be sliced so every step leaves behavior working?
