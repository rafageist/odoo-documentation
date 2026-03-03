---
tags: [odoo, enterprise, generated, views]
---

# views/mrp_production.xml

- Module: [[docs/Enterprise Addons/stock_barcode_mrp/stock_barcode_mrp|stock_barcode_mrp]]
- Scope: Enterprise Addons
- Source file: `views/mrp_production.xml`
- Views: 3
- Actions: 1
- Menus: 0
- Rules: 0

## View records

### `mrp_product_selector`
- Name: mrp.product.selector
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `form`
- Field references: 18
- Sample fields: `bom_line_id`, `company_id`, `is_completed`, `location_dest_id`, `lot_producing_ids`, `move_byproduct_ids`, `move_line_ids`, `move_raw_ids`, `picking_type_id`, `product_id`, and 8 more
- XPath or positional patches: 0

### `mrp_barcode_form`
- Name: mrp.form.view.barcode
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `form`
- Field references: 11
- Sample fields: `bom_id`, `company_id`, `components_availability`, `date_start`, `description_picking`, `move_raw_ids`, `origin`, `priority`, `product_id`, `product_uom_qty`, and 1 more
- XPath or positional patches: 0

### `mrp_barcode_kanban`
- Name: mrp.barcode.kanban
- Model: `mrp.production`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `date_start`, `name`, `priority`, `product_id`, `product_qty`, `product_uom_id`, `state`, `user_id`
- XPath or positional patches: 0

## Actions

- `mrp_action_kanban`: `act_window` Operations

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode_mrp/Views]]

