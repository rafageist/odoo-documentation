---
tags: [odoo, enterprise, generated, views]
---

# views/sale_order_line_views.xml

- Module: [[docs/Enterprise Addons/sale_account_accountant/sale_account_accountant|sale_account_accountant]]
- Scope: Enterprise Addons
- Source file: `views/sale_order_line_views.xml`
- Views: 2
- Actions: 2
- Menus: 3
- Rules: 0

## View records

### `sale_order_line_view_list`
- Name: sale.order.line.view.list
- Model: `sale.order.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 11
- Sample fields: `amount_to_invoice_at_date`, `currency_id`, `name`, `order_id`, `order_partner_id`, `price_unit`, `product_uom_id`, `product_uom_qty`, `qty_delivered_at_date`, `qty_invoiced_at_date`, and 1 more
- Buttons: `%(sale.action_accrued_revenue_entry_sale_order_line)d`
- XPath or positional patches: 0

### `sale_order_line_view_search`
- Name: sale.order.line.view.search
- Model: `sale.order.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 0

## Actions

- `sale_order_line_accrual_deferred_revenues_action`: `act_window` Invoiced Not Delivered
- `sale_order_line_accrual_to_bill_action`: `act_window` Invoices To Be Issued

## Menus

- `sale_accountant_accrual_menu`: Sales
- `menu_sale_order_line_accrual_deferred_revenues_action`: Invoiced Not Delivered
- `menu_sale_order_line_accrual_to_bill_action`: Invoices To Be Issued

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_account_accountant/Views]]

