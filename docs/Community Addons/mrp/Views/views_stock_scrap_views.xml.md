---
tags: [odoo, community, generated, views]
---

# views/stock_scrap_views.xml

- Module: [[docs/Community Addons/mrp/mrp|mrp]]
- Scope: Community Addons
- Source file: `views/stock_scrap_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `stock_scrap_search_view_inherit_mrp`
- Name: stock.scrap.search.inherit.mrp
- Model: `stock.scrap`
- Type: inferred from arch
- Inherits: `stock.stock_scrap_search_view`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 2

### `stock_scrap_view_form_mrp_inherit_mrp`
- Name: stock.scrap.view.form.inherit.mrp
- Model: `stock.scrap`
- Type: inferred from arch
- Inherits: `stock.stock_scrap_form_view`
- Root tag: `field`
- Field references: 6
- Sample fields: `bom_id`, `owner_id`, `product_is_kit`, `product_template`, `production_id`, `workorder_id`
- XPath or positional patches: 0

### `stock_scrap_view_form2_mrp_inherit_mrp`
- Name: stock.scrap.view.form2.inherit.mrp
- Model: `stock.scrap`
- Type: inferred from arch
- Inherits: `stock.stock_scrap_form_view2`
- Root tag: `field`
- Field references: 6
- Sample fields: `bom_id`, `owner_id`, `product_is_kit`, `product_template`, `production_id`, `workorder_id`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Community Addons/mrp/Views]]

