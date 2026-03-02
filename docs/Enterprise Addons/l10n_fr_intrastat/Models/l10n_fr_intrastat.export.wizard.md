<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# l10n_fr_intrastat.export.wizard

- Module: [[docs/Enterprise Addons/l10n_fr_intrastat/l10n_fr_intrastat|l10n_fr_intrastat]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/export_wizard.py`
- Python classes: `L10n_Fr_IntrastatExportWizard`
- Description: Options for the export of Intrastat in France

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 2, `Selection` x 2
- Relation fields: 0

## Sample fields

- `emebi_flow`: `Selection`
- `emebi_flow_visible`: `Boolean` (compute `_compute_export_type`)
- `export_type`: `Selection`
- `warning_incompatible_options`: `Boolean` (compute `_compute_warning_incompatible_options`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_export_type`, `_compute_warning_incompatible_options`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_fr_intrastat/Models]]

<!-- GENERATED:MODEL -->
