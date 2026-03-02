<!-- GENERATED:VIEWFILE -->
---
tags: [odoo, enterprise, generated, views]
---

# views/stock_picking_view.xml

- Module: [[docs/Enterprise Addons/l10n_ec_edi_stock/l10n_ec_edi_stock|l10n_ec_edi_stock]]
- Scope: Enterprise Addons
- Source file: `views/stock_picking_view.xml`
- Views: 2
- Actions: 0
- Menus: 0
- Rules: 0

## View records

### `view_l10n_ec_edi_stock_view_picking_internal_search`
- Name: view_l10n_ec_edi_stock_view_picking_internal_search
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_internal_search`
- Root tag: `filter`
- Field references: 0
- XPath or positional patches: 1

### `view_l10n_ec_edi_stock_picking_form`
- Name: view_l10n_ec_edi_stock_picking_form
- Model: `stock.picking`
- Type: inferred from arch
- Inherits: `stock.view_picking_form`
- Root tag: `field`
- Field references: 14
- Sample fields: `country_code`, `l10n_ec_allow_send_edi`, `l10n_ec_authorization_date`, `l10n_ec_authorization_number`, `l10n_ec_delivery_end_date`, `l10n_ec_delivery_guide_error`, `l10n_ec_delivery_start_date`, `l10n_ec_edi_document_number`, `l10n_ec_edi_status`, `l10n_ec_is_delivery_guide`, and 4 more
- Buttons: `button_action_cancel_delivery_guide`, `l10n_ec_action_create_delivery_guide`, `l10n_ec_action_download_delivery_guide`, `l10n_ec_send_delivery_guide_to_cancel`, `l10n_ec_send_delivery_guide_to_partner`, `l10n_ec_send_delivery_guide_to_send`
- XPath or positional patches: 3

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_ec_edi_stock/Views]]

<!-- GENERATED:VIEWFILE -->
