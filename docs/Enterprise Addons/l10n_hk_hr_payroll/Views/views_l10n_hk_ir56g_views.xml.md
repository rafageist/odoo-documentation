<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/l10n_hk_ir56g_views.xml

- Module: [[docs/Enterprise Addons/l10n_hk_hr_payroll/l10n_hk_hr_payroll|l10n_hk_hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/l10n_hk_ir56g_views.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `view_l10n_hk_ir56g_line_form`
- Name: l10n_hk.ir56g.line.view.form
- Model: `l10n_hk.ir56g.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 13
- Sample fields: `amount_money_payable`, `amount_non_exercised_stock_options`, `date_grant`, `date_return`, `employee_id`, `has_money_payable_held_under_ird`, `has_non_exercised_stock_options`, `is_salary_tax_borne`, `leave_hk_date`, `other_reason_departure`, and 3 more
- XPath or positional patches: 0

### `l10n_hk_ir56g_view_tree`
- Name: l10n_hk.ir56g.view.list
- Model: `l10n_hk.ir56g`
- Type: inferred from arch
- Inherits: `l10n_hk_hr_payroll.l10n_hk_ird_view_list`
- Root tag: `list`
- Field references: 0
- XPath or positional patches: 1

### `l10n_hk_ir56g_view_form`
- Name: l10n_hk_ir56g.view.form
- Model: `l10n_hk.ir56g`
- Type: inferred from arch
- Inherits: `l10n_hk_hr_payroll.l10n_hk_ird_view_form`
- Root tag: `form`
- Field references: 0
- XPath or positional patches: 3

## Actions

- `l10n_hk_ir56g_action`: `act_window` IR56G Sheet

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_hk_hr_payroll/Views]]

<!-- GENERATED:VIEWFILE -->
