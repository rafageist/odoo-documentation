---
tags: [comparison, inventory]
status: draft
---
# Inventory v18 vs v19

> **Summary:** Highlights structural updates in stock operations between v18 and v19, referencing the core process notes (`[[Odoo 18/Core/Processes/Inventory/Index.md]]`).

## Key observations so far
- Models renamed to explicit prefixes (`StockPickingType`, `StockPicking`) and constraints/indexes now use `models.Constraint` / `models.Index` wrappers.
- Domain helpers migrate to the new `Domain` API; search overrides now return `Domain.OR`/`Domain.AND` expressions instead of raw tuples.
- Picking types gain package options (`set_package_type`) and reuse action helpers that set domains contextually for incoming/outgoing/internal views.
- Pickings expose `reference_ids`, package history, and warning text; partner country cached via `partner_country_id` for logistics filters.
- Stock moves drop implicit procurement group defaults, store JSON `procurement_values`, add package tracking helpers, and tweak state labels (`Waiting Availability` → `Waiting`).
- Package/lot UI logic now checks state and user groups, ensuring combo and package updates keep sequencing consistent.

## Migration hints
- Replace manual tuple domains in overrides with `Domain` operations to stay compatible with v19 helpers.
- Review custom code accessing `group_id`, `move_ids_without_package`, or `move_line_ids_without_package`; equivalent data now exposed via reference/package helper fields.
- Update security-related domains (`groups_id`) to use `all_group_ids` on responsible/reservable user fields.
- If extending picking actions, account for `_get_code_report_name` and `_get_action` helpers that customize views per operation code.

## Next steps
- Diff `stock.move.line` and barcode components for UI/UX changes.
- Validate how the new package tracking fields surface in reports.
- Update migration scripts once v19 reference docs are imported.
