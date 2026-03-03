---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_views.xml

- Module: [[docs/Enterprise Addons/l10n_pe_edi_stock/l10n_pe_edi_stock|l10n_pe_edi_stock]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_views.xml`
- Views: 1
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_picking_edi_form`
- Name: stock.picking.edi.form
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `xpath`
- Field references: 12
- Sample fields: `l10n_latam_document_number`, `l10n_pe_edi_departure_start_date`, `l10n_pe_edi_document_number`, `l10n_pe_edi_error`, `l10n_pe_edi_observation`, `l10n_pe_edi_operator_id`, `l10n_pe_edi_reason_for_transfer`, `l10n_pe_edi_related_document_type`, `l10n_pe_edi_status`, `l10n_pe_edi_ticket_number`, and 2 more
- Buttons: `action_send_delivery_guide`, `l10n_pe_edi_action_download`
- XPath or positional patches: 4

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_pe_edi_stock/Views]]

