<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/sale_order_template_views.xml

- Module: [[docs/Enterprise Addons/sale_subscription/sale_subscription|sale_subscription]]
- Scope: Enterprise Addons
- Source file: `views/sale_order_template_views.xml`
- Views: 3
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `sale_subscription_template_view_form`
- Name: sale.order.template.form
- Model: `sale.order.template`
- Type: inferred from arch
- Inherits: `sale_management.sale_order_template_view_form`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `company_id`, `duration_unit`, `duration_value`, `is_subscription`, `is_unlimited`, `plan_id`, `recurring_invoice`
- XPath or positional patches: 3

### `sale_order_template_view_tree`
- Name: sale.order.template.list
- Model: `sale.order.template`
- Type: inferred from arch
- Inherits: `sale_management.sale_order_template_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `name`, `plan_id`
- XPath or positional patches: 0

### `sale_order_template_view_search`
- Name: sale.order.template.search
- Model: `sale.order.template`
- Type: inferred from arch
- Root tag: `search`
- Field references: 1
- Sample fields: `name`
- XPath or positional patches: 0

## Actions

- `sale_subscription_template_form`: `view`
- `sale_subscription_template_tree`: `view`
- `sale_subscription_template_action`: `act_window` Quotation Templates

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_subscription/Views]]

<!-- GENERATED:VIEWFILE -->
