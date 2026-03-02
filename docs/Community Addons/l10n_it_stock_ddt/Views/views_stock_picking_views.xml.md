<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Community Addons/l10n_it_stock_ddt/l10n_it_stock_ddt|l10n_it_stock_ddt]]
- Scope: Community Addons
- Source file: `views/stock_picking_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_picking_tree_inherit_l10n_it_ddt`
- Name: stock.picking.list.l10n.it.ddt
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.vpicktree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_it_ddt_number`, `origin`
- XPath or positional patches: 0

### `view_picking_search_inherit_l10n_it_ddt`
- Name: stock.picking.search.l10n.it.ddt
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_internal_search`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_it_ddt_number`, `origin`
- XPath or positional patches: 0

### `view_picking_form_inherit_l10n_it_ddt`
- Name: stock.picking.form.l10n.it.ddt
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `xpath`
- Field references: 7
- Sample fields: `country_code`, `l10n_it_ddt_number`, `l10n_it_parcels`, `l10n_it_show_print_ddt_button`, `l10n_it_transport_method`, `l10n_it_transport_method_details`, `l10n_it_transport_reason`
- Buttons: `%(l10n_it_stock_ddt.action_report_ddt)d`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Community Addons/l10n_it_stock_ddt/Views]]

<!-- GENERATED:VIEWFILE -->
