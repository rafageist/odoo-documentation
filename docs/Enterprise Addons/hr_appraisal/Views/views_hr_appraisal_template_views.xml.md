---
tags: [odoo, enterprise, generated, views]
---

# views/hr_appraisal_template_views.xml

- Module: [[docs/Enterprise Addons/hr_appraisal/hr_appraisal|hr_appraisal]]
- Scope: Enterprise Addons
- Source file: `views/hr_appraisal_template_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `hr_appraisal_template_view_tree`
- Name: hr.appraisal.template.list
- Model: `hr.appraisal.template`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `company_id`, `department_ids`, `description`, `sequence`
- XPath or positional patches: 0

### `view_hr_appraisal_template_form`
- Name: hr.appraisal.template.form
- Model: `hr.appraisal.template`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `appraisal_employee_feedback_template`, `appraisal_manager_feedback_template`, `company_id`, `department_ids`, `description`
- XPath or positional patches: 0

## Actions

- `hr_appraisal_config_templates_action`: `act_window` Appraisal Template

## Menus

- `hr_appraisal_template_menu`: Appraisal Templates

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal/Views]]

