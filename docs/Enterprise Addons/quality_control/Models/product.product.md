<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# product.product

- Module: [[docs/Enterprise Addons/quality_control/quality_control|quality_control]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/quality.py`
- Python classes: `ProductProduct`

## Field footprint

- Detected fields: 3
- Field types: `Integer` x 3
- Relation fields: 0

## Sample fields

- `quality_control_point_qty`: `Integer` (compute `_compute_quality_check_qty`)
- `quality_fail_qty`: `Integer` (compute `_compute_quality_check_qty`)
- `quality_pass_qty`: `Integer` (compute `_compute_quality_check_qty`)

## Method hints

- Detected methods: 6
- Action methods: `action_see_quality_checks`, `action_see_quality_control_points`
- Compute methods: `_compute_quality_check_qty`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality_control/Models]]

<!-- GENERATED:MODEL -->
