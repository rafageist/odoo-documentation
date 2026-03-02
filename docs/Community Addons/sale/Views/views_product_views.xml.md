<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/product_views.xml

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `views/product_views.xml`
- Views: 5
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `product_view_search_catalog`
- Name: product.view.search.catalog.inherit.sale
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_view_search_catalog`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `product_view_kanban_catalog`
- Name: product.view.kanban.catalog.inherit.sale
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_view_kanban_catalog`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `product_template_form_view_sale_order_button`
- Name: product.template.sale.order.button
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_only_form_view`
- Root tag: `button`
- Field references: 2
- Sample fields: `sales_count`, `uom_name`
- Buttons: `action_open_documents`, `action_view_sales`
- XPath or positional patches: 0

### `product_form_view_sale_order_button`
- Name: product.product.sale.order
- Model: `product.product`
- Type: inferred from arch
- Inherits: `product.product_normal_form_view`
- Root tag: `div`
- Field references: 2
- Sample fields: `sales_count`, `uom_name`
- Buttons: `action_view_sales`
- XPath or positional patches: 1

### `product_template_form_view`
- Name: product.template.form.view.inherit.sale
- Model: `product.template`
- Type: inferred from arch
- Inherits: `product.product_template_form_view`
- Root tag: `page`
- Field references: 8
- Sample fields: `expense_policy`, `invoice_policy`, `product_variant_count`, `sale_line_warn_msg`, `service_tracking`, `service_type`, `type`, `visible_expense_policy`
- XPath or positional patches: 2

## Actions

- `product_template_action`: `act_window` Products

## Navigation

- **Parent:** [[docs/Community Addons/sale/Views]]

<!-- GENERATED:VIEWFILE -->
