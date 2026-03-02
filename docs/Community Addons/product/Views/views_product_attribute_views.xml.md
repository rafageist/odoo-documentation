<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_attribute_views.xml

- Module: [[docs/Community Addons/product/product|product]]
- Scope: Community Addons
- Source file: `views/product_attribute_views.xml`
- Views: 7
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `product_attribute_search`
- Name: product.attribute.view.search
- Model: `product.attribute`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `product_template_attribute_value_view_search`
- Name: unnamed
- Model: `product.template.attribute.value`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

### `product_template_attribute_value_view_form`
- Name: product.template.attribute.value.view.form.
- Model: `product.template.attribute.value`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `currency_id`, `display_type`, `exclude_for`, `html_color`, `image`, `name`, `price_extra`, `product_tmpl_id`, `ptav_active`, `value_ids`
- XPath or positional patches: 0

### `product_template_attribute_value_view_tree`
- Name: product.template.attribute.value.view.list
- Model: `product.template.attribute.value`
- Type: inferred from arch
- Root tag: `list`
- Field references: 9
- Sample fields: `attribute_id`, `currency_id`, `display_type`, `html_color`, `image`, `name`, `price_extra`, `product_tmpl_id`, `ptav_active`
- XPath or positional patches: 0

### `product_template_attribute_line_form`
- Name: product.template.attribute.line.form
- Model: `product.template.attribute.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 4
- Sample fields: `attribute_id`, `html_color`, `name`, `value_ids`
- XPath or positional patches: 0

### `product_attribute_view_form`
- Name: product.attribute.form
- Model: `product.attribute`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `create_variant`, `default_extra_price`, `display_type`, `html_color`, `image`, `is_custom`, `name`, `number_related_products`, `sequence`, `value_ids`
- Buttons: `action_add_to_products`, `action_open_product_template_attribute_lines`, `action_update_prices`
- XPath or positional patches: 0

### `attribute_tree_view`
- Name: product.attribute.list
- Model: `product.attribute`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `create_variant`, `display_type`, `name`, `sequence`
- XPath or positional patches: 0

## Actions

- `attribute_action`: `act_window` Attributes

## Navigation

- **Parent:** [[docs/Community Addons/product/Views]]

<!-- GENERATED:VIEWFILE -->
