<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.partner.bank

- Module: [[docs/Enterprise Addons/l10n_us_direct_deposit/l10n_us_direct_deposit|l10n_us_direct_deposit]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_partner_bank.py`
- Python classes: `ResPartnerBank`

## Field footprint

- Detected fields: 2
- Field types: `Char` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `wise_account_type`: `Selection`
- `wise_bank_account`: `Char` (compute `_compute_wise_bank_account`, store `True`)

## Method hints

- Detected methods: 1
- Action methods: none
- Compute methods: `_compute_wise_bank_account`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_us_direct_deposit/Models]]

<!-- GENERATED:MODEL -->
