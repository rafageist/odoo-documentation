---
tags: [odoo, enterprise, generated, views]
---

# views/hr_work_entry_views.xml

- Module: [[docs/Enterprise Addons/hr_work_entry_enterprise/hr_work_entry_enterprise|hr_work_entry_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/hr_work_entry_views.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `hr_work_entry_gantt`
- Name: hr.work.entry.gantt
- Model: `hr.work.entry`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 7
- Sample fields: `color`, `display_code`, `duration`, `employee_id`, `name`, `state`, `work_entry_type_id`
- XPath or positional patches: 0

### `hr_work_entry_view_gantt_multi_create_form`
- Name: hr.work.entry.gantt.multi_create
- Model: `hr.work.entry`
- Type: inferred from arch
- Inherits: `hr_work_entry.hr_work_entry_view_calendar_multi_create_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `hr_work_entry_action_conflict_view_gantt`: `view`
- `hr_work_entry_action_view_gantt`: `view`

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_work_entry_enterprise/Views]]

