<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_leave_accrual_views.xml

- Module: [[docs/Community Addons/hr_holidays/hr_holidays|hr_holidays]]
- Scope: Community Addons
- Source file: `views/hr_leave_accrual_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_accrual_plan_view_search`
- Name: hr.leave.accrual.plan.search
- Model: `hr.leave.accrual.plan`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `hr_accrual_plan_view_form`
- Name: hr.leave.accrual.plan.form
- Model: `hr.leave.accrual.plan`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `accrued_gain_time`, `active`, `can_be_carryover`, `carryover_date`, `carryover_day`, `carryover_month`, `company_id`, `employees_count`, `is_based_on_worked_time`, `level_ids`, and 3 more
- Buttons: `action_create_accrual_plan_level`, `action_open_accrual_plan_employees`
- XPath or positional patches: 0

### `hr_accrual_plan_view_tree`
- Name: hr.leave.accrual.plan.list
- Model: `hr.leave.accrual.plan`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `employees_count`, `level_count`, `name`
- XPath or positional patches: 0

### `hr_accrual_level_view_form`
- Name: hr.leave.accrual.level.form
- Model: `hr.leave.accrual.level`
- Type: inferred from arch
- Root tag: `form`
- Field references: 26
- Sample fields: `accrual_validity`, `accrual_validity_count`, `accrual_validity_type`, `action_with_unused_accruals`, `added_value`, `added_value_type`, `can_modify_value_type`, `cap_accrued_time`, `cap_accrued_time_yearly`, `carryover_options`, and 16 more
- Buttons: `action_save_new`, `unlink`
- XPath or positional patches: 0

## Actions

- `open_view_accrual_plans`: `act_window` Accrual Plans

## Navigation

- **Parent:** [[docs/Community Addons/hr_holidays/Views]]

<!-- GENERATED:VIEWFILE -->
