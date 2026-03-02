<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_ticket_views.xml

- Module: [[docs/Enterprise Addons/helpdesk_repair/helpdesk_repair|helpdesk_repair]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_ticket_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `helpdesk_ticket_view_form_inherit_stock_user`
- Name: helpdesk.ticket.form.inherit.repair.stock.user
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_form`
- Root tag: `field`
- Field references: 2
- Sample fields: `stage_id`, `use_product_repairs`
- Buttons: `action_repair_order_form`
- XPath or positional patches: 0

### `helpdesk_ticket_view_form_inherit_helpdesk_repair`
- Name: helpdesk.ticket.form.inherit.helpdesk.repair
- Model: `helpdesk.ticket`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_ticket_view_form`
- Root tag: `button`
- Field references: 1
- Sample fields: `repairs_count`
- Buttons: `action_open_helpdesk_ticket`, `action_view_repairs`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_repair/Views]]

<!-- GENERATED:VIEWFILE -->
