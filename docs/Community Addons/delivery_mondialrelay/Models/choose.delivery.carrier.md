<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# choose.delivery.carrier

- Module: [[docs/Community Addons/delivery_mondialrelay/delivery_mondialrelay|delivery_mondialrelay]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `wizard/choose_delivery_carrier.py`
- Python classes: `ChooseDeliveryCarrier`

## Field footprint

- Detected fields: 8
- Field types: `Boolean` x 1, `Char` x 7
- Relation fields: 0

## Sample fields

- `is_mondialrelay`: `Boolean` (compute `_compute_is_mondialrelay`)
- `mondialrelay_allowed_countries`: `Char` (compute `_compute_mr_allowed_countries`)
- `mondialrelay_brand`: `Char` (related `carrier_id.mondialrelay_brand`)
- `mondialrelay_colLivMod`: `Char` (related `carrier_id.mondialrelay_packagetype`)
- `mondialrelay_last_selected`: `Char`
- `mondialrelay_last_selected_id`: `Char` (compute `_compute_mr_last_selected_id`)
- `shipping_country_code`: `Char` (related `order_id.partner_shipping_id.country_id.code`)
- `shipping_zip`: `Char` (related `order_id.partner_shipping_id.zip`)

## Method hints

- Detected methods: 4
- Action methods: none
- Compute methods: `_compute_is_mondialrelay`, `_compute_mr_allowed_countries`, `_compute_mr_last_selected_id`
- Onchange methods: none

## Navigation

- **Parent:** [[docs/Community Addons/delivery_mondialrelay/Models]]

<!-- GENERATED:MODEL -->
