<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# l10n_hu_edi.tax_audit_export

- Module: [[docs/Community Addons/l10n_hu_edi/l10n_hu_edi|l10n_hu_edi]]
- Scope: Community Addons
- Defined in module: yes
- Source files: `wizard/l10n_hu_edi_tax_audit_export.py`
- Python classes: `L10n_Hu_EdiTax_Audit_Export`
- Description: Tax audit export - Adóhatósági Ellenőrzési Adatszolgáltatás

## Field footprint

- Detected fields: 7
- Field types: `Binary` x 1, `Char` x 3, `Date` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `date_from`: `Date`
- `date_to`: `Date`
- `export_file`: `Binary`
- `filename`: `Char` (compute `_compute_filename`)
- `name_from`: `Char`
- `name_to`: `Char`
- `selection_mode`: `Selection`

## Method hints

- Detected methods: 2
- Action methods: `action_export`
- Compute methods: `_compute_filename`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/l10n_hu_edi/Models]]

<!-- GENERATED:MODEL -->
