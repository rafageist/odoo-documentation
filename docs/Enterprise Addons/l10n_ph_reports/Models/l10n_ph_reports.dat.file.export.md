<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_ph_reports.dat.file.export

- Module: [[docs/Enterprise Addons/l10n_ph_reports/l10n_ph_reports|l10n_ph_reports]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/vat_report_export.py`
- Python classes: `L10n_Ph_ReportsDatFileExport`
- Description: Philippine Periodic VAT Report Export Wizard

## Field footprint

- Detected fields: 3
- Field types: `Char` x 1, `Json` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `attachment_for`: `Selection` (compute `_compute_attachment_for`, store `True`)
- `available_forms`: `Char`
- `dat_export_warning`: `Json` (compute `_compute_dat_export_warning`)

## Method hints

- Detected methods: 3
- Action methods: `action_export_dat`
- Compute methods: `_compute_attachment_for`, `_compute_dat_export_warning`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ph_reports/Models]]

<!-- GENERATED:MODEL -->
