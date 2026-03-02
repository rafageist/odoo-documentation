---
tags: [odoo, glossary, business]
status: active
---

# Commercial Partner

## Definition
- A commercial partner is the top-level company entity used by Odoo to consolidate business relationships across child contacts, invoice addresses, and delivery addresses.
- It is not a separate business actor in the UI; it is the grouping concept behind many sales and accounting behaviors.

## Why developers should care
- Commercial fields, receivables, fiscal behavior, and partner deduplication often resolve to the commercial partner instead of the visible child contact.
- Bugs that look like "wrong customer", "wrong invoice owner", or "shared credit/accounting data" often come from misunderstanding this layer.

## Technical anchors
- Core model: `[[docs/Core/Master Data/res_partner|res.partner]]`
- Frequent modules: `[[docs/Community Addons/account/account|account]]`, `[[docs/Community Addons/crm/crm|crm]]`, `[[docs/Community Addons/contacts/contacts|contacts]]`

## Related terms
- `[[docs/Glossary/Partner]]`
- `[[docs/Glossary/Contact]]`
- `[[docs/Glossary/Company]]`

## Navigation
- **Parent:** [[docs/Glossary/Glossary]]
