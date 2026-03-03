---
tags: [odoo, community, generated, views]
---

# views/mail_message_reaction_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_message_reaction_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mail_message_reaction_view_tree`
- Name: mail.message.reaction.list
- Model: `mail.message.reaction`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `content`, `guest_id`, `id`, `message_id`, `partner_id`
- XPath or positional patches: 0

### `mail_message_reaction_view_form`
- Name: mail.message.reaction.form
- Model: `mail.message.reaction`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `content`, `guest_id`, `message_id`, `partner_id`
- XPath or positional patches: 0

## Actions

- `mail_message_reaction_action`: `act_window` Message Reactions

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

