---
tags: [odoo, enterprise, generated, views]
---

# views/stock_move_views.xml

- Module: [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/l10n_ke_edi_oscu_stock|l10n_ke_edi_oscu_stock]]
- Scope: Enterprise Addons
- Source file: `views/stock_move_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_ke_edi_oscu_view_move_form`
- Name: stock.move.form.inherit.l10n.ke.edi.oscu.stock
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `stock.view_move_form`
- Root tag: `header`
- Field references: 4
- Sample fields: `country_code`, `l10n_ke_oscu_flow_type_code`, `l10n_ke_oscu_sar_number`, `location_dest_id`
- Buttons: `action_l10n_ke_oscu_process_moves`
- XPath or positional patches: 1

### `l10n_ke_edi_oscu_view_move_tree`
- Name: stock.move.list.inherit.l10n.ke.edi.oscu.stock
- Model: `stock.move`
- Type: inferred from arch
- Inherits: `stock.view_move_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `l10n_ke_oscu_flow_type_code`, `l10n_ke_oscu_sar_number`, `state`
- XPath or positional patches: 0

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ke_edi_oscu_stock/Views]]

