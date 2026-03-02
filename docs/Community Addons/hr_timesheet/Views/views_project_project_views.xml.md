<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/project_project_views.xml

- Module: [[docs/Community Addons/hr_timesheet/hr_timesheet|hr_timesheet]]
- Scope: Community Addons
- Source file: `views/project_project_views.xml`
- Views: 6
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `project_templates_view_list_inherit_timesheet`
- Name: project.project.template.list.inherit.timesheet
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.project_templates_view_list`
- Root tag: `field`
- Field references: 2
- Sample fields: `effective_hours`, `remaining_hours`
- XPath or positional patches: 0

### `view_project_project_filter_inherit_timesheet`
- Name: project.project.view.inherit.timesheet
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project_project_filter`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_project_kanban_inherited`
- Name: project.project.timesheet.kanban.inherited
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project_kanban`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `allocated_hours`, `allow_timesheets`, `encode_uom_in_days`, `remaining_hours`
- XPath or positional patches: 3

### `project_project_view_tree_inherit_sale_project`
- Name: project.project.list.inherit.sale.timesheet
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `allocated_hours`, `allow_timesheets`, `effective_hours`, `remaining_hours`
- XPath or positional patches: 1

### `project_invoice_form`
- Name: Inherit project form : Invoicing Data
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.edit_project`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `allocated_hours`, `allow_timesheets`, `analytic_account_active`
- XPath or positional patches: 4

### `project_project_view_form_simplified_inherit_timesheet`
- Name: project.project.view.form.simplified.inherit.timesheet
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.project_project_view_form_simplified`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `allow_timesheets`
- XPath or positional patches: 1

## Actions

- `project.open_view_project_all_group_stage`: `act_window`
- `project.open_view_project_all`: `act_window`

## Navigation

- **Parent:** [[docs/Community Addons/hr_timesheet/Views]]

<!-- GENERATED:VIEWFILE -->
