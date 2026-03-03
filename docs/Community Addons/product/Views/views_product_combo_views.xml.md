---
tags: [odoo, community, generated, views]
---

# views/product_combo_views.xml

- Module: [[docs/Community Addons/product/product|product]]
- Scope: Community Addons
- Source file: `views/product_combo_views.xml`
- Views: 2
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `product.product_combo_view_tree`
- Name: product.combo.list
- Model: `product.combo`
- Type: inferred from arch
- Root tag: `list`
- Field references: 5
- Sample fields: `base_price`, `combo_item_count`, `currency_id`, `name`, `sequence`
- XPath or positional patches: 0

### `product.product_combo_view_form`
- Name: product.combo.form
- Model: `product.combo`
- Type: inferred from arch
- Root tag: `form`
- Field references: 7
- Sample fields: `combo_item_ids`, `company_id`, `currency_id`, `extra_price`, `lst_price`, `name`, `product_id`
- XPath or positional patches: 0

## Actions

- `product.product_combo_action`: `act_window` Combo Choices

## Navigation

- **Parent:** [[docs/Community Addons/product/Views]]

