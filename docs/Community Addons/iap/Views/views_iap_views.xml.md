<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/iap_views.xml

- Module: [[docs/Community Addons/iap/iap|iap]]
- Scope: Community Addons
- Source file: `views/iap_views.xml`
- Views: 2
- Actions: 1
- Menus: 2
- Rules: 0

## View records

### `iap_account_view_tree`
- Name: iap.account.list
- Model: `iap.account`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `account_token`, `balance`, `company_ids`, `description`, `name`, `service_id`, `warning_threshold`
- XPath or positional patches: 0

### `iap_account_view_form`
- Name: iap.account.form
- Model: `iap.account`
- Type: inferred from arch
- Root tag: `form`
- Field references: 8
- Sample fields: `account_token`, `balance`, `company_ids`, `description`, `name`, `service_id`, `warning_threshold`, `warning_user_ids`
- Buttons: `action_buy_credits`
- XPath or positional patches: 0

## Actions

- `iap_account_action`: `act_window` IAP Account

## Menus

- `iap_account_menu`: IAP Accounts
- `iap_root_menu`: IAP

## Navigation

- **Parent:** [[docs/Community Addons/iap/Views]]

<!-- GENERATED:VIEWFILE -->
