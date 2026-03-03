---
tags: [odoo, community, generated, views]
---

# views/mail_group_member_views.xml

- Module: [[docs/Community Addons/mail_group/mail_group|mail_group]]
- Scope: Community Addons
- Source file: `views/mail_group_member_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mail_group_member_view_search`
- Name: mail.group.member.view.search
- Model: `mail.group.member`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `email`, `mail_group_id`, `partner_id`
- XPath or positional patches: 0

### `mail_group_member_view_tree`
- Name: mail.group.member.view.list
- Model: `mail.group.member`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `email`, `email_normalized`, `mail_group_id`, `partner_id`
- Buttons: `%(mail_group.mail_compose_message_action_mail_group)d`
- XPath or positional patches: 0

## Actions

- `mail_group_member_action`: `act_window` Members

## Navigation

- **Parent:** [[docs/Community Addons/mail_group/Views]]

