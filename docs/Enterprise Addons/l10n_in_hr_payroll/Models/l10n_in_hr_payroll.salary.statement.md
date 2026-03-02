<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_in_hr_payroll.salary.statement

- Module: [[docs/Enterprise Addons/l10n_in_hr_payroll/l10n_in_hr_payroll|l10n_in_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/l10n_in_salary_statement.py`
- Python classes: `L10n_In_Hr_PayrollSalaryStatement`
- Description: Salary Statement Report
- Inherits: `hr.payroll.declaration.mixin`

## Field footprint

- Detected fields: 2
- Field types: `Char` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `month`: `Selection`
- `name`: `Char` (compute `_compute_name`, store `True`)

## Method hints

- Detected methods: 7
- Action methods: `action_generate_declarations`
- Compute methods: `_compute_name`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_in_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
