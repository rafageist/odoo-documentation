<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/auth_passkey_key_views.xml

- Module: [[docs/Community Addons/auth_passkey/auth_passkey|auth_passkey]]
- Scope: Community Addons
- Source file: `views/auth_passkey_key_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `auth_passkey_key_create_view_form`
- Name: Create Passkey Wizard Form
- Model: `auth.passkey.key.create`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `name`
- Buttons: `make_key`
- XPath or positional patches: 0

### `auth_passkey_key_rename`
- Name: auth.passkey.key.rename
- Model: `auth.passkey.key`
- Type: inferred from arch
- Root tag: `form`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `auth_passkey_key_view_kanban`
- Name: auth.passkey.key.kanban
- Model: `auth.passkey.key`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 3
- Sample fields: `create_date`, `name`, `write_date`
- XPath or positional patches: 0

## Actions

- `action_auth_passkey_key_create`: `act_window` Create Passkey Wizard

## Navigation

- **Parent:** [[docs/Community Addons/auth_passkey/Views]]

<!-- GENERATED:VIEWFILE -->
