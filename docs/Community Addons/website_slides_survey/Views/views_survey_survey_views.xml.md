<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/survey_survey_views.xml

- Module: [[docs/Community Addons/website_slides_survey/website_slides_survey|website_slides_survey]]
- Scope: Community Addons
- Source file: `views/survey_survey_views.xml`
- Views: 4
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `survey_survey_view_kanban`
- Name: survey.survey.view.kanban.inherit.website.slides
- Model: `survey.survey`
- Type: inferred from arch
- Inherits: `survey.survey_survey_view_kanban`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `slide_channel_count`
- XPath or positional patches: 1

### `survey_survey_view_form`
- Name: survey.survey.view.form.inherit.website.slides
- Model: `survey.survey`
- Type: inferred from arch
- Inherits: `survey.survey_survey_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `slide_channel_count`
- Buttons: `action_survey_view_slide_channels`
- XPath or positional patches: 1

### `survey_survey_view_search_slides`
- Name: survey.survey.view.search.slides
- Model: `survey.survey`
- Type: inferred from arch
- Inherits: `survey.survey_survey_view_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `survey_survey_view_tree_slides`
- Name: survey.survey.view.list.slides
- Model: `survey.survey`
- Type: inferred from arch
- Inherits: `survey.survey_survey_view_tree`
- Root tag: `field`
- Field references: 4
- Sample fields: `answer_count`, `answer_score_avg`, `success_ratio`, `title`
- Buttons: `certification`
- XPath or positional patches: 0

## Actions

- `survey_survey_action_slides_view_form`: `view`
- `survey_survey_action_slides_view_tree`: `view`
- `survey_survey_action_slides_view_kanban`: `view`
- `survey_survey_action_slides`: `act_window` Certifications

## Navigation

- **Parent:** [[docs/Community Addons/website_slides_survey/Views]]

<!-- GENERATED:VIEWFILE -->
