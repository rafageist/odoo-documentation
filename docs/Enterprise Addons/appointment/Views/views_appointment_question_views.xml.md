<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/appointment_question_views.xml

- Module: [[docs/Enterprise Addons/appointment/appointment|appointment]]
- Scope: Enterprise Addons
- Source file: `views/appointment_question_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `appointment_question_view_list`
- Name: appointment.question.view.list
- Model: `appointment.question`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `answer_ids`, `is_default`, `is_reusable`, `name`, `placeholder`, `question_required`, `question_type`, `sequence`
- Buttons: `action_view_question_answer_inputs`
- XPath or positional patches: 0

### `appointment_question_view_form`
- Name: appointment.question.view.form
- Model: `appointment.question`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `active`, `answer_ids`, `appointment_count`, `extra_comment`, `is_default`, `is_reusable`, `name`, `placeholder`, `question_required`, `question_type`, and 1 more
- Buttons: `action_view_appointment_types`
- XPath or positional patches: 0

### `appointment_question_view_search`
- Name: appointment.question.view.search
- Model: `appointment.question`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `appointment_type_ids`, `name`, `question_type`
- XPath or positional patches: 0

## Actions

- `appointment_question_action`: `act_window` Questions

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment/Views]]

<!-- GENERATED:VIEWFILE -->
