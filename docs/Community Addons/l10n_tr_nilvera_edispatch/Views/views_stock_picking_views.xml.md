---
tags: [odoo, community, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Community Addons/l10n_tr_nilvera_edispatch/l10n_tr_nilvera_edispatch|l10n_tr_nilvera_edispatch]]
- Scope: Community Addons
- Source file: `views/stock_picking_views.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_picking_form_inherit_l10n_tr_nilvera_edispatch`
- Name: view.picking.form.inherit.l10n.tr.nilvera.edispatch
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `xpath`
- Field references: 13
- Sample fields: `l10n_tr_nilvera_buyer_id`, `l10n_tr_nilvera_buyer_originator_id`, `l10n_tr_nilvera_carrier_id`, `l10n_tr_nilvera_delivery_date`, `l10n_tr_nilvera_delivery_notes`, `l10n_tr_nilvera_delivery_printed_number`, `l10n_tr_nilvera_dispatch_state`, `l10n_tr_nilvera_dispatch_type`, `l10n_tr_nilvera_driver_ids`, `l10n_tr_nilvera_edispatch_warnings`, and 3 more
- Buttons: `action_generate_l10n_tr_edispatch_xml`
- XPath or positional patches: 3

### `view_picking_internal_search_inherit_l10n_tr_nilvera_edispatch`
- Name: stock.picking.internal.search.inherit.l10n.tr.nilvera.edispatch
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_internal_search`
- Root tag: `xpath`
- Field references: 0
- XPath or positional patches: 1

## Actions

- `action_mark_l10n_tr_nilvera_edispatch_status`: `server` Mark as sent (GİB e-Dispatch)
- `action_export_l10n_tr_nilvera_edispatch_list`: `server` Generate GİB e-Dispatch (XML)

## Navigation

- **Parent:** [[docs/Community Addons/l10n_tr_nilvera_edispatch/Views]]

