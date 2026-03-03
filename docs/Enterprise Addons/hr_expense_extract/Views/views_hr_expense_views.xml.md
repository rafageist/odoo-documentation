---
tags: [odoo, enterprise, generated, views]
---

# views/hr_expense_views.xml

- Module: [[docs/Enterprise Addons/hr_expense_extract/hr_expense_extract|hr_expense_extract]]
- Scope: Enterprise Addons
- Source file: `views/hr_expense_views.xml`
- Views: 4
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `hr_expense_extract_view_kanban`
- Name: hr.expense.extract.view.kanban
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense.hr_expense_view_expenses_analysis_kanban`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 3

### `hr_expense_extract_view_list`
- Name: hr.expense.extract.view.list
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense.hr_expense_view_expenses_analysis_tree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `extract_state_processed`
- XPath or positional patches: 2

### `hr_expense_extract_view_graph`
- Name: hr.expense.extract.view.graph
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense.hr_expense_view_graph`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `extract_document_uuid`, `extract_status`
- XPath or positional patches: 1

### `hr_expense_extract_view_form`
- Name: hr.expense.extract.view.form
- Model: `hr.expense`
- Type: inferred from arch
- Inherits: `hr_expense.hr_expense_view_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `extract_can_show_send_button`, `extract_document_uuid`, `extract_error_message`, `extract_state`
- Buttons: `action_manual_send_for_digitization`
- XPath or positional patches: 3

## Actions

- `hr_expense_parse_action_server`: `server` Digitize document

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_expense_extract/Views]]

