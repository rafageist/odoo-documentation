---
tags: [odoo, glossary, business]
status: active
---

# Picking

## Definition
- A picking is the operational stock document that executes a goods movement, such as receiving, delivering, or transferring items.
- Users often call it a transfer, delivery, receipt, or warehouse operation depending on context.

## Why developers should care
- Stock customizations frequently attach extra fields, validations, labels, or automations to pickings.
- Different user-facing documents may still share the same underlying `stock.picking` model and differ only by operation type, routes, or state.

## Technical anchors
- Main model: `stock.picking`
- Functional module: `[[docs/Community Addons/stock/stock|stock]]`

## Related terms
- `[[docs/Glossary/Operation Type]]`
- `[[docs/Glossary/Warehouse]]`
- `[[docs/Glossary/Product]]`

## Navigation
- **Parent:** [[docs/Glossary/Glossary]]
