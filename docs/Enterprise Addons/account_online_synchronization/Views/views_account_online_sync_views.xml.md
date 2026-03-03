---
tags: [odoo, enterprise, generated, views]
---

# views/account_online_sync_views.xml

- Module: [[docs/Enterprise Addons/account_online_synchronization/account_online_synchronization|account_online_synchronization]]
- Scope: Enterprise Addons
- Source file: `views/account_online_sync_views.xml`
- Views: 3
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `account_online_link_view_tree`
- Name: account.online.link.list
- Model: `account.online.link`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `company_id`, `last_refresh`, `name`, `next_refresh`, `provider_type`, `state`
- XPath or positional patches: 0

### `account_online_account_view_form`
- Name: account.online.account.form
- Model: `account.online.account`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `account_number`, `available_balance`, `balance`, `company_id`, `journal_ids`, `last_sync`, `name`
- XPath or positional patches: 0

### `account_online_link_view_form`
- Name: account.online.link.form
- Model: `account.online.link`
- Type: inferred from arch
- Root tag: `form`
- Field references: 18
- Sample fields: `account_number`, `account_online_account_ids`, `auto_sync`, `available_balance`, `balance`, `client_id`, `company_id`, `expiring_synchronization_date`, `inverse_balance_sign`, `inverse_transaction_sign`, and 8 more
- Buttons: `action_fetch_transactions`, `action_new_synchronization`, `action_reconnect_account`, `action_reset_fetching_status`, `action_update_credentials`
- XPath or positional patches: 0

## Actions

- `action_account_online_link_form`: `act_window` Online Synchronization

## Menus

- `menu_action_online_link_account`: Online Synchronization

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_online_synchronization/Views]]

