---
tags: [odoo, community, generated, views]
---

# views/mrp_production_views.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `views/mrp_production_views.xml`
- Views: 8
- Actions: 15
- Menus: 3
- Rules: 0

## View records

### `view_mrp_production_filter`
- Name: mrp.production.select
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `move_raw_ids`, `name`, `origin`, `picking_type_id`, `product_id`, `product_variant_attributes`, `workcenter_id`
- XPath or positional patches: 0

### `view_production_graph`
- Name: mrp.production.graph
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `backorder_sequence`, `date_finished`, `product_uom_qty`, `qty_producing`
- XPath or positional patches: 0

### `view_production_pivot`
- Name: mrp.production.pivot
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 1
- Sample fields: `date_start`
- XPath or positional patches: 0

### `view_production_calendar`
- Name: mrp.production.calendar
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 3
- Sample fields: `product_id`, `product_qty`, `user_id`
- XPath or positional patches: 0

### `mrp_production_kanban_view`
- Name: mrp.production.kanban
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `activity_ids`, `date_start`, `json_popover`, `name`, `priority`, `product_id`, `product_qty`, `product_uom_id`, `state`
- XPath or positional patches: 0

### `mrp_production_form_view`
- Name: mrp.production.form
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `form`
- Field references: 83
- Sample fields: `additional`, `allow_workorder_dependencies`, `allowed_operation_ids`, `bom_id`, `bom_line_id`, `byproduct_id`, `company_id`, `components_availability`, `components_availability_state`, `consumption`, and 73 more
- Buttons: `%(action_mrp_production_moves)d`, `%(action_report_mo_overview)d`, `%(mrp.action_change_production_qty)d`, `%(stock.action_stock_report)d`, `action_add_from_catalog_byproduct`, `action_add_from_catalog_raw`, `action_assign`, `action_cancel`, `action_clear_lot_producing_ids`, `action_confirm`, and 19 more
- XPath or positional patches: 0

### `mrp_production_tree_view`
- Name: mrp.production.list
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `list`
- Field references: 25
- Sample fields: `activity_exception_decoration`, `activity_ids`, `bom_id`, `company_id`, `components_availability`, `components_availability_state`, `date_deadline`, `date_finished`, `date_start`, `delay_alert_date`, and 15 more
- Buttons: `action_assign`, `action_cancel`, `button_plan`
- XPath or positional patches: 0

### `mrp_production_view_activity`
- Name: mrp.production.view.activity
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 3
- Sample fields: `date_start`, `name`, `user_id`
- XPath or positional patches: 0

## Actions

- `action_mrp_production_form`: `act_window` Manufacturing Orders
- `mrp_production_action_unreserve_tree`: `server` Unreserve
- `mrp_production_action_picking_deshboard`: `act_window` Manufacturing Orders
- `mrp_production_action`: `act_window` Manufacturing Orders
- `action_production_order_mark_done`: `server` Mark as Done
- `action_production_order_merge`: `server` Merge
- `action_plan_with_components_availability`: `server` Plan based on Components Availability
- `action_print_labels`: `server` Print Labels
- `action_production_order_scrap`: `server` Scrap
- `action_production_order_lock_unlock`: `server` Lock/Unlock
- `action_print_labels`: `server` Labels
- `action_production_order_split`: `server` Split
- `action_mrp_display_fullscreen`: `client` Manufacturing
- `action_mrp_display`: `client` Mrp Display
- `action_report_mo_overview`: `client` MO Overview

## Menus

- `menu_mrp_work_order_report`: Work Orders
- `menu_mrp_workorder_todo`: Work Orders
- `menu_mrp_production_action`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

