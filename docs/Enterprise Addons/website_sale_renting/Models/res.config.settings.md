<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/website_sale_renting/website_sale_renting|website_sale_renting]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 7, `Integer` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `renting_forbidden_fri`: `Boolean` (comodel `Friday`, related `company_id.renting_forbidden_fri`)
- `renting_forbidden_mon`: `Boolean` (comodel `Monday`, related `company_id.renting_forbidden_mon`)
- `renting_forbidden_sat`: `Boolean` (comodel `Saturday`, related `company_id.renting_forbidden_sat`)
- `renting_forbidden_sun`: `Boolean` (comodel `Sunday`, related `company_id.renting_forbidden_sun`)
- `renting_forbidden_thu`: `Boolean` (comodel `Thursday`, related `company_id.renting_forbidden_thu`)
- `renting_forbidden_tue`: `Boolean` (comodel `Tuesday`, related `company_id.renting_forbidden_tue`)
- `renting_forbidden_wed`: `Boolean` (comodel `Wednesday`, related `company_id.renting_forbidden_wed`)
- `renting_minimal_time_duration`: `Integer` (related `company_id.renting_minimal_time_duration`)
- `renting_minimal_time_unit`: `Selection` (related `company_id.renting_minimal_time_unit`)
- `tz`: `Selection` (related `website_id.tz`)

## Method hints

- Detected methods: 0
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/website_sale_renting/Models]]

<!-- GENERATED:MODEL -->
