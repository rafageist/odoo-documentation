<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/mail_message_schedule_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_message_schedule_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mail_message_schedule_view_search`
- Name: mail.message.schedule.view.search
- Model: `mail.message.schedule`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `mail_message_id`
- XPath or positional patches: 0

### `mail_message_schedule_view_tree`
- Name: mail.message.schedule.view.list
- Model: `mail.message.schedule`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `mail_message_id`, `scheduled_datetime`
- XPath or positional patches: 0

### `mail_message_schedule_view_form`
- Name: mail.message.schedule.view.form
- Model: `mail.message.schedule`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `mail_message_id`, `notification_parameters`, `scheduled_datetime`
- Buttons: `force_send`
- XPath or positional patches: 0

## Actions

- `mail_message_schedule_action`: `act_window` Scheduled Messages

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

<!-- GENERATED:VIEWFILE -->
