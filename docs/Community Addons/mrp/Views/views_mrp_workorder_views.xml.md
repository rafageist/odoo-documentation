<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mrp_workorder_views.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `views/mrp_workorder_views.xml`
- Views: 12
- Actions: 10
- Menus: 0
- Rules: 0

## View records

### `view_work_center_load_graph`
- Name: report.workcenter.load.graph
- Model: `mrp.workorder`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `duration_expected`, `production_date`, `workcenter_id`
- XPath or positional patches: 0

### `view_workcenter_load_pivot`
- Name: report.workcenter.load.pivot
- Model: `mrp.workorder`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `duration_expected`, `production_date`, `workcenter_id`
- XPath or positional patches: 0

### `workcenter_line_kanban`
- Name: mrp.production.work.order.kanban
- Model: `mrp.workorder`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 13
- Sample fields: `date_start`, `finished_lot_ids`, `last_working_user_id`, `name`, `product_id`, `product_uom_id`, `production_date`, `production_id`, `qty_production`, `state`, and 3 more
- XPath or positional patches: 0

### `workcenter_line_pivot`
- Name: mrp.production.work.order.pivot
- Model: `mrp.workorder`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 5
- Sample fields: `date_start`, `duration`, `duration_expected`, `duration_unit`, `operation_id`
- XPath or positional patches: 0

### `workcenter_line_graph`
- Name: mrp.production.work.order.graph
- Model: `mrp.workorder`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `duration`, `duration_expected`, `duration_unit`, `production_id`
- XPath or positional patches: 0

### `workcenter_line_calendar`
- Name: mrp.production.work.order.calendar
- Model: `mrp.workorder`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 3
- Sample fields: `production_id`, `state`, `workcenter_id`
- XPath or positional patches: 0

### `view_mrp_production_workorder_form_view_filter`
- Name: mrp.production.work.order.select
- Model: `mrp.workorder`
- Type: inferred from arch
- Root tag: `search`
- Field references: 7
- Sample fields: `finished_lot_ids`, `move_raw_ids`, `name`, `product_id`, `product_variant_attributes`, `production_id`, `workcenter_id`
- XPath or positional patches: 0

### `mrp_production_workorder_form_view_inherit`
- Name: mrp.production.work.order.form
- Model: `mrp.workorder`
- Type: inferred from arch
- Root tag: `form`
- Field references: 35
- Sample fields: `allow_workorder_dependencies`, `blocked_by_workorder_ids`, `company_id`, `date_end`, `date_finished`, `date_start`, `duration`, `duration_expected`, `finished_lot_ids`, `is_planned`, and 25 more
- Buttons: `action_open_wizard`, `action_see_move_scrap`
- XPath or positional patches: 0

### `mrp_production_workorder_tree_view`
- Name: mrp.production.work.order.list
- Model: `mrp.workorder`
- Type: inferred from arch
- Inherits: `mrp.mrp_production_workorder_tree_editable_view`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `production_id`, `state`, `workcenter_id`
- XPath or positional patches: 1

### `mrp_production_workorder_tree_editable_view_mo_form`
- Name: mrp.production.work.order.list.editable
- Model: `mrp.workorder`
- Type: inferred from arch
- Inherits: `mrp_production_workorder_tree_editable_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sequence`
- XPath or positional patches: 3

### `mrp_production_workorder_tree_editable_view`
- Name: mrp.production.work.order.list.editable
- Model: `mrp.workorder`
- Type: inferred from arch
- Root tag: `list`
- Field references: 22
- Sample fields: `company_id`, `consumption`, `date_finished`, `date_start`, `duration`, `duration_expected`, `finished_lot_ids`, `is_produced`, `is_user_working`, `name`, and 12 more
- Buttons: `button_finish`, `button_pending`, `button_start`
- XPath or positional patches: 0

### `view_mrp_production_work_order_search`
- Name: mrp.production.work.order.search
- Model: `mrp.workorder`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `finished_lot_ids`, `product_id`, `production_id`, `workcenter_id`
- XPath or positional patches: 0

## Actions

- `action_pause_workorders`: `server` Pause
- `action_start_workorders`: `server` Start
- `action_mrp_workcenter_load_report_pivot`: `view`
- `action_mrp_workcenter_load_report_graph`: `act_window` Work Center Loads
- `mrp_workorder_todo`: `act_window` Work Orders
- `mrp_workorder_mrp_production_form`: `act_window` Work Orders
- `action_mrp_workorder_production`: `act_window` Work Orders Planning
- `action_mrp_workorder_workcenter`: `act_window` Work Orders Planning
- `action_mrp_workorder_production_specific`: `act_window` Work Orders
- `action_mrp_routing_time`: `act_window` Work Orders

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

<!-- GENERATED:VIEWFILE -->
