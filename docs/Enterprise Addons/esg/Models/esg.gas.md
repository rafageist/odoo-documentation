<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# esg.gas

- Module: [[docs/Enterprise Addons/esg/esg|esg]]
- Scope: Enterprise Addons
- Defined in module: yes
- Source files: `models/esg_gas.py`
- Python classes: `EsgGas`
- Description: Gas

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 1, `Char` x 2, `Integer` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `category`: `Selection`
- `code`: `Char`
- `global_warming_potential`: `Integer`
- `is_mandatory_gas`: `Boolean` (compute `_compute_is_mandatory_gas`)
- `name`: `Char`
- `sequence`: `Integer`

## Method hints

- Detected methods: 3
- Action methods: none
- Compute methods: `_compute_is_mandatory_gas`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Enterprise Addons/esg/Models]]

<!-- GENERATED:MODEL -->
