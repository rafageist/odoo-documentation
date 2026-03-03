---
tags: [odoo, community, generated, views]
---

# views/slide_question_views.xml

- Module: [[docs/Community Addons/website_slides/website_slides|website_slides]]
- Scope: Community Addons
- Source file: `views/slide_question_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `slide_question_view_search`
- Name: slide.question.view.search
- Model: `slide.question`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `question`, `slide_id`
- XPath or positional patches: 0

### `slide_question_view_tree_report`
- Name: slide.question.view.list.report
- Model: `slide.question`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `attempts_avg`, `attempts_count`, `done_count`, `question`, `sequence`, `slide_id`
- XPath or positional patches: 0

### `slide_question_view_tree`
- Name: slide.question.view.list
- Model: `slide.question`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `question`, `sequence`, `slide_id`
- XPath or positional patches: 0

### `slide_question_view_form`
- Name: slide.question.view.form
- Model: `slide.question`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `answer_ids`, `answers_validation_error`, `comment`, `display_name`, `is_correct`, `question`, `text_value`
- XPath or positional patches: 0

## Actions

- `slide_question_action_report`: `act_window` Quizzes

## Navigation

- **Parent:** [[docs/Community Addons/website_slides/Views]]

