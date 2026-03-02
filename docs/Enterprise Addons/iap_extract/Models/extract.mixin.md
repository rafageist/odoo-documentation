<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# extract.mixin

- Module: [[docs/Enterprise Addons/iap_extract/iap_extract|iap_extract]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/extract_mixin.py`
- Python classes: `ExtractMixin`
- Description: Base class to extract data from documents
- Inherits: `mail.thread.main.attachment`

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 3, `Char` x 2, `Selection` x 1, `Text` x 1
- Relation fields: 0

## Sample fields

- `extract_can_show_send_button`: `Boolean` (comodel `Can show the ocr send button`, compute `_compute_show_send_button`)
- `extract_document_uuid`: `Char` (comodel `ID of the request to IAP-OCR`)
- `extract_error_message`: `Text` (comodel `Error message`, compute `_compute_error_message`)
- `extract_state`: `Selection`
- `extract_state_processed`: `Boolean` (compute `_compute_extract_state_processed`, store `True`)
- `extract_status`: `Char` (comodel `Extract status`)
- `is_in_extractable_state`: `Boolean` (compute `_compute_is_in_extractable_state`, store `True`)

## Method hints

- Detected methods: 36
- Action methods: `action_manual_send_for_digitization`, `action_send_batch_for_digitization`
- Compute methods: `_compute_error_message`, `_compute_extract_state_processed`, `_compute_is_in_extractable_state`, `_compute_show_send_button`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/iap_extract/Models]]

<!-- GENERATED:MODEL -->
