<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu/l10n_ke_edi_oscu|l10n_ke_edi_oscu]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 3, `Char` x 5, `Float` x 1, `Selection` x 1
- Relation fields: 0

## Sample fields

- `l10n_ke_control_unit`: `Char` (related `company_id.l10n_ke_control_unit`)
- `l10n_ke_insurance_code`: `Char` (related `company_id.l10n_ke_insurance_code`)
- `l10n_ke_insurance_name`: `Char` (related `company_id.l10n_ke_insurance_name`)
- `l10n_ke_insurance_rate`: `Float` (related `company_id.l10n_ke_insurance_rate`)
- `l10n_ke_oscu_cmc_key`: `Char` (related `company_id.l10n_ke_oscu_cmc_key`)
- `l10n_ke_oscu_serial_number`: `Char` (related `company_id.l10n_ke_oscu_serial_number`)
- `l10n_ke_oscu_user_agreement`: `Boolean` (related `company_id.l10n_ke_oscu_user_agreement`)
- `l10n_ke_oscu_user_agreement_is_readonly`: `Boolean` (compute `_compute_l10n_ke_oscu_user_agreement_is_readonly`)
- `l10n_ke_oscu_user_help`: `Boolean` (related `company_id.l10n_ke_oscu_user_help`)
- `l10n_ke_server_mode`: `Selection` (related `company_id.l10n_ke_server_mode`)

## Method hints

- Detected methods: 4
- Action methods: `action_l10n_ke_oscu_initialize`, `action_l10n_ke_send_insurance`
- Compute methods: `_compute_l10n_ke_oscu_user_agreement_is_readonly`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu/Models]]

<!-- GENERATED:MODEL -->
