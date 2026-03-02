---
tags: [odoo, glossary, business]
status: active
---

# Company

## Definition
- A company is the legal and accounting entity under which transactions, journals, warehouses, taxes, and security boundaries are scoped.
- In multi-company setups, it is one of the strongest business separators in the whole system.

## Why developers should care
- Company context changes defaults, record visibility, journal selection, taxes, stock behavior, and cross-company validation.
- A requirement that sounds purely business-oriented, such as "this should belong to company B only", usually has direct ORM and security impact.

## Technical anchors
- Core model: `[[docs/Core/Master Data/res_company|res.company]]`
- Related infrastructure note: `[[docs/Core/Infrastructure/Security]]`
- Frequent modules: `[[docs/Community Addons/account/account|account]]`, `[[docs/Community Addons/stock/stock|stock]]`

## Related terms
- `[[docs/Glossary/Journal]]`
- `[[docs/Glossary/Warehouse]]`
- `[[docs/Glossary/Partner]]`

## Navigation
- **Parent:** [[docs/Glossary/Glossary]]
