---
tags: [odoo, community, generated, views]
---

# views/project_task_views.xml

- Module: [[docs/Community Addons/sale_project/sale_project|sale_project]]
- Scope: Community Addons
- Source file: `views/project_task_views.xml`
- Views: 13
- Actions: 4
- Menus: 0
- Rules: 0

## View records

### `project_milestone_view_kanban_inherit_sale_project`
- Name: project.milestone.view.kanban.inherit
- Model: `project.milestone`
- Type: inferred from arch
- Inherits: `project.project_milestone_view_kanban`
- Root tag: `field`
- Field references: 3
- Sample fields: `is_deadline_exceeded`, `quantity_percentage`, `sale_line_display_name`
- XPath or positional patches: 1

### `quick_create_task_form_res_partner`
- Name: project.task.form.quick_create.res.partner.inherit.sale_project
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.quick_create_task_form_res_partner`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_task_form_res_partner`
- Name: project.task.form.res.partner.inherit.sale_project
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_form_res_partner`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `project_milestone_view_tree`
- Name: project.milestone.view.list.inherit
- Model: `project.milestone`
- Type: inferred from arch
- Inherits: `project.project_milestone_view_tree`
- Root tag: `xpath`
- Field references: 5
- Sample fields: `allow_billable`, `product_uom_qty`, `project_partner_id`, `quantity_percentage`, `sale_line_id`
- Buttons: `action_view_sale_order`
- XPath or positional patches: 2

### `project_milestone_view_form`
- Name: project.milestone.view.form.inherit
- Model: `project.milestone`
- Type: inferred from arch
- Inherits: `project.project_milestone_view_form`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `allow_billable`, `product_uom_id`, `product_uom_qty`, `project_partner_id`, `quantity_percentage`, `sale_line_id`
- Buttons: `action_view_sale_order`
- XPath or positional patches: 2

### `project_task_view_search`
- Name: project.task.search.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_search_form_project_base`
- Root tag: `field`
- Field references: 2
- Sample fields: `partner_id`, `sale_order_id`
- XPath or positional patches: 1

### `view_task_tree2_inherit_sale_project`
- Name: project.task.form.inherit.sale.project
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_task_view_tree_base`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sale_line_id`
- XPath or positional patches: 1

### `project_task_view_tree_main_base`
- Name: project.task.main.list.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_task_view_tree_main_base`
- Root tag: `field`
- Field references: 2
- Sample fields: `allow_billable`, `partner_id`
- XPath or positional patches: 0

### `view_sale_project_inherit_form`
- Name: project.task.view.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.view_task_form2`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `allow_billable`, `project_id`, `project_sale_order_id`, `sale_line_id`, `sale_order_id`, `sale_order_state`
- Buttons: `action_view_so`
- XPath or positional patches: 8

### `view_sale_project_quick_create_task_form`
- Name: project.task.view.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.quick_create_task_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_edit_project_inherit_form`
- Name: project.project.view.inherit
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.edit_project`
- Root tag: `div`
- Field references: 9
- Sample fields: `allow_billable`, `display_sales_stat_buttons`, `has_any_so_to_invoice`, `has_any_so_with_nothing_to_invoice`, `privacy_visibility`, `reinvoiced_sale_order_id`, `sale_line_id`, `sale_order_count`, `sale_order_state`
- Buttons: `action_customer_preview`, `action_view_sos`
- XPath or positional patches: 5

### `project_project_view_tree_inherit_sale_project`
- Name: project.project.list.inherit.sale.project
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `allow_billable`, `sale_line_id`
- XPath or positional patches: 2

### `project_project_view_inherit_project_filter`
- Name: project.project.select.inherit.project
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.view_project_project_filter`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `sale_order_id`
- XPath or positional patches: 1

## Actions

- `project.action_project_task_user_tree`: `act_window`
- `project.action_view_all_task`: `act_window`
- `project.action_view_my_task`: `act_window`
- `project.action_view_task`: `act_window`

## Navigation

- **Parent:** [[docs/Community Addons/sale_project/Views]]

