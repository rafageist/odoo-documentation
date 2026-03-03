---
tags: [odoo, community, generated, views]
---

# views/product_view.xml

- Module: [[docs/Community Addons/point_of_sale/point_of_sale|point_of_sale]]
- Scope: Community Addons
- Source file: `views/product_view.xml`
- Views: 8
- Actions: 5
- Menus: 5
- Rules: 0

## View records

### `product_template_view_form_normalized_pos`
- Name: product.template.view.form.normalized
- Model: `product.template`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `barcode`, `color`, `image_1920`, `is_storable`, `list_price`, `name`, `pos_categ_ids`, `tax_string`, `taxes_id`, `tracking`
- XPath or positional patches: 0

### `product_product_tree_view`
- Name: product.product.product.list.inherit
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_product_tree_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `categ_id`, `pos_categ_ids`
- XPath or positional patches: 0

### `product_template_tree_view_point_of_sale`
- Name: product.template.view.list.point_of_sale
- Model: `product.template`
- Type: inferred from arch
- Inherits: `point_of_sale.product_template_tree_view`
- Root tag: `list`
- Field references: 2
- Sample fields: `is_favorite`, `pos_sequence`
- XPath or positional patches: 1

### `product_template_tree_view`
- Name: product.template.product.list.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_tree_view`
- Root tag: `field`
- Field references: 3
- Sample fields: `available_in_pos`, `categ_id`, `pos_categ_ids`
- XPath or positional patches: 0

### `product_uom_form_view_inherit`
- Name: product.uom.form.view.inherit
- Model: `uom.uom`
- Type: inferred from arch
- Inherits: `uom.product_uom_form_view`
- Root tag: `div`
- Field references: 1
- Sample fields: `is_pos_groupable`
- XPath or positional patches: 1

### `product_template_only_form_view`
- Name: product.template.product.form.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_only_form_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `product_template_form_view`
- Name: product.template.form.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `available_in_pos`, `color`, `pos_categ_ids`, `pos_optional_product_ids`, `public_description`, `to_weight`
- XPath or positional patches: 3

### `product_template_search_view_pos`
- Name: product.template.search.pos.form
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_search_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `categ_id`, `pos_categ_ids`
- XPath or positional patches: 2

## Actions

- `product_template_action_edit_pos`: `act_window` Edit Product
- `product_template_action_add_pos`: `act_window` New Product
- `product_category_action`: `act_window` Internal Categories
- `product_product_action`: `act_window` Product Variants
- `product_template_action_pos_product`: `act_window` Products

## Menus

- `pos_config_menu_action_product_pricelist`: unnamed
- `point_of_sale.menu_product_combo`: Combo Choices
- `pos_config_menu_action_product_product`: Product Variants
- `menu_pos_products`: unnamed
- `pos_config_menu_catalog`: Products

## Navigation

- **Parent:** [[docs/Community Addons/point_of_sale/Views]]

