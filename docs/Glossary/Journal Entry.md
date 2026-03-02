---
tags: [odoo, glossary, business]
status: active
---

# Journal Entry

## Definition
- A journal entry is the accounting document that records debits and credits for a transaction.
- In modern Odoo terminology, the same `account.move` object also underpins invoices and several other posted finance documents.

## Why developers should care
- Developers who treat invoices and journal entries as unrelated objects usually miss important accounting side effects.
- Posting logic, reconciliation, taxes, assets, and many finance automations converge on `account.move` and its lines.

## Technical anchors
- Main models: `account.move`, `account.move.line`
- Functional module: `[[docs/Community Addons/account/account|account]]`
- Related enterprise note: `[[docs/Enterprise Addons/account_asset/account_asset|account_asset]]`

## Related terms
- `[[docs/Glossary/Journal]]`
- `[[docs/Glossary/Company]]`

## Navigation
- **Parent:** [[docs/Glossary/Glossary]]
