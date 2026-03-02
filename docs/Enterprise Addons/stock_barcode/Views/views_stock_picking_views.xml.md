<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Enterprise Addons/stock_barcode/stock_barcode|stock_barcode]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `stock_picking_view_kanban`
- Name: stock.picking.view.kanban.stock.barcode
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.stock_picking_kanban`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `name`, `state`
- Buttons: `action_open_picking_client_action`
- XPath or positional patches: 4

### `view_picking_form`
- Name: stock.picking.form.inherit.stock.barcode
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_open_picking_client_action`
- XPath or positional patches: 1

### `stock_picking_barcode`
- Name: stock.picking.form.view.barcode
- Model: `stock.picking`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `company_id`, `description_picking`, `location_dest_id`, `location_id`, `move_ids`, `note`, `origin`, `owner_id`, `partner_id`, `picking_type_code`, and 6 more
- Buttons: `action_view_reception_report`
- XPath or positional patches: 0

### `view_stock_move_line_kanban_inherited`
- Name: stock.move.line.kanban.inherited
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.view_stock_move_line_kanban`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `location_processed`, `lots_visible`, `product_barcode`, `result_package_id`
- XPath or positional patches: 1

### `view_stock_move_line_detailed_operation_tree_inherit_stock_barcode`
- Name: stock.move.line.operations.list.inherit
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.view_stock_move_line_detailed_operation_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `location_processed`, `product_barcode`
- XPath or positional patches: 2

## Actions

- `open_picking`: `act_window` Open picking form

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode/Views]]

<!-- GENERATED:VIEWFILE -->
