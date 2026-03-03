---
tags: [odoo, enterprise, generated, views]
---

# views/shopee_item_views.xml

- Module: [[docs/Enterprise Addons/sale_shopee/sale_shopee|sale_shopee]]
- Scope: Enterprise Addons
- Source file: `views/shopee_item_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `shopee_item_view_search`
- Name: shopee.item.search
- Model: `shopee.item`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `product_id`, `shop_id`
- XPath or positional patches: 0

### `shopee_item_view_list`
- Name: shopee.item.list
- Model: `shopee.item`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `last_inventory_sync_date`, `product_id`, `shop_id`, `shopee_item_identifier`, `shopee_model_identifier`, `sync_to_shopee`
- XPath or positional patches: 0

## Actions

- `sale_shopee_item_action`: `act_window` Shopee Items

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_shopee/Views]]

