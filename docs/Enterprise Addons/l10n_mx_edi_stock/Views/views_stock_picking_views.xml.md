---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Enterprise Addons/l10n_mx_edi_stock/l10n_mx_edi_stock|l10n_mx_edi_stock]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `stock_picking_form_inherit_l10n_mx_edi_stock`
- Name: stock.picking.form.inherit.l10n_mx_edi_stock
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `xpath`
- Field references: 33
- Sample fields: `attachment_id`, `datetime`, `l10n_mx_edi_cfdi_cancel_picking_id`, `l10n_mx_edi_cfdi_origin`, `l10n_mx_edi_cfdi_sat_state`, `l10n_mx_edi_cfdi_state`, `l10n_mx_edi_cfdi_uuid`, `l10n_mx_edi_customs_doc_identification`, `l10n_mx_edi_customs_document_type_code`, `l10n_mx_edi_customs_document_type_id`, and 23 more
- Buttons: `action_download_file`, `action_retry`, `l10n_mx_edi_action_calculate_distance`, `l10n_mx_edi_action_print_cartaporte`, `l10n_mx_edi_action_set_partner_coordinates`, `l10n_mx_edi_cfdi_try_cancel`, `l10n_mx_edi_cfdi_try_sat`, `l10n_mx_edi_cfdi_try_send`
- XPath or positional patches: 6

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_mx_edi_stock/Views]]

