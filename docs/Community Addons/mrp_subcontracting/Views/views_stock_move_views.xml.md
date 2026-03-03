---
tags: [odoo, community, generated, views]
---

# views/stock_move_views.xml

- Module: [[docs/Community Addons/mrp_subcontracting/mrp_subcontracting|mrp_subcontracting]]
- Scope: Community Addons
- Source file: `views/stock_move_views.xml`
- Views: 8
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_move_search`
- Name: stock.move.search
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `stock.view_move_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `order_finished_lot_ids`
- XPath or positional patches: 1

### `mrp_subcontracting_move_tree_view`
- Name: mrp.subcontracting.move.list.view
- Model: `stock.move`
- Type: inferred from arch
- Root tag: `list`
- Field references: 18
- Sample fields: `bom_line_id`, `company_id`, `date`, `has_tracking`, `location_dest_id`, `location_id`, `operation_id`, `order_finished_lot_ids`, `picking_type_id`, `product_id`, and 8 more
- XPath or positional patches: 0

### `mrp_subcontracting_portal_move_form_view`
- Name: mrp.subcontracting.portal.move.form.view
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `mrp_subcontracting_move_form_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 3

### `mrp_subcontracting_move_form_view`
- Name: mrp.subcontracting.move.form.view
- Model: `stock.move`
- Type: inferred from arch
- Root tag: `form`
- Field references: 17
- Sample fields: `company_id`, `has_tracking`, `location_dest_id`, `location_id`, `lot_id`, `move_id`, `move_line_ids`, `order_finished_lot_ids`, `picking_id`, `product_id`, and 7 more
- XPath or positional patches: 0

### `mrp_subcontracting_view_stock_move_operations`
- Name: mrp.subcontracting.stock.move.operations.form
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `stock.view_stock_move_operations`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `mrp_subcontracting_view_stock_move_line_operation_tree`
- Name: mrp.subcontracting.stock.move.line.operations.list
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.view_stock_move_line_operation_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `mrp_subcontracting_portal_stock_move_line_tree_view`
- Name: mrp.subcontracting.portal.stock.move.line.list.view
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `mrp_subcontracting_stock_move_line_tree_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `mrp_subcontracting_stock_move_line_tree_view`
- Name: mrp.subcontracting.stock.move.line.list.view
- Model: `stock.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `company_id`, `id`, `location_dest_id`, `location_id`, `lot_id`, `owner_id`, `package_id`, `product_id`, `product_uom_id`, `quantity`, and 3 more
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/mrp_subcontracting/Views]]

