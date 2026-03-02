<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.employee

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona/l10n_be_hr_payroll_dimona|l10n_be_hr_payroll_dimona]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_employee.py`
- Python classes: `HrEmployee`

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 1, `Char` x 2, `Integer` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `l10n_be_dimona_declaration_state`: `Selection` (related `version_id.l10n_be_dimona_declaration_state`)
- `l10n_be_dimona_in_declaration_number`: `Char` (related `version_id.l10n_be_dimona_in_declaration_number`)
- `l10n_be_dimona_last_declaration_number`: `Char` (related `version_id.l10n_be_dimona_last_declaration_number`)
- `l10n_be_dimona_planned_hours`: `Integer` (related `version_id.l10n_be_dimona_planned_hours`)
- `l10n_be_is_student`: `Boolean` (related `version_id.l10n_be_is_student`)

## Method hints

- Detected methods: 2
- Action methods: `action_check_dimona`
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona/Models]]

<!-- GENERATED:MODEL -->
