<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# studio.export.wizard.data

- Module: [[docs/Enterprise Addons/web_studio/web_studio|web_studio]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `wizard/studio_export_wizard.py`
- Python classes: `StudioExportWizardData`
- Description: Studio Export Data

## Field footprint

- Detected fields: 9
- Field types: `Boolean` x 4, `Char` x 4, `Many2oneReference` x 1
- Relation fields: 0

## Sample fields

- `is_demo_data`: `Boolean`
- `model`: `Char`
- `model_name`: `Char` (compute `_compute_model_name`, store `True`)
- `name`: `Char` (comodel `Record Name`)
- `post`: `Boolean`
- `pre`: `Boolean`
- `res_id`: `Many2oneReference`
- `studio`: `Boolean`
- `xmlid`: `Char` (comodel `External ID`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_model_name`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/web_studio/Models]]

<!-- GENERATED:MODEL -->
