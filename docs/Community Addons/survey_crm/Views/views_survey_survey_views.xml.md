---
tags: [odoo, community, generated, views]
---

# views/survey_survey_views.xml

- Module: [[docs/Community Addons/survey_crm/survey_crm|survey_crm]]
- Scope: Community Addons
- Source file: `views/survey_survey_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `survey_survey_view_kanban`
- Name: survey.survey.view.kanban.inherit.survey.crm
- Model: `survey.survey`
- Type: inferred from arch
- Inherits: `survey.survey_survey_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `lead_count`
- XPath or positional patches: 1

### `survey_survey_view_form`
- Name: survey.survey.view.form.inherit.survey.crm
- Model: `survey.survey`
- Type: inferred from arch
- Inherits: `survey.survey_survey_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `lead_count`, `team_id`
- Buttons: `action_survey_see_leads`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Community Addons/survey_crm/Views]]

