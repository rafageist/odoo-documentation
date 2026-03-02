---
tags: [odoo, glossary, business]
status: active
---

# Pricelist

## Definition
- A pricelist is the business rule set that determines how sale prices are chosen, adjusted, or shown for a customer, channel, or context.
- It can encode fixed prices, discount logic, formulas, currency behavior, or segmentation rules.

## Why developers should care
- Pricing requirements rarely belong to a single field on the product. They usually depend on pricelist evaluation.
- Website, Sales, subscriptions, and custom portals often behave differently because they evaluate different pricelists.

## Technical anchors
- Main model family: `product.pricelist`, `product.pricelist.item`
- Related modules: `[[docs/Community Addons/product/product|product]]`, `[[docs/Community Addons/sale_management/sale_management|sale_management]]`, `[[docs/Community Addons/website_sale/website_sale|website_sale]]`

## Related terms
- `[[docs/Glossary/Product]]`
- `[[docs/Glossary/Product Variant]]`
- `[[docs/Glossary/Partner]]`

## Navigation
- **Parent:** [[docs/Glossary/Glossary]]
