---
tags: [odoo, enterprise, generated, views]
---

# views/project_project_views.xml

- Module: [[docs/Enterprise Addons/industry_fsm_sale/industry_fsm_sale|industry_fsm_sale]]
- Scope: Enterprise Addons
- Source file: `views/project_project_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_project_inherit_fsm_sale`
- Name: project.project.list.fsm.sale
- Model: `project.project`
- Type: inferred from arch
- Inherits: `sale_project.project_project_view_tree_inherit_sale_project`
- Root tag: `field`
- Field references: 3
- Sample fields: `is_fsm`, `partner_id`, `sale_line_id`
- XPath or positional patches: 0

### `project_project_view_inherit_project_filter_fsm_sale`
- Name: project.project.select.inherit.project
- Model: `project.project`
- Type: inferred from arch
- Inherits: `sale_project.project_project_view_inherit_project_filter`
- Root tag: `field`
- Field references: 1
- Sample fields: `sale_order_id`
- XPath or positional patches: 0

### `project_project_view_form_simplified_inherit`
- Name: project.project.view.form.simplified.inherit
- Model: `project.project`
- Type: inferred from arch
- Inherits: `project.project_project_view_form_simplified`
- Root tag: `field`
- Field references: 2
- Sample fields: `allow_billable`, `allow_material`
- XPath or positional patches: 0

### `project_view_form_inherit`
- Name: project.view.form.inherit
- Model: `project.project`
- Type: inferred from arch
- Inherits: `sale_timesheet.project_project_view_form`
- Root tag: `xpath`
- Field references: 6
- Sample fields: `allow_material`, `allow_quotations`, `hide_price`, `is_fsm`, `pricing_type`, `timesheet_product_id`
- XPath or positional patches: 16

## Navigation

- **Parent:** [[docs/Enterprise Addons/industry_fsm_sale/Views]]

