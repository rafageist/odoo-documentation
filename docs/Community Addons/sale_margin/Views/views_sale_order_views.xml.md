<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Community Addons/sale_margin/sale_margin|sale_margin]]
- Scope: Community Addons
- Source file: `views/sale_order_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `sale_margin_sale_order_graph`
- Name: sale.order.margin.view.graph
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sale_order_graph`
- Root tag: `graph`
- Field references: 1
- Sample fields: `margin_percent`
- XPath or positional patches: 1

### `sale_margin_sale_order_pivot`
- Name: sale.order.margin.view.pivot
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sale_order_pivot`
- Root tag: `pivot`
- Field references: 1
- Sample fields: `margin_percent`
- XPath or positional patches: 1

### `sale_margin_sale_order`
- Name: sale.order.margin.view.form
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_form`
- Root tag: `field`
- Field references: 5
- Sample fields: `amount_untaxed`, `margin`, `margin_percent`, `purchase_price`, `tax_totals`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/sale_margin/Views]]

<!-- GENERATED:VIEWFILE -->
