---
tags: [odoo, glossary, business]
status: active
---

# Contact

## Definition
- A contact is usually a child `res.partner` record linked to a parent company or partner.
- In business terms, it represents a person or a specific address role such as invoice, delivery, or private contact data under a broader partner relationship.

## Why developers should care
- Developers often confuse contacts with independent customers or vendors, but Odoo usually stores them inside the same partner model.
- Address routing, portal access, emails, and commercial ownership may resolve differently depending on whether the record is a parent partner or a child contact.

## Technical anchors
- Core model: `[[docs/Core/Master Data/res_partner|res.partner]]`
- Functional surface: `[[docs/Community Addons/contacts/contacts|contacts]]`

## Related terms
- `[[docs/Glossary/Partner]]`
- `[[docs/Glossary/Commercial Partner]]`
- `[[docs/Glossary/Company]]`

## Navigation
- **Parent:** [[docs/Glossary/Glossary]]
