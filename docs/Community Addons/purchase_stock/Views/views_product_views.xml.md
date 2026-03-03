---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/purchase_stock/purchase_stock|purchase_stock]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_view_search_catalog`
- Name: purchase.view.search.catalog.inherit.purchase_stock
- Model: `product.product`
- Type: inferred from arch
- Inherits: `purchase.product_view_search_catalog`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `product_view_kanban_catalog_purchase_only`
- Name: product.view.kanban.catalog.purchase_stock
- Model: `product.product`
- Type: inferred from arch
- Inherits: `purchase.product_view_kanban_catalog_purchase_only`
- Root tag: `field`
- Field references: 7
- Sample fields: `id`, `monthly_demand`, `qty_available`, `suggested_qty`, `type`, `uom_id`, `virtual_available`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Community Addons/purchase_stock/Views]]

