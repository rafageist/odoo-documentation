---
tags: [odoo, enterprise, generated, views]
---

# views/shopee_shop_views.xml

- Module: [[docs/Enterprise Addons/sale_shopee/sale_shopee|sale_shopee]]
- Scope: Enterprise Addons
- Source file: `views/shopee_shop_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `shopee_shop_view_search`
- Name: shopee.shop.search
- Model: `shopee.shop`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `shopee_shop_view_form`
- Name: shopee.shop.form
- Model: `shopee.shop`
- Type: inferred from arch
- Root tag: `form`
- Field references: 17
- Sample fields: `access_token`, `access_token_expiration_date`, `account_id`, `authorization_expiration_date`, `authorization_remaining_days`, `company_id`, `fbs_location_id`, `last_orders_sync_date`, `last_shop_status_sync_date`, `name`, and 7 more
- Buttons: `action_force_update_shop`, `action_sync_inventory`, `action_sync_orders`, `action_sync_pickings`, `action_view_orders`, `action_view_shopee_items`
- XPath or positional patches: 0

### `shopee_shop_view_list`
- Name: shopee.shop.list
- Model: `shopee.shop`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `account_id`, `company_id`, `last_orders_sync_date`, `name`, `shop_identifier`, `status`, `user_id`
- XPath or positional patches: 0

## Actions

- `action_shopee_shop_list`: `act_window` Shopee Shops

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_shopee/Views]]

