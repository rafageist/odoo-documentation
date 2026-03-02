<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_appraisal_views.xml

- Module: [[docs/Enterprise Addons/hr_appraisal_survey/hr_appraisal_survey|hr_appraisal_survey]]
- Scope: Enterprise Addons
- Source file: `views/hr_appraisal_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_hr_appraisal_tree`
- Name: hr.appraisal.view.list
- Model: `hr.appraisal`
- Type: inferred from arch
- Inherits: `hr_appraisal.view_hr_appraisal_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `employee_feedback_ids`
- XPath or positional patches: 1

### `hr_appraisal_view_form`
- Name: hr.appraisal.view.form
- Model: `hr.appraisal`
- Type: inferred from arch
- Inherits: `hr_appraisal.view_hr_appraisal_form`
- Root tag: `field`
- Field references: 4
- Sample fields: `completed_survey_count`, `employee_feedback_ids`, `manager_ids`, `total_survey_count`
- Buttons: `action_ask_feedback`, `action_done`, `action_open_survey_inputs`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal_survey/Views]]

<!-- GENERATED:VIEWFILE -->
