---
tags: [odoo, glossary, business]
status: active
---

# Product Variant

## Definition
- A product variant is one concrete sellable or stockable combination generated from a product template and its attributes.
- In business terms, it is the actual SKU or item instance that users select after choosing options such as size, color, or configuration.

## Why developers should care
- Inventory, stock moves, procurement, barcodes, and many integrations operate at the variant level, not at the abstract product template level.
- A customization that writes to the wrong level will often look correct in the UI but fail operationally in stock or pricing flows.

## Technical anchors
- Core note: `[[docs/Core/Master Data/product_product|product.product]]`
- Template note: `[[docs/Core/Master Data/product_template|product.template]]`
- Related modules: `[[docs/Community Addons/product/product|product]]`, `[[docs/Community Addons/stock/stock|stock]]`

## Related terms
- `[[docs/Glossary/Product]]`
- `[[docs/Glossary/Unit of Measure]]`
- `[[docs/Glossary/Pricelist]]`

## Navigation
- **Parent:** [[docs/Glossary/Glossary]]
