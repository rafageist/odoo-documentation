<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/hr_timesheet_views.xml

- Module: [[docs/Enterprise Addons/sale_timesheet_enterprise/sale_timesheet_enterprise|sale_timesheet_enterprise]]
- Scope: Enterprise Addons
- Source file: `views/hr_timesheet_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `timesheet_view_grid_by_invoice_type`
- Name: account.analytic.line.grid.invoice.type
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `grid`
- Field references: 5
- Sample fields: `date`, `employee_id`, `so_line`, `timesheet_invoice_id`, `unit_amount`
- XPath or positional patches: 0

### `timesheet_view_grid_by_employee`
- Name: sale_timesheet_enterprise.account.analytic.line.grid.employee
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `timesheet_grid.timesheet_view_grid_by_employee`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `so_line`
- XPath or positional patches: 1

### `timesheet_view_grid_by_project`
- Name: sale_timesheet_enterprise.account.analytic.line.grid.project
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `timesheet_grid.timesheet_view_grid_by_project`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `so_line`
- XPath or positional patches: 1

### `timesheet_view_grid`
- Name: sale_timesheet_enterprise.account.analytic.line.grid.inherit
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `timesheet_grid.timesheet_view_grid`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `so_line`
- XPath or positional patches: 1

## Actions

- `timesheet_action_from_sales_order_item_kanban`: `view`

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_timesheet_enterprise/Views]]

<!-- GENERATED:VIEWFILE -->
