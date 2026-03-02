<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/stock_move_line_views.xml

- Module: [[docs/Enterprise Addons/stock_barcode/stock_barcode|stock_barcode]]
- Scope: Enterprise Addons
- Source file: `views/stock_move_line_views.xml`
- Views: 4
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_stock_quant_tree`
- Name: stock_barcode.quant.list.inherit
- Model: `stock.quant`
- Type: inferred from arch
- Inherits: `stock.view_stock_quant_tree`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 3

### `stock_quant_barcode_kanban_2`
- Name: stock.quant.kanban.barcode
- Model: `stock.quant`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 8
- Sample fields: `available_quantity`, `id`, `location_id`, `lot_id`, `owner_id`, `package_id`, `product_uom_id`, `quantity`
- XPath or positional patches: 0

### `stock_quant_barcode_kanban`
- Name: stock.barcode.quant.kanban
- Model: `stock.quant`
- Type: inferred from arch
- Root tag: `kanban`
- Field references: 4
- Sample fields: `lot_id`, `product_id`, `product_uom_id`, `quantity`
- XPath or positional patches: 0

### `stock_move_line_product_selector`
- Name: stock.product.selector
- Model: `stock.move.line`
- Type: inferred from arch
- Root tag: `form`
- Field references: 26
- Sample fields: `company_id`, `formatted_product_barcode`, `id`, `image_1920`, `location_dest_id`, `location_id`, `lot_id`, `lot_name`, `lot_properties`, `move_id`, and 16 more
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode/Views]]

<!-- GENERATED:VIEWFILE -->
