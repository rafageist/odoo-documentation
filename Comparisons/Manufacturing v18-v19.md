---
tags: [comparison, manufacturing]
status: draft
---
# Manufacturing v18 vs v19

> **Summary:** Notes the main manufacturing (MRP) changes worth checking before migrating customizations. Tie back to `[[Odoo 18/Core/Processes/Manufacturing]]` for baseline behaviour.

## Key observations so far
- Manufacturing orders introduce grouping: `mrp.production.group` links parent/child MOs and `production_group_id` replaces ad-hoc `procurement_group_id` usage.
- Quantities now rely on unit helpers (`allowed_uom_ids`, `product_uom_id.compare`, `is_zero`) and support multiple finished lots (`lot_producing_ids`). Deadlines become editable.
- Finished/raw moves use Domain helpers and avoid scrap/filter clutter; references move to the shared `stock.reference` mechanism.
- Work orders gain a simpler state machine (`blocked`, `ready`, `progress`, …), track `qty_ready`, and reuse new Intervals utilities; worksheet binaries were dropped.
- New UI flags (`show_generate_bom`, `show_produce`) plus context-aware picking-type defaults honor forced warehouses.

## Migration hints
- Update custom domains or searches to use `Domain` objects rather than tuples when filtering productions or components.
- Replace code that expects single `lot_producing_id` or exact rounding helpers (`float_compare`) with the new UoM helpers (`compare`, `is_zero`).
- When grouping or splitting orders, leverage `mrp.production.group` instead of home-grown relationship fields.
- For work-order custom logic, account for the new states (`blocked`, `ready`) and quantities (`qty_ready`, `qty_reported_from_previous_wo`).

## Next steps
- Review BoM/department flows (`mrp_bom`) for additional Domain rewrites.
- Document barcode and tablet view adjustments once identified.
- Capture enterprise manufacturing deltas that piggyback on these core changes.

## Navigation
- **Parent:** [[Comparisons/Comparisons]]
