<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.config.settings

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 10
- Field types: `Boolean` x 10
- Relation fields: 0

## Sample fields

- `group_mrp_byproducts`: `Boolean` (comodel `By-Products`)
- `group_mrp_reception_report`: `Boolean` (comodel `Allocation Report for Manufacturing Orders`)
- `group_mrp_routings`: `Boolean` (comodel `MRP Work Orders`)
- `group_mrp_workorder_dependencies`: `Boolean` (comodel `Work Order Dependencies`)
- `group_unlocked_by_default`: `Boolean` (comodel `Unlock Manufacturing Orders`)
- `module_mrp_mps`: `Boolean` (comodel `Master Production Schedule`)
- `module_mrp_plm`: `Boolean` (comodel `Product Lifecycle Management (PLM)`)
- `module_mrp_subcontracting`: `Boolean` (comodel `Subcontracting`)
- `module_quality_control`: `Boolean` (comodel `Quality`)
- `module_quality_control_worksheet`: `Boolean` (comodel `Quality Worksheet`)

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: none
- Onchange methods: `_onchange_group_unlocked_by_default`

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Models]]

<!-- GENERATED:MODEL -->
