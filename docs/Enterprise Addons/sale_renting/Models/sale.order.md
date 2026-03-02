<!-- GENERATED:MODEL -->
---
tags: [odoo, enterprise, generated, model]
---

# sale.order

- Module: [[docs/Enterprise Addons/sale_renting/sale_renting|sale_renting]]
- Scope: Enterprise Addons
- Defined in module: extension only
- Source files: `models/sale_order.py`
- Python classes: `SaleOrder`

## Field footprint

- Detected fields: 12
- Field types: `Boolean` x 6, `Datetime` x 3, `Integer` x 2, `Selection` x 1
- Relation fields: 0

## Sample fields

- `duration_days`: `Integer` (compute `_compute_duration`)
- `has_pickable_lines`: `Boolean` (compute `_compute_has_action_lines`)
- `has_rented_products`: `Boolean` (compute `_compute_has_rented_products`)
- `has_returnable_lines`: `Boolean` (compute `_compute_has_action_lines`)
- `is_late`: `Boolean` (compute `_compute_is_late`)
- `is_rental_order`: `Boolean` (compute `_compute_is_rental_order`, store `True`)
- `next_action_date`: `Datetime` (compute `_compute_rental_status`, store `True`)
- `remaining_hours`: `Integer` (compute `_compute_duration`)
- `rental_return_date`: `Datetime`
- `rental_start_date`: `Datetime`
- `rental_status`: `Selection` (compute `_compute_rental_status`, store `True`)
- `show_update_duration`: `Boolean` (store `False`)

## Method hints

- Detected methods: 27
- Action methods: `action_open_pickup`, `action_open_return`, `action_update_rental_prices`
- Compute methods: `_compute_duration`, `_compute_has_action_lines`, `_compute_has_rented_products`, `_compute_is_late`, `_compute_is_rental_order`, `_compute_rental_status`
- Onchange methods: `_onchange_company_id_warning`, `_onchange_duration_show_update_duration`, `_onchange_is_rental_order`, `_onchange_pricelist_id_show_update_prices`, `_onchange_rental_return_date`, `_onchange_rental_start_date`

## Navigation

- **Parent:** [[docs/Enterprise Addons/sale_renting/Models]]

<!-- GENERATED:MODEL -->
