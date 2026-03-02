<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# ir.attachment.report

- Module: [[docs/Enterprise Addons/data_cleaning/data_cleaning|data_cleaning]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `report/data_storage.py`
- Python classes: `IrAttachmentReport`
- Description: Storage

## Field footprint

- Detected fields: 4
- Field types: `Char` x 2, `Integer` x 1, `Many2oneReference` x 1
- Relation fields: 0

## Sample fields

- `name`: `Char` (comodel `Resource Name`, compute `_compute_name`)
- `res_id`: `Many2oneReference` (comodel `Record`)
- `res_model`: `Char` (comodel `Model`)
- `size`: `Integer` (comodel `Total Size`)

## Method hints

- Detected methods: 3
- Action methods: `action_attachment_detail`
- Compute methods: `_compute_name`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/data_cleaning/Models]]

<!-- GENERATED:MODEL -->
