---
tags: [odoo, enterprise, generated, views]
---

# views/account_account_views.xml

- Module: [[docs/Enterprise Addons/account_base_import/account_base_import|account_base_import]]
- Scope: Enterprise Addons
- Source file: `views/account_account_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_account_base_import_list`
- Name: account.base.import.account.account.list
- Model: `account.account`
- Type: inferred from arch
- Inherits: `account.view_account_list`
- Root tag: `xpath`
- Field references: 0
- Buttons: `%(account_base_import.action_open_import_guide)d`
- XPath or positional patches: 1

## Actions

- `action_account_import`: `client` Import Chart of Accounts

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_base_import/Views]]

