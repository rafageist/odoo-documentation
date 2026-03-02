<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/survey_survey_views.xml

- Module: [[docs/Community Addons/survey/survey|survey]]
- Scope: Community Addons
- Source file: `views/survey_survey_views.xml`
- Views: 7
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `survey_survey_view_pivot`
- Name: survey.survey.view.pivot
- Model: `survey.survey`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 1
- Sample fields: `color`
- XPath or positional patches: 0

### `survey_survey_view_graph`
- Name: survey.survey.view.graph
- Model: `survey.survey`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 1
- Sample fields: `color`
- XPath or positional patches: 0

### `survey_survey_view_search`
- Name: survey.survey.search
- Model: `survey.survey`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `question_and_page_ids`, `restrict_user_ids`, `title`, `user_id`
- XPath or positional patches: 0

### `survey_survey_view_activity`
- Name: survey.survey.view.activity
- Model: `survey.survey`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 2
- Sample fields: `title`, `user_id`
- XPath or positional patches: 0

### `survey_survey_view_kanban`
- Name: survey.survey.view.kanban
- Model: `survey.survey`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 15
- Sample fields: `active`, `activity_ids`, `answer_count`, `answer_done_count`, `answer_duration_avg`, `certification`, `color`, `create_date`, `question_count`, `scoring_type`, and 5 more
- Buttons: `action_end_session`, `action_result_survey`, `action_send_survey`, `action_start_session`, `action_test_survey`
- XPath or positional patches: 0

### `survey_survey_view_tree`
- Name: survey.survey.view.list
- Model: `survey.survey`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `active`, `answer_count`, `answer_done_count`, `answer_duration_avg`, `answer_score_avg`, `certification`, `success_count`, `success_ratio`, `title`, `user_id`
- Buttons: `certification`
- XPath or positional patches: 0

### `survey_survey_view_form`
- Name: survey.survey.view.form
- Model: `survey.survey`
- Type: inferred from arch
- Root tag: `form`
- Field references: 51
- Sample fields: `access_mode`, `access_token`, `active`, `allowed_survey_types`, `answer_count`, `answer_done_count`, `attempts_limit`, `background_image`, `certification`, `certification_badge_id`, and 41 more
- Buttons: `action_archive`, `action_end_session`, `action_open_session_manager`, `action_result_survey`, `action_send_survey`, `action_start_session`, `action_survey_preview_certification_template`, `action_survey_user_input`, `action_survey_user_input_certified`, `action_survey_user_input_completed`, and 3 more
- XPath or positional patches: 0

## Actions

- `action_survey_form`: `act_window` Surveys

## Menus

- `menu_survey_form`: Surveys

## Navigation

- **Parent:** [[docs/Community Addons/survey/Views]]

<!-- GENERATED:VIEWFILE -->
