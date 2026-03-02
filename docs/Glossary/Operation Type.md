---
tags: [odoo, glossary, business]
status: active
---

# Operation Type

## Definition
- An operation type is the stock workflow definition that says what kind of warehouse operation a user is executing: receipt, delivery, internal transfer, manufacturing pick, and similar flows.
- It is more than a label; it carries default behavior, routes, and processing rules.

## Why developers should care
- Many stock requirements that users describe as "different forms" or "different transfer behaviors" are actually differences between operation types.
- If a field or rule appears in one picking flow but not another, the first thing to verify is usually the `stock.picking.type`.

## Technical anchors
- Main model: `stock.picking.type`
- Functional module: `[[docs/Community Addons/stock/stock|stock]]`

## Related terms
- `[[docs/Glossary/Warehouse]]`
- `[[docs/Glossary/Picking]]`

## Navigation
- **Parent:** [[docs/Glossary/Glossary]]
