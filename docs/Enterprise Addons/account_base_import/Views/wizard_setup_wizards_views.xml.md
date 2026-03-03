---
tags: [odoo, enterprise, generated, views]
---

# wizard/setup_wizards_views.xml

- Module: [[docs/Enterprise Addons/account_base_import/account_base_import|account_base_import]]
- Scope: Enterprise Addons
- Source file: `wizard/setup_wizards_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_setup_base_import_list`
- Name: account.setup.opening.account.account.list.account.base.import
- Model: `account.account`
- Type: inferred from arch
- Inherits: `account.init_accounts_tree`
- Root tag: `xpath`
- Field references: 0
- Buttons: `%(account_base_import.action_open_import_guide)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_base_import/Views]]

