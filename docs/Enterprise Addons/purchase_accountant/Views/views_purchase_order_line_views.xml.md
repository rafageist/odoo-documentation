---
tags: [odoo, enterprise, generated, views]
---

# views/purchase_order_line_views.xml

- Module: [[docs/Enterprise Addons/purchase_accountant/purchase_accountant|purchase_accountant]]
- Scope: Enterprise Addons
- Source file: `views/purchase_order_line_views.xml`
- Views: 2
- Actions: 2
- Menus: 3
- Rules: 0

## View records

### `purchase_order_line_view_list`
- Name: purchase.order.line.view.list
- Model: `purchase.order.line`
- Type: inferred from arch
- Root tag: `list`
- Field references: 10
- Sample fields: `amount_to_invoice_at_date`, `currency_id`, `order_id`, `partner_id`, `price_unit`, `product_id`, `product_qty`, `product_uom_id`, `qty_invoiced_at_date`, `qty_received_at_date`
- Buttons: `%(purchase.action_accrued_expense_entry)d`
- XPath or positional patches: 0

### `purchase_order_line_view_search`
- Name: purchase.order.line.view.search
- Model: `purchase.order.line`
- Type: inferred from arch
- Root tag: `search`
- Field references: 0
- XPath or positional patches: 0

## Actions

- `purchase_order_line_accrual_prepaid_expenses_action`: `act_window` Billed Not Received
- `purchase_order_line_accrual_bill_to_receive_action`: `act_window` Bill To Receive

## Menus

- `purchase_accountant_accrual_menu`: Purchases
- `menu_purchase_order_line_accrual_prepaid_expenses_action`: Billed Not Received
- `menu_purchase_order_line_accrual_bill_to_receives_action`: Bill To Receive

## Navigation

- **Parent:** [[docs/Enterprise Addons/purchase_accountant/Views]]

