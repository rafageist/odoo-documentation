---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_ticket_views.xml

- Module: [[docs/Enterprise Addons/helpdesk_sale/helpdesk_sale|helpdesk_sale]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_ticket_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `helpdesk_tickets_view_tree_inherit_helpdesk_sale`
- Name: helpdesk.ticket.form.inherit.sale
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_tickets_view_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `helpdesk_ticket_view_search_inherit_helpdesk_sale`
- Name: helpdesk.ticket.search.inherit.sale
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_tickets_view_search_base`
- Root tag: `field`
- Field references: 2
- Sample fields: `sale_order_id`, `stage_id`
- XPath or positional patches: 1

### `quick_create_ticket_form`
- Name: helpdesk.ticket.form.quick_create
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.quick_create_ticket_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `helpdesk_ticket_view_form_inherit_helpdesk_invoicing`
- Name: helpdesk.ticket.form.inherit.invoicing
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_form`
- Root tag: `field`
- Field references: 3
- Sample fields: `commercial_partner_id`, `email_cc`, `sale_order_id`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_sale/Views]]

