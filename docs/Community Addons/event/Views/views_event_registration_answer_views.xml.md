<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/event_registration_answer_views.xml

- Module: [[docs/Community Addons/event/event|event]]
- Scope: Community Addons
- Source file: `views/event_registration_answer_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `event_registration_answer_view_pivot`
- Name: event.registration.answer.view.pivot
- Model: `event.registration.answer`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `registration_id`, `value_answer_id`
- XPath or positional patches: 0

### `event_registration_answer_view_graph`
- Name: event.registration.answer.view.graph
- Model: `event.registration.answer`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 2
- Sample fields: `event_id`, `value_answer_id`
- XPath or positional patches: 0

### `event_registration_answer_view_tree`
- Name: event.registration.answer.view.list
- Model: `event.registration.answer`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `event_id`, `partner_id`, `question_id`, `registration_id`, `value_answer_id`, `value_text_box`
- XPath or positional patches: 0

### `event_registration_answer_view_search`
- Name: event.registration.answer.view.search
- Model: `event.registration.answer`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `event_id`, `question_id`, `value_answer_id`, `value_text_box`
- XPath or positional patches: 0

## Actions

- `action_event_registration_report`: `act_window` Answer Breakdown

## Navigation

- **Parent:** [[docs/Community Addons/event/Views]]

<!-- GENERATED:VIEWFILE -->
