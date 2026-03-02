<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_move_views.xml

- Module: [[docs/Community Addons/product_expiry/product_expiry|product_expiry]]
- Scope: Community Addons
- Source file: `views/stock_move_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_stock_move_line_detailed_operation_tree_expiry`
- Name: stock.move.line.operations.inherit.list
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.view_stock_move_line_detailed_operation_tree`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `expiration_date`, `is_expired`, `picking_type_use_existing_lots`, `removal_date`, `tracking`
- XPath or positional patches: 2

### `view_stock_move_line_operation_tree_expiry`
- Name: stock.move.line.inherit.list
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.view_stock_move_line_operation_tree`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `expiration_date`, `is_expired`, `picking_type_use_existing_lots`, `removal_date`
- XPath or positional patches: 2

### `view_stock_move_operations_expiry`
- Name: stock.move.operations.inherit.form
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `stock.view_stock_move_operations`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `picking_code`, `use_expiration_date`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/product_expiry/Views]]

<!-- GENERATED:VIEWFILE -->
