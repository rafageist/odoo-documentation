<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.company

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu/l10n_ke_edi_oscu|l10n_ke_edi_oscu]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_company.py`
- Python classes: `ResCompany`

## Field footprint

- Detected fields: 12
- Field types: `Boolean` x 3, `Char` x 6, `Datetime` x 1, `Float` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `l10n_ke_branch_code`: `Char` (related `partner_id.l10n_ke_branch_code`, store `True`)
- `l10n_ke_control_unit`: `Char`
- `l10n_ke_insurance_code`: `Char`
- `l10n_ke_insurance_name`: `Char`
- `l10n_ke_insurance_rate`: `Float`
- `l10n_ke_oscu_cmc_key`: `Char`
- `l10n_ke_oscu_is_active`: `Boolean`
- `l10n_ke_oscu_last_fetch_purchase_date`: `Datetime`
- `l10n_ke_oscu_serial_number`: `Char` (compute `_compute_l10n_ke_oscu_serial_number`, store `True`)
- `l10n_ke_oscu_user_agreement`: `Boolean`
- `l10n_ke_oscu_user_help`: `Boolean`
- `l10n_ke_server_mode`: `Selection`

## Method hints

- Detected methods: 15
- Action methods: `action_l10n_ke_create_branches`, `action_l10n_ke_get_items`, `action_l10n_ke_get_stock_moves`, `action_l10n_ke_oscu_initialize`, `action_l10n_ke_send_insurance`
- Compute methods: `_compute_l10n_ke_oscu_is_active`, `_compute_l10n_ke_oscu_serial_number`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu/Models]]

<!-- GENERATED:MODEL -->
