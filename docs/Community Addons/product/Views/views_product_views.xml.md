---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/product/product|product]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 13
- Actions: 6
- Menus: 0
- Rules: 0

## View records

### `product_view_search_catalog`
- Name: product.view.search.catalog
- Model: `product.product`
- Type: inferred from arch
- Root tag: `search`
- Field references: 5
- Sample fields: `categ_id`, `name`, `product_tag_ids`, `product_template_attribute_value_ids`, `product_tmpl_id`
- XPath or positional patches: 0

### `product_view_kanban_catalog`
- Name: product.view.kanban.catalog
- Model: `product.product`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 5
- Sample fields: `id`, `image_128`, `is_favorite`, `name`, `product_template_attribute_value_ids`
- XPath or positional patches: 0

### `product_product_view_activity`
- Name: product.product.activity
- Model: `product.product`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 3
- Sample fields: `default_code`, `id`, `name`
- XPath or positional patches: 0

### `product_kanban_view`
- Name: Product Kanban
- Model: `product.product`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `activity_state`, `color`, `default_code`, `image_128`, `is_favorite`, `lst_price`, `name`, `product_template_variant_value_ids`
- XPath or positional patches: 0

### `product_product_view_form_normalized`
- Name: product.product.view.form.normalized
- Model: `product.product`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `barcode`, `categ_id`, `company_id`, `cost_currency_id`, `currency_id`, `description`, `image_1920`, `list_price`, `name`, `weight`
- XPath or positional patches: 0

### `product_normal_form_view`
- Name: product.product.form
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `xpath`
- Field references: 10
- Sample fields: `additional_product_tag_ids`, `barcode`, `default_code`, `list_price`, `lst_price`, `name`, `product_tag_ids`, `product_template_variant_value_ids`, `product_tmpl_id`, `uom_ids`
- XPath or positional patches: 6

### `product_product_view_tree_tag`
- Name: product.product.view.list.tag
- Model: `product.product`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `default_code`, `description`, `name`, `product_template_variant_value_ids`
- XPath or positional patches: 0

### `product_template_view_tree_tag`
- Name: product.template.view.list.tag
- Model: `product.template`
- Type: inferred from arch
- Root tag: `list`
- Field references: 3
- Sample fields: `default_code`, `description`, `name`
- XPath or positional patches: 0

### `product_product_tree_view`
- Name: product.product.list
- Model: `product.product`
- Type: inferred from arch
- Root tag: `list`
- Field references: 15
- Sample fields: `active`, `additional_product_tag_ids`, `barcode`, `categ_id`, `company_id`, `default_code`, `is_favorite`, `lst_price`, `name`, `product_tag_ids`, and 5 more
- XPath or positional patches: 0

### `product_variant_easy_edit_view`
- Name: product.product.view.form.easy
- Model: `product.product`
- Type: inferred from arch
- Root tag: `form`
- Field references: 21
- Sample fields: `active`, `additional_product_tag_ids`, `barcode`, `company_id`, `cost_currency_id`, `currency_id`, `default_code`, `id`, `image_1920`, `lst_price`, and 11 more
- Buttons: `open_product_template`
- XPath or positional patches: 0

### `product_search_form_view`
- Name: product.product.search
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_template_search_view`
- Root tag: `field`
- Field references: 6
- Sample fields: `all_product_tag_ids`, `attribute_line_ids`, `name`, `product_tag_ids`, `product_template_attribute_value_ids`, `product_tmpl_id`
- XPath or positional patches: 1

### `product_template_search_view`
- Name: product.template.search
- Model: `product.template`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `attribute_line_ids`, `categ_id`, `name`, `product_tag_ids`
- XPath or positional patches: 0

### `product_template_form_view`
- Name: product.template.common.form
- Model: `product.template`
- Type: inferred from arch
- Root tag: `form`
- Field references: 37
- Sample fields: `active`, `attribute_line_ids`, `categ_id`, `combo_ids`, `company_id`, `cost_currency_id`, `currency_id`, `date_end`, `date_start`, `description`, and 27 more
- Buttons: `action_open_documents`
- XPath or positional patches: 0

## Actions

- `action_product_price_list_report`: `server` Pricelist Report
- `action_product_print_labels`: `server` Print Labels
- `product_normal_action_sell`: `act_window` Product Variants
- `product_variant_action`: `act_window` Product Variants
- `product_normal_action`: `act_window` Product Variants
- `product_template_action_all`: `act_window` Products

## Navigation

- **Parent:** [[docs/Community Addons/product/Views]]

