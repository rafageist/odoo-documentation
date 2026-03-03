---
tags: [odoo, enterprise, generated, views]
---

# views/mrp_workorder_views.xml

- Module: [[docs/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]]
- Scope: Enterprise Addons
- Source file: `views/mrp_workorder_views.xml`
- Views: 13
- Actions: 9
- Menus: 0
- Rules: 0

## View records

### `view_mrp_production_workorder_form_view_search_my_work_orders`
- Name: mrp.production.work.order.search
- Model: `mrp.workorder`
- Type: inferred from arch
- Inherits: `mrp.view_mrp_production_work_order_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `connected_employee_ids`
- XPath or positional patches: 1

### `view_mrp_production_workorder_form_view_filter_my_work_orders`
- Name: mrp.production.work.order.filter
- Model: `mrp.workorder`
- Type: inferred from arch
- Inherits: `mrp.view_mrp_production_workorder_form_view_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `connected_employee_ids`
- XPath or positional patches: 2

### `view_routing_steps_search`
- Name: view.routing.steps.search
- Model: `quality.point`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `active`
- XPath or positional patches: 0

### `mrp_workorder_view_kanban_inherit_quality`
- Name: mrp.workorder.view.kanban.inherit.quality
- Model: `mrp.workorder`
- Type: inferred from arch
- Inherits: `mrp.workcenter_line_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `employee_ids`
- XPath or positional patches: 1

### `mrp_workorder_view_form_tablet`
- Name: mrp.workorder.view.form.inherit.quality.tablet.new
- Model: `mrp.workorder`
- Type: inferred from arch
- Root tag: `form`
- Field references: 20
- Sample fields: `allow_producing_quantity_change`, `company_id`, `current_quality_check_id`, `duration`, `employee_ids`, `employee_name`, `finished_lot_ids`, `is_last_lot`, `is_last_unfinished_wo`, `is_user_working`, and 10 more
- Buttons: `action_back`, `action_generate_serial`, `action_open_manufacturing_order`, `button_pending`, `button_start`, `button_unblock`, `do_finish`, `openMenuPopup`, `popupEmployeeManagement`, `record_production`
- XPath or positional patches: 0

### `mrp_workorder_view_gantt_dependencies`
- Name: mrp.workorder.view.gantt.dependencies
- Model: `mrp.workorder`
- Type: inferred from arch
- Inherits: `mrp_workorder_view_gantt`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `workcenter_line_gantt_production_dependencies`
- Name: mrp.production.work.order.gantt.production.dependencies
- Model: `mrp.workorder`
- Type: inferred from arch
- Inherits: `workcenter_line_gantt_production`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `mrp_workorder_view_gantt`
- Name: mrp.workorder.view.gantt
- Model: `mrp.workorder`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 4
- Sample fields: `date_start`, `json_popover`, `state`, `workcenter_id`
- XPath or positional patches: 0

### `workcenter_line_gantt_production`
- Name: mrp.production.work.order.gantt.production
- Model: `mrp.workorder`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 4
- Sample fields: `date_start`, `json_popover`, `state`, `workcenter_id`
- XPath or positional patches: 0

### `workcenter_line_pivot_inherit_workorder`
- Name: mrp.production.work.order.pivot.inherit.mrp.workorder
- Model: `mrp.workorder`
- Type: inferred from arch
- Inherits: `mrp.workcenter_line_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `worksheet_page`
- XPath or positional patches: 1

### `workcenter_line_graph_inherit_workorder`
- Name: mrp.production.work.order.graph.inherit.mrp.workorder
- Model: `mrp.workorder`
- Type: inferred from arch
- Inherits: `mrp.workcenter_line_graph`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `worksheet_page`
- XPath or positional patches: 1

### `mrp_production_workorder_tree_editable_view_inherit_workorder`
- Name: mrp.production.work.order.list.editable.inherit.mrp.workorder
- Model: `mrp.workorder`
- Type: inferred from arch
- Inherits: `mrp.mrp_production_workorder_tree_editable_view`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `all_employees_allowed`, `allowed_employees`, `employee_assigned_ids`, `production_state`
- XPath or positional patches: 2

### `mrp_workorder_view_form_inherit_workorder`
- Name: mrp.workorder.view.form.inherit.workorder
- Model: `mrp.workorder`
- Type: inferred from arch
- Inherits: `mrp.mrp_production_workorder_form_view_inherit`
- Root tag: `xpath`
- Field references: 15
- Sample fields: `all_employees_allowed`, `allowed_employees`, `control_date`, `done_check_ids`, `employee_assigned_ids`, `employee_id`, `finished_lot_ids`, `production_state`, `quality_check_fail`, `quality_state`, and 5 more
- Buttons: `action_mark_as_done`, `action_open_mes`
- XPath or positional patches: 8

## Actions

- `action_open_employee_list`: `act_window` Select Employee
- `mrp.action_mrp_workorder_production`: `act_window`
- `mrp.action_mrp_workorder_workcenter`: `act_window`
- `mrp.action_mrp_workorder_production_specific`: `act_window`
- `mrp.action_mrp_routing_time`: `act_window`
- `mrp.mrp_workorder_todo`: `act_window`
- `mrp_workorder_action_tablet`: `act_window` Work Orders
- `action_mrp_workorder_dependencies_production`: `server` Work Orders Planning
- `action_mrp_workorder_dependencies_workcenter`: `server` Work Orders Planning

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_workorder/Views]]

