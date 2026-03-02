<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, community, generated, views]
---

# views/stock_picking_batch_views.xml

- Module: [[docs/Community Addons/l10n_ro_edi_stock_batch/l10n_ro_edi_stock_batch|l10n_ro_edi_stock_batch]]
- Scope: Community Addons
- Source file: `views/stock_picking_batch_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `l10n_ro_edi_stock_stock_picking_batch_filter`
- Name: unnamed
- Model: `stock.picking.batch`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_batch_filter`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_ro_edi_stock_state`, `user_id`
- XPath or positional patches: 2

### `l10n_ro_edi_stock_stock_picking_batch_view_tree`
- Name: unnamed
- Model: `stock.picking.batch`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_batch_tree`
- Root tag: `field`
- Field references: 3
- Sample fields: `company_id`, `l10n_ro_edi_stock_state`, `state`
- Buttons: `action_l10n_ro_edi_stock_fetch_status`
- XPath or positional patches: 0

### `l10n_ro_edi_stock_view_batch_form`
- Name: stock.picking.batch.form.inherit.l10n_ro_edi_stock
- Model: `stock.picking.batch`
- Type: inferred from arch
- Inherits: `stock_picking_batch.stock_picking_batch_form`
- Root tag: `xpath`
- Field references: 28
- Sample fields: `attachment`, `datetime`, `l10n_ro_edi_stock_available_end_loc_types`, `l10n_ro_edi_stock_available_operation_scopes`, `l10n_ro_edi_stock_available_start_loc_types`, `l10n_ro_edi_stock_document_ids`, `l10n_ro_edi_stock_enable`, `l10n_ro_edi_stock_enable_amend`, `l10n_ro_edi_stock_enable_fetch`, `l10n_ro_edi_stock_enable_send`, and 18 more
- Buttons: `action_l10n_ro_edi_stock_fetch_status`, `action_l10n_ro_edi_stock_send_etransport`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Community Addons/l10n_ro_edi_stock_batch/Views]]

<!-- GENERATED:VIEWFILE -->
