<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mrp_workcenter_views.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `views/mrp_workcenter_views.xml`
- Views: 15
- Actions: 8
- Menus: 2
- Rules: 0

## View records

### `oee_pivot_view`
- Name: mrp.workcenter.productivity.pivot
- Model: `mrp.workcenter.productivity`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `date_start`, `duration`, `loss_type`
- XPath or positional patches: 0

### `oee_graph_view`
- Name: mrp.workcenter.productivity.graph
- Model: `mrp.workcenter.productivity`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `duration`, `loss_id`, `workcenter_id`
- XPath or positional patches: 0

### `oee_tree_view`
- Name: mrp.workcenter.productivity.list
- Model: `mrp.workcenter.productivity`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `company_id`, `date_end`, `date_start`, `duration`, `loss_id`, `user_id`, `workcenter_id`
- XPath or positional patches: 0

### `oee_form_view`
- Name: mrp.workcenter.productivity.form
- Model: `mrp.workcenter.productivity`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `company_id`, `date_end`, `date_start`, `description`, `duration`, `loss_id`, `production_id`, `workcenter_id`, `workorder_id`
- XPath or positional patches: 0

### `oee_search_view`
- Name: mrp.workcenter.productivity.search
- Model: `mrp.workcenter.productivity`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `loss_id`, `workcenter_id`
- XPath or positional patches: 0

### `oee_loss_search_view`
- Name: mrp.workcenter.productivity.loss.search
- Model: `mrp.workcenter.productivity.loss`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `view_mrp_workcenter_productivity_loss_kanban`
- Name: mrp.workcenter.productivity.loss.kanban
- Model: `mrp.workcenter.productivity.loss`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `loss_type`, `manual`, `name`
- XPath or positional patches: 0

### `oee_loss_tree_view`
- Name: mrp.workcenter.productivity.loss.list
- Model: `mrp.workcenter.productivity.loss`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `loss_type`, `name`, `sequence`
- XPath or positional patches: 0

### `oee_loss_form_view`
- Name: mrp.workcenter.productivity.loss.form
- Model: `mrp.workcenter.productivity.loss`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `loss_id`, `name`
- XPath or positional patches: 0

### `view_mrp_workcenter_search`
- Name: mrp.workcenter.search
- Model: `mrp.workcenter`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `mrp_workcenter_view`
- Name: mrp.workcenter.form
- Model: `mrp.workcenter`
- Type: inferred from arch
- Root tag: `form`
- Field references: 22
- Sample fields: `active`, `alternative_workcenter_ids`, `blocked_time`, `capacity`, `capacity_ids`, `code`, `company_id`, `costs_hour`, `has_routing_lines`, `name`, and 12 more
- Buttons: `%(action_mrp_workcenter_load_report_graph)d`, `%(mrp_workcenter_productivity_report_blocked)d`, `%(mrp_workcenter_productivity_report_oee)d`, `%(mrp_workorder_report)d`, `action_show_operations`
- XPath or positional patches: 0

### `mrp_workcenter_kanban`
- Name: mrp.workcenter.kanban
- Model: `mrp.workcenter`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 10
- Sample fields: `color`, `kanban_dashboard_graph`, `name`, `oee`, `oee_target`, `working_state`, `workorder_count`, `workorder_late_count`, `workorder_progress_count`, `workorder_ready_count`
- Buttons: `action_work_order`, `action_work_order_alternatives`
- XPath or positional patches: 0

### `oee_pie_view`
- Name: mrp.workcenter.productivity.graph
- Model: `mrp.workcenter.productivity`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `duration`, `loss_id`
- XPath or positional patches: 0

### `mrp_workcenter_view_kanban`
- Name: mrp.workcenter.kanban
- Model: `mrp.workcenter`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `code`, `name`
- XPath or positional patches: 0

### `mrp_workcenter_tree_view`
- Name: mrp.workcenter.list
- Model: `mrp.workcenter`
- Type: inferred from arch
- Root tag: `list`
- Field references: 13
- Sample fields: `active`, `alternative_workcenter_ids`, `code`, `company_id`, `costs_hour`, `name`, `oee_target`, `productive_time`, `sequence`, `tag_ids`, and 3 more
- XPath or positional patches: 0

## Actions

- `mrp_workcenter_productivity_report`: `act_window` Overall Equipment Effectiveness
- `mrp_workcenter_kanban_action`: `act_window` Work Centers Overview
- `mrp_workcenter_action`: `act_window` Work Centers
- `mrp_workorder_report`: `act_window` Work Orders Analysis
- `mrp_workorder_workcenter_report`: `act_window` Work Orders Performance
- `mrp_workcenter_productivity_report_blocked`: `act_window` Productivity Losses
- `mrp_workcenter_productivity_report_oee`: `act_window` Overall Equipment Effectiveness
- `action_work_orders`: `act_window` Work Orders

## Menus

- `menu_mrp_workcenter_productivity_report`: unnamed
- `menu_view_resource_search_mrp`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

<!-- GENERATED:VIEWFILE -->
