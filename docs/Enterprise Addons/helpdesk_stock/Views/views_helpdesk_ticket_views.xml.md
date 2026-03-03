---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_ticket_views.xml

- Module: [[docs/Enterprise Addons/helpdesk_stock/helpdesk_stock|helpdesk_stock]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_ticket_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `helpdesk_ticket_view_form_inherit_stock_user`
- Name: helpdesk.ticket.form.inherit.return.stock.user
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_form`
- Root tag: `field`
- Field references: 3
- Sample fields: `has_partner_picking`, `stage_id`, `use_product_returns`
- Buttons: `%(stock.act_stock_return_picking)d`, `action_create_replacement`
- XPath or positional patches: 0

### `helpdesk_ticket_view_form_inherit_helpdesk_stock`
- Name: helpdesk.ticket.form.inherit.stock
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_form`
- Root tag: `button`
- Field references: 7
- Sample fields: `pickings_count`, `replacement_count`, `suitable_product_ids`, `tracking`, `use_credit_notes`, `use_product_repairs`, `use_product_returns`
- Buttons: `action_open_helpdesk_ticket`, `action_view_pickings`, `action_view_replacements`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_stock/Views]]

