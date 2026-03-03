---
tags: [odoo, community, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Community Addons/sale_timesheet/sale_timesheet|sale_timesheet]]
- Scope: Community Addons
- Source file: `views/sale_order_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_order_form_inherit_sale_timesheet`
- Name: sale.order.form.sale.timesheet
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale_project.view_order_form_inherit_sale_project`
- Root tag: `button`
- Field references: 2
- Sample fields: `timesheet_encode_uom_id`, `timesheet_total_duration`
- Buttons: `action_view_milestone`, `action_view_timesheet`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/sale_timesheet/Views]]

