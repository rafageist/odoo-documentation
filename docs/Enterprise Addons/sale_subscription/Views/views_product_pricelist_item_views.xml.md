<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/product_pricelist_item_views.xml

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Source file: `views/product_pricelist_item_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `product_pricelist_item_sale_subscription_view`
- Name: product.pricelist.item.sale.subscription.form.inherit
- Model: `product.pricelist.item`
- Type: inferred from arch
- Inherits: `product.product_pricelist_item_product_template_form_view`
- Root tag: `field`
- Field references: 2
- Sample fields: `plan_id`, `pricelist_id`
- XPath or positional patches: 0

### `product_pricelist_item_form_view_recurring`
- Name: sale.subscription.product.pricelist.item.form
- Model: `product.pricelist.item`
- Type: inferred from arch
- Inherits: `product.product_pricelist_item_form_view`
- Root tag: `field`
- Field references: 3
- Sample fields: `min_quantity`, `plan_id`, `product_tmpl_id`
- XPath or positional patches: 0

### `product_pricelist_item_form_view`
- Name: sale.subscription.product.pricelist.item.form
- Model: `product.pricelist.item`
- Type: inferred from arch
- Inherits: `product.product_pricelist_item_form_view`
- Root tag: `field`
- Field references: 1
- Sample fields: `product_tmpl_id`
- XPath or positional patches: 0

### `product_pricelist_item_view_search_inherit`
- Name: product.pricelist.item.search.remove_active_filter
- Model: `product.pricelist.item`
- Type: inferred from arch
- Inherits: `product.product_pricelist_item_view_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Views]]

<!-- GENERATED:VIEWFILE -->
