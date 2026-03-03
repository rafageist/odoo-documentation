---
tags: [odoo, enterprise, generated, views]
---

# views/crm_lead_views.xml

- Module: [[docs/Enterprise Addons/crm_helpdesk/crm_helpdesk|crm_helpdesk]]
- Scope: Enterprise Addons
- Source file: `views/crm_lead_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `helpdesk_ticket_view_form_inherited`
- Name: helpdesk.ticket.form.inherited
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_convert_ticket_to_lead_or_opportunity`
- XPath or positional patches: 1

### `crm_lead_view_form`
- Name: crm.lead.form
- Model: `crm.lead`
- Type: inferred from arch
- Inherits: `crm.crm_lead_view_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `%(crm_lead_convert2ticket_action)d`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/crm_helpdesk/Views]]

