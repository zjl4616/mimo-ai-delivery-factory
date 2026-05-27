# Operator Confirmation Rules

The system should run continuously, but the operator only needs to confirm irreversible or identity-sensitive actions.

## Auto-Allowed

- Generate leads from public information.
- Draft first messages and follow-ups.
- Draft public posts and articles.
- Draft proposals, scorecards, handoff docs, and case studies.
- Update internal logs and generated files.
- Publish generic public assets that contain no private customer data.
- Improve the public landing page and repository assets.

## Needs User Confirmation

- Send a message from a personal account where relationship context matters.
- Send a final quote, discount, payment term, invoice, or payment link.
- Accept a contract or statement of work.
- Promise a delivery date to a real client.
- Use or publish a real customer name, private screenshot, private file, or testimonial.
- Buy software, ads, domains, hosting, or paid data.
- Create an account or change security settings on an external platform.

## Confirmation Format

Each run should list confirmation items like this:

```text
NEEDS_USER_CONFIRMATION
- Action:
- Why it matters:
- Recommended yes/no:
- Draft message or terms:
```

If there are no confirmation items, write:

```text
NEEDS_USER_CONFIRMATION
- None
```
