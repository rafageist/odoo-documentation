<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# documents.document

- Module: [[docs/Enterprise Addons/documents_spreadsheet/documents_spreadsheet|documents_spreadsheet]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/documents_document.py`
- Python classes: `DocumentsDocument`
- Inherits: `spreadsheet.mixin`

## Field footprint

- Detected fields: 4
- Field types: `Binary` x 2, `Char` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `excel_export`: `Binary`
- `handler`: `Selection`
- `spreadsheet_binary_data`: `Binary` (compute `_compute_spreadsheet_binary_data`)
- `spreadsheet_thumbnail_checksum`: `Char` (compute `_compute_spreadsheet_thumbnail_checksum`)

## Method hints

- Detected methods: 38
- Action methods: `action_freeze_and_copy`, `action_open_new_spreadsheet`, `action_open_spreadsheet`
- Compute methods: `_compute_file_extension`, `_compute_spreadsheet_binary_data`, `_compute_spreadsheet_data`, `_compute_spreadsheet_thumbnail_checksum`, `_compute_thumbnail`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/documents_spreadsheet/Models]]

<!-- GENERATED:MODEL -->
