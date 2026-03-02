<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/product_template_views.xml

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Source file: `views/product_template_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `product_template_kanban_view_inherit_sale_subscription`
- Name: product.template.kanban.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_kanban_view`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `display_subscription_pricing`, `list_price`
- XPath or positional patches: 1

### `product_template_only_view_form_recurring`
- Name: sale.subscription.product.template.only.form.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `page`
- Field references: 12
- Sample fields: `allow_one_time_sale`, `allow_prorated_price`, `company_id`, `date_end`, `date_start`, `fixed_price`, `min_quantity`, `plan_id`, `pricelist_id`, `product_id`, and 2 more
- XPath or positional patches: 2

### `product_template_view_form_recurring`
- Name: sale.subscription.product.template.form.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `sale.product_template_form_view`
- Root tag: `page`
- Field references: 1
- Sample fields: `recurring_invoice`
- XPath or positional patches: 2

### `product_template_search_view_inherit_sale_subscription`
- Name: product.template.search.inherit
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_search_view`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `product_action_subscription`: `act_window` Products

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Views]]

<!-- GENERATED:VIEWFILE -->
