---
tags: [odoo, community, generated, views]
---

# views/sale_order_views.xml

- Module: [[docs/Community Addons/sale_project/sale_project|sale_project]]
- Scope: Community Addons
- Source file: `views/sale_order_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_order_simple_form`
- Name: sale.order.form.from.task
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_form`
- Root tag: `header`
- Field references: 0
- XPath or positional patches: 2

### `view_sales_order_filter_inherit_sale_project`
- Name: sale.order.list.select.inherit.sale_project
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_sales_order_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `order_line`, `project_id`
- XPath or positional patches: 0

### `view_order_form_inherit_sale_project`
- Name: sale.order.form.sale.project
- Model: `sale.order`
- Type: inferred from arch
- Inherits: `sale.view_order_form`
- Root tag: `button`
- Field references: 5
- Sample fields: `journal_id`, `milestone_count`, `project_count`, `project_id`, `tasks_count`
- Buttons: `action_view_invoice`, `action_view_milestone`, `action_view_project_ids`
- XPath or positional patches: 0

## Actions

- `model_sale_order_action_create_project`: `server` Create Project

## Navigation

- **Parent:** [[docs/Community Addons/sale_project/Views]]

