<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/project_task_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm/industry_fsm|industry_fsm]]
- Scope: Enterprise Addons
- Source file: `views/project_task_views.xml`
- Views: 6
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `project_view_form_inherit`
- Name: project.view.form.inherit
- Model: `project.project`
- Type: inferred from arch
- Inherits: `hr_timesheet.project_invoice_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `allow_geolocation`, `is_fsm`
- XPath or positional patches: 1

### `project_task_in_project_view_kanban`
- Name: project.task.in.project.kanban
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project_enterprise.view_task_kanban_inherited`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `quick_create_task_in_project`
- Name: project.task.quick_create_in_project.view.form.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `quick_create_task_form_fsm`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `quick_create_task_form_fsm`
- Name: project.task.form.quick_create
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.quick_create_task_form`
- Root tag: `field`
- Field references: 3
- Sample fields: `is_fsm`, `partner_id`, `user_ids`
- XPath or positional patches: 0

### `project_task_view_mobile_form`
- Name: fsm.task.form.view.mobile
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.view_task_form2_inherit`
- Root tag: `field`
- Field references: 1
- Sample fields: `project_id`
- XPath or positional patches: 6

### `view_task_form2_inherit`
- Name: view.task.form2.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_form2`
- Root tag: `xpath`
- Field references: 27
- Sample fields: `allocated_hours`, `allow_geolocation`, `allow_timesheets`, `date_deadline`, `display_enabled_conditions_count`, `display_mark_as_done_primary`, `display_mark_as_done_secondary`, `display_satisfied_conditions_count`, `display_send_report_primary`, `display_send_report_secondary`, and 17 more
- Buttons: `action_fsm_navigate`, `action_fsm_validate`, `action_preview_worksheet`, `action_send_report`
- XPath or positional patches: 18

## Actions

- `project.project_task_kanban_action_view`: `view`

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm/Views]]

<!-- GENERATED:VIEWFILE -->
