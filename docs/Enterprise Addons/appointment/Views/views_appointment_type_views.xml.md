---
tags: [odoo, enterprise, generated, views]
---

# views/appointment_type_views.xml

- Module: [[docs/Enterprise Addons/appointment/appointment|appointment]]
- Scope: Enterprise Addons
- Source file: `views/appointment_type_views.xml`
- Views: 6
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `appointment_type_view_form_custom_share`
- Name: appointment.type.view.form.custom.share
- Model: `appointment.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `allow_guests`, `event_videocall_source`, `location_id`, `message_confirmation`, `message_intro`, `name`, `staff_user_ids`
- XPath or positional patches: 0

### `appointment_type_view_form_add_simplified`
- Name: appointment.type.view.form.add.simplified
- Model: `appointment.type`
- Type: inferred from arch
- Inherits: `appointment.appointment_type_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `appointment_type_view_form`
- Name: appointment.type.form
- Model: `appointment.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 55
- Sample fields: `active`, `allday`, `allow_guests`, `answer_ids`, `appointment_count`, `appointment_duration`, `appointment_invite_count`, `appointment_tz`, `assignment_method`, `auto_confirm`, and 45 more
- Buttons: `action_calendar_meetings`, `action_customer_preview`, `action_share_invite`, `action_view_question_answer_inputs`, `add_videocall_source`, `appointment.appointment_invite_action_stat`, `appointment.appointment_resource_action_stat`, `durationArrow`
- XPath or positional patches: 0

### `appointment_type_view_tree`
- Name: appointment.type.list
- Model: `appointment.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 8
- Sample fields: `appointment_tz`, `country_ids`, `location_id`, `name`, `resource_ids`, `schedule_based_on`, `sequence`, `staff_user_ids`
- Buttons: `action_share_invite`
- XPath or positional patches: 0

### `appointment_type_view_kanban`
- Name: appointment.type.kanban
- Model: `appointment.type`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 10
- Sample fields: `appointment_count`, `appointment_count_request`, `appointment_count_upcoming`, `appointment_duration_formatted`, `category`, `name`, `resource_ids`, `schedule_based_on`, `sequence`, `staff_user_ids`
- XPath or positional patches: 0

### `appointment_type_view_search`
- Name: appointment.type.search
- Model: `appointment.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `category`, `location_id`, `name`, `resource_ids`, `staff_user_ids`
- XPath or positional patches: 0

## Actions

- `appointment_type_action`: `act_window` Appointments

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment/Views]]

