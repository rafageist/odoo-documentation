---
tags: [odoo, enterprise, generated, views]
---

# wizard/helpdesk_sale_giftcard_generate_views.xml

- Module: [[docs/Enterprise Addons/helpdesk_sale_loyalty/helpdesk_sale_loyalty|helpdesk_sale_loyalty]]
- Scope: Enterprise Addons
- Source file: `wizard/helpdesk_sale_giftcard_generate_views.xml`
- Views: 1
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `helpdesk_sale_giftcard_generate_wizard_view_form`
- Name: helpdesk.sale.giftcard.generate.wizard.form
- Model: `loyalty.generate.wizard`
- Type: inferred from arch
- Root tag: `form`
- Field references: 6
- Sample fields: `description`, `points_granted`, `points_name`, `program_id`, `program_type`, `valid_until`
- Buttons: `generate_giftcard`
- XPath or positional patches: 0

## Actions

- `helpdesk_sale_giftcard_generate_wizard_action`: `act_window` Generate & Send Gift Card

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_sale_loyalty/Views]]

