---
tags: [odoo, enterprise, generated, views]
---

# views/purchase_order_views.xml

- Module: [[docs/Enterprise Addons/partner_commission/partner_commission|partner_commission]]
- Scope: Enterprise Addons
- Source file: `views/purchase_order_views.xml`
- Views: 1
- Actions: 3
- Menus: 0
- Rules: 0

## View records

### `purchase_order_form_inherit_partner_commission`
- Name: purchase.order.form.partner.commission
- Model: `purchase.order`
- Type: inferred from arch
- Inherits: `purchase.purchase_order_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `invoice_commission_count`, `purchase_type`
- Buttons: `action_view_customer_invoices`
- XPath or positional patches: 2

## Actions

- `action_account_customer_invoice_form`: `view`
- `action_account_customer_invoice_tree`: `view`
- `action_view_customer_invoices`: `act_window` Customer Invoices

## Navigation

- **Parent:** [[docs/Enterprise Addons/partner_commission/Views]]

