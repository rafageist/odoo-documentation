<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.journal

- Module: [[docs/Enterprise Addons/l10n_us_payment_nacha/l10n_us_payment_nacha|l10n_us_payment_nacha]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_journal.py`
- Python classes: `AccountJournal`

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 1, `Char` x 6, `Selection` x 1
- Relation fields: 0

## Sample fields

- `nacha_company_identification`: `Char`
- `nacha_destination`: `Char`
- `nacha_discretionary_data`: `Char`
- `nacha_entry_class_code`: `Selection`
- `nacha_immediate_destination`: `Char`
- `nacha_immediate_origin`: `Char`
- `nacha_is_balanced`: `Boolean` (comodel `Generate Balanced Files`)
- `nacha_origination_dfi_identification`: `Char`

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_us_payment_nacha/Models]]

<!-- GENERATED:MODEL -->
