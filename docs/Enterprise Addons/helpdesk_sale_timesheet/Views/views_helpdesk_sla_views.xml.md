---
tags: [odoo, enterprise, generated, views]
---

# views/helpdesk_sla_views.xml

- Module: [[docs/Enterprise Addons/helpdesk_sale_timesheet/helpdesk_sale_timesheet|helpdesk_sale_timesheet]]
- Scope: Enterprise Addons
- Source file: `views/helpdesk_sla_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `helpdesk_sla_view_tree_inherit_sale_timesheet`
- Name: helpdesk.sla.list.inherit.sale.timesheet
- Model: `helpdesk.sla`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_sla_view_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `product_ids`
- XPath or positional patches: 1

### `helpdesk_sla_view_form_inherit_sale_timesheet`
- Name: helpdesk.sla.form.inherit.sale.timesheet
- Model: `helpdesk.sla`
- Type: inferred from arch
- Inherits: `helpdesk.helpdesk_sla_view_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `product_ids`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/helpdesk_sale_timesheet/Views]]

