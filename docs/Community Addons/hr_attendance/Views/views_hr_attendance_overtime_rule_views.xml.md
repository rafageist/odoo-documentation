<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_attendance_overtime_rule_views.xml

- Module: [[docs/Community Addons/hr_attendance/hr_attendance|hr_attendance]]
- Scope: Community Addons
- Source file: `views/hr_attendance_overtime_rule_views.xml`
- Views: 5
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `hr_attendance_overtime_ruleset_view_filter`
- Name: hr_attendance_overtime_ruleset_view_filter
- Model: `hr.attendance.overtime.ruleset`
- Type: inferred from arch
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 0

### `hr_attendance_overtime_ruleset_view_list`
- Name: hr.attendance.overtime.ruleset.list
- Model: `hr.attendance.overtime.ruleset`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `country_id`, `name`, `rate_combination_mode`, `rules_count`
- XPath or positional patches: 0

### `hr_attendance_overtime_ruleset_view_form`
- Name: hr.attendance.overtime.ruleset.form
- Model: `hr.attendance.overtime.ruleset`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `active`, `amount_rate`, `base_off`, `country_id`, `description`, `information_display`, `name`, `rate_combination_mode`, `rule_ids`, `sequence`
- Buttons: `action_regenerate_overtimes`
- XPath or positional patches: 0

### `hr_attendance_overtime_rule_view_list`
- Name: hr.attendance.overtime.rule.list
- Model: `hr.attendance.overtime.rule`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `base_off`, `expected_hours`, `expected_hours_from_contract`, `name`, `resource_calendar_id`
- XPath or positional patches: 0

### `hr_attendance_overtime_rule_view_form`
- Name: hr.attendance.overtime.rule.form
- Model: `hr.attendance.overtime.rule`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `amount_rate`, `base_off`, `company_id`, `description`, `employer_tolerance`, `expected_hours`, `expected_hours_from_contract`, `name`, `paid`, `quantity_period`, and 4 more
- XPath or positional patches: 0

## Actions

- `hr_attendance_overtime_ruleset_action`: `act_window` Rulesets
- `hr_attendance_overtime_rule_action`: `act_window` Overtime Rules

## Menus

- `menu_hr_attendance_overtime_rulesets`: Overtime Rulesets

## Navigation

- **Parent:** [[docs/Community Addons/hr_attendance/Views]]

<!-- GENERATED:VIEWFILE -->
