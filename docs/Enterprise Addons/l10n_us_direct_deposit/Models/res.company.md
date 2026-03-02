<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.company

- Module: [[docs/Enterprise Addons/l10n_us_direct_deposit/l10n_us_direct_deposit|l10n_us_direct_deposit]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_company.py`
- Python classes: `ResCompany`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 1, `Char` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `wise_api_key`: `Char`
- `wise_connected`: `Boolean` (compute `_compute_wise_connected`)
- `wise_environment`: `Selection`
- `wise_profile_identifier`: `Char` (compute `_compute_wise_profile`, store `True`)

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_wise_connected`, `_compute_wise_profile`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_us_direct_deposit/Models]]

<!-- GENERATED:MODEL -->
