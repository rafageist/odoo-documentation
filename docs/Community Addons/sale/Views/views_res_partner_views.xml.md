<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/res_partner_views.xml

- Module: [[docs/Community Addons/sale/sale|sale]]
- Scope: Community Addons
- Source file: `views/res_partner_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `res_partner_view_form_property_inherit`
- Name: res.partner.view.form.property.inherit
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `account.view_partner_property_form`
- Root tag: `group`
- Field references: 2
- Sample fields: `property_payment_term_id`, `property_supplier_payment_term_id`
- XPath or positional patches: 1

### `res_partner_view_form_payment_defaultcreditcard`
- Name: res.partner.view.form.payment.defaultcreditcard
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `payment.view_partners_form_payment_defaultcreditcard`
- Root tag: `button`
- Field references: 0
- Buttons: `%(payment.action_payment_token)d`
- XPath or positional patches: 0

### `res_partner_view_buttons`
- Name: res.partner.view.buttons
- Model: `res.partner`
- Type: inferred from arch
- Inherits: `base.view_partner_form`
- Root tag: `div`
- Field references: 2
- Sample fields: `sale_order_count`, `sale_warn_msg`
- Buttons: `sale.act_res_partner_2_sale_order`
- XPath or positional patches: 2

## Actions

- `act_res_partner_2_sale_order`: `act_window` Quotations and Sales

## Navigation

- **Parent:** [[docs/Community Addons/sale/Views]]

<!-- GENERATED:VIEWFILE -->
