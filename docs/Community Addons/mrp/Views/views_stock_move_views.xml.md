<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_move_views.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `views/stock_move_views.xml`
- Views: 6
- Actions: 1
- Menus: 3
- Rules: 0

## View records

### `view_move_line_tree`
- Name: stock.move.line.list
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.view_move_line_tree`
- Root tag: `field`
- Field references: 1
- Sample fields: `reference`
- XPath or positional patches: 0

### `stock_move_line_view_search`
- Name: stock.move.line.search
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.stock_move_line_view_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_stock_move_line_operation_tree_finished`
- Name: stock.move.line.operation.list.finished
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.view_stock_move_line_operation_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_mrp_stock_move_operations`
- Name: stock.move.mrp.operations.raw.form
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `stock.view_stock_move_operations`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `quantity`
- XPath or positional patches: 1

### `view_stock_move_operations_finished`
- Name: stock.move.operations.finished.form
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `stock.view_stock_move_operations`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_stock_move_operations_raw`
- Name: stock.move.operations.raw.form
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `stock.view_stock_move_operations`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `action_mrp_production_moves`: `act_window` Inventory Moves

## Menus

- `menu_procurement_compute_mrp`: unnamed
- `menu_mrp_scrap`: Scrap
- `menu_mrp_traceability`: Lots/Serial Numbers

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

<!-- GENERATED:VIEWFILE -->
