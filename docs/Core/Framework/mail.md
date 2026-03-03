---
tags: [core, framework, mail]
status: active
---

# mail (Core Framework)

## Focus
- `mail.thread`, activities, notifications, and Discuss-facing message transport.
- Real-time updates over bus/longpolling and client refresh behavior.
- Composer, followers, aliases, and activity scheduling as shared runtime services.

## Runtime boundary
- `mail.thread` is both a collaboration mixin and the entry point for inbound email routing.
- The framework-side contract stops at shared message parsing, alias routing, follower notifications, and bus-driven refresh.
- Business record creation from incoming mail belongs to model overrides such as `message_new(...)` and `message_update(...)`, not to generic controller code.

## Shared services
- Message ingestion converges on `mail.thread.message_process(...)`, whether the source is `fetchmail.server` or the local `odoo-mailgate.py` pipe script.
- Bounce handling and unroutable alias behavior are framework-level concerns before any business module-specific interpretation happens.
- Real-time message refresh is a separate concern handled through `bus`, which is why mail UX issues often need both `mail.thread` and `bus` traces.

## Related notes
- `[[docs/Core/Integrations/Mail Gateway]]` for inbound mail transport, alias routing, and failure semantics.
- `[[docs/Core/Infrastructure/Bus]]` for live notification delivery.

## Navigation
- **Parent:** [[docs/Core/Framework/Framework]]
