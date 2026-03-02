<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.partner.bank

- Module: [[docs/Community Addons/account_qr_code_emv/account_qr_code_emv|account_qr_code_emv]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_bank.py`
- Python classes: `ResPartnerBank`

## Field footprint

- Detected fields: 5
- Field types: `Boolean` x 2, `Char` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `country_proxy_keys`: `Char` (compute `_compute_country_proxy_keys`)
- `display_qr_setting`: `Boolean` (compute `_compute_display_qr_setting`)
- `include_reference`: `Boolean`
- `proxy_type`: `Selection`
- `proxy_value`: `Char`

## Method hints

- Detected methods: 14
- Action methods: none
- Compute methods: `_compute_country_proxy_keys`, `_compute_display_qr_setting`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/account_qr_code_emv/Models]]

<!-- GENERATED:MODEL -->
