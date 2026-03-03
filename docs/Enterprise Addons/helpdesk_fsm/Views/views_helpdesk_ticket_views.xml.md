---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_ticket_views.xml

- Module: [[docs/Enterprise Addons/helpdesk_fsm/helpdesk_fsm|helpdesk_fsm]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_ticket_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `helpdesk_ticket_view_form`
- Name: helpdesk.ticket.form.inherit
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `fsm_task_count`, `use_fsm`
- Buttons: `action_generate_fsm_task`, `action_view_fsm_tasks`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_fsm/Views]]

