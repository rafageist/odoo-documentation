<!-- GENERATED:MODEL -->
---
tags: [odoo, community, generated, model]
---

# res.config.settings

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Defined in module: extension only
- Source files: `models/res_config_settings.py`
- Python classes: `ResConfigSettings`

## Field footprint

- Detected fields: 38
- Field types: `Boolean` x 33, `Char` x 1, `Float` x 1, `Integer` x 1, `Selection` x 2
- Relation fields: 0

## Sample fields

- `annual_inventory_day`: `Integer` (related `company_id.annual_inventory_day`)
- `annual_inventory_month`: `Selection` (related `company_id.annual_inventory_month`)
- `barcode_separator`: `Char` (comodel `Separator`)
- `group_lot_on_delivery_slip`: `Boolean` (comodel `Display Lots & Serial Numbers on Delivery Slips`)
- `group_stock_adv_location`: `Boolean` (comodel `Multi-Step Routes`)
- `group_stock_lot_print_gs1`: `Boolean` (comodel `Print GS1 Barcodes for Lots & Serial Numbers`)
- `group_stock_multi_locations`: `Boolean` (comodel `Storage Locations`)
- `group_stock_production_lot`: `Boolean` (comodel `Lots & Serial Numbers`)
- `group_stock_reception_report`: `Boolean` (comodel `Reception Report`)
- `group_stock_sign_delivery`: `Boolean` (comodel `Signature`)
- `group_stock_tracking_lot`: `Boolean` (comodel `Packages`)
- `group_stock_tracking_owner`: `Boolean` (comodel `Consignment`)
- `group_warning_stock`: `Boolean` (comodel `Warnings for Stock`)
- `horizon_days`: `Float` (related `company_id.horizon_days`)
- `module_delivery`: `Boolean` (comodel `Delivery Methods`)
- `module_delivery_bpost`: `Boolean` (comodel `bpost Connector`)
- `module_delivery_dhl`: `Boolean` (comodel `DHL Express Connector`)
- `module_delivery_easypost`: `Boolean` (comodel `Easypost Connector`)
- `module_delivery_envia`: `Boolean` (comodel `Envia.com Connector`)
- `module_delivery_fedex_rest`: `Boolean` (comodel `FedEx Connector`)

## Method hints

- Detected methods: 7
- Action methods: none
- Compute methods: `_compute_replenish_on_order`
- Onchange methods: `_onchange_group_stock_multi_locations`, `_onchange_group_stock_production_lot`, `_onchange_stock_confirmation_fields`, `onchange_adv_location`

## Navigation

- **Parent:** [[docs/Community Addons/stock/Models]]

<!-- GENERATED:MODEL -->
