---
tags: [odoo, enterprise, generated, views]
---

# report/mrp_report_views.xml

- Module: [[docs/Enterprise Addons/mrp_workorder_hr_account/mrp_workorder_hr_account|mrp_workorder_hr_account]]
- Scope: Enterprise Addons
- Source file: `report/mrp_report_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `mrp_report_pivot_view`
- Name: mrp.report.pivot.inherit.hr
- Model: `mrp.report`
- Type: inferred from arch
- Inherits: `mrp_account_enterprise.mrp_report_pivot_view`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `unit_employee_cost`
- XPath or positional patches: 1

### `mrp_report_form_view`
- Name: mrp.report.form.inherit.hr
- Model: `mrp.report`
- Type: inferred from arch
- Inherits: `mrp_account_enterprise.mrp_report_form_view`
- Root tag: `xpath`
- Field references: 2
- Sample fields: `employee_cost`, `unit_employee_cost`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/mrp_workorder_hr_account/Views]]

