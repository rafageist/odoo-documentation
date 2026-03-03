---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/purchase/purchase|purchase]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `res_partner_view_purchase_buttons`
- Name: res.partner.view.purchase.buttons
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `div`
- Field references: 2
- Sample fields: `purchase_order_count`, `purchase_warn_msg`
- Buttons: `%(purchase.act_res_partner_2_purchase_order)d`
- XPath or positional patches: 2

### `view_partner_property_form`
- Name: res.partner.purchase.property.form.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `group`
- Field references: 5
- Sample fields: `buyer_id`, `property_purchase_currency_id`, `property_supplier_payment_term_id`, `receipt_reminder_email`, `reminder_date_before_receipt`
- XPath or positional patches: 1

## Actions

- `act_res_partner_2_supplier_invoices`: `act_window` Vendor Bills
- `act_res_partner_2_purchase_order`: `act_window` RFQs and Purchases

## Navigation

- **Parent:** [[docs/Community Addons/purchase/Views]]

