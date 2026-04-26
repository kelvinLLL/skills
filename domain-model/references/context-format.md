# CONTEXT.md Format

Use this format for domain language that should guide future specs, code, tests, and issues.

```md
# Context Name

One or two sentences describing this domain context and why it exists.

## Language

**Order**:
A customer's request to purchase one or more items.
Avoid: purchase, transaction

**Invoice**:
A request for payment sent to a customer after delivery.
Avoid: bill, payment request

## Relationships

- An **Order** produces one or more **Invoices**.
- An **Invoice** belongs to exactly one **Customer**.

## Example Dialogue

> Dev: "When a **Customer** places an **Order**, do we create the **Invoice** immediately?"
> Domain expert: "No. An **Invoice** is generated after **Fulfillment** is confirmed."

## Flagged Ambiguities

- "account" was used for both **Customer** and **User**. Resolved: these are distinct concepts.
```

## Rules

- Be opinionated: pick canonical terms and list aliases to avoid.
- Keep definitions to one sentence.
- Define what the thing is, not what code does with it.
- Include only terms that matter to domain experts.
- Show relationships and cardinality where obvious.
- Use examples to clarify boundaries between related concepts.

## Multi-Context Repos

When several bounded contexts exist, create a root `CONTEXT-MAP.md`:

```md
# Context Map

## Contexts

- [Ordering](./src/ordering/CONTEXT.md) - receives and tracks customer orders.
- [Billing](./src/billing/CONTEXT.md) - generates invoices and processes payments.

## Relationships

- **Ordering -> Billing**: Ordering emits `OrderPlaced`; Billing consumes it.
```

Only create this when more than one context is real.
