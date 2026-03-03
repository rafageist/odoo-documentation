---
tags: [odoo, community, generated, views]
---

# views/product_pricelist_item_views.xml

- Module: [[docs/Community Addons/product/product|product]]
- Scope: Community Addons
- Source file: `views/product_pricelist_item_views.xml`
- Views: 6
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_pricelist_item_product_product_form_view`
- Name: product.pricelist.item.product.product.form.inherit
- Model: `product.pricelist.item`
- Type: inferred from arch
- Inherits: `product.product_pricelist_item_product_template_form_view`
- Root tag: `field`
- Field references: 1
- Sample fields: `product_id`
- XPath or positional patches: 0

### `product_pricelist_item_product_template_form_view`
- Name: product.pricelist.item.product.template.form.inherit
- Model: `product.pricelist.item`
- Type: inferred from arch
- Inherits: `product.product_pricelist_item_form_view`
- Root tag: `field`
- Field references: 4
- Sample fields: `date_start`, `display_applied_on`, `pricelist_id`, `product_tmpl_id`
- XPath or positional patches: 0

### `product_pricelist_item_form_view`
- Name: product.pricelist.item.form
- Model: `product.pricelist.item`
- Type: inferred from arch
- Root tag: `form`
- Field references: 27
- Sample fields: `applied_on`, `base`, `base_pricelist_id`, `categ_id`, `company_id`, `compute_price`, `currency_id`, `date_end`, `date_start`, `display_applied_on`, and 17 more
- XPath or positional patches: 0

### `product_pricelist_item_tree_view_from_product`
- Name: product.pricelist.item.list
- Model: `product.pricelist.item`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `applied_on`, `categ_id`, `company_id`, `currency_id`, `date_end`, `date_start`, `fixed_price`, `min_quantity`, `pricelist_id`, `product_id`, and 1 more
- XPath or positional patches: 0

### `product_pricelist_item_tree_view`
- Name: product.pricelist.item.list
- Model: `product.pricelist.item`
- Type: inferred from arch
- Root tag: `list`
- Field references: 7
- Sample fields: `company_id`, `date_end`, `date_start`, `min_quantity`, `name`, `price`, `pricelist_id`
- XPath or positional patches: 0

### `product_pricelist_item_view_search`
- Name: product.pricelist.item.search
- Model: `product.pricelist.item`
- Type: inferred from arch
- Root tag: `search`
- Field references: 3
- Sample fields: `company_id`, `currency_id`, `pricelist_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/product/Views]]

