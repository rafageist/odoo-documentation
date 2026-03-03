---
tags: [odoo, community, generated, views]
---

# views/snailmail_views.xml

- Module: [[docs/Community Addons/snailmail/snailmail|snailmail]]
- Scope: Community Addons
- Source file: `views/snailmail_views.xml`
- Views: 2
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `snailmail_letter_form`
- Name: snailmail.letter.form
- Model: `snailmail.letter`
- Type: inferred from arch
- Root tag: `form`
- Field references: 12
- Sample fields: `attachment_datas`, `attachment_fname`, `color`, `display_name`, `duplex`, `info_msg`, `model`, `partner_id`, `reference`, `res_id`, and 2 more
- Buttons: `cancel`, `snailmail_print`
- XPath or positional patches: 0

### `snailmail_letter_list`
- Name: snailmail.letter.list
- Model: `snailmail.letter`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `attachment_id`, `company_id`, `info_msg`, `partner_id`, `state`, `user_id`
- XPath or positional patches: 0

## Actions

- `action_mail_letters`: `act_window` Snailmail Letters

## Menus

- `menu_snailmail_letters`: unnamed

## Navigation

- **Parent:** [[docs/Community Addons/snailmail/Views]]

