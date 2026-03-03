---
tags: [odoo, enterprise, generated, views]
---

# views/pos_order_views.xml

- Module: [[docs/Enterprise Addons/l10n_br_edi_pos/l10n_br_edi_pos|l10n_br_edi_pos]]
- Scope: Enterprise Addons
- Source file: `views/pos_order_views.xml`
- Views: 2
- Actions: 2
- Menus: 0
- Rules: 0

## View records

### `view_pos_pos_form`
- Name: pos.order.form
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_pos_form`
- Root tag: `header`
- Field references: 7
- Sample fields: `l10n_br_access_key`, `l10n_br_avatax_error`, `l10n_br_edi_authorization_date`, `l10n_br_edi_number`, `l10n_br_edi_protocol_authorization_number`, `l10n_br_edi_series`, `l10n_br_last_avatax_status`
- Buttons: `action_pos_order_invoice`, `button_l10n_br_edi`
- XPath or positional patches: 3

### `view_pos_order_tree`
- Name: unnamed
- Model: `pos.order`
- Type: inferred from arch
- Inherits: `point_of_sale.view_pos_order_tree`
- Root tag: `field`
- Field references: 2
- Sample fields: `l10n_br_last_avatax_status`, `state`
- XPath or positional patches: 0

## Actions

- `action_download_pos_order_xml`: `server` Download NFC-e XML
- `model_pos_order_send_nfce`: `server` Send NFC-e

## Navigation

- **Parent:** [[docs/Enterprise Addons/l10n_br_edi_pos/Views]]

