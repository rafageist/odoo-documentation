<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_strategy_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `views/product_strategy_views.xml`
- Views: 3
- Actions: 3
- Menus: 1
- Rules: 0

## View records

### `view_putaway_search`
- Name: stock.putaway.rule.search
- Model: `stock.putaway.rule`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `category_id`, `location_in_id`, `location_out_id`, `product_id`
- XPath or positional patches: 0

### `view_removal`
- Name: product.removal.form
- Model: `product.removal`
- Type: inferred from arch
- Root tag: `form`
- Field references: 2
- Sample fields: `method`, `name`
- XPath or positional patches: 0

### `stock_putaway_list`
- Name: stock.putaway.rule.list
- Model: `stock.putaway.rule`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `category_id`, `company_id`, `location_in_id`, `location_out_id`, `package_type_ids`, `product_id`, `sequence`, `storage_category_id`, `sublocation`
- XPath or positional patches: 0

## Actions

- `location_open_putaway`: `act_window` Putaway Rules
- `category_open_putaway`: `act_window` Putaway Rules
- `action_putaway_tree`: `act_window` Putaway Rules

## Menus

- `menu_putaway`: Putaway Rules

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

<!-- GENERATED:VIEWFILE -->
