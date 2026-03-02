<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/project_task_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm_sale/industry_fsm_sale|industry_fsm_sale]]
- Scope: Enterprise Addons
- Source file: `views/project_task_views.xml`
- Views: 4
- Actions: 21
- Menus: 2
- Rules: 0

## View records

### `project_task_view_mobile_form_inherit`
- Name: industry_fsm_sale.project.task.view.mobile.form
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.project_task_view_mobile_form`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `view_task_form2_inherit`
- Name: view.task.form2.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.view_task_form2_inherit`
- Root tag: `xpath`
- Field references: 14
- Sample fields: `allow_material`, `allow_quotations`, `currency_id`, `display_create_invoice_primary`, `display_create_invoice_secondary`, `invoice_count`, `is_fsm`, `material_line_product_count`, `material_line_total_price`, `partner_id`, and 4 more
- Buttons: `action_create_invoice`, `action_fsm_create_quotation`, `action_fsm_view_material`, `action_fsm_view_quotations`, `action_view_invoices`
- XPath or positional patches: 12

### `project_task_view_search_fsm_inherit_sale`
- Name: project.task.view.search
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.project_task_view_search_fsm`
- Root tag: `field`
- Field references: 2
- Sample fields: `partner_zip`, `sale_order_id`
- XPath or positional patches: 1

### `project_task_view_list_fsm_sale_inherit`
- Name: project.task.list.fsm.sale.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `industry_fsm.project_task_view_list_fsm`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `partner_id`, `under_warranty`
- Buttons: `action_create_invoice`
- XPath or positional patches: 2

## Actions

- `product_action_fsm`: `act_window` Products
- `industry_fsm.project_project_action_only_fsm`: `act_window`
- `project_task_action_to_invoice_fsm2_view_form`: `view`
- `project_task_action_to_invoice_fsm2_view_pivot`: `view`
- `project_task_action_to_invoice_fsm2_view_activity`: `view`
- `project_task_action_to_invoice_fsm2_view_gantt`: `view`
- `project_task_action_to_invoice_fsm2_view_calendar`: `view`
- `project_task_action_to_invoice_fsm2_view_map`: `view`
- `project_task_action_to_invoice_fsm2_view_kanban`: `view`
- `project_task_action_to_invoice_fsm2_view_list`: `view`
- `project_task_action_to_invoice_fsm2`: `act_window` To Invoice
- `project_task_action_to_invoice_fsm_view_form`: `view`
- `project_task_action_to_invoice_fsm_view_pivot`: `view`
- `project_task_action_to_invoice_fsm_view_activity`: `view`
- `project_task_action_to_invoice_fsm_view_gantt`: `view`
- `project_task_action_to_invoice_fsm_view_calendar`: `view`
- `project_task_action_to_invoice_fsm_view_map`: `view`
- `project_task_action_to_invoice_fsm_view_kanban`: `view`
- `project_task_action_to_invoice_fsm_view_list`: `view`
- `project_task_action_to_invoice_fsm`: `act_window` To Invoice

## Menus

- `fsm_menu_all_tasks_invoice`: To Invoice
- `fsm_menu_settings_product`: Products

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm_sale/Views]]

<!-- GENERATED:VIEWFILE -->
