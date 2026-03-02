<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_leave_type_views.xml

- Module: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- Scope: Community Addons
- Source file: `views/hr_leave_type_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_holiday_status_normal_tree`
- Name: hr.leave.type.normal.list
- Model: `hr.leave.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `allocation_validation_type`, `color`, `company_id`, `country_id`, `display_name`, `employee_requests`, `leave_validation_type`, `request_unit`, `requires_allocation`, `responsible_ids`, and 1 more
- XPath or positional patches: 0

### `hr_holiday_status_view_kanban`
- Name: hr.leave.type.kanban
- Model: `hr.leave.type`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `leaves_taken`, `max_leaves`, `name`
- XPath or positional patches: 0

### `edit_holiday_status_form`
- Name: hr.leave.type.form
- Model: `hr.leave.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 23
- Sample fields: `accrual_count`, `active`, `allocation_count`, `allocation_validation_type`, `allow_request_on_top`, `allows_negative`, `color`, `company_id`, `country_id`, `elligible_for_accrual_rate`, and 13 more
- Buttons: `action_see_accrual_plans`, `action_see_days_allocated`, `action_see_group_leaves`
- XPath or positional patches: 0

### `view_holidays_status_filter`
- Name: hr.leave.type.filter
- Model: `hr.leave.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `create_calendar_meeting`, `name`
- XPath or positional patches: 0

## Actions

- `open_view_holiday_status`: `act_window` Time Off Types

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays/Views]]

<!-- GENERATED:VIEWFILE -->
