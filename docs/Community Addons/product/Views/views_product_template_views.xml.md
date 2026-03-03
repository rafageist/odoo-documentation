---
tags: [odoo, community, generated, views]
---

# views/product_template_views.xml

- Module: [[docs/Community Addons/product/product|product]]
- Scope: Community Addons
- Source file: `views/product_template_views.xml`
- Views: 6
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `product_template_view_activity`
- Name: product.template.activity
- Model: `product.template`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 3
- Sample fields: `default_code`, `id`, `name`
- XPath or positional patches: 0

### `product_template_kanban_view`
- Name: Product.template.product.kanban
- Model: `product.template`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 10
- Sample fields: `activity_state`, `categ_id`, `currency_id`, `default_code`, `image_128`, `is_favorite`, `list_price`, `name`, `product_properties`, `product_variant_count`
- XPath or positional patches: 0

### `product_template_only_form_view`
- Name: product.template.product.form
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `xpath`
- Field references: 11
- Sample fields: `attribute_id`, `attribute_line_ids`, `barcode`, `categ_id`, `default_code`, `product_properties`, `product_variant_count`, `sequence`, `valid_product_template_attribute_line_ids`, `value_count`, and 1 more
- Buttons: `%(product.product_variant_action)d`, `action_open_attribute_values`, `action_open_documents`
- XPath or positional patches: 3

### `product_template_list_view_purchasable`
- Name: product.template.list.purchasable
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_tree_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `product_template_list_view_sellable`
- Name: product.template.list.sellable
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_tree_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `product_template_tree_view`
- Name: product.template.product.list
- Model: `product.template`
- Type: inferred from arch
- Root tag: `list`
- Field references: 17
- Sample fields: `active`, `activity_exception_decoration`, `barcode`, `categ_id`, `company_id`, `cost_currency_id`, `currency_id`, `default_code`, `is_favorite`, `list_price`, and 7 more
- XPath or positional patches: 0

## Actions

- `action_product_template_price_list_report`: `server` Pricelist Report
- `action_product_template_print_labels`: `server` Print Labels
- `product_template_action`: `act_window` Products

## Navigation

- **Parent:** [[docs/Community Addons/product/Views]]

