<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_question_views.xml

- Module: [[docs/Community Addons/event/event|event]]
- Scope: Community Addons
- Source file: `views/event_question_views.xml`
- Views: 4
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `event_question_view_list_add`
- Name: event.question.view.list.add
- Model: `event.question`
- Type: inferred from arch
- Inherits: `event.event_question_view_list`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `event_question_view_list`
- Name: event.question.view.list
- Model: `event.question`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `answer_ids`, `is_default`, `is_mandatory_answer`, `is_reusable`, `once_per_order`, `question_type`, `title`
- Buttons: `action_view_question_answers`
- XPath or positional patches: 0

### `event_question_view_form`
- Name: event.question.view.form
- Model: `event.question`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `answer_ids`, `display_name`, `event_count`, `event_type_ids`, `is_default`, `is_mandatory_answer`, `is_reusable`, `name`, `once_per_order`, `question_type`, and 2 more
- Buttons: `action_event_view`, `action_view_question_answers`
- XPath or positional patches: 0

### `event_question_view_search`
- Name: event.question.view.search
- Model: `event.question`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `answer_ids`, `question_type`, `title`
- XPath or positional patches: 0

## Actions

- `event_question_action`: `act_window` Event Question

## Menus

- `event_question_menu`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/event/Views]]

<!-- GENERATED:VIEWFILE -->
