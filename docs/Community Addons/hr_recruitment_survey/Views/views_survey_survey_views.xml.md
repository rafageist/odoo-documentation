<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/survey_survey_views.xml

- Module: [[docs/Community Addons/hr_recruitment_survey/hr_recruitment_survey|hr_recruitment_survey]]
- Scope: Community Addons
- Source file: `views/survey_survey_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `survey_survey_view_kanban`
- Name: survey.survey.view.kanban.inherit.recruitment
- Model: `survey.survey`
- Type: inferred from arch
- Inherits: `survey.survey_survey_view_kanban`
- Root tag: `button`
- Field references: 0
- Buttons: `action_send_survey`, `action_start_session`
- XPath or positional patches: 0

### `survey_survey_view_form`
- Name: survey.survey.view.form.inherit.recruitment
- Model: `survey.survey`
- Type: inferred from arch
- Inherits: `survey.survey_survey_view_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_archive`, `action_send_survey`, `action_start_session`
- XPath or positional patches: 8

## Actions

- `survey_survey_action_recruitment`: `act_window` Interviews

## Menus

- `menu_hr_recruitment_config_surveys`: Interviews

## Navigation

- **Parent:** [[docs/Community Addons/hr_recruitment_survey/Views]]

<!-- GENERATED:VIEWFILE -->
