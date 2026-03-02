<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mail_activity_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_activity_views.xml`
- Views: 13
- Actions: 11
- Menus: 0
- Rules: 0

## View records

### `mail_activity_view_calendar`
- Name: mail.activity.view.calendar
- Model: `mail.activity`
- Type: inferred from arch
- Root tag: `calendar`
- Field references: 5
- Sample fields: `activity_type_id`, `date_deadline`, `res_name`, `summary`, `user_id`
- XPath or positional patches: 0

### `mail_activity_view_kanban_open_target`
- Name: mail.activity.view.kanban.open.target
- Model: `mail.activity`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `active`, `activity_type_id`, `date_deadline`, `icon`, `res_model_id`, `res_name`, `summary`, `user_id`
- Buttons: `action_done`, `unlink`
- XPath or positional patches: 0

### `mail_activity_view_tree_open_target`
- Name: mail.activity.view.list.open.target
- Model: `mail.activity`
- Type: inferred from arch
- Inherits: `mail_activity_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `mail_activity_view_tree_without_record_access`
- Name: mail.activity.view.list.without.record.access
- Model: `mail.activity`
- Type: inferred from arch
- Inherits: `mail_activity_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `mail_activity_view_tree`
- Name: mail.activity.view.list
- Model: `mail.activity`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `activity_type_id`, `date_deadline`, `date_done`, `feedback`, `res_name`, `summary`, `user_id`
- Buttons: `action_cancel`, `action_done`, `action_reschedule_nextweek`, `action_reschedule_today`, `action_reschedule_tomorrow`, `unlink`
- XPath or positional patches: 0

### `mail_activity_view_search`
- Name: mail.activity.view.search
- Model: `mail.activity`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `activity_type_id`, `res_name`, `user_id`
- XPath or positional patches: 0

### `mail_activity_view_form_without_record_access`
- Name: mail.activity.view.form.without.record.access
- Model: `mail.activity`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `activity_type_id`, `date_deadline`, `display_name`, `note`, `summary`
- Buttons: `action_done_redirect_to_other`
- XPath or positional patches: 0

### `mail_activity_view_form`
- Name: mail.activity.view.form
- Model: `mail.activity`
- Type: inferred from arch
- Inherits: `mail.mail_activity_view_form_popup`
- Root tag: `field`
- Field references: 2
- Sample fields: `activity_type_id`, `res_name`
- XPath or positional patches: 2

### `mail_activity_view_form_popup`
- Name: mail.activity.view.form.popup
- Model: `mail.activity`
- Type: inferred from arch
- Root tag: `form`
- Field references: 14
- Sample fields: `activity_category`, `activity_type_id`, `chaining_type`, `date_deadline`, `has_recommended_activities`, `id`, `note`, `previous_activity_type_id`, `recommended_activity_type_id`, `res_id`, and 4 more
- Buttons: `action_close_dialog`, `action_done`, `action_open_document`
- XPath or positional patches: 0

### `mail_activity_type_view_kanban`
- Name: mail.activity.type.view.kanban
- Model: `mail.activity.type`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `default_user_id`, `icon`, `name`, `res_model`, `summary`
- XPath or positional patches: 0

### `mail_activity_type_view_tree`
- Name: mail.activity.type.view.list
- Model: `mail.activity.type`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `delay_from`, `delay_label`, `icon`, `name`, `res_model`, `sequence`, `suggested_next_type_ids`, `summary`, `triggered_next_type_id`
- XPath or positional patches: 0

### `mail_activity_type_view_search`
- Name: mail.activity.type.search
- Model: `mail.activity.type`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `mail_activity_type_view_form`
- Name: mail.activity.type.view.form
- Model: `mail.activity.type`
- Type: inferred from arch
- Root tag: `form`
- Field references: 18
- Sample fields: `active`, `category`, `chaining_type`, `decoration_type`, `default_note`, `default_user_id`, `delay_count`, `delay_from`, `delay_unit`, `icon`, and 8 more
- XPath or positional patches: 0

## Actions

- `mail_activity_action_my_view_calendar`: `view`
- `mail_activity_action_my_view_kanban`: `view`
- `mail_activity_action_my_view_tree`: `view`
- `mail_activity_action_my`: `act_window` My Activities
- `mail_activity_action_without_access_view_form`: `view`
- `mail_activity_action_without_access_view_tree`: `view`
- `mail_activity_without_access_action`: `act_window` Other activities
- `mail_activity_action_view_form`: `view`
- `mail_activity_action_view_tree`: `view`
- `mail_activity_action`: `act_window` Activity Overview
- `mail_activity_type_action`: `act_window` Activity Types

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

<!-- GENERATED:VIEWFILE -->
