---
tags: [odoo, glossary, business]
status: active
---

# Journal

## Definition
- A journal is the accounting bucket that groups entries by purpose, such as customer invoices, vendor bills, bank transactions, cash, or miscellaneous operations.
- In business language, it tells finance users where a transaction belongs before they think about the individual entry lines.

## Why developers should care
- Many accounting flows are configurable mainly through journals: sequences, default accounts, payment methods, posting logic, and reporting behavior.
- Bugs around posting, sequencing, or wrong account defaults are often journal-configuration issues before they are code issues.

## Technical anchors
- Main model: `account.journal`
- Functional module: `[[docs/Community Addons/account/account|account]]`
- Related finance addons: `[[docs/Enterprise Addons/account_reports/account_reports|account_reports]]`

## Related terms
- `[[docs/Glossary/Journal Entry]]`
- `[[docs/Glossary/Company]]`

## Navigation
- **Parent:** [[docs/Glossary/Glossary]]
