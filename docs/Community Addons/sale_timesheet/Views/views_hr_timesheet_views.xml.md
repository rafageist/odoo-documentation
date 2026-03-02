<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_timesheet_views.xml

- Module: [[docs/Community Addons/sale_timesheet/sale_timesheet|sale_timesheet]]
- Scope: Community Addons
- Source file: `views/hr_timesheet_views.xml`
- Views: 9
- Actions: 11
- Menus: 0
- Rules: 0

## View records

### `view_calendar_account_analytic_line_multi_create`
- Name: account.analytic.line.calendar.multi_create
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_calendar_account_analytic_line_multi_create`
- Root tag: `field`
- Field references: 3
- Sample fields: `allow_billable`, `so_line`, `unit_amount`
- XPath or positional patches: 0

### `view_calendar_account_analytic_line`
- Name: account.analytic.line.calendar
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_calendar_account_analytic_line`
- Root tag: `field`
- Field references: 2
- Sample fields: `name`, `so_line`
- XPath or positional patches: 0

### `view_hr_timesheet_line_pivot_inherited`
- Name: account.analytic.line.pivot
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.view_hr_timesheet_line_pivot`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_hr_timesheet_line_graph_invoice_employee`
- Name: account.analytic.line.graph.invoice.employee
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `view_hr_timesheet_line_graph_employee_per_date`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `timesheet_invoice_id`
- XPath or positional patches: 1

### `view_hr_timesheet_line_graph_employee_per_date`
- Name: account.analytic.line.graph.employee.per.date
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 4
- Sample fields: `amount`, `date`, `employee_id`, `unit_amount`
- XPath or positional patches: 0

### `view_hr_timesheet_line_pivot_billing_rate`
- Name: account.analytic.line.pivot.billing.rate
- Model: `account.analytic.line`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 4
- Sample fields: `amount`, `date`, `timesheet_invoice_type`, `unit_amount`
- XPath or positional patches: 0

### `hr_timesheet_line_form_inherit`
- Name: account.analytic.line.form.inherit
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_timesheet_line_form`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `allow_billable`, `commercial_partner_id`, `is_so_line_edited`, `order_id`, `sale_order_state`, `so_line`, `timesheet_invoice_id`
- Buttons: `action_invoice_from_timesheet`, `action_sale_order_from_timesheet`
- XPath or positional patches: 2

### `hr_timesheet_line_tree_inherit`
- Name: account.analytic.line.list.inherit
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_timesheet_line_tree`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `allow_billable`, `commercial_partner_id`, `is_so_line_edited`, `so_line`
- XPath or positional patches: 1

### `timesheet_view_search`
- Name: account.analytic.line.search
- Model: `account.analytic.line`
- Type: inferred from arch
- Inherits: `hr_timesheet.hr_timesheet_line_search`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `order_id`
- XPath or positional patches: 3

## Actions

- `timesheet_action_from_plan`: `act_window` Timesheet
- `timesheet_action_plan_pivot`: `act_window` Timesheet
- `timesheet_action_from_sales_order_item_form`: `view`
- `timesheet_action_from_sales_order_item_graph`: `view`
- `timesheet_action_from_sales_order_item_pivot`: `view`
- `timesheet_action_from_sales_order_item_kanban`: `view`
- `timesheet_action_from_sales_order_item_tree`: `view`
- `timesheet_action_from_sales_order_item`: `act_window` Timesheets
- `timesheet_action_from_sales_order_form`: `view`
- `timesheet_action_from_sales_order_tree`: `view`
- `timesheet_action_from_sales_order`: `act_window` Timesheets

## Navigation

- **Parent:** [[docs/Community Addons/sale_timesheet/Views]]

<!-- GENERATED:VIEWFILE -->
