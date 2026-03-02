<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_work_entry_views.xml

- Module: [[docs/Community Addons/hr_work_entry/hr_work_entry|hr_work_entry]]
- Scope: Community Addons
- Source file: `views/hr_work_entry_views.xml`
- Views: 11
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `hr_work_entry_type_view_kanban`
- Name: hr.work.entry.type.kanban.view
- Model: `hr.work.entry.type`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `code`, `color`, `display_code`, `name`
- XPath or positional patches: 0

### `hr_work_entry_type_view_form`
- Name: hr.work.entry.type.form
- Model: `hr.work.entry.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `active`, `amount_rate`, `code`, `color`, `country_id`, `display_code`, `external_code`, `is_extra_hours`, `name`, `sequence`
- XPath or positional patches: 0

### `hr_work_entry_type_view_tree`
- Name: hr.work.entry.type.list
- Model: `hr.work.entry.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `code`, `color`, `country_id`, `display_code`, `name`
- XPath or positional patches: 0

### `hr_work_entry_type_view_search`
- Name: hr.work.entry.type.view.search
- Model: `hr.work.entry.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `hr_work_entry_view_search`
- Name: hr.work.entry.filter
- Model: `hr.work.entry`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `department_id`, `employee_id`, `name`, `work_entry_type_id`
- XPath or positional patches: 0

### `hr_work_entry_view_pivot`
- Name: hr.work.entry.pivot
- Model: `hr.work.entry`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `duration`, `employee_id`, `work_entry_type_id`
- XPath or positional patches: 0

### `hr_work_entry_view_tree`
- Name: hr.work.entry.list
- Model: `hr.work.entry`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `code`, `date`, `duration`, `employee_id`, `external_code`, `name`, `state`, `work_entry_type_id`
- XPath or positional patches: 0

### `hr_work_entry_calendar_gantt_view_form`
- Name: hr.work.entry.form
- Model: `hr.work.entry`
- Type: inferred from arch
- Inherits: `hr_work_entry.hr_work_entry_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 4

### `hr_work_entry_view_form`
- Name: hr.work.entry.form
- Model: `hr.work.entry`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `company_id`, `date`, `duration`, `employee_id`, `name`, `state`, `work_entry_type_id`
- XPath or positional patches: 0

### `hr_work_entry_view_calendar`
- Name: hr.work.entry.calendar
- Model: `hr.work.entry`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 6
- Sample fields: `display_code`, `duration`, `employee_id`, `name`, `state`, `work_entry_type_id`
- XPath or positional patches: 0

### `hr_work_entry_view_calendar_multi_create_form`
- Name: hr.work.entry.calendar.multi_create
- Model: `hr.work.entry`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `color`, `display_code`, `duration`, `employee_id`, `name`, `work_entry_type_id`
- XPath or positional patches: 0

## Actions

- `hr_work_entry_type_action`: `act_window` Work Entry Types
- `hr_work_entry_action`: `act_window` Work Entry
- `hr_work_entry_action_conflict`: `act_window` Work Entry

## Navigation

- **Parent:** [[docs/Community Addons/hr_work_entry/Views]]

<!-- GENERATED:VIEWFILE -->
