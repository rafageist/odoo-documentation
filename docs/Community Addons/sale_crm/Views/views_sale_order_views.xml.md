---
tags: [odoo, community, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Community Addons/sale_crm/sale_crm|sale_crm]]
- Scope: Community Addons
- Source file: `views/sale_order_views.xml`
- Views: 1
- Actions: 1
- Menus: 1
- Rules: 0

## View records

### `sale_view_inherit123`
- Name: sale.order.form.inherit.sale
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `opportunity_id`, `origin`
- XPath or positional patches: 0

## Actions

- `sale_action_quotations_new`: `act_window` Quotation

## Menus

- `sale_order_menu_quotations_crm`: My Quotations

## Navigation

- **Parent:** [[docs/Community Addons/sale_crm/Views]]

