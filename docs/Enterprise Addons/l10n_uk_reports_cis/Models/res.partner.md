<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.partner

- Module: [[docs/Enterprise Addons/l10n_uk_reports_cis/l10n_uk_reports_cis|l10n_uk_reports_cis]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_partner.py`
- Python classes: `ResPartner`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Char` x 4, `Selection` x 1
- Relation fields: 0

## Sample fields

- `l10n_uk_cis_enabled`: `Boolean`
- `l10n_uk_reports_cis_deduction_rate`: `Selection` (compute `_compute_l10n_uk_reports_cis_deduction_rate`, store `True`)
- `l10n_uk_reports_cis_forename`: `Char` (compute `_compute_l10n_uk_cis_name_fields`, store `True`)
- `l10n_uk_reports_cis_second_forename`: `Char` (store `True`)
- `l10n_uk_reports_cis_surname`: `Char` (compute `_compute_l10n_uk_cis_name_fields`, store `True`)
- `l10n_uk_reports_cis_verification_number`: `Char`

## Method hints

- Detected methods: 6
- Action methods: none
- Compute methods: `_compute_l10n_uk_cis_name_fields`, `_compute_l10n_uk_reports_cis_deduction_rate`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_uk_reports_cis/Models]]

<!-- GENERATED:MODEL -->
