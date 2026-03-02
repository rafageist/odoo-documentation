<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# wizard/edit_billable_time_target_views.xml

- Module: [[docs/Enterprise Addons/sale_timesheet_enterprise/sale_timesheet_enterprise|sale_timesheet_enterprise]]
- Scope: Enterprise Addons
- Source file: `wizard/edit_billable_time_target_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_edit_billable_time_target_update_kanban`
- Name: edit.billable.time.target.kanban
- Model: `edit.billable.time.target`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 12
- Sample fields: `avatar_128`, `birthday_public_display_string`, `company_id`, `hr_icon_display`, `image_1024`, `image_128`, `job_id`, `name`, `show_hr_icon_display`, `user_id`, and 2 more
- XPath or positional patches: 0

### `view_edit_billable_time_target_update_tree`
- Name: edit.billable.time.target.tree
- Model: `edit.billable.time.target`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `billable_time_target`, `company_id`, `department_id`, `job_id`, `name`, `parent_id`, `resource_calendar_id`, `timesheet_manager_id`
- XPath or positional patches: 0

### `view_edit_billable_time_target_update_form`
- Name: edit.billable.time.target.form
- Model: `edit.billable.time.target`
- Type: inferred from arch
- Root tag: `form`
- Field references: 19
- Sample fields: `active`, `address_id`, `avatar_1920`, `billable_time_target`, `child_ids`, `coach_id`, `company_id`, `department_id`, `hr_icon_display`, `image_128`, and 9 more
- XPath or positional patches: 0

### `view_edit_billable_time_target_update_filter`
- Name: view.hr.employee.update.filter
- Model: `edit.billable.time.target`
- Type: inferred from arch
- Root tag: `search`
- Field references: 6
- Sample fields: `company_id`, `department_id`, `name`, `parent_id`, `resource_calendar_id`, `timesheet_manager_id`
- XPath or positional patches: 0

## Actions

- `action_open_edit_billable_time_target`: `act_window` Employees

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_timesheet_enterprise/Views]]

<!-- GENERATED:VIEWFILE -->
