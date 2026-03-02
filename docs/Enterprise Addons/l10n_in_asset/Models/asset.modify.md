<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# asset.modify

- Module: [[docs/Enterprise Addons/l10n_in_asset/l10n_in_asset|l10n_in_asset]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `wizard/asset_modify.py`
- Python classes: `AssetModify`

## Field footprint

- Detected fields: 2
- Field types: `Char` x 1, `Monetary` x 1
- Relation fields: 0

## Sample fields

- `l10n_in_fiscal_code`: `Char` (related `company_id.account_fiscal_country_id.code`)
- `l10n_in_value_residual`: `Monetary` (compute `_compute_l10n_in_value_residual`, store `True`)

## Method hints

- Detected methods: 5
- Action methods: none
- Compute methods: `_compute_l10n_in_value_residual`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_in_asset/Models]]

<!-- GENERATED:MODEL -->
