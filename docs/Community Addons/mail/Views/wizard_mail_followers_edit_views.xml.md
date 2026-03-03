---
tags: [odoo, community, generated, views]
---

# wizard/mail_followers_edit_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `wizard/mail_followers_edit_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `mail_followers_list_edit_form`
- Name: mail.followers.list.edit.form
- Model: `mail.followers.edit`
- Type: inferred from arch
- Inherits: `mail_followers_edit_form`
- Root tag: `data`
- Field references: 1
- Sample fields: `operation`
- Buttons: `edit_followers`
- XPath or positional patches: 0

### `mail_followers_edit_form`
- Name: mail.followers.edit.form
- Model: `mail.followers.edit`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `message`, `notify`, `operation`, `partner_ids`, `res_ids`, `res_model`
- Buttons: `edit_followers`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

