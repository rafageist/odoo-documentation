<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/survey_user_views.xml

- Module: [[docs/Community Addons/survey/survey|survey]]
- Scope: Community Addons
- Source file: `views/survey_user_views.xml`
- Views: 7
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `survey_user_input_line_view_search`
- Name: survey.user_input.line.view.search
- Model: `survey.user_input.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `survey_id`, `user_input_id`
- XPath or positional patches: 0

### `survey_response_line_view_tree`
- Name: survey.user_input.line.view.list
- Model: `survey.user_input.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `answer_score`, `answer_type`, `create_date`, `question_id`, `skipped`, `survey_id`, `user_input_id`
- XPath or positional patches: 0

### `survey_user_input_line_view_form`
- Name: survey.user_input.line.view.form
- Model: `survey.user_input.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `answer_score`, `answer_type`, `create_date`, `matrix_row_id`, `question_id`, `skipped`, `suggested_answer_id`, `value_char_box`, `value_date`, `value_datetime`, and 2 more
- XPath or positional patches: 0

### `survey_user_input_viuew_kanban`
- Name: survey.user_input.view.kanban
- Model: `survey.user_input`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `create_date`, `state`, `survey_id`
- XPath or positional patches: 0

### `survey_user_input_view_tree`
- Name: survey.user_input.view.list
- Model: `survey.user_input`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `attempts_number`, `create_date`, `deadline`, `email`, `nickname`, `partner_id`, `scoring_percentage`, `scoring_success`, `state`, `survey_id`, and 1 more
- XPath or positional patches: 0

### `survey_user_input_view_form`
- Name: survey.user_input.view.form
- Model: `survey.user_input`
- Type: inferred from arch
- Root tag: `form`
- Field references: 24
- Sample fields: `access_token`, `answer_is_correct`, `answer_score`, `answer_type`, `attempts_count`, `attempts_limit`, `attempts_number`, `create_date`, `deadline`, `display_name`, and 14 more
- Buttons: `action_print_answers`, `action_redirect_to_attempts`, `action_resend`
- XPath or positional patches: 0

### `survey_user_input_view_search`
- Name: survey.user_input.view.search
- Model: `survey.user_input`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `email`, `partner_id`, `survey_id`
- XPath or positional patches: 0

## Actions

- `survey_user_input_line_action`: `act_window` Detailed Answers
- `action_survey_user_input`: `act_window` Participants

## Menus

- `menu_survey_type_form1`: Participants

## Navigation

- **Parent:** [[docs/Community Addons/survey/Views]]

<!-- GENERATED:VIEWFILE -->
