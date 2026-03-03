---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_ticket_views.xml

- Module: [[docs/Enterprise Addons/helpdesk_account/helpdesk_account|helpdesk_account]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_ticket_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `helpdesk_ticket_view_form_inherit_helpdesk_invoicing`
- Name: helpdesk.ticket.form.inherit.invoicing
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_form`
- Root tag: `field`
- Field references: 3
- Sample fields: `invoices_count`, `stage_id`, `use_credit_notes`
- Buttons: `%(helpdesk_account.helpdesk_ticket_action_refund)d`, `action_open_helpdesk_ticket`, `action_view_credit_notes`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_account/Views]]

