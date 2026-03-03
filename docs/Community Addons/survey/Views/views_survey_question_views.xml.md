---
tags: [odoo, community, generated, views]
---

# views/survey_question_views.xml

- Module: [[docs/Community Addons/survey/survey|survey]]
- Scope: Community Addons
- Source file: `views/survey_question_views.xml`
- Views: 6
- Actions: 2
- Menus: 3
- Rules: 0

## View records

### `survey_question_answer_view_search`
- Name: survey.question.answer.view.search
- Model: `survey.question.answer`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `question_id`
- XPath or positional patches: 0

### `survey_question_answer_view_form`
- Name: survey.question.answer.view.form
- Model: `survey.question.answer`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `answer_score`, `is_correct`, `matrix_question_id`, `question_id`, `question_type`, `scoring_type`, `sequence`, `value`, `value_image`
- XPath or positional patches: 0

### `survey_question_answer_view_tree`
- Name: survey.question.answer.view.list
- Model: `survey.question.answer`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `answer_score`, `question_id`, `sequence`, `value`
- XPath or positional patches: 0

### `survey_question_search`
- Name: Search view for survey question
- Model: `survey.question`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `question_type`, `survey_id`, `title`
- XPath or positional patches: 0

### `survey_question_tree`
- Name: List view for survey question
- Model: `survey.question`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `constr_mandatory`, `question_type`, `survey_id`, `title`
- XPath or positional patches: 0

### `survey_question_form`
- Name: Form view for survey question
- Model: `survey.question`
- Type: inferred from arch
- Root tag: `form`
- Field references: 55
- Sample fields: `allowed_triggering_question_ids`, `answer_date`, `answer_datetime`, `answer_numerical_box`, `answer_score`, `background_image`, `comment_count_as_answer`, `comments_allowed`, `comments_message`, `constr_error_msg`, and 45 more
- XPath or positional patches: 0

## Actions

- `survey_question_answer_action`: `act_window` Suggested Values
- `action_survey_question_form`: `act_window` Questions

## Menus

- `menu_survey_response_line_form`: Detailed Answers
- `menu_survey_label_form1`: Suggested Values
- `menu_survey_question_form1`: Questions

## Navigation

- **Parent:** [[docs/Community Addons/survey/Views]]

