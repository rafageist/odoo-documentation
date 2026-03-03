---
tags: [odoo, community, generated, views]
---

# views/mail_notification_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_notification_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mail_notification_view_form`
- Name: mail.notification.view.form
- Model: `mail.notification`
- Type: inferred from arch
- Root tag: `form`
- Field references: 9
- Sample fields: `failure_reason`, `failure_type`, `is_read`, `mail_mail_id`, `mail_message_id`, `notification_status`, `notification_type`, `read_date`, `res_partner_id`
- XPath or positional patches: 0

### `mail_notification_view_tree`
- Name: mail.notification.view.list
- Model: `mail.notification`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `failure_type`, `is_read`, `mail_message_id`, `notification_type`, `res_partner_id`
- XPath or positional patches: 0

## Actions

- `mail_notification_action`: `act_window` Notifications

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

