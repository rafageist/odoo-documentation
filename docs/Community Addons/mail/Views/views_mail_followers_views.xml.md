---
tags: [odoo, community, generated, views]
---

# views/mail_followers_views.xml

- Module: [[docs/Community Addons/mail/mail|mail]]
- Scope: Community Addons
- Source file: `views/mail_followers_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_mail_subscription_form`
- Name: mail.followers.form
- Model: `mail.followers`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `partner_id`, `res_id`, `res_model`, `subtype_ids`
- XPath or positional patches: 0

### `view_followers_tree`
- Name: mail.followers.list
- Model: `mail.followers`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `partner_id`, `res_id`, `res_model`
- XPath or positional patches: 0

## Actions

- `action_view_followers`: `act_window` Followers

## Navigation

- **Parent:** [[docs/Community Addons/mail/Views]]

