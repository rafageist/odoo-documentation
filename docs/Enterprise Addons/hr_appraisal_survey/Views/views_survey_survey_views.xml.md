---
tags: [odoo, enterprise, generated, views]
---

# views/survey_survey_views.xml

- Module: [[docs/Enterprise Addons/hr_appraisal_survey/hr_appraisal_survey|hr_appraisal_survey]]
- Scope: Enterprise Addons
- Source file: `views/survey_survey_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `survey_survey_view_kanban`
- Name: survey.survey.view.kanban.inherit.appraisal
- Model: `survey.survey`
- Type: inferred from arch
- Inherits: `survey.survey_survey_view_kanban`
- Root tag: `button`
- Field references: 0
- Buttons: `action_result_survey`, `action_send_survey`, `action_start_session`
- XPath or positional patches: 0

### `survey_survey_view_form`
- Name: survey.survey.view.form.inherit.appraisal
- Model: `survey.survey`
- Type: inferred from arch
- Inherits: `survey.survey_survey_view_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_archive`, `action_result_survey`, `action_send_survey`
- XPath or positional patches: 8

## Actions

- `survey_survey_action_appraisal`: `act_window` 360 Feedback

## Menus

- `menu_hr_appraisal_surveys`: 360 Feedback

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_appraisal_survey/Views]]

