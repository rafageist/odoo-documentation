<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.config.settings

- Module: [[docs/Community Addons/product/product|product]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 6
- Field types: `Boolean` x 4, `Selection` x 2
- Relation fields: 0

## Sample fields

- `group_product_pricelist`: `Boolean` (comodel `Pricelists`)
- `group_product_variant`: `Boolean` (comodel `Variants`)
- `group_uom`: `Boolean` (comodel `Units of Measure & Packagings`)
- `module_loyalty`: `Boolean` (comodel `Promotions, Coupons, Gift Card & Loyalty Program`)
- `product_volume_volume_in_cubic_feet`: `Selection`
- `product_weight_in_lbs`: `Selection`

## Method hints

- Detected methods: 2
- Action methods: none
- Compute methods: none
- Onchange methods: `_onchange_group_sale_pricelist`

## Navigation

- **Parent:** [[docs/Community Addons/product/Models]]

<!-- GENERATED:MODEL -->
