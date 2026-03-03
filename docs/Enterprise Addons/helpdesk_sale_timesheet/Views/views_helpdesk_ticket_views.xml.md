---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_ticket_views.xml

- Module: [[docs/Enterprise Addons/helpdesk_sale_timesheet/helpdesk_sale_timesheet|helpdesk_sale_timesheet]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_ticket_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `helpdesk_ticket_view_tree_inherit_sale_timesheet`
- Name: helpdesk.ticket.list.inherit.sale.timesheet
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_tickets_view_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `partner_id`, `sale_line_id`
- XPath or positional patches: 0

### `helpdesk_ticket_view_form_inherit_helpdesk_sale_timesheet`
- Name: helpdesk.ticket.form.inherit.sale.timesheet
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk_timesheet.helpdesk_ticket_view_form_inherit_helpdesk_timesheet`
- Root tag: `xpath`
- Field references: 11
- Sample fields: `display_invoice_button`, `helpdesk_ticket_id`, `invoice_count`, `is_so_line_edited`, `remaining_hours_available`, `remaining_hours_so`, `sale_line_id`, `sale_order_state`, `so_line`, `timesheet_invoice_id`, and 1 more
- Buttons: `action_view_invoices`, `action_view_so`
- XPath or positional patches: 6

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_sale_timesheet/Views]]

