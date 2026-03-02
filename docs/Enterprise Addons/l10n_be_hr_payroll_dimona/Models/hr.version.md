<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# hr.version

- Module: [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona/l10n_be_hr_payroll_dimona|l10n_be_hr_payroll_dimona]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/hr_version.py`
- Python classes: `HrVersion`

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 1, `Char` x 2, `Integer` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `l10n_be_dimona_declaration_state`: `Selection`
- `l10n_be_dimona_in_declaration_number`: `Char`
- `l10n_be_dimona_last_declaration_number`: `Char`
- `l10n_be_dimona_planned_hours`: `Integer` (comodel `Student Planned Hours`)
- `l10n_be_is_student`: `Boolean` (compute `_compute_l10n_be_is_student`)

## Method hints

- Detected methods: 11
- Action methods: `action_check_dimona`
- Compute methods: `_compute_l10n_be_is_student`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_be_hr_payroll_dimona/Models]]

<!-- GENERATED:MODEL -->
