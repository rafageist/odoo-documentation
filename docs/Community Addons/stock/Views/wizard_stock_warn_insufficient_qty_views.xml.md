<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# wizard/stock_warn_insufficient_qty_views.xml

- Module: [[docs/Community Addons/stock/stock|stock]]
- Scope: Community Addons
- Source file: `wizard/stock_warn_insufficient_qty_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `stock_warn_insufficient_qty_scrap_form_view`
- Name: stock.warn.insufficient.qty.scrap
- Model: `stock.warn.insufficient.qty.scrap`
- Type: inferred from arch
- Inherits: `stock.stock_warn_insufficient_qty_form_view`
- Root tag: `xpath`
- Field references: 3
- Sample fields: `location_id`, `product_uom_name`, `quantity`
- Buttons: `action_cancel`
- XPath or positional patches: 2

### `stock_warn_insufficient_qty_form_view`
- Name: stock.warn.insufficient.qty
- Model: `stock.warn.insufficient.qty`
- Type: inferred from arch
- Root tag: `form`
- Field references: 5
- Sample fields: `location_id`, `lot_id`, `product_id`, `quant_ids`, `quantity`
- Buttons: `action_done`, `cancel_button`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/stock/Views]]

<!-- GENERATED:VIEWFILE -->
