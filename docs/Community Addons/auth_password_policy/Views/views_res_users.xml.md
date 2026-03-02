<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_users.xml

- Module: [[docs/Community Addons/auth_password_policy/auth_password_policy|auth_password_policy]]
- Scope: Community Addons
- Source file: `views/res_users.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `change_password_multi`
- Name: Enable password meter on multi passwords wizard
- Model: `change.password.user`
- Type: inferred from arch
- Inherits: `base.change_password_wizard_user_tree_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `change_password`
- Name: Enable password meter on own password wizard
- Model: `change.password.own`
- Type: inferred from arch
- Inherits: `base.change_password_own_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Community Addons/auth_password_policy/Views]]

<!-- GENERATED:VIEWFILE -->
