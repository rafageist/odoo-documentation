---
tags: [odoo, enterprise, generated, views]
---

# views/amazon_offer_views.xml

- Module: [[docs/Enterprise Addons/sale_amazon/sale_amazon|sale_amazon]]
- Scope: Enterprise Addons
- Source file: `views/amazon_offer_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `amazon_offer_view_search`
- Name: amazon.offer.search
- Model: `amazon.offer`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `marketplace_id`, `product_id`
- XPath or positional patches: 0

### `amazon_offer_view_tree`
- Name: amazon.offer.list
- Model: `amazon.offer`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `account_id`, `active_marketplace_ids`, `amazon_channel`, `amazon_feed_ref`, `amazon_sync_status`, `marketplace_id`, `product_id`, `sku`, `sync_stock`
- Buttons: `action_view_online`
- XPath or positional patches: 0

## Actions

- `amazon_offer_action`: `act_window` Offers

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_amazon/Views]]

