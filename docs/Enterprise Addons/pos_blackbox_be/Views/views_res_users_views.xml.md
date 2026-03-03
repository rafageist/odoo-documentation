---
tags: [odoo, enterprise, generated, views]
---

# views/res_users_views.xml

- Module: [[docs/Enterprise Addons/pos_blackbox_be/pos_blackbox_be|pos_blackbox_be]]
- Scope: Enterprise Addons
- Source file: `views/res_users_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `res_users_view_form_profile`
- Name: res.users.preferences.form.inherit
- Model: `res.users`
- Type: inferred from arch
- Inherits: `hr.res_users_view_form_preferences`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `insz_or_bis_number`
- XPath or positional patches: 1

### `res_users_form_view`
- Name: res.users.form.view
- Model: `res.users`
- Type: inferred from arch
- Inherits: `base.view_users_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `insz_or_bis_number`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/pos_blackbox_be/Views]]

