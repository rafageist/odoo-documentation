<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_quant_views.xml

- Module: [[docs/Community Addons/stock_account/stock_account|stock_account]]
- Scope: Community Addons
- Source file: `views/stock_quant_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_stock_quant_tree_inventory_editable_inherit_stock_account`
- Name: stock.quant.inventory.list.editable.inherit.stock.account
- Model: `stock.quant`
- Type: inferred from arch
- Inherits: `stock.view_stock_quant_tree_inventory_editable`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `accounting_date`
- XPath or positional patches: 1

### `view_stock_quant_tree_editable_inherit`
- Name: stock.quant.list.editable.inherit
- Model: `stock.quant`
- Type: inferred from arch
- Inherits: `stock.view_stock_quant_tree_editable`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `cost_method`, `currency_id`, `value`
- XPath or positional patches: 1

### `view_stock_quant_tree_inherit`
- Name: stock.quant.list.inherit
- Model: `stock.quant`
- Type: inferred from arch
- Inherits: `stock.view_stock_quant_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `currency_id`, `value`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/stock_account/Views]]

<!-- GENERATED:VIEWFILE -->
