<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_es_reports.aeat.boe.mod390.export.wizard

- Module: [[docs/Enterprise Addons/l10n_es_reports/l10n_es_reports|l10n_es_reports]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/aeat_boe_export_wizards.py`
- Python classes: `L10n_Es_ReportsAeatBoeMod390ExportWizard`
- Description: BOE Export Wizard for (mod390)
- Inherits: `l10n_es_reports.aeat.boe.export.wizard`

## Field footprint

- Detected fields: 17
- Field types: `Boolean` x 7, `Char` x 9, `Date` x 1
- Relation fields: 0

## Sample fields

- `group_number`: `Char`
- `is_in_tax_unit`: `Boolean` (compute `_compute_is_in_tax_unit`)
- `is_substitute_decl_by_rectif_of_quotas`: `Boolean`
- `is_substitute_declaration`: `Boolean`
- `judicial_person_name`: `Char`
- `judicial_person_nif`: `Char`
- `judicial_person_notary`: `Char`
- `judicial_person_procuration_date`: `Date`
- `monthly_return`: `Boolean`
- `physical_person_name`: `Char`
- `previous_decl_number`: `Char`
- `principal_activity`: `Char`
- `principal_code_activity`: `Char`
- `principal_iae_epigrafe`: `Char`
- `special_cash_basis`: `Boolean`
- `special_cash_basis_beneficiary`: `Boolean`
- `special_regime_applicable_163`: `Boolean`

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: `_compute_is_in_tax_unit`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_es_reports/Models]]

<!-- GENERATED:MODEL -->
