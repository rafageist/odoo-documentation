<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_employee_views.xml

- Module: [[docs/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]]
- Scope: Enterprise Addons
- Source file: `views/hr_employee_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_employee_tree`
- Name: hr.employee.view.list.inherit
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `next_appraisal_date`
- Buttons: `%(action_open_appraisal_campaign_wizard)d`
- XPath or positional patches: 2

### `hr_employee_select_from_goal_view_list`
- Name: hr.employee.select.from.goal.view.list
- Model: `hr.employee`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `department_id`, `employee_id`, `job_id`
- XPath or positional patches: 0

### `hr_employee_view_form`
- Name: hr.employee.view.form.inherit.appraisal
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `appraisal_count`, `goals_count`, `last_ongoing_appraisal_date`, `next_appraisal_date`, `ongoing_appraisal_count`
- Buttons: `action_open_employee_appraisals`, `action_open_goals`, `action_open_versions`, `action_send_appraisal_request`
- XPath or positional patches: 3

### `hr_employee_view_search`
- Name: hr.employee.view.search.inherit.appraisal
- Model: `hr.employee`
- Type: inferred from arch
- Inherits: `hr.view_employee_filter`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

## Actions

- `hr.act_hr_employee_tree_view`: `view`
- `action_create_multi_appraisals`: `server` Request Appraisals

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal/Views]]

<!-- GENERATED:VIEWFILE -->
