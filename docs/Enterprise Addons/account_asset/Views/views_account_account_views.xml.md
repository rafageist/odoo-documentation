<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_account_views.xml

- Module: [[docs/Enterprise Addons/account_asset/account_asset|account_asset]]
- Scope: Enterprise Addons
- Source file: `views/account_account_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_form_asset_inherit`
- Name: account.account.form
- Model: `account.account`
- Type: inferred from arch
- Inherits: `account.view_account_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `asset_model_ids`, `can_create_asset`, `create_asset`, `form_view_ref`, `multiple_assets_per_line`
- XPath or positional patches: 1

### `view_move_line_tree`
- Name: account.move.line.list
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account_accountant.view_move_line_tree`
- Root tag: `xpath`
- Field references: 0
- Buttons: `turn_as_asset`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_asset/Views]]

<!-- GENERATED:VIEWFILE -->
