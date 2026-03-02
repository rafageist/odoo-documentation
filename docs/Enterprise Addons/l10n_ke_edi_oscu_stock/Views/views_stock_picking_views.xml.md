<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/l10n_ke_edi_oscu_stock|l10n_ke_edi_oscu_stock]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `stock_picking_tree_inherit_l10n_ke_edi_stock_special`
- Name: stock.picking.list.inherit.l10n.ke.edi.oscu.stock
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.vpicktree`
- Root tag: `field`
- Field references: 3
- Sample fields: `default_order`, `l10n_ke_state`, `origin`
- XPath or positional patches: 1

### `stock_picking_tree_inherit_l10n_ke_edi_stock`
- Name: stock.picking.list.inherit.l10n.ke.edi.oscu.stock
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.vpicktree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_ke_state`, `origin`
- XPath or positional patches: 0

### `stock_picking_form_inherit_l10n_ke_edi_stock`
- Name: stock.picking.form.inherit.l10n.ke.edi.oscu.stock
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `l10n_ke_error_msg`, `l10n_ke_oscu_flow_type_code`, `l10n_ke_oscu_sar_number`, `l10n_ke_state`, `l10n_ke_validation_msg`, `origin`, `partner_id`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/Views]]

<!-- GENERATED:VIEWFILE -->
