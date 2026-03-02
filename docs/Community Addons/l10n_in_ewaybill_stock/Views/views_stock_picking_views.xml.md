<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Community Addons/l10n_in_ewaybill_stock/l10n_in_ewaybill_stock|l10n_in_ewaybill_stock]]
- Scope: Community Addons
- Source file: `views/stock_picking_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_picking_list_inherit_ewaybill`
- Name: view.picking.list.inherit.ewaybill
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.vpicktree`
- Root tag: `xpath`
- Field references: 1
- Sample fields: `l10n_in_ewaybill_name`
- XPath or positional patches: 1

### `view_picking_form_inherit_ewaybill`
- Name: view.picking.form.inherit.ewaybill
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `xpath`
- Field references: 0
- Buttons: `action_l10n_in_ewaybill_create`, `action_open_l10n_in_ewaybill`
- XPath or positional patches: 2

## Navigation

- **Parent:** [[docs/Community Addons/l10n_in_ewaybill_stock/Views]]

<!-- GENERATED:VIEWFILE -->
