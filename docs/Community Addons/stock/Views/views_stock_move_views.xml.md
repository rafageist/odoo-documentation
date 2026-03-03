---
tags: [odoo, community, generated, views]
---

# views/stock_move_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_move_views.xml`
- Views: 11
- Actions: 6
- Menus: 1
- Rules: 0

## View records

### `view_move_tree_receipt_picking`
- Name: stock.move.tree2
- Model: `stock.move`
- Type: inferred from arch
- Root tag: `list`
- Field references: 12
- Sample fields: `company_id`, `date`, `date_deadline`, `location_dest_id`, `location_id`, `origin`, `picking_id`, `product_id`, `product_uom`, `product_uom_qty`, and 2 more
- XPath or positional patches: 0

### `view_move_search`
- Name: stock.move.search
- Model: `stock.move`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `location_dest_id`, `location_id`, `origin`, `partner_id`, `product_id`, `reference`
- XPath or positional patches: 0

### `view_move_form`
- Name: stock.move.form
- Model: `stock.move`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `company_id`, `date`, `date_deadline`, `location_dest_id`, `location_id`, `move_dest_ids`, `move_orig_ids`, `origin`, `procure_method`, `product_id`, and 4 more
- XPath or positional patches: 0

### `view_stock_move_line_detailed_operation_tree`
- Name: stock.move.line.operations.list
- Model: `stock.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 20
- Sample fields: `company_id`, `is_locked`, `location_dest_id`, `location_id`, `lot_id`, `lot_name`, `lots_visible`, `move_id`, `owner_id`, `package_id`, and 10 more
- Buttons: `action_put_in_pack`
- XPath or positional patches: 0

### `view_stock_move_line_operation_tree`
- Name: stock.move.line.operations.list
- Model: `stock.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 20
- Sample fields: `company_id`, `is_locked`, `location_dest_id`, `location_id`, `lot_id`, `lot_name`, `move_id`, `owner_id`, `package_id`, `picked`, and 10 more
- XPath or positional patches: 0

### `view_stock_move_operations`
- Name: stock.move.operations.form
- Model: `stock.move`
- Type: inferred from arch
- Root tag: `form`
- Field references: 21
- Sample fields: `company_id`, `display_assign_serial`, `display_import_lot`, `has_tracking`, `is_locked`, `location_dest_id`, `location_id`, `move_line_ids`, `picking_code`, `picking_id`, and 11 more
- XPath or positional patches: 0

### `view_move_kandan`
- Name: stock.move.kanban
- Model: `stock.move`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `is_inventory`, `product_id`, `product_qty`, `product_uom`, `product_uom_qty`, `quantity`
- XPath or positional patches: 0

### `view_picking_move_tree`
- Name: stock.picking.move.list
- Model: `stock.move`
- Type: inferred from arch
- Root tag: `list`
- Field references: 20
- Sample fields: `additional`, `company_id`, `date`, `is_initial_demand_editable`, `is_locked`, `is_quantity_done_editable`, `location_dest_id`, `location_id`, `move_lines_count`, `packaging_uom_id`, and 10 more
- XPath or positional patches: 0

### `view_move_tree`
- Name: stock.move.list
- Model: `stock.move`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `company_id`, `date`, `location_dest_id`, `location_dest_usage`, `location_id`, `location_usage`, `picking_type_id`, `product_id`, `product_uom`, `product_uom_qty`, and 3 more
- XPath or positional patches: 0

### `view_move_graph`
- Name: stock.move.graph
- Model: `stock.move`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `location_dest_id`, `product_id`, `product_uom_qty`
- XPath or positional patches: 0

### `view_move_pivot`
- Name: stock.move.pivot
- Model: `stock.move`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `date`, `picking_type_id`
- XPath or positional patches: 0

## Actions

- `action_stock_move_kanban_all`: `view`
- `action_stock_move_graph_all`: `view`
- `action_stock_move_pivot_all`: `view`
- `action_stock_move_form_all`: `view`
- `action_stock_move_tree_all`: `view`
- `stock_move_action`: `act_window` Moves Analysis

## Menus

- `stock_move_menu`: Moves Analysis

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

