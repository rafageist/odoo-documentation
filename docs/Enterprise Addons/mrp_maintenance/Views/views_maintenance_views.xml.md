---
tags: [odoo, enterprise, generated, views]
---

# views/maintenance_views.xml

- Module: [[docs/Enterprise Addons/mrp_maintenance/mrp_maintenance|mrp_maintenance]]
- Scope: Enterprise Addons
- Source file: `views/maintenance_views.xml`
- Views: 8
- Actions: 1
- Menus: 3
- Rules: 0

## View records

### `hr_equipment_request_view_graph_inherit_maintenance`
- Name: maintenance.request.view.graph.inherit.mrp.maintenance
- Model: `maintenance.request`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_request_view_graph`
- Root tag: `field`
- Field references: 2
- Sample fields: `recurring_leaves_count`, `repeat_interval`
- XPath or positional patches: 0

### `maintenance_request_view_kanban_inherit_mrp`
- Name: maintenance.request.view.kanban.inherit.mrp
- Model: `maintenance.request`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_request_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `workcenter_id`
- XPath or positional patches: 1

### `maintenance_request_view_search_inherit_mrp`
- Name: maintenence.request.view.search.inherit.mrp
- Model: `maintenance.request`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_request_view_search`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `production_id`, `workcenter_id`
- XPath or positional patches: 1

### `maintenance_request_view_form_inherit_mrp_workorder`
- Name: maintenance.request.view.form.inherit.mrp.tablet
- Model: `maintenance.request`
- Type: inferred from arch
- Inherits: `mrp_maintenance.maintenance_request_view_form_inherit_mrp`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `maintenance_request_view_form_inherit_mrp`
- Name: maintenance.request.view.form.inherit.mrp
- Model: `maintenance.request`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_request_view_form`
- Root tag: `xpath`
- Field references: 8
- Sample fields: `block_workcenter`, `equipment_id`, `maintenance_for`, `production_company_id`, `production_id`, `recurring_leaves_count`, `workcenter_id`, `workorder_id`
- XPath or positional patches: 5

### `maintenance_workcenter_view_kanban_inherit_mrp`
- Name: maintenance.workcenter.view.kanban.inherit.mrp
- Model: `mrp.workcenter`
- Type: inferred from arch
- Inherits: `mrp.mrp_workcenter_view_kanban`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `activity_ids`, `maintenance_open_count`, `technician_user_id`
- XPath or positional patches: 1

### `maintenance_equipment_view_form_inherit_mrp`
- Name: maintenance.equipment.view.form.inherit.mrp
- Model: `maintenance.equipment`
- Type: inferred from arch
- Inherits: `stock_maintenance.maintenance_stock_equipment_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `workcenter_id`
- Buttons: `button_mrp_workcenter`
- XPath or positional patches: 2

### `maintenance_stage_view_tree_inherit_mrp`
- Name: maintenance.stage.view.list.inherit.mrp
- Model: `maintenance.stage`
- Type: inferred from arch
- Inherits: `maintenance.hr_equipment_stage_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `create_leaves`
- XPath or positional patches: 1

## Actions

- `maintenance_workcenter_action`: `act_window` Work Centers

## Menus

- `menu_equipment_dashboard`: Machines & Tools
- `menu_workcenter_tree`: unnamed
- `maintenance.menu_equipment_form`: Equipment

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_maintenance/Views]]

