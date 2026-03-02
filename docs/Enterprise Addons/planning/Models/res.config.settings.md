<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# res.config.settings

- Module: [[docs/Enterprise Addons/planning/planning|planning]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 4
- Field types: `Boolean` x 1, `Integer` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `module_project_forecast`: `Boolean`
- `planning_employee_unavailabilities`: `Selection` (related `company_id.planning_employee_unavailabilities`)
- `planning_generation_interval`: `Integer` (comodel `Rate Of Shift Generation`, related `company_id.planning_generation_interval`)
- `planning_self_unassign_days_before`: `Integer` (comodel `Days before shift for unassignment`, related `company_id.planning_self_unassign_days_before`)

## Method hints

- Detected methods: 0
- Action methods: none
- Compute methods: none
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/planning/Models]]

<!-- GENERATED:MODEL -->
