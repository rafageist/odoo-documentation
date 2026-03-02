<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_pricelist_views.xml

- Module: [[docs/Community Addons/product/product|product]]
- Scope: Community Addons
- Source file: `views/product_pricelist_views.xml`
- Views: 4
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `product_pricelist_view`
- Name: product.pricelist.form
- Model: `product.pricelist`
- Type: inferred from arch
- Root tag: `form`
- Field references: 15
- Sample fields: `active`, `applied_on`, `base`, `company_id`, `compute_price`, `country_group_ids`, `currency_id`, `date_end`, `date_start`, `item_ids`, and 5 more
- Buttons: `action_open_pricelist_report`
- XPath or positional patches: 0

### `product_pricelist_view_kanban`
- Name: product.pricelist.kanban
- Model: `product.pricelist`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 2
- Sample fields: `currency_id`, `name`
- XPath or positional patches: 0

### `product_pricelist_view_tree`
- Name: product.pricelist.list
- Model: `product.pricelist`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `company_id`, `country_group_ids`, `currency_id`, `name`, `sequence`
- XPath or positional patches: 0

### `product_pricelist_view_search`
- Name: product.pricelist.search
- Model: `product.pricelist`
- Type: inferred from arch
- Root tag: `search`
- Field references: 2
- Sample fields: `currency_id`, `name`
- XPath or positional patches: 0

## Actions

- `product_pricelist_item_action`: `act_window` Price Rules
- `product_pricelist_action2`: `act_window` Pricelists

## Navigation

- **Parent:** [[docs/Community Addons/product/Views]]

<!-- GENERATED:VIEWFILE -->
