<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Enterprise Addons/l10n_uy_edi_stock/l10n_uy_edi_stock|l10n_uy_edi_stock]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_views.xml`
- Views: 3
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_picking_edi_search`
- Name: stock.picking.edi.search
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_internal_search`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_latam_document_type_id`, `partner_id`
- XPath or positional patches: 1

### `view_picking_edi_tree`
- Name: stock.picking.edi.tree
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.vpicktree`
- Root tag: `field`
- Field references: 2
- Sample fields: `json_popover`, `l10n_uy_edi_cfe_state`
- XPath or positional patches: 0

### `view_picking_edi_form`
- Name: stock.picking.edi.form
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `xpath`
- Field references: 8
- Sample fields: `l10n_latam_document_type_id`, `l10n_uy_edi_addenda_ids`, `l10n_uy_edi_cfe_state`, `l10n_uy_edi_cfe_uuid`, `l10n_uy_edi_document_id`, `l10n_uy_edi_error`, `l10n_uy_edi_operation_type`, `l10n_uy_edi_reference`
- Buttons: `l10n_uy_edi_action_download_preview_xml`, `l10n_uy_edi_action_update_dgi_state`, `l10n_uy_edi_create_delivery_guide`
- XPath or positional patches: 5

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_uy_edi_stock/Views]]

<!-- GENERATED:VIEWFILE -->
