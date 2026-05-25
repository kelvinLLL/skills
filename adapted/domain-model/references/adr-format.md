# ADR Format

ADRs live in `docs/adr/` unless the project already has another ADR location.

Use sequential names:

```text
docs/adr/0001-short-slug.md
docs/adr/0002-short-slug.md
```

## Minimal Template

```md
# Short Decision Title

One to three sentences: what context existed, what was decided, and why.
```

## Optional Sections

Only add sections when they genuinely help a future reader.

- Status: proposed, accepted, deprecated, superseded.
- Considered Options.
- Consequences.

## When To Create

Create or offer an ADR only when all are true:

- Hard to reverse.
- Surprising without context.
- Result of a real trade-off.

Skip ADRs for obvious implementation details, easily reversible choices, or temporary delivery notes.
