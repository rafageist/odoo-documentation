<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_ticket_views.xml

- Module: [[docs/Enterprise Addons/helpdesk_sale_loyalty/helpdesk_sale_loyalty|helpdesk_sale_loyalty]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_ticket_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `helpdesk_ticket_view_form_inherit_helpdesk_sale_coupon`
- Name: helpdesk.ticket.form.inherit.sale.coupon
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_form`
- Root tag: `field`
- Field references: 5
- Sample fields: `coupons_count`, `default_giftcard_program_id`, `gift_card_count`, `stage_id`, `use_coupons`
- Buttons: `%(helpdesk_sale_coupon_generate_action)d`, `%(helpdesk_sale_giftcard_generate_wizard_action)d`, `action_open_helpdesk_ticket`, `open_coupons`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_sale_loyalty/Views]]

<!-- GENERATED:VIEWFILE -->
