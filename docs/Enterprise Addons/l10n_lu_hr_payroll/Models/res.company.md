<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.company

- Module: [[docs/Enterprise Addons/l10n_lu_hr_payroll/l10n_lu_hr_payroll|l10n_lu_hr_payroll]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_company.py`
- Python classes: `ResCompany`

## Field footprint

- Detected fields: 6
- Field types: `Char` x 2, `Float` x 2, `Selection` x 2
- Relation fields: 0

## Sample fields

- `l10n_lu_accident_insurance_factor`: `Selection`
- `l10n_lu_accident_insurance_rate`: `Float` (compute `_compute_l10n_lu_accident_insurance_rate`)
- `l10n_lu_mutuality_class`: `Selection`
- `l10n_lu_mutuality_rate`: `Float` (compute `_compute_l10n_lu_mutuality_rate`)
- `l10n_lu_official_social_security`: `Char`
- `l10n_lu_seculine`: `Char`

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_l10n_lu_accident_insurance_rate`, `_compute_l10n_lu_mutuality_rate`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_lu_hr_payroll/Models]]

<!-- GENERATED:MODEL -->
