---
tags: [odoo, enterprise, generated, views]
---

# views/appointment_invite_views.xml

- Module: [[docs/Enterprise Addons/appointment/appointment|appointment]]
- Scope: Enterprise Addons
- Source file: `views/appointment_invite_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `appointment_invite_view_form_insert_link`
- Name: appointment.invite.view.form
- Model: `appointment.invite`
- Type: inferred from arch
- Inherits: `appointment_invite_view_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `appointment_invite_view_form`
- Name: appointment.invite.view.form
- Model: `appointment.invite`
- Type: inferred from arch
- Root tag: `form`
- Field references: 19
- Sample fields: `appointment_type_count`, `appointment_type_ids`, `appointment_type_info_msg`, `base_book_url`, `book_url`, `book_url_params`, `identical_config_id`, `resource_ids`, `resources_choice`, `resources_resource_choice`, and 9 more
- XPath or positional patches: 0

### `appointment_invite_view_tree`
- Name: appointment.invite.view.list
- Model: `appointment.invite`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `appointment_type_count`, `appointment_type_ids`, `book_url`, `calendar_event_count`, `create_date`, `create_uid`, `resource_ids`, `staff_user_ids`, `suggested_resource_ids`, `suggested_staff_user_ids`
- XPath or positional patches: 0

### `appointment_invite_view_search`
- Name: appointment.invite.view.search
- Model: `appointment.invite`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `appointment_type_ids`, `resource_ids`, `short_code`, `staff_user_ids`
- XPath or positional patches: 0

## Actions

- `appointment_invite_action_stat`: `act_window` Share Links
- `appointment_invite_action`: `act_window` Share Links

## Navigation

- **Parent:** [[docs/Enterprise Addons/appointment/Views]]

