<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# digest.digest

- Module: [[docs/Enterprise Addons/account_accountant/account_accountant|account_accountant]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/digest.py`
- Python classes: `DigestDigest`

## Field footprint

- Detected fields: 2
- Field types: `Boolean` x 1, `Monetary` x 1
- Relation fields: 0

## Sample fields

- `kpi_account_bank_cash`: `Boolean` (comodel `Bank & Cash Moves`)
- `kpi_account_bank_cash_value`: `Monetary` (compute `_compute_kpi_account_total_bank_cash_value`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: `_compute_kpi_account_total_bank_cash_value`, `_compute_kpis_actions`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/account_accountant/Models]]

<!-- GENERATED:MODEL -->
