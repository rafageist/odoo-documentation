---
tags: [odoo, glossary, business]
status: active
---

# Unit of Measure

## Definition
- A unit of measure describes how a quantity is expressed and converted, such as units, boxes, kilograms, hours, or liters.
- In Odoo, it is not just display text; it drives conversions, rounding, and business constraints.

## Why developers should care
- Quantity bugs often come from UoM category mismatches, conversion assumptions, or rounding configuration rather than from broken business formulas.
- Sales, purchasing, stock, manufacturing, and accounting can all read the same quantity differently when units are not aligned.

## Technical anchors
- Core note: `[[docs/Core/Master Data/uom_uom|uom.uom]]`
- Related modules: `[[docs/Community Addons/uom/uom|uom]]`, `[[docs/Community Addons/stock/stock|stock]]`, `[[docs/Community Addons/purchase/purchase|purchase]]`

## Related terms
- `[[docs/Glossary/Product]]`
- `[[docs/Glossary/Product Variant]]`
- `[[docs/Glossary/Picking]]`

## Navigation
- **Parent:** [[docs/Glossary/Glossary]]
