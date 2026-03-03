---
tags: [odoo, community, generated, views]
---

# wizard/sale_make_invoice_advance_views.xml

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `wizard/sale_make_invoice_advance_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_sale_advance_payment_inv`
- Name: Invoice Orders
- Model: `sale.advance.payment.inv`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `advance_payment_method`, `amount`, `amount_invoiced`, `company_id`, `consolidated_billing`, `count`, `currency_id`, `display_draft_invoice_warning`, `fixed_amount`, `has_down_payments`, and 1 more
- Buttons: `create_invoices`
- XPath or positional patches: 0

## Actions

- `action_view_sale_advance_payment_inv`: `act_window` Create invoice(s)

## Navigation

- **Parent:** [[docs/Community Addons/sale/Views]]

