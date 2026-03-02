<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_job_views.xml

- Module: [[docs/Community Addons/hr/hr|hr]]
- Scope: Community Addons
- Source file: `views/hr_job_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_job_filter`
- Name: hr.job.search
- Model: `hr.job`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `department_id`, `name`
- XPath or positional patches: 0

### `hr_job_view_kanban`
- Name: hr.job.kanban
- Model: `hr.job`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `department_id`, `expected_employees`, `name`
- XPath or positional patches: 0

### `view_hr_job_tree`
- Name: hr.job.list
- Model: `hr.job`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `name`, `no_of_employee`, `sequence`
- XPath or positional patches: 0

### `view_hr_job_form`
- Name: hr.job.form
- Model: `hr.job`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `active`, `company_id`, `contract_type_id`, `department_id`, `description`, `name`, `no_of_recruitment`, `user_id`
- XPath or positional patches: 0

## Actions

- `action_hr_job`: `act_window` Job Positions
- `action_create_job_position`: `act_window` Create a Job Position

## Navigation

- **Parent:** [[docs/Community Addons/hr/Views]]

<!-- GENERATED:VIEWFILE -->
