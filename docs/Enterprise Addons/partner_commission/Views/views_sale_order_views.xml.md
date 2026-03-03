---
tags: [odoo, enterprise, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Enterprise Addons/partner_commission/partner_commission|partner_commission]]
- Scope: Enterprise Addons
- Source file: `views/sale_order_views.xml`
- Views: 5
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `sale_order_form_quote_inherit_partner_commission`
- Name: sale.order.form.quote.partner.commission
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale_management.sale_order_form_quote`
- Root tag: `field`
- Field references: 6
- Sample fields: `commission`, `commission_plan_frozen`, `commission_plan_id`, `partner_id`, `referrer_id`, `tax_totals`
- XPath or positional patches: 0

### `account_move_view_search_inherit_partner_commission`
- Name: account.move.search.inherit.partner_commission
- Model: `account.move`
- Type: inferred from arch
- Inherits: `account.view_account_invoice_filter`
- Root tag: `group`
- Field references: 0
- XPath or positional patches: 1

### `sale_order_view_search_inherit_partner_commission`
- Name: sale.order.search.inherit.partner.commission
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sales_order_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `order_line`, `referrer_id`
- XPath or positional patches: 1

### `sale_order_subscription_view_tree_inherit_partner_commission`
- Name: sale.order.subscription.list.inherit.partner.commission
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale_subscription.sale_subscription_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `partner_id`, `referrer_id`
- XPath or positional patches: 0

### `sale_order_subsciption_view_search_inherit_partner_commission`
- Name: sale.order.subscription.search.inherit.partner.commission
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale_subscription.sale_subscription_view_search`
- Root tag: `field`
- Field references: 2
- Sample fields: `order_line`, `referrer_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/partner_commission/Views]]

