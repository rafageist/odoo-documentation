---
tags: [odoo, enterprise, generated, views]
---

# views/mrp_workcenter_views.xml

- Module: [[docs/Enterprise Addons/mrp_workorder/mrp_workorder|mrp_workorder]]
- Scope: Enterprise Addons
- Source file: `views/mrp_workcenter_views.xml`
- Views: 2
- Actions: 3
- Menus: 1
- Rules: 0

## View records

### `mrp_workcenter_form_view_inherit`
- Name: mrp.workcenter.form.view.inherit
- Model: `mrp.workcenter`
- Type: inferred from arch
- Inherits: `mrp.mrp_workcenter_view`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `employee_costs_hour`, `employee_ids`
- XPath or positional patches: 2

### `mrp_workcenter_view_kanban_inherit_workorder`
- Name: mrp.workcenter.view.kanban.inherit.mrp.workorder
- Model: `mrp.workcenter`
- Type: inferred from arch
- Inherits: `mrp.mrp_workcenter_kanban`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_work_order`
- XPath or positional patches: 1

## Actions

- `mrp.mrp_workorder_report`: `act_window`
- `mrp.mrp_workorder_workcenter_report`: `act_window`
- `mrp.action_work_orders`: `act_window`

## Menus

- `menu_mrp_dashboard`: Overview

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_workorder/Views]]

