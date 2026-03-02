<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/shopee_account_views.xml

- Module: [[docs/Enterprise Addons/sale_shopee/sale_shopee|sale_shopee]]
- Scope: Enterprise Addons
- Source file: `views/shopee_account_views.xml`
- Views: 3
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `quick_create_account_form`
- Name: Quick Create Shopee Account Form
- Model: `shopee.account`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `api_endpoint`, `partner_identifier`, `partner_key`
- Buttons: `action_open_auth_link`
- XPath or positional patches: 0

### `shopee_account_view_form`
- Name: shopee.account.form
- Model: `shopee.account`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `api_endpoint`, `company_ids`, `name`, `partner_identifier`, `partner_key`, `shop_count`
- Buttons: `action_open_auth_link`, `action_view_shops`
- XPath or positional patches: 0

### `shopee_account_view_list`
- Name: shopee.account.list
- Model: `shopee.account`
- Type: inferred from arch
- Root tag: `list`
- Field references: 2
- Sample fields: `api_endpoint`, `name`
- Buttons: `%(sale_shopee.quick_create_account_action)d`
- XPath or positional patches: 0

## Actions

- `quick_create_account_action_form`: `view`
- `action_shopee_account_list`: `act_window` Shopee Accounts
- `quick_create_account_action`: `act_window` Create Shopee Accounts

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_shopee/Views]]

<!-- GENERATED:VIEWFILE -->
