---
tags: [odoo, enterprise, generated, views]
---

# views/account_account_views.xml

- Module: [[docs/Enterprise Addons/account_fiscal_categories/account_fiscal_categories|account_fiscal_categories]]
- Scope: Enterprise Addons
- Source file: `views/account_account_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_account_search`
- Name: account.account.search
- Model: `account.account`
- Type: inferred from arch
- Inherits: `account.view_account_search`
- Root tag: `field`
- Field references: 2
- Sample fields: `fiscal_category_id`, `name`
- XPath or positional patches: 0

### `view_account_list`
- Name: account.account.list
- Model: `account.account`
- Type: inferred from arch
- Inherits: `account.view_account_list`
- Root tag: `field`
- Field references: 3
- Sample fields: `company_ids`, `current_rate`, `fiscal_category_id`
- XPath or positional patches: 0

### `view_account_form`
- Name: account.account.form
- Model: `account.account`
- Type: inferred from arch
- Inherits: `account.view_account_form`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `company_id`, `date_from`, `fiscal_category_id`, `rate`, `rate_ids`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_fiscal_categories/Views]]

