<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.groups

- Module: [[docs/Community Addons/auth_timeout/auth_timeout|auth_timeout]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_groups.py`
- Python classes: `ResGroups`

## Field footprint

- Detected fields: 12
- Field types: `Boolean` x 4, `Integer` x 4, `Selection` x 4
- Relation fields: 0

## Sample fields

- `has_lock_timeout`: `Boolean` (compute `_compute_has_lock_timeout`)
- `has_lock_timeout_inactivity`: `Boolean` (compute `_compute_lock_timeout_inactivity_bool`)
- `lock_timeout`: `Integer`
- `lock_timeout_2fa_selection`: `Selection` (compute `_compute_lock_timeout_2fa_selection`)
- `lock_timeout_delay_in_unit`: `Integer` (compute `_compute_lock_timeout_delay_unit`)
- `lock_timeout_delay_unit`: `Selection` (compute `_compute_lock_timeout_delay_unit`)
- `lock_timeout_inactivity`: `Integer`
- `lock_timeout_inactivity_2fa_selection`: `Selection` (compute `_compute_lock_timeout_inactivity_2fa_selection`)
- `lock_timeout_inactivity_delay_in_unit`: `Integer` (compute `_compute_lock_timeout_inactivity_delay_unit`)
- `lock_timeout_inactivity_delay_unit`: `Selection` (compute `_compute_lock_timeout_inactivity_delay_unit`)
- `lock_timeout_inactivity_mfa`: `Boolean`
- `lock_timeout_mfa`: `Boolean`

## Method hints

- Detected methods: 16
- Action methods: none
- Compute methods: `_compute_has_lock_timeout`, `_compute_lock_timeout_2fa_selection`, `_compute_lock_timeout_delay_unit`, `_compute_lock_timeout_inactivity_2fa_selection`, `_compute_lock_timeout_inactivity_bool`, `_compute_lock_timeout_inactivity_delay_unit`
- Onchange methods: `_onchange_has_lock_timeout`, `_onchange_has_lock_timeout_inactivity`, `_onchange_lock_timeout_delay_unit`, `_onchange_lock_timeout_inactivity_delay_unit`

## Navigation

- **Parent:** [[docs/Community Addons/auth_timeout/Models]]

<!-- GENERATED:MODEL -->
