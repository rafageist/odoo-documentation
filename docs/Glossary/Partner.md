---
tags: [odoo, glossary, business]
status: active
---

# Partner

## Definition
- A partner is the generic business-party record used for customers, vendors, companies, contacts, and many shared identities in Odoo.
- It is the broad relationship container, not just a CRM contact card.

## Why developers should care
- Many functional areas extend `res.partner` instead of creating their own actor model.
- Requirements that mention customer, vendor, patient, supplier, branch contact, or portal person often still map back to partner logic.

## Technical anchors
- Core model: `[[docs/Core/Master Data/res_partner|res.partner]]`
- Frequent modules: `[[docs/Community Addons/contacts/contacts|contacts]]`, `[[docs/Community Addons/crm/crm|crm]]`, `[[docs/Community Addons/account/account|account]]`

## Related terms
- `[[docs/Glossary/Contact]]`
- `[[docs/Glossary/Commercial Partner]]`
- `[[docs/Glossary/Company]]`

## Navigation
- **Parent:** [[docs/Glossary/Glossary]]
