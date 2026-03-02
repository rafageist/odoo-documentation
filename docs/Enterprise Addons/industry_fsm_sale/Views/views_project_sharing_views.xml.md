<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/project_sharing_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm_sale/industry_fsm_sale|industry_fsm_sale]]
- Scope: Enterprise Addons
- Source file: `views/project_sharing_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `project_sharing_inherit_project_task_view_tree`
- Name: project.task.view.list.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_project_task_view_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `allow_milestones`, `is_fsm`, `partner_id`
- XPath or positional patches: 0

### `project_sharing_project_task_inherit_view_form`
- Name: project.sharing.project.task.view.form.inherit
- Model: `project.task`
- Type: inferred from arch
- Inherits: `project.project_sharing_project_task_view_form`
- Root tag: `xpath`
- Field references: 10
- Sample fields: `allow_material`, `allow_quotations`, `currency_id`, `is_fsm`, `material_line_product_count`, `material_line_total_price`, `partner_id`, `portal_invoice_count`, `portal_quotation_count`, `warning_message`
- Buttons: `action_fsm_view_material`, `action_project_sharing_view_invoices`, `action_project_sharing_view_quotations`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm_sale/Views]]

<!-- GENERATED:VIEWFILE -->
