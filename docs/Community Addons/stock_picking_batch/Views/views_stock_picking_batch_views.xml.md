---
tags: [odoo, community, generated, views]
---

# views/stock_picking_batch_views.xml

- Module: [[docs/Community Addons/stock_picking_batch/stock_picking_batch|stock_picking_batch]]
- Scope: Community Addons
- Source file: `views/stock_picking_batch_views.xml`
- Views: 11
- Actions: 3
- Menus: 2
- Rules: 0

## View records

### `stock_move_line_view_search_inherit_stock_picking_batch`
- Name: stock.move.line.search.stock_picking_batch
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.stock_move_line_view_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_move_line_tree_inherit_stock_picking_batch`
- Name: stock.move.line.list.stock_picking_batch
- Model: `stock.move.line`
- Type: inferred from arch
- Inherits: `stock.view_move_line_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `batch_id`
- XPath or positional patches: 1

### `view_picking_internal_search_inherit_stock_picking_batch`
- Name: stock.picking.search
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_internal_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `batch_id`
- XPath or positional patches: 1

### `stock_picking_batch_filter`
- Name: stock.picking.batch.filter
- Model: `stock.picking.batch`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `name`, `picking_type_id`, `user_id`
- XPath or positional patches: 0

### `stock_picking_batch_calendar`
- Name: stock.picking.batch.calendar
- Model: `stock.picking.batch`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 1
- Sample fields: `scheduled_date`
- XPath or positional patches: 0

### `stock_picking_batch_kanban`
- Name: stock.picking.batch.kanban
- Model: `stock.picking.batch`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 7
- Sample fields: `company_id`, `description`, `name`, `picking_type_id`, `scheduled_date`, `state`, `user_id`
- XPath or positional patches: 0

### `stock_picking_batch_tree`
- Name: stock.picking.batch.list
- Model: `stock.picking.batch`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `activity_exception_decoration`, `company_id`, `description`, `name`, `picking_type_id`, `scheduled_date`, `state`, `user_id`
- XPath or positional patches: 0

### `stock_picking_batch_form`
- Name: stock.picking.batch.form
- Model: `stock.picking.batch`
- Type: inferred from arch
- Root tag: `form`
- Field references: 16
- Sample fields: `allowed_picking_ids`, `company_id`, `description`, `is_wave`, `move_ids`, `name`, `picking_ids`, `picking_type_code`, `picking_type_id`, `properties`, and 6 more
- Buttons: `action_assign`, `action_batch_detailed_operations`, `action_cancel`, `action_confirm`, `action_done`, `action_open_label_layout`, `action_print`, `action_put_in_pack`, `action_see_packages`, `action_view_reception_report`
- XPath or positional patches: 0

### `view_move_line_tree`
- Name: stock_picking_batch.move.line.list
- Model: `stock.move.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 16
- Sample fields: `company_id`, `is_locked`, `location_dest_id`, `location_id`, `lot_id`, `lot_name`, `package_id`, `picking_id`, `picking_location_id`, `product_id`, and 6 more
- Buttons: `action_put_in_pack`
- XPath or positional patches: 0

### `view_picking_move_tree_inherited`
- Name: stock_picking_batch.picking.move.list
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `stock.view_picking_move_tree`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `picked`, `picking_id`
- Buttons: `action_show_details`
- XPath or positional patches: 4

### `view_picking_form_inherited`
- Name: stock_picking_batch.picking.form
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `state`
- XPath or positional patches: 1

## Actions

- `action_merge_batch_picking`: `server` Merge
- `action_unreserve_batch_picking`: `server` Unreserve
- `stock_picking_batch_action`: `act_window` Batch Transfers

## Menus

- `stock_picking_batch_menu`: unnamed
- `menu_stock_jobs`: Jobs

## Navigation

- **Parent:** [[docs/Community Addons/stock_picking_batch/Views]]

