<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/stock_barcode_views.xml

- Module: [[docs/Enterprise Addons/stock_barcode/stock_barcode|stock_barcode]]
- Scope: Enterprise Addons
- Source file: `views/stock_barcode_views.xml`
- Views: 1
- Actions: 3
- Menus: 1
- Rules: 0

## View records

### `product_view_list_barcodes`
- Name: product.list.barcodes
- Model: `product.product`
- Type: inferred from arch
- Root tag: `list`
- Field references: 4
- Sample fields: `barcode`, `code`, `company_id`, `name`
- XPath or positional patches: 0

## Actions

- `product_action_barcodes`: `act_window` Product Barcodes
- `stock_picking_action_kanban`: `act_window` Operations
- `stock_barcode_action_main_menu`: `client` Barcode

## Menus

- `stock_barcode_menu`: unnamed

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode/Views]]

<!-- GENERATED:VIEWFILE -->
