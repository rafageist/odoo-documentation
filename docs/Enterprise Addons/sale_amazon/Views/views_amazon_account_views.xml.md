<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/amazon_account_views.xml

- Module: [[docs/Enterprise Addons/sale_amazon/sale_amazon|sale_amazon]]
- Scope: Enterprise Addons
- Source file: `views/amazon_account_views.xml`
- Views: 4
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `amazon_account_view_search`
- Name: amazon.account.search
- Model: `amazon.account`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `active_marketplace_ids`, `name`
- XPath or positional patches: 0

### `quick_create_account_form`
- Name: Quick Create Amazon Account Form
- Model: `amazon.account`
- Type: inferred from arch
- Root tag: `form`
- Field references: 3
- Sample fields: `base_marketplace_id`, `company_id`, `name`
- Buttons: `action_redirect_to_oauth_url`
- XPath or positional patches: 0

### `amazon_account_view_form`
- Name: amazon.account.form
- Model: `amazon.account`
- Type: inferred from arch
- Root tag: `form`
- Field references: 15
- Sample fields: `active`, `active_marketplace_ids`, `base_marketplace_id`, `company_id`, `default_product_ids`, `last_orders_sync`, `location_id`, `name`, `offer_count`, `order_count`, and 5 more
- Buttons: `action_recover_order`, `action_redirect_to_oauth_url`, `action_reset_refresh_token`, `action_sync_feeds_status`, `action_sync_inventory`, `action_sync_orders`, `action_sync_pickings`, `action_update_available_marketplaces`, `action_view_offers`, `action_view_orders`
- XPath or positional patches: 0

### `amazon_account_view_tree`
- Name: amazon.account.list
- Model: `amazon.account`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `active_marketplace_ids`, `company_id`, `last_orders_sync`, `name`, `state`, `team_id`, `user_id`
- Buttons: `%(sale_amazon.quick_create_account_action)d`
- XPath or positional patches: 0

## Actions

- `quick_create_account_action_form`: `view`
- `list_amazon_account_action`: `act_window` Amazon Accounts
- `quick_create_account_action`: `act_window` Amazon Accounts

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_amazon/Views]]

<!-- GENERATED:VIEWFILE -->
