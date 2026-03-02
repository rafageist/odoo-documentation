<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/hr_expense_views.xml

- Module: [[docs/Community Addons/hr_expense/hr_expense|hr_expense]]
- Scope: Community Addons
- Source file: `views/hr_expense_views.xml`
- Views: 14
- Actions: 11
- Menus: 9
- Rules: 0

## View records

### `hr_expense_view_search_with_panel`
- Name: hr.expense.view.search.with.panel
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense_view_search`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `company_id`, `employee_id`, `state`
- XPath or positional patches: 1

### `hr_expense_view_activity`
- Name: hr.expense.activity
- Model: `hr.expense`
- Type: inferred from arch
- Root tag: `activity`
- Field references: 4
- Sample fields: `currency_id`, `employee_id`, `name`, `total_amount_currency`
- XPath or positional patches: 0

### `hr_expense_view_search`
- Name: hr.expense.view.search
- Model: `hr.expense`
- Type: inferred from arch
- Root tag: `search`
- Field references: 4
- Sample fields: `company_id`, `department_id`, `employee_id`, `name`
- XPath or positional patches: 0

### `hr_expense_view_graph`
- Name: hr.expense.graph
- Model: `hr.expense`
- Type: inferred from arch
- Root tag: `graph`
- Field references: 6
- Sample fields: `date`, `employee_id`, `price_unit`, `quantity`, `tax_amount`, `total_amount`
- XPath or positional patches: 0

### `hr_expense_view_pivot`
- Name: hr.expense.pivot
- Model: `hr.expense`
- Type: inferred from arch
- Root tag: `pivot`
- Field references: 3
- Sample fields: `date`, `employee_id`, `total_amount_currency`
- XPath or positional patches: 0

### `hr_expense_kanban_view_header`
- Name: hr.expense.kanban
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense_view_expenses_analysis_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `hr_expense_kanban_view`
- Name: hr.expense.kanban
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense_view_expenses_analysis_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `hr_expense_kanban_view_minimal`
- Name: hr.expense.kanban
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense_view_expenses_analysis_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `hr_expense_view_expenses_analysis_kanban`
- Name: hr.expense.kanban
- Model: `hr.expense`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 6
- Sample fields: `currency_id`, `date`, `employee_id`, `name`, `state`, `total_amount_currency`
- XPath or positional patches: 0

### `hr_expense_view_form_without_header`
- Name: hr.expense.view.form
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense.hr_expense_view_form`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `company_id`, `employee_id`
- XPath or positional patches: 1

### `hr_expense_view_form`
- Name: hr.expense.view.form
- Model: `hr.expense`
- Type: inferred from arch
- Root tag: `form`
- Field references: 34
- Sample fields: `account_id`, `analytic_distribution`, `company_currency_id`, `company_id`, `currency_id`, `currency_rate`, `date`, `department_id`, `description`, `duplicate_expense_ids`, and 24 more
- Buttons: `action_approve`, `action_open_account_move`, `action_open_split_expense`, `action_post`, `action_refuse`, `action_reset`, `action_split_wizard`, `action_submit`
- XPath or positional patches: 0

### `view_my_expenses_tree`
- Name: hr.expense.list
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense.view_expenses_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `view_expenses_tree`
- Name: hr.expense.list
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense_view_expenses_analysis_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `hr_expense_view_expenses_analysis_tree`
- Name: hr.expense.list
- Model: `hr.expense`
- Type: inferred from arch
- Root tag: `list`
- Field references: 27
- Sample fields: `account_id`, `activity_ids`, `analytic_distribution`, `company_currency_id`, `company_id`, `currency_id`, `date`, `department_id`, `employee_id`, `is_editable`, and 17 more
- Buttons: `action_get_attachment_view`
- XPath or positional patches: 0

## Actions

- `action_hr_expense_department_filtered`: `act_window` Expense Analysis
- `action_hr_expense_department_to_approve`: `act_window` Expense to Approve
- `action_hr_expense_account`: `act_window` Employee Expenses
- `hr_expense_actions_all_tree`: `view`
- `hr_expense_actions_all_pivot`: `view`
- `hr_expense_actions_all_graph`: `view`
- `hr_expense_actions_all`: `act_window` Expenses Analysis
- `hr_expense_actions_to_process`: `act_window` Expenses to Process
- `hr_expense_actions_my_all_kanban`: `view`
- `hr_expense_actions_my_all_tree`: `view`
- `hr_expense_actions_my_all`: `act_window` My Expenses

## Menus

- `menu_hr_expense_account_employee_expenses`: Employee Expenses
- `menu_hr_product`: Expense Categories
- `menu_hr_expense_configuration`: Configuration
- `menu_hr_expense_all_expenses`: Expenses Analysis
- `menu_hr_expense_reports`: Reporting
- `menu_hr_expense_expenses_to_process`: Expenses to Process
- `menu_hr_expense_my_expenses_all`: My Expenses
- `menu_hr_expense_my_expenses`: My Expenses
- `menu_hr_expense_root`: Expenses

## Navigation

- **Parent:** [[docs/Community Addons/hr_expense/Views]]

<!-- GENERATED:VIEWFILE -->
