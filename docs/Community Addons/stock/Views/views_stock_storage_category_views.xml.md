---
tags: [odoo, community, generated, views]
---

# views/stock_storage_category_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/stock_storage_category_views.xml`
- Views: 3
- Actions: 2
- Menus: 1
- Rules: 0

## View records

### `stock_storage_category_capacity_tree`
- Name: stock.storage.category.capacity.list
- Model: `stock.storage.category.capacity`
- Type: inferred from arch
- Root tag: `list`
- Field references: 6
- Sample fields: `company_id`, `package_type_id`, `product_id`, `product_uom_id`, `quantity`, `storage_category_id`
- XPath or positional patches: 0

### `stock_storage_category_tree`
- Name: stock.storage.category.list
- Model: `stock.storage.category`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `allow_new_product`, `company_id`, `max_weight`, `name`
- XPath or positional patches: 0

### `stock_storage_category_form`
- Name: stock.storage.category.form
- Model: `stock.storage.category`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `allow_new_product`, `company_id`, `max_weight`, `name`, `package_capacity_ids`, `package_type_id`, `product_capacity_ids`, `product_id`, `product_uom_id`, `quantity`, and 1 more
- Buttons: `%(action_storage_category_locations)d`
- XPath or positional patches: 0

## Actions

- `action_storage_category_capacity`: `act_window` Storage Category Capacity
- `action_storage_category`: `act_window` Storage Categories

## Menus

- `menu_storage_categoty_config`: Storage Categories

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

