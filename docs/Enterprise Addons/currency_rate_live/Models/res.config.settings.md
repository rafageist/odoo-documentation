<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/currency_rate_live/currency_rate_live|currency_rate_live]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 3
- Field types: `Date` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `currency_interval_unit`: `Selection` (related `company_id.currency_interval_unit`)
- `currency_next_execution_date`: `Date` (related `company_id.currency_next_execution_date`)
- `currency_provider`: `Selection` (related `company_id.currency_provider`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: none
- Onchange methods: `onchange_currency_interval_unit`

## Navigation

- **Parent:** [[docs/Enterprise Addons/currency_rate_live/Models]]

<!-- GENERATED:MODEL -->
