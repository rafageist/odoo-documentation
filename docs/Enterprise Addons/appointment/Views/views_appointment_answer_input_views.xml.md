<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/appointment_answer_input_views.xml

- Module: [[docs/Enterprise Addons/appointment/appointment|appointment]]
- Scope: Enterprise Addons
- Source file: `views/appointment_answer_input_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `appointment_answer_input_view_pivot`
- Name: appointment.answer.input.view.pivot
- Model: `appointment.answer.input`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 2
- Sample fields: `question_id`, `value_answer_id`
- XPath or positional patches: 0

### `appointment_answer_input_view_graph`
- Name: appointment.answer.input.view.graph
- Model: `appointment.answer.input`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 1
- Sample fields: `value_answer_id`
- XPath or positional patches: 0

### `appointment_answer_input_view_tree`
- Name: appointment.answer.input.view.list
- Model: `appointment.answer.input`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `appointment_type_id`, `create_date`, `partner_id`, `question_id`, `value_answer_id`, `value_text_box`
- XPath or positional patches: 0

### `appointment_answer_input_view_form`
- Name: appointment.answer.input.view.form
- Model: `appointment.answer.input`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `appointment_type_id`, `calendar_event_id`, `partner_id`, `question_id`, `question_type`, `value_answer_id`, `value_text_box`
- XPath or positional patches: 0

### `appointment_answer_input_view_search`
- Name: appointment.answer.input.view.search
- Model: `appointment.answer.input`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `appointment_type_id`, `question_id`, `value_answer_id`, `value_text_box`
- XPath or positional patches: 0

## Actions

- `appointment_answer_input_action`: `act_window` Answer Breakdown

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment/Views]]

<!-- GENERATED:VIEWFILE -->
