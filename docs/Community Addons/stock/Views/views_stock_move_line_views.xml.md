<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_move_line_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_move_line_views.xml`
- Views: 7
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `view_stock_move_line_pivot`
- Name: stock.move.line.pivot
- Model: `stock.move.line`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `date`, `product_category_name`
- XPath or positional patches: 0

### `view_stock_move_line_kanban`
- Name: stock.move.line.kanban
- Model: `stock.move.line`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 11
- Sample fields: `date`, `location_dest_id`, `location_id`, `lot_id`, `lot_name`, `product_id`, `product_uom_id`, `quant_id`, `quantity`, `reference`, and 1 more
- XPath or positional patches: 0

### `stock_move_line_view_search`
- Name: stock.move.line.search
- Model: `stock.move.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 9
- Sample fields: `location_id`, `lot_id`, `owner_id`, `package_id`, `picking_id`, `product_category_name`, `product_id`, `reference`, `result_package_id`
- XPath or positional patches: 0

### `view_move_line_mobile_form`
- Name: stock.move.line.mobile.form
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.view_move_line_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_move_line_form`
- Name: stock.move.line.form
- Model: `stock.move.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 19
- Sample fields: `company_id`, `create_uid`, `date`, `location_dest_id`, `location_id`, `lot_id`, `lot_name`, `origin`, `owner_id`, `package_id`, and 9 more
- XPath or positional patches: 0

### `view_move_line_tree_detailed`
- Name: stock.move.line.list.detailed
- Model: `stock.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 12
- Sample fields: `company_id`, `location_dest_id`, `location_id`, `lot_id`, `package_id`, `picking_id`, `picking_partner_id`, `product_id`, `product_uom_id`, `quantity`, and 2 more
- XPath or positional patches: 0

### `view_move_line_tree`
- Name: stock.move.line.list
- Model: `stock.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 16
- Sample fields: `company_id`, `create_uid`, `date`, `location_dest_id`, `location_dest_usage`, `location_id`, `location_usage`, `lot_id`, `package_id`, `picking_partner_id`, and 6 more
- XPath or positional patches: 0

## Actions

- `stock_move_line_action`: `act_window` Moves History
- `action_revert_inventory_adjustment`: `server` Revert Inventory Adjustment

## Menus

- `stock_move_line_menu`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

<!-- GENERATED:VIEWFILE -->
