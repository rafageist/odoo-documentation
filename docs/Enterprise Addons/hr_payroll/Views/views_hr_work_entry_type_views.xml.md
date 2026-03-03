---
tags: [odoo, enterprise, generated, views]
---

# views/hr_work_entry_type_views.xml

- Module: [[docs/Enterprise Addons/hr_payroll/hr_payroll|hr_payroll]]
- Scope: Enterprise Addons
- Source file: `views/hr_work_entry_type_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `payroll_hr_work_entry_type_view_form_inherit_contract`
- Name: payroll.hr.work.entry.type.view.form.inherit.contract
- Model: `hr.work.entry.type`
- Type: inferred from arch
- Inherits: `hr_work_entry.hr_work_entry_type_view_form`
- Root tag: `group`
- Field references: 1
- Sample fields: `is_unforeseen`
- XPath or positional patches: 1

### `payroll_hr_work_entry_type_view_form_inherit`
- Name: payroll.hr.work.entry.type.view.form.inherit
- Model: `hr.work.entry.type`
- Type: inferred from arch
- Inherits: `hr_work_entry.hr_work_entry_type_view_form`
- Root tag: `xpath`
- Field references: 4
- Sample fields: `is_work`, `round_days`, `round_days_type`, `unpaid_structure_ids`
- XPath or positional patches: 1

## Navigation

- **Parent:** [[docs/Enterprise Addons/hr_payroll/Views]]

