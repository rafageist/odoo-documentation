<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/website_sale/website_sale|website_sale]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 9
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `product_product_view_form_easy_inherit_website_sale`
- Name: product.product.view.form.easy.inherit.website_sale
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_variant_easy_edit_view`
- Root tag: `group`
- Field references: 7
- Sample fields: `base_unit_count`, `base_unit_id`, `base_unit_name`, `base_unit_price`, `product_variant_image_ids`, `variant_ribbon_id`, `website_ribbon_id`
- XPath or positional patches: 3

### `product_template_form_view`
- Name: product.template.product.website.form
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `span`
- Field references: 9
- Sample fields: `accessory_product_ids`, `alternative_product_ids`, `description_ecommerce`, `is_published`, `product_template_image_ids`, `public_categ_ids`, `website_id`, `website_ribbon_id`, `website_sequence`
- XPath or positional patches: 8

### `product_product_normal_website_form_view`
- Name: product.product.normal.view.website
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_normal_form_view`
- Root tag: `field`
- Field references: 5
- Sample fields: `base_unit_count`, `base_unit_id`, `base_unit_name`, `base_unit_price`, `categ_id`
- XPath or positional patches: 0

### `product_template_only_website_form_view`
- Name: product.template.product.only.website.form
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_only_form_view`
- Root tag: `field`
- Field references: 6
- Sample fields: `base_unit_count`, `base_unit_id`, `base_unit_name`, `base_unit_price`, `categ_id`, `compare_list_price`
- XPath or positional patches: 0

### `product_template_view_kanban_website_sale`
- Name: product.template.view.kanban.website_sale
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_kanban_view`
- Root tag: `kanban`
- Field references: 0
- XPath or positional patches: 1

### `product_template_view_tree_website_sale`
- Name: product.template.view.list.website_sale
- Model: `product.template`
- Type: inferred from arch
- Inherits: `website_sale.product_template_view_tree`
- Root tag: `list`
- Field references: 5
- Sample fields: `is_favorite`, `is_published`, `public_categ_ids`, `website_id`, `website_sequence`
- XPath or positional patches: 1

### `product_template_view_tree`
- Name: product.template.view.list.inherit.website_sale
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_tree_view`
- Root tag: `field`
- Field references: 4
- Sample fields: `default_code`, `product_tag_ids`, `website_id`, `website_ribbon_id`
- XPath or positional patches: 0

### `product_product_website_tree_view`
- Name: product.product.website.list
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_product_tree_view`
- Root tag: `field`
- Field references: 6
- Sample fields: `additional_product_tag_ids`, `is_published`, `name`, `variant_ribbon_id`, `website_id`, `website_ribbon_id`
- XPath or positional patches: 0

### `product_template_search_view_website`
- Name: product.template.search.published
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_search_view`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 2

## Actions

- `product_template_action_website`: `act_window` Products

## Navigation

- **Parent:** [[docs/Community Addons/website_sale/Views]]

<!-- GENERATED:VIEWFILE -->
