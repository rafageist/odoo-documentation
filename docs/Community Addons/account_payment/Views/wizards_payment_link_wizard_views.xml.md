<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# wizards/payment_link_wizard_views.xml

- Module: [[docs/Community Addons/account_payment/account_payment|account_payment]]
- Scope: Community Addons
- Source file: `wizards/payment_link_wizard_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `payment_link_wizard__form_inherit_account_payment`
- Name: payment.link.wizard.form.inherit.account_payment
- Model: `payment.link.wizard`
- Type: inferred from arch
- Inherits: `payment.payment_link_wizard_view_form`
- Root tag: `div`
- Field references: 6
- Sample fields: `amount`, `currency_id`, `epd_info`, `invoice_amount_due`, `open_installments`, `open_installments_preview`
- XPath or positional patches: 2

## Actions

- `action_invoice_order_generate_link`: `act_window` Generate a Payment Link

## Navigation

- **Parent:** [[docs/Community Addons/account_payment/Views]]

<!-- GENERATED:VIEWFILE -->
