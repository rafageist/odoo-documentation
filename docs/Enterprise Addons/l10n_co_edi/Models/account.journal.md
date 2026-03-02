<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# account.journal

- Module: [[docs/Enterprise Addons/l10n_co_edi/l10n_co_edi|l10n_co_edi]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/account_journal.py`
- Python classes: `AccountJournal`

## Field footprint

- Detected fields: 7
- Field types: `Boolean` x 2, `Char` x 1, `Date` x 2, `Integer` x 2
- Relation fields: 0

## Sample fields

- `l10n_co_edi_debit_note`: `Boolean`
- `l10n_co_edi_dian_authorization_date`: `Date`
- `l10n_co_edi_dian_authorization_end_date`: `Date`
- `l10n_co_edi_dian_authorization_number`: `Char`
- `l10n_co_edi_is_support_document`: `Boolean` (comodel `Support Document`, compute `_compute_l10n_co_edi_is_support_document`, store `False`)
- `l10n_co_edi_max_range_number`: `Integer`
- `l10n_co_edi_min_range_number`: `Integer`

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_l10n_co_edi_is_support_document`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_co_edi/Models]]

<!-- GENERATED:MODEL -->
