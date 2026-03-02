<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_views.xml

- Module: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- Scope: Community Addons
- Source file: `views/hr_views.xml`
- Views: 7
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_employee_public_form_view_inherit`
- Name: hr.employee.public.leave.form.inherit
- Model: `hr.employee.public`
- Type: inferred from arch
- Inherits: `hr.hr_employee_public_view_form`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `allocation_display`, `allocation_remaining_display`, `show_leaves`
- Buttons: `%(hr_leave_action_new_request)d`, `action_open_time_off_calendar`
- XPath or positional patches: 2

### `view_employee_tree_inherit_leave`
- Name: hr.employee.list.leave
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `leave_manager_id`
- XPath or positional patches: 1

### `view_employee_form_leave_inherit`
- Name: hr.employee.leave.form.inherit
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `allocation_display`, `allocation_remaining_display`, `hr_icon_display`, `is_absent`, `leave_manager_id`, `show_leaves`
- Buttons: `action_open_versions`, `action_time_off_dashboard`
- XPath or positional patches: 2

### `hr_kanban_view_employees_kanban`
- Name: hr.employee.kanban.leaves.status
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.hr_kanban_view_employees`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `current_leave_id`, `current_leave_state`, `is_absent`, `leave_date_from`, `leave_date_to`
- XPath or positional patches: 2

### `hr_kanban_view_public_employees_kanban`
- Name: hr.employee.public.kanban.leaves.status
- Model: `hr.employee.public`
- Type: inferred from arch
- Inherits: `hr.hr_employee_public_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `is_absent`
- XPath or positional patches: 1

### `hr_employee_view_search`
- Name: hr.employee.search.view.inherit
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `hr_department_view_kanban`
- Name: hr.department.kanban.inherit
- Model: `hr.department`
- Type: inferred from arch
- Inherits: `hr.hr_department_view_kanban`
- Root tag: `data`
- Field references: 4
- Sample fields: `absence_of_today`, `allocation_to_approve_count`, `leave_to_approve_count`, `total_employee`
- XPath or positional patches: 4

## Actions

- `hr_employee_action_from_department`: `act_window` Absent Employees

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays/Views]]

<!-- GENERATED:VIEWFILE -->
