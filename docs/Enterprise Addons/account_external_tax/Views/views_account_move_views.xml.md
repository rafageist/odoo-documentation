---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Enterprise Addons/account_external_tax/account_external_tax|account_external_tax]]
- Scope: Enterprise Addons
- Source file: `views/account_move_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `move_form_inherit`
- Name: account.move.form.inherit
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `button`
- Field references: 1
- Sample fields: `is_tax_computed_externally`
- Buttons: `button_draft`, `button_external_tax_calculation`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_external_tax/Views]]

