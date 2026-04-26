---
name: ubiquitous-language
description: Use when extracting a quick project glossary, resolving overloaded terms, naming domain concepts, or turning conversation/code language into reusable domain vocabulary.
---

# Ubiquitous Language

Use this skill when the project needs a fast, durable glossary but does not yet need a full domain-model session.

## Workflow

1. Gather evidence.
   - Scan the current conversation.
   - Read existing `CONTEXT.md`, `CONTEXT-MAP.md`, or `UBIQUITOUS_LANGUAGE.md` if present.
   - Skim relevant code, tests, docs, and issue text when available.

2. Extract candidate terms.
   - Domain nouns: actors, resources, lifecycle states, events, policies.
   - Domain verbs: actions users or systems perform.
   - Relationship words: owns, belongs to, emits, consumes, derives from.

3. Flag language problems.
   - One word used for different concepts.
   - Multiple words used for one concept.
   - Generic terms hiding real domain meaning.
   - Names that conflict with code behavior or existing documentation.

4. Produce a glossary.
   - Prefer the existing project glossary file.
   - If no domain document exists, write `UBIQUITOUS_LANGUAGE.md`.
   - If the user is actively doing domain modeling, write or update `CONTEXT.md` instead.

## Output Format

```md
# Ubiquitous Language

## Terms

| Term | Definition | Avoid |
| --- | --- | --- |
| **Customer** | A person or organization that places orders. | client, buyer, account |

## Relationships

- A **Customer** can place many **Orders**.

## Example Dialogue

> Dev: "Can a **Customer** have multiple **Orders**?"
> Domain expert: "Yes. Each **Order** belongs to exactly one **Customer**."

## Flagged Ambiguities

- "account" appears to mean both **Customer** and **User**. Recommended split: keep both terms distinct.
```

## Rules

- Keep definitions to one sentence.
- Pick canonical terms. Do not list synonyms without choosing.
- Avoid class names unless the class name is also a real domain term.
- Do not include generic programming vocabulary.
- If a term has unresolved meaning, mark it under ambiguities instead of pretending it is settled.

## Escalate To Domain Model

Use `domain-model` when the glossary reveals decisions about ownership, lifecycle, cross-context relationships, or ADR-worthy trade-offs.

<!-- Skill Supervisor Footer -->
## Skill Supervisor Footer

When this supervised skill is used, append one sanitized JSONL record to `~/.codex/skill-supervisor/usage.jsonl`.

Suggested record:

```json
{"timestamp":"<ISO-8601 UTC>","skill": "ubiquitous-language","workspace":"<workspace basename or unknown>","trigger":"<short non-sensitive reason>","task_type":"<planning|implementation|review|research|other>","outcome":"<started|completed|blocked|skipped>","verification":"<passed|failed|not_run|not_applicable>"}
```

Only record metadata. Do not record secrets, credentials, full prompts, file contents, private user data, or long task transcripts. If logging is unavailable, continue the task normally.

If the `skill-supervisor` skill is installed globally, prefer its helper script:

```bash
python3 ~/.codex/skills/skill-supervisor/scripts/log_usage.py --skill "ubiquitous-language" --trigger "<short non-sensitive reason>" --task-type "<type>" --outcome "<outcome>" --verification "<status>"
```
