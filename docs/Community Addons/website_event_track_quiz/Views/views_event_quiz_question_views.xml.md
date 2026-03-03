---
tags: [odoo, community, generated, views]
---

# views/event_quiz_question_views.xml

- Module: [[docs/Community Addons/website_event_track_quiz/website_event_track_quiz|website_event_track_quiz]]
- Scope: Community Addons
- Source file: `views/event_quiz_question_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `event_quiz_question_view_form_from_quiz`
- Name: event.quiz.question.view.form.from.quiz
- Model: `event.quiz.question`
- Type: inferred from arch
- Inherits: `website_event_track_quiz.event_quiz_question_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `event_quiz_question_view_form`
- Name: event.quiz.question.view.form
- Model: `event.quiz.question`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `answer_ids`, `awarded_points`, `comment`, `is_correct`, `name`, `quiz_id`, `sequence`, `text_value`
- XPath or positional patches: 0

### `event_quiz_question_view_tree_from_quiz`
- Name: event.quiz.question.view.list.from.quiz
- Model: `event.quiz.question`
- Type: inferred from arch
- Inherits: `website_event_track_quiz.event_quiz_question_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `event_quiz_question_view_tree`
- Name: event.quiz.question.view.list
- Model: `event.quiz.question`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `awarded_points`, `name`, `quiz_id`, `sequence`
- XPath or positional patches: 0

### `event_quiz_question_view_search`
- Name: event.quiz.question.view.search
- Model: `event.quiz.question`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `name`, `quiz_id`
- XPath or positional patches: 0

## Actions

- `event_quiz_question_action`: `act_window` Event Quiz Questions

## Navigation

- **Parent:** [[docs/Community Addons/website_event_track_quiz/Views]]

