<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_leave_allocation_views.xml

- Module: [[docs/Community Addons/hr_holidays_attendance/hr_holidays_attendance|hr_holidays_attendance]]
- Scope: Community Addons
- Source file: `views/hr_leave_allocation_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_leave_allocation_overtime_manager_view_form`
- Name: unnamed
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Inherits: `hr_attendance_holidays_hr_leave_allocation_view_form_inherit`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 4

### `hr_attendance_holidays_hr_leave_allocation_view_form_inherit`
- Name: unnamed
- Model: `hr.leave.allocation`
- Type: inferred from arch
- Inherits: `hr_holidays.hr_leave_allocation_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `employee_overtime`
- XPath or positional patches: 1

## Actions

- `hr_leave_allocation_overtime_manager_action`: `act_window` New Allocation Request

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays_attendance/Views]]

<!-- GENERATED:VIEWFILE -->
