<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/stock_scrap_views.xml

- Module: [[docs/Enterprise Addons/stock_barcode/stock_barcode|stock_barcode]]
- Scope: Enterprise Addons
- Source file: `views/stock_scrap_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `scrap_product_selector`
- Name: scrap.product.selector
- Model: `stock.scrap`
- Type: inferred from arch
- Root tag: `form`
- Field references: 10
- Sample fields: `company_id`, `location_id`, `lot_id`, `product_id`, `product_uom_id`, `scrap_location_id`, `scrap_qty`, `should_replenish`, `state`, `tracking`
- Buttons: `action_validate`
- XPath or positional patches: 0

### `stock_scrap_inherit_mrp_barcode`
- Name: stock.scrap.form.inherit.barcode
- Model: `stock.scrap`
- Type: inferred from arch
- Inherits: `stock.stock_scrap_form_view`
- Root tag: `form`
- Field references: 1
- Sample fields: `_barcode_scanned`
- XPath or positional patches: 1

### `stock_scrap_wizard_inherit_mrp_barcode`
- Name: stock.scrap.form.inherit.barcode
- Model: `stock.scrap`
- Type: inferred from arch
- Inherits: `stock.stock_scrap_form_view2`
- Root tag: `form`
- Field references: 1
- Sample fields: `_barcode_scanned`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/stock_barcode/Views]]

<!-- GENERATED:VIEWFILE -->
