---
tags: [v18, core, master_data, product_product]
status: draft
---
# `product.product` (Odoo 18)

> **Summary:** Variant records carry the operational details for stock moves, procurement, barcode scanning, and reporting. They inherit most fields from `product.template` while providing per-variant combinations that downstream flows consume.

## Variant anatomy
- **Class:** `ProductProduct` in `odoo/addons/product/models/product.py`
- **Table:** `product_product`
- **Key fields:**
  - `product_tmpl_id`: parent template.
  - `attribute_value_ids`: ordered set of selected attribute values.
  - `default_code`, `barcode`: SKU identifiers used across inventory and PoS.
  - `qty_available`, `virtual_available`, `incoming_qty`, `outgoing_qty`: computed quantities fed by `stock.quant` and `stock.move` (see `[[Odoo 18/Core/Processes/Inventory/Index.md]]`).
  - `valuation_layer_ids`: linkage to valuation history and cost layers.

## Synchronisation with templates
- Most readable fields delegate to the template by default; overrides (`_inherits`-like behaviour through fields) let the variant store custom values such as `list_price` only when `product_variant_count > 1`.
- `ProductTemplate._create_variant_ids` ensures attribute combinations stay in sync, archiving missing variants and updating sequences.
- Single variant optimisation: `product_variant_id` directly points to the lone variant, avoiding one-to-many overhead in forms.

## Operational hooks
- **Inventory:** `stock.move` references variant `product_id`; reservations rely on `tracking` (lot/serial) and `responsible_id` fields.
- **MRP & BOM:** BoMs attach to variants via `product_variant_ids`, enabling configurator flows.
- **Procurement:** `seller_ids` provide vendor price lists at the variant level.
- **Reporting:** aggregated KPIs use `product_variant_ids` to drill down from template dashboards.

## Security & performance considerations
- Quantities are computed fields with `GROUP BY` heavy queries; keep an eye on record rules from `[[Odoo 18/Core/Infrastructure/Security.md]]` when introducing custom domains.
- Attachments (images, documents) reside via `attachment=True` fields inherited from the template (`image_*`); storage details in `[[Odoo 18/Core/Infrastructure/Files.md]]`.
- Variant-specific fields should be added to `attribute_line_ids` to guarantee configurator compatibility.

## Related notes
- Template definition: `[[Odoo 18/Core/Master Data/product_template.md]]`
- Units of measure: `[[Odoo 18/Core/Master Data/uom_uom.md]]`
- Accounting entry impact: `[[Odoo 18/Core/Processes/Accounting/account_move.md]]`
- Inventory execution: `[[Odoo 18/Core/Processes/Inventory/Index.md]]`
