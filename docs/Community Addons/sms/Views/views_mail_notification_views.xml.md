---
tags: [odoo, community, generated, views]
---

# views/mail_notification_views.xml

- Module: [[docs/Community Addons/sms/sms|sms]]
- Scope: Community Addons
- Source file: `views/mail_notification_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `mail_notification_view_form`
- Name: mail.notification.view.form
- Model: `mail.notification`
- Type: inferred from arch
- Inherits: `mail.mail_notification_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `sms_id`, `sms_number`
- XPath or positional patches: 2

### `mail_notification_view_tree`
- Name: mail.notification.view.list
- Model: `mail.notification`
- Type: inferred from arch
- Inherits: `mail.mail_notification_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sms_number`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/sms/Views]]

