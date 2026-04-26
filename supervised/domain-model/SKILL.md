---
name: domain-model
description: Use when project work needs precise domain terms, CONTEXT.md updates, ADR decisions, DDD language, or plans/specs must be checked against business concepts before coding.
---

# Domain Model

Use this skill to make project language explicit before implementation or architecture work hardens around fuzzy terms.

## Core Principle

Names are design. If the team uses one word for two concepts, or two words for one concept, code and specs will drift. Resolve the language first, then let modules, tests, and issues inherit it.

## Workflow

1. Inspect before asking.
   - Read `CONTEXT-MAP.md` if it exists.
   - Read the relevant `CONTEXT.md`.
   - Read nearby ADRs under `docs/adr/` or context-local `docs/adr/`.
   - Skim code, tests, feature docs, and issues that already use the terms.

2. Find language risks.
   - Same word used for different concepts.
   - Different words used for the same concept.
   - Vague verbs such as "process", "handle", "sync", "manage", "resolve".
   - Terms that disagree with existing code behavior.
   - Hidden lifecycle states or ownership rules.

3. Resolve one decision at a time.
   - If code answers the question, cite the code behavior and avoid asking.
   - If code and user intent conflict, surface the conflict directly.
   - Ask one focused question only when the answer cannot be inferred safely.
   - Provide your recommended answer with the question.

4. Update domain documentation as decisions crystallize.
   - Single-context repo: root `CONTEXT.md`.
   - Multi-context repo: `CONTEXT-MAP.md` plus context-local `CONTEXT.md`.
   - Create files lazily only when there is resolved language to record.
   - Use `references/context-format.md`.

5. Record ADRs sparingly.
   - Offer an ADR only when the decision is hard to reverse, surprising without context, and the result of a real trade-off.
   - Use `references/adr-format.md`.

## Output

Always finish with:

- Terms resolved.
- Ambiguities still open.
- Files updated.
- Any ADR offered or created.

## Relationship To Other Skills

- Use `ubiquitous-language` for a quick glossary extraction without a full interview.
- Use `architecture-review` after domain terms are stable enough to judge module seams.
- Use `methodologier` for durable cross-project engineering principles, not domain vocabulary.

## Common Mistakes

- Do not add generic programming terms to `CONTEXT.md`.
- Do not couple domain language to class names or file paths.
- Do not create ADRs for obvious or easily reversible choices.
- Do not let a glossary become a diary. Keep it concise and decision-shaping.

<!-- Skill Supervisor Footer -->
## Skill Supervisor Footer

When this supervised skill is used, append one sanitized JSONL record to `~/.codex/skill-supervisor/usage.jsonl`.

Suggested record:

```json
{"timestamp":"<ISO-8601 UTC>","skill": "domain-model","workspace":"<workspace basename or unknown>","trigger":"<short non-sensitive reason>","task_type":"<planning|implementation|review|research|other>","outcome":"<started|completed|blocked|skipped>","verification":"<passed|failed|not_run|not_applicable>"}
```

Only record metadata. Do not record secrets, credentials, full prompts, file contents, private user data, or long task transcripts. If logging is unavailable, continue the task normally.

If the `skill-supervisor` skill is installed globally, prefer its helper script:

```bash
python3 ~/.codex/skills/skill-supervisor/scripts/log_usage.py --skill "domain-model" --trigger "<short non-sensitive reason>" --task-type "<type>" --outcome "<outcome>" --verification "<status>"
```
