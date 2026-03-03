---
tags: [odoo, community, generated, views]
---

# views/event_quiz_views.xml

- Module: [[docs/Community Addons/website_event_track_quiz/website_event_track_quiz|website_event_track_quiz]]
- Scope: Community Addons
- Source file: `views/event_quiz_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `event_quiz_view_form`
- Name: event.quiz.view.form
- Model: `event.quiz`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `event_id`, `event_track_id`, `name`, `question_ids`, `repeatable`
- XPath or positional patches: 0

### `event_quiz_view_tree`
- Name: event.quiz.view.list
- Model: `event.quiz`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `event_id`, `event_track_id`, `name`
- XPath or positional patches: 0

### `event_quiz_view_search`
- Name: event.quiz.view.search
- Model: `event.quiz`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `event_id`, `event_track_id`, `name`
- XPath or positional patches: 0

## Actions

- `event_quiz_action`: `act_window` Event Quizzes

## Navigation

- **Parent:** [[docs/Community Addons/website_event_track_quiz/Views]]

