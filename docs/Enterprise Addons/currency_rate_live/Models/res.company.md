<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.company

- Module: [[docs/Enterprise Addons/currency_rate_live/currency_rate_live|currency_rate_live]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResCompany`

## Field footprint

- Detected fields: 3
- Field types: `Date` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `currency_interval_unit`: `Selection`
- `currency_next_execution_date`: `Date`
- `currency_provider`: `Selection` (compute `_compute_currency_provider`, store `True`)

## Method hints

- Detected methods: 32
- Action methods: none
- Compute methods: `_compute_currency_provider`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/currency_rate_live/Models]]

<!-- GENERATED:MODEL -->
