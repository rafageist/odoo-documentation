<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/sale_timesheet_enterprise/sale_timesheet_enterprise|sale_timesheet_enterprise]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 3
- Field types: `Boolean` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `invoiced_timesheet`: `Selection`
- `timesheet_show_leaderboard`: `Boolean` (related `company_id.timesheet_show_leaderboard`)
- `timesheet_show_rates`: `Boolean` (related `company_id.timesheet_show_rates`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: none
- Onchange methods: `_onchange_timesheet_show_rates`

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_timesheet_enterprise/Models]]

<!-- GENERATED:MODEL -->
