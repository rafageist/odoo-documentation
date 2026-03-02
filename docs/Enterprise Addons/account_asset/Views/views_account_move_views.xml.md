<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/account_move_views.xml

- Module: [[docs/Enterprise Addons/account_asset/account_asset|account_asset]]
- Scope: Enterprise Addons
- Source file: `views/account_move_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_move_line_form_asset_inherit`
- Name: account.move.line.form
- Model: `account.move.line`
- Type: inferred from arch
- Inherits: `account.view_move_line_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `asset_ids`, `move_id`
- XPath or positional patches: 0

### `view_move_form_asset_inherit`
- Name: account.move.form
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_move_form`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `asset_id`, `asset_id_display_name`, `asset_ids`, `asset_move_type`, `count_asset`, `draft_asset_exists`
- Buttons: `action_open_asset_ids`, `open_asset_view`
- XPath or positional patches: 3

## Actions

- `action_account_aml_to_asset`: `server` Create Asset

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_asset/Views]]

<!-- GENERATED:VIEWFILE -->
