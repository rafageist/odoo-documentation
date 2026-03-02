<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_quant_views.xml

- Module: [[docs/Community Addons/product_expiry/product_expiry|product_expiry]]
- Scope: Community Addons
- Source file: `views/stock_quant_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `quant_search_view_inherit_product_expiry`
- Name: stock.quant.search.inherit
- Model: `stock.quant`
- Type: inferred from arch
- Inherits: `stock.quant_search_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_stock_quant_tree_inventory_editable`
- Name: stock.quant.inventory.list.editable.inherit.expiry_date
- Model: `stock.quant`
- Type: inferred from arch
- Inherits: `stock.view_stock_quant_tree_inventory_editable`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `expiration_date`, `removal_date`, `use_expiration_date`
- XPath or positional patches: 1

### `view_stock_quant_tree_editable`
- Name: stock.quant.list.editable.inherit.expiry_date
- Model: `stock.quant`
- Type: inferred from arch
- Inherits: `stock.view_stock_quant_tree_editable`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `expiration_date`, `removal_date`, `use_expiration_date`
- XPath or positional patches: 1

### `view_stock_quant_tree`
- Name: stock.quant.list.inherit.expiry_date
- Model: `stock.quant`
- Type: inferred from arch
- Inherits: `stock.view_stock_quant_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `removal_date`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/product_expiry/Views]]

<!-- GENERATED:VIEWFILE -->
