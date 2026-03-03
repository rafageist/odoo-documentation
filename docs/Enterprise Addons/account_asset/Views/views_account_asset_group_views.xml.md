---
tags: [odoo, enterprise, generated, views]
---

# views/account_asset_group_views.xml

- Module: [[docs/Enterprise Addons/account_asset/account_asset|account_asset]]
- Scope: Enterprise Addons
- Source file: `views/account_asset_group_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `asset_group_list_view`
- Name: account.asset.group.list
- Model: `account.asset.group`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `company_id`, `name`
- XPath or positional patches: 0

### `asset_group_form_view`
- Name: account.asset.group.form
- Model: `account.asset.group`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `company_id`, `count_linked_assets`, `name`
- Buttons: `action_open_linked_assets`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_asset/Views]]

