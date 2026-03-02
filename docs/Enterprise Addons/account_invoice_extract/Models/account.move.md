<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.move

- Module: [[docs/Enterprise Addons/account_invoice_extract/account_invoice_extract|account_invoice_extract]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/account_invoice.py`
- Python classes: `AccountMove`
- Inherits: `extract.mixin.with.words`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 1, `Char` x 1, `Integer` x 1, `Json` x 1
- Relation fields: 0

## Sample fields

- `extract_can_show_banners`: `Boolean` (comodel `Can show the ocr banners`)
- `extract_detected_layout`: `Integer` (comodel `Extract Detected Layout Id`)
- `extract_partner_name`: `Char` (comodel `Extract Detected Partner Name`)
- `extract_prefill_data`: `Json`

## Method hints

- Detected methods: 38
- Action methods: `action_reload_ai_data`
- Compute methods: `_compute_is_in_extractable_state`, `_compute_show_banners`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_invoice_extract/Models]]

<!-- GENERATED:MODEL -->
