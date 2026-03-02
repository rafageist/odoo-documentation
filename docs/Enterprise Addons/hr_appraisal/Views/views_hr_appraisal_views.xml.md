<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_appraisal_views.xml

- Module: [[docs/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]]
- Scope: Enterprise Addons
- Source file: `views/hr_appraisal_views.xml`
- Views: 10
- Actions: 7
- Menus: 5
- Rules: 0

## View records

### `hr_appraisal_view_pivot`
- Name: hr.appraisal.pivot
- Model: `hr.appraisal`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `date_close`, `department_id`, `employee_appraisal_count`
- XPath or positional patches: 0

### `hr_appraisal_view_graph`
- Name: hr.appraisal.graph
- Model: `hr.appraisal`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 3
- Sample fields: `assessment_note`, `department_id`, `employee_appraisal_count`
- XPath or positional patches: 0

### `hr_appraisal_view_calendar`
- Name: hr.appraisal.calendar
- Model: `hr.appraisal`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 4
- Sample fields: `appraisal_properties`, `department_id`, `display_name`, `employee_id`
- XPath or positional patches: 0

### `hr_appraisal_view_gantt`
- Name: hr.appraisal.gantt
- Model: `hr.appraisal`
- Type: inferred from arch
- Root tag: `gantt`
- Field references: 0
- XPath or positional patches: 0

### `hr_appraisal_view_activity`
- Name: hr.appraisal.activity
- Model: `hr.appraisal`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 3
- Sample fields: `date_close`, `employee_id`, `state`
- XPath or positional patches: 0

### `hr_appraisal_kanban`
- Name: hr.appraisal.kanban
- Model: `hr.appraisal`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 9
- Sample fields: `activity_ids`, `appraisal_properties`, `avatar_128`, `date_close`, `department_id`, `employee_id`, `manager_ids`, `state`, `waiting_feedback`
- Buttons: `%(action_open_appraisal_campaign_wizard)d`
- XPath or positional patches: 0

### `hr_appraisal_search`
- Name: hr.appraisal.search
- Model: `hr.appraisal`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `activity_type_id`, `activity_user_id`, `department_id`, `employee_id`, `job_id`
- XPath or positional patches: 0

### `hr_appraisal_view_tree_orderby_create_date`
- Name: hr.appraisal.list
- Model: `hr.appraisal`
- Type: inferred from arch
- Inherits: `view_hr_appraisal_tree`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `view_hr_appraisal_tree`
- Name: hr.appraisal.list
- Model: `hr.appraisal`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `active`, `activity_exception_decoration`, `assessment_note`, `company_id`, `create_date`, `date_close`, `department_id`, `employee_id`, `next_appraisal_date`, `state`
- Buttons: `%(action_open_appraisal_campaign_wizard)d`
- XPath or positional patches: 0

### `view_hr_appraisal_form`
- Name: hr.appraisal.form
- Model: `hr.appraisal`
- Type: inferred from arch
- Root tag: `form`
- Field references: 29
- Sample fields: `accessible_employee_feedback`, `accessible_manager_feedback`, `active`, `appraisal_properties`, `appraisal_template_id`, `assessment_note`, `can_see_employee_publish`, `can_see_manager_publish`, `company_id`, `date_close`, and 19 more
- Buttons: `action_back`, `action_calendar_event`, `action_confirm`, `action_done`, `action_open_employee_appraisals`, `action_open_goals`, `action_send_appraisal_request`
- XPath or positional patches: 0

## Actions

- `hr_appraisal_action_from_department`: `act_window` Appraisal to start
- `open_view_hr_appraisal_graph_department`: `act_window` Department Appraisals
- `open_view_hr_appraisal_graph`: `act_window` Appraisal Analysis
- `open_view_hr_appraisal_tree`: `act_window` Appraisals
- `action_load_appraisal_demo_data`: `server` Load appraisal scenario
- `action_open_appraisal_campaign_wizard`: `server` Launch Campaign
- `hr_appraisal_action_multiple_appraisals`: `act_window` Appraisals

## Menus

- `menu_appraisal_analysis_report`: Appraisal Analysis
- `menu_hr_appraisal_report`: Reporting
- `menu_open_view_hr_appraisal_tree`: Appraisals
- `menu_hr_appraisal_configuration`: Configuration
- `menu_hr_appraisal_root`: Appraisals

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal/Views]]

<!-- GENERATED:VIEWFILE -->
