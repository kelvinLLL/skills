# Seed Insights

## 1. Purpose and usage
- What this document is for
- When future agents should consult it
- What kinds of decisions it should shape

## 2. Project context snapshot
- Product / system goal
- Repo type and quality bar
- Expected evolution pattern
- Important constraints or risks

## 3. Hard constraints
- Non-negotiable technical or organizational constraints
- Compatibility, compliance, latency, deployment, or interface limits

## 4. Strong defaults
- Preferred design patterns
- Preferred testing posture
- Preferred data modeling choices
- Preferred rollout / migration style

## 5. Architecture and design heuristics
### 5.1 Decomposition and boundaries
### 5.2 Coupling and extensibility
### 5.3 Data model and state
### 5.4 Error handling and observability
### 5.5 Performance / scale assumptions

For each heuristic, include:
- why it matters here
- what good looks like
- anti-patterns to avoid

## 6. Delivery and verification heuristics
- How work should be broken down
- What should be validated before merging
- Which tests / checks matter most
- How to treat risky refactors or migrations

## 7. Documentation and memory rules
- Which docs are canonical
- What should be updated during implementation
- What should *not* be recorded as durable guidance

## 8. Future-agent operating instructions
- How to use this doc during planning
- How to use it during implementation
- How to use it during review / refactor

## 9. Open questions / watchpoints
- unsettled design choices
- likely future stress points
- things to revisit after the next milestone
