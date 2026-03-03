---
tags: [odoo, enterprise, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Enterprise Addons/sale_planning/sale_planning|sale_planning]]
- Scope: Enterprise Addons
- Source file: `views/sale_order_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_order_form_inherit_sale_planning`
- Name: sale.order.form.sale.planning
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_form`
- Root tag: `button`
- Field references: 4
- Sample fields: `planning_first_sale_line_id`, `planning_hours_planned`, `planning_hours_to_plan`, `planning_initial_date`
- Buttons: `%(planning.planning_action_schedule_by_resource)d`, `action_view_invoice`, `action_view_planning`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_planning/Views]]

