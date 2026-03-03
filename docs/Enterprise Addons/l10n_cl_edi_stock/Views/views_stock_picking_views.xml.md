---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Enterprise Addons/l10n_cl_edi_stock/l10n_cl_edi_stock|l10n_cl_edi_stock]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_views.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_picking_edi_tree`
- Name: stock.picking.edi.list
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.vpicktree`
- Root tag: `field`
- Field references: 4
- Sample fields: `country_code`, `json_popover`, `l10n_cl_dte_status`, `l10n_latam_document_number`
- XPath or positional patches: 0

### `view_picking_edi_form`
- Name: stock.picking.edi.form
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `xpath`
- Field references: 16
- Sample fields: `date`, `l10n_cl_delivery_guide_reason`, `l10n_cl_draft_status`, `l10n_cl_dte_file`, `l10n_cl_dte_status`, `l10n_cl_is_return`, `l10n_cl_reference_doc_internal_type`, `l10n_cl_reference_doc_type_id`, `l10n_cl_reference_ids`, `l10n_cl_sii_send_file`, and 6 more
- Buttons: `create_delivery_guide`, `l10n_cl_confirm_draft_delivery_guide`, `l10n_cl_send_dte_to_sii`, `l10n_cl_set_delivery_guide_to_draft`, `l10n_cl_verify_dte_status`, `print_delivery_guide_pdf`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_cl_edi_stock/Views]]

