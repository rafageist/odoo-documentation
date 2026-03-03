---
tags: [odoo, community, generated, views]
---

# views/production_lot_views.xml

- Module: [[docs/Community Addons/product_expiry/product_expiry|product_expiry]]
- Scope: Community Addons
- Source file: `views/production_lot_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_production_lot_view_kanban`
- Name: stock.production.lot.kanban.inherit.product.expiry
- Model: `stock.lot`
- Type: inferred from arch
- Inherits: `stock.view_production_lot_kanban`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `alert_date`, `expiration_date`, `product_expiry_alert`, `product_qty`, `removal_date`
- XPath or positional patches: 3

### `view_production_lot_view_tree`
- Name: stock.production.lot.list.inherit.product.expiry
- Model: `stock.lot`
- Type: inferred from arch
- Inherits: `stock.view_production_lot_tree`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `alert_date`, `expiration_date`, `product_qty`, `removal_date`, `use_date`
- XPath or positional patches: 1

### `search_product_lot_filter_inherit_product_expiry`
- Name: stock.production.lot.search.inherit
- Model: `stock.lot`
- Type: inferred from arch
- Inherits: `stock.search_product_lot_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_move_form_expiry`
- Name: stock.production.lot.inherit.form
- Model: `stock.lot`
- Type: inferred from arch
- Inherits: `stock.view_production_lot_form`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `alert_date`, `expiration_date`, `product_expiry_alert`, `removal_date`, `use_date`, `use_expiration_date`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Community Addons/product_expiry/Views]]

