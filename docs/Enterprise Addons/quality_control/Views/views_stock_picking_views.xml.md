<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Enterprise Addons/quality_control/quality_control|quality_control]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `stock_picking_view_search_inherit_quality`
- Name: stock.picking.view.search.inherit.quality
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_internal_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

### `stock_picking_view_tree_inherit_quality`
- Name: stock.picking.view.tree.inherit.quality
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.vpicktree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `quality_check_todo`
- XPath or positional patches: 1

### `stock_picking_view_form_inherit_quality`
- Name: stock.picking.view.form.inherit.quality
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `quality_alert_count`
- Buttons: `action_open_quality_check_picking`, `button_quality_alert`, `check_quality`, `open_quality_alert_picking`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Enterprise Addons/quality_control/Views]]

<!-- GENERATED:VIEWFILE -->
