<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_picking_views.xml`
- Views: 6
- Actions: 25
- Menus: 3
- Rules: 0

## View records

### `view_picking_internal_search`
- Name: stock.picking.internal.search
- Model: `stock.picking`
- Type: inferred from arch
- Root tag: `search`
- Field references: 9
- Sample fields: `activity_type_id`, `activity_user_id`, `lot_id`, `move_line_ids`, `name`, `origin`, `partner_id`, `picking_type_id`, `product_id`
- XPath or positional patches: 0

### `view_picking_form`
- Name: stock.picking.form
- Model: `stock.picking`
- Type: inferred from arch
- Root tag: `form`
- Field references: 56
- Sample fields: `additional`, `backorder_id`, `company_id`, `date`, `date_deadline`, `date_done`, `description_picking`, `display_import_lot`, `forecast_availability`, `forecast_expected_date`, and 46 more
- Buttons: `%(act_stock_return_picking)d`, `%(action_report_delivery)d`, `%(action_stock_report)d`, `action_add_packages`, `action_assign`, `action_cancel`, `action_confirm`, `action_detailed_operations`, `action_next_transfer`, `action_picking_move_tree`, and 9 more
- XPath or positional patches: 0

### `vpicktree`
- Name: stock.picking.list
- Model: `stock.picking`
- Type: inferred from arch
- Root tag: `list`
- Field references: 20
- Sample fields: `activity_exception_decoration`, `backorder_id`, `company_id`, `date_deadline`, `date_done`, `is_signed`, `json_popover`, `location_dest_id`, `location_id`, `name`, and 10 more
- Buttons: `action_assign`, `do_unreserve`
- XPath or positional patches: 0

### `stock_picking_kanban`
- Name: stock.picking.kanban
- Model: `stock.picking`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 10
- Sample fields: `activity_ids`, `json_popover`, `name`, `partner_id`, `picking_properties`, `picking_type_id`, `priority`, `scheduled_date`, `state`, `user_id`
- XPath or positional patches: 0

### `stock_picking_calendar`
- Name: stock.picking.calendar
- Model: `stock.picking`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 5
- Sample fields: `origin`, `partner_id`, `picking_properties`, `picking_type_id`, `state`
- XPath or positional patches: 0

### `stock_picking_view_activity`
- Name: stock.picking.view.activity
- Model: `stock.picking`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 2
- Sample fields: `name`, `scheduled_date`
- XPath or positional patches: 0

## Actions

- `stock_split_picking`: `server` Split
- `action_picking_form`: `act_window` New Transfer
- `action_get_picking_type_operations`: `act_window` Operations
- `action_install_barcode`: `server` Install Barcode
- `action_get_picking_type_ready_moves`: `act_window` Ready Moves
- `action_picking_tree_backorder`: `act_window` Backorders
- `action_picking_tree_late`: `act_window` Late Transfers
- `action_picking_tree_waiting`: `act_window` Waiting Transfers
- `action_picking_tree_graph`: `act_window` To Do
- `action_picking_tree_ready`: `act_window` To Do
- `stock_picking_action_picking_type`: `act_window` All Transfers
- `method_action_picking_tree_internal`: `server` stock.method_action_picking_tree_internal
- `method_action_picking_tree_outgoing`: `server` stock.method_action_picking_tree_outgoing
- `method_action_picking_tree_incoming`: `server` stock.method_action_picking_tree_incoming
- `click_dashboard_graph`: `server` stock.click_dashboard_graph
- `action_lead_mass_mail`: `act_window` Send email
- `action_scrap`: `server` Scrap
- `action_toggle_is_locked`: `server` Lock/Unlock
- `action_print_labels`: `server` Labels
- `action_unreserve_picking`: `server` Unreserve

## Menus

- `int_picking`: Internal
- `out_picking`: Deliveries
- `in_picking`: Receipts

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

<!-- GENERATED:VIEWFILE -->
